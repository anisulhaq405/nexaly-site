from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[3]
def take(s,sid):
 pattern=r'<section id="'+re.escape(sid)+r'">.*?</section>'
 m=re.search(pattern,s,re.S);assert m,sid
 return s[:m.start()]+s[m.end():],m[0]
def change(path,fn):
 p=ROOT/path;p.write_text(fn(p.read_text()))
def maintenance(s):
 s,a=take(s,'service-trigger-review');marker='<h2 id="offline">';assert marker in s;s=s.replace(marker,a+marker,1)
 s=s if 'href="#service-trigger-review"' in s else s.replace('<a href="#offline">','<a href="#service-trigger-review">Check service triggers and release evidence</a></li><li><a href="#offline">',1)
 return s
change('journal/rental-equipment-maintenance-log/index.html',maintenance)
def po(s):
 s,a=take(s,'receipt-reconciliation-review');a=a.replace('The worked receipt example later in this guide','The worked receipt example below').replace('a negative open balance of 26','an open quantity of −26 units')
 marker='<h2 id="the-fields-your-tracker-needs">';assert marker in s;return s.replace(marker,a+marker,1)
change('journal/purchase-order-tracker/index.html',po)
def agency(s):
 s,a=take(s,'capacity-review-handoff')
 s=re.sub(r'<h3( id="(?:step-[^"]+|common-questions)")>(.*?)</h3>',r'<h2\1>\2</h2>',s,flags=re.S)
 marker='<h3>Use the format this guide actually provides</h3>';assert marker in a
 review,formattext=a.split(marker,1)
 review+='</section>'
 formattext='<section id="capacity-example-format"><h2>Use the format this guide actually provides</h2>'+formattext
 marker='<h2 id="step-1-define-the-month-and-usable-hours">';assert marker in s;s=s.replace(marker,formattext+marker,1)
 marker='<h2 id="step-4-convert-monthly-totals-into-a-weekly-plan">';assert marker in s;return s.replace(marker,review+marker,1)
change('journal/agency-capacity-planning-example/index.html',agency)
for relative,sid,label in [('tools/document-renewal-calendar/index.html','renewal-boundary-review','Date boundaries'),('tools/rental-booking-conflict-checker/index.html','booking-boundary-review','Overlap examples')]:
 p=ROOT/relative;s=p.read_text();s,a=take(s,sid)
 a=a.replace('<h3>When a contract needs a different record</h3>','<h4>When a contract needs a different record</h4>')
 a=re.sub(r'<h2>(.*?)</h2>',r'<h3>\1</h3>',a,count=1)
 marker='<h3 id="saving">';assert marker in s;s=s.replace(marker,a+marker,1)
 s=s.replace('<a href="#saving">','<a href="#'+sid+'">'+label+'</a><a href="#saving">',1)
 if sid=='renewal-boundary-review':
  s=s.replace('The sample expires on November 15, 2026. Subtracting 45 calendar days produces October 1. At an October 16 review, renewal work is 15 days late to start while expiry is still 30 days away. These are two separate signals; changing the status to Renewal in progress does not extend the expiry or clear the renewal-start date.','The worked example has two separate signals: renewal work is overdue to start, while the current document has not reached its entered expiry. Changing the status to Renewal in progress does not extend that expiry or remove the original renewal-start date. Keep both dates visible until the replacement is checked.')
 p.write_text(s)
paths=['journal/rental-equipment-maintenance-log/index.html','journal/purchase-order-tracker/index.html','journal/agency-capacity-planning-example/index.html','tools/document-renewal-calendar/index.html','tools/rental-booking-conflict-checker/index.html']
for relative in paths:
 p=ROOT/relative;s=p.read_text()
 if 'article:modified_time' in s:s=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>2026-10-23',s)
 else:s=s.replace('</title>','</title><meta property="article:modified_time" content="2026-10-23">',1)
 s=re.sub(r'("dateModified"\s*:\s*")[^"]+',r'\g<1>2026-10-23',s)
 s=s.replace('Updated October 16, 2026 · Free browser worksheet','Updated October 23, 2026 · Free browser worksheet')
 p.write_text(s)
print('Editorial pass: examples moved into relevant reading flow; tool guidance remains outside printed reports; dates updated for publication.')
