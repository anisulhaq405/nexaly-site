"""Independent arithmetic and content contract for the opening-stock worked example."""
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import json,re,subprocess
D=Decimal
s=Path('journal/how-much-inventory-start-boutique/index.html').read_text()
# Compute from per-category SKU inputs, not the totals printed on the page.
lines=[(3,2,2,D('18')),(2,2,2,D('25')),(1,2,2,D('28'))]
variants=sum(a*b*c for a,b,c,_ in lines)
assert variants==24
expected={5:(120,D('2640'),D('860')),6:(144,D('3168'),D('332')),8:(192,D('4224'),D('-724'))}
ceiling=D('5000')-D('900')-D('600')
assert ceiling==D('3500')
for depth,(units,cost,headroom) in expected.items():
 assert sum(a*b*c*depth for a,b,c,_ in lines)==units
 assert sum(a*b*c*depth*p for a,b,c,p in lines)==cost
 assert ceiling-cost==headroom
 assert f'{units} units' in s
 assert '${:,.0f}'.format(cost) in s
assert D('2640')/120==22
assert 3500//22==159 and 159*22==3498 and 160*22==3520
assert sum(a*b*4*5*p for a,b,_,p in lines)==5280
assert D('2640')*D('.30')==792 and D('2640')-792==1848
assert 900+2640+860+600==5000
assert (1+2+2+1)*2==12 and 12*22==264
assert 60*17+180==1200 and 60*18==1080
sale=D('44')*(1-D('.20'))
assert sale==D('35.20') and (sale-22)/sale*100==D('37.5') and sale-22-5==D('8.20')
assert 120-42+4-3==79 and 79-5==74
assert (D(42-4)/120*100).quantize(D('.01'),rounding=ROUND_HALF_UP)==D('31.67')
assert 2*3+2==8 and 2*(3+1)+2==10 and 10-7==3 and ((3+5)//6)*6==6 and 6*22==132
# Publication date, established intent and image are retained; no sideways tables introduced.
assert 'article:published_time" content="2026-09-29"' in s
assert 'article:modified_time" content="2026-11-13"' in s
assert '<table' not in s[s.index('<article'):s.index('</article>')]
assert 'how-much-inventory-start-boutique-20260929.webp' in s
nodes=[json.loads(t)for t in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>',s,re.S)]
faq=next(x for x in nodes if x.get('@type')=='FAQPage')
assert len(faq['mainEntity'])==8
from html import unescape
visible=re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>',s,re.S)
assert [(q['name'],q['acceptedAnswer']['text'])for q in faq['mainEntity']]==[(unescape(q),unescape(a))for q,a in visible]
old=subprocess.check_output(['git','show','HEAD:journal/how-much-inventory-start-boutique/index.html'],text=True)
for anchor in re.findall(r'\bid="([^"]+)"',old):
 if anchor!='nexaly-seo':assert s.count('id="'+anchor+'"')==1,anchor
print('PASS boutique: budget, variants, packs, size coverage, deposits, margins, returns, sell-through, reorder scenario, original anchors/date/image and FAQ parity')
