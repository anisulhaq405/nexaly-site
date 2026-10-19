#!/usr/bin/env python3
"""Build this original release; deliberately leaves protected storefront code alone."""
import html,json,re,subprocess,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CONFIGS=json.loads((ROOT/'assets/js/keyword-workflows-configs.json').read_text())
ARTICLES=json.loads((ROOT/'docs/editorial/oct13/articles.json').read_text())
BY_KIND={c['kind']:c for c in CONFIGS}
DATE='2026-10-13';SITE='https://nexalyplanner.com'
def esc(s):return html.escape(str(s),quote=True)
def link(route,label):return f'<a href="{route}">{esc(label)}</a>'
OPTIMIZATION=json.loads((ROOT/'docs/editorial/oct13/optimization.json').read_text())
def page_label(route):
 text=(ROOT/route.strip('/')/'index.html').read_text()
 return html.unescape(re.sub('<[^>]+>', '', re.search(r'<h1\b[^>]*>(.*?)</h1>',text,re.S)[1])).strip()
def next_steps(kind, article=False):
 if kind not in OPTIMIZATION:return ''
 _,_,related,heading,paragraph=OPTIMIZATION[kind]
 level='h2' if article else 'h3'
 output=('<'+level+'>'+esc(heading)+'</'+level+'><p>'+esc(paragraph)+'</p>') if heading else ''
 output+='<'+level+'>Choose your next planning step</'+level+'><ul>'
 for slug,label,reason in related:
  output+='<li>'+link('/tools/'+slug+'/',label)+': '+esc(reason)+'</li>'
 return output+'</ul>'
def contextual_text(text):
 output=esc(text)
 for phrase,slug in [('maintenance-due planner','equipment-maintenance-due-planner'),('invoice collection schedule','invoice-collection-schedule'),('publishing checklist','content-publishing-checklist')]:
  output=output.replace(phrase,link('/tools/'+slug+'/',phrase),1)
 return output
tool_base=(ROOT/'tools/content-publishing-checklist/index.html').read_text()
HEADER=re.search(r'<header class="nav">.*?</header>',tool_base,re.S)[0]
FOOTER=re.search(r'<footer.*?</footer>',tool_base,re.S)[0]
SAVE=re.search(r'<section class="tool-panel no-print"><h2>Save or download.*?</section>',tool_base,re.S)[0]
STYLE='<link rel="stylesheet" href="/assets/css/style.css"><link rel="stylesheet" href="/assets/css/free-tools.css"><link rel="stylesheet" href="/assets/css/small-tools.css"><link rel="stylesheet" href="/assets/css/keyword-workflows.css"><link rel="icon" href="/assets/img/logo-mark.png">'
def head(title,desc,route,image,article=False):
 return f'<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{SITE+route}"><meta property="og:url" content="{SITE+route}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="{SITE+image}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{SITE+image}"><meta property="article:modified_time" content="{DATE}">'+(f'<meta property="article:published_time" content="{DATE}"><meta property="og:type" content="article">' if article else '')+STYLE
def wrapclose(scripts=''):return '</main>'+FOOTER+'<div id="toast" class="toast" role="status"></div><script src="/assets/js/main.js" defer></script>'+scripts+('<script src="/assets/js/free-planner-tables.js" defer></script>' if 'small-tools-ui.js' in scripts else '')+'</body></html>\n'
node="const a=require('./assets/js/keyword-workflows-models.js');console.log(JSON.stringify(a.configs.filter(c=>c.theme.startsWith('workflow-')).map(c=>{const s=structuredClone(c.sample);s.rows.forEach((r,i)=>r.id='row-'+i);return {kind:c.kind,result:a.evaluate(c.slug,s)};})));"
RESULTS={r['kind']:r['result'] for r in json.loads(subprocess.check_output(['node','-e',node],cwd=ROOT))}
def value(v):
 if isinstance(v,dict) and 'money'in v:return ('-$' if v['money']<0 else '$')+f"{abs(v['money'])/100:,.2f}"
 return str(v)
