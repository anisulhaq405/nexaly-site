# Journal publication log

## October 20, 2026 — two new free-template journals

New: `/journal/inventory-count-sheet/` and `/journal/production-schedule-template/`. Original worked examples, two-page printable HTML downloads, unique editorial covers and contextual links. Fresh US provider lookup informed keyword selection; monthly data lag is documented in release notes. Publication requires exact-head CI and live verification. GSC remains deferred. Details: `docs/editorial/oct20-new-blogs/README.md`.


## October 10, 2026 — procurement workflow continuation

Prepared four substantive existing-page updates on current main: Inventory & Procurement Planner and VendorPulse OS buying pages now explain buyer fit, manual decision boundaries, browser-local backup ownership and evidence-based handoffs; purchase-order and reorder-point journals now connect a replenishment trigger to one controlled PO and show how open/cancelled inbound quantities prevent duplicate orders. No new URL or product. Original publication dates retained; substantive journal/product modification date October 10. Supplier comparison and scorecard owners were already complete enough to avoid filler and remain for focused review within the October 10–12 window. Accuracy, calculations, limits and release gates: `docs/editorial/oct10/README.md`. Publication requires protected diff review, local checks, exact-head green CI and live verification.

## 15 September 2026 — supplied-keyword batch

- New: `/journal/adhd-planner-for-adults/` — selection checklist, 20-minute setup, worked daily plan, reset routine and accurate non-medical positioning.
- New: `/journal/student-planner-guide/` — connected timetable, assignment, exam and study-session system with semester setup and worked exam plan.
- New: `/journal/business-planner-weekly-review/` — sales, cash, orders, capacity, marketing and next-action review with a fictional shop example.
- Keyword selection comes from the owner's supplied research. Private keyword metrics and source files are intentionally excluded from the public repository.
- Three unique 1200×800 JPEG editorial covers. Each page has a distinct intent, descriptive metadata and alt text, truthful BlogPosting markup, visible publication date and paid-product anchors.
- The user explicitly requested three journals for this batch, overriding the ordinary one-new/one-refresh preference. No existing journal or product body, checkout link, price or shared layout was manually changed.

Publication must use a feature PR and the required rebuild check. Live deployment and indexing are separate verification steps.

## 14 September 2026 batch

Batch contents:

- New: /journal/reorder-point-small-business/ — worked reorder-point, inventory-position, case-pack and periodic-review examples; links to Inventory & Procurement and two relevant guides. Original formula feature illustration.
- Refreshed: /journal/inventory-software-without-subscription/ — usable on-page evaluation checklist, fictional three-year license/time comparison, corrected misleading download anchor, relevant Inventory & Procurement link and new guide cross-link. Original buying-checklist illustration replaces reused product feature image. Existing title/URL retained.
- Both receive truthful BlogPosting markup and modification dates. New journal publication date is 14 September 2026; no unknown original publication date is invented for the refreshed article.

Evidence: public query searches for reorder-point calculation and subscription-free/one-time inventory software. Reviewed inFlow's formula guide https://www.inflowinventory.com/blog/reorder-point-formula-safety-stock/ and Vertex42 inventory template https://www.vertex42.com/ExcelTemplates/inventory-control-template.html. Related search results included Netstock, NetSuite, Zoho, QuickBooks, Bloomreach, Ply, Knack, GigaTrak, Unleashed and Lark. Search returned some homepage-resolved snippets and irrelevant rows. This is a qualitative competitor/intent review, not a verified US top-10 ranking audit. No exact search volume or KD claims appear in the articles.

Original calculations: 120/30=4; 4*7+12=40; 32+24-8=48; ceil((100-40)/24)*24=72; 40+72=112; 4*(7+7)+12=68; 10-2+1=9; 12-5=7; 10*36=360; 360-30=330; 0.5*36=18 hours; 18*20=360. All figures are explicitly hypothetical, not vendor prices or customer results.

Technical checks and live publication outcome are reported in the publishing session. Next run must confirm these URLs in the current repository before creating anything, and update this log rather than repeating this batch.

## 15 September 2026 batch

