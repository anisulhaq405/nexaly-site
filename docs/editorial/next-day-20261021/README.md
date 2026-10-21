# Next-day editorial draft — prepared October 21, 2026 (Asia/Karachi)

Status: CONTENT DRAFT SAVED; NOT IMPLEMENTED OR PUBLISHED. Owner requested morning implementation after draft preparation. No automated morning deployment is scheduled.

## Deliverables

1. Complete boutique inventory article draft. Correct the contradictory free-workbook FAQ, link the existing actual XLSX, and add a 437-word period-rollover walkthrough with a four-stage worked table and contextual inventory-count link.
2. Complete sales/inventory article draft. Replace the paid-product link mislabeled as an example download with an actual static CSV example. Replace nonexistent linked-workbook/tab claims with explicit CSV limitations and a four-checkpoint numerical workflow. Remove a product image incorrectly captioned as an exact worked calculation and replace it with the relevant count-guide link.
3. Four-row original CSV with order, stock, reservations, cash, fulfillment amounts and cost fields.
4. Guarded application script, manifest and validation notes.

These are refreshes of existing intent owners, not two new blogs. Existing feature covers are retained. No new public journal URL, paid-page edit, checkout, shared CSS or product-feature change. Headers/footers and original publication dates are preserved. Draft previews retain current modification dates; the application script sets the actual implementation date when run.

## Why this scope

The current monthly plan prioritizes existing inventory owners and discourages duplicate URLs. The October 21 release tracker primarily calls for monitoring; GSC remains deferred by the owner. The two concrete content defects above justify targeted corrections without claiming performance evidence. October 21 batch/calibration work was already prepared in PR204. The owner reports the two PR205 blogs published; no fresh live verification is claimed here.

Source files checked at base commit 574666dd91986de2f4a8e6a1539b7d2300ca7318. No new keyword-volume or ranking claims. Historical keyword estimates were not copied into this public repository.

## Source review

Reviewed October 21:
- https://help.shopify.com/en/manual/inventory-and-locations/fundamentals/inventory-states
- https://help.shopify.com/en/manual/inventory-and-locations/inventory-counts/performing-and-reviewing-counts

Used to cross-check stock-state distinctions and count review only. All new figures and examples are original fictional operational illustrations. No compliance or accounting-policy advice. Retained product claims are existing copy, not new verification.

The supplied local attachments could not be opened because the execution environment is unavailable. Their contents were not claimed as read. Existing repository editorial instructions and the current saved monthly plan/release tracker were read.

## Checks completed

- Exact original text matched before each replacement.
- One H1 on each full-page draft.
- All relative internal href paths resolve against the current repository tree, including the staged CSV.
- Local fragment links resolve.
- Four CSV rows checked arithmetically: stock, availability, unpaid balance, fulfilled amount, fulfilled cost and merchandise margin.
- Original publication dates, shared header/footer and existing covers retained.

## Remaining release gates — not passed yet

Local execution is unavailable. Python apply-script execution, generated-output rebuild, browser/mobile rendering and live HTTP/download checks have NOT run. A green PR check here validates the unchanged published source tree, not an applied release. This package is not claimed 100% deployment-ready.

## Morning implementation

1. Rebase/review against current main. The apply script rejects changed source blobs and an existing CSV target.
2. From repository root run:
   python3 docs/editorial/next-day-20261021/apply.py --date ACTUAL-YYYY-MM-DD
3. Run python3 scripts/seo-build.py, python3 scripts/test-seo.py, python3 scripts/seo-build.py --check and the protected-content/link checks.
4. Preview both pages at mobile and desktop widths. Confirm standard single date header, table keyboard scrolling, working XLSX/CSV links and retained cover placement.
5. Commit applied source plus generated output; update publication log. Require green exact-head PR checks before merge.
6. Only after morning authorization/implementation: deploy, verify both live pages and downloads, and update the existing URL register. No indexing status change without GSC evidence.

Do not merge this docs-only PR expecting publication: the production paths intentionally remain untouched.
