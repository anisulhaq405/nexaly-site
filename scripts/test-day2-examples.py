from decimal import Decimal as D
from pathlib import Path
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
# Independent arithmetic across seven article examples.
assert 84+6+10+20==120 and 336+24+40+80==480
assert 840-336-64-75-35-60-21==249
assert 1200-480-170+840-21==1369
assert D(650)/D('9.75')<67 and D(650)/D('9.75')>66
assert 600-240-64-170-15==111 and 1200-480-170+600-15==1135
assert 160-32-16-8==104 and 12*6+4*5==92 and 92+3*5==107
assert 12*450+4*250==6400 and 6400-1300==5100
assert 1800+6400-5000==3200 and 4500+5000-1300-3200==5000
assert 18+72-4-70==16 and 63/70==.9 and round(61/70*100,2)==87.14
assert 84*22+700+252==2800 and 80-12==68 and 24+48-68==4
assert 40-8-4-2-4==22 and D(22)/D('1.1')==20
assert 20*85-80*16-120-80-180==40
assert 3000+1360-1660==2700 and 17*85-1580-68==-203
assert 20-4-3==13 and 4+3+6==13
assert 2*1000*D('.2')+3*1500*D('.5')+2000*D('.7')==4050
assert 240-40==200 and round(200/6,2)==33.33 and 3*6-12==6
assert 40*25-40*12==520 and 1000-1200==-200 and 60*12==720
for n,count in [('business-plan-template',3),('business-startup-checklist',2)]:
 reader=PdfReader(R/'downloads'/f'{n}.pdf');assert len(reader.pages)==count
 assert not reader.get_fields()
 for page in reader.pages:assert tuple(page.mediabox)[2:]==(612,792);assert len(page.extract_text())>300
print('PASS Day2 journal reconciliations and 5 static Letter PDF pages; rendered pages visually reviewed separately.')
