from pathlib import Path
import json,re
from decimal import Decimal as N
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];D=R/'docs/editorial/2026-11-19-combined-day2'
A=json.loads((D/'articles.json').read_text());T=json.loads((D/'tools.json').read_text());scope=json.loads((D/'scope.json').read_text());assert len(scope)==15 and len({x['master_id']for x in scope})==15
assert 50*40-700-450-150==700 and 5*700-2000==1500
assert 3*(2000-800-450-150)-2000==-200
assert 1000+800-1300+1200==1700 and 1000-1300==-300
assert 9000+3000+2000+4000==18000 and 18000-10000==8000
assert 60*4*2000==480000 and 30*2000==60000 and N(60000)/480000==N('.125')
assert 4*2000-80*35-1800==3400 and 4*2000-112*35-1800==2280
assert 3000+6000-2800-1800==4400
assert 60*26*25==39000 and N('39000')*N('.66')-20000==5740
assert 45*26*24==28080 and N('28080')*N('.66')-20000==N('-1467.20')
assert (N(20000)/N('.66')/25).to_integral_value(rounding='ROUND_CEILING')==1213
assert 10000+37000-13000-12000-8000-3000==11000
for x in A+T:
 kind='tools'if x in T else'journal';s=(R/kind/x['slug']/'index.html').read_text();assert len(re.findall(r'<h1\b',s))==1
 asset='/images/journal/'+x['slug']+'-20261119.webp';assert s.count('src="'+asset+'"')==1 and 'https://nexalyplanner.com'+asset in s
 assert (R/asset.lstrip('/')).stat().st_size>10000
 for href in re.findall(r'href="([^"]+)"',s):
  if href.startswith('/')and not href.startswith('//'):
   path=href.split('#')[0].split('?')[0];p=R/path.lstrip('/');p=p/'index.html'if path.endswith('/')else p;assert p.exists(),(x['slug'],href)
 assert '2026-11-19'in s
 if x in T:
  pdf=PdfReader(R/'downloads'/f'{x["slug"]}.pdf');assert len(pdf.pages)==2
  txt=' '.join(p.extract_text()for p in pdf.pages);assert 'BLANK WRITING SHEET'in txt and 'ORIGINAL FICTIONAL EXAMPLE'in txt
  assert not pdf.get_fields()
  for id in ['bp-form','bp-sample','bp-result','bp-csv','bp-import','bp-dialog']:assert s.count('id="'+id+'"')==1
for a in json.loads((D/'audits.json').read_text()):
 s=(R/a['owner'].strip('/')/'index.html').read_text();assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==a['datePublished'];assert 'business-planning-day2'in s
s=(R/'tools/index.html').read_text();assert len(re.findall(r'<article\b[^>]*\bdirectory-tool\b',s))==67 and '<b>67</b>'in s
for t in T:
 cards=[c for c in re.findall(r'<article\b[^>]*\bdirectory-tool\b.*?</article>',s,re.S)if '/tools/'+t['slug']+'/'in c];assert len(cards)==1 and 'directory-preview'in cards[0]
for m in re.finditer(r'<section class="tool-category".*?</section>',s,re.S):
 p=m[0];n=len(re.findall(r'<article\b',p));assert f'data-visible-count="{n}"'in p and f'class="category-count">{n} planners'in p
print('PASS Day2 original arithmetic,15-owner scope,9 images, links,3 static PDFs, publication dates and67 image-complete directory cards.')
