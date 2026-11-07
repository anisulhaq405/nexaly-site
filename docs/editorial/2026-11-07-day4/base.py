"""Original Day4 editorial sources. Run before the SEO generator."""
from pathlib import Path
import json,re,html
from io import BytesIO
from PIL import Image
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parent;E=html.escape
A=[]
def p(s):return '<p>'+s+'</p>'
def h(s):return '<h2>'+s+'</h2>'
def table(c,heads,rows):return '<div class="table-wrap"><table><caption>'+c+'</caption><thead><tr>'+''.join('<th scope="col">'+v+'</th>' for v in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(v)+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
SBA=('SBA: write your business plan','https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan')
def add(slug,title,desc,alt,sections,sources,related):
 body=p(desc)+p('<strong>Example basis:</strong> Businesses, amounts, fees and outcomes in the worked examples are fictional planning assumptions in USD, prepared November 7, 2026. They are not market averages, observed customer results or income promises.')
 toc=[]
 for i,(heading,content) in enumerate(sections,1):
  body+=f'<h2 id="section-{i}">{E(heading)}</h2>'+content;toc.append(f'<li><a href="#section-{i}">{E(heading)}</a></li>')
 body='<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>'+''.join(toc)+'</ol></nav>'+body
 body+=h('Sources and method')+p('The examples and reconciliations are original. These publisher resources provide context for planning structures and workflow definitions; their platform features or regional requirements are not automatically NexalyPlanner features.')+'<ul>'+''.join(f'<li><a href="{u}">{E(t)}</a></li>' for t,u in sources)+'</ul>'
 A.append(dict(slug=slug,title=title,desc=desc,alt=alt,body=body,sources=sources,related=related))
