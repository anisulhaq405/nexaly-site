"""Idempotent visible, accessible feature-image integration for seven early free tools."""
from pathlib import Path
import re,json,html
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parent;E=html.escape
items=json.loads((D/'images.json').read_text())
for x in items:
 p=R/'tools'/x['slug']/'index.html';s=p.read_text();url='https://nexalyplanner.com'+x['asset']
 if 'id="tool-feature-cover"'not in s:
  pattern=r'(<main\b[^>]*>\s*<nav\b.*?</nav>)(<div class="d1-hide">.*?</div>)'
  m=re.search(pattern,s,re.S);assert m,x['slug']
  form=re.search(r'<form\b[^>]*id="([^"]+)"',s);assert form
  fig='<figure class="tool-feature" id="tool-feature-cover"><img src="'+x['asset']+'" width="1200" height="800" alt="'+E(x['alt'],quote=True)+'" fetchpriority="high" decoding="async"><figcaption>AI-generated conceptual illustration. Use the worksheet for its actual inputs, outputs and download formats.</figcaption></figure>'
  intro=m[2].replace('</div>','<a class="tool-feature-jump" href="#'+form[1]+'">Use the editable worksheet ↓</a></div>')
  s=s[:m.start()]+m[1]+'<div class="tool-feature-intro d1-hide">'+intro+fig+'</div>'+s[m.end():]
 if '/assets/css/tool-feature-covers.css'not in s:s=s.replace('</head>','<link rel="stylesheet" href="/assets/css/tool-feature-covers.css"></head>',1)
 for tag,key in [('property','og:image'),('name','twitter:image')]:
  pat=r'(<meta\b[^>]*'+tag+'="'+re.escape(key)+r'"[^>]*content=")[^"]*';s,n=re.subn(pat,lambda m:m[1]+url,s);assert n==1
 for tag,key in [('property','og:image:alt'),('name','twitter:image:alt')]:
  pat=r'(<meta\b[^>]*'+tag+'="'+re.escape(key)+r'"[^>]*content=")[^"]*'
  if re.search(pat,s):s=re.sub(pat,lambda m:m[1]+E(x['alt'],quote=True),s)
  else:s=s.replace('</head>',f'<meta {tag}="{key}" content="{E(x["alt"],quote=True)}"></head>',1)
 # WebApplication uses the same actual feature asset; leave dates and capability claims intact.
 for m in list(re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)):
  data=json.loads(m[1])
  if data.get('@type')=='WebApplication':data['image']=url;s=s.replace(m[0],'<script type="application/ld+json">'+json.dumps(data)+'</script>',1)
 p.write_text(s)
p=R/'tools/index.html';s=p.read_text()
for x in items:
 def card(m):
  c=m[0]
  if '/tools/'+x['slug']+'/'not in c:return c
  if 'class="directory-preview"'in c:return c
  preview='<a class="directory-preview" href="/tools/'+x['slug']+'/" aria-label="Open '+E(x['title'],quote=True)+'"><img src="'+x['asset']+'" width="1200" height="800" alt="'+E(x['alt'],quote=True)+'" loading="lazy" decoding="async"></a>'
  return c.replace('<div class="library-card-body">',preview+'<div class="library-card-body">',1)
 s=re.sub(r'<article\b[^>]*\bdirectory-tool\b.*?</article>',card,s,flags=re.S)
p.write_text(s);print('Applied seven visible covers, directory previews, social metadata and schema images.')
