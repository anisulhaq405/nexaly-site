from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from PIL import Image
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT.parent/'day5-content-review'
pdfmetrics.registerFont(TTFont('Nexaly','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('NexalyBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
items=[('ASSETS',None),('Cash',6000),('Accounts receivable, net',2500),('Inventory',4000),('Equipment at cost',3500),('Less accumulated depreciation',-1000),('Other assets',0),('Total assets',15000),('LIABILITIES',None),('Accounts payable',2200),('Current debt portion',800),('Long-term debt, excluding current',3000),('Other liabilities',0),('Total liabilities',6000),('EQUITY',None),('Contributed capital',7500),('Retained earnings or deficit',2000),('Less owner withdrawals',-500),('Other equity, signed',0),('Total equity',9000),('Liabilities plus equity',15000),('Difference: assets minus funding',0)]
assert 6000+2500+4000+3500-1000==15000 and 2200+800+3000==6000 and 7500+2000-500==9000
c=canvas.Canvas(str(ROOT/'assets/downloads/small-business-balance-sheet-template.pdf'),pagesize=(612,792));c.setTitle('Small business balance sheet');c.setAuthor('NexalyPlanner')
for i,filled in enumerate([False,True],1):
 c.setFillColor(HexColor('#203d4a'));c.setFont('NexalyBold',20);c.drawString(42,746,'Small business balance sheet')
 c.setFont('Nexaly',10);c.drawString(42,723,'Fictional filled example' if filled else 'Blank printable worksheet')
 c.drawString(42,700,'Business: '+('Example Workshop' if filled else '________________________________'))
 c.drawString(42,681,'As of: '+('October 23, 2026' if filled else '________________')+'     Currency: '+('USD' if filled else '____________'))
 y=651
 for label,amount in items:
  if amount is None:
   c.setFillColor(HexColor('#e8eff3'));c.rect(42,y-5,528,20,fill=1,stroke=0);c.setFillColor(HexColor('#203d4a'));c.setFont('NexalyBold',10);c.drawString(48,y,label)
  else:
   total=label.startswith('Total') or label.startswith('Liabilities plus') or label.startswith('Difference')
   c.setFont('NexalyBold' if total else 'Nexaly',10);c.drawString(48,y,label)
   if filled:c.drawRightString(564,y,f'({abs(amount):,.2f})' if amount<0 else f'{amount:,.2f}')
   else:c.drawRightString(564,y,'________________')
   if total:c.setStrokeColor(HexColor('#b8c6ce'));c.line(42,y-5,570,y-5)
  y-=21
 c.setFont('NexalyBold',10);c.drawString(48,y,'Balance check');c.drawRightString(564,y,'Balanced' if filled else '________________');y-=25
 c.setFont('Nexaly',9);c.drawString(42,y,'Basis: '+('Simplified accrual example' if filled else '____________________________________________'))
 c.setFont('Nexaly',8);c.drawString(42,104,'Static writing form. The PDF does not calculate; use the workbook for formulas and input warnings.')
 c.drawString(42,88,'Example deduction lines show parentheses. Enter positive deductions in the corresponding workbook cells.')
 c.drawString(42,72,'A zero difference does not establish complete or correctly classified accounts. Keep source records.')
 c.drawString(42,43,'NexalyPlanner | Original fictional teaching figures | Definitions: SEC financial-statements guide.')
 c.drawRightString(570,28,f'{i} / 2');c.showPage()
c.save()
for f in ['balance-sheet-blank','balance-sheet-example']:
 im=Image.open(OUT/(f+'.png'));im.thumbnail((1100,1600));im.save(ROOT/'assets/img/resource-previews'/('small-business-'+f+'.webp'),quality=88)
print('Prepared two-page blank/example PDF and actual workbook previews.')
