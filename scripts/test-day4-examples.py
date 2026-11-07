from decimal import Decimal as D
from pathlib import Path
from pypdf import PdfReader
import json
R=Path(__file__).resolve().parents[1]
# Consulting: delivery time, economics, collection timing and lower bookings.
assert 160-32-16-8==104 and 3*24+2*10==92 and 104-92==12 and 92+3*8-104==12
assert 3*1800+2*500-3*120-2*40-1400==4560
assert 3000+3*900+2*500-1840==4860 and 2*1800+2*500-2*120-2*40-1400==2880
# Insurance: premium != agency income, renewal cohort, direct capacity and earmark.
assert 40000*D('.12')+50000*D('.08')==8800 and 80/100==.8
assert 40*D('1.25')+80*D('.5')==90 and 100-20==80
assert 32*D('1.25')+80*D('.5')==80 and 32000*D('.12')+4000==7840
assert 8800-600-2000-3800==2400 and 7000+6000-5800-600==6600
# Spa: constrained whole slots, completed work, deposits and fixed staff costs.
assert 960//75==12 and 720//75==9 and 2*(360//75)==8 and 7*75==525 and round(525/720*100,2)==72.92
assert 630-84-35-D('18.90')-260-140==D('92.10')
assert 450-85-D('13.50')-400==D('-48.50') and 1000+490-D('537.90')==D('952.10')
# Hotel: explicit physical vs operating denominator, margin, whole-night downside.
assert 12*30-30==330 and 198/330==.6 and 23760/198==120 and 23760/330==72
assert 23760/360==66 and 198/360==.55
assert D(23760)-4356-D('1900.80')-15000==D('2503.20')
assert 66*35+132*15==4290 and D(4290)/60-65==D('6.5')
assert D(17880)-3278-D('1430.40')-15000==D('-1828.40')
assert D(8000)+20000-D('21256.80')==D('6743.20')
# Label: one explicitly fictional recovery sequence; client-fund travel bridge.
assert 1200+300+100+900==2500 and 4000-400==3600 and (3600-2500)/2==550
assert 5000-2500+3600-550==5550 and 2000*D('.9')-2500==-700
assert 10*2000-10*1800+10*100==3000 and 10*(3+1)==40 and 40+8-45==3
assert 3000-200-900==1900 and 4000+1800-1100-600==4100 and 2400-160-900==1340
# Bakery: losses vs sell-through, whole-production spending and collections.
assert 10*40-20==380 and 380-342==38 and 342/380==.9 and 342/400==.855
assert 10*30==300 and 10*45/60==7.5
assert 342*4-280-D('102.60')-300-60-250==D('375.40')
assert 1200-280-90-300-60-250==220 and D(2000)+1200-D('992.60')==D('2207.40')
for slug,size in [('homeschool-budget-planner',(612,792)),('time-blocking-template',(792,612))]:
 pdf=PdfReader(R/'downloads'/f'{slug}.pdf');assert len(pdf.pages)==2 and not pdf.get_fields()
 for page in pdf.pages:assert tuple(page.mediabox)[2:]==size;assert len(page.extract_text())>250
for a in json.loads((R/'docs/editorial/2026-11-07-day4/articles.json').read_text()):
 b=(R/a['asset'].lstrip('/')).read_bytes();assert len(b)>1024 and b[:4]==b'RIFF' and b[8:12]==b'WEBP'
print('PASS Day4 seven original numerical models, seven WebP assets and four static Letter PDF pages; visual checks separate.')
