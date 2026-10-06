# Eight-category free tools release — October 6, 2026

Scope: seven new free worksheets plus the existing craft fair tracker. Eight available tools out of the planned fifty. Each category has one working page; no unfinished tool page was published.

| Category | Available tool | Theme |
|---|---|---|
| Inventory & procurement | Craft Fair Inventory Tracker | Teal |
| Cashflow & renewals | Weekly Cash Commitments Planner | Navy ledger |
| Freelancers & agencies | Freelancer Weekly Capacity Planner | Purple rounded cards |
| Repairs, rentals & operations | Repair Parts & Labour Worksheet | Orange workshop |
| Personal & study | Assignment Deadline Planner | Blue study layout |
| Homeschool | Homeschool Attendance Log | Green paper layout |
| Caregiving | Caregiver Visit Coordination Planner | Rose rounded cards |
| Content | Content Repurposing Planner | Amber task cards |

## Verification

- Independent fixtures and boundaries for seven models: weekly cash 800, free capacity 8 hours, repair estimate 110, assignment remaining 2 hours, two subject entries one instructional date, visit gap 60 minutes, three repurposing tasks.
- Scenario rules, exact money cents, half-cent labour rounding, overbooking, zero capacity, invalid dates, duplicate row IDs, excessive rows, visit availability and overlapping interval union checked.
- Chromium UI checks: fictional examples, explicit save, reload/restore, JSON download/reset/import preview/confirm, CSV, PDF, edited-result invalidation and required-field errors for every new tool.
- Spreadsheet formula escaping and literal HTML text rendering verified. Wrong-tool backup rejected without replacing work. Blocked browser storage reports an error rather than claiming a save.
- Content channel generator makes three editable rows and preserves existing rows on repeat use.
- Every new page checked at widths 360, 768, 1024 and 1440; directory checked at the same widths. Native date-time field overflow found and fixed with fieldset minimum size and single-column phone rows.
- Seven unique scoped accents verified. Shared storefront files, prices, checkout, paid demos and navigation remain protected by core-lock checks.
- Feature images are compressed screenshots of working reports with fictional data. Image dimensions match files. No invented dashboard or unrelated imagery.
- All seven PDFs checked to contain the report and exclude guide, saving controls and sales CTA.
- Relevant journal inbound links, directory cards, self-canonicals, breadcrumbs, truthful WebApplication metadata and sitemap entries included.
- Attendance supports 400 rows for annual records; other new tools support 100. Backups are versioned and tool-specific; no sync, automatic publishing or background reminders are claimed.

Rollback: revert this release PR to remove the seven new pages, images and scoped assets together, restoring the directory and journal links. The paid storefront has no migration dependency on these tools.
