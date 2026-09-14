#!/usr/bin/env python3
"""Rebuild crawlable catalogues and metadata from published HTML; stdlib only."""
import argparse, hashlib, html, json, re, subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from seo_validate import validate
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://nexalyplanner.com'

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source=source; self.elements=[]; self.stack=[]
        self.offsets=[0]
        for line in source.splitlines(True): self.offsets.append(self.offsets[-1]+len(line))
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        line,col=self.getpos(); start=self.offsets[line-1]+col
        item={'tag':tag,'attrs':dict(attrs),'start':start,'open_end':start+len(self.get_starttag_text()),'end':None}
        self.elements.append(item)
        if tag not in {'meta','link','img','input','br','hr','source','area','base','embed','param','wbr','col'}: self.stack.append(item)
        else: item['end']=item['open_end']
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag,attrs)
    def handle_endtag(self, tag):
        line,col=self.getpos(); start=self.offsets[line-1]+col
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:
                item=self.stack[i];item['close_start']=start;item['end']=self.source.find('>',start)+1
                del self.stack[i:];break
    def find(self, tag, **attrs):
        return [e for e in self.elements if e['tag']==tag and all(e['attrs'].get(k)==v for k,v in attrs.items())]
    def inner(self,e): return self.source[e['open_end']:e.get('close_start',e['open_end'])]
    def meta(self,key):
        for e in self.find('meta'):
            if e['attrs'].get('name')==key or e['attrs'].get('property')==key:return e['attrs'].get('content','')
        return ''

def plain(s): return html.unescape(re.sub('<[^>]+>',' ',s)).strip()
def esc(s): return html.escape(str(s),quote=True)
def jsdata(source, render=False):
    code="const vm=require('node:vm'),fs=require('node:fs');const s=fs.readFileSync(0,'utf8');const c={};vm.createContext(c);vm.runInContext(s.slice(0,s.indexOf(\"fill('featTrack'\")),c,{timeout:1000});process.stdout.write(JSON.stringify(RESULT));"
    expr="{products:c.products,posts:c.posts}"
    if render:expr="{products:c.products.map((p,i)=>({cat:p.cat,html:c.cardHTML(p,i)})),posts:c.posts.map(p=>c.postHTML(p))}"
    return json.loads(subprocess.run(['node','-e',code.replace('RESULT',expr)],input=source,text=True,capture_output=True,check=True).stdout)
def replace_inner(source, ident, contents):
    doc=Document(source); entries=[e for e in doc.elements if e['attrs'].get('id')==ident]
    if len(entries)!=1 or 'close_start' not in entries[0]: raise ValueError(f'Missing/duplicate listing container: {ident}')
    e=entries[0];return source[:e['open_end']]+'\n'+contents+'\n'+source[e['close_start']:]
