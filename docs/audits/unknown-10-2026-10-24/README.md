# Ten retained Unknown URLs — 24 October 2026

Scope: ten exact canonical URLs individually reported “URL is unknown to Google” in the retained inspection audit. This is a historical GSC observation, not a fresh inspection after this release. The earlier 41 Discovered queue remains separate.

## Findings and patch

All ten live URLs returned HTTP 200, matched main source, used the correct self-canonical, had one H1 and visible content, were present in the sitemap and allowed by robots, and had no observed meta/HTTP noindex directive. No confirmed crawl exclusion was found. We cannot infer the cause of Google's unknown state from these checks; Googlebot/server logs and a new GSC live inspection were unavailable. The GSC inspection quota had already been exhausted.

Six targets already had main-content links from an individually inspected indexed source in the retained sample. Four did not. Added four contextual links from relevant indexed articles to the iPad app comparison, digital planner app/file guide, iPad buying checklist and OwnerOS Core product page. Those four targets also had other internal links before this patch; they were not orphan pages.

No target URL migrations, redirects, robots/canonical rule changes, title rewrites, fabricated modification dates or paid app changes are needed for this patch. Existing pages and sitemap remain intact. The prior 41-URL improvements remain in place.

## Reproduce and limits

`python scripts/audit-indexability.py --audit-dir docs/audits/unknown-10-2026-10-24`

Add `--live` after deployment to verify actual production source, sitemap/robots and the four production links. The audit accepts a queue directory while defaulting to the existing 41-URL queue. `baseline.json` deliberately has `passed: false` because four lacked the sampled indexed-source path; all ten live technical eligibility checks passed. `source-verification.json` checks the new paths. Saved indexed-source observations are dated, not a fresh indexing guarantee.

Run the SEO generation/check and publishing regression suite, preserve the owner core freeze, then merge only the current-head CI-passing revision. After deployment confirm ten live eligibility/source checks plus four live contextual links. Do not describe these checks as GSC indexing confirmation. Once quota is available, inspect the exact canonical URLs and selectively request indexing where the live test succeeds; no quota bypass or repeated bulk submission is part of this release.

Rollback: revert this release through a checked PR, preserving later unrelated changes. Baseline main: `40f6aae0d23c930e96378af83e8a954e50ca0f75`.
