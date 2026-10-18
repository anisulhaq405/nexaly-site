# Consistent journal date placement — October 18

Owner reported updated dates appearing above the image on one repair article and below it on another, and requested consistent blog headers.

All 80 journal pages now have a single author/date line immediately after the H1: By NexalyPlanner, recorded publication date if known, and recorded update date when later than publication. Unknown publication dates are not invented. Duplicate article bylines and stale header dates removed. Relevant fictional-example and audience qualifiers retained separately. Topic content, images, article schema dates, card dates, URLs and paid pages preserved.

The SEO builder now applies the same idempotent journal-only rule through scripts/journal_header.py so later publishing updates cannot recreate the inconsistency. Scoped metadata styling keeps date labels readable and dates unbroken. Existing navigation, hero designs and article layouts are retained.

Verification: 80 structured date comparisons passed; one metadata line directly after H1 on every journal; 160 Chromium viewport checks passed (all 80 pages at 390px and 1440px), including metadata bounds and text overflow. Both requested pages visually inspected. Core lock passed; 176 pages, zero orphan pages and zero broken internal URLs; generated freshness and whitespace checks passed. Publishing regression and remote CI are required release gates. No physical-phone or search-indexing claim.
