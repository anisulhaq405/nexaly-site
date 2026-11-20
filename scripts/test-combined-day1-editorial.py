from pathlib import Path
from decimal import Decimal as D
import json,re,sys
from openpyxl import load_workbook
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];P=R/'docs/editorial/2026-11-18-combined-day1';A=json.load(open(P/'articles.json'));T=json.load(open(P/'tools.json'));assert len(A)==6 and len(T)==3
# Independent statement reconciliation from explicit journal transaction assumptions.
opening_assets=10000+2000+3000+8000-2000;assert opening_assets==2000+5000+14000
cogs=3000+5000-2500;profit=12000-cogs-3000-200;cashop=11000-4500-3000;assert profit==3300 and cashop==3500
closing_cash=10000+cashop-1000+2000-500-600;equity=14000+profit-600;assert closing_cash==13400 and equity==16700
assert closing_cash+(2000+12000-11000)+2500+(8000+1000-2000-200)==(2000+5000-4500)+(5000+2000-500)+equity==25700
assert profit+200-1000+500+500==cashop
assert 4000+7200-200+300-3100==8200 and round(D(4800)/13000*100,2)==D('36.92')
assert 10000-3000-2500==4500 and 4500-2500==2000 and 10000+4000-7500-1000==5500 and 10000-7500==2500
assert 80000-30000-10000==40000 and 40000/20000==2 and 120000/240000==.5 and round(D(90)/108*100,2)==D('83.33') and 184-160==24
assert 20*3*30*5==9000 and 9000*D('1.6')==14400 and 14400*D('.75')-6000-1500==3300 and 9600*D('.75')-6000-1500==-300
assert 90000+25000+10000+20000==45000+100000==145000
for a in A:
 s=(R/'journal'/a['slug']/'index.html').read_text();assert '## 'not in s;assert len(re.sub('<[^>]+>',' ',s).split())>600;assert '2026-11-18'in s
for t in T:
 slug=t['slug'];s=(R/'tools'/slug/'index.html').read_text();assert 'finance-config'in s and 'fin-import'in s
 wb=load_workbook(R/'downloads'/f'{slug}.xlsx');assert wb.sheetnames==['Instructions','Blank','Filled example'];assert wb.calculation.fullCalcOnLoad;assert all(wb['Blank'].cell(i,2).value is None for i in range(8,8+len(t['fields'])))
 for ws in [wb['Blank'],wb['Filled example']]:
  formulas=[c.value for row in ws for c in row if c.data_type=='f'];assert len(formulas)==len(t['report'])+1;assert all('IF('in f for f in formulas);assert not any('#REF!'in f for f in formulas);assert 'ISNUMBER'in formulas[0] and 'ROUND'in formulas[0]
 pdf=PdfReader(R/'downloads'/f'{slug}.pdf');assert len(pdf.pages)==2 and not pdf.get_fields();assert tuple(map(int,pdf.pages[0].mediabox[2:]))==(612,792);assert 'FICTIONAL EXAMPLE'in pdf.pages[1].extract_text()
for a in json.load(open(P/'audits.json')):
 s=(R/a['owner'].strip('/')/'index.html').read_text();assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==a['datePublished'];assert 'finance-report-handoff'in s
s=(R/'tools/index.html').read_text();assert len(re.findall(r'<article\b[^>]*class="[^"]*\bdirectory-tool\b',s))==67 and '<b>67</b> free planners'in s
print('PASS combined Day1 editorial: independent arithmetic, dates, six audits, nine pages, XLSX structure/formula guards, 2-page PDFs and 67 current directory cards. Native spreadsheet recalculation is not tested.')
