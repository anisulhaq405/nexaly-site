"""Keep public guide dates and TechArticle dates consistent with publication history."""
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / 'guides'
FIRST = {'adhd-digital-planner', 'ai-student-planner', 'content-marketing-planner', 'digital-homeschool-planner', 'small-business-planner'}
SEPT_25 = {'calibratrack-os', 'consignclear-os', 'renewguard-os'}
SEPT_27 = {'agency-client-profitability-capacity-os', 'cashflow-13-os', 'business-runway-burn-rate-os'}
UPDATED_SEPT_28 = {'adhd-digital-planner', 'ai-student-planner', 'batchtrace-os', 'boutique-business-planner', 'caregiver-planner-aging-parents', 'content-marketing-planner', 'digital-homeschool-planner', 'offline-ai-business-copilot', 'rentflow-os', 'repairbench-os', 'sales-management-system', 'small-business-planner', 'vendorpulse-os'}

def pretty(iso):
    return f'{date.fromisoformat(iso):%B} {date.fromisoformat(iso).day}, {date.fromisoformat(iso):%Y}'

for path in sorted(ROOT.glob('*/index.html')):
    slug = path.parent.name
    published = '2026-09-16' if slug in FIRST else '2026-09-25' if slug in SEPT_25 else '2026-09-27' if slug in SEPT_27 else '2026-09-19'
    modified = '2026-09-28' if slug in UPDATED_SEPT_28 else '2026-09-19' if slug in FIRST else '2026-09-27' if slug in SEPT_25 | SEPT_27 else published
    html = path.read_text()
    assert 'datePublished' in html and 'dateModified' in html, slug
    html = re.sub(r'("datePublished"\s*:\s*")[^"]+', lambda m: m.group(1)+published, html)
    html = re.sub(r'("dateModified"\s*:\s*")[^"]+', lambda m: m.group(1)+modified, html)
    meta = f'<meta property="article:modified_time" content="{modified}">'
    if 'property="article:modified_time"' in html:
        html = re.sub(r'<meta property="article:modified_time" content="[^"]*">', meta, html, count=1)
    else:
        html = html.replace('</head>', meta+'</head>', 1)
    html = re.sub(r'(<strong>Updated:</strong>\s*<br>)[^<]+', lambda m:m.group(1)+pretty(modified), html, count=1)
    # Rebuild the date row so repeated runs never append a second visible row.
    html = re.sub(r'<div class="guide-dates">.*?</div>', '', html, flags=re.S)
    dates = f'<div class="guide-dates"><span>Published <time datetime="{published}">{pretty(published)}</time></span><span>Updated <time datetime="{modified}">{pretty(modified)}</time></span></div>'
    html, count = re.subn(r'(<header class="guide-hero"><div class="kicker">).*?(</div>)', lambda m:m.group(1)+'NEXALY PRODUCT GUIDE'+m.group(2)+dates, html, count=1, flags=re.S)
    assert count == 1, slug
    if 'id="guide-date-style"' not in html:
        style = '<style id="guide-date-style">.guide-dates{display:flex;flex-wrap:wrap;gap:8px 24px;margin:12px 0 16px;color:#e1f0f1;font-size:.9rem}.guide-dates span{display:inline-flex;gap:5px}.guide-dates time{font-weight:700;color:#fff}</style>'
        html = html.replace('</head>', style+'</head>', 1)
    path.write_text(html)
print('Normalized visible and structured publish/update dates for 21 guides')
