# October 8: next eight free planners

Release status: implementation and desktop preview QA complete; final CI and production verification pending.

The batch implements eight distinct drafts from the original package. Inventory and cashflow receive two each because the original care/content drafts are already represented by working tools. No duplicate caregiver/content variant was added just to make category counts equal.

| Planner | Category | Primary intent phrase | Relevant product |
|---|---|---|---|
| Reserved vs Available Stock Planner | inventory | available to sell inventory calculator | Inventory & Procurement Planner |
| Boutique Size & Color Stock Matrix | inventory | clothing inventory size color template | Boutique Business Planner |
| Invoice Collection Schedule | cashflow | invoice collection tracker template | Sales Management System |
| Subscription Price Increase Budget Planner | cashflow | subscription price increase calculator | RenewGuard OS |
| Fixed-Fee Scope Change Planner | agency | scope creep cost calculator | Agency Client Profitability & Capacity OS |
| Rental Booking Conflict Checker | operations | equipment booking conflict checker | RentFlow OS |
| Study Catch-Up Planner | personal | study schedule maker catch up | AI Student Planner |
| Homeschool Portfolio Index | homeschool | homeschool portfolio checklist | Digital Homeschool Planner |

## Evidence and claims

Pre-build specifications were used for the chosen inputs, formulas, boundaries and fixtures. Intent phrases are candidate utility queries, not confirmed search volume, difficulty or trends. No new country-level demand figures are invented. Free public search corroborated existing invoice templates and portfolio/stock workflows; this is not a localized rank audit. US English, USD first, and optional GBP/CAD/AUD/EUR/NZD currency labels serve the target audience; labels do not convert amounts.

Implementation refinements: the boutique matrix uses explicit counted on-hand values instead of a movement ledger; study windows are a consistent daily capacity over a short horizon; rental timestamps are explicitly UTC to avoid silently mishandling local daylight-saving times. These boundaries are explained beside the working planners.

## Distinct behavior

Reserved stock floors sellable availability at zero and exposes shortfalls. Size/color matrix distinguishes missing combinations from counted zero units and rejects duplicate variants. Invoice schedule separates actual payments from estimated collections. Subscription costs show annualized run rates rather than fake prorated cash impact. Fixed-fee scope uses forecast base hours and adds incremental scope separately. Rental capacity uses a sweep line over UTC half-open buffered intervals. Study catch-up honors date deadlines and preserves unallocated effort. Portfolio index stores text references, not actual child documents.

## Measurement and sales path

Each page is connected from its directory category, a related working free planner and an existing journal. Its guide links to a relevant paid product and product guide, with accurate compatibility language. Existing optional analytics counts calculate/export/sample button clicks without worksheet values. Clicks are not proof of successful completion or a sale. Evaluate impressions, queries, countries and product interest after the release has had time to collect data; indexing and sales are not guaranteed.

## Fifty-planner register reconciliation

This release brings the collection to 24, with 23 originating in the original 50 and the previously added Content Publishing Checklist. Retire draft 26, Retainer Hours Rollover Tracker, from the remaining launch backlog because eligible carried hours are already recorded by the live Retainer Overage Calculator. That leaves 26 distinct drafts plus 24 released planners = 50. No live planner is removed.

## Validation

Eight independent worked fixtures and boundary checks pass, including negative raw stock, missing matrix cells, invoice paid/overpaid, zero old subscription price, half-cent scope costs, exact booking boundaries, triple overlaps, study capacity and missing portfolio references. Existing fifteen shared-model and craft-fair suites pass. New suite is added to CI. Desktop HTTPS preview checks passed for all eight fictional sample reports. Actual browser report screenshots replace the provisional illustrations. Stock JSON and CSV downloads, import review/replacement, stale report clearing, and portfolio CSV were verified. Device save survived reload and restored correctly. Print control was invoked, but the cloud browser did not expose a print dialog or saved PDF; no PDF-output claim. Phone viewport/touch rendering was unavailable (browser zoom did not change the viewport); responsive CSS was reviewed, with actual phone QA still outstanding. Final current-head CI and deployment verification remain before release.
