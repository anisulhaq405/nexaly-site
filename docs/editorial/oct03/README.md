# October 3 editorial release

Prepared October 2; publication is authorized for October 3 at 08:00 Asia/Karachi. Do not merge early. The feature branch contains final full HTML, not outline-only drafts. If delayed, use actual release dates, rebuild and require green current-head CI. Never claim live until deployment is verified.

## Scope

New: equipment-calibration-log, batch-lot-traceability-log, rental-equipment-maintenance-log. Three unique 1200×800 WebP covers and three original downloadable CSV starters. Five substantive updates: equipment-rental-business-plan-example, repair-shop-parts-inventory, inventory-software-without-subscription, contract-renewal-workflow, how-to-track-consignment-inventory. Original publication dates retained; modification dates planned October 3. Source bodies and exact update insertions are kept in this folder for review; deployed source lives in journal/{slug}/index.html.

New intent matches reviewed against 63 existing journals on current main. General inventory buying advice, rental business planning and existing user guides remain their own intent owners. Internal inbound links reach all three new articles from updated existing owners. Products and guides are linked with descriptive contextual anchors. Product detail pages, prices, checkout, header/footer markup and product functions remain unchanged; only normal generated catalogue/listing and script cache references change.

## Evidence and limits

Public search and page opens October 2 identified template/log intent. Thirty relevant page URLs (ten per topic including primary references) were opened; available excerpts were inspected, not a verified geolocated US Google top-ten ranking audit. The GS1 current-standard URL returned an internal retrieval error; the official GS1 traceability overview PDF and GS1 US lot identification page support the factual explanations. No search-volume, difficulty, authority, traffic or conversion estimates are asserted. No private keyword or Search Console export is uploaded.

Primary factual references:
- NIST recommended calibration interval: https://www.nist.gov/calibrations/recommended-calibration-interval
- NIST metrological traceability policy: https://www.nist.gov/calibrations/traceability
- GS1 traceability overview: https://www.gs1.org/docs/traceability/GS1_tracebility_what_you_need_to_know.pdf
- GS1 US lot identification: https://www.gs1us.org/upcs-barcodes-prefixes/gs1-128
- OSHA 1926.20: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.20 (explicitly construction scope, not universal party-rental checklist)

Examples and calculations are original and fictional. Verified April 6 + 180 days = October 3; December 31 minus 90 days = October 2; 50 units = 2 rejected + 30 shipped + 18 on hand; 11 kg input = 10 kg fill + 1 kg documented loss; $135 repair = $45 parts + 2 × $45 labor; $207 repair/opportunity scenario = $135 + $90 − $18; $18 settlement difference = $108 − ($180 − $30) × 60%. Intervals, legal interpretation, equipment acceptance and regulatory decisions are not delegated to the app.

Actual live demo screen verification October 2: CalibraTrack calibration schedule displays instruments, intervals and due dates; BatchTrace embedded Trace & Mock Recall displays source → batch → finished lot → destinations; RentFlow Maintenance & Downtime displays asset, work, window, available-after time, vendor, cost and status. Source code and product descriptions checked for claimed workflow limits. No live customer data entered. These checks do not certify every product function.

## Feature images

Generated with built-in imagegen; final assets images/journal/{new-slug}-20261003.webp. Reviewed 3:2 composition, topic fit and legible titles. Conceptual editorial photos, not authentic product screenshots; articles label this.

Prompt briefs: calibration — metrology bench with caliper, micrometer, reference blocks and record clipboard; exact title CALIBRATION LOG, navy/copper. Batch — candle maker workbench with labeled materials, finished candle groups, production ledger and shipping carton; title BATCH & LOT TRACKING, copper/teal. Rental — event-rental warehouse with moving-head light, flight case, cable and service-hold tag; title RENTAL MAINTENANCE LOG, navy/amber. All: no logos, software mockup, certification badges or watermark.

## Release checks

Local SEO build, regression, freshness, JS syntax, diff and internal-link audit pass: 121 public pages, 21 products, 66 journals; zero orphan or broken internal URLs. CSV samples parsed and calculations checked. Current-head GitHub CI must pass before merge. Live article/image/download/card/sitemap/date/links and responsive rendering checks remain for the scheduled deployment; pre-release source eligibility is not Google indexing.
