from pathlib import Path
import re,importlib.util
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parent
p=R/'journal/planners-2026-full-comparison/index.html';s=p.read_text()
changes={
'and a digital planner when you want tablet handwriting or file storage.':'then choose paper, a printable PDF or an editable browser planner as the medium.',
'or a digital planner for tablet handwriting and file storage.':'or a digital format suited to typed browser entries or PDF annotation.',
'<td>Digital planner</td><td>Tablet users and searchable files</td><td>Linked or repeated daily, weekly, and monthly pages</td><td>Easy to duplicate, annotate, and store</td><td>Requires a compatible app or PDF workflow</td>':'<td>Digital format</td><td>Typed planning or tablet annotation, depending on the file</td><td>Browser fields, app views or PDF pages</td><td>Editable entries or reusable pages, depending on the product</td><td>Check exact file type, saving and backup; a browser planner is not automatically a handwriting PDF</td>',
'Neither is automatically better. Digital planners support tablet handwriting and file storage; paper planners are easy to open and need no device.':'Neither is automatically better. PDF planners may support handwriting in a compatible annotation app; browser planners typically use typed fields and product-specific saving. Paper planners are easy to open and need no device.'}
for old,new in changes.items():
 if old not in s: print('MISSING exact edit',old[:80])
 else:s=s.replace(old,new,1)
s=re.sub(r'("dateModified":\s*")2026-10-24',r'\g<1>2026-11-04',s)
s=s.replace('property="article:modified_time" content="2026-10-24"','property="article:modified_time" content="2026-11-04"')
s=s.replace('<time datetime="2026-10-24">October 24, 2026</time>','<time datetime="2026-11-04">November 4, 2026</time>')
p.write_text(s)
# Add discoverable cards to existing categories without replacing prior directory content.
p=R/'tools/index.html';s=p.read_text()
for category,slug,title,desc,formats in [('daily','adhd-cleaning-planner','ADHD Cleaning Planner','Small cleaning actions with flexible days, estimated minutes and planned, done or skipped status.','PDF · CSV · JSON'),('business','business-plan-cover-page','Business Plan Cover Page','Create a cover with company, author, version and a fixed issue date.','PDF · HTML · JSON')]:
 # Identify the actual category section by ID, retaining its existing search controls.
 ids=re.findall(r'<section class="tool-category" id="([^"]+)"',s)
 if category not in ids: category='personal' if 'personal' in ids else ids[0]
 start=s.index(f'<section class="tool-category" id="{category}"');end=s.index('</section>',start)
 chunk=s[start:end]
 card=f'<article class="directory-tool theme-card theme-teal" data-category="{category}" data-latest="true" data-search="{title} {desc}"><div class="library-card-body"><p class="library-card-meta"><span>Free resource</span><span class="library-new">Latest addition</span></p><h3><a href="/tools/{slug}/">{title}</a></h3><p class="library-card-description">{desc}</p><div class="library-card-footer"><a class="library-card-link" href="/tools/{slug}/">Open free resource <span aria-hidden="true">↗</span></a><span class="library-card-formats">{formats}</span></div></div></article>'
 if '/tools/'+slug+'/' not in chunk:
  at=chunk.rfind('</div>');chunk=chunk[:at]+card+chunk[at:];s=s[:start]+chunk+s[end:]
 # Recount category cards and visible count (client JS handles filter counts).
 start=s.index(f'<section class="tool-category" id="{category}"');end=s.index('</section>',start);chunk=s[start:end];count=chunk.count('class="directory-tool ')
 chunk=re.sub(r'data-visible-count="\d+"',f'data-visible-count="{count}"',chunk);chunk=re.sub(r'(<p class="category-count">)\d+ planners',rf'\g<1>{count} planners',chunk);s=s[:start]+chunk+s[end:]
p.write_text(s)
# Add current feature JS/CSS to generator's cache hashing without changing behavior.
p=R/'scripts/seo-build.py';s=p.read_text();needle="for tool_name in ('small-tools-models.js',";assert needle in s;s=s.replace(needle,"for tool_name in ('day1-planning-tools.js',",1) if False else s
# New scoped files have explicit date cache tokens; existing cache pipeline remains unchanged.
# Add this release's meaningful UI test to required CI.
p=R/'.github/workflows/technical-seo.yml';s=p.read_text();needle='          NEXALY_JSDOM_PATH="$RUNNER_TEMP/nexaly-ui-tests/node_modules/jsdom" node scripts/test-business-summary-copy.cjs';assert needle in s;s=s.replace(needle,needle+'\n          NEXALY_JSDOM_PATH="$RUNNER_TEMP/nexaly-ui-tests/node_modules/jsdom" node scripts/test-day1-tools.cjs');p.write_text(s)
