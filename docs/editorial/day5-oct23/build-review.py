from pathlib import Path
import sys, re, html, json, subprocess, base64, zipfile, hashlib, mimetypes
from urllib.parse import urlsplit, unquote
from fractions import Fraction
from importlib.machinery import SourceFileLoader
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT.parent/'day5-content-review'
sys.path.insert(0,str(ROOT/'scripts'))
M=SourceFileLoader('seo4review',str(ROOT/'scripts/seo-build.py')).load_module();D=M.Document
rows=json.loads((OUT/'content-register.json').read_text())
route={('/'+x['path'][:-10]):'#page-'+str(i+1) for i,x in enumerate(rows)}
newfiles=['assets/downloads/small-business-balance-sheet-template.xlsx','assets/downloads/small-business-balance-sheet-template.pdf']

def enc(path):
 p=ROOT/path;mime=mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
 return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
def text(s):return html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',s,flags=re.S)))
def reading(s,i):
 d=D(s);main=d.inner(d.find('main')[0]);d=D(main);cuts=[]
 for e in d.elements:
  if e['tag'] in ['script','style','input','button','textarea','select','dialog','noscript'] and e.get('end') is not None:cuts.append((e['start'],e['end']))
 merged=[]
 for a,b in sorted(cuts):
  if merged and a<=merged[-1][1]:merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
  else:merged.append((a,b))
 for a,b in reversed(merged):main=main[:a]+main[b:]
 # Omit decorative article covers; keep actual new resource previews embedded.
 main=re.sub(r'<figure class="article-feature">.*?</figure>','',main,flags=re.S)
 main=re.sub(r'<h1\b[^>]*>(.*?)</h1>',r'<h2>\1</h2>',main,flags=re.S)
 ids=re.findall(r'\bid="([^"]+)"',main)
 for sid in sorted(ids,key=len,reverse=True):main=main.replace('id="'+sid+'"',f'id="p{i}-'+sid+'"').replace('href="#'+sid+'"',f'href="#p{i}-'+sid+'"')
 def link(m):
  u=html.unescape(m[1]);p=urlsplit(u).path
  if p in route:return 'href="'+route[p]+'"'
  if p.lstrip('/') in newfiles:return 'href="'+enc(p.lstrip('/'))+'" download="'+Path(p).name+'"'
  if u.startswith('/'):return 'href="https://nexalyplanner.com'+html.escape(u,quote=True)+'"'
  return m[0]
 main=re.sub(r'href="([^"]+)"',link,main)
 for path in ['assets/img/resource-previews/small-business-balance-sheet-example.webp','assets/img/resource-previews/small-business-balance-sheet-blank.webp']:
  main=main.replace('src="/'+path+'"','src="'+enc(path)+'"')
 # Existing unrelated images can remain linked to the public site.
 main=re.sub(r'src="(/[^\"]+)"',r'src="https://nexalyplanner.com\1"',main)
 return main

