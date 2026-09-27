#!/usr/bin/env python3
"""Build operating manuals for the three newest offline business systems."""
from pathlib import Path
from html import escape
import json
import re
import hashlib

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = (ROOT / 'guides/calibratrack-os/index.html').read_text()
CSS = REFERENCE[REFERENCE.index('<style>'):REFERENCE.index('</style>') + 8]
NAV = REFERENCE[REFERENCE.index('<header class="nav">'):REFERENCE.index('<header class="guide-hero">')]
FOOT = REFERENCE[REFERENCE.index('</main>') + len('</main>'):]
SCRIPT_VERSION = hashlib.sha256((ROOT / 'assets/js/main.js').read_bytes()).hexdigest()[:12]
FOOT = re.sub(r'/assets/js/main\.js\?v=[a-f0-9]+', '/assets/js/main.js?v=' + SCRIPT_VERSION, FOOT)

GUIDES = [
  {
    'slug': 'agency-client-profitability-capacity-os',
    'name': 'Agency Client Profitability & Capacity OS',
    'title': 'Agency Client Profitability & Capacity OS: Complete User Guide',
    'description': 'Set up clients, retainers, projects, team rates and time entries; interpret margin and capacity, test rate scenarios, print reports and back up Agency Portfolio OS.',
    'image': '/images/products/agency-client-profitability-capacity-os/01.jpg',
    'image_alt': 'Actual Agency Portfolio OS executive overview with fictional demo records',
    'intro': 'This manual follows the buyer app from first launch through a monthly agency review. The downloaded ZIP contains NexalyPlanner_Agency_Portfolio_OS.html and START_HERE.txt. Its sample names and figures are fictional. The public demo is temporary; use the extracted buyer app for your own records.',
    'quick': 'Extract the ZIP, open the HTML app, select language and one base currency, start a blank workspace, add team loaded rates and available hours, then clients and projects. Log time and direct costs before reading client margin or capacity. Back up the workspace as JSON.',
    'menus': [
      ('Executive Overview', 'Monthly portfolio snapshot: revenue, cost, profit, margin, available hours and decision prompts.'),
      ('Services and Clients', 'Define what you sell, client status, monthly retainer, planned hours, software and contractor allocations.'),
      ('Projects', 'Record fees, planned hours, due dates, status and the month in which a completed fee is recognized.'),
      ('Team Capacity', 'Compare available hours, billable target, logged time and planned retainer/project load.'),
      ('Time & Cost', 'Log dated team hours and client or project direct expenses; CSV exchange applies to time entries.'),
      ('Profitability', 'Review the selected month by client, margin and effective revenue per hour.'),
      ('Forecast / Renewal Lab', 'Explore rate, retainer and hiring assumptions; a scenario is not a booked sale.'),
      ('Reports / Data Center / Settings', 'Print a summary, exchange time CSV, back up or restore JSON, and set language, theme and currency.'),
    ],
    'sections': [
      ('Open and choose a workspace', '''Download and <strong>extract</strong> the ZIP to a permanent folder. Open the HTML file in current desktop Chrome, Edge, Firefox or Safari. Choose the fictional US demo to learn the screens, or <strong>start blank</strong> before entering real information. Demo values are not your business results. A different browser, profile or device has a separate local workspace.'''),
      ('Set business preferences first', '''In Settings, enter the business name, language, theme and intended display currency. Arabic uses right-to-left layout. Choose currency before entering monetary records: changing the selector later changes the symbol and display unit, <strong>not</strong> exchange rates or stored values. Check reporting month before comparing figures.'''),
      ('Create service lines and client records', '''Add each service once with a consistent name. For each client, enter status, monthly retainer and planned monthly retainer hours where applicable. Record monthly software and contractor allocations that belong to that client. Avoid putting the same direct cost into both a client allocation and a project expense. Review which clients are active in the selected month.'''),
      ('Add team members and loaded rates', '''For each person, enter available monthly hours, billable target and a realistic <strong>loaded hourly rate</strong> that reflects the cost assumption you wish to use. Keep the rate period and currency consistent with client fees. Update rates when costs change; existing reports are planning views based on current settings, not a frozen historical ledger.'''),
      ('Plan and track projects', '''Create a project under the correct client, with a fee, planned hours, due date and status. An open project due in the month contributes to planned load. A completed project fee is included as revenue in its recognition month. Check the recognition month and completion status before interpreting monthly profit. Project detail compares the fee with directly linked time and costs; general client retainer allocations are not added to that project detail.'''),
      ('Log time and direct expenses', '''Enter a date, team member, client, project when relevant, and actual hours for each time entry. Add dated direct expenses with a clear client or project link. Client delivery cost uses logged hours multiplied by that member’s loaded hourly rate, plus dated direct costs and active monthly client allocations. Review entries for duplicates and wrong months before using the dashboard. CSV import/export covers <strong>time entries only</strong>.'''),
      ('Read profitability correctly', '''Choose a month in Profitability. Revenue includes active monthly retainers plus completed project fees recognized that month. Profit is revenue minus calculated delivery costs; margin is profit divided by revenue when revenue is nonzero. Effective revenue per hour uses logged hours. A negative or surprising margin should prompt a check of missing time, recognition month, team rate, allocations and duplicated expenses. Historical retainer views use current client settings.'''),
      ('Compare team capacity and planned load', '''Capacity target is available hours multiplied by the billable target percentage. Compare it with logged billable time; planned load includes active retainers’ planned hours and open projects due that month. This is a staffing signal, not an appointment schedule. If load is high, inspect the underlying clients and project due dates before making a hiring decision.'''),
      ('Test rates, renewals and hiring', '''Use the rate builder with owner compensation, overhead, reserve and billable-hour assumptions to inspect minimum and target rates. In Renewal Lab, vary retainer increase or hiring assumptions and read the scenario result. These sliders model possibilities and do not change a contract, invoice or actual sale. Record the decision separately after checking scope and client terms.'''),
      ('Report, export and protect data', '''Open Reports to print a monthly summary through your browser. For a full portable copy, use <strong>Data Center → Backup</strong> to download JSON after meaningful edits and at month end. Keep dated copies outside the browser; test a restore in a separate safe workspace before relying on the backup. Restore can replace the current workspace, so back up the current state first. CSV is not a full backup.'''),
    ],
    'example': ('Example: review an unprofitable retainer', [
      'Select one month and inspect the client’s retainer, completed fees and calculated margin.',
      'Open Time & Cost; confirm the client’s hours, team member loaded rates, direct expenses and month.',
      'Check client software/contractor allocations and remove any accidental double count.',
      'Compare actual hours with planned retainer hours and open project commitments in Capacity.',
      'Try a revised retainer in Renewal Lab, then discuss scope and pricing with the client yourself.',
      'Print the reviewed report and save a dated JSON backup.',
    ]),
    'routine': [('Each workday', 'Log time and direct expenses using their actual dates and links.'), ('Weekly', 'Review open projects, due dates, planned load and missing time.'), ('Monthly', 'Confirm completed fee recognition, reconcile assumptions, inspect client margin and capacity, print the report and back up JSON.'), ('Before changing device or browser', 'Back up the entire workspace and test where your backup file is stored.')],
    'limits': 'This app is a planning tool, not an accounting ledger or sales forecast. Retainer history reflects current client settings. Currency selection does not convert amounts. The app has no automatic cloud sync; local browser storage is not a secure archive. Verify financial inputs and accounting treatment with your own records.',
    'trouble': [('Profit seems wrong', 'Check selected month, project completion and recognition month, missing or duplicate time, loaded rates and client allocations.'), ('Capacity seems too high', 'Inspect available hours, billable target, planned retainer hours and due dates on open projects.'), ('CSV does not restore clients', 'CSV handles time entries only. Use the full JSON backup and restore for the workspace.'), ('Records are missing', 'Return to the original browser/profile and file location; locate a dated JSON backup. Do not reset the workspace before making a copy of the current state.')],
    'faqs': [('Does the app bill clients or pay staff?', 'No. It records and models agency information; billing and payroll happen elsewhere.'), ('Can I move to another computer?', 'Export a JSON backup and restore it in the buyer app on the new computer. Check totals afterward.'), ('Does the currency picker convert values?', 'No. Select one base unit before entry and convert externally if needed.')],
  },
  {
    'slug': 'cashflow-13-os',
    'name': 'CashFlow 13 OS',
    'title': 'CashFlow 13 OS: Complete 13-Week Cash Flow User Guide',
    'description': 'Open CashFlow 13 OS, enter verified opening cash, receipts, payments and recurrence, record actuals, read weekly risk, test scenarios and preserve data.',
    'image': '/images/products/cashflow-13-os/01.jpg',
    'image_alt': 'Actual CashFlow 13 OS overview with fictional US cash records',
    'intro': 'This manual explains the purchased single-file HTML app. The ZIP contains NexalyPlanner_CashFlow_13_OS.html, READ_ME_FIRST.txt and release notes with model limits. The public demo is temporary; use the extracted buyer app for your own data.',
    'quick': 'Extract and open the HTML file. Choose one base currency and Start Blank. Set the Monday forecast week, verified opening cash at the start of that week and minimum safety threshold. Add dated cash in/out; then review all 13 weekly closings and download a JSON backup.',
    'menus': [('Overview', 'Cash balance chart, weekly pulse and current warning summary.'), ('13-Week Forecast', 'Chained opening, cash in, cash out and closing balance for each week; open a week for drivers.'), ('Cash In / Receivables', 'Expected customer collections and other incoming cash, with actual status.'), ('Cash Out / Payables', 'Expected supplier, payroll, tax and other outgoing cash.'), ('Recurring Items', 'Weekly and monthly expected receipts or payments.'), ('Scenarios', 'Isolated collection delay and planned inflow/outflow adjustments.'), ('Cash Alerts', 'Weekly closing-cash warnings against zero or your safety threshold.'), ('Reports / Data Center / Settings', 'Print report, exchange cash-record CSV, back up or restore JSON, and select language, currency and theme.')],
    'sections': [
      ('Extract and start with blank data', '''Extract the ZIP and open NexalyPlanner_CashFlow_13_OS.html in a current desktop browser. Explore USA Demo if useful, then use Start Blank for actual business planning. Keep the app in a stable folder and use the same browser/profile. Private browsing and clearing browser storage can remove local records.'''),
      ('Set one currency, opening week and safe cash', '''Choose the base currency before entry; the selector changes the unit displayed but <strong>does not convert saved numbers</strong>. Set the selected Monday week and enter available cash at the <strong>start</strong> of that week from a verified cash or bank position. Set a practical minimum safety threshold. A negative opening balance is allowed if it reflects reality. The app does not connect to your bank.'''),
      ('Enter expected receipts and payments', '''Add a descriptive title, direction (in or out), expected date and positive amount. Choose a category and counterparty; use notes for timing assumptions. Enter cash movements rather than accrual revenue or expense merely because an invoice exists. Receivables and payables help organize expected timing. Check taxes and irregular obligations yourself.'''),
      ('Set repeating transactions', '''Use weekly or monthly recurrence for flows that repeat. Monthly occurrences keep the original day of month where possible: a 31st may become the last day of a shorter month. Inspect forecast occurrences for duplicate entries before using totals. A one-time item should use no recurrence.'''),
      ('Replace a one-time estimate with actual cash', '''When money arrives or leaves, enter the <strong>actual amount and actual date</strong> on that one-time item. The forecast uses the actual values in place of its estimate. Do not create another entry for the same transaction. Confirm the actual date belongs to the intended week; a different week changes both weekly balances.'''),
      ('Read the 13-week chain', '''Open Forecast and inspect each week’s drivers. Closing cash = opening cash + cash in − cash out; the next week opens with that closing balance. Inspect the chart and weekly bars alongside source entries. A receipt moved after a supplier payment may create an earlier shortage even if the total over 13 weeks is positive.'''),
      ('Interpret cash alerts and runway', '''Cash Alerts compares <strong>weekly closing cash</strong> with zero and your minimum safety threshold. It does not detect a midweek or intraday overdraft. A rough runway estimate divides opening cash by average weekly net cash burn; it is not a guarantee. Investigate flagged weeks by opening their individual receipts and payments.'''),
      ('Run isolated what-if scenarios', '''In Scenarios, delay planned collections or vary planned inflows and outflows by percentage. Actual entries remain unchanged. A delayed receipt can move outside the 13-week window; inspect the week-by-week effect and compare it with the live plan. Saving a scenario stores assumptions, not a frozen copy of all source records. Do not treat scenario results as actual cash.'''),
      ('Roll the forecast forward', '''At a new week, use <strong>Roll to current week</strong> and enter the verified available cash at that week’s start. Prior projected closing cash is not automatically treated as actual opening cash. Review outstanding expected and actual items for duplicates or stale dates before interpreting the new window.'''),
      ('Print, exchange CSV and back up JSON', '''Print the management report after checking assumptions. Data Center exports and imports cash records as CSV; the required UTF-8 header columns are <code>title,direction,date,amount</code>. Direction is <code>in</code> or <code>out</code>, dates are <code>YYYY-MM-DD</code> and amounts are nonnegative decimals. Optional fields include <code>category,counterparty,recurrence,actual_date,actual_amount,notes,archived</code>. Review rejected row numbers in the preview. The <strong>JSON backup</strong> preserves the full workspace; export dated copies regularly. Back up current data before a restore.'''),
    ],
    'example': ('Example: a customer pays two weeks late', ['Enter a verified opening cash balance and safety threshold for a Monday-start window.', 'Add the customer receipt and payroll/supplier payments with their expected dates.', 'Review the original 13-week closings and note the lowest week.', 'In Scenarios, delay the planned receipt by two weeks; compare the revised weekly low against zero and the threshold.', 'Discuss collection timing or payment decisions outside the app; update the real record only when the actual cash arrives.', 'Roll to the next week with a verified cash position and save a JSON backup.']),
    'routine': [('Daily', 'Update one-time actual dates/amounts only when cash moves.'), ('Weekly', 'Verify opening cash, roll the 13-week window, review flagged weeks and adjust expected timing.'), ('Monthly', 'Check recurring entries, print a management report and test backup/restore readiness.'), ('Before changing browser or device', 'Download JSON and keep a safe second copy outside local browser storage.')],
    'limits': 'One aggregate base-currency forecast. No bank connection, reconciliation, payments, FX calculation or guaranteed liquidity. Risk alerts use weekly closing balances, not intraday cash. Local storage is not encrypted or synced. Scenario percentages affect planned entries, not actuals.',
    'trouble': [('Closing cash differs from expectation', 'Check opening cash date, entry direction, actual replacement, recurrence and which week each date falls in.'), ('A late receipt vanishes from the scenario', 'It may fall outside the 13-week window after the simulated delay.'), ('CSV import rejects rows', 'Check required headers, YYYY-MM-DD dates, positive amounts, in/out direction and none/weekly/monthly recurrence; review row numbers.'), ('Records are unavailable', 'Use the original browser/profile and file path or restore a dated JSON backup. Browser file:// storage behavior varies.')],
    'faqs': [('Does it connect to my bank?', 'No. Verify cash externally and enter it yourself.'), ('Do alerts show a Wednesday cash shortage?', 'Only if it affects that week’s closing balance; inspect timing within the week separately.'), ('Does currency selection convert amounts?', 'No. Convert amounts independently before entering them in one base currency.')],
  },
  {
    'slug': 'business-runway-burn-rate-os',
    'name': 'Business Runway & Burn Rate OS',
    'title': 'Business Runway & Burn Rate OS: Complete User Guide',
    'description': 'Set up cash accounts, revenue, expenses and safe cash; read runway and burn, compare hiring and funding scenarios, track milestones and back up the offline app.',
    'image': '/images/products/business-runway-burn-rate-os/01.jpg',
    'image_alt': 'Actual Business Runway and Burn Rate OS cockpit with fictional Juniper Labs data',
    'intro': 'This manual covers the standalone buyer app NexalyPlanner_Business_Runway_Burn_Rate_OS.html. The customer ZIP also contains READ_ME_FIRST.txt. The interactive site preview uses fictional, temporary records; work with your own data in the extracted offline buyer file.',
    'quick': 'Extract the ZIP, open the HTML app, start a blank workspace, choose one currency, then enter a dated current cash balance, recurring and one-time revenue and expenses, and a minimum safe cash threshold. Review the monthly projection, test one scenario and export JSON backup.',
    'menus': [('Runway Cockpit', 'Current cash, gross/net burn, recurring revenue, safe cash and depletion projection.'), ('Cash Accounts', 'Dated available balances that anchor the projection.'), ('Revenue / Expenses', 'Dated and recurring cash flows, amounts and categories.'), ('Burn Analysis', 'Revenue and expense trends, expense mix and recorded monthly actuals.'), ('Scenarios', 'Preview revenue growth or recurring cost changes without rewriting live records.'), ('Milestones', 'Target-month cash needs compared with projected cash.'), ('Hiring Simulator', 'Continuing salary and one-time hiring cost timing.'), ('Funding Simulator', 'A hypothetical injection in a chosen month.'), ('Alerts', 'Stale balance dates, missing inputs, threshold crossings and data-quality signals.'), ('Reports / Data Center / Settings', 'Print a summary, exchange records by CSV, back up or restore JSON, and set language, currency and theme.')],
    'sections': [
      ('Open the buyer app and choose a clean workspace', '''Extract the ZIP to a normal folder; double-click the HTML file and use a current desktop browser. Explore the fictional US sample first if you like, then start blank for your business. Choose language and light or dark theme in Settings. Select one base currency before entering figures: switching display currency later <strong>does not convert stored amounts</strong>.'''),
      ('Anchor the model with dated cash', '''In Cash Accounts, enter the available balance and its actual as-of date. Include only cash you regard as available under your planning assumptions. If multiple accounts are supported in your workspace, enter and check each separately. A stale as-of date can make today’s runway misleading; update balances from verified records rather than from a prior forecast.'''),
      ('Enter revenue and expenses by timing', '''Record expected or actual revenue and expenses with the correct amount, date, recurrence and category. Distinguish one-time cash movements from continuing flows. Recurring flows are normalized monthly for the projection; one-time flows enter the dated month. Review whether payroll, taxes, subscriptions, customer receipts and irregular bills are represented once each.'''),
      ('Set a minimum safe cash threshold', '''Choose the cash buffer below which you want an in-app warning. The threshold is your management assumption, not a regulatory or bank minimum. Compare the forecast curve with both zero and this buffer. A future threshold crossing deserves a source-record review before you act.'''),
      ('Read gross burn, net burn and runway', '''The cockpit uses entered balances and flows to show monthly gross burn, net burn, recurring revenue and estimated runway. Gross burn focuses on outflows; net burn accounts for inflows under the model. Review Burn Analysis to see expense mix and recorded trends. A positive net cash trend or a 36-month display cap should not be read as unlimited runway. Check dated balances and projected monthly cash rather than one headline number alone.'''),
      ('Inspect the projection and alerts', '''Trace months where cash drops sharply to the revenue and expenses driving them. Alerts flag stale balance dates, missing inputs, minimum threshold crossings and other data-quality concerns. They appear <strong>only while the app is open</strong>; there are no automatic emails, texts or vendor/bank connections. Correct the underlying record and review again.'''),
      ('Test revenue growth or cost reduction', '''Open Scenarios and preview compounded monthly revenue growth or changes to recurring expense levels. Change one assumption at a time, compare the result against baseline and inspect the month of lowest cash. The preview does not edit live records; save a scenario snapshot to revisit assumptions. A snapshot is a planning comparison, not a promise of new revenue or savings.'''),
      ('Evaluate hiring and funding timing', '''In Hiring Simulator, enter a proposed hire’s ongoing salary and one-time cost and review the effect on monthly cash and runway. In Funding Simulator, put a hypothetical cash injection into a chosen month. Compare the timing with the safe cash threshold; funding that arrives after a projected shortfall cannot prevent that earlier shortfall in the model. Verify financing terms outside the app.'''),
      ('Track milestones', '''Add a target month and estimated cash required for a business milestone. Compare it with projected cash in that month and the safe buffer. If the milestone appears underfunded, revisit timing or assumptions rather than changing real cash records to fit the target.'''),
      ('Print reports, exchange records and back up', '''Use Reports to print or save a PDF via the browser after reviewing inputs. Data Center handles CSV import/export for records and JSON backup/restore of the full workspace. Check imported rows and totals before decisions. Download dated JSON backups regularly and store a second copy outside the browser. Before restoring, export the current state because restore can replace it.'''),
    ],
    'example': ('Example: compare hiring now with hiring later', ['Update Cash Accounts with a verified dated balance and check recurring revenue and expenses.', 'Inspect the baseline cash curve and minimum safe cash for the next several months.', 'Enter proposed salary and one-time hiring cost in Hiring Simulator at the earlier start month.', 'Change only the start month to compare a later hire and note the lowest projected cash in each case.', 'Review a milestone requiring cash in that period; confirm whether each scenario preserves the buffer.', 'Choose a business decision outside the app, document your assumptions and save a dated JSON backup.']),
    'routine': [('Weekly', 'Update dated cash balances and check new revenue/expense evidence.'), ('Monthly', 'Review burn trends, recurring flows, projection, alerts and milestones.'), ('Before hiring or funding decisions', 'Compare baseline and scenario assumptions and verify external terms.'), ('After major edits', 'Export a dated JSON backup to a safe second location.')],
    'limits': 'Projection maximum display is 36 months. Forecasts depend on entered timing and assumptions and do not guarantee solvency. The app has no bank sync, accounting reconciliation, automatic notifications or FX conversion. Records remain in the local browser profile without cloud sync or encryption.',
    'trouble': [('Runway looks unexpectedly long', 'Review stale balances, missing expenses, duplicated revenue, recurrence and the 36-month display limit.'), ('Alert did not notify me by email', 'Alerts appear only while the app is open; use your own external reminders for deadlines.'), ('Scenario changed but actual records did not', 'That is expected: previews are isolated from live records.'), ('Data is missing on another device', 'Use a dated JSON backup and restore there. Each browser/profile/device has separate local storage.')],
    'faqs': [('Does the app update cash from a bank?', 'No. Enter verified dated balances yourself.'), ('Does a funding scenario mean money is committed?', 'No. It is a hypothetical injection for comparison.'), ('Can I rely on the 36-month result as a guarantee?', 'No. It is a capped display and assumptions-based projection.')],
  },
]

