from pathlib import Path
import sys, re, html, json, subprocess, base64, zipfile, hashlib, mimetypes
from urllib.parse import urlsplit, unquote
from fractions import Fraction
from importlib.machinery import SourceFileLoader
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT.parent/'day4-content-review'
sys.path.insert(0,str(ROOT/'scripts'))
M=SourceFileLoader('seo4review',str(ROOT/'scripts/seo-build.py')).load_module();D=M.Document
rows=json.loads((OUT/'content-register.json').read_text())
notes=[
 'Adds a real daily PDF and editable text copy, printing instructions and an actual worksheet preview; corrects the example desk-start time.',
 'Explains Sunday-first date placement, six-row months and a 180-minute monthly allocation with 30 minutes spare.',
 'Removes unsupported workbook and automatic-date claims; supplies an editable ten-day text plan and connects practice gaps to the new study guide.',
 'Uses the existing printable layout for one main action, an explicit blocker and a restart point; distinguishes handwriting layouts from editable tools.',
 'Tests a two-learner support rotation against the adult time actually available; keeps schedule, completed work and attendance distinct.',
 'Adds a checked 130-minute production example and sold-out-product decisions; separates a clothing post calendar from the generic marketing-plan owner.',
 'New resource with a blank PDF, original fraction example, editable text, format limits, source-based recall instructions and contextual student links.'
]
route={('/'+x['path'][:-10]):'#page-'+str(i+1) for i,x in enumerate(rows)}
newfiles=['assets/downloads/study-guide-template.pdf','assets/downloads/study-guide-template.txt','assets/downloads/daily-planner-template.pdf','assets/downloads/daily-planner-template.txt','assets/downloads/exam-study-schedule-template.txt']
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
 for path in ['assets/img/resource-previews/study-guide-template.webp','assets/img/resource-previews/daily-planner-template.webp']:
  main=main.replace('src="/'+path+'"','src="'+enc(path)+'"')
 # Existing unrelated images can remain linked to the public site.
 main=re.sub(r'src="(/[^\"]+)"',r'src="https://nexalyplanner.com\1"',main)
 return main

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
 if row['path'].startswith('journal/'):
  old=subprocess.check_output(['git','show','HEAD:'+row['path']],cwd=ROOT,text=True)
  norm=lambda z:re.sub(r'main.js\?v=[a-z0-9]+','main.js?v=CACHE',z)
  scripts=lambda z:[norm(x) for x in re.findall(r'<script\b[^>]*>.*?</script>',z,re.S) if 'application/ld+json' not in x]
  assert scripts(old)==scripts(s),(p,'executable behavior changed')
  assert re.findall(r'<meta property="article:(?:published|modified)_time"[^>]*>',s)==re.findall(r'<meta property="article:(?:published|modified)_time"[^>]*>',old),(p,'historical date changed')
 checks.append({'path':row['path'],'local_targets':'pass','unique_ids':'pass','h1':'pass'})
new=(ROOT/'tools/study-guide-template/index.html').read_text()
assert 'noindex,follow' in new
assert 'https://nexalyplanner.com/tools/study-guide-template/' not in (ROOT/'sitemap.xml').read_text()
assert 'recalculate from that input' not in (ROOT/'journal/exam-study-schedule-template/index.html').read_text()
arithmetic={
 'fraction_addition':Fraction(3,4)+Fraction(1,8)==Fraction(7,8),
 'fraction_recall':Fraction(1,2)+Fraction(1,4)==Fraction(3,4),
 'fraction_revision':Fraction(2,3)+Fraction(1,6)==Fraction(5,6),
 'study_minutes':sum([25,30,30,25,30,25,40,25,20])==250,
 'monthly_capacity':4*45-2*60-30==30,
 'homeschool_rotation':20+5+20+10==55 and 30+5+20+10==65,
 'clothing_production':40+3*20+3*10==130 and 130+30-140==20,
 'daily_morning':60+15+30+15+30+15+15==180}
assert all(arithmetic.values())
reg=Path('/tmp/day4-seo-final-test.log').read_text().strip();assert reg.startswith('PASS:'),'Wait for publishing regression to finish.'
validation={'prepared':'2026-10-23','baseline':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'status':'draft only','pages':checks,'arithmetic':arithmetic,'pdf_pages_rendered_and_inspected':4,'existing_monthly_pdf_verified':'six Sunday-first date rows','seo_output':'pass','core_freeze':'pass','publishing_regression':reg,'new_resource':'noindex; excluded from sitemap','remote_writes':'none','pending':['USA location/device top-ten verification','native phone/PDF annotation save-reopen','GA4 receipt','fresh GSC inspection','browser viewport rendering']}
(OUT/'validation.json').write_text(json.dumps(validation,indent=2))
ownership=[
 ('daily planner template','daily-planner-complete-guide','Evergreen daily method and actual generic daily PDF. Hourly page owns fine time slots; dated layout pages keep dated/layout intent.'),
 ('monthly planner template','monthly-planner-free-templates','Evergreen undated monthly resource; 2026 month pages remain for dated queries.'),
 ('study schedule template','exam-study-schedule-template','Study-session timing; the new guide owns concepts and practice, not the schedule.'),
 ('adhd to do list template','adhd-planner-for-adults','Use existing adult planning sheet and concrete next actions; no general to-do or treatment claims.'),
 ('free printable homeschool attendance sheets','homeschool-attendance-tracker','Reassign from schedule to current attendance article/tool. Multi-age schedule remains about support rotations.'),
 ('content marketing plan template','content-marketing-plan-template-capacity','Reassign generic strategy/capacity query from the clothing calendar. Clothing page retains product-specific post planning.'),
 ('study guide template','/tools/study-guide-template/','Proposed new resource: blank + filled PDF and editable text; distinct from time allocation and coursework deadlines.')]
