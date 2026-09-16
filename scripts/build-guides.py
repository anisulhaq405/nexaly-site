#!/usr/bin/env python3
"""Build NexalyPlanner's first-party product guides from reviewed product facts."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / 'journal/adhd-planner-for-adults/index.html').read_text()
NAV = SOURCE[SOURCE.index('<header class="nav">'):SOURCE.index('<header class="article-hero">')]
SHELL = SOURCE[SOURCE.index('<!-- ============ AUTH MODAL ============ -->'):]

GUIDES = [
    {
        'slug':'adhd-digital-planner',
        'title':'How to Use the ADHD Digital Planner | Nexaly Guide',
        'h1':'How to Use the ADHD Digital Planner',
        'description':'Set up the Nexaly ADHD Digital Planner, capture tasks, choose daily priorities, use focus tools, review progress and protect your offline records.',
        'product':'ADHD Digital Planner',
        'product_url':'/planners/adhd-digital-planner/',
        'image':'/images/products/adhd-digital-planner/03-dashboard.png',
        'image_alt':'Nexaly ADHD Digital Planner daily dashboard with main focus, top tasks and progress overview',
        'intro':'This guide explains the practical first-run setup for the Nexaly ADHD Digital Planner. You will open the downloaded HTML app, create a simple daily workflow, use the focus and reset tools, and make a backup before records become important.',
        'quick':'Start with the Brain Dump, choose one main focus and no more than three priority tasks, then place only time-sensitive work into time blocks. Review unfinished items before closing the planner.',
        'steps':[
            ('Open the downloaded planner','Extract the downloaded package if it arrives as a ZIP file. Keep all included files together, then open <strong>NexalyPlanner-ADHD-Planner.html</strong> in a current version of Chrome, Edge, Safari or Firefox. Bookmark the local file only after confirming it opens correctly.'),
            ('Set your preferences','Open the planner settings. Add the personal details you want displayed, choose a language, select one of the color themes and switch between light and dark mode. If you enable the optional password lock, store the password somewhere safe.'),
            ('Clear your head into the Brain Dump','Enter loose tasks and reminders without trying to organize each item immediately. The Brain Dump is the capture point; it prevents new thoughts from interrupting the task already in progress.'),
            ('Build today’s short plan','Move the most important items into the daily view. Set one main focus, choose the Top Three Tasks and add fixed commitments to time blocks. Leave open space for delays instead of filling every hour.'),
            ('Use the focus and recovery tools','Start a Pomodoro session when a task needs a defined work interval. Use the Hyperfocus Exit Plan when you need a stopping cue. If the day becomes overloaded, open Emergency Reset and work through the short restart checklist.'),
            ('Review routines and progress','Update morning or evening routines and the personal trackers you actually use. Weekly and monthly views help you move unfinished work, while progress analytics summarize the records you entered. These trackers are for personal organization, not diagnosis or treatment.'),
        ],
        'routine_rows':[
            ('Start of day','Check fixed commitments, choose one main focus and set three priorities.'),
            ('During the day','Capture interruptions in Brain Dump; use time blocks and the focus timer.'),
            ('End of day','Mark finished work and move only tasks that still matter.'),
            ('Weekly','Review goals, routines and the next seven days; create a fresh backup.'),
        ],
        'troubleshooting':[
            ('My records disappeared','Open the planner in the same browser and from the same saved HTML file. Browser storage is local; another browser or device will have a separate record set.'),
            ('The planner feels too busy','Use only the dashboard, Brain Dump and Top Three Tasks for the first week. Add routines, goals and trackers after the daily habit is stable.'),
            ('I need to move my data','Create a portable backup inside the planner before changing devices, browsers or files. Keep a dated copy outside the Downloads folder.'),
        ],
        'related':[
            ('ADHD planner for adults: build a reusable system','/journal/adhd-planner-for-adults/'),
            ('How offline digital planners store your data','/journal/offline-digital-planners-guide/'),
        ]
    },
    {
        'slug':'ai-student-planner',
        'title':'How to Use the AI Student Planner | Nexaly Guide',
        'h1':'How to Use the AI Student Planner',
        'description':'Set up subjects, timetables, assignments, exams, revision and study sessions in the Nexaly AI Student Planner with this practical user guide.',
        'product':'AI Student Planner',
        'product_url':'/planners/ai-student-planner/',
        'image':'/images/products/ai-student-planner/ai-student-planner-how-it-works.jpg',
        'image_alt':'Nexaly AI Student Planner setup workflow for profile, subjects, assignments, focus sessions and analytics',
        'intro':'Use this manual to turn the Nexaly AI Student Planner into one reliable academic workspace. The order matters: set up subjects first, add the timetable, enter real deadlines and then schedule revision around those commitments.',
        'quick':'Create your profile and subjects before adding assignments or exams. Enter due dates accurately, review the dashboard each day and record study sessions so the analytics reflect your actual work.',
        'steps':[
            ('Open the app and choose your starting point','Open <strong>AI-Student-Planner.html</strong> in a modern browser. Review the included demo data if you want to understand the screens, or begin with a clean workspace. Use the same browser for regular study planning.'),
            ('Create your profile and subjects','Add your student details, then create each current subject or course. Use names you recognize quickly. Complete this step before entering assignments so records can be assigned to the correct subject.'),
            ('Build the class timetable','Enter recurring classes, labs or study commitments in the timetable. Check that days and times match your real schedule. The daily dashboard can then show useful context alongside deadlines.'),
            ('Enter assignments and exams','Add each assignment with its subject, due date and priority. Add confirmed exam dates to the exam countdown. Break large projects into smaller tasks rather than storing the entire project as one item.'),
            ('Plan revision and focused study','Create revision sessions for the topics that need work. Use focus sessions to record concentrated study time, and add notes where they will be easy to retrieve during revision.'),
            ('Review grades and analytics','Record grades only after results are confirmed. The analytics summarize data you enter, including study time, streaks, subject distribution and weekly patterns. Use the patterns to adjust your schedule; they do not predict academic outcomes.'),
        ],
        'routine_rows':[
            ('After class','Add new assignments, exam dates and useful notes.'),
            ('Each morning','Check today’s classes, deadlines and planned study sessions.'),
            ('Study block','Start a focus session and record the subject or topic.'),
            ('Every week','Review overdue work, the next two weeks and revision coverage.'),
        ],
        'troubleshooting':[
            ('An assignment is missing from the right view','Check its subject, due date and completion status. An incorrect date or subject can place it somewhere unexpected.'),
            ('Analytics look incomplete','Analytics are based on saved planner records. Add or update study sessions, grades and tasks before interpreting the charts.'),
            ('I opened the app on another device','Offline data does not automatically sync. Use the same device or move a supported backup before relying on the new copy.'),
        ],
        'related':[
            ('Build a college assignment tracker','/journal/college-assignment-tracker/'),
            ('Create an exam study schedule','/journal/exam-study-schedule-template/'),
            ('Student planner setup guide','/journal/student-planner-guide/'),
        ]
    },
    {
        'slug':'small-business-planner',
        'title':'How to Use the Small Business Planner | Nexaly',
        'h1':'How to Use the Small Business Planner',
        'description':'Learn how to set up goals, finances, projects and operating reviews in the Nexaly Small Business Planner 2026–2028 offline browser app.',
        'product':'Small Business Planner 2026–2028',
        'product_url':'/planners/small-business-planner-2026-2028/',
        'image':'/images/products/small-business-planner-2026-2028/01-business-organizer.png',
        'image_alt':'Nexaly Small Business Planner organizer for goals, finances, projects and weekly business planning',
        'intro':'This manual shows how to set up the Nexaly Small Business Planner 2026–2028 without turning planning into extra administrative work. Begin with a small number of goals, connect them to current projects and review the financial records on a fixed schedule.',
        'quick':'Add your business details, define a few measurable goals, create only active projects and establish one weekly review. Enter financial figures consistently so summaries remain useful.',
        'steps':[
            ('Open the planner package','Extract <strong>NexalyPlanner-Business-Planner.zip</strong> and keep the app, helper files and installation guide together. Open the main HTML planner in a current browser and confirm the dashboard loads before entering business records.'),
            ('Add your business details','Complete the available business profile and display preferences. Choose the language, theme and currency that match the records you intend to enter. Keep naming consistent across customers, projects and financial entries.'),
            ('Set goals for the current period','Create a small set of specific goals for revenue, operations, marketing or delivery. Give each goal a target and review date. Avoid creating goals that have no next action or responsible project.'),
            ('Create active projects and tasks','Add the projects currently in progress, then break each into dated actions. Keep ideas and future projects separate from committed work so the weekly view remains realistic.'),
            ('Record financial activity consistently','Enter income, expenses or other supported business figures using one repeatable naming system. Review totals against your own source documents. This planner organizes information; it is not accounting, tax or legal advice.'),
            ('Run a weekly business review','Check overdue tasks, upcoming deadlines, project status and financial entries. Decide what to stop, continue or move. Print or save the supported view when you need a dated review copy.'),
        ],
        'routine_rows':[
            ('Daily','Update important tasks and record completed work.'),
            ('Weekly','Review projects, deadlines, cash records and next actions.'),
            ('Monthly','Compare goals with recorded results and adjust the next month.'),
            ('Quarterly','Archive completed work and create a fresh backup copy.'),
        ],
        'troubleshooting':[
            ('The dashboard does not reflect a recent entry','Save or complete the entry, then confirm its date and category. Summaries depend on correctly dated records.'),
            ('My plan contains too many priorities','Keep active goals and projects limited to work that can move during the current review period. Archive or defer the rest.'),
            ('I need records for an adviser','Use the available print or PDF option for a readable copy, then verify figures against original financial documents before sharing.'),
        ],
        'related':[
            ('Run a practical weekly business review','/journal/business-planner-weekly-review/'),
            ('Choose offline small business software','/journal/best-offline-small-business-software/'),
        ]
    },
    {
        'slug':'content-marketing-planner',
        'title':'How to Use the Content Marketing Planner | Nexaly',
        'h1':'How to Use the Content Marketing Planner',
        'description':'Set up brand details, content pillars, ideas, campaigns, a visual calendar and sales tracking in the Nexaly Content Marketing Planner.',
        'product':'Content Marketing Planner',
        'product_url':'/planners/content-marketing-planner/',
        'image':'/images/products/content-marketing-planner/content-marketing-planner-command-center-dashboard.jpg',
        'image_alt':'Nexaly Content Marketing Planner command center with content, engagement and sales tracking',
        'intro':'This guide explains how to set up the Nexaly Content Marketing Planner for a fashion or e-commerce brand. A useful workflow moves from brand settings to content pillars, ideas, campaigns, calendar dates and recorded results.',
        'quick':'Set your brand and currency first, define three to five content pillars, capture ideas in the Idea Bank and schedule only approved posts on the visual calendar. Record results after publishing.',
        'steps':[
            ('Open the planner and set your brand','Open <strong>Content-Marketing-Planner.html</strong> in a modern browser. Add your brand name, logo, colors, language and currency in settings. Choose light or dark mode and enable the optional password only if you can store it safely.'),
            ('Define content pillars','Create a short set of repeatable themes such as product education, customer questions, proof, behind the scenes or offers. Clear pillars make the Idea Bank and calendar easier to filter.'),
            ('Capture and qualify ideas','Add rough ideas to the Idea Bank before assigning publishing dates. Give useful ideas a format, platform, pillar and objective. The prompt library can help develop drafts, but review every output for accuracy and brand voice.'),
            ('Create drops and campaigns','Set up a campaign when several posts support the same launch, promotion or product drop. Record the offer, dates and products involved so calendar items can be reviewed in context.'),
            ('Schedule the visual calendar','Move approved content onto the calendar. Balance pillars and formats across the month, check for empty launch periods and avoid scheduling more content than the team can produce.'),
            ('Record engagement and sales','After publishing, enter the supported performance and sales figures consistently. Analytics summarize the information you record; they do not connect automatically to social platforms or stores.'),
        ],
        'routine_rows':[
            ('Any time','Capture ideas without assigning a date too early.'),
            ('Weekly','Approve content, assign owners and fill the next calendar window.'),
            ('After publishing','Record available engagement and sales results.'),
            ('Monthly','Review pillar balance, campaign results and content gaps.'),
        ],
        'troubleshooting':[
            ('The calendar feels overcrowded','Remove unapproved ideas from scheduled dates and keep them in the Idea Bank until production is realistic.'),
            ('Analytics do not match a social platform','The planner uses figures you enter; it does not automatically sync with external platforms. Check the date range and recorded values.'),
            ('A logo does not display as expected','Use a clear image file and reselect it in brand settings. Keep the original logo file with your planner package.'),
        ],
        'related':[
            ('Build a clothing brand content calendar','/journal/content-calendar-clothing-brand/'),
            ('Plan boutique social media posts','/journal/boutique-social-media-post-ideas/'),
            ('Create a small-business Black Friday plan','/journal/black-friday-marketing-plan-small-business/'),
        ]
    },
    {
        'slug':'digital-homeschool-planner',
        'title':'How to Use the Digital Homeschool Planner | Nexaly',
        'h1':'How to Use the Digital Homeschool Planner',
        'description':'Set up children, curriculum, lessons, assignments, attendance, grades and reports in the Nexaly Digital Homeschool Planner offline app.',
        'product':'Digital Homeschool Planner',
        'product_url':'/planners/digital-homeschool-planner/',
        'image':'/images/products/digital-homeschool-planner/digital-homeschool-planner-parent-command-center.jpg',
        'image_alt':'Nexaly Digital Homeschool Planner parent command center for multiple children and learning records',
        'intro':'This user manual shows how to set up the Nexaly Digital Homeschool Planner for multiple children. Create the family structure first, then connect curriculum, lessons, assignments, attendance and grades to the correct learner.',
        'quick':'Create a separate profile for each child before adding subjects or records. Build curriculum and lessons in that order, record attendance consistently and verify local reporting requirements yourself.',
        'steps':[
            ('Open the offline planner','Open <strong>Digital-Homeschool-Planner.html</strong> in a current browser. Keep the START-HERE and license files with the app. Use one primary browser and device unless you intentionally move a supported backup.'),
            ('Create each child profile','Add a separate learner profile for every child. Check names, grade or level information and goals before entering curriculum records. Selecting the right profile prevents records from being mixed.'),
            ('Build subjects and curriculum','Create the subjects taught to each learner, then organize the supported curriculum fields by unit, topic and objective. Start with the current term instead of entering an entire future year at once.'),
            ('Schedule lessons and assignments','Add lessons to daily, weekly or monthly calendar views. Create assignments and projects with clear due dates and priorities. Check the selected child and subject before saving each item.'),
            ('Record attendance, hours and grades','Use one consistent routine for attendance and learning hours. Enter assessment results in the gradebook after they are confirmed. Requirements vary by location; the planner does not determine whether a record meets state or local law.'),
            ('Review progress and prepare reports','Use progress views and analytics to find incomplete work or topics needing attention. Generate supported progress reports or transcripts from verified records, then print, save to PDF or export to CSV as available.'),
        ],
        'routine_rows':[
            ('Before the week','Schedule lessons and check materials for each child.'),
            ('Each school day','Record attendance, learning hours and completed work.'),
            ('After assessment','Enter the confirmed grade and any useful note.'),
            ('Monthly or term end','Review progress, verify records and save a backup.'),
        ],
        'troubleshooting':[
            ('A record appears under the wrong child','Open the record and check its learner profile and subject. Correct the assignment before producing reports.'),
            ('A transcript or report looks incomplete','Confirm attendance, grades, dates and child details are complete. Reports can only use saved planner information.'),
            ('I need official compliance advice','Check the current homeschool requirements for your state or jurisdiction. The planner helps organize records but does not provide legal advice or guarantee compliance.'),
        ],
        'related':[
            ('Plan homeschool for multiple children','/journal/homeschool-planner-multiple-children/'),
            ('Create a homeschool attendance routine','/journal/homeschool-attendance-tracker/'),
            ('Build a schedule for multiple ages','/journal/homeschool-schedule-multiple-ages/'),
        ]
    },
]

STYLE = """
:root{--guide-navy:#163044;--guide-teal:#167a74;--guide-ink:#203d4a;--guide-muted:#5b707a;--guide-line:#dce6e6;--guide-paper:#f5f8f7}
body{background:var(--guide-paper);color:var(--guide-ink)}.guide-hero{background:linear-gradient(135deg,#163044,#20596a);color:#fff;padding:52px max(24px,calc((100vw - 1080px)/2)) 46px}.guide-hero .kicker{font-size:.76rem;font-weight:800;letter-spacing:.16em;color:#aee7dc}.guide-hero h1{max-width:900px;margin:12px 0;font-size:clamp(2rem,5vw,3.25rem);line-height:1.1;color:#fff}.guide-hero p{max-width:800px;margin:0;color:#e1f0f1;font-size:1.08rem}.guide-main{max-width:1080px;margin:auto;padding:30px 24px 80px}.guide-crumbs{font-size:.9rem;color:var(--guide-muted);margin-bottom:20px}.guide-layout{display:grid;grid-template-columns:minmax(0,1fr) 270px;gap:30px;align-items:start}.guide-article{background:#fff;border:1px solid var(--guide-line);border-radius:16px;padding:38px 44px;font-size:1.05rem;line-height:1.72}.guide-article h2{font-size:1.75rem;line-height:1.25;margin:2.1rem 0 .7rem;color:var(--guide-navy)}.guide-article h3{font-size:1.2rem;margin:1.45rem 0 .45rem;color:var(--guide-navy)}.guide-article img{display:block;width:100%;height:auto;border:1px solid var(--guide-line);border-radius:12px}.guide-article figcaption{font-size:.82rem;color:var(--guide-muted);margin-top:8px}.guide-quick{background:#e9f4f1;border-left:4px solid var(--guide-teal);padding:18px 20px;border-radius:0 10px 10px 0}.guide-step{padding:4px 0 10px}.guide-step .number{display:inline-grid;place-items:center;width:30px;height:30px;margin-right:8px;border-radius:50%;background:var(--guide-teal);color:#fff;font-size:.86rem}.guide-table{overflow:auto;border:1px solid var(--guide-line);border-radius:10px}.guide-table table{width:100%;border-collapse:collapse;min-width:560px}.guide-table th,.guide-table td{text-align:left;padding:13px;border-bottom:1px solid var(--guide-line);vertical-align:top}.guide-table th{background:#e7f2ef;color:var(--guide-navy)}.guide-table tr:last-child td{border-bottom:0}.guide-aside{position:sticky;top:86px;background:#fff;border:1px solid var(--guide-line);border-radius:14px;padding:22px}.guide-aside h2{font-size:1.15rem;margin:0 0 12px}.guide-aside ol{margin:0;padding-left:20px;font-size:.92rem}.guide-aside a{color:#096d7d}.guide-cta,.guide-related{margin-top:30px;padding:24px;border-radius:12px}.guide-cta{background:var(--guide-navy);color:#fff}.guide-cta h2{color:#fff;margin-top:0}.guide-cta a{display:inline-block;background:#fff;color:var(--guide-navy);padding:11px 16px;border-radius:7px;font-weight:750;text-decoration:none}.guide-related{background:#fff8ee;border:1px solid #eadcc8}.guide-related h2{margin-top:0}.guide-related li{margin:.6rem 0}.guides-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.guide-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--guide-line);border-radius:14px;overflow:hidden;text-decoration:none;color:var(--guide-ink)}.guide-card img{width:100%;aspect-ratio:16/9;object-fit:cover}.guide-card div{padding:20px}.guide-card h2{font-size:1.25rem;margin:0 0 8px;color:var(--guide-navy)}.guide-card p{margin:0;color:var(--guide-muted)}@media(max-width:820px){.guide-layout{grid-template-columns:1fr}.guide-aside{position:static;order:-1}.guide-article{padding:28px 24px}.guides-grid{grid-template-columns:1fr}}@media(max-width:520px){.guide-main{padding:20px 14px 60px}.guide-article{padding:22px 17px}.guide-hero{padding:38px 20px}.guide-table{margin-left:-17px;margin-right:-17px;border-radius:0}}
"""

def schema(g):
    url = f'https://nexalyplanner.com/guides/{g["slug"]}/'
    return ('{"@context":"https://schema.org","@type":"TechArticle","headline":"' + escape(g['h1'], quote=True) +
            '","description":"' + escape(g['description'], quote=True) + '","image":"https://nexalyplanner.com' + g['image'] +
            '","mainEntityOfPage":"' + url + '","author":{"@type":"Organization","name":"NexalyPlanner","url":"https://nexalyplanner.com/about/"},' +
            '"publisher":{"@type":"Organization","name":"NexalyPlanner","url":"https://nexalyplanner.com/"},"datePublished":"2026-09-16","dateModified":"2026-09-16","inLanguage":"en-US"}')

def head(g, collection=False):
    structured = ('{"@context":"https://schema.org","@type":"CollectionPage","name":"' + escape(g['h1'], quote=True) +
                  '","description":"' + escape(g['description'], quote=True) + '","url":"https://nexalyplanner.com/guides/"}') if collection else schema(g)
    return f'''<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{escape(g['title'])}</title><meta name="description" content="{escape(g['description'], quote=True)}"><meta property="og:image" content="https://nexalyplanner.com{g['image']}"><meta property="og:image:alt" content="{escape(g['image_alt'], quote=True)}"><meta name="twitter:card" content="summary_large_image"><meta name="date" content="2026-09-16"><style>{STYLE}</style><link rel="stylesheet" href="/assets/css/style.css?v=2"><script type="application/ld+json">{structured}</script></head><body>'''

def guide_page(g):
    toc = ''.join(f'<li><a href="#step-{i}">{escape(title)}</a></li>' for i,(title,_) in enumerate(g['steps'],1))
    steps = ''.join(f'<section class="guide-step" id="step-{i}"><h3><span class="number">{i}</span>{escape(title)}</h3><p>{body}</p></section>' for i,(title,body) in enumerate(g['steps'],1))
    rows = ''.join(f'<tr><td>{escape(when)}</td><td>{escape(action)}</td></tr>' for when,action in g['routine_rows'])
    fixes = ''.join(f'<h3>{escape(title)}</h3><p>{escape(body)}</p>' for title,body in g['troubleshooting'])
    related = ''.join(f'<li><a href="{url}">{escape(label)}</a></li>' for label,url in g['related'])
    return head(g) + NAV + f'''<header class="guide-hero"><div class="kicker">NEXALY PRODUCT GUIDE</div><h1>{escape(g['h1'])}</h1><p>{escape(g['description'])}</p></header><main class="guide-main"><nav class="guide-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/guides/">Product Guides</a> › {escape(g['product'])}</nav><div class="guide-layout"><article class="guide-article"><figure><img src="{g['image']}" width="1200" height="750" alt="{escape(g['image_alt'], quote=True)}" fetchpriority="high"><figcaption>Product interface shown for orientation. Labels may vary slightly by screen size.</figcaption></figure><p>{escape(g['intro'])}</p><div class="guide-quick"><strong>Quick start:</strong> {escape(g['quick'])}</div><h2>Set up and use the planner</h2>{steps}<h2>A simple routine to maintain your records</h2><div class="guide-table"><table><thead><tr><th>When</th><th>What to do</th></tr></thead><tbody>{rows}</tbody></table></div><h2 id="data">Protect your offline data</h2><p>Your planner records are stored locally in the browser on the device you use. They do not automatically sync to another browser or device. Create a supported backup regularly, especially before clearing browser data, moving the HTML file, changing devices or reinstalling a browser. Keep dated backup copies in a location you control.</p><h2>Troubleshooting</h2>{fixes}<div class="guide-cta"><h2>View the {escape(g['product'])}</h2><p>See the full feature list, screenshots, download contents and current purchase terms on the product page.</p><a href="{g['product_url']}">View product details</a></div><div class="guide-related"><h2>Related planning articles</h2><ul>{related}</ul></div></article><aside class="guide-aside"><h2>In this guide</h2><ol>{toc}<li><a href="#data">Data and backups</a></li></ol><hr><p><strong>Updated:</strong><br>September 16, 2026</p><p><a href="/guides/">All product guides</a></p></aside></div></main>''' + SHELL

def index_page():
    cards = ''.join(f'''<a class="guide-card" href="/guides/{g['slug']}/"><img src="{g['image']}" alt="{escape(g['image_alt'], quote=True)}" loading="lazy"><div><h2>{escape(g['h1'])}</h2><p>{escape(g['description'])}</p></div></a>''' for g in GUIDES)
    meta = {'title':'NexalyPlanner Product Guides & User Manuals','description':'Open step-by-step NexalyPlanner product guides for setup, daily workflows, offline data, backups and troubleshooting across five digital planning apps.','image':'/images/og-default.jpg'}
    return head(meta | {'slug':'','h1':meta['title'],'image_alt':'NexalyPlanner product guides and user manuals'}, collection=True) + NAV + f'''<header class="guide-hero"><div class="kicker">NEXALY HELP CENTER</div><h1>Product Guides &amp; User Manuals</h1><p>Step-by-step setup, daily workflows, offline data guidance and troubleshooting for NexalyPlanner products.</p></header><main class="guide-main"><nav class="guide-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › Product Guides</nav><section class="guides-grid">{cards}</section></main>''' + SHELL

for guide in GUIDES:
    target = ROOT / 'guides' / guide['slug'] / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(guide_page(guide))

index = ROOT / 'guides/index.html'
index.parent.mkdir(parents=True, exist_ok=True)
index.write_text(index_page())
print(f'Built {len(GUIDES)} guides and the guides index')
