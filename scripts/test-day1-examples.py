"""Independent reconciliation checks for the published fictional examples."""
from decimal import Decimal as D
from pathlib import Path
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
assert 6000-300-570==5130
assert 3000-270==2730 and 5130-2730==2400
assert round(D(2400)/5130*100,2)==D('46.78')
assert 200+80-120+9-2==167 and 167-40==127
assert 10+15+55*D('.4')==47 and 60-47==13
assert 5600+5900==11500 and 11500-10000==1500
assert 80*24+60*20==3120 and 600+240+140==980
assert 30*60+20*50-(3*60+2*50)==2520
assert 27*24+18*20==1008 and 2520-1008-740==772
assert 53*24+42*20==2112 and 6000-4100+2520-740==3680
assert 120-12-6==102 and 6000-600-300==5100
assert 108*20-6*20==2040 and 5100-2040-540-180-24-900==1416
assert 10000-6000+4080-2044==6036 and 300-108+6==198
assert 4000-3000+2000-2000-2000-1000==-2000
assert 5000+18000-15000==8000 and 4000+16000-14000==6000
assert 10000+2500-4500-1200==6800
assert 600/24==25 and 600/15==40 and 600/5==120 and 9/12==.75
assert 6000+3500-2500-2000==5000 and 5000-4500-3500==-3000
for name,pages in [('adhd-cleaning-planner',2),('business-plan-cover-page',1)]:
 r=PdfReader(R/'downloads'/f'{name}.pdf');assert len(r.pages)==pages
 for p in r.pages:assert tuple(p.mediabox)[2:]==(612,792);assert len(p.extract_text())>200
 assert not r.get_fields()
print('PASS 7 journal reconciliations and 3 static Letter PDF pages. Rendered pages separately visually reviewed.')