notes=[
 'Explains the $400 volume reduction and $200 total effect from higher average unit cost behind the net $200 variable-cost reduction; separates operating, cash and balance-sheet records.',
 'Adds a paired principal-payment example and checks a $1,200 collection delay without duplicate receipts; preserves the existing workbook and Sheets link.',
 'Shows why 3.80 weighted points with an unmeasured 10% response criterion is not a comparable final score; retains source counts and policy history.',
 'Adds a checked partial-material example: 4.5 first-batch hours + 1.5 later hours = 6, versus the original uninterrupted 5.5 hours.',
 'Explains the existing $600/$500 campaign sample, channel duplicate counts, zero denominators and the decision before allocating the remaining $100.',
 'Adds an explicitly manual ecommerce assumption test; preserves the builder as a compact text/evidence summary, with no new arithmetic or funding-application claims.',
 'New educational balance-sheet guide, two-tab workbook, actual previews and two-page blank/filled PDF. Thirteen workbook tests and an XLSX round-trip test pass.'
]
checks=[]
for row in rows:
 p=ROOT/row['path'];s=p.read_text();d=D(s);ids=[e['attrs']['id'] for e in d.elements if 'id' in e['attrs']]
 assert len(ids)==len(set(ids)),p
 for e in d.elements:
  for attr in ['href','src']:
   u=urlsplit(html.unescape(e['attrs'].get(attr,'')))
   if u.scheme or u.netloc:continue
   if u.path:
    t=ROOT/u.path.lstrip('/') if u.path.startswith('/') else p.parent/u.path
    if t.is_dir():t=t/'index.html'
    assert t.exists(),(p,u.path)
   elif u.fragment:assert unquote(u.fragment) in ids,(p,u.fragment)
 assert len(d.find('h1'))==1,p
 if row is not rows[-1]:
  old=subprocess.check_output(['git','show','HEAD:'+row['path']],cwd=ROOT,text=True)
  norm=lambda z:re.sub(r'main.js\?v=[a-z0-9]+','main.js?v=CACHE',z)
  scripts=lambda z:[norm(x) for x in re.findall(r'<script\b[^>]*>.*?</script>',z,re.S) if 'application/ld+json' not in x]
  assert scripts(old)==scripts(s),(p,'executable behavior changed')
  assert re.findall(r'<meta property="article:(?:published|modified)_time"[^>]*>',s)==re.findall(r'<meta property="article:(?:published|modified)_time"[^>]*>',old),(p,'historical date changed')
 checks.append({'path':row['path'],'local_links':'pass','unique_ids':'pass','one_h1':'pass','existing_scripts':'preserved' if row is not rows[-1] else 'new resource'})
new=(ROOT/rows[-1]['path']).read_text();assert 'noindex,follow' in new
assert 'https://nexalyplanner.com/journal/small-business-balance-sheet-template/' not in (ROOT/'sitemap.xml').read_text()
arith={
 'budget_volume':180*20-4000==-400,
 'budget_rate':3800-180*20==200,
 'supplier_missing':round(4*.4+4*.3+5*.2,2)==3.8,
 'production_split':.75+30*6/60+.75==4.5 and .25+10*6/60+.25==1.5,
 'campaign_email':180/12==15 and 180/3==60,
 'campaign_search':320/8==40 and 320/1==320,
 'ecommerce_example':40-18-5-2==15 and 10*15-120==30,
 'balance_equation':6000+2500+4000+3500-1000==15000 and 2200+800+3000==6000 and 7500+2000-500==9000,
 'debt_payment':15000-1000==6000-1000+9000}
assert all(arith.values())
model=json.loads((OUT/'balance-sheet-tests.json').read_text());assert len(model)==13 and all(x['pass'] for x in model)
rt=json.loads((OUT/'balance-sheet-roundtrip.json').read_text());assert rt['pass']
reg=Path('/tmp/day5-seo-test.log').read_text().strip();assert reg.startswith('PASS:'),'Publishing regression still running'
validation={'prepared':'2026-10-23','baseline':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'status':'draft only','pages':checks,'content_arithmetic':arith,'workbook_tests':13,'xlsx_export_import_recalculation':'pass; not native Excel','workbook_views_inspected':2,'pdf_pages_inspected':2,'formula_error_scan':'no errors in new workbook','publishing_regression':reg,'core_protection':'pass','generated_seo':'pass','new_route':'noindex; excluded from sitemap','remote_writes':'none','pending':['Qualified accounting review before consequential reporting/publication','Native Excel/Sheets recalculation and print','Physical phone save/reopen','Signed-in Google Sheets copy access','Fresh USA top-ten location/device verification','GSC indexing and GA4 backend events','Browser viewport rendering']}
(OUT/'validation.json').write_text(json.dumps(validation,indent=2))
ownership=[
 ('company budget template','/journal/small-business-budget-template-monthly-variance/','Improve current business budget/variance resource; exclude unrelated household budgets.'),
 ('cash flow template excel','/journal/cash-flow-forecast-template-example/','Reuse existing 13-week workbook; keep cash timing separate from profit and dated balances.'),
 ('supplier scorecard','/journal/supplier-scorecard-template/','Reuse existing workbook and explain documented weights and incomplete evidence.'),
 ('production schedule template','/journal/production-schedule-template/','Keep manufacturing resource scheduling distinct from content production.'),
 ('marketing budget template','/tools/marketing-campaign-budget-planner/','Preserve current planner controls; explain sample spend and attribution limits.'),
 ('ecommerce business plan template','Hold exact broad-query assignment','The one-page builder is a compact summary; full ecommerce plan intent needs separate verification. Reviewed builder is not relabeled a complete plan.'),
 ('business balance sheet template','/journal/small-business-balance-sheet-template/','Proposed free resource, separate from budget, profit-and-loss and cash forecast.')]