- New: /journal/supplier-quote-comparison/ — same-spec quote table, fictional landed/accepted-unit costs, quantity and deadline constraints, deposit reconciliation and VendorPulse link.
- Refreshed: /journal/boutique-inventory-spreadsheet/ — variant-level stock table/formulas, reservations, shipping, returns and weekly reconciliation; corrected misleading free-workbook language; paid app clearly identified.
- Image correction: /journal/reorder-point-small-business/ — new editorial cover only; publication and substantive-modification dates retained.
- Three distinct feature illustrations, 1200×800 JPEGs. Journal-only listing ratio changed to3:2 so landscape headings are not cropped by product portrait styling.
- New page publication date and refreshed page modification date:2026-09-15. Existing publication dates/order retained.
- Research, source URLs, assumptions, original calculations and cover briefs: docs/research/2026-09-15-supplier-boutique.md. Qualitative review only; no verified local top-ten or volume/KD claims.
- Publication uses a feature PR and required rebuild check. Live verification outcome is reported in the publishing session; do not infer Google indexing from successful deployment.

Next candidates: batch/lot tracking guide and a substantive sales-inventory tracking refresh. Check the current catalog and intent overlap before creating another URL. Continue one new guide plus one useful refresh when quality allows.

## 15 September 2026 — AI journal layout repair

Restored the standard site header, footer, auth markup and shared stylesheet on /journal/how-to-run-a-one-person-business-with-ai/. Scoped legacy article styles under .ai-journal to prevent shared navigation, wrap, button and footer collisions. Preserved article body content and all product/checkout files. Added visible Updated September 15, 2026 and matching dateModified; original publication date remains unknown.

Created a new original AI-generated editorial cover at /images/journal/one-person-business-ai-concept.jpg (1200×800 optimized JPEG). The initial built-in generation hit the account limit; after the advertised reset time passed, one retry succeeded. Final prompt brief: one human business owner at a laptop, restrained research/writing/support/records panels, emerald/navy and brass palette, exact headline “ONE PERSON. AI ASSISTED.” and NexalyPlanner branding; conceptual editorial scene, not an actual product screenshot. Replaced the interim diagram cover before merging; no pending cover work remains.

Local SEO build/check and publishing regression suite pass; standard header/footer exact-match and article-body preservation verified. Publish through required PR checks; live result reported in session.

## 15 September 2026 — journal navigation and date polish

Added the missing top-level Back to the NexalyPlanner Journal link to the AI article with article-scoped spacing. Audited all 18 journal pages for an in-content return link and a single H1. Updated the SEO builder to derive card dates from recorded publication/modification metadata, including BlogPosting/Article JSON-LD. A newer or modification-only date is explicitly labeled Updated; dates are never fabricated from the build time. Existing undated-source records and reading-time suffixes are preserved. All 18 current journal cards now display dates in both static and JavaScript-rendered lists.

Regression coverage includes new publication dates, later updates, schema-only update dates and repeated-build stability. Existing protected storefront tests remain required. Shared header/footer markup, product details, prices, checkout logic and shared CSS unchanged.

## 15 September 2026 — exact return-link format and exam cover

Matched the AI journal return-link wording to the existing standard: “Back to the Nexaly Planner Journal”, without an arrow. Moved it below the article introduction and above the feature image, with the plain small-text styling used by the reference journal. Shared header/footer untouched.

Replaced the exam guide's mismatched product screenshot feature and SVG social/card source with one original 1200×800 JPEG: /images/journal/exam-prep-20260915.jpg. Built-in generated prompt: premium indigo/lavender study-desk editorial, notebook, books and clock, headline “PLAN YOUR EXAM PREP”, NexalyPlanner branding, no app screenshot or outcome claims. Removed an unrelated inline product screenshot incorrectly captioned as a ten-day study plan; the actual worked ten-day HTML table remains. No publication dates, product files or checkout logic changed.
## 28 September 2026 — eight planning journals

New, distinct editorial intents: retail store business plan, freelance business plan, event-equipment rental business plan, SaaS business plan, one-page marketing plan, 13-week cash forecast, weekly digital planner for a small business, and small-business budget example. URLs are under /journal/ with corresponding descriptive slugs. Each includes an original 1200×800 SVG feature illustration, a filled numerical example, stated assumptions, source links, relevant internal links and 2026-09-28 publication metadata. There are no claims of customer outcomes or product features beyond the linked product pages.

