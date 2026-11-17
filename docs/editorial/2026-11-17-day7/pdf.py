from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
R=Path(__file__).resolve().parents[3];p=R/'downloads/meal-planning-worksheet.pdf';c=canvas.Canvas(str(p),pagesize=(792,612));c.setTitle('Meal Planning Worksheet - Blank and Fictional Example');c.setAuthor('NexalyPlanner')
TEAL=HexColor('#176c66');INK=HexColor('#203d4a');LINE=HexColor('#c7d8d2')
def header(n,title,sub):
 c.setFillColor(TEAL);c.rect(0,560,792,52,fill=1,stroke=0);c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',12);c.drawString(32,581,'NEXALYPLANNER / FREE WEEKLY WORKSHEET');c.setFillColor(INK);c.setFont('Helvetica-Bold',22);c.drawString(32,526,title);c.setFont('Helvetica',10);c.drawString(32,507,sub);c.setFont('Helvetica',8);c.drawString(32,17,f'nexalyplanner.com | US Letter landscape | Static writing sheet, not fillable | {n} / 2')
def table(x,y,widths,heads,rows,height):
 c.setFillColor(HexColor('#e9f3ef'));c.rect(x,y-24,sum(widths),24,fill=1,stroke=0);c.setFillColor(INK);c.setFont('Helvetica-Bold',9);xx=x
 for w,t in zip(widths,heads):c.drawString(xx+7,y-16,t);xx+=w
 c.setFont('Helvetica',9)
 for i,row in enumerate(rows):
  yy=y-24-i*height;xx=x;c.setStrokeColor(LINE);c.line(x,yy-height,x+sum(widths),yy-height)
  for w,t in zip(widths,row):c.drawString(xx+7,yy-17,t);xx+=w
header(1,'Seven-day meal plan','Choose meals and enter grocery quantities separately. Changing servings does not scale ingredients.')
c.setFont('Helvetica',10);c.drawString(32,479,'Plan label: ___________________________________    First date: ____________________')
table(32,457,[92,212,212,212],['Day / date','Breakfast / servings / prep min','Lunch / servings / prep min','Dinner / servings / prep min'],[['Day '+str(i+1),'','','']for i in range(7)],35)
c.setFont('Helvetica-Bold',11);c.drawString(32,168,'Manual grocery check: additional to buy = max(0, needed - usable stock), in the same unit.')
table(32,152,[272,80,125,125,126],['Ingredient','Unit','Total needed','Usable stock','Additional to buy'],[['','','','','']for _ in range(3)],24)
c.setFont('Helvetica',8);c.drawString(32,39,'No automatic recipe scaling, unit conversion, nutrition/allergen check, food-safety validation or price estimate.')
c.showPage()
header(2,'Fictional example and quantity check','Example only. Three entered meals do not make a complete week or a nutritional recommendation.')
c.setFont('Helvetica',10);c.drawString(32,479,'Plan: Fictional weekly meal plan | First date: November 16, 2026 | Last date: November 22, 2026')
table(32,457,[112,108,292,100,116],['Date','Slot','Meal label','Servings','Prep minutes'],[['2026-11-16','Breakfast','Oats and fruit','4','10'],['2026-11-16','Lunch','Rice bowls','4','20'],['2026-11-16','Dinner','Vegetable pasta','4','30']],29)
c.setFont('Helvetica-Bold',11);c.drawString(32,319,'3 of 21 slots planned | 18 unplanned | 12 serving-occasions | 60 summed prep minutes')
c.setFont('Helvetica',9);c.drawString(32,300,'Serving-occasions are not unique people. Summed prep minutes are not an automatically scheduled kitchen calendar.')
table(32,276,[272,80,125,125,126],['Ingredient','Unit','Total needed','Usable stock','Additional to buy'],[['Rice','g','600','250','350'],['Tomatoes','g','800','900','0'],['Beans','each','2','1','1']],29)
c.setFont('Helvetica',10)
for y,t in [(142,'Two ingredient lines need additional quantities. Do not sum unlike units into one total.'),(122,'Ingredient lines are independent manual inputs, not a complete recipe list for the example meals.'),(102,'Convert units yourself. Keep each ingredient/unit need and stock on one line to avoid double counting.'),(82,'The browser worksheet exports reviewed CSV and same-tool editable JSON backups; it does not auto-save.'),(62,'Review recipes, usable stock, preferences and all real-world food requirements separately before using a list.')]:c.drawString(32,y,t)
c.save();print(p)
