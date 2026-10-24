from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.lib.utils import simpleSplit
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[3];configs=json.loads((root/'assets/js/business-forms-configs.json').read_text());qa=root/'docs/editorial/day7-three-forms/qa';pre=root/'assets/img/resource-previews'
for c in configs:
 out=root/'assets/downloads'/f"{c['slug']}.pdf";cv=canvas.Canvas(str(out),pagesize=(792,612));cv.setTitle(c['name']+' - blank and fictional example');cv.setAuthor('NexalyPlanner Editorial')
 for filled in [False,True]:
  col=HexColor(c['color']);cv.setFillColor(col);cv.rect(0,542,792,70,fill=1,stroke=0);cv.setFillColor(white);cv.setFont('Helvetica-Bold',22);cv.drawString(32,578,c['name']);cv.setFont('Helvetica',10);cv.drawString(32,557,'NEXALYPLANNER  |  '+('FILLED FICTIONAL EXAMPLE' if filled else 'BLANK PRINTABLE FORM')+'  |  USD example / one currency per form')
  s=c['sample'];y=519
  pairs=[('Reference','reference','Prepared by','person'),('Date','date','Needed by / period end','due'),('Business / department / customer','party','Currency','currency'),('Reviewer','reviewer','Manual review status','decision')]
  cv.setFillColor(HexColor('#243E48'))
  for a,k,b,j in pairs:
   cv.setFont('Helvetica-Bold',8);cv.drawString(32,y,a);cv.drawString(410,y,b);cv.setFont('Helvetica',9);cv.drawString(32,y-13,s[k] if filled else '_'*53);cv.drawString(410,y-13,s[j] if filled else '_'*49);y-=30
  cv.setFont('Helvetica-Bold',8);cv.drawString(32,y,'Purpose / delivery details');cv.setFont('Helvetica',8);cv.drawString(180,y,s['notes'][:115] if filled else '_'*110);y-=20
  widths=[65,95,124,63,64,70,70,177] if c['kind']=='expense' else [65,120,100,50,65,65,132,131]
  # Total available width is 728 points.
  widths=[v*728/sum(widths) for v in widths];x=32
  cv.setFillColor(col);cv.rect(32,y-30,728,30,fill=1,stroke=0);cv.setFillColor(white);cv.setFont('Helvetica-Bold',8)
  for h,w in zip(c['headers'],widths):
   for n,line in enumerate(simpleSplit(h,'Helvetica-Bold',8,w-8)[:2]):cv.drawString(x+4,y-12-n*9,line)
   x+=w
  y-=30;cv.setFont('Helvetica',8)
  for i,r in enumerate(s['rows']):
   cv.setFillColor(HexColor('#F2F6F5') if i%2==0 else white);cv.rect(32,y-22,728,22,fill=1,stroke=0);cv.setFillColor(HexColor('#243E48'));x=32
   values=list(r) if filled else ['']*8
   if filled and c['kind']!='expense' and values[3]:values[5]=f'{float(values[3])*float(values[4]):.2f}'
   for v,w in zip(values,widths):
    for n,line in enumerate(simpleSplit(str(v),'Helvetica',8,w-8)[:2]):cv.drawString(x+4,y-9-n*9,line)
    x+=w
   cv.setStrokeColor(HexColor('#CFDCDA'));cv.line(32,y-22,760,y-22);y-=22
  y-=14
  if c['kind']=='expense':totals=[('Recorded costs','228.00'),('Employee-paid eligible','178.00'),('Advance','60.00'),('Prior reimbursement','0.00'),('Net reimbursement','118.00')]
  elif c['kind']=='requisition':totals=[('Estimated shipping','10.00'),('Estimated tax','0.00'),('Estimated request','170.00'),('Available budget','160.00'),('Budget headroom','-10.00')]
  else:totals=[('Shipping','8.00'),('Entered tax','0.00'),('Discount','0.00'),('Order total','78.00'),('Paid to date','30.00'),('Balance remaining','48.00')]
  yy=y
  for label,value in totals:
   cv.setFont('Helvetica-Bold',9);cv.drawString(470,yy,label);cv.setFont('Helvetica',9);cv.drawRightString(756,yy,value if filled else '____________');yy-=14
  cv.setFont('Helvetica',8)
  left=['Review date: '+('Not reviewed' if filled else '________________________'),('Related / payment / PO ref: '+(s['related']or'Not issued')) if filled else 'Related / payment / PO ref: ________________________','Fixed entries; this PDF does not calculate or accept typed fields.','Manual review and supporting evidence are still required.']
  for i,t in enumerate(left):cv.drawString(32,y-i*14,t)
  cv.setStrokeColor(HexColor('#CFDCDA'));cv.line(32,34,760,34);cv.setFont('Helvetica',8);cv.drawString(32,20,'nexalyplanner.com/tools/'+c['slug']+'/');cv.drawRightString(760,20,('2 / 2' if filled else '1 / 2')+'  |  US Letter landscape');cv.showPage()
 cv.save()
print('Created three two-page PDFs')
# Exact worksheet previews and designed covers use the actual rendered spreadsheet.
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for c in configs:
 src=qa/(c['slug']+'-example.png')
 if not src.exists():continue
 im=Image.open(src).convert('RGB');im.save(pre/(c['slug']+'-worksheet.webp'),'WEBP',quality=90)
 cover=Image.new('RGB',(1200,800),'#F0F4F1');d=ImageDraw.Draw(cover);d.rectangle((0,0,1200,170),fill=c['color']);d.text((44,30),'NEXALYPLANNER  /  FREE EXCEL + PDF',font=ImageFont.truetype(font,17),fill='white');d.text((44,75),c['name'],font=ImageFont.truetype(font,42),fill='white');d.text((44,139),'Actual workbook excerpt · Fictional example',font=ImageFont.truetype(font,17),fill='white')
 im.thumbnail((1120,565));cover.paste(im,((1200-im.width)//2,190));cover.save(pre/(c['slug']+'-cover.webp'),'WEBP',quality=90)
print('Rendered actual workbook covers when workbook previews are available')