def metadata(source,url):
    doc=Document(source)
    heads=doc.find('head');titles=[e for e in doc.find('title') if heads and e['start'] < heads[0]['end']];h1=doc.find('h1')
    if len(heads)!=1 or len(h1)!=1:raise ValueError(f'{url}: expected one head and one H1')
    title=plain(doc.inner(titles[0])) if titles else plain(doc.inner(h1[0]))+' | Nexaly Planner'
    if not title: raise ValueError(f'{url}: empty title')
    desc=doc.meta('description')
    if not desc:
        paragraphs=[plain(doc.inner(e)) for e in doc.find('p') if e['start']>=h1[0]['end']]
        desc=next((p for p in paragraphs if len(p)>40),'')[:160]
    if not desc:raise ValueError(f'{url}: add a meaningful opening paragraph or description')
    replacements=[]
    for e in doc.elements:
        a=e['attrs']
        if e['start']>heads[0]['end']:continue
        if e['tag']=='title' or (e['tag']=='link' and a.get('rel')=='canonical') or (e['tag']=='meta' and (a.get('name') in {'description','twitter:title','twitter:description'} or a.get('property') in {'og:url','og:title','og:description'})):
            replacements.append((e['start'],e['end'],''))
    block=f'<title>{esc(title)}</title>\n<meta name="description" content="{esc(desc)}">\n<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">\n<meta property="og:title" content="{esc(title)}">\n<meta property="og:description" content="{esc(desc)}">\n<meta name="twitter:title" content="{esc(title)}">\n<meta name="twitter:description" content="{esc(desc)}">\n'
    # Keep the generated block in place on subsequent builds (idempotent).
    first=min(x[0] for x in replacements) if replacements else heads[0]['open_end']
    replacements.append((first,first,block))
    for start,end,value in sorted(replacements,key=lambda x:(x[0],x[1]),reverse=True):source=source[:start]+value+source[end:]
    # Adjacent removed metadata left whitespace; normalize only the head.
    end=source.index('</head>');source=re.sub(r'\n[ \t]*\n+','\n',source[:end])+source[end:]
    source=re.sub(r'<script id="nexaly-seo" type="application/ld\+json">[\s\S]*?</script>\n?','',source)
    crumbs=[{'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'}]
    parts=url[len(SITE):].strip('/').split('/')
    if parts[0]:
        if len(parts)>1:crumbs.append({'@type':'ListItem','position':2,'name':'Journal' if parts[0]=='journal' else 'Products','item':SITE+'/'+parts[0]+'/'})
        crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':plain(doc.inner(h1[0])),'item':url})
    graph=[{'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':desc,'isPartOf':{'@id':SITE+'/#website'}}, {'@type':'BreadcrumbList','itemListElement':crumbs}]
    if url==SITE+'/':graph.append({'@type':'WebSite','@id':SITE+'/#website','url':SITE+'/','name':'Nexaly Planner'})
    schema=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')
    source=source.replace('</head>','<script id="nexaly-seo" type="application/ld+json">'+schema+'</script>\n</head>')
    return source