research='''# Day 5 research and ownership

Prepared October 23, 2026. Draft only; no push, PR, merge, deployment or indexing request.

The saved seven-day plan is the source of the seven topic assignments. Historical keyword metrics are not described as a fresh ranking report. Public search discovery and comparator pages help assess formats and practical intent, but country/device rankings and ranking causes were not verified. No new keyword targets were imported from competitors.

The SEC Beginners' Guide to Financial Statements was read at https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements for the basic statement definitions and equation. The example numbers are original fictional teaching figures. Sage's balance-sheet template page was read for format/intent comparison; its calculations or template were not copied. Further public discovery covered budget variance, 13-week cash forecasts, supplier scorecards, production schedules, campaign budgets and ecommerce plan templates.

The response uses direct workbook access, blank and filled examples, visible input checks, independent equity balances, a $100 mismatch walkthrough, real previews and explicit print instructions to meet the observed template intent. These features do not establish why a competitor ranks or promise a position.

Financial scope: this simplified educational template does not determine real account classifications, depreciation, tax or filing compliance. The user-supplied playbook calls for a qualified reviewer before consequential financial claims are published. Qualified accounting review remains open; nothing is published in this draft round. No paid product features, prices, checkout, shared JS/CSS, canonical templates or redirects are changed.

Release gates: review latest main, resolve accounting/content review, set actual publication/update dates, remove only the new article draft noindex/banner, regenerate, pass current-head CI, verify live files, then update the existing URL register with Unverified indexing until Google evidence exists. Existing Google Sheets and native-device access checks remain open.
'''
(OUT/'research-and-ownership.md').write_text(research+'\n## Ownership\n\n'+'\n'.join('- '+k+': '+owner+'. '+why for k,owner,why in ownership))
panels=[];summary=[]
for i,(row,note) in enumerate(zip(rows,notes),1):
 s=(ROOT/row['path']).read_text();title=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S)[1]);d=D(s);wc=len(text(d.inner(d.find('main')[0])).split())
 if i<=6:
  old=subprocess.check_output(['git','show','HEAD:'+row['path']],cwd=ROOT,text=True);dd=D(old);before=len(text(dd.inner(dd.find('main')[0])).split())
 else:before=0
 row.update({'change':note,'before_words_approx':before,'draft_words_approx':wc})
 summary.append(f'<tr><td><a href="#page-{i}">{html.escape(title)}</a></td><td>{html.escape(note)}</td><td>{before} → {wc}</td></tr>')
 panels.append(f'<section class="page" id="page-{i}"><p class="eyebrow">DRAFT {i} OF 7 · NOT PUBLISHED</p><h1>{html.escape(title)}</h1><p class="small">'+html.escape(row['path'])+f'</p><p>{html.escape(note)}</p><div class="copy">'+reading(s,i)+'</div><p><a href="#overview">Back to overview</a></p></section>')
