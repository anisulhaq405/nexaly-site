# NexalyPlanner deployment-triggered social publishing

Make scenario: https://eu1.make.com/3058803/scenarios/7793204

Publishing destinations configured: NexalyPlanner Facebook Page, @nexalyplanner Instagram,
Pinterest Business Planner board, and verified @NexalyPlanner YouTube channel.
TikTok and X remain unconfigured; do not claim that all six platforms are active.

## One-time activation

1. Configure GitHub Actions repository secret `MAKE_NEXALY_SOCIAL_WEBHOOK_URL`
   with the webhook URL from the NexalyPlanner Make scenario. Do not commit the URL.
2. Verify and activate the Make scenario after its payload structure is learned.
3. Merge passing source changes to main through a pull request. The first successful
   technical SEO run initializes an archive baseline without sending old content.
4. Run the social workflow with `test_url` equal to one existing journal page URL.
   Check actual post IDs in Make and the `social-publish-state` branch.

## Behavior

Successful main-branch technical SEO checks wake a separate serialized social workflow.
It checks out current main and compares content revisions with saved destination records.
It verifies that changed source content and its feature image are served by the live site
before sending any delivery. Failed or not-yet-live pages are reported without publishing.
No editorial pages, shared styles, navigation, pricing, checkout or demos are rewritten.

JPEG copies and 18-second vertical video previews are hosted as immutable assets on the
public `social-publish-state` GitHub branch. Previews contain authored title, feature image,
description and website call to action; they contain no AI narration or realistic synthetic
footage. Videos go to YouTube's Education category with public visibility. Text and JPEG
posts go to Facebook/Instagram, and image pins with destination links go to Pinterest.
Instagram calls to action point to the website via the bio; verify the profile bio link separately.

The first run baselines the existing 108 eligible journal, guide and product detail pages.
Subsequent runs publish new entries and meaningful body, title, description or image changes.
Shared JS cache-busting alone does not republish the catalogue.
Each destination is reserved in Git before delivery and confirmed with a provider post ID.
Git push transport failures retry safely. Timeouts or uncertain publishing responses are marked
`needs_review` and never automatically retried. Reconcile Make history and actual social posts
before changing that record. Other destinations continue when one fails.

Repository variable `NEXALY_SOCIAL_DESTINATIONS` can limit destinations to a comma-separated
subset of `facebook,instagram,pinterest,youtube`. Do not enable an untested destination.
Both brands share the Make account's existing credit allowance; no additional paid bridge
has been provisioned by this change. Publication tests and failures consume credits too.

Checks: `python3 scripts/test-social.py`, `python3 scripts/social-feed.py`,
`python3 scripts/check-core-lock.py`, `python3 scripts/seo-build.py --check`,
and `python3 scripts/test-seo.py`.
