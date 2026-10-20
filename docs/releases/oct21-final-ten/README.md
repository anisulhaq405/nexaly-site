# Ten free planners — October 21, 2026

Owner authorized completion and publication to bring the directory from 40 to 50 planners. Selected ten absent routes from the existing backlog; no exact pre-agreed ten-name list was found. This release adds ten focused worksheets and ten separate input/workflow guides. It does not implement draft PR206.

## Implementation
- Separate final-ten configuration/model/theme files reuse the existing tested save, restore, backup, CSV and print controls.
- Ten original SVG worked-example diagrams; these are exact illustrative diagrams, not product screenshots or claimed photographs.
- Unique references, input/date validation, bounded fields, quantity reconciliation, calendar-day boundaries, cent-accurate shared-charge allocation, separate inspection/approval decisions.
- Each page links its guide, a related free planner and existing journal. The directory has 50 searchable cards; sitemap contains 198 indexable pages and 82 journals.
- No paid pages, checkout, pricing or shared styles changed.

## Verification
- scripts/test-final-ten.cjs passes samples, invalid dates, duplicate and empty records, stock reconciliation, markdown limits, fractional-cent allocation, inactive records and cancellation confirmation.
- Browser checks pass all ten worksheets at 390 and 1440 pixels: sample, save/reload/restore, JSON download/import, CSV, print invocation, PDF generation, image load, no page overflow or JS errors. Physical mobile devices were not tested.
- SEO build, regression and freshness checks pass; internal links: zero broken URLs and zero orphans; protected-core check passes.
- Model tests added to required CI. Green exact-head CI and live verification still required for publication.

## Source and limits
NIST calibration interval guidance reviewed October 21: https://www.nist.gov/calibrations/recommended-calibration-interval . Calibration planner takes an approved due date; it does not recommend intervals or authorize use. Stock and task examples are original fictional calculations. No new keyword volume or ranking claims. GSC remains deferred.

## Rebuild
Run build.py for configs, then generate final-ten-models.js from the configuration plus models-body.js (wrapper uses small-tools-models.js). Run pages.py, then scripts/seo-build.py. The page generator is idempotent for directory cards. Keep reviewed dates truthful when releasing a later revision.
