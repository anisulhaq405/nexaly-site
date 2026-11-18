from pathlib import Path
import re,json,html,runpy,textwrap
from PIL import Image,ImageDraw,ImageFont
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.properties import CalcProperties
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
D=Path(__file__).resolve().parent;R=D.parents[2];E=html.escape;tools=json.loads((D/'tools.json').read_text());A=runpy.run_path(str(D/'content.py'))['A']
base=(R/'docs/editorial/2026-11-12-day6/build.py').read_text().split('for a in A:page')[0];base=base.replace("A=runpy.run_path(str(D/'content.py'))['A'];",'').replace('2026-11-12','2026-11-18').replace('20261112','20261118').replace('November 12, 2026','November 18, 2026').replace('day6-strategy.js','finance-statements-20261118.js');exec(base,globals())
def visual(slug,title,labels,values,note):
 im=Image.new('RGB',(1200,800),'#f5f0e7');d=ImageDraw.Draw(im);font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';f=lambda n:ImageFont.truetype(font,n);d.rectangle((0,0,1200,16),fill='#176c66');d.text((65,50),'NEXALYPLANNER  /  ORIGINAL WORKED EXAMPLE',font=f(20),fill='#176c66');y=108
 for line in textwrap.wrap(title,35):d.text((60,y),line,font=f(43),fill='#173d38');y+=59
 y=max(y+35,285);maxv=max(abs(v) for v in values) or 1
 for lab,val in zip(labels,values):
  d.text((65,y),lab,font=f(25),fill='#173d38');bar=max(3,int(abs(val)/maxv*520));d.rounded_rectangle((470,y-1,470+bar,y+32),radius=6,fill='#b35832' if val<0 else '#176c66');d.text((1010,y),f'{val:,.0f}',font=f(24),fill='#173d38');y+=78
 for i,line in enumerate(textwrap.wrap(note,84)):d.text((65,710+i*27),line,font=f(19),fill='#4d625b')
 path=R/'images/journal'/f'{slug}-20261118.webp';im.save(path,'WEBP',quality=91);return path
spec={
'small-business-financial-statements':(['Net income','Operating cash','Net cash increase'],[3300,3500,3400],'Fictional USD workshop; different measures. Full reconciliation is in the guide.'),
'operating-cash-flow-example':(['Direct method','Indirect method','Delayed collection'],[3500,3500,2500],'Fictional USD example. A collection delay changes cash, not the stated sale.'),
'cost-of-goods-sold-example':(['Available stock cost','Closing inventory','COGS'],[11300,3100,8200],'Fictional USD reseller. COGS = 11,300 minus 3,100; not supplier cash paid.'),
'owner-draw-cash-planning':(['Day 5 before draw','Chosen cash floor','Day 5 after 2,500 draw'],[4500,4000,2000],'Fictional USD scenario. Ending headroom does not make an early draw safe.'),
'nonprofit-dashboard-example':(['Total cash','Restricted in model','After designation'],[80000,30000,40000],'Fictional USD balances. Restrictions and internal designations differ.'),
'laundromat-business-plan':(['Base after principal','Downside after principal','Fixed operating payments'],[3300,-300,6000],'Fictional monthly USD model. Excludes tax, interest, capex and owner pay.'),
'income-statement-template':(['Net sales','Gross profit','Net income'],[12000,6500,3300],'Original fictional USD example. Profit is not closing bank cash.'),
'cash-flow-statement-template':(['Operating cash','Investing cash','Financing cash'],[3500,-1000,900],'Original fictional USD example. Net movement = 3,400; closing = 13,400.'),
'startup-budget-template':(['Upfront cash uses','Operating shortfall','Retained reserve'],[14000,6000,4000],'Original fictional USD assumptions. Funding target is 24,000; funding gap 1,000.')}
for slug,(labs,vals,note) in spec.items():
 title=next((a['title'] for a in A if a['slug']==slug),next((x['title']for x in tools if x['slug']==slug),slug));visual(slug,title,labs,vals,note)
def normalize_image(path,slug):
 s=path.read_text();s=s.replace('— conceptual planning scene','— original worked-example comparison').replace('AI-generated editorial illustration. Screens and documents are conceptual; exact examples appear in the text.','Original NexalyPlanner chart of the fictional example. Amounts and scope are explained in the guide.').replace('Primary and provider sources inform brief definitions and boundaries. Examples and acceptance criteria are original. These are relevant references, not verified Google positions 1–3, hands-on vendor certification or guaranteed integrations.','References explain the definitions and reporting boundaries used here. Worked figures and decision examples are original.');path.write_text(s)
for a in A:
 page(a['slug'],a['title'],a['desc'],a['text'],sources=a['sources']);normalize_image(R/'journal'/a['slug']/'index.html',a['slug'])
