# All 21 product journeys — October 5, 2026

Source base: 48cf28c088c518b0bc8ecf03c22603b22bf0688f. The first three products were verified in the preceding PR121 audit; the remaining eighteen were individually visited in the desktop cloud browser (1363px viewport), their demo launcher was clicked, the embedded interface was observed after load, and a product purchase link was clicked to inspect the actual Polar checkout.

## Product matrix

| Product route slug | Embedded demo | Guide | Single checkout |
|---|---|---|---|
| adhd-digital-planner | Loaded | Linked | Correct product, $11.99 |
| agency-client-profitability-capacity-os | Loaded | Linked | Correct product, $11.99 |
| ai-student-planner | Loaded | Linked | Correct product, $11.99 |
| batchtrace-os | Loaded | Linked | Correct product, $11.99 |
| boutique-business-planner | Loaded | Linked | Correct product, $11.99 |
| business-runway-burn-rate-os | Loaded | Linked | Correct product, $11.99 |
| calibratrack-os | Loaded | Linked | Correct product, $11.99 |
| caregiver-planner-aging-parents | Loaded | Linked | Correct product, $11.99 |
| cashflow-13-os | Loaded | Linked | Correct product, $11.99 |
| consignclear-os | Loaded | Linked | Correct product, $11.99 |
| content-marketing-planner | Loaded | Linked | Correct product, $11.99 |
| digital-homeschool-planner | Loaded | Linked | Correct product, $11.99 |
| inventory-procurement-planner | Loaded | Linked | Correct product, $11.99 |
| offline-ai-business-copilot | Loaded | Linked | Wrong displayed product: RepairBench |
| owneros-core | Loaded | Linked | Correct product, $11.99 |
| renewguard-os | Loaded | Linked | Correct product, $11.99 |
| rentflow-os | Loaded | Linked | Correct product, $11.99 |
| repairbench-os | Loaded | Linked | Correct product, $11.99 |
| sales-management-system | Loaded | Linked | Correct product, $11.99 |
| small-business-planner-2026-2028 | Loaded | Linked | Correct product, $11.99 |
| vendorpulse-os | Loaded | Linked | Correct product, $11.99 |

All eighteen remaining product pages had no document overflow at the observed desktop viewport. Their guide links were present, including the deliberately different /guides/small-business-planner/ route. Small Business language onboarding (English → Get started) exposed its dashboard; Content Marketing Skip for now exposed its dashboard without setting a password. These are entry/checkout smoke checks, not exhaustive feature, calculation, accessibility or mobile-device certification. The initial empty ConsignClear checkout snapshot was a loading state; the completed checkout showed the correct product and $11.99.

## Bundles

- Any 3: preceding audit selected Boutique, Inventory and OwnerOS, $25.99 and reference_id=b3-boutique.inventory.owneros.
- Any 5: Student, RepairBench, Homeschool, ADHD and Boutique; correct $39.99 checkout, reference_id=b5-student.repairbench.homeschool.adhd.boutique.
- Any 10: those five plus Small Business, Caregiver, Inventory, OwnerOS and BatchTrace; correct $69.99 checkout, all ten selection IDs in reference_id.
- Whole Collection: title All 21 Products and $109.99, but public description still says all 15. Download benefits are not certified from the title.

No payment information entered, payment completed, download delivery verified, feedback submitted or account record changed. Purchase links open payment forms; successful charges and fulfilment remain untested.

## Open provider exceptions

Copilot uses a distinct link polar_cl_xqL0Mx8Vxk2IiMH9tENfft5QH6tZ4CQFLEPed24slVT but Polar displays RepairBench OS — Small Engine Repair Shop Manager with a Copilot return link. RepairBench's own link is polar_cl_LDfhqo384rYgSE1QMxqnNVTvf9jqYVQqYfUiL4Yx0Ps. This is a confirmed displayed identity mismatch; it does not establish which download is attached. Verify the product identity and downloadable benefit in Polar before renaming or substituting a URL. Whole Collection's 15-versus-21 public description is a separate provider mismatch. The current admin browser is at a sign-in wall, so neither exception was changed.

## Site and freeze checks

Current source link audit: 121 indexable pages, 21 products, 66 journals, zero orphan pages and zero broken internal targets. Bulk HTTP/source comparisons are recorded in oct05-all-products-http.json; inspect explicit errors rather than claiming all passed from source tests alone.

Owner-requested freeze protects existing demo HTML, shared CSS, logos, bundle page, behavior portion of main.js, and each product's header/footer/styles/scripts, structured prices and Polar URLs. Product/post catalogue JSON and prose/FAQ updates remain allowed. Controlled verification proved an editorial text change passes while unexpected main.js behavior-section drift fails; files were restored afterwards. Existing publishing tests, SEO build/check, syntax and diff checks remain required. Core freeze is a CI safeguard, not immutable hosting or verified GitHub branch-rule administration. Provider exceptions remain open under the freeze.

Fresh mobile rendering and all-feature calculation accuracy were not checked here. Prior speed/mobile releases are preserved without making new mobile claims.
