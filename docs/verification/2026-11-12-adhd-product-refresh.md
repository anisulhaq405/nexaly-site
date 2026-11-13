# ADHD product-page refresh — November 12, 2026

Owner instruction: update `/planners/adhd-digital-planner/`; the owner reports it has the most impressions in their GSC. That relative priority is owner-reported. The connected Windsor account exposes only `https://mybreakeven.com/`, so Nexaly impressions, query positions, CTR and conversion baselines were not available. No numerical performance claim or projected improvement is made.

## Intent and source review

Research queries: `ADHD digital planner adult digital planner`, `ADHD digital planner for adults planner app`.

Three primary competitor pages reviewed (not verified Google positions1–3):

- https://futureadhd.com/product/future-adhd-digital-planner/ — explicit device/app fit, test page and restart-after-a-missed-day positioning. Informed a clearer compatibility check and a practical restart demonstration. No competitor endorsement or efficacy claim copied.
- https://customdigitalplanner.com/planners/adhd-planner — preview, visible example pages and section-by-section contents. Informed a grouped inventory of this product's actual navigation areas and better demo discoverability.
- https://www.tiimoapp.com/ — visual timeline, focus timer, AI planning and connected-device positioning. Informed clear separation of Nexaly's manual offline workspace from connected scheduling requirements. No invented AI, sync or notification capability added.

Nexaly primary implementation evidence: `demos/adhd-digital-planner/index.html` and `guides/adhd-digital-planner/index.html`. The demo has15navigation areas and its actual language selector contains en/ar/es/nl/fr/pt/it. The product page incorrectly listed German; this release corrects it to Dutch. The Daily Planner has Must/Should/Could fields and morning/afternoon/evening activity notes, not an auto-scheduling engine. In-page timer, temporary demo, manual backups and limits are distinguished.

## Changes and boundaries

- Retain the established title, H1, canonical, price and meta description. Without actual query/CTR evidence, there is no basis to promise a title rewrite would improve this high-impression page.
- Put free-demo and format-check links beside the main purchase information; clarify HTML format and one-time price.
- Render the actual hero image in initial HTML and add intrinsic screenshot dimensions. Existing gallery script still controls the same images; this provides a meaningful no-JavaScript/early-render fallback without altering protected code.
- Consolidate repeated buying/workflow blocks into a single sequence inside the main content. Preserve existing fragment IDs (`daily-planning-example`, `adhd-digital-planner-app`, `app-format-and-backup`, `adhd-buyer-fit`, `adhd-planner-real-day`).
- Describe a short real-world interruption test, group actual15navigation areas, compare planner formats and explain storage/device/backup limits.
- Eleven visible FAQs match their FAQPage schema exactly. No ratings, reviews, clinical efficacy, scientific validation, compatibility certification or ranking claims invented.
- Review date and sitemap updated. Only target content CSS added. Existing product scripts, styles, header/footer, demo, price, checkout URL/behavior and core baseline are unchanged.

## Verification

Use existing publishing/SEO, paid-product feedback and core-freeze checks. Focused source/DOM checks compare the previous page with the refresh: protected markup/code unchanged, anchors preserved, FAQ parity, static hero, language correction and demo launch behavior. A DOM test is not physical-device certification. Required remote rebuild gates merge; verify live page/CSS/sitemap bytes after deployment.

## November13 live visual follow-up

PR311 merged after successful required rebuild43214277531. The live page and embedded demo were observed in the desktop browser. The language selector includes Nederlands and the new content, demo links and all11FAQs are present. The product-only stylesheet loaded10rules; the content-fetch service's CSS404 was an extraction outcome rather than a browser stylesheet failure.

The browser also exposed an existing shared-selector collision: `.nx-head` had computed background rgb(44,33,23), identical to the h2 foreground. A target-only `#live-demo .nx-head` override now clears that background, preserving the light parent surface and existing heading/paragraph colors. No script, price, checkout, protected inline style or demo code changes. A versioned CSS reference ensures visitors receive this correction. Required rebuild and live visual check gate this follow-up.
