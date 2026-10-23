from pathlib import Path
import json,re,html,subprocess,sys,hashlib,urllib.request,concurrent.futures,datetime
from urllib.parse import urlsplit,unquote
from importlib.machinery import SourceFileLoader
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT.parent/'day6-content-review';OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'scripts'));D=SourceFileLoader('day6seo',str(ROOT/'scripts/seo-build.py')).load_module().Document
pages=[];resources=[]
for n in [2,3,4,5]:
 a=json.loads((ROOT.parent/f'day{n}-content-review/content-register.json').read_text());a=a['pages'] if isinstance(a,dict) else a
 for x in a[:6]:pages.append({'path':x['path'],'day':n,'status':'Earlier published resource reviewed; no new draft change','decision':x.get('keyword_ownership') or x.get('change') or '; '.join(x.get('notes',[]))})
 resources.append({'path':a[-1]['path'],'day':n})
new=[('journal/rental-equipment-maintenance-log/index.html','fleet maintenance spreadsheet','Retain equipment-rental scope; broad vehicle-fleet query held.','Service source/trigger, forecast 18-hour booking and release evidence.'),('tools/document-renewal-calendar/index.html','contract tracker','Retain document renewal owner; full contract management intent held.','Due-date boundaries, in-progress status and verified replacement handoff.'),('tools/rental-booking-conflict-checker/index.html','rental tracking','Retain equipment booking owner; property rent-ledger intent excluded.','Three-way conflict, exact buffer boundary and UTC source conversion.'),('journal/agency-capacity-planning-example/index.html','resource planning template excel','HTML capacity example retained; exact Excel-template intent held because no workbook exists.','Contractor review effort and honest format/scope.'),('journal/purchase-order-tracker/index.html','purchase order tracking','Retain PO quantity-tracking owner, separate from PO form and payments.','Snapshot reconciliation; duplicate receipt; accepted/due wording and explicit target48 correction.')]
for p,k,d,c in new:pages.append({'path':p,'day':6,'candidate_keyword':k,'status':'Draft updated; not published','decision':d,'change':c})
assert len(pages)==len({x['path'] for x in pages})==29
downloadfiles=set();imagefiles=set();checks=[]
for row in pages+resources:
 p=ROOT/row['path'];s=p.read_text();d=D(s);ids=[e['attrs']['id'] for e in d.elements if 'id' in e['attrs']];assert len(ids)==len(set(ids)),p
 assert len(d.find('h1'))==1,p
 route='/'+row['path'][:-10];assert d.meta('robots')!='noindex,follow'
 assert f'<link rel="canonical" href="https://nexalyplanner.com{route}">' in s
 assert 'https://nexalyplanner.com'+route in (ROOT/'sitemap.xml').read_text()
 for e in d.elements:
  for attr in ['href','src']:
   u=urlsplit(html.unescape(e['attrs'].get(attr,'')))
   if u.scheme or u.netloc:continue
   if u.path:
    f=ROOT/unquote(u.path).lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)
    if f.is_dir():f=f/'index.html'
    assert f.exists(),(p,u.path)
    if '/assets/downloads/' in u.path:downloadfiles.add(str(f.relative_to(ROOT)))
    if e['tag']=='img':imagefiles.add(str(f.relative_to(ROOT)))
   elif u.fragment:assert unquote(u.fragment) in ids,(p,u.fragment)
 row.update(title=html.unescape(re.search(r"<title>(.*?)</title>",s,re.S)[1]),reviewed='2026-10-23',release='draft only' if row.get('day')==6 else 'Earlier release; fresh Google inspection not performed')
 checks.append({'path':row['path'],'h1':1,'canonical':'pass','local_targets_and_anchors':'pass','sitemap':'pass','index_status':'Unverified; no new Google inspection'})
# Preserve all executable behavior and historic date metadata in this draft.
changed=[x[0] for x in new]+['journal/small-business-balance-sheet-template/index.html']
for p in changed:
 old=subprocess.check_output(['git','show','HEAD:'+p],cwd=ROOT,text=True);s=(ROOT/p).read_text()
 scripts=lambda z:[x for x in re.findall(r'<script\b[^>]*>.*?</script>',z,re.S) if 'application/ld+json' not in x]
 assert scripts(old)==scripts(s),p
 dates=lambda z:re.findall(r'<meta property="article:(?:published|modified)_time"[^>]*>',z)
 assert dates(old)==dates(s),p
 assert (ROOT/'assets/js/main.js').read_bytes()==subprocess.check_output(['git','show','HEAD:assets/js/main.js'],cwd=ROOT)
(OUT/'review-ledger.json').write_text(json.dumps(pages,indent=2));(OUT/'new-resource-ledger.json').write_text(json.dumps(resources,indent=2));(OUT/'static-checks.json').write_text(json.dumps(checks,indent=2))
(OUT/'xlsx-files.json').write_text(json.dumps(sorted(x for x in downloadfiles if x.endswith('.xlsx')),indent=2));(OUT/'resource-files.json').write_text(json.dumps(sorted(downloadfiles),indent=2))
# Compare the published baseline, not unpublished draft bytes, to live responses.
requests=[x['path'] for x in pages+resources]+sorted(downloadfiles|imagefiles)
def live(p):
 url='https://nexalyplanner.com/'+(p[:-10] if p.endswith('/index.html') else p)
 try:
  expected=subprocess.check_output(['git','show','HEAD:'+p],cwd=ROOT)
  with urllib.request.urlopen(url,timeout=35) as r:
   b=r.read();return {'path':p,'url':url,'http':r.status,'published_baseline_match':b==expected,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 except Exception as e:return {'path':p,'url':url,'error':str(e),'published_baseline_match':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:results=list(ex.map(live,requests))
(OUT/'live-baseline-checks.json').write_text(json.dumps({'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(results),'passed':sum(x.get('http')==200 and x['published_baseline_match'] for x in results),'results':results},indent=2))
print(json.dumps({'existing_reviews':len(pages),'first_wave_resources':len(resources),'download_files':len(downloadfiles),'images':len(imagefiles),'live_checks':len(results),'passed':sum(x.get('http')==200 and x['published_baseline_match'] for x in results)},indent=2))
