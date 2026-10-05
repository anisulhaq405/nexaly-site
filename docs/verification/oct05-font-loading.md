# October 5: storefront font loading

External Google Fonts CSS previously blocked screen rendering on 34 indexable pages. The generator now loads the identical stylesheet with print media, switching to all media after load. A noscript stylesheet preserves font loading without JavaScript. No page body, navigation, footer, prices, checkout script, product code, images or editorial dates changed.

## Evidence

Fresh Ubersuggest mobile lab report before this release: FCP 2.9 s, LCP 2.9 s, Speed Index 2.9 s, TBT 0 ms, CLS 0.044. Redirect opportunity estimates 630 ms. These are lab estimates, not real-user Core Web Vitals or measured savings.

Isolated Chromium test on homepage, homeschool product and student journal at 390 and 1363 px. With an intentionally delayed 2-second external font stylesheet, homepage first contentful paint was 2412/2388 ms before and 64/120 ms after. This demonstrates removal of the stylesheet dependency; it is not a production speed benchmark. External CSS was fulfilled with an empty stylesheet, so actual downloaded font rendering is outside that test. The original font request URLs, families, weights and display=swap remain identical. Background font arrival can still cause a text reflow, as with the existing swap policy.

All six updated-page/viewport combinations had document width equal to viewport; mobile navigation opened. Product checkout anchors remain three existing Polar links. Product interactive demo launch checked separately. Screenshots inspected. All 34 changed HTML page bodies are byte-identical to main and include exactly one deferred font link and one noscript fallback. SEO regression, generator idempotence/check, internal-link audit and whitespace checks passed: 121 indexable pages, 21 products, 66 journals, zero orphan pages and broken internal URLs.

## Remaining verification

Direct canonical HTTPS homepage returns HTTP 200 without changing URL. HTTP and www variants resolve to canonical HTTPS. Preserve necessary canonical redirects; the audit's 630 ms estimate does not justify deleting them. No hosting redirect changes made.

No Search Console connector is available in this session. Google indexing, last crawl and Google-selected canonical remain unverified. No analytics provider/property identifier was found in the inspected storefront source; USA traffic, demo starts and completed payment measurement cannot be asserted. Provider/account configuration is required before adding actual analytics events. No payment or feedback submission performed.

Publish through a passing PR and verify live HTML contains the new font loading attributes. Tomorrow's editorial draft PR117 stays scheduled separately.
