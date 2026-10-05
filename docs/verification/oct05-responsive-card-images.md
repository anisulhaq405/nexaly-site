# October 5: responsive catalogue image delivery

## Change

Add 28 WebP card variants generated from the existing 21 product thumbnails and three current homepage journal covers. Browser srcset chooses a smaller image for card width/device density. Original assets, image composition, social metadata, product galleries and article feature images remain intact. The product modal retains the original source rather than card size hints. Journal card intrinsic hints now match the existing 3:2 reserved container.

Scope: assets/js/main.js rendering helper; five generated catalogue pages; new images/cards assets. No CSS, SEO generator, product detail HTML, editorial dates, sitemap URLs, prices, checkout code or navigation changes. Header and footer markup remain byte-identical.

## Verification

- SEO publishing regression, generator check, JS syntax, whitespace and internal links pass: 121 indexable pages, 21 products, 66 journals; zero orphans/broken internal links.
- All responsive candidate files exist.
- Chromium before/after: homepage at 360/390/430/1363 px; product catalogue, both product categories, journal catalogue and homeschool product at 390/1363 px. Fourteen paired comparisons. Page heights, main heading positions and image box dimensions match exactly; no horizontal overflow or broken images. Screenshots inspected.
- Mobile navigation opens. Homeschool interactive demo loads the existing demo URL; three Polar checkout anchors remain. Exact navigation, checkout and product behavior JS preserved.
- At devicePixelRatio 1, sum of unique homepage image file sizes after scrolling: 1,515,514 bytes before; 1,109,573 bytes after at 390/430 px (405,941 bytes smaller, 26.8%); 623,495 bytes after at 360/1363 px (892,019 bytes smaller, 58.9%). These are encoded local file sizes, not measured network transfer, LCP savings or a guaranteed PageSpeed score. Source choices differ by viewport/density/cache. DPR 2 at 390 px also passed with unchanged heights/heading positions and no broken images: 1,515,514 bytes before, 1,377,538 bytes after (137,976 bytes smaller).
- External font/analytics services blocked in isolated rendering. This is local static-release verification, not a physical phone or production Core Web Vitals measurement. Compression/resizing can change pixel detail; originals remain selectable on higher-density screens. No crop or content redesign introduced.

## Release

Publish via passing latest-head CI and verify live catalogue HTML, JS and representative new image bytes. Recheck manual PageSpeed afterwards. Remaining report warnings must be inspected individually; core CSS and protected header/footer were not changed just to chase a score. Tomorrow's editorial PR117 remains separate.
