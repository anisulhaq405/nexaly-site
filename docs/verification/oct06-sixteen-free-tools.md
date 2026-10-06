# Second eight-category release — October 6, 2026 (Asia/Karachi)

Eight additional tools bring the collection to 16 of the planned 50. Every category now has two working tool pages. Existing paid applications and checkout remain protected.

| Category | New tool | Scoped accent |
|---|---|---|
| Inventory & procurement | Supplier Quote Comparison | Copper #853d29 |
| Cashflow & renewals | Software Renewal Decision Planner | Indigo #4338a4 |
| Freelancers & agencies | Retainer Overage Calculator | Burgundy #822137 |
| Repairs, rentals & operations | Equipment Maintenance Due Planner | Graphite #37434e |
| Personal & study | Leave-on-Time Routine Planner | Olive #5f651e |
| Homeschool | Homeschool Subject Hours Log | Turquoise #086b81 |
| Caregiving | Family Caregiver Handoff Sheet | Plum #794574 |
| Content | Content Publishing Checklist | Cobalt #2343bd |

## Calculations and validation

Independent fixtures: supplier score 68 from 80×60 and 50×40; a 100-unit landed quote of 230; October 31 minus 30 notice days gives October 1; five overage hours at 50 gives 250; meter threshold 1,000+250 gives 1,250; 08:00 minus 45 routine minutes and 10 buffer gives 07:05; 45+30 learning minutes gives 1.25 hours; an unfinished handoff stays open; publishing readiness requires every entered check to pass.

Boundary checks cover zero score weights, zero billing-term rejection, carried hours, below-allowance use, half-cent charges, unconfirmed authorization, exact maintenance thresholds, missing intervals, decreasing meters, future last-service dates, overnight routine dates, reordered steps, adjacent versus overlapping learning sessions, subject normalization, unfinished tasks and an empty checklist. All 15 shared-model samples round-trip through validation; duplicate IDs, unknown fields, excessive rows and missing required values are rejected. The original craft fair tests remain in the release checks.

## UI and reports

All eight new tools checked in Chromium with fictional examples, explicit device save, reload/restore, JSON backup/reset/import preview/confirmation, CSV and report-only PDF. Edited values invalidate the old report; missing required values prevent recalculation. Literal HTML remains text and CSV escapes formula-like values. Wrong-tool import leaves the current worksheet unchanged. Blocked storage shows an error instead of claiming a save.

Routine move controls preserve the revised order through device restore. Subject-session overlap shows a blocking error. The directory has 16 cards, two per category; search and the empty-results state are checked. Cash search correctly matches both cashflow-category tools.

Each new worksheet and the directory checked at 360, 768, 1024 and 1440 widths. Tables scroll inside their containers without expanding the page. The eight new accents are unique and distinct from the initial eight. Feature images are compressed screenshots of the actual fictional reports, not invented dashboards. Dimensions match the assets. Supplier price/freight/fee inputs, renewal notice periods and maintenance intervals also appear in report detail tables so CSV and PDF preserve the entered calculation inputs.

PDF checks confirm report titles and entered labels are present while guides, device-save controls and sales CTAs are excluded. Contextual links connect the new pages to existing journals, related free tools, relevant paid products and their guides. Unique metadata, self-canonicals, breadcrumbs, truthful WebApplication data and eight sitemap entries are included. Shared model/UI scripts use content hashes to invalidate stale caches.

## Release gates

Run model tests, craft tests, SEO build idempotence, SEO regression, core-lock, mocked social tests, internal-link audit and diff whitespace checks. The link audit reports 138 indexable pages, zero orphan pages and zero broken internal URLs. CI must pass before merging; verify the deployed directory and every new working example afterward. Indexing, rankings and AI-search inclusion are not claimed.

The publishing checklist is a new content-category workflow beyond the original single-content-tool draft. The goal remains 50 total; remaining backlog count is 34. Category labels now state available tools rather than freezing the original draft allocation.

Rollback: revert this release PR to remove new pages, images, metadata and links together. Existing device saves use unchanged versioned keys and schemas. No paid-product migration depends on this release.
