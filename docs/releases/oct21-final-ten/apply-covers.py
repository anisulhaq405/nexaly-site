"""Apply responsive covers while retaining exact worked examples in guides."""
from pathlib import Path
import json,re,html
R=Path(__file__).resolve().parents[3]
items=json.loads(Path(__file__).with_name('cover-manifest.json').read_text())
hub=R/'tools/index.html';directory=hub.read_text()
for item in items:
 slug,alt=item['slug'],html.escape(item['alt'],quote=True)
 base='/assets/img/tools/'+slug;cover=base+'-cover-1200.webp';diagram=base+'-workflow.svg'
 srcset=', '.join(base+f'-cover-{w}.webp {w}w' for w in (480,960,1200))
 guide=slug if slug.startswith('free-') else 'free-'+slug
 for route in ('tools/'+slug,'guides/'+guide):
  p=R/route/'index.html';head,body=p.read_text().split('</head>',1);head=head.replace(diagram,cover)
  if route.startswith('tools/'):
   image=f'<img src="{base}-cover-480.webp" srcset="{srcset}" sizes="(max-width:700px) 120px, 300px" width="1200" height="800" alt="{alt}" fetchpriority="high" decoding="async">'
   body=re.sub(r'(<figure class="oct16-cover">).*?(</figure>)',lambda m:m[1]+image+m[2],body,count=1,flags=re.S)
  p.write_text(head+'</head>'+body)
 image=f'<img src="{base}-cover-480.webp" srcset="{srcset}" sizes="(max-width:600px) calc(100vw - 48px), (max-width:1000px) 45vw, 360px" width="1200" height="800" alt="{alt}" loading="lazy" decoding="async">'
 directory=re.sub(r'<img\b[^>]*src="'+re.escape(base)+r'-(?:workflow\.svg|cover-\d+\.webp)"[^>]*>',lambda m:image,directory)
hub.write_text(directory)
print('Applied ten responsive planner covers and metadata.')
