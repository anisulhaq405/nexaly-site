# Shipment cost allocation upgrade — November 12, 2026

Owner scope: improve `/tools/shipment-cost-allocation-tool/`, including the calculator and its content, informed by three relevant competitors. No scheduled editorial batch or paid product changes are included.

## Research boundary

Queries: `shipment cost allocation calculator`, `shipping cost allocation calculator`, `shipment cost allocation tool landed cost calculator`. Search performed November 12, 2026. Direct Google search results could not be accessed through the research service. These are three prominent relevant results in the available search, not verified Google positions 1–3. No ranking or superiority guarantee is claimed.

| Reviewed competitor | Observed public capability | Change informed |
|---|---|---|
| https://toolstic.net/shipping-logistics-tools/shipping-cost-allocation-calculator/ | Weight, volume, value, quantity and equal-share allocation; browser-local processing; scope limitations | Five explicit bases and clearer per-unit versus per-line labels |
| https://jatechnologysolutions.com/tools/shipment-cost-allocator/ | Manual/CSV/Excel lines and four-basis comparison described; freight allocation distinguished from full landed cost | Side-by-side sensitivity comparison, product CSV paste, direct-cost distinction. Our tool does not claim native XLSX upload |
| https://www.warelium.com/landed-cost-calculator/ | Volume/weight/value/quantity allocation, CSV/Excel input, per-unit measurement labels, largest-remainder cents and stale-result invalidation | Exact per-pool cent reconciliation and measurement audit; existing stale-result behavior retained |

Primary method references: https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/ and https://www.help.cbp.gov/s/article/Article1126 . Inventory cost scope and customs value are kept distinct. The tool chooses neither tax eligibility nor customs valuation and infers no tariff rates.

## Implementation

A target-only model extension adds five bases, separate freight/insurance/handling/other charge pools, known direct line costs, 6-decimal per-unit kg/CBM, integer-cent largest-remainder allocation, pool reconciliation, measurement audit and comparison. Comparison uses the entire shared-cost total under one basis at a time; direct line amounts are never redistributed.

Every line needs positive data for a nonzero pool's selected basis. Zero pools do not require that basis. Missing data never silently falls back to equal allocation. Original version 1 JSON/device saves migrate added fields to zero/default bases, preserving original shared costs and basis. Existing shared runtime files are unchanged; the new files are loaded only on this page.

CSV paste accepts 1–100 lines, required `ref,item,qty,cost` and optional `weight,volume,direct`. It parses quoted commas/newlines, rejects malformed input before mutation and confirms replacement. It replaces only rows, not settings or device saves. Money is two decimals; quantities are positive integers. CSV reports retain existing formula neutralization. No native XLSX support, FX feed, customs/tax lookup, inventory synchronization or auto-posting is promised.

The expanded original content explains driver selection, formulas, rounding, a $1,955 mixed-pool example, partial receipt scope, double-counting, accounting/customs boundaries, import/export/legacy saves, FAQs and primary sources. Original publication date October21 is preserved; modification date and sitemap are November12.

## Validation

- `node scripts/test-shipment-allocation.cjs`: independent mixed-pool arithmetic, 150 integer-rational conservation/fairness cases, direct costs, missing/zero data, duplicates, precision and original-backup compatibility.
- `scripts/test-shipment-allocation-ui.cjs` with jsdom26.1.0: actual page script order, five report tables, stale results, valid/invalid quoted CSV, unchanged state after invalid CSV, legacy import preview/confirmation, save/JSON/CSV/print/clear and safe text rendering.
- Existing ten-tool model and DOM regression passed. SEO build/check and protected core guard passed; full publishing regression and required remote rebuild gate also apply before merge.
- Local cloud-browser preview could not connect to the local server (`ERR_CONNECTION_REFUSED`); DOM tests do not certify browser visual layout or physical mobile behavior. Live verification is recorded separately after deployment.
