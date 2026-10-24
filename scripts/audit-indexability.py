#!/usr/bin/env python3
"""Reproducible source/live eligibility checks for the 41 inspected discovered URLs.
Not a Google URL Inspection API client; it cannot confirm Google indexing.
"""
import argparse, concurrent.futures, datetime, json, re, sys, urllib.request, urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin,urlsplit
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'docs/audits/indexability-2026-10-24'
SITE='https://nexalyplanner.com'
class Page(HTMLParser):
 def __init__(self,source):
  super().__init__();self.canon=[];self.robots=[];self.links=[];self.h1=0;self.main=0;self.text=[];self.skip=0;self.body=False;self.body_text=[];self.feed(source)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='body':self.body=True
  if t=='main':self.main+=1
  if t in ('script','style'):self.skip+=1
  if t=='h1':self.h1+=1
  if t=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
  if t=='meta' and a.get('name','').lower() in ('robots','googlebot'):self.robots.append(a.get('content',''))
  if t=='a' and self.main and a.get('href'):self.links.append(a['href'])
 def handle_endtag(self,t):
  if t=='body':self.body=False
  if t=='main':self.main=max(0,self.main-1)
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if self.main and not self.skip:self.text.append(d)
  if self.body and not self.skip:self.body_text.append(d)
def request(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache'}),timeout=35) as r:return r.status,r.url,dict(r.headers),r.read()
def run(live=False, audit_dir=None):
 global AUDIT
 if audit_dir:
  AUDIT=ROOT/audit_dir
 targets=json.loads((AUDIT/'targets.json').read_text());reference=json.loads((AUDIT/'inspection-reference.json').read_text());indexed={x['url'] for x in reference if x['code']=='I'}
 incoming={};pages={}
 for f in ROOT.rglob('index.html'):
  if '.git' in f.parts:continue
  url=SITE+'/'+str(f.relative_to(ROOT)).removesuffix('index.html');p=Page(f.read_text());pages[url]=p
  for h in p.links:
   h=urljoin(url,h).split('#')[0]
   if h!=url:incoming.setdefault(h,set()).add(url)
 status,final,headers,body=request(SITE+'/robots.txt') if live else (200,SITE+'/robots.txt',{},(ROOT/'robots.txt').read_bytes())
 rp=urllib.robotparser.RobotFileParser();rp.parse(body.decode().splitlines());assert status==200
 status,final,headers,body=request(SITE+'/sitemap.xml') if live else (200,SITE+'/sitemap.xml',{},(ROOT/'sitemap.xml').read_bytes())
 assert status==200;sitemap={x.text for x in ET.fromstring(body).findall('{*}url/{*}loc')}
 def check(t):
  u=t['url'];p=pages[u];d={'url':u,'in_sitemap':u in sitemap,'robots_allowed':rp.can_fetch('Googlebot',u),'self_canonical':p.canon==[u],'one_h1':p.h1==1,'no_noindex':not any(re.search(r'\b(noindex|none)\b',x,re.I) for x in p.robots),'main_content_present':bool(' '.join(p.text or p.body_text).strip()),'incoming_sources':sorted(incoming.get(u,set())),'inspected_indexed_sources':sorted(incoming.get(u,set())&indexed)}
  d['source_eligible']=all(d[k] for k in ['in_sitemap','robots_allowed','self_canonical','one_h1','no_noindex','main_content_present']) and bool(d['incoming_sources']) and bool(d['inspected_indexed_sources'])
  if live:
   try:
    status,final,headers,b=request(u);q=Page(b.decode());xrobots=' '.join(v for k,v in headers.items() if k.lower()=='x-robots-tag')
    d.update(http=status,final_url=final,live_canonical=q.canon,live_robots=q.robots,x_robots=xrobots,source_match=b==(ROOT/urlsplit(u).path.strip('/')/'index.html').read_bytes())
    d['live_eligible']=status==200 and final==u and q.canon==[u] and not any(re.search(r'\b(noindex|none)\b',x,re.I) for x in q.robots+[xrobots]) and q.h1==1 and bool(' '.join(q.text or q.body_text).strip())
   except Exception as e:d.update(error=str(e),live_eligible=False,source_match=False)
  return d
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(check,targets))
 changes=json.loads((AUDIT/'changes.json').read_text());added=[]
 for x in changes['contextual_links']:
  src=SITE+x['source'];target=SITE+x['target'];d={'source':src,'target':target,'source_inspected_indexed':src in indexed,'present_in_main':target in {urljoin(src,h).split('#')[0] for h in pages[src].links}}
  if live:
   try:
    status,final,h,b=request(src);p=Page(b.decode());d['live_present']=status==200 and target in {urljoin(src,h).split('#')[0] for h in p.links}
   except Exception as e:d.update(live_present=False,error=str(e))
  added.append(d)
 passed=all(x['source_eligible'] and (not live or (x['live_eligible'] and x['source_match'])) for x in rows) and all(x['source_inspected_indexed'] and x['present_in_main'] and (not live or x['live_present']) for x in added)
 result={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'live' if live else 'source','passed':passed,'targets':len(rows),'added_links':len(added),'note':'Indexed source status is the saved 24 October inspection, not a new Google status check. Eligibility does not guarantee indexing.','rows':rows,'link_checks':added}
 path=AUDIT/('live-verification.json' if live else 'source-verification.json');path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['rows','link_checks']}));return 0 if passed else 1
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--live',action='store_true');ap.add_argument('--audit-dir');args=ap.parse_args();sys.exit(run(args.live,args.audit_dir))