def table(headers,rows):return '<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+esc(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(value(v))+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
for c in CONFIGS:
 kind=c['kind'];article=next((a for a in ARTICLES if a['tool']==kind),None)
 route='/tools/'+c['slug']+'/';image='/assets/img/workflows/'+c['slug']+'-cover-v3.webp'
 desc={'variance': 'Reconcile one period of forecast and actual cash. Calculate the cash bridge, record causes and follow-up owners, then save or export your report.', 'budget': 'Compare budget and actual revenue, variable costs and fixed costs. Calculate monthly variances and assign review owners with a free browser worksheet.', 'builder': 'Build a daily or weekly writing page with your own hours and sections. Choose Letter, A4 or A5, preview the planner and print or save PDF.', 'teacher': 'Track monthly lessons, preparation due dates, material tasks and owners. Review overdue preparation in a free editable teacher worksheet.', 'production': 'Check content production hours against each working day. Find overloaded dates, keep review owners visible and export a local capacity report.', 'campaign': 'Allocate a campaign test budget and compare planned and actual spend. Calculate cost per entered inquiry or customer without automatic attribution.', 'lean': 'Create a compact customer, problem, offer and economics summary with an editable assumption test log. Save a backup or print the plan.', 'projections': 'Model consecutive service-business months with billed revenue, incurred expense and cash movements. Keep principal, funding and withdrawals distinct.', 'coffee': 'Calculate a coffee shop daily operating remainder from orders, staffing and entered costs. Compare a slower day with unchanged staffing assumptions.', 'construction': 'Schedule project deposits, materials and labor payments by date. Compare all entered receipts with confirmed receipts only and inspect low cash points.', 'trucking': 'Calculate a trip cost using loaded and empty miles, fuel and your maintenance allowance. Compare total-mile economics and entered payment dates.'}[kind]
 schema={'@context':'https://schema.org','@type':'WebApplication','name':c['name'],'url':SITE+route,'image':SITE+image,'applicationCategory':'ProductivityApplication' if kind in ['builder','teacher'] else 'BusinessApplication','operatingSystem':'Web browser','isAccessibleForFree':True,'offers':{'@type':'Offer','price':'0','priceCurrency':'USD'},'featureList':['Editable worksheet','Device save and restore','JSON backup','CSV report','Browser print and PDF']}
 source=head('Free '+c['name']+' | NexalyPlanner',desc,route,image)+f'<script type="application/ld+json">{json.dumps(schema)}</script></head><body>'+HEADER
 source+=f'<main class="free-tools new-tool workflow-tool theme-{c["theme"]}" style="--accent:{c["color"]};--soft:{c["color"]}12;--canvas:#f5f7f8;--ink:#19303d" data-tool="{c["slug"]}"><nav aria-label="Breadcrumb">{link("/","Home")} / {link("/tools/","Free planners")} / {esc(c["name"])}</nav><div class="tool-intro"><p class="eyebrow">FREE · NO ACCOUNT NEEDED</p><h1>{esc(c["name"])}</h1><p>{esc(desc)}</p><div class="tool-actions"><a class="tool-cta" href="#worksheet">Use free planner</a><a href="#tool-guide">Read the complete guide</a></div><p class="hint">Enter your own assumptions, calculate and keep a backup. Load the fictional example to see a filled-in report.</p></div><noscript><p>The interactive worksheet needs JavaScript. The input rules, formulas and fictional example below remain readable.</p></noscript>'
 source+='<section class="tool-panel tool-input" id="worksheet" aria-labelledby="settings-heading"><h2 id="settings-heading">Set up your worksheet</h2><div id="tool-settings" class="event-grid"></div><div class="tool-actions"><button id="tool-add" type="button">Add entry</button><button id="tool-sample" type="button" class="secondary">Load fictional example</button></div><div id="tool-rows"></div><button id="tool-calculate" type="button">Calculate / review results</button><p id="tool-message" role="status" aria-live="polite" tabindex="-1"></p></section><section class="tool-panel tool-report" aria-labelledby="report-heading"><h2 id="report-heading">Your report</h2><div id="tool-results" aria-live="polite"><p>Enter your details, then calculate to review results.</p></div></section>'+SAVE
 source+='<section class="tool-panel no-print tool-guide" id="tool-guide"><h2>'+esc(c['name'])+': complete guide</h2><nav class="tool-categories" aria-label="On this page"><a href="#features">Features</a><a href="#inputs">Inputs</a><a href="#calculation">Calculation</a><a href="#example">Worked example</a><a href="#saving">Saving</a><a href="#questions">Questions</a></nav>'
 if kind in ['trucking','construction']:
  preview='/assets/img/workflows/'+c['slug']+'.webp'
  source+=f'<figure class="tool-preview"><img src="{preview}" width="1200" height="800" alt="{esc(c["name"])}: calculated fictional example report" loading="lazy" decoding="async"><figcaption>Calculated fictional example. Load the fictional example in the planner above to reproduce this report, then enter your own assumptions.</figcaption></figure>'
 else:
  source+=f'<figure class="tool-preview"><img src="{image}" width="1200" height="800" alt="{esc(c["name"])} conceptual planning illustration" loading="lazy" decoding="async"><figcaption>Conceptual illustration of this planning topic. Use the interactive planner above for your own calculations.</figcaption></figure>'
 source+=f'<h3 id="features">What this worksheet does</h3><p>{esc(c["reportNote"])}</p><p>Keep up to {c["maxRows"]} editable entries. The worksheet runs in your browser and does not send its entries to another service. The calculations use the inputs you provide; currency selectors label amounts without conversion.</p><h3>How to use it</h3><ol><li>Set a descriptive worksheet name and complete the settings for your planning period.</li><li>Add one entry per record. Use consistent units and keep the evidence behind your assumptions.</li><li>Calculate and inspect the report, including any review notes. Change an input and calculate again to replace the old result.</li><li>Save an editable backup before changing a scenario. Use the related guide below for the wider operating workflow.</li></ol>'
 fieldRows=[]
 for f in c['fields']+c['rowFields']:
  rule='Optional.' if f.get('optional') else 'Required for calculation.'
  if f['type']=='number':rule+=f' {f["min"]}–{f["max"]}; '+('whole numbers.' if f.get('integer') else 'up to two decimal places.')
  elif f['type']=='select':rule+=' Choose '+', '.join(f['options'])+'.'
  elif f['type']=='date':rule+=' Valid calendar date, 1900–2200; no timezone shift.'
  else:rule+=f' Up to {f["maxLength"]} characters.'
  fieldRows.append([f['label'],rule])
 source+='<h3 id="inputs">Inputs and units</h3>'+table(['Field','Rule'],fieldRows)+'<h3 id="calculation">Calculation and scope</h3><p>'+esc(c['reportNote'])+'</p>'
 if kind in ['coffee','trucking']:source+='<p>Unit-based cost components are rounded to cents individually, with half-cent ties rounded up. For example, 2.01 hours at $0.50 per hour produces a rounded $1.01 cost.</p>'
 result=RESULTS[kind];source+='<h3 id="example">Fictional worked example</h3><p>Load the fictional example to reproduce this report. The sample is an original illustration, not a customer result or a market benchmark. The dollar figures below use USD.</p>'+table(['Result','Sample value'],[[m['label'],{'money':m['value']} if m['format']=='money' else m['value']] for m in result['metrics']])
 source+=table(result['headers'],result['rows'])
 for x in result['extra']:source+='<h4>'+esc(x['title'])+'</h4>'+table(x['headers'],x['rows'])
 source+='<h3 id="saving">Save, restore and export</h3><p>Save on this device writes an explicit save to this browser; it does not download a file or sync across devices. Clearing browser storage can remove it. Download backup keeps an editable JSON file for this exact worksheet. Import previews the backup before replacing current entries; save again if you want to replace the device save. CSV contains the calculated report, not an editable import format. Print / Save PDF opens the browser print dialog; choose Save as PDF where available.</p><h3 id="questions">Questions and limits</h3><h4>Is the example my result?</h4><p>No. It is fictional data. Replace its assumptions with your own records, then calculate again.</p><h4>Does saving share my worksheet?</h4><p>No. Device saves belong to this browser. Move an editable worksheet with its JSON backup and keep sensitive information out of a shared device.</p><h4>Does a report establish that my plan is correct?</h4><p>No. Arithmetic can be consistent while the input assumptions are wrong. Keep evidence, review the scope described above and check any decisions against your real records.</p>'
 parent='one-page-marketing-plan-example' if kind=='campaign' else article['parent'];product='content-marketing-planner' if kind=='campaign' else article['product']
 source+='<h3>Continue the workflow</h3><p>'+link('/journal/'+parent+'/',page_label('/journal/'+parent+'/'))+'. '+(link('/journal/'+article['slug']+'/',article['title'])+'.' if article else 'The existing marketing guide explains the offer, campaign and review process behind this budget.')+'</p></section>'
 source+='<section class="tool-panel no-print">'+next_steps(kind)+'</section>'
 source+='<section class="tool-panel no-print tool-upgrade"><h2>'+esc(OPTIMIZATION[kind][0])+'</h2><p>'+esc(OPTIMIZATION[kind][1])+' '+link('/planners/'+product+'/',page_label('/planners/'+product+'/'))+'. Paid products are separate; the free JSON backup is not a paid-product import file.</p></section>'
 guide_slug='small-business-planner' if product=='small-business-planner-2026-2028' else product
 guide_route='/guides/'+guide_slug+'/'
 if (ROOT/guide_route.strip('/')/'index.html').exists():
  extra='<p>Before choosing the paid product, '+link(guide_route,'read '+page_label(guide_route))+' to check its workflow and supported features.</p>'
  source=source[:-len('</section>')]+extra+'</section>'

 scripts='<script src="/assets/js/small-tools-models.js" defer></script><script src="/assets/js/keyword-workflows-models.js" defer></script><script src="/assets/js/small-tools-ui.js" defer></script>'
 if kind=='builder':scripts+='<script src="/assets/js/keyword-workflows-preview.js" defer></script>'
 p=ROOT/'tools'/c['slug']/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(source+wrapclose(scripts))
