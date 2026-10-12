from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,subprocess,textwrap
r=Path(__file__).resolve().parents[1];out=r/'assets/img/workflows';out.mkdir(parents=True,exist_ok=True)
configs=json.loads((r/'assets/js/keyword-workflows-configs.json').read_text());articles=json.loads((r/'docs/editorial/oct13/articles.json').read_text())
node="const a=require('./assets/js/keyword-workflows-models.js');console.log(JSON.stringify(a.configs.filter(c=>c.theme.startsWith('workflow-')).map(c=>{const s=structuredClone(c.sample);s.rows.forEach((r,i)=>r.id='row-'+i);return {kind:c.kind,result:a.evaluate(c.slug,s)};})));"
results={x['kind']:x['result'] for x in json.loads(subprocess.check_output(['node','-e',node],cwd=r))}
fontdir=Path('/usr/share/fonts/truetype/dejavu')
def font(n,b=False):return ImageFont.truetype(str(fontdir/('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf')),n)
def wrap(d,s,f,width):
 words=s.split();lines=[];line=''
 for w in words:
  next=(line+' '+w).strip()
  if d.textlength(next,font=f)>width and line:lines.append(line);line=w
  else:line=next
 if line:lines.append(line)
 return lines

def tool(c):
 im=Image.new('RGB',(1200,800),c['color']);d=ImageDraw.Draw(im)
 d.text((48,36),'NEXALY  /  FREE WORKSHEET',font=font(17,True),fill='#f5f4ef')
 title=wrap(d,c['name'],font(42,True),1100)
 y=80
 for line in title:d.text((48,y),line,font=font(42,True),fill='white');y+=55
 d.text((48,y+8),'Calculated fictional example  •  Enter your own assumptions',font=font(20),fill='#eee9df');y+=65
 d.rounded_rectangle((40,y,1160,750),radius=24,fill='#f9fbfc')
 metrics=results[c['kind']]['metrics']
 for i,m in enumerate(metrics[:4]):
  x=64+(i%2)*548;yy=y+23+(i//2)*150
  d.rounded_rectangle((x,yy,x+522,yy+130),radius=15,fill='white',outline=c['color'],width=2)
  label=wrap(d,m['label'],font(18),480)
  for j,l in enumerate(label):d.text((x+22,yy+14+j*23),l,font=font(18),fill='#435763')
  value=m['value'];value=(('-$' if value<0 else '$')+format(abs(value)/100,',.2f')) if m['format']=='money' else str(value)+(' h' if m['format']=='hours' else '')
  d.text((x+22,yy+67),value,font=font(32,True),fill=c['color'])
 yy=y+334;d.text((65,yy),'WORKFLOW',font=font(16,True),fill=c['color'])
 note=c['reportNote'].split('. ')[0]+'.'
 for j,line in enumerate(wrap(d,note,font(19),1040)[:3]):d.text((65,yy+31+j*28),line,font=font(19),fill='#263f4b')
 d.text((48,771),'Browser worksheet · Device save · Editable backup · CSV · Print / PDF',font=font(14),fill='white')
 im.save(out/(c['slug']+'.webp'),'WEBP',quality=86,method=6)

diagrams={
'variance':['Reconcile the cash bridge','$1,700 forecast closing','−$300 receipt impact','−$100 payment impact','$1,300 actual closing'],
'budget':['Explain the monthly difference','$3,000 budget remainder','−$1,000 revenue impact','Cost impacts cancel','$2,000 actual remainder'],
'builder':['Make the page fit your hours','Letter / A4 / A5','Daily or weekly','Your writing sections','Preview before printing'],
 'teacher':['Prepare before the lesson','October 16 lesson','October 12 prep due','October 13 review','1 preparation overdue'],
'production':['Check the day, not just the window','3 hours daily capacity','2-hour article block','2-hour demonstration','1 hour over capacity'],
'lean':['Move an assumption into a test','Specific customer','Bounded offer','Evidence observed','Next test + review'],
'projections':['Separate result from cash','$1,800 October result','$1,500 October cash','$2,100 November result','$2,200 November cash'],
'coffee':['Test a slower operating day','120 orders → $960 sales','$240 base remainder','80 orders → $640 sales','$20 slower-day remainder'],
'construction':['Find the gap before collecting','$3,000 after deposit','$500 after materials','−$700 after labor','$2,300 after collection'],
 'trucking':['Use the same mileage denominator','400 loaded + 100 empty','500 total miles','$870 modeled cost','$1.74 / total mile'],
'interior':['Protect project time and cash','$3,000 project fee','$1,300 base contribution','8 added revision hours','$800 revised contribution'],
'it':['Keep potential charges distinct','20 included hours','27 used hours','7 potential extra hours','$700 needs authorization']}

def article(a):
 k=a['tool']or('interior' if a['slug'].startswith('interior')else'it');values=diagrams[k]
 c=next((c for c in configs if c['kind']==k),None);color=c['color']if c else('#725b6d'if k=='interior'else'#285373')
 im=Image.new('RGB',(1200,800),'#f3f0e9');d=ImageDraw.Draw(im);d.rectangle((0,0,20,800),fill=color)
 d.text((60,42),'NEXALYPLANNER JOURNAL  /  ORIGINAL EXAMPLE',font=font(16,True),fill=color)
 y=94
 for line in wrap(d,a['title'],font(39,True),1080):d.text((60,y),line,font=font(39,True),fill='#203340');y+=52
 d.text((60,y+13),values[0],font=font(24,True),fill=color);y+=70
 for i,v in enumerate(values[1:]):
  x=60+(i%2)*550;yy=y+(i//2)*175;dark=i==3
  d.rounded_rectangle((x,yy,x+520,yy+150),radius=18,fill=color if dark else 'white',outline=color,width=1)
  d.text((x+25,yy+22),'STEP '+str(i+1),font=font(15,True),fill='white'if dark else color)
  for j,line in enumerate(wrap(d,v,font(27,True),475)):d.text((x+25,yy+62+j*35),line,font=font(27,True),fill='white'if dark else '#203340')
 d.text((60,760),'Fictional planning example · Read the assumptions and worked guide',font=font(16),fill='#53616a')
 im.save(out/(a['slug']+'.webp'),'WEBP',quality=86,method=6)
for c in configs:tool(c)
for a in articles:article(a)
print('Created',len(configs)+len(articles),'unique precise cover diagrams')
