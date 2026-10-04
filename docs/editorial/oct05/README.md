# October 5 student planning draft

Prepared October 4, 2026. **Draft only. Do not merge before the October 5 08:00 Asia/Karachi publishing run.** A one-time release run is scheduled for this draft; the earlier recurring topical task is paused. Do not create a duplicate timer.

## Scope

| Existing URL | October 5 change |
| --- | --- |
| `/journal/student-planner-guide/` | Move the previously appended two-deadline example into the planning sequence; add a concrete procedure for handling a changed due date without duplicating the official record. |
| `/journal/academic-planner-school-year/` | Move the workload example before FAQs; add a term-calendar change check that reconciles the official school calendar, course source, and weekly blocks. |
| `/journal/exam-study-schedule-template/` | Move the missed-session recovery before FAQs; show how two exams can compete for the same limited block; replace unrelated recommendations with the relevant education cluster. |

No new URL, product, download, price, claim about ranking, or AI capability. Keep original publication dates, planned modified date October 5. Examples are fictional and arithmetic is explicit. The school/course source remains authoritative for dates and submission requirements. Existing articles already had substantial October 2 additions; this pass places those sections in the reading flow and adds only the missing decisions.

## Release gate

1. Rebase onto the latest main, including today's guide-table CSS fix if merged; resolve any unrelated changes rather than overwriting them.
2. Rebuild metadata/cards/sitemap with `scripts/seo-build.py`; run `scripts/test-seo.py`, `scripts/seo-build.py --check`, `scripts/audit-internal-links.py`, JavaScript syntax and diff checks.
3. Inspect all three pages on an actual narrow viewport and a desktop viewport. Check table scrolling, images, header menu, footer, internal anchors and links. Source-only inspection is not a mobile visual pass.
4. Require green CI for the exact head, then publish no earlier than October 5 08:00 Asia/Karachi. Verify live paths and append truthful release evidence. Do not create duplicate pages or merge the draft today.

Today's eight-page mobile visual audit remains open: the available cloud browser viewport was 1363px and the user's separately opened tab was not exposed in that browser session. The source audit identified the guide-table offset and PR #114 contains the scoped fix. Do not record an eight-page mobile visual pass until a true phone-size rendering is inspected.
