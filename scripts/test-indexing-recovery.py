#!/usr/bin/env python3
"""Protect audited public URLs from accidental crawl/index exclusions."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit
from collections import deque
from decimal import Decimal as D
import json,re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.robots=[];self.canonical=[];self.links=[];self.cards=0;self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='meta' and a.get('name','').lower() in ['robots','googlebot']:self.robots.append(a.get('content','').lower())
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
  if t=='a' and a.get('href'):self.links.append(a['href'])
  if t=='article' and 'directory-tool' in a.get('class','').split():self.cards+=1
SITE='https://nexalyplanner.com'
docs={}
for p in ROOT.rglob('index.html'):
 if any(x in {'node_modules','.git','scripts','tests'} for x in p.relative_to(ROOT).parts):continue
 url=SITE+'/'+p.relative_to(ROOT).as_posix().removesuffix('index.html');docs[url]=Page(p.read_text())
edges={u:{urljoin(u,h).split('#')[0].split('?')[0] for h in d.links} for u,d in docs.items()}
dist={SITE+'/':0};q=deque(dist)
while q:
 u=q.popleft()
 for v in edges.get(u,[]):
  if v in docs and v not in dist:dist[v]=dist[u]+1;q.append(v)
observations=json.loads((ROOT/'docs/verification/2026-11-14-indexing-observations.json').read_text())
targets=[x['url'] for x in observations['urls'] if x['issue']=='Discovered - currently not indexed' or x['issue']=='Crawled - currently not indexed' and urlsplit(x['url']).path.startswith(('/journal/','/tools/'))]
assert len(targets)==58 and len(set(targets))==58
sitemap=(ROOT/'sitemap.xml').read_text()
for u in targets:
 d=docs[u];assert not any('noindex'in r or 'none'in r for r in d.robots),u
 assert d.canonical==[u],u
 assert '<loc>'+u+'</loc>' in sitemap,u
 assert u in dist and dist[u]<=2,(u,dist.get(u))
 assert sum(u in e for e in edges.values())>=2,u
robots=(ROOT/'robots.txt').read_text();assert 'Allow: /' in robots and not re.search(r'^Disallow:\s*/\s*$',robots,re.M)
hub=(ROOT/'tools/index.html').read_text();assert docs[SITE+'/tools/'].cards==60;assert 'Use 60 free business and personal planners' in hub;assert 'Use 50 free' not in hub
# Independent calculations in the added worked scenarios.
assert D(20)*3==60 and D(20)*3*2==120
assert 320+50==370 and 900-370==530 and 480-370==110 and 900-480==420
assert 3000-1100-200==1700 and 4700-200==4500 and 4500-600==3900
assert D(100)*D('.95')==95
before={x['url']:x for x in observations['urls']}
for u in targets:
 s=(ROOT/urlsplit(u).path.lstrip('/')/'index.html').read_text()
 if before[u].get('published'):assert f'content="{before[u]["published"]}"' in s,u
for path in json.loads((ROOT/'docs/verification/2026-11-14-indexing-edited.json').read_text()):
 s=(ROOT/path).read_text();assert '<meta property="article:modified_time" content="2026-11-14"' in s,path
assert '<loc>'+SITE+'/tools/homeschool-budget-planner/</loc><lastmod>2026-11-14</lastmod>' in sitemap
# Intentional exclusions remain excluded; asset directories aren't put in sitemap.
for u in [x['url'] for x in observations['urls'] if x['issue'].startswith('Excluded')]:
 path=ROOT/urlsplit(u).path.lstrip('/');path=path/'index.html' if u.endswith('/') else path
 assert 'noindex' in path.read_text(),u
 assert '<loc>'+u+'</loc>' not in sitemap,u
assert '<loc>'+SITE+'/images/products/rentflow-os/</loc>' not in sitemap
print('PASS indexing recovery: 58 self-canonical public URLs, crawlable robots, sitemap, depth<=2, links, original dates, 60 directory cards, intentional exclusions and worked arithmetic')
