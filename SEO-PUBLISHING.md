# Automatic technical SEO

Publish complete product pages at `planners/<slug>/index.html` and complete articles at
`journal/<slug>/index.html` in this repository. GitHub Actions runs after pushes to
main, updates generated files, and commits the output. Hostinger remains the existing
deployment provider. This is post-push maintenance, not a pre-deployment gate.

The pipeline discovers published pages, maintains unique self-canonicals and social
metadata, generates sitemap.xml, and synchronizes static and JavaScript catalogues.
New articles appear first after initial migration. Existing catalogue titles, prices,
categories, imagery, checkout logic, header, footer and CSS are preserved.

Existing metadata is retained where appropriate. A missing title is derived from the
H1; a missing description comes from the first substantive paragraph. These are fallback
values, not a replacement for writing accurate product information.

New product pages need a real price in Product JSON-LD offers or a
`product:price:amount` meta tag. Provide `nexaly:category` as `Digital Planners` or
`Business Operating Systems` for automatic category placement; otherwise the product
appears in All Products. Supply a real `og:image` and the actual checkout link in the
page. Never fabricate a price, review, stock claim, AI capability or checkout URL.

Use `noindex` in robots metadata for drafts/private pages. They are excluded from
the sitemap and generated catalogues. Changing an established URL requires a hosting
redirect; this tool does not guess deleted-page destinations.

Run `python3 scripts/seo-build.py` before committing for a single-step publish, or let
the automatic workflow maintain output after a push. Run `--check` to verify generated
output is current. Python 3 and Node.js are required, with no package installation.

A workflow failure is visible in GitHub Actions. Existing Hostinger auto-deployment
does not wait for this job, so invalid source changes can still reach the host.
GitHub Actions must remain enabled with permission to commit generated files.
Hosting availability, Google indexing, rankings, factual copy, image quality and
payment-provider setup remain outside this generator's guarantees.
