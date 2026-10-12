# AdSense integration: account-dependent next steps

Status on October 12, 2026: no AdSense account associated with the NexalyPlanner Google account; owner confirmed this is their first account. Site-readiness repairs are in the October 12 batch. Advertising is not active.

## Account and ownership

1. Owner creates the first AdSense account using their actual country and account information, checks eligibility and accepts Google's Terms themselves. Do not infer payment country from a timezone or invent payment/identity details.
2. Add `https://nexalyplanner.com` and use an ownership method actually offered by the account. Prefer a non-serving verification method when available while consent setup is unfinished. Use only the real account snippet/ID; Google Analytics ID is not an AdSense publisher ID.
3. Add the exact account-provided authorized seller line to root ads.txt when the publisher ID is available. ads.txt is recommended, not a substitute for site review. Do not publish a placeholder publisher ID or guess one.

## Consent before ad activation

1. Configure Google-certified advertising consent messaging for the applicable EEA, UK and Swiss traffic, using the account's Privacy & messaging options. Existing Analytics settings are not a certified advertising CMP.
2. Review applicable US state privacy messaging/options in the account; do not claim that a generic banner satisfies every jurisdiction.
3. Update the privacy page to describe the active providers and controls after the actual configuration is known. Replace planned/inactive wording only once it is true.
4. Test accept, reject and change/withdraw choices, including Google's documented message preview parameters. Avoid overlapping Analytics and advertising banners or silently granting advertising consent from an old Analytics choice.

## Placement plan

Start with useful journal articles. Exclude checkout/pricing screens, product feedback/contact forms, error/thank-you screens, app demos, offline app files and downloadable resources from ad serving. Keep advertisements visually separate from download and Google Sheets-copy buttons; do not encourage clicking ads.

This is a placement plan, not a configured AdSense exclusion list. Confirm the actual account's page exclusions and ad settings before activation; verification snippets, automatic ads and ad units have different roles.

## Review submission

Verify ownership, crawler reachability, complete pages, genuine resources and the account's required setup/identity steps before submitting review. No first-account application, review request, CMP publication or ad serving has occurred in the readiness batch. Record actual status and any rejection reason before deciding on another content repair. Do not claim request success means approval or indexing.
