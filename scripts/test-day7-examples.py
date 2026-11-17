from pathlib import Path
from decimal import Decimal as D
from datetime import date
from pypdf import PdfReader
import json,re
R=Path(__file__).resolve().parents[1];A=json.loads((R/'docs/editorial/2026-11-17-day7/articles.json').read_text());assert len(A)==8
for a in A:
 s=(R/'journal'/a['slug']/'index.html').read_text();assert '2026-11-17' in s and '## 'not in s;assert (R/'images/journal'/f'{a["slug"]}-20261117.webp').stat().st_size>1000
 if a['slug'] not in ['kpi-dashboard-guide','hr-automation-guide']:assert 'href="/journal/kpi-dashboard-guide/"'in s
assert (date(2026,10,19)-date(2026,9,22)).days+1==28 and (date(2026,11,16)-date(2026,10,20)).days+1==28
assert D(120)/3000*100==4 and (D(120)-100)/100*100==20 and (D(3000)-2000)/2000*100==50
assert 600/20==30 and 600/5==120 and 1000-100-300-600==0
assert 4*1000+5*2000+3*3000==23000 and 4*1000*D('.2')+5*2000*D('.5')+3*3000*D('.8')==13000 and 6/(6+4)*100==60
assert round(D(91)/102*100,2)==D('89.22') and (D(90)+50)/2==70
assert 600+400+500+250==1750 and 2*(600+400)+500+250==2750
assert 54/72*100==75 and round(D(5)/6*100,2)==D('83.33') and 40*15-(40*(4+5)+6*20+60)==60 and D(60)/60*30-40==-10
assert 18000-6000-8000==4000 and 12000-3000-2000==7000 and 12000+4000-8000-5000==3000 and 132-120==12
pdf=PdfReader(R/'downloads/meal-planning-worksheet.pdf');assert len(pdf.pages)==2 and not pdf.get_fields();assert tuple(map(int,pdf.pages[0].mediabox[2:]))==(792,612);assert '350'in pdf.pages[1].extract_text()
for a in json.loads((R/'docs/editorial/2026-11-17-day7/audits.json').read_text()):
 s=(R/'journal'/a['slug']/'index.html').read_text();assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==a['datePublished']
 if a['id']!='O019':assert re.findall(r'"dateModified"\s*:\s*"([^"]+)"',s)==a['previousDateModified']
print('PASS Day7 independent arithmetic, reporting windows, cluster links, PDF and original audit dates')

# Public directory counts must match available cards before JavaScript runs.
s=(R/"tools/index.html").read_text();total=0
for section in re.findall(r'<section class="tool-category".*?</section>',s,re.S):
 n=len(re.findall(r'<article\b[^>]*\bclass="[^"]*\bdirectory-tool\b',section));total+=n;assert f'class="category-count">{n} planners'in section
assert f'<b>{total}</b> free planners'in s and total==61
print("PASS directory headline and category counts match actual resources")
