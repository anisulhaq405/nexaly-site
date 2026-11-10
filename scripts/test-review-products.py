#!/usr/bin/env python3
"""Match the paid catalog and test feedback HTTP behavior using synthetic data."""
import argparse
import json
import re
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    source = (ROOT / 'feedback/review-lib.php').read_text()
    registry = source.split('const NEXALY_PRODUCTS = [', 1)[1].split('];', 1)[0]
    slugs = re.findall(r"^\s*'([^']+)'\s*=>", registry, re.M)
    paid = {p.parent.name for p in (ROOT / 'planners').glob('*/index.html')
            if 'https://buy.polar.sh/' in p.read_text()}
    assert len(slugs) == len(set(slugs)), 'Duplicate review product'
    assert set(slugs) == paid, f'Registry mismatch: missing {paid-set(slugs)}, extra {set(slugs)-paid}'
    print(f'PASS feedback registry matches all {len(paid)} paid products', flush=True)
    if args.source_only:
        return
    assert shutil.which('php'), 'PHP is required for HTTP regression tests'
    with tempfile.TemporaryDirectory(prefix='nexaly-feedback-test-') as temp:
        root = Path(temp)
        shutil.copytree(ROOT / 'feedback', root / 'feedback')
        storage = root / 'private-feedback'
        storage.mkdir()
        product = 'agency-client-profitability-capacity-os'
        fixtures = [dict(id=str(i), type='review', status=status, publish_consent=consent,
                         rating=5, title='Example', name='Example reviewer',
                         message='Synthetic review', created_at='2026-11-10T00:00:00Z',
                         email='private@example.com', ip_hash='private')
                    for i, (status, consent) in enumerate([
                        ('approved', True), ('pending', True), ('approved', False)])]
        (storage / f'{product}-feedback.jsonl').write_text(
            ''.join(json.dumps(row)+'\n' for row in fixtures))
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            port = sock.getsockname()[1]
        server = subprocess.Popen(['php', '-S', f'127.0.0.1:{port}', '-t', temp],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            base = f'http://127.0.0.1:{port}/feedback/'
            for attempt in range(100):
                try:
                    with urllib.request.urlopen(base+'reviews.php?product='+product, timeout=1):
                        break
                except (OSError, urllib.error.URLError):
                    if server.poll() is not None:
                        raise RuntimeError('PHP test server stopped')
                    time.sleep(.05)
            for slug in sorted(paid):
                with urllib.request.urlopen(base+'reviews.php?product='+slug, timeout=3) as response:
                    data = json.load(response)
                    assert response.status == 200 and data['product'] == slug
                    assert response.headers['X-Robots-Tag'] == 'noindex'
                    assert response.headers['Cache-Control'] == 'no-store'
                    assert data['count'] == (1 if slug == product else 0)
                    if slug == product:
                        assert data['reviews'][0]['id'] == '0'
                        assert not {'email', 'ip_hash'} & data['reviews'][0].keys()
            for slug in ['unknown-product', '..%2Fprivate-feedback', '']:
                try:
                    urllib.request.urlopen(base+'reviews.php?product='+slug, timeout=3)
                except urllib.error.HTTPError as error:
                    assert error.code == 404 and json.load(error)['ok'] is False
                else:
                    raise AssertionError('Unknown product was accepted')
            print('PASS isolated HTTP: all products, noindex, consent/privacy, unknown-product 404')
        finally:
            server.terminate()
            server.wait(timeout=5)


if __name__ == '__main__':
    main()