def p(text): return '<p>' + text + '</p>'
def list_html(items, ordered=False):
    tag = 'ol' if ordered else 'ul'
    return f'<{tag}>' + ''.join('<li>' + escape(item) + '</li>' for item in items) + f'</{tag}>'

def render(g):
    slug = g['slug']; url = 'https://nexalyplanner.com/guides/' + slug + '/'
    schema = {'@context':'https://schema.org','@type':'TechArticle','headline':g['title'],'description':g['description'],'image':'https://nexalyplanner.com'+g['image'],'mainEntityOfPage':url,'author':{'@type':'Organization','name':'NexalyPlanner'},'publisher':{'@type':'Organization','name':'NexalyPlanner'},'datePublished':'2026-09-27','dateModified':'2026-09-27','inLanguage':'en-US'}
    head = f'''<!doctype html><html lang="en-US"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{escape(g['title'])} | Nexaly Planner</title><meta name="description" content="{escape(g['description'],quote=True)}"><link rel="canonical" href="{url}"><meta property="og:type" content="article"><meta property="og:url" content="{url}"><meta property="og:title" content="{escape(g['title'],quote=True)}"><meta property="og:description" content="{escape(g['description'],quote=True)}"><meta property="og:image" content="https://nexalyplanner.com{g['image']}"><meta property="og:image:alt" content="{escape(g['image_alt'],quote=True)}"><meta name="twitter:card" content="summary_large_image"><meta name="date" content="2026-09-27"><link rel="stylesheet" href="/assets/css/style.css?v=3">{CSS}<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head><body>'''
    toc = [('start','Start and scope'),('menus','Screen map')] + [(f'step-{i}',title) for i,(title,_) in enumerate(g['sections'],1)] + [('example','Worked example'),('routine','Maintenance routine'),('data','Data and limits'),('troubleshooting','Troubleshooting'),('faq','Questions')]
    aside = '<aside class="guide-aside"><h2>In this guide</h2><ol>' + ''.join(f'<li><a href="#{key}">{escape(label)}</a></li>' for key,label in toc) + '</ol><p><strong>Updated:</strong> September 27, 2026</p><p><a href="/guides/">All product guides</a></p></aside>'
    rows = ''.join(f'<tr><td>{escape(name)}</td><td>{escape(purpose)}</td></tr>' for name,purpose in g['menus'])
    routine = ''.join(f'<tr><td>{escape(when)}</td><td>{escape(task)}</td></tr>' for when,task in g['routine'])
    sections = ''.join(f'<section id="step-{i}"><h2>{i}. {escape(title)}</h2>{p(body)}</section>' for i,(title,body) in enumerate(g['sections'],1))
    troubleshooting = ''.join(f'<h3>{escape(title)}</h3>{p(escape(answer))}' for title,answer in g['trouble'])
    faqs = ''.join(f'<details><summary>{escape(q)}</summary>{p(escape(a))}</details>' for q,a in g['faqs'])
    product = '/planners/' + slug + '/'
    article = f'''<article class="guide-article"><figure><img src="{g['image']}" alt="{escape(g['image_alt'],quote=True)}" width="1440" height="1080" fetchpriority="high"><figcaption>Actual product screen with fictional sample data.</figcaption></figure><section id="start"><h2>Start here</h2>{p(escape(g['intro']))}<blockquote><strong>First 15 minutes:</strong> {escape(g['quick'])}</blockquote></section><section id="menus"><h2>What each screen is for</h2><div class="guide-table"><table><thead><tr><th>Screen</th><th>Use it for</th></tr></thead><tbody>{rows}</tbody></table></div><p>Menu labels may vary slightly with the selected language or viewport. Use the app’s own labels when entering records.</p></section>{sections}<section id="example"><h2>{escape(g['example'][0])}</h2>{list_html(g['example'][1],True)}</section><section id="routine"><h2>Practical maintenance routine</h2><div class="guide-table"><table><thead><tr><th>When</th><th>Action</th></tr></thead><tbody>{routine}</tbody></table></div></section><section id="data"><h2>Data safety and operating limits</h2>{p(escape(g['limits']))}<p>Use the full JSON backup after important changes. Keep dated copies outside the browser, verify the file exists, and retain the original ZIP as your installation copy. Never put real confidential records into the public live demo.</p></section><section id="troubleshooting"><h2>Troubleshooting</h2>{troubleshooting}</section><section id="faq"><h2>Frequently asked questions</h2>{faqs}</section><div class="guide-cta"><h2>Explore {escape(g['name'])}</h2><p>See real screenshots, the interactive sample, download contents and current checkout terms.</p><a href="{product}">View product details</a></div><div class="guide-related"><h2>Related help</h2><ul><li><a href="/guides/">All NexalyPlanner product guides</a></li><li><a href="/journal/offline-digital-planners-guide/">How offline browser records work</a></li></ul></div></article>'''
    hero = f'''<header class="guide-hero"><div class="kicker">NEXALY PRODUCT GUIDE · UPDATED 2026-09-27</div><h1>{escape(g['title'])}</h1><p>{escape(g['description'])}</p></header><main class="guide-main"><nav class="guide-crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/guides/">Product Guides</a> › {escape(g['name'])}</nav><div class="guide-layout">{article}{aside}</div></main>'''
    return head + NAV + hero + FOOT

