# Combined sprint Day 1 — finance reports and startup cash

Owner request: start and complete new combined-plan Day1, not original sprint Day1. Baseline main `7d0aadd96582e350baaf474bf2e9a69c2204f6c4` (original Day7). Scope is exactly15 master IDs in scope.json:6 original journals,3 working free resources,6 existing owner updates. Protected paid apps, prices, checkout and storefront logic are unchanged; SEO-generated catalogs and asset-cache references change normally.

## Ownership and architecture

- F05/M080: explain the relationships of statements, not a new collection/builder URL.
- F09/M072: explain operating cash via a direct/indirect reconciliation; historical classified statement stays with F08.
- F26/M054: inventory/COGS education. Income worksheet accepts reconciled COGS rather than choosing inventory policy.
- O087/M073: sole-owner dated draw planning; not salary, corporate distribution or tax advice.
- O090/M071: nonprofit board decisions, restrictions and operational capacity, not a treasurer receipt/payment report.
- B08/M069: laundromat industry plan with machine-based assumptions, original funding/downside model, not a synonym laundry URL.
- F01/M097: historical simple P&L. F08/M088: historical direct cash activity worksheet. F11/M106: startup funding need, not monthly variance or a dated forecast.
- O053 financial-statement builder remains pending. Shared browser model `assets/js/finance-statements-20261118.js` exposes validate/calculate and versioned same-tool backups. Any future collection must reference/reuse these definitions, retain each owner's purpose and pass independent integration/reconciliation tests before advertising a complete builder.

## Research and evidence limits

18 November public queries included historical income/cash-flow/startup templates, operating cash flow/owner draw/COGS and laundromat/nonprofit dashboard terms. Public responses were not a verified localized Google rank report. No top-three position, vendor testing, source traffic or ranking metric is asserted. Supplied Semrush country/database is unconfirmed; no new traffic estimates were manufactured. Complete raw keyword provenance remains in the saved master report.

Primary factual references reviewed:
- SEC https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements — report scope, equity and profit/cash distinction. The numerical reconciliations are independently authored.
- IRS https://www.irs.gov/publications/p334 — 2025 Schedule C-specific context for COGS and personal-use merchandise. Limited US tax context, no filing conclusion or entity-general compensation claim.
- Propel https://propelnonprofits.org/resources/managing-restricted-funds/ — donor restrictions versus internal designation. No assumption that restricted net assets equal bank cash.
- National Council of Nonprofits financial-literacy guidance — board reporting purpose.
- Laundry Association https://www.laundryassociation.org/wp-content/uploads/2021/02/WhitePaper_BusinessPlan_Vol5No11_final.pdf — surfaced as an industry business-plan reference; direct PDF retrieval through search opener failed. Do not claim the full paper was inspected. Industry checks were cross-checked against accessible provider/association planning results; all financial figures here are original assumptions.
- https://laundryassociation.org/how-to-start-a-laundromat/ — site, equipment and planning topics in public association resource.
- Michigan State University https://openbooks.lib.msu.edu/financialmanagement1ed/chapter/financial-statements/ — owner draw separately identified in a cash model.

Representative content competitors/providers:
- Vertex42 income-statement page: downloadable small-business single/multi-step structures. Differentiation: validated browser review, cents arithmetic, guarded stale reports, explicit period/basis and aligned original three-report example. No competitor workbook downloaded or copied.
- Vertex42 historical cash statement and Smartsheet financial/cash templates: cash categories and file-format intent. Differentiation: independently entered closing-cash mismatch, specific exclusions, and separate forecast/variance owners.
- Smartsheet startup-budget collection: startup funding, cost and template-format intent. Differentiation: distinguish retained reserve from spending, show assumptions about constant monthly receipts/payments and do not claim daily solvency.
- LivePlan laundromat sample and association planning results: industry plan sections, machine/site economics and funding. Differentiation: reproducible turns-based base/downside case, explicit omitted costs, two different break-even boundaries and a reconciled opening cash reserve. No copied sample text or market-average costs.
- SEC educational report guide and original financial provider guides: explain statement types. Differentiation: a fully connected original workshop example with closing assets and liabilities/equity both25,700, operating cash3,500 and total cash movement3,400.
- Nonprofit board/Propel resources: restrictions and board literacy. Differentiation: separately sourced cash schedule, no net-assets-to-cash shortcut, transparent enrolment/participation denominators and24-hour capacity gap.

## Existing audits and original improvements

See audits.json for retained publication dates, previous modification evidence and exact owners. Balance-sheet and forecast pages already had useful downloadable resources and examples: retain them. Add distinctive report-choice and owner-draw timing explanations rather than redundant rewrites. Variance page distinguishes a financing receipt from operating sales; dashboard separates its bounded operating remainder from net income; bookkeeping adds an equipment close/handoff example; projections labels historical-versus-projected scope and links startup funding. Changes justify a November18 modification date. Do not rerun audit.py on already-updated pages: it is a one-time source patch.

## Resource contract and QA

Three resources: all required amounts intentional, money in integer cents in browser, input ranges, date/basis validation, losses/mismatches visible, same-tool validated JSON backup/import with replacement confirmation, text-safe output, reviewed CSV with formula protection and stale-report invalidation, browser print, static two-page writing/example PDFs and original XLSX Blank/Filled example formula workbooks. No bank integration, automatic storage or Google Sheets copy promise. Native Excel/Sheets recalculation and physical printing are not certified; the page says so. Browser DOM behavior and XLSX formula structure are tested separately.

Nine original example-chart covers were generated from the exact article/tool figures and visually inspected as a contact sheet. No fabricated app screenshots or AI photographs. Existing page artwork is retained. New directory cards appear in the cashflow category:64 searchable cards. Six pre-existing download-only resources still lack cards and remain a Day8 sitewide task; do not call the directory exhaustive.

Acceptance commands: seo-build.py; test-seo.py; seo-build.py --check; core-lock; empty images; existing Day6/Day7 arithmetic/date regressions; new model, DOM and editorial/XLSX/PDF tests; current-head PR rebuild check before merge. Record actual release SHA and production results separately, not as assumed success.

The combined108-action inventory is in docs/editorial/combined-master-20261118.json. This release assigns only15 Day1 owners; remaining93 are pending. Original deferred keyword sources remain unavailable; new ledger is not a substitute. Conditional40 families are outside108. No background jobs are created.
