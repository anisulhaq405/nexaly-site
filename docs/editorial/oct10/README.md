# October 10 procurement workflow release

## Scope

This batch strengthens four existing owners and creates no new URL or product:

- `/planners/inventory-procurement-planner/`: buyer fit, manual boundaries, partial-receipt handoff and browser-local backup ownership.
- `/planners/vendorpulse-os/`: buyer fit, quote-to-PO decision boundary, scorecard evidence limits and browser-local backup ownership.
- `/journal/purchase-order-tracker/`: reorder-to-PO handoff with an open-order and cancellation example.
- `/journal/reorder-point-small-business/`: controlled purchase-request handoff and reciprocal purchase-order next step.

The two supplier journals already contain complete comparison/scorecard tables and worked examples, so they were not padded or date-refreshed in this first day of the October 10–12 window. They remain candidates for a focused evidence-to-action review on October 11–12.

## Accuracy and boundaries

Claims were checked against the current product pages, guides and demo source. The copy states that both products are downloadable HTML browser apps with local records and manual JSON backup. It does not claim cloud sync, supplier messaging, automatic approval, external inventory synchronization, independent certification or automatic off-device backup. Fictional calculations are labeled and reconcile: `32 + 24 - 8 = 48`; after 12 inbound units are cancelled, `32 + 12 - 8 = 36`; `970 / 1000 = 97%`.

This update does not change price, checkout URLs, executable product/demo behavior, shared styles, header/footer markup, navigation, images or the protected core baseline. Original journal publication dates remain; substantive modification date is October 10, 2026.

The first CI run exposed that the catalogue generator rewrote only the shared-JavaScript cache query on protected `bundles/index.html`. The generator now deliberately leaves that core-locked checkout page's reviewed script revision unchanged. This preserves the protected byte baseline while other public pages receive the current generated catalogue revision; no checkout behavior or baseline was changed.

## Release gates

Run the SEO builder, generated-output check, publishing regression suite, core-lock guard, internal-link audit, JavaScript syntax check and whitespace check. Review the protected diff, require green CI on the exact PR head, merge only that head, then verify the four live pages, journal card dates, sitemap entries, images and responsive layout. A successful deployment confirms availability, not Google indexing or performance uplift.