for g in GUIDES:
    target = ROOT / 'guides' / g['slug'] / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(g))

index = ROOT / 'guides/index.html'
s = index.read_text()
s = s.replace('Open 17 step-by-step', 'Open 21 step-by-step')
for g in GUIDES:
    href = '/guides/' + g['slug'] + '/'
    if href not in s:
        card = f'<a class="guide-card" href="{href}"><img src="{g["image"]}" alt="{escape(g["image_alt"],quote=True)}" loading="lazy"><div><h2>{escape(g["name"])} User Guide</h2><p>{escape(g["description"])}</p></div></a>'
        s = s.replace('<section class="guides-grid">','<section class="guides-grid">'+card,1)
    else:
        s = re.sub(r'(<a class="guide-card" href="'+re.escape(href)+r'"><img src=")[^"]+', lambda m: m.group(1)+g['image'], s, count=1)
index.write_text(s)

# The pre-existing three manuals remain intact, but load the current catalogue script.
for slug in ('calibratrack-os', 'consignclear-os', 'renewguard-os'):
    path = ROOT / 'guides' / slug / 'index.html'
    text = re.sub(r'/assets/js/main\.js\?v=[a-f0-9]+', '/assets/js/main.js?v=' + SCRIPT_VERSION, path.read_text())
    path.write_text(text)
index.write_text(re.sub(r'/assets/js/main\.js\?v=[a-f0-9]+', '/assets/js/main.js?v=' + SCRIPT_VERSION, index.read_text()))

for g in GUIDES:
    path = ROOT / 'planners' / g['slug'] / 'index.html'
    s = path.read_text(); href = '/guides/' + g['slug'] + '/'
    if href not in s:
        needle = '</aside></div><section class="nx-live"'
        assert needle in s, g['slug']
        s = s.replace(needle, f'<p class="pd-note"><a href="{href}">Read the complete {escape(g["name"])} user guide</a> for setup, every workflow, examples and backups.</p>'+needle, 1)
        path.write_text(s)
print('Built three full operating guides and linked their product pages')
