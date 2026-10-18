"""Keep journal author/date metadata in one predictable location."""
import re,json,html
from datetime import date

def normalize_journal_header(source, Document):
    doc=Document(source)
    pub=doc.meta('article:published_time') or doc.meta('date')
    mod=doc.meta('article:modified_time')
    for node in doc.find('script',type='application/ld+json'):
        try: data=json.loads(doc.inner(node))
        except ValueError: continue
        for root in data if isinstance(data,list) else [data]:
            if not isinstance(root,dict): continue
            for item in [root]+root.get('@graph',[]):
                if isinstance(item,dict) and item.get('@type') in ('Article','BlogPosting'):
                    pub=pub or item.get('datePublished');mod=mod or item.get('dateModified')
    def parsed(value):
        try:return date.fromisoformat(str(value)[:10])
        except (ValueError,TypeError):return None
    pub,mod=parsed(pub),parsed(mod)
    if not(pub or mod):return source
    def stamp(label,d):
        return f'{label} <time datetime="{d.isoformat()}">{d.strftime("%B")} {d.day}, {d.year}</time>'
    parts=['By NexalyPlanner']
    if pub:parts.append(stamp('Published',pub))
    if mod and (not pub or mod>pub):parts.append(stamp('Updated',mod))
    line='<p class="metadata journal-metadata">'+' · '.join(parts)+'</p>'
    # Remove old date/byline blocks, preserving non-date editorial qualifiers.
    edits=[]
    for e in doc.find('p'):
        classes=set(e['attrs'].get('class','').split())
        if not(classes & {'metadata','article-byline','meta'}):continue
        text=html.unescape(re.sub('<[^>]+>',' ',doc.inner(e)))
        if not(classes & {'metadata','article-byline'}) and not re.search(r'Published|Updated',text):continue
        replacement=''
        if 'Fictional worked examples' in text:replacement='<p class="journal-context">Fictional worked examples</p>'
        if 'For solopreneurs and micro-SaaS founders' in text:replacement='<p class="journal-context">Practical workflow guide · For solopreneurs and micro-SaaS founders</p>'
        edits.append((e['start'],e['end'],replacement))
    for start,end,replacement in sorted(edits,reverse=True):source=source[:start]+replacement+source[end:]
    source=re.sub(r'(</h1>)',lambda m:m[0]+line,source,count=1)
    css='<style id="journal-metadata-style">.journal-metadata{font-size:14px;line-height:1.65;margin:14px 0 22px;font-weight:400;letter-spacing:normal}.journal-metadata time{white-space:nowrap}.journal-context{font-size:14px;line-height:1.65}</style>'
    if 'id="journal-metadata-style"' not in source:source=source.replace('</head>',css+'</head>',1)
    return source
