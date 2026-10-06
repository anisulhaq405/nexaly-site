#!/usr/bin/env python3
"""Publish verified live changes, reserving each destination before delivery."""
import importlib.util
import json
import os
import subprocess
import tempfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('social_feed', ROOT / 'scripts/social-feed.py')
feed_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feed_module)
video_spec = importlib.util.spec_from_file_location('social_video', ROOT / 'scripts/social-video.py')
video_module = importlib.util.module_from_spec(video_spec)
video_spec.loader.exec_module(video_module)
BRANCH = 'social-publish-state'

def now():
    return datetime.now(timezone.utc).isoformat()

def run():
    webhook = os.environ.get('MAKE_NEXALY_SOCIAL_WEBHOOK_URL')
    if not webhook:
        print('Social delivery disabled: configure MAKE_NEXALY_SOCIAL_WEBHOOK_URL.')
        return
    destinations = os.environ.get('SOCIAL_DESTINATIONS', 'facebook,instagram,pinterest,youtube').split(',')
    if not set(destinations) <= {'facebook', 'instagram', 'pinterest', 'youtube'}:
        raise ValueError('Unsupported destination; configure it only after a successful publishing test.')
    feed = feed_module.build_feed()
    repository = os.environ['GITHUB_REPOSITORY']
    directory = Path(tempfile.mkdtemp(prefix='nexaly-social-'))
    def git(*args, required=True):
        result = subprocess.run(['git', *args], cwd=directory, text=True, capture_output=True)
        if required and result.returncode:
            # Do not echo command output containing credentials or private webhook data.
            raise RuntimeError('Git publication-state operation failed: ' + args[0])
        return result.stdout.strip()
    git('init')
    git('remote', 'add', 'origin', f'https://github.com/{repository}.git')
    header = subprocess.run(['git', 'config', '--get', 'http.https://github.com/.extraheader'],
                            cwd=ROOT, text=True, capture_output=True).stdout.strip()
    if header:
        git('config', 'http.https://github.com/.extraheader', header)
    git('config', 'user.name', 'NexalyPlanner Automation')
    git('config', 'user.email', 'automation@nexalyplanner.com')
    existing = git('ls-remote', '--heads', 'origin', BRANCH)
    if existing:
        git('fetch', '--depth=1', 'origin', BRANCH)
        git('checkout', '-B', BRANCH, 'FETCH_HEAD')
        state = json.loads((directory / 'state.json').read_text())
    else:
        git('checkout', '--orphan', BRANCH)
        state = {'version': 1, 'records': {}}
    def save(message):
        (directory / 'state.json').write_text(json.dumps(state, indent=2) + '\n')
        git('add', 'state.json', 'media', required=False)
        git('add', 'state.json')
        if not git('status', '--porcelain'):
            return
        git('commit', '-m', message)
        for attempt in range(3):
            result = subprocess.run(['git', 'push', 'origin', f'HEAD:refs/heads/{BRANCH}'],
                                    cwd=directory, capture_output=True)
            if result.returncode == 0:
                return
            # The workflow serializes all runs. Retry transport failures, and rebase
            # any independent remote changes; a conflict stops before another delivery.
            git('fetch', 'origin', BRANCH, required=False)
            remote = git('rev-parse', '--verify', 'FETCH_HEAD', required=False)
            if remote:
                git('rebase', 'FETCH_HEAD')
            time.sleep(2 * (attempt + 1))
        raise RuntimeError('Could not persist delivery reservation; no further posts sent.')
    test_url = os.environ.get('SOCIAL_TEST_URL', '')
    if test_url and test_url not in {item['url'] for item in feed['items']}:
        raise ValueError('Test URL must identify one existing editorial page')
    (directory / 'media').mkdir(exist_ok=True)
    if not existing:
        for item in feed['items']:
            for destination in destinations:
                if item['url'] != test_url:
                    state['records'][item['url'] + '|' + destination] = {
                        'revision': item['revision'], 'status': 'baseline'}
        save('Baseline existing editorial content without archive publishing')
    failures = []
    for item in feed['items']:
        if test_url and item['url'] != test_url:
            continue
        pending = []
        for destination in destinations:
            previous = state['records'].get(item['url'] + '|' + destination, {})
            if previous.get('status') in ('attempting', 'needs_review'):
                failures.append(item['url'] + '|' + destination)
            elif previous.get('revision') != item['revision'] or (test_url == item['url'] and previous.get('status') == 'baseline'):
                pending.append(destination)
        if not pending:
            continue
        live = False
        for attempt in range(12):
            try:
                req = urllib.request.Request(item['url'] + '?social_revision=' + item['revision'],
                                             headers={'Cache-Control': 'no-cache', 'User-Agent': 'NexalyPlanner-Live-Verification/1.0'})
                with urllib.request.urlopen(req, timeout=15) as response:
                    source = response.read().decode('utf-8')
                live = feed_module.content_hash(source) == item['contentHash']
                if live:
                    with urllib.request.urlopen(item['imageSource'], timeout=15) as response:
                        live = feed_module.digest(response.read()) == feed_module.digest((ROOT / item['imagePath']).read_bytes())
            except Exception:
                live = False
            if live:
                break
            time.sleep(15)
        if not live:
            failures.append(item['url'] + '|deployment-not-live')
            continue
        filename = item['revision'] + '.jpg'
        target = directory / 'media' / filename
        with Image.open(ROOT / item['imagePath']) as original:
            image = ImageOps.exif_transpose(original).convert('RGB')
            image = ImageOps.pad(image, (1200, 675), color='#f5f8f7')
            image.save(target, 'JPEG', quality=90, optimize=True)
        git('add', 'media/' + filename)
        if 'youtube' in pending:
            video_module.render_video(item, ROOT / item['imagePath'], directory / 'media' / (item['revision'] + '.mp4'))
            git('add', 'media/' + item['revision'] + '.mp4')
        save('Store immutable JPEG for confirmed live editorial content')
        media_url = f'https://raw.githubusercontent.com/{repository}/{BRANCH}/media/{filename}'
        for attempt in range(6):
            try:
                with urllib.request.urlopen(media_url, timeout=15) as response:
                    if response.status == 200:
                        break
            except Exception:
                if attempt == 5:
                    raise RuntimeError('Social JPEG is not publicly reachable; no delivery sent.')
                time.sleep(10)
        for destination in pending:
            key = item['url'] + '|' + destination
            state['records'][key] = {'revision': item['revision'], 'status': 'attempting', 'attemptedAt': now()}
            save('Reserve ' + destination + ' delivery')
            caption = item['title'] + '\n\n' + item['description']
            if destination == 'instagram':
                caption += '\n\nExplore the guide at NexalyPlanner.com — link in bio.\n#NexalyPlanner #DigitalPlanner #SmallBusinessTools'
            else:
                caption += '\n\nRead more: ' + item['url']
            destination_media = media_url.replace('.jpg', '.mp4') if destination == 'youtube' else media_url
            payload = dict(item, kind=destination, image=destination_media, caption=caption,
                           title=item['title'][:100], description=item['description'][:700])
            try:
                req = urllib.request.Request(webhook, data=json.dumps(payload).encode(),
                                             headers={'Content-Type': 'application/json'}, method='POST')
                with urllib.request.urlopen(req, timeout=120) as response:
                    result = json.load(response)
                if not result.get('postId') or result.get('revision') != item['revision']:
                    raise ValueError('Missing confirmed post ID')
            except Exception:
                state['records'][key]['status'] = 'needs_review'
                save('Flag uncertain ' + destination + ' delivery; never duplicate automatically')
                failures.append(key)
            else:
                state['records'][key] = {'revision': item['revision'], 'status': 'published',
                                         'postId': str(result['postId']), 'publishedAt': now()}
                save('Record ' + destination + ' publication')
                print('Published', destination, item['url'], result['postId'])
    if failures:
        raise RuntimeError('Some deliveries need review: ' + ', '.join(failures))
    print('Social publication state saved. No duplicate archive deliveries.')

if __name__ == '__main__':
    run()