(OUT/'content-register.json').write_text(json.dumps(rows,indent=2))
css=(OUT/'review-style.txt').read_text()+'.copy section[id*="budget-variance-review"],.copy section[id*="cash-and-balance-sheet"],.copy section[id*="scorecard-missing-evidence"],.copy section[id*="production-partial-materials"],.copy section[id*="campaign-budget-decisions"],.copy section[id*="test-ecommerce-assumptions"]{background:#f1f8f5;padding:18px}'
downloadlinks=''.join(f'<a href="{enc(p)}" download="{Path(p).name}">{html.escape(Path(p).name)}</a>' for p in newfiles)
owners=''.join(f'<tr><td>{html.escape(k)}</td><td>{html.escape(owner)}</td><td>{html.escape(why)}</td></tr>' for k,owner,why in ownership)
review='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NexalyPlanner Day 5 Draft Review</title><style>'+css+'</style><header><p class="eyebrow">NEXALYPLANNER · DAY 5</p><h1>Business and finance content draft review</h1><p>Prepared October 23, 2026 · USA primary audience · Draft only</p></header><main><section class="panel" id="overview"><p class="status"><strong>NOT PUBLISHED.</strong> Six existing page revisions and one proposed balance-sheet guide. No remote writes. Existing dates remain historical; the new page is noindex and excluded from sitemap.</p><p>Read the complete drafts below. New content is shaded. Controls and decorative article covers are omitted in this reading copy. The two new download links embed the actual workbook/PDF; links between draft pages stay in this review. Other links open existing public pages.</p><div class="table-wrap"><table><thead><tr><th>Draft</th><th>Completed work</th><th>Approximate main-content words</th></tr></thead><tbody>'+''.join(summary)+'</tbody></table></div><h2>Draft balance-sheet files</h2><div class="downloads">'+downloadlinks+'</div><p>The workbook contains Blank and Filled example tabs. The PDF contains a blank form and fictional filled example. Total assets 15,000, liabilities 6,000 and equity 9,000; the $100 mismatch and one-cent difference tests pass.</p><h2>Ownership and overlap decisions</h2><div class="table-wrap"><table><thead><tr><th>Agreed query</th><th>Owner</th><th>Decision</th></tr></thead><tbody>'+owners+'</tbody></table></div><h2>Verification and release gates</h2><p>Thirteen workbook checks, XLSX export/import recalculation, nine content arithmetic checks, both worksheet renders, both PDF pages, local links/anchors, unchanged existing scripts, generated SEO, publishing regression and protected core pass. Original supplier/cash-flow workbooks are preserved; read-only formula scans are included separately.</p><p>Qualified accounting review remains open before consequential financial publication/reporting. Native Excel/Sheets, real phone/PDF app saving and printing, signed-in Google Sheets copy access, browser viewport rendering, GA4/GSC and fresh country/device top-ten ranking checks are not certified. Public research is not presented as confirmed USA rankings.</p></section>'+''.join(panels)+'</main></html>'
name='NexalyPlanner-Day-5-Content-Draft-Review-2026-10-23.html';(OUT/name).write_text(review)
patch=subprocess.check_output(['git','diff','--binary','HEAD'],cwd=ROOT);(OUT/'changes.patch').write_bytes(patch)
changed=subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=ROOT,text=True).splitlines()
added=newfiles+['journal/small-business-balance-sheet-template/index.html','assets/img/resource-previews/small-business-balance-sheet-blank.webp','assets/img/resource-previews/small-business-balance-sheet-example.webp']+[str(p.relative_to(ROOT)) for p in (ROOT/'docs/editorial/day5-oct23').glob('*') if p.is_file()]
sources=sorted(set(changed+added));manifest=[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in sources]
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2))
(OUT/'README.md').write_text('# Day 5 draft packet\n\nOpen '+name+' for all seven reading drafts and embedded workbook/PDF downloads. Source files are for review, not deployment. See research-and-ownership.md and validation.json for review gates and evidence. No native application, Google backend or qualified accounting review is claimed.\n')
with zipfile.ZipFile(OUT/'NexalyPlanner-Day-5-Content-Drafts-2026-10-23.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in [OUT/name,OUT/'README.md',OUT/'content-register.json',OUT/'validation.json',OUT/'research-and-ownership.md',OUT/'source-manifest.json',OUT/'changes.patch',OUT/'balance-sheet-tests.json',OUT/'balance-sheet-roundtrip.json',OUT/'balance-sheet-errors.ndjson']:z.write(p,p.name)
 for p in OUT.glob('*xlsx-*.ndjson'):z.write(p,'qa/'+p.name)
 for p in sources:z.write(ROOT/p,'source/'+p)
 for p in OUT.glob('balance-sheet-*.png'):z.write(p,'qa-previews/'+p.name)
 for p in (OUT/'pdf-renders').glob('*.png'):z.write(p,'qa-previews/'+p.name)
print(json.dumps({'pages':7,'workbook_tests':13,'content_arithmetic_checks':9,'source_files':len(sources),'status':'draft only','review':str(OUT/name)},indent=2))

