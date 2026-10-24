# Discovery and indexability review — 24 October 2026

Scope: the 41 URLs retained as Discovered–currently not indexed in the individual inspection audit. This is not all 103 URLs in the older aggregate report. The separate Unknown, reconciliation and quota-limited queues are outside this release.

## Baseline evidence

All 41 live URLs returned HTTP 200, matched the current main source, had one H1 and a correct self-canonical, and had no observed meta or HTTP noindex directive. All are in the sitemap, allowed by the public robots file and linked internally. No confirmed technical exclusion was found; this work does not claim a broken robots/canonical rule was repaired. Googlebot-specific server behavior, server logs and a new GSC live inspection were not available in this review. Google's property inspection quota had been exhausted earlier.

Thirteen target URLs lacked a main-content link from a page individually observed indexed in the saved inspection sample. This is a limitation of that sample, not proof those URLs had no indexed backlinks anywhere. We added 13 relevant main-content links from eight inspected indexed resources. All 41 targets now have at least one such source in the retained sample.

## Editorial changes

Three older overlapping planner comparisons now have different decision scopes, titles, descriptions and original tables: choosing paper/digital formats, choosing daily/weekly/monthly layouts, and checking a purchase. Publication dates remain unchanged; only these substantive refreshes receive October 24 modification dates. The generator synchronizes cards, schema, sitemap dates and JS cache revisions. Other HTML changes are generated cache references, not 205 editorial rewrites.

No redirects or URL migrations are introduced. Paid app behavior, checkouts, prices and protected styling remain under the core freeze.

## Evidence and validation

- `targets.json`: the exact 41-URL queue, with retained GSC observations.
- `baseline.json`: live pre-change responses and source/internal-link evidence.
- `inspection-reference.json`: dated indexed/discovered status reference, not a fresh inspection.
- `changes.json`: explicit source-to-target links and the 11 editorial source pages changed.
- `source-verification.json`: reproducible post-change source checks.
- `python scripts/audit-indexability.py`: checks sitemap membership, robots, canonical, directives, H1, visible content and links from the retained indexed sample.
- `python scripts/audit-indexability.py --live`: also checks production HTTP, deployed source equality and the 13 actual production links; run after deployment.

Indexability checks cannot establish Google's selected canonical or guarantee indexing. Actual inclusion requires later individual GSC checks. Review last-crawl and indexing state after roughly 7, 14 and 28 days; these are review intervals, not promised indexing dates or scheduled automations. Do not repeatedly request the same unchanged URL or bypass an inspection quota.

## Rollback

Revert this release merge through a new PR, regenerate SEO output, pass current-head CI and deploy. Baseline commit: `9aaad5460ecec41aaae21db31a1c54f9ea1e8aef`. Preserve unrelated later changes. No new credentials, external messages or indexing API submissions are part of this patch.
