# NexalyPlanner keyword intent guardrails — 2026-10-27

Purpose: prevent competing pages from targeting the same *primary search task*. This is an editorial map, not an assertion of GSC cannibalization. Maintain existing canonicals and routes unless verified GSC query/page evidence justifies a change.

| Canonical path | Primary job/search intent | Supporting context, not a second primary page |
| --- | --- | --- |
| /journal/purchase-order-tracker/ | Track PO lines, accepted receipts, cancellations and outstanding balances | Partial deliveries, rejected goods and supplier follow-up |
| /tools/purchase-order-template/ | Generate or download a purchase order form | Initial PO documentation; link to tracker for ongoing receipts |
| /journal/supplier-scorecard-template/ | Explain supplier performance evaluation methodology with a worked example | Delivery, quality, evidence and weighting |
| /journal/supplier-quote-comparison/ | Teach how to compare supplier quotations and costs | Purchase decision before PO creation |
| /tools/supplier-quote-comparison/ | Interactive comparison worksheet | Link to the explanatory quote comparison guide |
| /journal/cash-flow-forecast-template-example/ | Create a rolling 13-week forecast by receipt/payment date | Cash-floor testing and weekly shortfalls |
| /planners/cashflow-13-os/ | Evaluate/purchase the offline 13-week cashflow operating planner | Product capabilities and checkout |
| /journal/cash-flow-report-template-variance/ | Explain forecast-versus-actual cash variance reporting | Diagnose deviations after a period closes |
| /tools/cash-flow-variance-report/ | Use a cash flow variance worksheet | Interactive tool; link to the method guide |
| /journal/cash-runway-template/ | Estimate cash runway and model reserve, burn and hiring assumptions | Scenario examples, not a week-by-week receipts forecast |
| /planners/business-runway-burn-rate-os/ | Evaluate/purchase the offline cash runway product | Product features and actual supported use cases |
| /journal/inventory-software-without-subscription/ | Compare an offline/no-subscription inventory workflow with alternatives | Software evaluation, not supplier scorecard or PO tracker |

## Required checks for each proposed article or content update

1. Write the reader's specific job in one sentence and compare against the existing canonical routes above.
2. Check GSC US query-to-page pairs if already available; do not claim harmful cannibalization merely because a term appears on more than one URL.
3. Keep distinct intents distinct: explain vs calculate vs template vs purchase; avoid assigning the same primary query to two informational pages.
4. Preserve current slugs, existing useful examples, product pricing, design, downloads, images and checkout.
5. Use contextual HTML links where user tasks naturally connect (quote comparison → PO → receipt tracking → supplier evaluation; cash forecast → variance; cash forecast → longer-term runway).
6. If two pages *demonstrably* answer the same task and compete on the same query, gather URL-level evidence first, then propose consolidation for review. Never bulk canonicalize/noindex/redirect on keyword similarity alone.
7. Validate SEO-build, regression tests and core freeze before any merge. Check deployed HTML and monitor GSC after release.

## Scope and next audit

This is a proactive planning control derived from the existing route structure. Current US GSC query-page exports were not read in preparing this document. It must not be called a confirmed cannibalization audit without that evidence.