def build(check=False):
    files={p.relative_to(ROOT).as_posix():p.read_text() for p in ROOT.rglob('index.html') if not any(x.startswith('.') or x in {'node_modules','scripts','tests'} for x in p.relative_to(ROOT).parts)}
    js=(ROOT/'assets/js/main.js').read_text();data=jsdata(js)
    validate(files, ROOT, Document, data)
    old_products={p['url']:p for p in data['products']};old_posts={p['url']:p for p in data['posts']}
    products=[];posts=[];public=[];warnings=[]
    known_path=ROOT/'assets/seo-pages.json'
    known=set(json.loads(known_path.read_text())) if known_path.exists() else None
    for path,source in sorted(files.items()):
        url=SITE+'/'+path.removesuffix('index.html');doc=Document(source)
        if 'noindex' in doc.meta('robots').lower() or doc.meta('nexaly:status').lower()=='draft':continue
        public.append(url);source=metadata(source,url);files[path]=source;doc=Document(source)
        relative=url[len(SITE):];title=plain(doc.inner(doc.find('h1')[0]));desc=doc.meta('description');image=doc.meta('og:image')
        image=image.removeprefix(SITE) if image.startswith(SITE+'/') else image
        if re.fullmatch(r'planners/[^/]+/index.html',path) and '/digital-planners/' not in relative and '/business-operating-systems/' not in relative:
            if relative in old_products:p=dict(old_products[relative])
            else:
                price=doc.meta('product:price:amount')
                for e in doc.find('script',type='application/ld+json'):
                    try:
                        s=json.loads(doc.inner(e))
                        if s.get('@type')=='Product' and isinstance(s.get('offers'),dict):price=price or s['offers'].get('price')
                    except (ValueError,AttributeError):pass
                if price is None or price=='':raise ValueError(f'{path}: product needs its real price in Product offers or product:price:amount')
                checkout=next(e['attrs']['href'] for e in doc.find('a') if urlsplit(e['attrs'].get('href','')).hostname=='buy.polar.sh')
                p={'title':title,'desc':desc,'price':float(price),'img':image,'url':relative,'cat':doc.meta('nexaly:category') or 'Products','video':'','buyUrl':checkout,'m1':'#E5EDF2','m2':'#D8E5E8'}
            products.append(p)
        elif re.fullmatch(r'journal/[^/]+/index.html',path):
            p=dict(old_posts.get(relative,{}));p.update(url=relative)
            p.update(title=title, excerpt=desc, img=image)
            p['alt']=doc.meta('og:image:alt') or next((e['attrs'].get('alt') for e in doc.find('img') if e['attrs'].get('src','').removeprefix(SITE)==image and e['attrs'].get('alt')), title)
            p.setdefault('tag','Planning Guides');p.setdefault('date','')
            p['_order']=doc.meta('article:published_time') or doc.meta('date') or ''
            posts.append(p)
        for e in doc.find('script',type='application/ld+json'):
            try:json.loads(doc.inner(e))
            except ValueError:raise ValueError(f'{path}: invalid JSON-LD')
    # Preserve merchandising order; new entries appear first.
    products.sort(key=lambda p:(p['url'] in old_products,list(old_products).index(p['url']) if p['url'] in old_products else p['url']))
    posts.sort(key=lambda p:(0 if known is not None and SITE+p['url'] not in known else 1, list(old_posts).index(p['url']) if p['url'] in old_posts else len(old_posts)))
    for p in posts:p.pop('_order',None)
    js=re.sub(r'var products = \[[\s\S]*?\];\s*var posts = ',lambda m:'var products = '+json.dumps(products,ensure_ascii=False,indent=2)+';\nvar posts = ',js,count=1)
    js=re.sub(r'var posts = \[[\s\S]*?\];\s*var heartSvg',lambda m:'var posts = '+json.dumps(posts,ensure_ascii=False,indent=2)+';\nvar heartSvg',js,count=1)
    if jsdata(js)!={'products':products,'posts':posts}:raise ValueError('Catalogue update failed')
    rendered=jsdata(js,True)
    for path,ident,cat in [('index.html','featTrack',None),('planners/index.html','allCards',None),('planners/digital-planners/index.html','allCards','Digital Planners'),('planners/business-operating-systems/index.html','allCards','Business Operating Systems')]:
        cards=rendered['products'];cards=cards[:15] if path=='index.html' else cards
        files[path]=replace_inner(files[path],ident,'\n'.join(p['html'] for p in cards if not cat or p['cat']==cat))
    files['index.html']=replace_inner(files['index.html'],'homePosts','\n'.join(rendered['posts'][:3]))
    files['journal/index.html']=replace_inner(files['journal/index.html'],'blogPosts','\n'.join(rendered['posts']))
    # Keep browser rendering in sync with static catalogues; do not edit checkout logic.
    version=hashlib.sha256(js.encode()).hexdigest()[:12]
    for path in files:
        # Product detail files are protected: catalogue refreshes must not rewrite them.
        if re.fullmatch(r'planners/[^/]+/index.html',path) and path not in {'planners/digital-planners/index.html','planners/business-operating-systems/index.html'}:continue
        files[path]=re.sub(r'(/assets/js/main\.js)(?:\?[^"\s>]*)?',lambda m:m[1]+'?v='+version,files[path])
    files['assets/js/main.js']=js
    # No made-up lastmod dates: omit when the content modification date is unknown.
    files['sitemap.xml']='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+esc(u)+'</loc></url>\n' for u in sorted(public))+'</urlset>\n'
    robots=(ROOT/'robots.txt').read_text() if (ROOT/'robots.txt').exists() else 'User-agent: *\nAllow: /\n'
    if re.search(r'^Sitemap:',robots,re.M):robots=re.sub(r'^Sitemap:.*$', 'Sitemap: '+SITE+'/sitemap.xml',robots,flags=re.M)
    else:robots+='\nSitemap: '+SITE+'/sitemap.xml\n'
    files['robots.txt']=robots
    files['assets/seo-pages.json']=json.dumps(sorted(public),indent=2)+'\n'
    ET.fromstring(files['sitemap.xml'])
    validate({p:s for p,s in files.items() if p.endswith('index.html')}, ROOT, Document, {'products':products,'posts':posts}, generated=True)
    changes=[p for p,s in files.items() if not (ROOT/p).exists() or (ROOT/p).read_text()!=s]
    if check and changes:raise ValueError('SEO output is stale: '+', '.join(changes))
    if not check:
        for p in changes:(ROOT/p).write_text(files[p])
    print(json.dumps({'pages':len(public),'products':len(products),'journals':len(posts),'updated':changes,'warnings':warnings},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();build(args.check)
