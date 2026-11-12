from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
R=Path(__file__).resolve().parents[3];c=canvas.Canvas(str(R/'downloads/strategic-plan-template.pdf'),pagesize=(612,792));c.setTitle('Strategic Plan Worksheet - Blank and Fictional Example');c.setAuthor('NexalyPlanner')
def header(n,sub):
 c.setFillColor(HexColor('#176c66'));c.rect(0,738,612,54,fill=1,stroke=0);c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',13);c.drawString(36,758,'NEXALYPLANNER / FREE WORKSHEET');c.setFillColor(HexColor('#203d4a'));c.setFont('Helvetica-Bold',22);c.drawString(36,696,'One-objective strategic plan');c.setFont('Helvetica',9);c.drawString(36,676,sub);c.setFont('Helvetica',8);c.drawString(36,24,f'nexalyplanner.com | US Letter | Static writing sheet, not fillable | {n} / 2')
def line(label,y,n=1):
 c.setFont('Helvetica-Bold',10);c.drawString(36,y,label);c.setStrokeColor(HexColor('#c3d4ce'))
 for i in range(n):c.line(36,y-20-i*22,576,y-20-i*22)
header(1,'Blank planning sheet. Keep outcome measurement separate from action completion.')
for y,t in [(642,'Plan: ____________________________  Owner: ________________________________'),(614,'Start: ______________  End: ______________  Review: ________________________')]:c.setFont('Helvetica',10);c.drawString(36,y,t)
line('One objective',580,2);line('Metric unit, definition, source and matched comparison periods',498,2)
c.setFont('Helvetica',10);c.drawString(36,415,'Baseline: __________  Target: __________  Current: __________');c.drawString(36,389,'Available plan minutes: __________  Allocated-plan budget USD: __________')
c.setFont('Helvetica-Bold',9)
for x,t in [(36,'Action / owner'),(300,'Due date'),(380,'Minutes'),(448,'USD'),(518,'Status')]:c.drawString(x,347,t)
for i in range(4):c.line(36,320-i*35,576,320-i*35)
c.setFont('Helvetica',9)
for y,t in [(174,'Metric progress = (current - baseline) / (target - baseline) x 100.'),(155,'Target must differ from baseline; lower targets mean a decrease is intended.'),(136,'Raw metric progress can be negative or above 100%; it is not task completion.'),(117,'All action minutes and allocations are planned totals, including completed actions.'),(98,'No scheduling-conflict detection, reminders, bank cash or automatic collection.'),(79,'Keep an editable same-tool JSON backup in the browser worksheet.')]:c.drawString(36,y,t)
c.showPage();header(2,'Fictional example only - invented observations and allocations, not business results.')
c.setFont('Helvetica',10)
for y,t in [(641,'Objective: improve qualified inquiries with a defined review workload.'),(615,'Owner: Example owner | Plan: Nov 12-Dec 11, 2026 | Review: Nov 12, 2026'),(589,'Metric: unique qualified inquiries under the same definition and source rule.'),(563,'Baseline window: Sep 14-Oct 13; current: Oct 14-Nov 12 (30 days each).'),(537,'Baseline 20 | Target 40 | Current 30 | Metric progress: 50.0%'),(511,'Remaining metric gap: 10 units. This is not a causal effect or forecast.')]:c.drawString(36,y,t)
rows=[('Offer review / owner','Nov 20','180','$100','done'),('Two variants / editor','Nov 27','240','$150','active'),('Outcome review / owner','Dec 04','60','$50','planned')]
c.setFont('Helvetica-Bold',9)
for x,t in [(36,'Action / owner'),(300,'Due date'),(380,'Minutes'),(448,'USD'),(518,'Status')]:c.drawString(x,467,t)
for i,row in enumerate(rows):
 c.setFont('Helvetica',9);y=437-i*35
 for x,t in zip([36,300,380,448,518],row):c.drawString(x,y,t)
 c.line(36,y-12,576,y-12)
c.setFont('Helvetica',10)
for y,t in [(304,'Planned effort: 480 minutes | Capacity: 420 | Capacity gap: 60 minutes'),(276,'Allocated cost: $300 | Budget: $350 | Budget headroom: $50'),(248,'Actions marked done: 1 of 3 (33.3%), separate from 50.0% metric progress.')]:c.drawString(36,y,t)
line('Next decision / evidence to verify',208,3);c.setFont('Helvetica',9);c.drawString(36,105,'Resolve the capacity gap; extra budget does not create additional time.');c.drawString(36,83,'The interactive worksheet supports CSV, editable JSON backup and browser print.');c.showPage();c.save()
