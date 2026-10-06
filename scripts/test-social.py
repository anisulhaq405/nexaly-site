#!/usr/bin/env python3
"""Exercise delivery reservations against a real disposable Git repository."""
import copy
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('publisher', ROOT / 'scripts/publish-social.py')
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)

class Response(io.BytesIO):
    status = 200

class DeliveryTests(unittest.TestCase):
    def test_hosting_recompression_and_changed_image(self):
        original = Image.new('RGB', (200, 100), (80, 110, 130))
        first, recompressed, changed = io.BytesIO(), io.BytesIO(), io.BytesIO()
        original.save(first, 'JPEG', quality=95)
        original.save(recompressed, 'JPEG', quality=85)
        Image.new('RGB', (200, 100), 'red').save(changed, 'JPEG')
        self.assertTrue(publisher.image_matches(recompressed.getvalue(), first.getvalue()))
        self.assertFalse(publisher.image_matches(changed.getvalue(), first.getvalue()))
        self.assertFalse(publisher.image_matches(b'<html>not an image</html>', first.getvalue()))
    def test_baseline_retry_and_ambiguous_timeout(self):
        with tempfile.TemporaryDirectory() as tmp:
            remote = Path(tmp) / 'remote.git'
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            original_run = subprocess.run
            item = copy.deepcopy(publisher.feed_module.build_feed()['items'][0])
            source = (ROOT / item['url'].split('nexalyplanner.com/')[1] / 'index.html').read_bytes()
            image = (ROOT / item['imagePath']).read_bytes()
            calls = []
            uncertain = False
            transport_failures = 1
            def local_git(args, **kwargs):
                nonlocal transport_failures
                if args[:4] == ['git', 'remote', 'add', 'origin']:
                    args = [*args[:4], str(remote)]
                if args[:2] == ['git', 'push'] and transport_failures:
                    transport_failures -= 1
                    return subprocess.CompletedProcess(args, 1, b'', b'transient transport failure')
                return original_run(args, **kwargs)
            def request(req, **kwargs):
                url = req.full_url if isinstance(req, publisher.urllib.request.Request) else req
                if url == 'https://test.invalid/webhook':
                    payload = json.loads(req.data)
                    calls.append(payload['kind'])
                    if uncertain and payload['kind'] == 'facebook':
                        raise TimeoutError('Delivery may already have published')
                    return Response(json.dumps({'postId': 'test-' + str(len(calls)), 'revision': payload['revision']}).encode())
                if url.startswith(item['url']):
                    return Response(source)
                return Response(image)
            env = {'MAKE_NEXALY_SOCIAL_WEBHOOK_URL': 'https://test.invalid/webhook',
                   'GITHUB_REPOSITORY': 'test/repo', 'SOCIAL_DESTINATIONS': 'facebook,instagram,pinterest',
                   'SOCIAL_TEST_URL': ''}
            with patch.dict(os.environ, env), patch.object(publisher.subprocess, 'run', side_effect=local_git), \
                 patch.object(publisher.urllib.request, 'urlopen', side_effect=request), \
                 patch.object(publisher.feed_module, 'build_feed', side_effect=lambda: {'items': [item]}), \
                 patch.object(publisher.time, 'sleep'):
                publisher.run()
                self.assertEqual(calls, [], 'Initial archive baseline must not publish')
                os.environ['SOCIAL_TEST_URL'] = item['url']
                publisher.run()
                self.assertEqual(calls, ['facebook', 'instagram', 'pinterest'])
                publisher.run()
                self.assertEqual(len(calls), 3, 'Repeat deployment must not duplicate')
                item['revision'] += '-changed'
                uncertain = True
                with self.assertRaisesRegex(RuntimeError, 'need review'):
                    publisher.run()
                self.assertEqual(calls[3:], ['facebook', 'instagram', 'pinterest'], 'One failure must not stop other destinations')
                with self.assertRaisesRegex(RuntimeError, 'need review'):
                    publisher.run()
                self.assertEqual(len(calls), 6, 'Ambiguous timeout must never retry automatically')
                state = json.loads(original_run(['git', '--git-dir', str(remote), 'show',
                                                 'social-publish-state:state.json'], text=True, capture_output=True, check=True).stdout)
                self.assertEqual(state['records'][item['url'] + '|facebook']['status'], 'needs_review')
                self.assertEqual(state['records'][item['url'] + '|instagram']['status'], 'published')

if __name__ == '__main__':
    unittest.main()
