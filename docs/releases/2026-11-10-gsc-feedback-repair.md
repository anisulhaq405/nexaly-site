# GSC feedback endpoint repair — November 10, 2026

## Confirmed defect

The November 10 GSC export reports a 404 for
`/feedback/reviews.php?product=agency-client-profitability-capacity-os`.
Production returned HTTP 404 on November 10. The shared feedback allowlist
contained 18 entries while the paid storefront contains 21 products.
Agency Client Profitability & Capacity OS, Business Runway & Burn Rate OS,
and Cashflow-13 OS were missing. This affects public review reads and the
shared product validation used by submissions and moderation.

## Repair

Register those three existing products. Keep strict rejection of unknown
slugs, pending-review moderation, publication consent, noindex and private
customer fields intact. No customer submissions or stored records are changed.

Add a regression check comparing registration with every paid product page.
The PHP HTTP test runs in a temporary directory with synthetic records and
checks all products, unknown-product 404s, noindex, consent and privacy.

Technical-only release commits use `[skip social]` to prevent the existing
downstream publisher from retrying unrelated delivery backlog. Explicit
manual publishing and ordinary editorial releases retain their behavior.

## Baseline checks

Source audit: 243 indexable HTML pages, zero orphan pages and zero broken
internal path targets. This path-level audit does not inspect dynamic PHP
query validation; the new feedback test covers that gap.
SEO generated output is current. The protected core check passes for
21 products and 26 protected files/sections. Product prices, checkout,
design, applications and original publication dates are unchanged.

The 55 discovered and 19 crawled exclusions in the export need individual
Google URL Inspection and content assessment. These statuses alone do not
prove a robots/canonical defect. An image-directory 403 is not evidence
that its individual images are inaccessible. Intentional demo noindex and
bundle canonical alternatives are retained.

## Verification limits

Local PHP is unavailable; local registration checks run with `--source-only`.
The complete isolated HTTP test is required in GitHub CI. Production status
must be checked after deployment; this document does not assert indexing,
traffic improvement, successful deployment or successful customer submission.
