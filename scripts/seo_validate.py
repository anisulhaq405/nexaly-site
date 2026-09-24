"""Deterministic publishing checks. Never calls or modifies the payment provider."""
import json, math, re
from urllib.parse import urlsplit, urljoin, unquote

SITE='https://nexalyplanner.com'
def validate(files, root, Document, data, generated=False):
    errors=[];titles={};descriptions={};warnings=[]
    catalog={p['url']:p for p in data['products']}
    def fail(path,message): errors.append(path+': '+message)
    def local_exists(value, page):
        u=urlsplit(urljoin(SITE+'/'+page.removesuffix('index.html'),value))
        if u.netloc not in {'nexalyplanner.com','www.nexalyplanner.com'}:return True
        dest=unquote(u.path).lstrip('/')
        if not dest or dest.endswith('/'):dest+='index.html'
        return (root/dest).is_file() or (root/dest/'index.html').is_file() or dest in files
    for path,source in files.items():
        doc=Document(source);heads=doc.find('head')
        draft=doc.meta('nexaly:status').lower()=='draft'
        noindex='noindex' in doc.meta('robots').lower()
        if draft and not noindex:fail(path,'draft requires robots noindex; a custom status alone does not stop indexing')
        if noindex or draft:continue
        if len(heads)!=1:fail(path,'expected one head');continue
        h=heads[0]
        inside=lambda e:h['open_end']<=e['start']<h['end']
        title=[e for e in doc.find('title') if inside(e)]
        if len(title)!=1:fail(path,'expected exactly one document title')
        else:
            value=re.sub(r'\s+',' ',doc.inner(title[0])).strip().casefold()
            if not value:fail(path,'empty document title')
            if value in titles:fail(path,'duplicate title with '+titles[value])
            titles[value]=path
        desc=[e for e in doc.find('meta',name='description') if inside(e)]
        if len(desc)!=1 or not desc[0]['attrs'].get('content','').strip():fail(path,'provide one meaningful meta description')
        else:
            value=desc[0]['attrs']['content'].strip().casefold()
            if value in descriptions:fail(path,'duplicate description with '+descriptions[value])
            descriptions[value]=path
        if len(doc.find('h1'))!=1:fail(path,'expected one H1')
        if generated:
            can=doc.find('link',rel='canonical')
            if len(can)!=1 or can[0]['attrs'].get('href')!=SITE+'/'+path.removesuffix('index.html'):fail(path,'incorrect self-canonical')
        for e in doc.find('script',type='application/ld+json'):
            try:
                value=json.loads(doc.inner(e))
                if not isinstance(value,(dict,list)):raise ValueError()
            except ValueError:fail(path,'invalid JSON-LD object')
        for e in doc.elements:
            # Stale generated listings are rebuilt before final validation.
            if not generated and any(region['start']<=e['start']<region['end'] for region in doc.elements if region['attrs'].get('id') in {'featTrack','allCards','homePosts','blogPosts'} and region.get('end')):continue
            key={'a':'href','img':'src','script':'src','source':'src','link':'href'}.get(e['tag'])
            value=e['attrs'].get(key,'') if key else ''
            if not value or value.startswith(('#','mailto:','tel:','data:','javascript:')):continue
            if not local_exists(value,path):
                fail(path,'missing internal target '+value)
        relative='/'+path.removesuffix('index.html')
        product=bool(re.fullmatch(r'planners/[^/]+/index.html',path)) and relative not in {'/planners/digital-planners/','/planners/business-operating-systems/'}
        article=bool(re.fullmatch(r'journal/[^/]+/index.html',path))
        if product or article:
            image=doc.meta('og:image')
            if not image or not local_exists(image,path):fail(path,'missing or nonexistent og:image')
        if product:
            prices=[]
            if doc.meta('product:price:amount'):prices.append(doc.meta('product:price:amount'))
            for e in doc.find('script',type='application/ld+json'):
                try:
                    obj=json.loads(doc.inner(e))
                    for node in (obj if isinstance(obj,list) else obj.get('@graph',[obj])):
                        if node.get('@type')=='Product' and isinstance(node.get('offers'),dict):
                            prices.append(node['offers'].get('price'))
                except (ValueError,AttributeError,TypeError):pass
            if relative in catalog:prices.append(catalog[relative].get('price'))
            try:
                amounts=[float(p) for p in prices]
                if not amounts or any(not math.isfinite(p) or p<0 for p in amounts) or max(amounts)-min(amounts)>0.000001:raise ValueError()
            except (ValueError,TypeError):fail(path,'missing, invalid or inconsistent actual product price')
            links=[e['attrs'].get('href','') for e in doc.find('a')]
            checkouts=[v for v in links if urlsplit(v).scheme=='https' and urlsplit(v).hostname=='buy.polar.sh' and len(urlsplit(v).path.strip('/'))>5 and not any(w in v.lower() for w in ['placeholder','your-link','example'])]
            if not checkouts and doc.meta('nexaly:checkout')!='pending':fail(path,'provide an actual HTTPS Polar checkout link')
            if checkouts and doc.meta('nexaly:checkout')=='pending':fail(path,'remove pending checkout marker when checkout is live')
            old=catalog.get(relative,{})
            if old.get('buyUrl') and old['buyUrl'] not in checkouts:fail(path,'catalog checkout does not match product page')
    for warning in sorted(set(warnings)):print('WARNING: '+warning)
    if errors:raise ValueError('Publishing validation failed:\n'+'\n'.join(errors))

    return sorted(set(warnings))
