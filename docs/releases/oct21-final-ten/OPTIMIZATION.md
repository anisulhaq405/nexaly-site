# Ten-planner audit and cover refresh

Replaces all ten feature images with unique topic-relevant generated editorial covers. The accurate SVG worked examples remain in the guides. Covers use responsive 480/960/1200px WebP, explicit dimensions, eager hero loading and lazy directory loading. Small covers are approximately 17–32KB; full covers 58–132KB. Alt text describes actual scenes. Social/schema images use the full covers.

## Actual defects fixed

- New model/UX/CSS files had no cache revision despite 30-day static caching. The SEO builder now adds content-hash revisions, preventing stale browser code after releases.
- Native validity checks did not focus whitespace-only required text or duplicate references. Scoped error handling now focuses and marks the relevant field on calculate, CSV and print.
- Added automated UI regression tests for these ten planners to required CI.

## Reverse-engineered rules

| Planner | Reviewed behavior |
|---|---|
| Dead stock | Receipt/sale chronology; inactivity threshold; zero stock; cost cents; leap day and total overflow |
| Returns | Sellable + rejected + pending reconciles to returned units; future receipts rejected |
| Clearance | Markdown price, revenue, fees and contribution; zero revenue and negative contribution |
| Shipment | Units/value weighting; positive quantity; zero weight rejection; largest-remainder exact cents |
| Repair handoff | Open/handed-over distinction; overdue dates; approval/parts blockers |
| Rental | Returned <= dispatched; held <= returned; inspection decision before release candidates |
| Calibration | Approved date chronology; active/out-of-service; today and look-ahead boundaries |
| Batch expiry | Date ordering; disposed units must be zero; date status does not authorize release |
| Tasks | Ready/blocked/completed effort and capacity gap |
| Trials | Calendar-day buffer; lower date bound; requested cancellation remains active until confirmed |

No reproducible arithmetic defect was found in the tested cases; model arithmetic is preserved. Added leap-day, 100-row, precision and 100 deterministic shipment conservation cases.

## Verification and reproduction

Model and DOM tests cover samples, malformed/duplicate records, backups, import confirmation, wrong-tool rejection, CSV escaping, safe text rendering, print calls and storage failure. Desktop 1440px and mobile-emulated 390px Chromium flows cover save/reload/restore, imports, exports, images, overflow and page errors. Physical phones and every browser version are not certified.

SEO generation/regression, zero broken/orphan internal pages and protected-core checks are release gates. Exact-head CI must pass before merge; live verification follows deployment.

`apply-covers.py` is idempotent and runs after the original page generator. `cover-manifest.json` records source image names, alt text and output sizes. Image concept: natural-light commercial scenes representing each tool's use, cream palette, distinct accent colors, no branded UI screenshots. Encoding: Pillow Lanczos, WebP quality 78/method 6.

No new URL, paid-product, checkout, price or shared-core style change. Existing URL-register entries remain valid. PR206 editorial work is separate.
