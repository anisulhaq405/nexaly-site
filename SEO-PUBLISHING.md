# Validated technical SEO publishing

Main is the existing Hostinger deployment branch. Publish every content batch through a feature branch and pull request.

1. Add or update complete pages under journal/<slug>/index.html or planners/<slug>/index.html.
2. Run python3 scripts/seo-build.py to generate canonical/social metadata, sitemap and static/JavaScript listings.
3. Run python3 scripts/test-seo.py, then python3 scripts/seo-build.py --check.
4. Commit all source and generated changes together.
5. Open a PR to main. Wait for the rebuild status check on the current revision; merge only when successful.
6. Verify the live deployment, article/listing content and sitemap.

The workflow is read-only. It checks committed generated output BEFORE running isolated regression tests. It no longer commits directly to main after deployment, so it is compatible with mandatory PR protection. Stale generated output fails CI instead of reaching main through the approved flow.

## Validation and protected scope

Validation rejects missing internal targets (including header/footer links), duplicate document titles/descriptions, invalid JSON-LD, missing images and invalid/mismatched product price or checkout data. The legacy-link exceptions have been removed after the owner's authorized navigation repair.

Checkout validation checks HTTPS Polar URL structure and consistency, not payment-provider availability; no payment is made. Existing product detail files, product catalogue, prices, bundles, CSS, worker and checkout JS are preserved by tests. Journal cards refresh title, description, image and alt text from page metadata. Publication dates and editorial order are retained.

New products need their real price, an existing image, actual HTTPS Polar checkout link, and the appropriate nexaly:category (Digital Planners or Business Operating Systems). Noindex drafts stay out of sitemap/listings. A custom draft status also needs robots noindex. URL changes need genuine hosting redirects; never redirect an unavailable calculator to an unrelated product.

## One-time GitHub enforcement activation

The prepared ruleset is docs/nexaly-main-protection.json. It requires a PR, an up-to-date successful rebuild check, blocks force pushes/deletion, and has no bypass actors. It allows the solo repository owner to merge their own passing PR (zero mandatory reviewers).

Repository administrators must import this JSON under Settings > Rules > Rulesets > New ruleset > Import a ruleset, review Active enforcement and main targeting, then Create. Saving the JSON in git does not activate protection. The connected GitHub tools do not expose administration writes.

After activation, verify the ruleset is Active and main is protected through GitHub's rules/branch endpoints. Do not claim enforcement until verified. Direct Hostinger uploads remain outside GitHub's rules. Hosting/TLS, performance and Google indexing require separate live verification.

The four broken legacy navigation destinations in the old AI-business journal have been replaced with existing category, Journal and Business Copilot pages. Design and unrelated links remain unchanged.
