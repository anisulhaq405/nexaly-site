from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
R=Path(__file__).resolve().parents[3];c=canvas.Canvas(str(R/'downloads/business-proposal-template.pdf'),pagesize=(612,792));c.setTitle('Business Proposal Template - Blank Scope and Pricing');c.setAuthor('NexalyPlanner')
def head(n,sub):
 c.setFillColor(HexColor('#176c66'));c.rect(0,738,612,54,fill=1,stroke=0);c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',13);c.drawString(36,758,'NEXALYPLANNER / FREE WORKSHEET');c.setFillColor(HexColor('#203d4a'));c.setFont('Helvetica-Bold',23);c.drawString(36,694,'Business proposal');c.setFont('Helvetica',9);c.drawString(36,674,sub);c.setFont('Helvetica',8);c.drawString(36,25,f'nexalyplanner.com | US Letter | Static writing template, not fillable | {n} / 2')
def lines(label,y,n):
 c.setFont('Helvetica-Bold',11);c.drawString(36,y,label);c.setStrokeColor(HexColor('#bdceca'))
 for i in range(n):c.line(36,y-22-i*24,576,y-22-i*24)
head(1,'Scope and delivery - confirm details with the client before relying on a final offer.')
c.setFont('Helvetica',10)
for y,t in [(640,'Title: ____________________________________________________________________'),(613,'Prepared by: ____________________  Prepared for: ___________________________'),(586,'Issue date: _____________________  Valid until: ______________________________')]:c.drawString(36,y,t)
lines('Client objective',550,3);lines('Deliverables, revision limit and acceptance criteria',438,4);lines('Excluded work',302,2);lines('Delivery / review timing and client dependencies',213,4);c.showPage();head(2,'Itemized USD pricing; no tax, discounts or currency conversion calculated.')
c.setFont('Helvetica-Bold',10)
for x,t in [(36,'Deliverable / price line'),(330,'Quantity'),(410,'Unit price $'),(510,'Line total $')]:c.drawString(x,631,t)
c.setStrokeColor(HexColor('#bdceca'))
for i in range(6):c.line(36,605-i*36,576,605-i*36)
c.setFont('Helvetica',10)
for y,t in [(375,'Total: $________________  Proposed deposit: ______% = $________________'),(347,'Remaining balance: $________________'),(319,'Line = whole quantity x unit price. Balance = total minus rounded deposit.')]:c.drawString(36,y,t)
lines('Payment due dates and change approval terms to confirm',277,4);c.setFont('Helvetica',9)
for y,t in [(128,'A draft is not evidence of client acceptance or payment.'),(110,'Confirm the agreement and applicable requirements for the actual work.'),(92,'The browser worksheet calculates prices and keeps editable JSON backups.'),(74,'Example: $300 + (6 x $150) + $200 = $1,400; 30% = $420; balance = $980.')]:c.drawString(36,y,t)
c.showPage();c.save()
