"""Apply approved editorial feature assets without changing article examples or tool behavior."""
from pathlib import Path
import json,re,html
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parent
manifest=json.loads((D/'images.json').read_text())
for x in manifest:
 p=R/x['kind']/x['slug']/'index.html';s=p.read_text();s=s.replace(x['previous_asset'],x['asset'])
 def feature(m):
  f=m[0];f=re.sub(r'(<img\b[^>]*\balt=")[^"]*',lambda z:z[1]+html.escape(x['alt'],quote=True),f,count=1);f=re.sub(r'<figcaption>.*?</figcaption>','<figcaption>AI-generated editorial illustration. Documents and screens are conceptual; the exact examples and working resources appear on this page.</figcaption>',f,flags=re.S);return f
 s,n=re.subn(r'<figure class="article-feature">.*?</figure>',feature,s,count=1,flags=re.S);assert n==1
 for prop in ['og:image:alt','twitter:image:alt']:
  s=re.sub(r'(<meta\b[^>]*(?:property|name)="'+re.escape(prop)+r'"[^>]*content=")[^"]*',lambda m:m[1]+html.escape(x['alt'],quote=True),s)
 p.write_text(s)
p=R/'tools/index.html';s=p.read_text()
for x in manifest:
 if x['kind']!='tools':continue
 s=s.replace(x['previous_asset'],x['asset']);s=re.sub(r'(<img\b[^>]*src="'+re.escape(x['asset'])+r'"[^>]*alt=")[^"]*',lambda m:m[1]+html.escape(x['alt'],quote=True),s)
p.write_text(s)
print('Applied nine topic-specific covers, truthful captions, social image metadata and three directory previews.')
