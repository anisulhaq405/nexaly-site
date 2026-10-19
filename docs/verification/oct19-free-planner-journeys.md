# October 19: all 40 free-planner journeys

Owner requested all 40 rather than the proposed five. Reviewed current release 1307993 and retained existing controls/model validation from earlier releases. No GSC or keyword-demand conclusions in this audit.

## Findings and fixes
- All 40 already have a working worksheet, in-page guide, relevant article, next free tool and product/category route. No redundant next-step sections added.
- 35 lacked explicit keyboard focus and accessible region names on horizontally scrollable tables. Added a free-page-only helper for static and dynamically rebuilt report tables. The latest five already have this behavior and keep their existing helper.
- Ten October 13 tool pages linked to a specific paid product without its user guide. Added verified guide routes, including the small-business product/guide slug difference. Printable Planner Builder links to a category, so no arbitrary product guide is forced into it.
- Four generic article anchors now name their actual destination.
- 39 free pages changed; Document Renewal Calendar required no edit. No new URL. Calculation, storage, import/export code, shared CSS, paid pages, pricing and checkout unchanged.

## Verification
- 80 Chromium checks: all 40 pages at 390px and 1440px; fictional example reports, no JS errors, no page overflow, loaded images, one H1, labeled inputs and working in-page anchors.
- All 40 retain relevant journal and next-free-tool routes. All local internal link destinations exist. Product guide missing only on the intentionally category-linked printable builder.
- Real keyboard ArrowRight scrolling on craft, rental, cash variance and stock coverage tables; print-media hides optional upgrade panels on these four representative implementations.
- Directory still lists 40 planners.
- SEO freshness, core freeze (21 products / 26 protected files or sections), internal-link graph (176 indexable, zero orphans, zero broken URLs) pass.
- Prior calculation/save/restore/import/CSV tests were not repeated manually; their code is unchanged. Normal publishing CI remains required.
- Browser emulation is not a physical Android/iPhone test. No new physical-device or Google-indexing claim.

## Per-planner results

| Planner | Mobile + desktop | Guide route | Change |
|---|---|---|---|
| assignment-deadline-planner | Pass | Product guide present | Focused fix |
| boutique-size-color-stock-matrix | Pass | Product guide present | Focused fix |
| caregiver-visit-coordination-planner | Pass | Product guide present | Focused fix |
| cash-flow-variance-report | Pass | Product guide present | Focused fix |
| coffee-shop-daily-operating-plan | Pass | Product guide present | Focused fix |
| consignment-settlement-planner | Pass | Product guide present | Focused fix |
| construction-milestone-cash-schedule | Pass | Product guide present | Focused fix |
| content-production-capacity-planner | Pass | Product guide present | Focused fix |
| content-publishing-checklist | Pass | Product guide present | Focused fix |
| content-repurposing-planner | Pass | Product guide present | Focused fix |
| craft-fair-stock-reconciliation | Pass | Product guide present | Focused fix |
| document-renewal-calendar | Pass | Product guide present | No change needed |
| equipment-maintenance-due-planner | Pass | Product guide present | Focused fix |
| family-caregiver-handoff-sheet | Pass | Product guide present | Focused fix |
| fixed-fee-scope-change-planner | Pass | Product guide present | Focused fix |
| freelancer-weekly-capacity-planner | Pass | Product guide present | Focused fix |
| homeschool-attendance-log | Pass | Product guide present | Focused fix |
| homeschool-portfolio-index | Pass | Product guide present | Focused fix |
| homeschool-subject-hours-log | Pass | Product guide present | Focused fix |
| invoice-collection-schedule | Pass | Product guide present | Focused fix |
| leave-on-time-routine-planner | Pass | Product guide present | Focused fix |
| marketing-campaign-budget-planner | Pass | Product guide present | Focused fix |
| monthly-business-budget-variance | Pass | Product guide present | Focused fix |
| monthly-teacher-lesson-planner | Pass | Product guide present | Focused fix |
| one-page-business-plan-builder | Pass | Product guide present | Focused fix |
| physical-count-adjustment-worksheet | Pass | Product guide present | Focused fix |
| price-increase-budget-planner | Pass | Product guide present | Focused fix |
| printable-planner-builder | Pass | Product category; intentional | Focused fix |
| rental-booking-conflict-checker | Pass | Product guide present | Focused fix |
| repair-parts-labour-worksheet | Pass | Product guide present | Focused fix |
| reserved-vs-available-stock-planner | Pass | Product guide present | Focused fix |
| retainer-overage-calculator | Pass | Product guide present | Focused fix |
| service-business-financial-projections | Pass | Product guide present | Focused fix |
| software-renewal-decision-planner | Pass | Product guide present | Focused fix |
| stock-coverage-planner | Pass | Product guide present | Focused fix |
| study-catch-up-planner | Pass | Product guide present | Focused fix |
| supplier-lead-time-log | Pass | Product guide present | Focused fix |
| supplier-quote-comparison | Pass | Product guide present | Focused fix |
| trucking-trip-cost-worksheet | Pass | Product guide present | Focused fix |
| weekly-cash-commitments-planner | Pass | Product guide present | Focused fix |