for a in ARTICLES:
 c=BY_KIND.get(a['tool']);color=c['color'] if c else ('#725b6d' if 'interior' in a['slug'] else '#285373')
 route='/journal/'+a['slug']+'/';image='/assets/img/workflows/'+a['slug']+'-cover-v3.webp'
 source=head(a['title'],a['description'],route,image,True)+'</head><body>'+HEADER+f'<main class="workflow-article" style="--accent:{color};--soft:{color}12"><p>{link("/journal/","Back to Journal")}</p><article><p class="eyebrow">PRACTICAL PLANNING GUIDE</p><h1>{esc(a["title"])}</h1><p class="metadata">By NexalyPlanner · Published October 13, 2026 · Fictional worked examples</p><figure class="article-feature"><img src="{image}" width="1200" height="800" alt="{esc(a["title"])} editorial planning illustration" fetchpriority="high" decoding="async"><figcaption>Conceptual editorial illustration of this planning topic.</figcaption></figure><p>{esc(a["intro"])}</p>'
 source+='<nav class="toc" aria-label="In this guide">'+''.join(link('#section-'+str(i+1),heading) for i,(heading,_) in enumerate(a['sections']))+'</nav>'
 if c:source+='<div class="workflow-callout"><p>'+link('/tools/'+c['slug']+'/','Use the free '+c['name'])+' to enter your own assumptions, calculate the report and keep an editable backup. No account is needed.</p></div>'
 else:
  tools=[('fixed-fee-scope-change-planner','fixed-fee scope-change planner'),('freelancer-weekly-capacity-planner','weekly capacity planner')] if 'interior' in a['slug'] else [('retainer-overage-calculator','retainer-overage calculator'),('freelancer-weekly-capacity-planner','weekly capacity planner'),('invoice-collection-schedule','invoice collection schedule')]
  source+='<div class="workflow-callout"><p>Use the existing '+', '.join(link('/tools/'+slug+'/',label) for slug,label in tools)+' for the distinct calculations in this example.</p></div>'
 for i,(heading,paragraph) in enumerate(a['sections']):
  # Paragraph breaks follow concrete ideas, without automatic filler.
  sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',paragraph);mid=len(sentences)//2
  parts=[' '.join(sentences[:mid]),' '.join(sentences[mid:])] if len(sentences)>5 else [paragraph]
  source+='<section id="section-'+str(i+1)+'"><h2>'+esc(heading)+'</h2>'+''.join('<p>'+contextual_text(part)+'</p>' for part in parts)+'</section>'
 if c and c['kind'] not in ['builder','lean']:
  source+='<h2>Reproduce the worksheet example</h2><p>The sample button loads the following results from the assumptions described in this guide. Change one input at a time to inspect its effect.</p>'+table(['Result','Fictional sample'],[[m['label'],{'money':m['value']} if m['format']=='money' else m['value']] for m in RESULTS[c['kind']]['metrics']])
 source+=next_steps(a['tool'],article=True)
 source+='<h2>Keep a version you can review</h2><p>Save on this device keeps the worksheet in the current browser. Download a JSON backup for an editable copy before changing assumptions. CSV is a calculated report; Print / Save PDF produces a browser print copy. Device saving does not provide cloud synchronization. A static PDF needs its own annotation and backup workflow.</p>'
 if a['tool']in ['variance','budget','projections','coffee','construction']:
  source+='<h2>Reference and example scope</h2><p>'+link('https://business.gov.au/finance/financial-tools-and-templates/create-a-budget','business.gov.au budgeting guidance')+' explains the role of comparing a budget with actual results. The numerical examples and worksheet scope here are NexalyPlanner originals; they are not official accounting templates.</p>'
 elif a['tool']=='lean' or not a['tool'] or a['tool']=='trucking':
  source+='<h2>Reference and example scope</h2><p>The '+link('https://legacy.sba.gov/business-guide/plan-your-business/write-your-business-plan','SBA business-plan guide')+' distinguishes lean and traditional formats. This article adds an original operating example and does not replace the wider plan or supporting evidence a reader may request.</p>'
 source+='<section class="workflow-callout"><h2>Connect this task to your existing plan</h2><p>'+link('/journal/'+a['parent']+'/',page_label('/journal/'+a['parent']+'/'))+' for the wider workflow. '+link('/planners/'+a['product']+'/',page_label('/planners/'+a['product']+'/'))+' for documented features and compatibility. Paid products are separate from these free worksheets.</p></section></article>'
 p=ROOT/'journal'/a['slug']/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(source+wrapclose())

