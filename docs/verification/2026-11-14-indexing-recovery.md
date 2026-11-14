# Indexing recovery — November 14, 2026

## Evidence and limits
Six owner GSC exports reconcile to 83 URLs: 55 discovered, 15 crawled/unindexed, 8 intentional noindex, 3 canonical bundle variants, one review API 404 and one asset-directory 403. Only 58 are public HTML content targets (55 plus three crawled content pages). Charts stop November 9; last-crawl fields for individual rows can be later. The 1970-01-01 placeholder in discovered rows is not a historical Google crawl date.

Public range fetches succeeded for all 58 content URLs, with complete bodies under the range cap, self-canonicals and no noindex directive/header. Range responses are expected 206, not normal full-GET status evidence. Separate ordinary GETs returned 200 for robots, sitemap and the three crawled content pages. The reported API 404 now returns 200 JSON with X-Robots-Tag noindex. The image directory still returns 403; opening directory listing is not a remedy for content indexing.

All 55 discovered content URLs have sitemap entries and ordinary HTML incoming links; shortest static navigation distance is one or two steps. There is no evidence of a current blanket crawl block, orphan URLs or missing sitemap entries. Public requests are not Googlebot identity checks and do not establish historical host capacity. Google-selected canonical, URL Inspection outcome, Crawl Stats, server logs and WAF events were unavailable. No sitemap submission or indexing request was performed or claimed.

## Focused repairs
- Correct stale 50-planner metadata and all-planners fallback count to the actual 60 directory cards. The source has 66 tool landing URLs; six are linked resource pages outside the main card collection. Remove the inaccurate claim that downloads and browser worksheets are wholly separate.
- Improve the homeschool budget page with shared-versus-individual purchase boundaries, payment reconciliation and clear answers. Add relevant incoming links from multi-child planning and attendance guides.
- Replace the travel-agency article's terse one-line FAQ with a booking-reconciliation workflow, isolated commission-reversal scenario and full answers, linking dated cash and business-plan worksheets.
- Add a measured print-fit procedure to the sizes chart and contextual incoming links from daily/monthly planner guides.
- Preserve original publication dates, URLs, feature images, prices, checkout, demos and shared executable/CSS behavior. Refresh modification dates only on substantively edited pages.
- Review the iPad/2026 clusters. Existing pages explicitly distinguish file choice, app workflow, purchase checks, PDF import and free options. No automatic merge/redirect is justified by the available evidence. No unsupported claim that the content is rejected or low quality.

## Validation and follow-up
The regression guard covers all 58 targets: index eligibility in source, self-canonical, sitemap membership, crawlable robots, HTML-link discovery depth <=2, incoming links, original dates and retained intentional exclusions. Independent arithmetic checks cover shared subscriptions, planned versus paid amounts, commission reversal and print scaling. Standard SEO/publishing and protected-core checks remain required.

Generated catalogue date changes update main.js and its cache reference throughout public pages; those reference changes do not rewrite other articles or products. Publish only after successful exact-head rebuild, then inspect actual deployed pages and links. Recheck priority URLs in authenticated GSC URL Inspection and Crawl Stats when access is available. Do not equate live eligibility, sitemap submission or a recrawl request with indexing.
