# Five business guides: editorial lock - October 29, 2026

Scope: the five article files in `oct29-five-blog-lock.sha256`. This closes the PR #286 editorial batch after a reverse review of the published examples and their linked worksheet models. Preserve the accepted content unless the owner requests a change or new evidence establishes a specific defect. This is a recorded baseline, not a claim that future rankings or indexation are guaranteed.

## Reverse-review findings and narrow improvements
- Financial projections: model output matches the published operating/cash examples. Clarify that package quantities/hours are preparation calculations and billing must not be added to receipts.
- Construction: reducing the milestone amount to 2700 produces base closing 2000 and confirmed-only closing -700 while status remains Expected. Clarify that an agreed amount is not confirmation of collection timing.
- Interior design: enter 30 base hours plus eight change hours. The extra scope costs 500; an extra fee of 500 restores contribution dollars to 1300, while zero extra fee leaves 800. Entering 38 base hours plus eight change hours reproduces double-counting. Clarify the exact fields without changing the calculator.
- IT consulting: the capacity model reports 28 available, 34 booked and -6 free hours. The separate client-overage example reports seven hours, 700 potential charges and zero confirmed charges. Clarify separate tools and that the monthly retainer fee is not an overage input.
- Trucking: 1372 revenue with 100 empty miles produces 502 trip remainder; 1412 revenue with 150 empty miles produces 500 remainder and 912 total cost. Clarify total-revenue entry versus per-mile quote arithmetic.

## Validation
Executed the actual keyword-workflows, small-tools and next-tools model suites and additional disposable scenario checks against the guide assumptions. Generated-output check returned no changes; protected-core guard passed. Checked all five article structures, duplicate IDs, local links/fragments and editorial image paths/dimensions/alt text. Both external reference destinations (SBA business planning and business.gov.au budgeting) were retrievable. No executable model, UI, pricing, checkout, artwork, dates or shared cache references changed in this correction.

## Lock verification
From the repository root:

```bash
sha256sum -c docs/verification/oct29-five-blog-lock.sha256
```

The manifest checks these five article bytes. It does not freeze unrelated articles or tools and does not enforce GitHub branch protection. For a later authorized edit, review the specific change and refresh the corresponding baseline deliberately. Keep existing SEO, tool-model and protected-core checks in place. Publish through a passing PR and independently compare live output with the source; the manifest alone does not prove deployment, mobile rendering or Google indexation.