# Directory: extend the existing categories and controls, not the store layout.
p=ROOT/'tools/index.html';s=p.read_text()
# Upsert this batch so reproducing it does not create duplicate directory cards.
own_routes={'href=\"/tools/'+c['slug']+'/\"' for c in CONFIGS}
s=re.sub(r'<article class=\"directory-tool\b[^>]*>.*?</article>',lambda match:'' if any(route in match[0] for route in own_routes) else match[0],s,flags=re.S)
s=s.replace('data-latest=\"true\"','data-latest=\"false\"').replace('<span class=\"library-new\">Latest addition</span>','')
categories={'cashflow':'Cashflow & renewals','personal':'Personal planning','homeschool':'Homeschool & learning','content':'Content & publishing','agency':'Agency & freelance','operations':'Operations & equipment'}
for category in categories:
 pattern=r'(<section class="tool-category" id="'+category+r'".*?</section>)';match=re.search(pattern,s,re.S);section=match[0];cards=''
 for c in CONFIGS:
  if c['category']!=category:continue
  route='/tools/'+c['slug']+'/';image='/assets/img/workflows/'+c['slug']+'-cover-v3.webp'
  cards+=f'<article class="directory-tool theme-card" style="--accent:{c["color"]}" data-category="{category}" data-latest="true" data-search="{esc(c["name"]+" "+c["reportNote"])}"><a class="directory-preview" href="{route}" aria-label="Open {esc(c["name"])}"><img src="{image}" width="1200" height="800" alt="{esc(c["name"])} conceptual planning illustration" loading="lazy" decoding="async"></a><div class="library-card-body"><p class="library-card-meta"><span>{esc(categories[category])}</span><span class="library-new">Latest addition</span></p><h3>{link(route,c["name"])}</h3><p class="library-card-description">{esc(c["reportNote"].split(". ")[0]+".")}</p><div class="library-card-footer"><a class="library-card-link" href="{route}">Open free planner <span aria-hidden="true">↗</span></a><span class="library-card-formats">CSV · JSON · Print</span></div></div></article>'
 updated=section.replace('</div></section>',cards+'</div></section>');count=len(re.findall(r'class="directory-tool',updated));updated=re.sub(r'data-visible-count="\d+"',f'data-visible-count="{count}"',updated);updated=re.sub(r'(<p class="category-count">)\d+ planners',rf'\g<1>{count} planners',updated)
 s=s[:match.start()]+updated+s[match.end():]
