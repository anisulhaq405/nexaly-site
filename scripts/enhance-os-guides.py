"""Editorial links and compact navigation for the six OS manuals."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINKS = {
    'calibratrack-os': [
        ('routine', 'For supplier contract notice dates alongside the calibration schedule, follow the <a href="/guides/renewguard-os/">RenewGuard OS renewal and notice workflow</a>.'),
        ('routine', 'If service costs affect the next quarter, map expected payments in the <a href="/guides/cashflow-13-os/">CashFlow 13 OS weekly cash forecast</a>.'),
    ],
    'consignclear-os': [
        ('ownership', 'For merchandise you buy and replenish yourself, use the <a href="/guides/inventory-procurement-planner/">Inventory &amp; Procurement Planner stock and reorder guide</a>.'),
        ('routine', 'To plan the timing of owner payouts against other bills, use the <a href="/guides/cashflow-13-os/">CashFlow 13 OS 13-week cash planning guide</a>.'),
    ],
    'renewguard-os': [
        ('records', 'When you need to review a supplier beyond contract dates, see the <a href="/guides/vendorpulse-os/">VendorPulse OS supplier performance guide</a>.'),
        ('routine', 'Put upcoming renewal payments into the <a href="/guides/cashflow-13-os/">CashFlow 13 OS weekly cash forecast</a>; review recurring commitments over a longer horizon with the <a href="/guides/business-runway-burn-rate-os/">Business Runway &amp; Burn Rate OS guide</a>.'),
    ],
    'agency-client-profitability-capacity-os': [
        ('step-7', 'If client invoices and payroll fall in different weeks, use the <a href="/guides/cashflow-13-os/">CashFlow 13 OS weekly cash forecast</a> to see the payment timing.'),
        ('step-9', 'Before committing to another hire, compare the staffing scenario with the <a href="/guides/business-runway-burn-rate-os/">Business Runway &amp; Burn Rate OS hiring and runway guide</a>.'),
    ],
    'cashflow-13-os': [
        ('step-7', 'For a multi-month view of spending and hiring capacity, continue with the <a href="/guides/business-runway-burn-rate-os/">Business Runway &amp; Burn Rate OS scenario guide</a>.'),
        ('routine', 'For vendor contracts that can change future payments, use the <a href="/guides/renewguard-os/">RenewGuard OS contract renewal guide</a> to confirm notice dates and amounts.'),
    ],
    'business-runway-burn-rate-os': [
        ('step-5', 'For the exact week when receipts and bills land, use the <a href="/guides/cashflow-13-os/">CashFlow 13 OS 13-week cash forecast</a>.'),
        ('routine', 'If agency staffing drives burn, review client margins in the <a href="/guides/agency-client-profitability-capacity-os/">Agency Client Profitability &amp; Capacity OS guide</a>. Track future vendor obligations with the <a href="/guides/renewguard-os/">RenewGuard OS renewal calendar guide</a>.'),
    ],
}

STYLE = '''<style id="os-guide-enhancements">
.guide-hero{padding-top:38px;padding-bottom:38px}.guide-hero h1{font-size:clamp(2rem,4vw,2.85rem)}
.guide-layout{grid-template-columns:minmax(0,1fr) 230px;gap:22px}
.guide-article{padding:34px 38px}.guide-article>figure:first-child{max-width:590px;margin:0 auto 22px}
.guide-article>figure:first-child img{max-height:350px;object-fit:contain;background:#f5f9f8}
.guide-aside{max-height:none;overflow:visible;padding:20px}.guide-aside ol{list-style:none;padding:0}
.guide-aside li{margin:0;border-bottom:1px solid #e8efed}.guide-aside li:last-child{border:0}
.guide-aside li a{display:block;padding:9px 4px;font-weight:650;text-decoration:none;line-height:1.35}
.guide-aside li a:hover,.guide-aside li a:focus-visible{color:#064f5c;text-decoration:underline}
.guide-article section{padding-bottom:7px}.guide-article section+section{border-top:1px solid #edf1f0}
.guide-article section+section h2{margin-top:1.6rem}
.guide-article .workflow-link{background:#eef7f5;border-left:4px solid #1b827f;border-radius:0 10px 10px 0;padding:14px 18px;margin:20px 0;line-height:1.55}
.guide-article .workflow-link a{font-weight:700;color:#075e6b;text-decoration:underline;text-underline-offset:3px}
.guide-next{margin-top:30px;padding:22px;background:#f5f9f8;border:1px solid #d9e8e5;border-radius:12px}
.guide-next h2{font-size:1.3rem;margin:0 0 8px}.guide-next p{margin:0 0 10px}
.guide-next a{font-weight:700;color:#075e6b}
@media(max-width:820px){.guide-layout{grid-template-columns:1fr}.guide-aside{order:-1;position:static}.guide-aside ol{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3px 12px}}
@media(max-width:520px){.guide-article{padding:22px 17px}.guide-aside ol{grid-template-columns:1fr}.guide-article>figure:first-child img{max-height:260px}}
</style>'''

NAV = [('start', 'Start here'), ('quick', 'Quick start'), ('menus', 'Screens'), ('example', 'Worked example'), ('routine', 'Regular routine'), ('data', 'Data and backups'), ('troubleshooting', 'Troubleshooting'), ('faq', 'FAQs')]

for slug, contextual in LINKS.items():
    path = ROOT / 'guides' / slug / 'index.html'
    html = path.read_text()
    if 'id="os-guide-enhancements"' in html:
        continue
    html = html.replace('</head>', STYLE + '</head>', 1)
    ids = set(re.findall(r'id="([a-z0-9-]+)"', html))
    nav = [(anchor, label) for anchor, label in NAV if anchor in ids]
    if slug in ('calibratrack-os', 'consignclear-os', 'renewguard-os'):
        nav = [(a, label) for a, label in nav if a != 'data']
        backup = 'backup' if 'backup' in ids else None
        if backup: nav.insert(5, (backup, 'Reports and backups'))
    if 'quick' not in ids:
        nav.insert(1, ('step-1', 'First steps'))
    nav_html = '<aside class="guide-aside"><h2>On this page</h2><ol>' + ''.join(f'<li><a href="#{a}">{label}</a></li>' for a, label in nav) + '</ol><p><a href="/guides/">Browse all product guides</a></p></aside>'
    html, count = re.subn(r'<aside class="guide-aside">.*?</aside>', nav_html, html, count=1, flags=re.S)
    assert count == 1, slug
    for anchor, sentence in contextual:
        # Insert in the named section, after its existing prose and before its closing tag.
        pattern = r'(<section\b(?=[^>]*(?:id="' + anchor + r'"|aria-labelledby="' + anchor + r'"))[^>]*>.*?)(</section>)'
        html, count = re.subn(pattern, lambda m: m.group(1) + '<p class="workflow-link">' + sentence + '</p>' + m.group(2), html, count=1, flags=re.S)
        assert count == 1, (slug, anchor)
    product = f'/planners/{slug}/'
    next_block = f'<div class="guide-next"><h2>Continue in the software</h2><p>See the actual screens and work through sample data before entering your own records.</p><a href="{product}#live-demo">Open the {slug.replace("-", " ").title()} live demo</a></div>'
    html = html.replace('<div class="guide-cta">', next_block + '<div class="guide-cta">', 1)
    path.write_text(html)
print('Enhanced six OS guides with compact navigation and contextual internal links')
