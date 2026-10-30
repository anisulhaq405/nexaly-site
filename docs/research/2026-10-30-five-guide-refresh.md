# Five existing guides: GSC-informed review, October 30, 2026

## Evidence and selection

Read both supplied October 29 GSC performance workbooks (overall and United States). Their daily chart ends October 26; these are historical exports, not a fresh live Search Console pull. Queries and Pages are independent aggregate tabs. No query-to-page join, traffic volume or ranking improvement is inferred.

| Existing guide | Export evidence | Scope of selection |
| --- | --- | --- |
| Academic Planner | Overall and US page: 1 impression, position 97; query `what is academic planner`: 1 impression, position 97 in each view | Define the term and show the deadline-to-preparation handoff |
| Monthly Teacher Planner | Overall page: 2 impressions, position 49; no matching explicit teacher query row | Preparation dates and review boundaries |
| Weekly Digital Planner for Small Business | Overall page: 1 impression, position 9; `business weekly planner`: 1 impression, position 60 in overall and US query tabs | Related intent, not proof this query served this page |
| Hourly Planner | No direct matching query/page row found in supplied exports | Related time-blocking gap; do not claim GSC demand for this exact URL |
| Retail Store Business Plan | No direct matching query/page row found; adjacent boutique opening-stock queries exist (6 impressions, position 27 for the longer query in both views) | Adjacent retail planning intent, not exact URL attribution |

All five are outside October 29's ten-guide refresh. They have prior editorial history: Academic/Teacher were enriched in 54c277d2, Hourly in 55b1a732, Retail in dcf7f2d1; Weekly also has earlier substantive edits. They are not described as never edited. Excluded recent dedicated batches and already refreshed high-impression URLs. Do not add overall and country counts together.

## Source review

Public search followed by the primary pages below; not a verified local top-ten ranking report. Sources support general methods; dated tables and business figures are original fictional illustrations.

- https://ace.fsu.edu/study-tools-and-tips/time-management — semester assignment calendars versus weekly study schedules; academic guide cites this.
- https://www.atlassian.com/team-playbook/plays/redesign-your-calendar — calendar review and time blocking; weekly guide cites the method without promising outcomes.
- https://ctl.indianapolis.iu.edu/Resources/Preparing-to-Teach/Planning-a-Learning-Session — learning objectives, prerequisite work, materials, timings and assessment; teacher guide cites this.
- https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan — redirects to https://www.sba.gov/counseling/plan-your-business/; retail guide uses the current route for broader planning context.
- https://www.niu.edu/academic-support/student-guides/using-calendars-and-planners.shtml — search review confirms separation of semester overview, fixed weekly commitments and estimated work. No borrowed example or quoted passage.
- https://students.unimelb.edu.au/academic-skills/study-skills/time-management/semester-planner — search review of flexible term planning; no claim about Nexaly file features.

## Changes and reproducible checks

- Academic: title/description answer the definition intent. Six-hour dated paper sequence plus one-hour buffer; adding 90 minutes exposes a 30-minute shortage. Correct existing Saturday rubric check after Friday submission.
- Teacher: November teaching dates with October preparation; due-today stays distinct from overdue. Actual model returns 3 lessons / 1 ready / 1 overdue / 2 not ready; marking overdue row Ready yields 2 ready / 0 overdue / 1 not ready.
- Weekly business: 20 working - 6 admin - 3 buffer = 11 delivery hours; rows 3+1+2+4 = 10, 90.91% booked, 1 free. Adding 2 gives -1 free in the actual model. Align Thursday email / Friday review across existing tables; remove the false claim that finishing Wednesday before a Thursday deadline is a scheduling mistake.
- Hourly: 10-minute call/travel overlap; moving travel still leaves no setup buffer. Eight-hour 22:00–06:00 shift; actual builder supplies eight rows and +1 day at midnight. Remove unmatched second main closing tag.
- Retail: original returned-unit stock/margin/cash reconciliation. Sellable stock 66, net sales 1944, retained-sale cost 972, contribution 443, cash 4055, uncommitted cash after 300 setup/1000 reserve 2755. Show the 132 profit versus 240 cash change and distinguish damaged stock.

Preserve publication dates, images, shared design, executable tools, products, prices and checkout. Update modification dates, descriptions, generated schema/catalog/sitemap. Prior five-guide lock hashes may change only after comparison proves their sole difference is generated main.js cache references. Exact scope audit and live release evidence belong in the final verification record. Mobile/physical printer QA and Google indexing/ranking effects require their own evidence.
