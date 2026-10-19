# October 20 advance batch — prepared October 19

Status: complete source draft, not published. This continues the monthly October 19–21 repair/rental/renewal window one day ahead. October 19 repair improvements and the all-journal metadata fix are already live via PR200/201; do not repeat them. Paid products are outside this batch.

## Audit and decision

Reviewed rental-equipment-maintenance-log, equipment-rental-business-plan-example, contract-renewal-workflow, Rental Booking Conflict Checker and Software Renewal Decision Planner against current main 7fc953909b8f9c89b389bf1241478d3bb6e0eb28.

Existing rental guide covers day-level downtime and release evidence but lacks a filled late-return-to-dispatch handoff. The new section supplies exact actual/expected timestamps, 30-minute loading, a 15-minute conflict and an unresolved-inspection branch. It points accurately to the free UTC-input conflict checker and preserves human release ownership. All numbers are explicitly fictional. No safety, compliance or automatic-monitoring claim is added.

The renewal guide already covers controlling source documents, amendments, owner handoffs and delivery evidence. Its free planner already distinguishes cancellation intent from confirmation and annual equivalents from actual bills. No useful missing section identified today: preserve both instead of padding or changing dates.

## Publication instructions

Insert rental-return-dispatch-section.html before the existing 'Measure downtime and repair cost without double counting' heading in /journal/rental-equipment-maintenance-log/index.html. Do not duplicate it if the late-return-dispatch-window ID already exists. Set article:modified_time and BlogPosting dateModified to the actual publication date (planned October 20); preserve datePublished. Run scripts/seo-build.py to refresh the single header date, listing and sitemap. Preserve the existing feature image, downloads, styles and paid pages.

No new public URL: the indexed/nonindexed register requires no new entry. Do not mark this article indexed without GSC evidence. Publication must pass normal exact-head CI and live checks; today's source draft is not a live release or a newly scheduled automation.

## Checks

Arithmetic: actual return is 75 minutes later than 09:00; 11:00 + 30 minutes = 11:30; 11:30 - 11:15 = 15 minutes. Both linked URLs already exist. Integrated preview passed at 390px and 1440px: one section, standard header, no page overflow and working table scrolling. SEO generated-output check passed; internal-link audit found 176 pages with zero orphans/broken URLs. Preview was restored after testing; only the draft files are committed. No new image is needed for a substantive section in an existing guide.

## October 21 GSC review preparation

Use the same property, Web search type, device settings and complete-date window for comparisons. If data through October 19 is complete, compare October 13–19 with October 6–12; otherwise use two adjacent complete seven-day windows and state the cutoff. Separate USA, UK, Canada and Australia; do not combine unequal windows. Record clicks, impressions, CTR, average position, page and query, plus brand/non-brand separation. Low counts require absolute values alongside percentages.

Inspect the two repair URLs and rental guide individually: reported index status, last crawl, user and Google-selected canonical, fetch/crawl availability and exclusion reason. A successful live HTTP response is not index confirmation. Separate deliberate exclusions and duplicates from intended indexable pages. Request indexing only for eligible changed pages when the inspection evidence supports it; no mass requests or guarantee.

Prioritize actual exclusion fixes first, then existing pages with relevant impressions and weak click-through, then genuine content gaps. Compare observed queries to each page's intent before editing titles. Preserve the purchase-order-form hold until the planned October 28 decision. No GSC metrics were fetched or invented in this preparation.