s=s.replace('Use 24 free','Use 35 free').replace('<b>24</b> free planners','<b>35</b> free planners').replace('>24 planners</p>','>35 planners</p>').replace('All planners <span class="filter-count">24','All planners <span class="filter-count">35').replace('Latest additions <span class="filter-count">8','Latest additions <span class="filter-count">11')
for category in categories:
 count=len(re.findall(r'class="directory-tool[^>]*data-category="'+category+'"',s));s=re.sub(r'(data-filter="'+category+r'".*?<span class="filter-count">)\d+',rf'\g<1>{count}',s)
s=re.sub(r'<meta property="article:modified_time" content="[^"]+">',f'<meta property="article:modified_time" content="{DATE}">',s);p.write_text(s)
# Keep latest-filter wording independent of the number of added tools.
p=ROOT/'assets/js/tools-directory.js';p.write_text(p.read_text().replace('The latest eight additions to the collection.','The latest additions to the collection.'))

UPDATES={}
def add_update(slug,heading,body,section='journal'):
 p=ROOT/section/slug/'index.html';s=p.read_text();marker='oct13-workflow-'+hashlib.sha256((section+'/'+slug).encode()).hexdigest()[:8];addition=f'<section class="'+('tool-panel no-print tool-guide' if section=='tools' else 'related-guides')+'" id="'+marker+'"><h2>'+heading+'</h2>'+body+'</section>'
 s=re.sub(r'<section[^>]*id="'+re.escape(marker)+r'".*?</section>','',s,flags=re.S)
 anchor='</main>' if section=='tools' else '</article>'
 assert anchor in s,(slug,'missing anchor');s=s.replace(anchor,addition+anchor,1)
 if 'property="article:modified_time"'in s:s=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',rf'\g<1>{DATE}',s)
 else:s=s.replace('</head>',f'<meta property="article:modified_time" content="{DATE}"></head>',1)
 s=re.sub(r'("dateModified"\s*:\s*")[^"]+',rf'\g<1>{DATE}',s);p.write_text(s);UPDATES[section+'/'+slug]=heading
