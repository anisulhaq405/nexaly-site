# ADHD screenshot proportions — November 13, 2026

Owner supplied a full-page screenshot showing severe vertical stretching after the product-page refresh. Live DOM measurements confirmed seven screenshot images rendered about345px wide but retained the newly added2240–3040px HTML height attributes. The existing CSS set width:100% without a responsive height declaration. The prior dimension additions therefore introduced the regression.

Add target-only `.pd-more .pd-shots img{height:auto}` and version the existing target stylesheet reference. Preserve intrinsic width/height attributes, image files, grid column structure, protected inline CSS/scripts/header/footer, checkout, price and all content. This restores natural proportions while keeping dimension-based layout reservation. No shared asset or demo changes.

Release acceptance: required rebuild succeeds; live browser checks every image's rendered width/height against naturalWidth/naturalHeight (within1CSSpx), then visually inspects the screenshot grid. Verify a narrow layout if the browser exposes a supported resizing method; otherwise report the limit rather than claiming physical-device certification.
