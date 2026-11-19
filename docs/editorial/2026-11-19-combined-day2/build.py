from pathlib import Path
import runpy,json,re,html,textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
D=Path(__file__).resolve().parent;R=D.parents[2];E=html.escape
A=runpy.run_path(str(D/'content.py'))['A'];T=runpy.run_path(str(D/'tools.py'))['T']
# Reuse the established article shell, not the historical source-generation side effects.
base=(R/'docs/editorial/2026-11-12-day6/build.py').read_text().split('for a in A:page')[0]
base=base.replace("A=runpy.run_path(str(D/'content.py'))['A'];",'').replace('2026-11-12','2026-11-19').replace('20261112','20261119').replace('November 12, 2026','November 19, 2026').replace('day6-strategy.js','business-planning-20261119.js')
exec(base,globals())
def readable(s):return re.sub(r'(?<=[a-z])(?=\d)|(?<=\d)(?=[A-Za-z])|(?<=[×÷])(?=\d)',' ',s)
for a in A:a['text']=readable(a['text'])
for t in T:
 for k in ['scope','guide','example']:t[k]=readable(t[k])
 t['fields']=[[k,readable(l),v]for k,l,v in t['fields']]
pdfmetrics.registerFont(TTFont('Planner','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PlannerBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
for a in A:page(a['slug'],a['title'],a['desc'],a['text'],sources=a['sources'])
for t in T:
 slug=t['slug'];fields=''
 for k,l in [('name','Project / decision name (max100 characters)'),('start','Period start'),('end','Period end'),('asof','Review date within period'),('notes','Basis, sources, exclusions and assumptions (max1,000 characters)')]+[(k,l)for k,l,v in t['fields']]:
  if t['mode']=='benefit' and k in ['start','end']:l='Decision-review window '+('start'if k=='start'else'end')
  control=f'<textarea id="bp-{k}" maxlength="1000" required></textarea>'if k=='notes'else f'<input id="bp-{k}" '+('type="date" min="1900-01-01" max="2200-12-31"'if k in ['start','end','asof']else'type="text" maxlength="100"'if k=='name'else'type="text" maxlength="12" inputmode="decimal"')+' required>'
  fields+=f'<label for="bp-{k}">{E(l)}{control}</label>'
 content=f'''<div class="bp-controls"><p><a href="#bp-form">Use the editable worksheet ↓</a> · <a href="/downloads/{slug}.pdf" download>Download static blank + example PDF</a></p><p>{E(t['scope'])}</p><p>Money fields:0–1,000,000 USD, up to2 decimals. Staffing hours:0–10,080 per role, up to2 decimals. Enter all relevant fields including intentional zeros. No currency conversion.</p><noscript><p>JavaScript is needed for editable controls. The guide and static writing PDF remain available.</p></noscript><h2>Enter your fixed-period assumptions</h2><form id="bp-form">{fields}'''
 if t['rows']:content+='<h3>'+('Cost lines'if t['mode']=='project'else'Distinct role / skill pools')+'</h3><div id="bp-rows"></div><button id="bp-add" type="button">Add row</button>'
 content+='''<p><button type="submit">Review worksheet</button><button id="bp-sample" type="button">Load fictional example</button></p></form><p id="bp-status" role="status" aria-live="polite"></p></div><h2>Reviewed report</h2><div id="bp-result" aria-live="polite"><p>Enter your assumptions and review the worksheet.</p></div><div class="bp-controls"><h2>Keep a deliberate copy</h2><p>No automatic saving, account connection or cross-device sync. Closing/reloading loses entries unless you keep a JSON backup. Entries are not sent to a server. Same-tool JSON restores editable inputs; CSV and print are static reports, not editable spreadsheet formulas or paid-app imports. Each input edit removes the previous report until reviewed again.</p><button id="bp-backup" type="button">Download valid JSON inputs</button><label>Import same-tool JSON (64 KB maximum)<input id="bp-import" type="file" accept=".json,application/json"></label><button id="bp-csv" type="button" disabled>Download reviewed CSV</button><button id="bp-print" type="button" disabled>Print / Save PDF</button><button id="bp-clear" type="button">Clear entries</button><dialog id="bp-dialog" aria-labelledby="bp-dialog-title"><h2 id="bp-dialog-title">Replace page entries?</h2><p id="bp-dialog-text"></p><button id="bp-confirm" type="button">Replace entries</button><button id="bp-cancel" type="button">Keep current entries</button></dialog></div><h2>Original fictional example</h2><p>'''+E(t['example'])+'</p>'+body(t['guide'])+'<h2>Downloads and printing</h2><p>The separate two-page US Letter PDF has a blank writing sheet and an original filled example. It is static, not fillable or calculating. Browser Print / Save PDF prints the reviewed report; inspect pagination and paper size before sharing. CSV is a reviewed report, not an XLSX workbook. Keep the JSON backup for browser editing. Native printer output is device-specific.</p><h2>Continue the planning task</h2><ul>'+''.join(f'<li><a href="{u}">{E(l)}</a></li>'for u,l in t['links'])+'</ul>'
 page(slug,t['title'],t['desc'],content,'tools');p=R/'tools'/slug/'index.html';s=p.read_text()
 # Keep usable controls before the conceptual cover; the jump remains above the inputs.
 fig=re.search(r'<figure class="article-feature">.*?</figure>',s)[0];s=s.replace(fig,'',1).replace('<h2>Original fictional example</h2>',fig+'<h2>Original fictional example</h2>',1)
 s=s.replace('</head>','<link rel="stylesheet" href="/assets/css/business-planning-20261119.css"><script type="application/json" id="bp-config">'+json.dumps(t).replace('<','\\u003c')+'</script></head>',1);p.write_text(s)
 c=canvas.Canvas(str(R/'downloads'/f'{slug}.pdf'),pagesize=letter,invariant=1);c.setTitle(t['title'])
 def line(txt,y,size=10,bold=False):
  font='PlannerBold'if bold else'Planner';c.setFont(font,size);words=readable(txt).split();lines=[];current=''
  for word in words:
   next=(current+' '+word).strip()
   if pdfmetrics.stringWidth(next,font,size)>528 and current:lines.append(current);current=word
   else:current=next
  if current:lines.append(current)
  for ln in lines:c.drawString(40,y,ln);y-=15 if size<=10 else 21
  return y
 for sample in [False,True]:
  y=line(t['title'],750,15,True);y=line('ORIGINAL FICTIONAL EXAMPLE'if sample else'BLANK WRITING SHEET',y-8,10,True)
  y=line(t['scope'],y-10)
  for label,val in [('Project / decision name','Fictional planning example'),('Period start / end','2026-11-01 / 2026-11-30'),('Review date','2026-11-19'),('Assumptions and source references','Original educational scenario; see guide for exclusions')]:y=line(label+': '+(val if sample else'_'*48),y-12)
  if sample:
   for k,label,val in t['fields']:y=line(label+': '+val,y-8)
   if t['rows']:
    for row in t['sampleRows']:y=line('; '.join(k+': '+str(v)for k,v in row.items()),y-10)
   y=line('Worked interpretation',y-18,11,True);y=line(t['example'],y-6)
  else:
   if t['rows']:
    y=line('Row fields: '+ '; '.join(r[1]for r in t['rows']),y-16)
    for n in range(1,5):y=line('Row '+str(n)+': '+'_'*77,y-20)
   else:
    for k,label,val in t['fields']:y=line(label+': __________',y-12)
   y=line('Reviewed result and decision: '+'_'*44,y-26)
  assert y>70,(slug,y)
  c.setFont('Helvetica',8);c.drawString(40,38,'NexalyPlanner | Static writing/example sheet: not fillable or calculating. See online guide for scope.');c.drawRightString(570,24,'2'if sample else'1');c.showPage()
 c.save()
(D/'articles.json').write_text(json.dumps([{k:a[k]for k in ['id','slug','title','desc','sources']}for a in A],indent=2)+'\n');(D/'tools.json').write_text(json.dumps(T,indent=2)+'\n')
# Add new, image-complete cards to the existing business category; do not disturb old cards.
p=R/'tools/index.html';s=p.read_text()
for t in T:
 if 'href="/tools/'+t['slug']+'/"'in s:continue
 card=f'''<article class="directory-tool theme-card theme-teal" data-category="{t['category']}" data-latest="true" data-search="{E(t['title']+' '+t['desc'],quote=True)}"><a class="directory-preview" href="/tools/{t['slug']}/" aria-label="Open {E(t['title'],quote=True)}"><img src="/images/journal/{t['slug']}-20261119.webp" width="1200" height="800" alt="{E(t['title'],quote=True)} conceptual planning cover" loading="lazy" decoding="async"></a><div class="library-card-body"><p class="library-card-meta"><span>Business planning</span><span class="library-new">Latest addition</span></p><h3><a href="/tools/{t['slug']}/">{E(t['title'])}</a></h3><p class="library-card-description">{E(t['desc'])}</p><div class="library-card-footer"><a class="library-card-link" href="/tools/{t['slug']}/">Open free planner ↗</a><span class="library-card-formats">PDF · CSV · JSON · Print</span></div></div></article>'''
 pos=s.index('data-category="'+t['category']+'"');start=s.rfind('<section',0,pos);end=s.index('</section>',pos);part=s[start:end];part=part.replace('</div>', '</div>',1);ix=part.rfind('</div>');part=part[:ix]+card+part[ix:];s=s[:start]+part+s[end:]
count=len(re.findall(r'<article\b[^>]*\bdirectory-tool\b',s));assert count==67,count
s=s.replace('64 free business','67 free business').replace('<b>64</b>','<b>67</b>').replace('>40 planners</p>','>67 planners</p>')
# Reconcile visible category badges with actual cards.
def counts(m):
 part=m[0];n=len(re.findall(r'<article\b[^>]*\bdirectory-tool\b',part));part=re.sub(r'data-visible-count="\d+"',f'data-visible-count="{n}"',part);return re.sub(r'(<p class="category-count">)\d+( planners</p>)',lambda q:q[1]+str(n)+q[2],part)if n else part
s=re.sub(r'<section\b.*?</section>',counts,s,flags=re.S);p.write_text(s)
print('Built6 journals,3 interactive resources,3 PDFs and67 directory cards')
