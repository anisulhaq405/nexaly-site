# Supplier Lead Time Log refresh — November 16, 2026

Owner requested the existing /tools/supplier-lead-time-log/ updated. Base main 7c39cde9e9561630ebb9853664868e1802373ada. Keep original October 16 publication date, stable URL, title, cover, input fields, saved-state key and version-1 backup shape. Actual modification date November 16. No new page, product or paid-feature changes.

## Implemented

Lead model now returns received-only median, shortest/longest actual calendar lead, observed max-minus-min range and on-time received count, alongside existing average/percentage/open counts. Supplier history gains the same statistics plus overdue open count. Open follow-up queue sorts original promise ascending, then reference. Open ages and overdue days retain existing definitions, with due-today not overdue. No quantity/quality weighting, forecast, holidays or reorder recommendation added. Empty received cohorts show Not available; single receipt has zero observed range without implying reliability.

Only the existing lead branch and its report note change in the five-tool model. Exact checks prove other four configurations/branches unchanged. The target HTML alone receives the new shared-model content-hash URL; other tools have no HTML or behavior changes. Legacy backup inputs, version, storage key and drafts remain compatible. Shared UI already exports all metrics/extra tables, recalculates CSV and print, safely renders text, and confirms imports/clears; model/DOM regression exercises those behaviors.

Guide adds definitions, a three-receipt comparison, censored/open-cohort caveat, partial delivery example, original versus revised promise, limits/OTIF distinction, focused FAQs and primary references. Meta description and truthful WebApplication feature list updated. Page-only heading scroll margin keeps guide anchors below fixed navigation. No global CSS, paid product, price, checkout or sitewide JS cache churn.

## Research

Public exact/adjacent search and direct pages reviewed; not verified country-locked Google positions, search metrics or a firsthand ERP integration test. Search reader could not retrieve the Nexaly URL (DisabledError); repository source was read and normal live/browser QA is required.

- MONITOR ERP, https://help.monitorerp.com/SE-MONITOR_G5/en-us/Content/Topics/Purchase/StatisticsFollowUp/OrderLeadTimeP/wOrderLeadTimeP.htm — primary product documentation distinguishes registration, confirmation, initial and arrival lead times. Our log explicitly fixes order placed to full receipt and does not import its ERP events or scheduling features.
- Microsoft, https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/supplier-requested-confirmed-dates — primary requested ship/receipt and calendar distinction. Our elapsed calendar-day rule does not claim working-day scheduling.
- ToolsFYI, https://www.toolsfyi.com/tools/business-tools/supplier-delivery-performance-report — primary tool description uses line-count on-time and lateness, with equal row weight and quantity/quality limits. Our added open queue prevents presenting completed-only performance as the whole outstanding cohort. Not a verified hands-on competitor test.
- TaroStack, https://www.tarostack.com/articles/lead-time-calculation-formula — primary publisher example and downloadable-log discussion cover average/worst/spread. Our range is explicitly max minus min, not their standard deviation, safety-stock formula or automated receiving. Original dates and examples used; no copied supplier data or product claims.

No asserted keyword volumes, ranking gains, GSC results or supplier benchmarks. Definitions are brief original paraphrases; examples and arithmetic are independently authored.

## Independent examples and boundaries

Built-in historical two-row sample preserved: order Oct1, promise Oct8, full receipt Oct11 =>10 actual calendar days, 3 late; open Oct5/promise Oct14 at Oct16 =>11 days age, 2 overdue. One received row =>median/shortest/longest10, range0, on-time0%.

Separate completed comparison: TEST-A10 days late3, TEST-B6 days on time, TEST-C14 days late5. Sorted6/10/14 =>average10, median10, min6, max14, range8, on-time1/3=33.33%. Adding a same-day fourth receipt gives sorted0/6/10/14, median8 and average7.5. Open rows do not change these statistics. Order Sep1 to Oct16 age45; promiseOct14 overdue2. DueOct16 is not overdue; futureOct20 remains upcoming. Supplier case/outer-space variations group together.

Partial 100-unit scope:60 receivedOct8 and40Oct11 =>full receiptOct11, 10 actual days fromOct1, 3 late against originalOct8. No quantity field or weighted partial-date calculation exists; preserve source evidence elsewhere.

## Required verification

All five model and DOM suites, including historical backups/save/restore, wrong-tool import, CSV escaping, text-only rendering, print call and storage failure. Added independent odd/even/zero/single/empty medians, range, cohort exclusion, supplier grouping, queue ordering, unique refs and date boundaries. SEO build/check, full publishing regression, core freeze, local links and guide anchor checks. Current-head CI before merge, then main CI and normal production byte checks. Live browser verifies sample metrics/queue, stale report after edit, save/restore and visible layout; no physical phone certification. Final evidence retained in PR.
