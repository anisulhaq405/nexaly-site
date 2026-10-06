#!/usr/bin/env python3
"""Build an editorial change feed without changing storefront files."""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://nexalyplanner.com'
sys.path.insert(0, str(ROOT / 'scripts'))
spec = importlib.util.spec_from_file_location('nexaly_seo', ROOT / 'scripts/seo-build.py')
seo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seo)

def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()

def editorial(source):
    doc = seo.Document(source)
    elements = doc.find('article') or doc.find('main')
    if not elements:
        elements = doc.find('body')
    if not elements:
        raise ValueError('Missing editorial body')
    body = doc.inner(elements[0])
    for tag in ('script', 'style', 'header', 'footer', 'nav'):
        body = re.sub(fr'<{tag}\b.*?</{tag}>', '', body, flags=re.S)
    body = re.sub(r'(/assets/[^"\s?]+)\?[^"\s]*', r'\1', body)
    return re.sub(r'\s+', ' ', body).strip()

def content_hash(source):
    doc = seo.Document(source)
    h1 = doc.find('h1')
    if len(h1) != 1:
        raise ValueError('Expected one editorial heading')
    value = [seo.plain(doc.inner(h1[0])), doc.meta('description'), editorial(source)]
    return digest(json.dumps(value, ensure_ascii=False))

def build_feed():
    items = []
    for url in json.loads((ROOT / 'assets/seo-pages.json').read_text()):
        route = urlsplit(url).path
        if not re.fullmatch(r'/(journal|planners|guides)/[^/]+/', route):
            continue
        path = ROOT / route.lstrip('/') / 'index.html'
        source = path.read_text()
        doc = seo.Document(source)
        if 'noindex' in doc.meta('robots').lower() or doc.meta('nexaly:status') == 'draft':
            continue
        # Exclude product/category hubs; include only real product detail pages.
        if route.startswith('/planners/') and not doc.meta('product:price:amount') and 'buy.polar.sh/' not in source:
            continue
        image = doc.meta('og:image')
        image_path = ROOT / urlsplit(image).path.lstrip('/')
        if urlsplit(image).hostname not in ('nexalyplanner.com', 'www.nexalyplanner.com') or not image_path.is_file():
            raise ValueError(f'Missing local editorial image: {route}')
        title = seo.plain(doc.inner(doc.find('h1')[0]))
        description = doc.meta('description')
        content = content_hash(source)
        revision = digest(content + digest(image_path.read_bytes()))
        items.append(dict(url=url, title=title, description=description,
                          imageSource=image, imagePath=str(image_path.relative_to(ROOT)),
                          contentHash=content, revision=revision,
                          contentType=route.split('/')[1]))
    return dict(version=1, site=SITE, items=items,
                revision=digest(json.dumps(items, sort_keys=True, ensure_ascii=False)))

if __name__ == '__main__':
    print(json.dumps(build_feed(), indent=2, ensure_ascii=False))
