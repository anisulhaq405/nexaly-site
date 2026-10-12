# AdSense readiness: October 12, 2026

## Scope and evidence

Owner requested work on the agreed AdSense preparation steps. This batch is a readiness repair, not an AdSense approval, an application submission or certification of legal compliance.

- Inventoried all 68 journal articles: titles, headings, text length, tables, source links, downloadable resources, internal editorial text and repeated paragraph patterns. Word count is an inventory field, not a Google approval threshold.
- Detailed source review and repairs cover the 10 articles listed below. The remaining 58 received structural/content-pattern checks; the inventory does not assign them an approval grade. Similar iPad and annual-planner topic clusters remain candidates for later intent review; no URLs, redirects or indexing rules were changed to hide them.
- Checked all 148 live sitemap URLs before editing: all returned HTTP 200 with readable HTML, no authentication required. robots.txt allows crawling and declares the sitemap. This does not prove Google has crawled, indexed or approved those pages.
- Found no exact repeated long article paragraphs apart from the shared instructions for making a Google Sheets copy. This is an internal duplication check, not an external plagiarism or image-licence certification.
- The AdSense browser showed that the NexalyPlanner Google account had no AdSense account. Owner confirmed this will be their first account. No publisher ID exists in this batch, no ads.txt with a placeholder was created and no advertising tag was installed.

Full article inventory: `adsense-content-inventory-oct12.csv`.

## Verified gaps and repairs

| Area | Evidence before repair | Result |
| --- | --- | --- |
| Contact | sendContact cleared the inputs and showed a reply promise without sending a request | Form prepares an encoded mailto draft, preserves text, requires the visitor to send it and provides a direct email fallback. No message was sent during testing; mailbox delivery remains untested. |
| Newsletter | 147 signup blocks invoked a handler that cleared the address and falsely reported subscription | Replaced that block with a working Contact link using the existing footer layout. Legacy cached forms get a truthful fallback without clearing their input. |
| About | Brand story and examples, but no explicit publishing/comparison method | Identifies organizational authorship, the relationship to paid products, fictional examples, documentation-based comparisons, testing limits and a correction route. No invented credentials or founder history. |
| Privacy | Covered analytics but not new copy/download clicks or Google Sheets storage | Documents actual contact, order, optional analytics, local files and Google copies. Advertising is explicitly planned and inactive; a CMP has not been claimed or activated. |
| Caregiver daily log | A FAQ discussed whether another SEO article should be created | Replaced internal planning text with reader-facing handoff guidance, an editable blank TXT file, acknowledged task ownership and a primary NIA source. No clinical dose, diagnosis or treatment advice. |
| One-time/offline apps | Universal cost, ownership and privacy claims | Balanced hypothetical total-cost example, licence/version checks, device-storage limits and a sample migration test. |
| One-person business with AI | An unsupported equivalent-output comparison of three hires with a low-cost AI stack | Removed staffing and price benchmark claims. Added an eight-reply trial measuring preparation, review and corrections; clarified what the local Copilot does and does not do. |
| iPad app comparison / setup | Overlapping format discussions with no precise current provider references | App guide separates appointments, reminders, PDF writing and project records. Setup guide focuses on PDF import/navigation/export checks. Apple, Goodnotes and Notion documentation is linked; no native iPad test is claimed. |
| Free layout pages | Described layouts but supplied no first-party file | Added original dated 2026 monthly, undated monthly and weekly PDFs. Daily and free-iPad pages reuse the existing daily PDF. Paid products remain separate from the free resources. |

## Substantive article updates

- caregiver-daily-log-template
- why-one-time-purchase-offline-apps
- how-to-run-a-one-person-business-with-ai
- best-planner-app-for-ipad-2026
- ipad-digital-planner-setup-guide
- 2026-monthly-planner-free-layouts
- monthly-planner-free-templates
- weekly-planner-2026-free-templates
- daily-planner-2026-free-layouts
- free-digital-planner-for-ipad

Publication dates are retained; modification dates change only on the 10 substantive refreshes. Footer/cache updates do not pretend to be article refreshes.

## Validation

- Rendered and inspected the final 14 PDF pages, with embedded fonts. Dated calendar has 12 Letter portrait pages, undated monthly 1 Letter portrait page, weekly 1 Letter landscape page. All 365 day numbers were checked against calendar grid positions.
- Checked the fictional arithmetic: AI trial 40 minutes before, 36 including preparation/review/rework; software example $84 initial total, $96/$288 subscription charges at the stated assumptions.
- Contact regression tests cover encoded body text, retained input, invalid/empty fields and absence of false send/subscription confirmations. Tests do not send email.
- Analytics regression tests cover the four new resource names, known Google Sheets IDs, product versus category clicks, unset/rejected/withdrawn consent and omission of query strings.
- New behavior tests are included in the read-only publishing workflow.
- Source link audit reports 0 broken internal URLs and 0 orphan pages. A separate fragment check found 0 missing anchor targets.
- Core review compared every one of the 21 product pages against origin/main. Restoring only the old newsletter block yields an identical footer; product headers, styles, executable scripts, prices and checkout URLs are identical. Demos, shared CSS, logos and bundles are unchanged. main.js behavior differs only in the contact draft, truthful legacy newsletter fallback and analytics cache revision. These owner-authorized focused repairs were reviewed before the core baseline was deliberately updated.
- Required SEO build/idempotence and protected-storefront regression checks pass locally. Merge requires CI on the exact PR head; final deployment is verified after merge.

## Account-dependent work

First account creation needs the owner's actual payment country and acceptance of Google's binding Terms. Payment/identity information must be provided by the owner. The site URL can be prepared, but the account, ownership connection, certified consent messaging and site-review request are not completed by this batch. See `docs/adsense-integration-plan.md`.

## Official references checked

- https://support.google.com/adsense/answer/81904?hl=en
- https://support.google.com/publisherpolicies/answer/11112688?hl=en
- https://support.google.com/publisherpolicies/answer/10437794?hl=en
- https://support.google.com/adsense/answer/10924669?hl=en
- https://support.google.com/adsense/answer/13554116?hl=en
- https://support.google.com/adsense/answer/12171612?hl=en
- https://policies.google.com/technologies/ads
- https://www.nia.nih.gov/health/caregiving/sharing-caregiving-responsibilities
- https://support.goodnotes.com/hc/en-us/articles/7353717816463-Import-files-into-Goodnotes
- https://www.notion.com/help/use-pages-offline
- https://support.apple.com/guide/ipad/ipadb80e59c7/ipados
