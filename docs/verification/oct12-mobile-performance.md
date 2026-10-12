# October 12 mobile performance repair

Owner request: repair the supplied homepage PageSpeed findings without disrupting the storefront.

## Diagnosis

Supplied report: mobile 81, LCP 5.1 s, CLS 0, TBT 10 ms; desktop 96, LCP 1.0 s, CLS 0.018. Fresh pre-change Google PageSpeed run (16:32 Karachi) varied: mobile 67, FCP 3.5 s, LCP 5.8 s, CLS 0.125, TBT 0 ms. Report: https://pagespeed.web.dev/analysis/https-nexalyplanner-com/fqy114jp3d?form_factor=mobile.

Expanded audit identifies the late Analytics preferences paragraph as the LCP element, the planner-paper block as the layout-shift culprit, and oversized card/footer images. The hero is HTML/CSS, not an image. Scores vary; do not conflate these two lab runs or describe them as real-user Core Web Vitals.

## Focused repairs

- Homepage renders the same consent panel in its initial HTML. A tiny local choice check hides it for saved accepted/rejected choices. Analytics reuses the original nodes and binds buttons without recreating the paragraph. Buttons remain disabled until handlers are ready. No optional Google Analytics request/event is emitted before acceptance. Other pages retain their existing dynamic panel fallback.
- Preload the same cache-versioned first-party Analytics script so its handler download can start before the storefront loader completes. Defer the homepage storefront script; static navigation, catalogue and planner links remain available.
- Declare the existing Fraunces/Inter families early using local Latin WOFF2 variable fonts with font-display optional, avoiding late arrival of an external font stylesheet. Original font families/weights, fallback behavior and homepage layout remain. Other pages' font delivery is unchanged. Font licenses are included under assets/fonts.
- Add smaller WebP candidates for four featured free-planner cards, two recent journal cards, RenewGuard and the homepage footer logo. Originals and full article/product feature images remain. Native auto sizes lets supporting browsers use actual lazy-image layout widths; existing sizes remains the fallback. Eager images use the fallback sizes, not auto.
- Darken only the audit-flagged homepage sticky-note, trust-bar and payment-label text for contrast. Keep the established colors/layout elsewhere.

## Regression scope and evidence

Reviewed core snapshot: all 21 protected product structures/prices/checkout URLs, demos, shared CSS, original logos and bundle selector remain identical. main.js executable differences are limited to two responsive image entries, a RenewGuard candidate, the auto sizes hint and the Analytics cache revision. Only that reviewed digest is updated, rather than regenerating the baseline.

Consent behavioral checks cover initial, accepted, rejected, blocked-storage and withdrawal cases, and ensure existing first-render markup is not recreated. Existing resource-click, product/Sheets-link, no-query-leakage and contact-draft tests remain. SEO publishing regression, generator idempotence, internal links, core guard and exact-head CI are required before merge.

Representative generated image variants visually inspected; no new imagery, crop or content redesign. Browser/live deployment and fresh PageSpeed results must be verified after merge; source checks alone cannot promise an LCP or score. No physical-phone test or AdSense account creation is claimed by this release.

## First deployed measurement and follow-up

PR178 merged at ded24f6d438abc7a551fbcbc174b84d378a3423f. Fresh 17:12 Karachi Google PageSpeed report: mobile 90 / Accessibility 100 / Best Practices 100 / SEO 100; LCP 3.3 s, FCP 2.0 s, TBT 0 ms, CLS 0. Desktop 100 in all four categories, LCP 0.4 s, FCP 0.3 s, TBT 0 ms, CLS 0. Mobile image-delivery estimate is now 9 KiB. Report: https://pagespeed.web.dev/analysis/https-nexalyplanner-com/fv5cek0eii?form_factor=mobile.

The mobile LCP paragraph is still the consent notice. Follow-up removes unnecessary cssText assignments to the pre-rendered panel/buttons, preserving their original styles while binding handlers. A regression test throws if the first-render panel or button styles are rewritten. Legacy dynamic panels retain their existing styles. This is a focused repaint repair, not removal/delay of consent choices. Recheck final deployed metrics; do not claim LCP below 2.5 s from this intermediate report.
