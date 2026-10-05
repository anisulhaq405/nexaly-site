# October 5: homepage render-blocking CSS

## Evidence and implementation

Anonymous isolated Chromium identifies the homepage H1 as LCP and /assets/css/style.css as render-blocking. The deferred Google Fonts stylesheet is non-blocking with JavaScript enabled. The main script at the end of body remains an existing parser-blocking resource.

On the homepage only, deliver an exact copy of the shared CSS at the same cascade position inside HTML, eliminating the additional blocking CSS request. Other pages retain their shared cacheable stylesheet. Reserve logo space using PNG-derived aspect ratios to prevent an early-paint brand-text shift. Header/footer/body markup, final layout, CSS source file, JS/checkout behavior, product details, editorial dates, sitemap and URLs remain unchanged.

The SEO build automatically synchronizes the homepage CSS and logo dimensions. The regression test proves a later CSS change fails --check until the homepage is rebuilt. URL-bearing CSS, @import and style-closing text are explicitly rejected for manual escaping/path review before future builds can publish them incorrectly.

## Tradeoff

Homepage gzip HTML grows from 7,583 to about 17,000 bytes; the shared CSS is 9,621 bytes gzipped. This exchanges a separate cold-load CSS request for CSS in HTML. A returning visitor with warm CSS cache may have different performance. This is confined to the homepage to avoid duplicating CSS across all pages. All rules are retained to preserve the complete cascade, including menus, modal and footer; no asynchronous unstyled content is introduced.

## Checks

- SEO publishing regression and generator idempotence/check passed; internal links: 121 indexable pages, 21 products, 66 journals, zero broken URLs/orphans.
- Before/after Chromium at 360, 390, 430 and 1363 px: identical measured final element geometry, page height, computed fonts, colors and backgrounds; no horizontal overflow or broken images. Mobile menus open. Screenshot reviewed.
- Controlled cold-cache local gzip server; CDP network 150ms latency, 1.6Mbps download, 750Kbps upload, CPU 4x slowdown. Fonts/external services blocked. LCP before/after: 808/372ms at 360; 904/304ms at 390; 896/296ms at 430; 1000/384ms at 1363. These illustrate removal of a dependency, not production PageSpeed/Core Web Vitals results.
- After reserving logo space, recorded local CLS is zero at 390/430/1363 and 0.00014 at 360 (baseline zero). Before reserving it, earlier paint exposed brand-text movement. Final geometry remains identical.
- No-JavaScript homepage geometry checked. Desktop search and checkout catalogue checked without payment or feedback submission.
- Exact homepage body and shared CSS content checked against main. New code is limited to generated homepage head, builder synchronization, regression test and this report.

## Release

Merge only passing current-head CI, then exact-byte-check live homepage and preserved JS/CSS. A new manual PageSpeed run is required to verify real deployment LCP/CLS; the prior 91/100 mobile screenshot is before this release. Future editorial publishing must retain this generated stylesheet block, logo reservation and existing responsive card/font-loading improvements.
