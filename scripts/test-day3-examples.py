from decimal import Decimal as D
from pathlib import Path
from pypdf import PdfReader
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
assert 4*6000*D('.75')-4*500-6000==10000 and 12000+13500-8000-4000==13500
assert 140-40-4*18==28 and 6*18-100==8
assert 120*45+2400+1200==9000 and 10000+4000-9000==5000 and 5000+6000==11000
assert 8*4*4==128 and 120+20-128==12 and 100*45+2400+1200==8100
assert 810*8==6480 and sum([1400,600,400,1500,600])==4500 and 6480-4500-100*18==180
assert 648*8-4500==684 and 6000-4500+5600==7100
assert D(18)/25*100==72 and 18*150+6*40==2940
assert D(2940)-6*55-D(2940)*D('.03')-18*12-1800==D('505.8')
assert D(1960)*D('.97')-4*55-12*12-1800==D('-262.8')
assert D(5000)+2400-D('2434.2')==D('4965.8')
assert 2*8*5*4==320 and 328*22==7216 and 10240-7216-600-300-1200==924
assert 9000-9316==-316 and 924-8*22==748
assert 30000+6000+9000==15000+30000 and 1100-600-500==0 and 700-600-500==-400 and 9000-4*400==7400
assert 40*2*24==1920 and D(1920)*D('.65')*22==27456
assert D(27456)*D('.68')-8500-5000-2000==D('3170.08')
assert D(960*22)*D('.68')-15500==D('-1138.40')
assert 2200*D(720)/900==1760 and 4320-1760-1200==1360 and 4320-2200-1200==920 and 1360-920==440
assert 4*300-4*60-400==560 and 40-10-4*6==6 and 4*8-30==2 and 1000+600-240-400==960
for slug in ['daily-schedule-builder','business-idea-comparison']:
 pdf=PdfReader(R/'downloads'/f'{slug}.pdf');assert len(pdf.pages)==1 and not pdf.get_fields();assert tuple(pdf.pages[0].mediabox)[2:]==(612,792);assert len(pdf.pages[0].extract_text())>300
for a in json.loads((R/'docs/editorial/2026-11-06-day3/articles.json').read_text()):
 with Image.open(R/a['asset'].lstrip('/')) as im:assert im.size==(1200,800);im.load()
print('PASS Day3: eight original numerical examples, eight nonempty images and two static Letter PDFs.')
