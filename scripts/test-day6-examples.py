from pathlib import Path
from decimal import Decimal as D
from datetime import date
from pypdf import PdfReader
import json,re
R=Path(__file__).resolve().parents[1];A=json.loads((R/'docs/editorial/2026-11-12-day6/articles.json').read_text());assert len(A)==7
for a in A:
 s=(R/'journal'/a['slug']/'index.html').read_text();assert '2026-11-12' in s;assert '## 'not in s;assert (R/'images/journal'/f'{a["slug"]}-20261112.webp').stat().st_size>1000
assert 15+12-7==20 and 20*45-(20*(15+20)+4*25+60)==40 and D(40)/60*30-40==-20
assert 3000-700-100==2200 and 5000+2400-700-100+1000-500==7100 and 3000-2400==600
assert 90+60+30-(60+45+45)==30 and 200-(10*(6+8)+2*15+20)==10
assert 200*3+20==620
assert (30+2*25)*12==960 and (15+4*25)*12==1380 and (20+6*25)*12==2040
assert 3*20*12+15*12==900 and 900+6*30==1080 and 3*30*12==1080
assert D(340)/8==D('42.5') and 360/9==40 and D(190)/8==D('23.75') and round(D(220)/9,2)==D('24.44')
assert 50*20-40*20==200 and 800-300==500 and 960-(360+180+120)==300 and 300/(5*30-100)==6
assert (30-20)/(40-20)*100==50 and 180+240+60-420==60 and 350-(100+150+50)==50
assert (date(2026,10,13)-date(2026,9,14)).days+1==30 and (date(2026,11,12)-date(2026,10,14)).days+1==30
pdf=PdfReader(R/'downloads/strategic-plan-template.pdf');assert len(pdf.pages)==2;assert '50.0%'in pdf.pages[1].extract_text()
for a in json.loads((R/'docs/editorial/2026-11-12-day6/audits.json').read_text()):
 s=(R/'journal'/a['slug']/'index.html').read_text()
 if 'datePublished'in a:assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==a['datePublished']
print('PASS independent Day6 editorial arithmetic, matched measurement windows, assets, PDF and retained dates')