for parent in sorted(set(a['parent'] for a in ARTICLES)):
 items=[a for a in ARTICLES if a['parent']==parent]
 body='<p>The following focused workflows extend this guide without replacing its example:</p><ul>'
 for a in items:
  body+='<li>'+link('/journal/'+a['slug']+'/',a['title'])
  if a['tool']:body+='; '+link('/tools/'+BY_KIND[a['tool']]['slug']+'/','use the free '+BY_KIND[a['tool']]['name'])
  body+='.</li>'
 body+='</ul>';add_update(parent,'Put the next operating decision into a worksheet',body)
add_update('one-page-marketing-plan-example','Review a campaign against its actual test budget','<p>'+link('/tools/marketing-campaign-budget-planner/','Use the free Marketing Campaign Budget Planner')+' to allocate a test ceiling, compare planned and actual spending and calculate cost per entered inquiry or customer. Keep the attribution note with each channel; overlapping customer counts are not unique acquisitions. The worksheet does not infer revenue, ROI or publish the campaign.</p>')
add_update('daily-planner-2026-free-layouts','Make a daily page fit an overnight shift','<p>The existing PDF remains available above. If its hours do not fit your workday, '+link('/tools/printable-planner-builder/','build a daily printable planner with your own hours')+'. For example, 22:00 to 06:00 creates eight hourly slots with after-midnight labels. '+link('/journal/create-your-own-printable-planner/','Read the paper-size and print-preview walkthrough')+' before choosing Letter, A4 or A5.</p>')
add_update('weekly-planner-2026-free-templates','Print the week with the starting day you use','<p>Keep the existing weekly PDF for its simple blank layout. For a dated page with Monday or Sunday as the first day, '+link('/tools/printable-planner-builder/','use the printable planner builder')+'. Choose Weekly and a date within the week; the report derives the seven dates from your week-start setting. It creates a static writing page, not calendar synchronization.</p>')
add_update('monthly-planner-free-templates','Trace one monthly deadline into the week and day','<p>Keep the deadline in the monthly view and choose a next action in the '+link('/journal/weekly-planner-2026-free-templates/','weekly planner')+'. For a fictional October 30 presentation, set an October 23 draft review and an October 20 action to write the first outline. Put that action in the '+link('/journal/daily-planner-2026-free-layouts/','daily planning page')+' with a realistic work block. If the deadline changes, review its weekly milestone and daily action together rather than leaving three conflicting dates.</p>')
add_update('craft-fair-stock-reconciliation','Farmers market vendor example: stock, spoilage and selling costs','<p>This is an individual stall workflow, not a plan for operating an entire farmers market. In a fictional produce example, bring 100 packs, sell 70, give away 5, record 10 spoiled packs in the damaged/unusable field and count 15 usable returns: 100 − 70 − 5 − 10 = 15. At $6 average price, sales are $420. Enter $40 stall fees, $30 travel and $10 packaging as $80 event costs, giving $340 sales less entered event costs. This remainder is not profit: the crop/product cost and selling labor must be considered separately.</p><p>Write down selling and travel hours beside the event report. The '+link('https://www.extension.umd.edu/resource/booth-farmers-market-profit-or-loss','University of Maryland farmers-market cost example')+' is a reference for considering the wider cost scope; the figures here are original illustrations. Preserve a separate row when a different pack size or sale price needs its own stock tally.</p>',section='tools')
(ROOT/'docs/editorial/oct13/implementation-manifest.json').write_text(json.dumps(dict(date=DATE,tools=[c['slug'] for c in CONFIGS],articles=[a['slug'] for a in ARTICLES],existing_updates=UPDATES,unchanged_reviewed=['adhd-planner-for-adults','best-planner-app-for-ipad-2026','digital-planner-app-how-it-works','college-assignment-tracker','retail-store-business-plan-example'],held=['nonprofit','real-estate','sustainable-farm'],merged=['business-plan-sections','startup-business-plan']),indent=2)+'\n')
print(json.dumps({'new_tools':len(CONFIGS),'new_articles':len(ARTICLES),'existing_substantive_link_or_example_updates':len(UPDATES)},indent=2))