def calc_expr(expr,refs):return re.sub(r'[A-Za-z]+',lambda m:refs[m[0]],expr)
for t in tools:
 slug=t['slug'];fields=''
 for k,label,val in t['fields']:
  fields+=f'<label for="fin-{k}">{E(label)}'+(' (USD, 0–1,000,000; up to 2 decimals)'if k!='months'else '')+f'</label><input id="fin-{k}" name="{k}" type="text" inputmode="'+('numeric'if k=='months'else'decimal')+'" maxlength="12" required>'
 content=f'''<div class="fin-controls"><p><a href="#fin-form">Use the free worksheet</a> · <a href="/downloads/{slug}.xlsx" download>Download Excel blank + example</a> · <a href="/downloads/{slug}.pdf" download>Download static blank + example PDF</a></p><p>{E(t['scope'])}</p><noscript><p>Browser calculations need JavaScript. Use the Excel download or static writing PDF if JavaScript is unavailable.</p></noscript><h2>Enter the record and period</h2><p>Enter every field, including intentional zeros. USD only; no currency conversion. Dates label the historical period, or the preparation window for the startup assumptions. The startup model’s separate month count controls its trading horizon.</p><form id="fin-form"><label for="fin-name">Business / scenario name (max 100 characters)</label><input id="fin-name" name="name" maxlength="100" required><div class="fin-grid"><div><label for="fin-start">Start date / preparation-window start</label><input id="fin-start" type="date" min="1900-01-01" max="2200-12-31" required></div><div><label for="fin-end">End date / preparation-window end</label><input id="fin-end" type="date" min="1900-01-01" max="2200-12-31" required></div></div><label for="fin-basis">Accounting basis / model assumptions and source references (max 500 characters)</label><textarea id="fin-basis" maxlength="500" required></textarea>{fields}<p><button type="submit">Review and calculate</button><button id="fin-sample" type="button">Load fictional example</button></p></form><p id="fin-status" role="status" aria-live="polite"></p></div><h2>Reviewed results</h2><div id="fin-result" aria-live="polite"></div><div class="fin-controls"><h2>Save a copy deliberately</h2><p>No automatic storage or bank connection. These controls do not send entries to a server. Closing/reloading loses entries unless you download a backup. JSON restores valid editable inputs in this exact tool; CSV and print are static reports. Backups do not import into other free tools, Excel or paid products.</p><button id="fin-backup" type="button">Download valid JSON inputs</button><label for="fin-import">Import same-tool JSON, up to 32 KB</label><input id="fin-import" type="file" accept=".json,application/json"><button id="fin-csv" type="button" disabled>Download reviewed CSV</button><button id="fin-print" type="button" disabled>Print / Save PDF</button><button id="fin-clear" type="button">Clear entries</button><dialog id="fin-dialog"><p id="fin-replace-label"></p><button id="fin-confirm" type="button">Replace entries</button><button id="fin-cancel" type="button">Keep current entries</button></dialog><h2>How the calculation works</h2><p>{E(t['formula'])}</p><h2>Original filled example</h2><p>{E(t['example'])}</p><h2>Use the Excel or writing PDF</h2><p>The original .xlsx workbook has Instructions, Blank and Filled example tabs. Yellow cells are editable; green cells calculate only after required inputs pass the sheet checks. Enter numeric zeros deliberately. The check flags missing, out-of-range and excess-decimal inputs; it cannot verify source records. Keep formulas intact. Date and basis checks label the model, not accounting compliance.</p><p>The workbook requests recalculation when opened; test its formulas in your actual application before relying on it. No native Google Sheets copy link or native Excel compatibility certification is claimed. CSV is not an Excel formula workbook. JSON is a browser-tool backup, not a spreadsheet import format.</p><p>The separate two-page PDF is a static US Letter portrait writing sheet followed by the fictional example, not fillable and not calculating. Browser Print / Save PDF prints the reviewed report. Inspect the preview and pagination before sharing. Native printer and spreadsheet-app checks remain application-specific.</p><h2>Review before using the result</h2><p>Check dates, missing accounts, classification, duplicate transactions and source evidence. A zero reconciliation difference or positive result is not an audit or approval to spend. This educational resource does not select accounting methods, calculate tax or certify GAAP/IFRS compliance. If the supported categories do not fit, use a reviewed accounting report rather than forcing the figures into this model.</p><h2>Related tasks</h2><ul>'''+''.join(f'<li><a href="{u}">{E(l)}</a></li>'for u,l in t['links'])+'''</ul><h2>Practical questions</h2><p><strong>Why is a blank amount rejected?</strong> Missing is different from intentional zero. Enter each supported amount and basis before calculating.</p><p><strong>Can I edit after exporting?</strong> Yes. Any input edit removes the old browser result and disables its report exports until reviewed again. Previously downloaded files remain unchanged.</p><p><strong>Can I combine all reports automatically?</strong> No. These are separately reviewed component tools. Their examples align where stated, but the worksheet does not create a ledger or automatically transfer data between statements.</p></div>'''
 page(slug,t['title'],t['desc'],content,'tools');p=R/'tools'/slug/'index.html';normalize_image(p,slug);s=p.read_text();s=s.replace('</head>','''<style>.fin-controls label{display:block;margin:16px 0 5px}.fin-controls input:not([type=file]),.fin-controls textarea{box-sizing:border-box;width:100%;padding:12px;font:inherit;border:1px solid #8bada6;border-radius:6px}.fin-controls textarea{min-height:90px}.fin-grid{display:grid;grid-template-columns:1fr 1fr;gap:15px}.reading a{text-underline-offset:3px}#fin-result .table-wrap:focus{outline:3px solid #176c66}dialog{max-width:460px;border:1px solid #8bada6;border-radius:12px}#fin-form{scroll-margin-top:110px}button:focus-visible,input:focus-visible,textarea:focus-visible{outline:3px solid #a05d2b;outline-offset:2px}@media(max-width:650px){.fin-grid{grid-template-columns:1fr}}@media print{.fin-controls{display:none!important}.reading h2{break-after:avoid}.reading{border:0}#fin-result{display:block}#fin-result table{min-width:0;table-layout:fixed;width:100%}#fin-result th,#fin-result td{overflow-wrap:anywhere}@page{size:portrait;margin:15mm}}</style>'''+f'<script id="finance-config" type="application/json">'+json.dumps(t).replace('<','\\u003c')+'</script></head>',1)
 # Usable input controls precede the chart.
 fig=re.search(r'<figure class="article-feature">.*?</figure>',s)[0];s=s.replace(fig,'',1).replace('<h2>Original filled example</h2>',fig+'<h2>Original filled example</h2>');p.write_text(s)
 # Original workbook; no competitor downloads copied.
 wb=Workbook();inst=wb.active;inst.title='Instructions';instructions=[t['title'],'Original NexalyPlanner educational resource; USD only.','Edit yellow cells. Numeric amounts: 0 to 1,000,000; up to two decimals. Enter all amounts, including zero.','Dates must be real supported dates; start <= end. Basis/source notes are required.','Blank and Filled example use identical formulas. Green results remain blank unless checks pass.',t['scope'],t['formula'],'Save a working .xlsx copy. Native spreadsheet compatibility and print checks are not certified.','Print each sheet: A1:B'+str(8+len(t['fields'])+len(t['report'])+4)+'. Formulas require recalculation.','Cash mismatch is not fixed automatically. Do not use unexplained adjustments.']
 for i,l in enumerate(instructions,1):inst.cell(i,1,l);inst.cell(i,1).alignment=Alignment(wrap_text=True,vertical='top');inst.row_dimensions[i].height=45 if i<6 else 90
 inst.column_dimensions['A'].width=110
 for sample in [False,True]:
  ws=wb.create_sheet('Filled example'if sample else'Blank');ws.append([t['title']]);ws.append(['USD only; fictional figures in Filled example; yellow inputs, green formulas.']);ws.append(['Business / scenario','Fictional '+slug if sample else None]);ws.append(['Start date / preparation window','2026-11-01'if sample else None]);ws.append(['End date / preparation window','2026-11-30'if sample else None]);ws.append(['Basis / assumptions','Simplified USD model; see Instructions. Startup trading horizon is separate.'if sample else None]);ws.append(['Field','USD amount, except months']);refs={}
  for i,(k,l,v) in enumerate(t['fields'],8):
   refs[k]='B'+str(i);ws.cell(i,1,l);ws.cell(i,2,v if sample else None);ws.cell(i,2).fill=PatternFill('solid',fgColor='FFF1BA');ws.cell(i,2).number_format='0'if k=='months'else'#,##0.00;[Red]-#,##0.00'
   dv=DataValidation(type='whole'if k=='months'else'decimal',operator='between',formula1='1'if k=='months'else'0',formula2='24'if k=='months'else'1000000');dv.errorTitle='Check input';dv.error='Use the supported numeric range; up to two decimals for USD.';dv.showErrorMessage=True;dv.errorStyle='stop';ws.add_data_validation(dv);dv.add(ws.cell(i,2))
  end=7+len(t['fields']);check=end+2;checks=[]
  for k,cell in refs.items():checks.append(f'AND(ISNUMBER({cell}),{cell}>={1 if k=="months"else 0},{cell}<={24 if k=="months"else 1000000},{cell}=ROUND({cell},{0 if k=="months"else 2}))')
  # ISO date text keeps the workbook independent of local spreadsheet date serial display.
  ds=lambda c:f'AND(LEN({c})=10,IFERROR(TEXT(DATE(VALUE(LEFT({c},4)),VALUE(MID({c},6,2)),VALUE(RIGHT({c},2))),"yyyy-mm-dd")={c},FALSE),{c}>="1900-01-01",{c}<="2200-12-31")'
  checks+=['LEN(TRIM(B3))>0','LEN(B3)<=100','LEN(TRIM(B6))>0','LEN(B6)<=500',ds('B4'),ds('B5'),'B4<=B5']
  if slug=='income-statement-template':checks.append(refs['returns']+'<='+refs['sales'])
  ws.cell(check,1,'Input review');ws.cell(check,2,'=IFERROR(IF(AND('+','.join(checks)+'),"Ready","Check inputs"),"Check inputs")')
  if slug=='startup-budget-template':
   uses='+'.join(refs[k]for k in ['equipment','setup','deposits','contingency']);net=f'({refs["monthlyPayments"]}-{refs["monthlyReceipts"]})';short=f'MAX(0,{net})*{refs["months"]}';target=f'({uses}+{short}+{refs["reserve"]})';expressions=[uses,net,short,target,f'{refs["funding"]}-{target}',f'{refs["funding"]}-({uses})-{net}*{refs["months"]}']
  else:expressions=[calc_expr(expr,refs)for lab,expr in t['report']]
  for i,((lab,expr),formula)in enumerate(zip(t['report'],expressions),check+2):ws.cell(i,1,lab);ws.cell(i,2,f'=IF(B{check}="Ready",ROUND({formula},2),"")');ws.cell(i,2).fill=PatternFill('solid',fgColor='DDEEE6');ws.cell(i,2).number_format='#,##0.00;[Red]-#,##0.00'
  for r in [3,4,5,6]:ws.cell(r,2).fill=PatternFill('solid',fgColor='FFF1BA')
  for row in ws:
   for c in row:c.alignment=Alignment(wrap_text=True,vertical='top');c.font=Font(name='Calibri',size=11,color='173D38')
  ws.column_dimensions['A'].width=65;ws.column_dimensions['B'].width=46;ws.row_dimensions[1].height=45;ws.row_dimensions[6].height=50;ws.freeze_panes='B8';ws.print_options.horizontalCentered=True;ws.sheet_properties.pageSetUpPr.fitToPage=True;ws.page_setup.orientation='portrait';ws.page_setup.paperSize=ws.PAPERSIZE_LETTER;ws.page_setup.fitToWidth=1;ws.page_setup.fitToHeight=1;ws.print_area=f'A1:B{check+1+len(t["report"])}'
 wb.calculation=CalcProperties(calcId=191029,fullCalcOnLoad=True);wb.save(R/'downloads'/f'{slug}.xlsx')
 # Two-page static PDF: writing sheet and exact worked example.
 c=canvas.Canvas(str(R/'downloads'/f'{slug}.pdf'),pagesize=letter)
 for sample in [False,True]:
  y=750;c.setFont('Helvetica-Bold',15)
  for line in textwrap.wrap(t['title'],62):c.drawString(40,y,line);y-=20
  c.setFont('Helvetica',10);c.drawString(40,y,'FILLED FICTIONAL EXAMPLE'if sample else'BLANK WRITING SHEET · USD ONLY');y-=24
  for label in ['Business / scenario','Start / end dates','Basis and source references']:
   c.drawString(40,y,label+': '+('See original example and guide.'if sample else'_'*48));y-=23
  for k,label,v in t['fields']:c.drawString(40,y,label[:75]);c.drawRightString(568,y,str(v)if sample else'________________');y-=22
  y-=10
  for label,expr in t['report']:c.drawString(40,y,label[:72]);c.drawRightString(568,y,'See guide'if sample else'________________');y-=22
  if sample:
   y-=10
   for line in textwrap.wrap(t['example'],99):c.drawString(40,y,line);y-=14
  c.setFont('Helvetica',8);c.drawString(40,36,'Static writing/example sheet: not fillable or calculating. Original NexalyPlanner model; see page for scope.');c.showPage()
 c.save()
(D/'articles.json').write_text(json.dumps([{k:a[k]for k in ['id','slug','title','desc','sources']}for a in A],indent=2));print('Built 6 original journals, 3 working resources, 9 original charts and 6 downloadable files')

# Preserve the owner-approved editorial covers after rebuilding Day1 source.
if (R/'docs/editorial/2026-11-18-feature-refresh/images.json').exists():
 runpy.run_path(str(R/'docs/editorial/2026-11-18-feature-refresh/apply.py'))
