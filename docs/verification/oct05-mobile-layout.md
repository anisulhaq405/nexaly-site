# October 5 education mobile layout audit

Scope: eight October 4 pages and three October 5 journals. Tested the current main release plus the focused layout fix in local Chromium 138 at widths 360, 390, 430 and 1363 pixels (844 pixel height). This is actual browser rendering, not a source-only assertion. External network services were blocked during the isolated local test; newsletter/review submission and payment transactions were not performed.

## Confirmed issues and fix

- Newsletter input/button intrinsic width extended the document to about 397px at a 360px viewport. Stack controls below 520px and allow the input/form to shrink. Header/footer markup is unchanged; this scoped footer CSS correction is authorized by the owner’s mobile-fix request.
- Both education guides still had one unwrapped menu-reference table with a 620px minimum width. Put each table in a keyboard-focusable horizontal scroll region and use normal table layout within that region. Previously wrapped worked-example tables remain wrapped.

## After-fix results

44 page/viewport combinations have document width equal to viewport width and no broken page images. Scrollable tables retain their content inside their own container. Deliberately off-screen review honeypot inputs are not visible overflow defects. Products submenu starts closed when hamburger opens, toggles on Products, and resets after menu close/reopen. No form was submitted.

## Pages

- `/planners/digital-homeschool-planner/`
- `/planners/ai-student-planner/`
- `/guides/digital-homeschool-planner/`
- `/guides/ai-student-planner/`
- `/journal/homeschool-attendance-tracker/`
- `/journal/college-assignment-tracker/`
- `/journal/homeschool-planner-multiple-children/`
- `/journal/homeschool-schedule-multiple-ages/`
- `/journal/student-planner-guide/`
- `/journal/academic-planner-school-year/`
- `/journal/exam-study-schedule-template/`

Screenshot inspection covers headers, representative table views, newsletter/footer and product media; desktop screenshots are also captured. Source anchors and destinations are checked by the existing SEO/link audits. Publication and live verification must still be performed after current-head CI passes. No claim about indexing, traffic, purchases or physical-device testing.