Keyword selection used the owner's supplied private research exports. Metrics from those files are intentionally omitted from the repository. The chosen topics were screened for relevant, specific search intent and checked against existing journal URLs. These are editorial targets, not ranking or traffic guarantees. The cash-flow article explains a spreadsheet layout but does not offer an Excel download. The rental article concerns event equipment, not real estate.

Primary external reference points: SBA business plan guide (https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan), SBA budgets/forecasts (https://www.sba.gov/blog/2019/2019-07/5-classic-fails-budgets-forecasts/), SCORE quick-start marketing plan (https://www.score.org/tools/quick-start-marketing-plan/), IRS recordkeeping (https://www.irs.gov/businesses/small-businesses-self-employed/recordkeeping). Examples and diagrams are original illustrative calculations. Public search is a qualitative intent check, not a verified localized top-ten ranking report.

Source authoring script: scripts/author-eight-journals.py. Run the SEO build, regression suite and generated-output check, then publish through a feature PR and successful rebuild status. Verify live pages, journal cards and sitemap after merge; no Google indexing claim.
## 28 September 2026 — expanded plans and replacement covers

Owner feedback: the first eight feature graphics were generic and the articles were brief outlines. Replaced all eight covers with distinct 1200×800 editorial JPEGs showing the actual planning context (boutique range/stock, freelance delivery, event-equipment rental, SaaS subscriber/runway, one-page marketing, 13-week cash, a digital week, and budget variance). The generated image originals were produced with the built-in image tool and the final JPEGs were resized/optimized for journal cards. Removed the eight obsolete SVG feature assets. Each page has descriptive image alt text, matching social image metadata, a full worked plan and five jump links to the detailed steps.

Expanded plans now walk from research and validation through offer/operations, assumptions and cash, a dated execution schedule, risk and review. Original figures remain illustrative. The 13-week cash forecast includes all 13 weeks; the SaaS article includes a three-month cash path; retail and rental include purchase/stock or utilization gates; the marketing plan includes a 30-day workback; the budget includes a volume-versus-unit-cost variance; the weekly digital plan includes work estimates and exceptions. Source: scripts/author-eight-journals.py and scripts/deep_plans.py. Product checkout and pricing are untouched. Rebuild/test/check and live verification are required on the resulting feature PR.

## 2026-09-30 — credibility and contextual navigation fixes

- Replaced unverified About year/download/rating stats with verified catalog count and offline workflow facts; explained local storage, backups and lack of automatic device synchronization.
- Added contextual journal links in cash forecast, agency capacity and repair inventory; preserved publication dates and updated modification dates.
- SEO build/check, regression suite, JS syntax and diff checks passed. Product details, header/footer, prices and checkout behavior preserved.
- Public homepage/About GET checks returned 200 with zero redirects. Prior CDN HEAD 307/504 was not sufficient evidence to change redirect rules.
- No article consolidation, backlink creation or indexing submission. Planner-format overlap needs GSC query evidence; AI visibility remains unmeasured.


## 2026-10-01 — three journals and five refreshes
Supplier scorecard, purchase order tracker and small-engine repair plan added with three distinct 1200×800 WebP covers. Cash forecast, rental plan, freelance plan, student guide and homeschool attendance refreshed; two related owners receive inbound links. Original publication dates preserved, modification dates and sitemap rebuilt. Local regression/SEO/link checks pass (115 public pages, 60 journals, no orphans or broken internal URLs). Competitor review and limitations recorded in docs/oct01-release.md. Publish through checked PR; verify deployment separately.


## October 2, 2026 — draft prepared October 1

Three new guides: marketing-agency-profit-margins, client-profitability-analysis, cash-runway-template. Five substantive refreshes: exam-study-schedule-template, academic-planner-school-year, college-assignment-tracker, homeschool-schedule-multiple-ages, homeschool-planner-multiple-children. Contextual inbound edits: agency-capacity-planning-example and saas-business-plan-template-example. Existing publication dates retained; adjust planned October 2 dates if delayed. Original fictional calculations, primary factual sources, three separate feature images. Historical approved September 28 keyword estimates; ten public pages reviewed per topic without claiming localized rank positions or current Authority Scores. Not published today. Release requires green latest-head CI and live verification.

## October 3, 2026 — draft prepared October 2

Prepared three complete journals: equipment-calibration-log, batch-lot-traceability-log, rental-equipment-maintenance-log; each with a distinct optimized WebP and original CSV starter. Five substantive updates: equipment-rental-business-plan-example (maintenance-adjusted capacity), repair-shop-parts-inventory (reservation/issue closure), inventory-software-without-subscription (lot and offline handoff tests), contract-renewal-workflow (amendment/owner handoff), how-to-track-consignment-inventory (post-payout partial refund). Original publication dates retained. Source/evidence/release scope in docs/editorial/oct03/README.md. Local tests: 121 public pages, 66 journals, zero orphans/broken URLs. Not yet live; release only through checked PR at scheduled October 3 publication. If delayed, correct dates and rebuild. Later topical runs must skip duplicating these three intents.


## October 4, 2026 — draft prepared October 3

Prepared refresh of two product pages (Digital Homeschool Planner and AI Student Planner), two setup guides, and four existing journals (multi-child planner, multi-age schedule, attendance tracker and college assignment tracker). Added child-specific record and assignment-to-session examples, accurate offline/JSON backup guidance, source-confirmed rule-based assistant scope, attendance/workbook reconciliation and contextual links. Corrected student concept/quiz and deadline-guarantee claims and schedule metadata's unsupported download wording. Original publication dates preserved; October 4 modification dates are planned until release. Existing images retained; no new journals or forced coverage. Source ledger, actual scope, visual-check limitation and publishing instructions: docs/editorial/oct04/README.md. Not published October 3; require green latest-head CI and final mobile/live verification at release.

## October 5 mobile layout follow-up (prepared for immediate release)

Actual Chromium render of the eight October 4 pages plus three October 5 journals found newsletter overflow at 360px and one unwrapped 620px guide-reference table in each education guide. The focused fix stacks newsletter controls below 520px and wraps those reference tables in keyboard-focusable scroll regions. All 44 combinations (11 pages at 360/390/430/1363px) now have document width equal to viewport width and no broken page images. Table scroll and Products submenu close/toggle/reset behavior passed. Details: `docs/verification/oct05-mobile-layout.md`. This entry records tested local preparation; verify current-head CI and live assets after merging. Header/footer markup, prices, checkout and executable app behavior are preserved.

## October 5 — buying journey copy correction

Audited three existing buying pages and embedded demos, opened their corresponding $11.99 Polar checkouts, and tested a selected three-product bundle at $25.99. Corrected Boutique product wording to distinguish manual stock/order records from automatic sync and explain JSON backup/device transfer/restore. No new journal or product. Evidence and coverage limits: docs/verification/oct05-buying-journey.md. Release requires exact-head CI and live copy verification.

## October 5 — all-product journey audit and core freeze

Completed the remaining eighteen desktop product/demo entry and single-checkout smoke checks. Combined with the earlier three, twenty checkouts showed the correct product and $11.99; Copilot displayed RepairBench and remains a Polar provider exception. All 3/5/10 bundle checkouts opened with selection references and correct prices. Whole Collection displays 21/$109.99 but its Polar description still says 15; benefits require admin verification. Added documented source baseline and CI core-freeze guard that allows editorial prose/catalogue changes. No site design, product feature, price or checkout mapping changed. Evidence/limits: docs/verification/oct05-all-products.md and docs/SITE-CORE-LOCK.md.

## October 6 release recovery

Owner reported the scheduled updates absent. PR #117 remained draft on an older base and conflicted with October 5 performance/core work. The four approved content edits were reapplied to main f22f6b3 and generated listings/sitemap rebuilt, retaining the performance fixes and core baseline. Scope: three existing homeschool journals and homeschool product copy; no new URLs. Two substantive journals/product carry October 6 modification dates; section-order-only journal keeps October 4. This records preparation; current-head CI and live verification are required before reporting publication.

October 5 Polar corrections were publicly verified: Copilot correct identity/$11.99, Whole Collection 21-product description/$109.99. Owner confirmed download delivery. No agent payment was made and no checkout URL/baseline changed.

## October 7 inventory cluster preparation

Prepared October 6: four existing pages, no new journal. Inventory buying guide gets evidence-status decision notes; boutique spreadsheet gets a count cutoff and one-event/one-correction example; OwnerOS guide distinguishes workspace activity from verified stock effects; Boutique guide gets manual cancellation/return records. Original publication dates retained; substantive update date planned October7. Core guard, generator, JS, whitespace and link audit pass (121 pages, zero broken URLs/orphans). Release requires exact-head CI and live/mobile validation. Do not merge before October7 08:00 Asia/Karachi; 08–09 publication window is a target, not guaranteed deployment time.

## October 8 inventory buying-page continuation

Prepared two substantive existing-product refinements on the current post-free-planner main: OwnerOS Core now explains buyer fit, evidence boundaries, a consistent order/SKU handoff and manual backup ownership; Boutique Business Planner now explains manual marketplace limits, a variant sale/cancellation example and restore-as-replacement behavior. Both product pages link contextually to their October 7 guide/journal owners and the next useful workflow. No new URL, product, feature, price, checkout, demo behavior, shared style or core baseline change. Actual modification date: October 8, 2026. Release requires core lock, regenerated catalogue/sitemap, regression/link/JS/diff checks, exact-head CI and live/mobile verification.

## October 9 inventory buying-page release

PR #148 was reconciled onto main `fe41941a313c970156af63a237c2824e58cff65e`, checked at exact head `0a6ccd82127e4cb903fd88c0964181f42ae58675`, and merged as `a0dc69f5f84723f486b9314f8811e29d17c0633b`. GitHub Actions run `37877275613` passed publishing regression, generated-output, 24 free-planner calculation/backup, core-lock and social duplicate-protection checks. The two product pages and sitemap returned HTTP 200 and byte-matched the merged files after deployment; headings, one H1 per page, image sources and the unchanged Polar checkout destinations were verified. No new URL was published. Local Chromium remained unavailable, so this release does not claim a fresh narrow-viewport browser pass; the added content reuses the existing responsive `pd-feats` grid and changes no CSS or executable behavior. Do not repeat this inventory batch.

## October 12, 2026 — AdSense readiness repairs

Owner authorized starting the agreed preparation work. Inventoried 68 articles and checked 148 live sitemap pages (all HTTP 200). Completed substantive refreshes of 10 existing guides: caregiver daily log, one-time/offline software comparison, solo-business AI workflow, iPad app comparison, iPad PDF setup, dated monthly layouts, monthly templates, weekly templates, daily layouts and the free-iPad guide. No new journal URL, paid product or redirect was created.

Added original 2026 monthly, undated monthly and weekly PDF resources and a blank caregiver TXT log; reused the existing daily PDF where suitable. Corrected internal editorial FAQ text and unsupported promotional claims. About/Privacy now explain organizational authorship, comparison/test limits, actual storage and planned/inactive advertising. Replaced 147 false newsletter blocks with a Contact link and changed contact to a clearly labeled email-draft flow. No email was sent.

All 365 calendar dates, 14 rendered PDF pages, worked arithmetic, consent/download events and contact behavior checked. Product header/style/script/price/checkout preservation proved before the focused footer/main.js baseline update. SEO regression/build, link and fragment checks pass locally; CI and live checks complete the release. Full evidence and account-only blockers: docs/verification/oct12-adsense-readiness.md. The owner confirmed this will be their first AdSense account; real account country/Terms, publisher ID, ownership connection, CMP and review submission remain account-dependent.

## October 13, 2026: clustered keyword workflows

Published 12 original guides and 11 distinct worksheets, with 14 contextual existing-page updates in PR #180. CI passed; all 201 changed public files matched live and all 11 new worksheet examples calculated in the cloud browser. Scope, exact routes, research confidence and verification status are recorded in `docs/verification/oct13-keyword-workflows.md`. Three lower-priority extensions remain held. Existing completed guides were preserved; no keyword-country, indexing or ranking result was inferred.

## October 19, 2026 — repair workflow draft prepared October 18

Prepared two substantive existing-journal improvements: small-engine weekly ready/blocked capacity and repair-parts supplier-delay/receipt/cancellation follow-up. Existing rental and renewal examples already cover the planned gap and were preserved. No new URL or paid product edit. Original publication dates retained; October 19 modification dates are planned until release. Local publishing/core/link/freshness checks pass. Exact scope and remaining release gates: `docs/editorial/oct19/README.md`. Hold draft until the October 19 publishing window; not live at preparation.

October 18 follow-up: owner authorized immediate publication of the October 19 prepared batch. Actual modification dates set to October 18; mobile/desktop Chromium checks passed. Paid/pricing content preservation proved after removing only generated script cache-query differences. Exact-head CI and live verification remain release gates.


## 24 October 2026 — discovered URL review

Audited the exact 41 retained Discovered URLs; all returned HTTP 200 with correct self-canonicals and no observed noindex. Added 13 contextual links from eight individually inspected indexed resources. Refreshed three overlapping 2026 planner comparisons with separate format/layout/purchase scopes and original comparison tables. Full scope, baseline, rollback and reproducible checks: `docs/audits/indexability-2026-10-24/README.md`. Indexing is not confirmed by these eligibility checks; the separate Unknown and uninspected queues remain open.


## 24 October 2026 — ten retained Unknown URLs

Live-audited all ten exact canonical URLs: HTTP 200, source match, sitemap/robots eligibility, self-canonical and no observed noindex. Added four contextual discovery paths from the retained indexed sample; six targets already had such paths. No confirmed technical exclusion or new Google indexing status is claimed. Evidence and reproduction: `docs/audits/unknown-10-2026-10-24/README.md`.


## October 29, 2026 - second five-guide refresh

Prepared competitor-informed updates to the existing Coffee Shop Daily Capacity, Content Marketing Capacity, Day vs Daily Planner, A5 Planner and Create Your Own Printable Planner guides. Add original threshold/peak-load arithmetic, a reusable content brief and dated capacity example, daily time budgeting, A5 physical-fit checks and tested builder presets/troubleshooting. Correct two unmatched main closing tags and clarify A5-on-Letter printing. Preserve all original publication dates, artwork, layout, tools, prices and checkout. Research URLs, distinct intents, selection limits and generated-only maintenance of the prior five-blog lock are recorded in `docs/research/2026-10-29-next-five-competitor-review.md`. Publish only through successful current-head PR CI and verify live pages, listing and sitemap before reporting completion.


## October 30, 2026 — five additional existing guides

Prepared Academic Planner, Monthly Teacher Planner, Weekly Digital Planner for Small Business, Hourly Planner and Retail Store Business Plan updates. Supplied October 29 GSC exports end October 26: three selected pages have direct page rows; two are related-intent gap choices without exact query/page rows. No independent query/page tabs were joined. All five have earlier editorial history and are outside October 29's ten-guide batch. Research, counts, selection limits, original examples and repairs: `docs/research/2026-10-30-five-guide-refresh.md`.

Add dated submission workback, cross-month preparation status checks, tested 11-hour weekly delivery budget, overlap/overnight checks and returned-stock/margin/cash reconciliation. Correct weekly schedule inconsistency, post-submission rubric timing and one extra main closing tag. Preserve publication dates, artwork and core; refresh actual modification dates and generated SEO output. Prior five-blog hash maintenance is cache-query-only after exact preservation proof. Publish through passing current-head PR CI; verify live pages, catalog and sitemap before reporting release.


## October 30, 2026 — owner advances saved five-blog shortlist

Owner requested immediate execution of the October 31 shortlist. Prepared Opening Boutique Inventory, Small Business Order Tracking, College Assignment Tracker, SaaS Business Plan and Adult ADHD Planner updates with actual October 30 modification dates. Add pack-rounding and duplicate-intake examples plus a copyable SaaS decision plan; consolidate repetitive assignment/ADHD sections into source-specific sorting and task-to-format guidance. Retain existing fragments, artwork, original publication dates and core. Historical GSC limits and primary-source/competitor review: `docs/research/2026-10-30-shortlisted-five-release.md`. No new URL or tool/download behavior changes. Require passing current-head PR CI and live verification before reporting completion.


## October 31, 2026 — fifth five-journal batch

Prepared Clothing Content Calendar, Boutique Social Media Ideas, Homeschool Attendance, Exam Study Schedule and Offline Digital Planners updates. Add variant-level publication gates, evidence-to-post briefs, source-reproduced attendance and deadline-capacity examples, and safer offline storage/recovery guidance. Correct blanket offline/payment/storage claims. Preserve prior twenty articles and core. Historical GSC evidence, web-search limitation, actual model results and release gates: `docs/research/2026-10-31-five-journal-refresh.md`. No new URL or download/tool behavior change. Require current-head CI and live verification before reporting completion.
