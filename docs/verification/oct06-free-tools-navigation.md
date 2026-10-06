# Free tools navigation — 6 October 2026

Owner authorization: adjust navigation for the 50 planned free planners/tools to fit design, SEO discovery and usability.

Adds exactly one `Free Tools` link after Products in each existing storefront navigation. Keeps original design; adds a narrowly scoped 781–1100 px menu spacing rule. Preserves checkout links, pricing, demos and executable behavior unchanged. Before the tablet spacing rule, existing HTML diffs were checked against the previous revision: removing the inserted menu link restores byte-identical original content. The owner-authorized menu addition changes protected product-header hashes and the bundle hash; the baseline was deliberately refreshed after this comparison and browser tests passed. A second deliberate update includes the authorized tablet menu spacing rule; no checkout or demo behavior changed.

The `/tools/` directory has eight category anchors, one working tool and an available-tool search. Planned tools have no fabricated live links or published empty detail pages. Category anchors do not create separate duplicate sitemap URLs. SEO generation retains the Free Tools link without duplicating it.

Local Chromium checks passed at 360, 390, 768, 820, 1024 and 1440 px: menu visibility, mobile burger state, one Free Tools link, direct navigation, category anchors, search success/no-match/reset, no document overflow and no runtime errors. Desktop and mobile screenshots inspected. Existing product page menu checked. SEO generation consistency and core freeze pass. Existing publishing regressions run before release.

This change improves discovery and navigation; it does not guarantee Google indexing or an authority-score increase. New tools must be fully functional and tested before cards and sitemap entries are added.