research='''# Day 4 research and ownership\n\nPrepared October 23, 2026. This is a draft-only implementation based on the saved seven-day plan. No push, PR, merge, deployment or indexing request was made.\n\nThe plan's reported keyword metrics are historical. The attached 2100 CSV reports different KD values for daily planner template (36), study schedule template (28) and adhd to do list template (12), at the same volumes of 2900, 480 and 170. These exports are not a current USA ranking verification; do not silently merge snapshots or fabricate missing metrics.\n\nPublic search discovery was checked with both search services. Country/device positions and ranking causes were not verified. The following competitor features suggest intent fit; they do not prove why Google ranks a page. No new keyword targets were imported from these pages.\n\n| Public comparator | Observed feature | Draft response |\n|---|---|---|\n| freelydocs.com/templates/study-guide-template/ | Direct document copy/download choices | Label actual PDF/text formats at the top |\n| lessonhq.us/templates/study-guide | Direct blank files, preview and self-quiz structure | Blank and filled PDF, actual preview and checked questions |\n| ugc.studypdf.net/templates/study-guide-template | One-page concepts and question slots | One objective per page with a correction field |\n| studigems.com/blog/study-guide-template | Format choices and generated-guide pathway | Original worked example without generation claims |\n| scholarsail.com/tools/text-editor/study-guide | Editable document workflow | Real editable text download, with limits |\n| thegoodocs.com/freebies/study-notes/ | Multiple document layouts and formats | Offer only files actually supplied |\n| canva.com/collection/study/ | Study materials linked across formats | Distinguish guide, schedule and tracker roles |\n| mountainheightsacademy.org/blog/how-to-make-a-study-guide-template-to-ace-your-exams | Objectives, own explanation and gaps | Link each weak area to a next practice task |\n| airtable.com/templates/study-guides/expgvEEs9ehSRRYrR | Workspace template and views | Explain that downloads do not synchronize |\n| teacherspayteachers.com/Product/Study-Guide-Template-5684928 | A free teacher resource listing | Direct downloads with no signup in the draft |\n\nOther relevant comparisons included Smartsheet daily templates, Canva monthly templates, ADHDAIPlaybook to-do layouts, and ClickUp's clothing calendar. Cornell's current Learning Strategies Center page was read for the limited explanation of retrieval and spaced practice. The new page links directly to that source; it does not prescribe study intervals or promise outcomes.\n\n## Release gates\n\nKeep the new resource noindex while draft. Before a later authorized release: review latest main, recheck dates/links, set real modification/publication dates, remove only the new draft banner/noindex, rebuild, pass current-head CI, then verify live bytes and add the new URL to the existing URL register. Until Google evidence exists, its indexing status stays Unverified. Native-device and analytics backend checks remain separate.\n'''
(OUT/'research-and-ownership.md').write_text(research+'\n## Ownership decisions\n\n'+'\n'.join(f'- {k}: {slug}. {why}' for k,slug,why in ownership))
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
css='''*{box-sizing:border-box}body{margin:0;background:#eff3f5;color:#203d4a;font:17px/1.75 system-ui,sans-serif}body>header{background:#203d4a;color:white;padding:36px max(20px,calc((100vw - 1060px)/2))}main{max-width:1120px;margin:auto;padding:24px}.panel,.page{background:white;border:1px solid #d4dfe3;border-radius:10px;padding:28px;margin-bottom:26px}h1{font-size:30px;line-height:1.25}h2{font-size:24px;line-height:1.4;margin-top:28px}h3{font-size:20px}a{color:#14677f;overflow-wrap:anywhere}.eyebrow,.small{font-size:13px}.eyebrow{font-weight:750;letter-spacing:1px}.status{background:#fff0c9;padding:15px}.copy{border-top:1px solid #d4dfe3;padding-top:18px}.copy article{margin:0;padding:0;max-width:none}.copy section[id]{scroll-margin-top:20px}.copy section[id*="daily-template"],.copy section[id*="place-monthly"],.copy section[id*="connect-study"],.copy section[id*="write-a-small"],.copy section[id*="prepare-support"],.copy section[id*="check-clothing"]{background:#f1f8f5;padding:18px}.table-wrap{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.6}th,td{border:1px solid #d4dfe3;padding:10px;vertical-align:top;text-align:left}th{background:#edf3f5}img{max-width:100%;height:auto}figure{margin:20px 0}figure img{max-width:650px;width:100%;border:1px solid #d4dfe3}figcaption{font-size:13px}li{margin:6px 0}.downloads a{display:inline-block;padding:10px 14px;margin:5px;background:#203d4a;color:white;border-radius:6px}@media(max-width:650px){main{padding:12px}.page,.panel{padding:17px}h1{font-size:25px}.table-wrap table{min-width:600px}}@media print{body{background:white}body>header{background:white;color:#203d4a}.page{break-before:page;border:0}}'''
downloadlinks=''.join(f'<a href="{enc(p)}" download="{Path(p).name}">{html.escape(Path(p).name)}</a>' for p in newfiles)
owners=''.join(f'<tr><td>{html.escape(k)}</td><td>{html.escape(slug)}</td><td>{html.escape(why)}</td></tr>' for k,slug,why in ownership)
review='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NexalyPlanner Day 4 Draft Review</title><style>'+css+'</style><header><p class="eyebrow">NEXALYPLANNER · DAY 4</p><h1>Student and planner content draft review</h1><p>Prepared October 23, 2026 · Original plan labels this Day 4 · USA primary audience</p></header><main><section class="panel" id="overview"><p class="status"><strong>DRAFT ONLY.</strong> Six guide revisions and one proposed resource. Nothing pushed, merged or deployed. Draft URLs are review targets, not live publication claims.</p><p>Read the complete seven drafts below. New content sections are shaded. The download buttons in this review embed the actual new PDF/text files; links between these seven drafts stay in this review. Other links open existing public pages. Site navigation, decorative covers and app controls are omitted from this reading copy.</p><div class="table-wrap"><table><thead><tr><th>Draft</th><th>Work completed</th><th>Approx. main-content words</th></tr></thead><tbody>'+''.join(summary)+'</tbody></table></div><h2>Download the draft resources</h2><div class="downloads">'+downloadlinks+'</div><h2>Keyword ownership and overlap decisions</h2><div class="table-wrap"><table><thead><tr><th>Agreed query</th><th>Owner</th><th>Decision</th></tr></thead><tbody>'+owners+'</tbody></table></div><h2>Validation and limits</h2><p>Seven pages: local links, unique IDs, one H1 and unchanged existing script behavior pass. Eight numerical checks pass using exact fraction arithmetic where needed. Both two-page PDF packs were rendered and visually inspected. Existing monthly PDF has six calendar rows. Publishing regression, generated SEO and core freeze checks pass.</p><p>The new study-guide page is noindex and excluded from the draft sitemap. Existing page dates remain historical until an authorized release. Public competitor research is format/intent discovery, not a verified USA top-ten report or proof of ranking causes. Physical phone/PDF annotation save-reopen, browser viewport rendering, GA4 receipt and fresh GSC checks remain unverified.</p></section>'+''.join(panels)+'</main></html>'
name='NexalyPlanner-Day-4-Content-Draft-Review-2026-10-23.html';(OUT/name).write_text(review)
patch=subprocess.check_output(['git','diff','--binary','HEAD'],cwd=ROOT);(OUT/'changes.patch').write_bytes(patch)
changed=subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=ROOT,text=True).splitlines()
newpaths=[str(p.relative_to(ROOT)) for p in (ROOT/'docs/editorial/day4-oct23').glob('*') if p.is_file()]+newfiles+['tools/study-guide-template/index.html','assets/img/resource-previews/study-guide-template.webp','assets/img/resource-previews/daily-planner-template.webp']
sources=sorted(set(changed+newpaths));manifest=[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in sources]
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2))
(OUT/'README.md').write_text('# Day 4 draft packet\n\nOpen '+name+' for all seven reading drafts and embedded PDF/text downloads. New work is draft only. Source files and changes.patch are for review; do not deploy this packet without a new release review. See validation.json and research-and-ownership.md for evidence, keyword ownership and pending gates.\n')
with zipfile.ZipFile(OUT/'NexalyPlanner-Day-4-Content-Drafts-2026-10-23.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in [OUT/name,OUT/'README.md',OUT/'content-register.json',OUT/'validation.json',OUT/'research-and-ownership.md',OUT/'source-manifest.json',OUT/'changes.patch']:z.write(p,p.name)
 for p in sources:z.write(ROOT/p,'source/'+p)
 for p in (OUT/'pdf-renders').glob('*.png'):z.write(p,'qa-previews/'+p.name)
print(json.dumps({'review':str(OUT/name),'source_files':len(sources),'status':'draft only','pages':len(rows),'arithmetic_checks':len(arithmetic)},indent=2))
