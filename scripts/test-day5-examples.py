from decimal import Decimal as D
from pathlib import Path
import json,re
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];A=json.loads((R/'docs/editorial/2026-11-11-day5/articles.json').read_text());assert len(A)==8
for a in A:
 s=(R/'journal'/a['slug']/'index.html').read_text();assert '2026-11-11' in s;assert 'Frequently asked questions' in s;assert (R/'images/journal'/f'{a["slug"]}-20261111.webp').stat().st_size>1000
assert 800-(180+80+60)==480 and 8*25-50==150 and 300/150==2
assert D(30)/500-D(20)/500==D('.02') and 10*40-250==150
assert 960-(360+120+120)==360 and 540/(6*30-90)==6 and 3*30-90==0
assert D(32)/100==D('.32') and D(8)/40==D('.2') and 1000-(68*10+80)==240
assert 300-20-10==270 and 270-6==264 and D(33)/264==D('.125')
assert 50*24-900==300 and 900//24==37 and 900//21==42 and 5*2000*D('.4')==4000
assert 70+20+6+4==100 and 500+20==520
assert 8*500-8*150-1400==1400 and 1400/(500-150)==4 and 40//6==6 and 3000-1800-1400-1200+2000==600
assert 150+90-210==30
assert 'day5-assignment-capacity' in (R/'journal/college-assignment-tracker/index.html').read_text()
pdf=PdfReader(R/'downloads/business-proposal-template.pdf');assert len(pdf.pages)==2 and '1,400' in pdf.pages[1].extract_text()
print('PASS independent Day5 arithmetic, assets and two-page proposal PDF')
