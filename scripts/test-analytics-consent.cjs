const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('assets/js/analytics.js', 'utf8');
function fixture(choice, pathname = '/journal/monthly-planner-free-templates/', existing = false) {
  let click;
  const choices = ['accepted','rejected'].map(value=>({dataset:{choice:value},style:{},addEventListener(type,fn){this.listener=fn;}}));
  const element = ()=>({style:{},hidden:false,setAttribute(){},addEventListener(){},querySelectorAll:()=>choices});
  const panel = existing ? element() : null;
  if (panel) { Object.defineProperty(panel.style, 'cssText', {set(){throw new Error('First-render panel styles must not be reapplied');}}); choices.forEach(button=>Object.defineProperty(button.style, 'cssText', {set(){throw new Error('First-render button styles must not be reapplied');}})); panel.parentNode = {}; Object.defineProperty(panel, 'innerHTML', {set(){throw new Error('First-render consent markup must not be recreated');}}); }
  const ctx = {location:{protocol:'https:',hostname:'nexalyplanner.com',origin:'https://nexalyplanner.com',pathname},localStorage:{getItem:()=>choice,setItem(){}},document:{getElementById:()=>panel,cookie:'',title:'A public guide',createElement:element,head:{appendChild(){}},body:{appendChild(){}},addEventListener:(type,fn)=>{if(type==='click')click=fn;}},URL,Date};
  ctx.window = ctx;
  vm.runInNewContext(source,ctx);
  return {ctx,choices,panel,events:()=>Array.from(ctx.dataLayer||[]).filter(x=>x[0]==='event').map(x=>[x[1],x[2]]),click:href=>click({target:{closest:selector=>selector==='a[href]'?{href}:null}})};
}
const allowed = fixture('accepted');
for (const path of ['2026-monthly-planner.pdf','undated-monthly-planner-template.pdf','weekly-planner-template.pdf','caregiver-daily-log-template.txt']) {
  allowed.click('https://nexalyplanner.com/assets/downloads/'+path+'?private=secret');
}
allowed.click('https://nexalyplanner.com/planners/ai-student-planner/?private=secret');
allowed.click('https://nexalyplanner.com/planners/digital-planners/');
allowed.click('https://docs.google.com/spreadsheets/d/1rxi5554h8Wfc3Vd66TY9_ZXuiTZZ3KBO8Lvcb_24bqM/copy?private=secret');
allowed.click('https://docs.google.com/spreadsheets/d/unknown/copy');
allowed.click('https://other.example/assets/downloads/weekly-planner-template.pdf');
assert.deepEqual(allowed.events().map(x=>x[0]),['page_view','template_download','template_download','template_download','template_download','product_click','template_open']);
assert(!JSON.stringify(allowed.events()).includes('secret'));
assert.equal(allowed.events()[4][1].file_extension,'txt');
const before = allowed.events().length;
allowed.choices[1].listener();
allowed.click('https://nexalyplanner.com/assets/downloads/weekly-planner-template.pdf');
assert.equal(allowed.events().length,before);
for (const choice of [null,'rejected']) {
  const declined = fixture(choice);
  declined.click('https://nexalyplanner.com/assets/downloads/weekly-planner-template.pdf');
  assert.equal(declined.events().length,0);
}
const home = fixture('accepted','/');
home.click('https://nexalyplanner.com/planners/ai-student-planner/');
assert.deepEqual(home.events().map(x=>x[0]),['page_view']);
console.log('PASS analytics: all new resource clicks, known Sheets IDs, actual product links, consent rejection/withdrawal and no query-string leakage.');

for (const choice of [null, 'accepted', 'rejected']) {
  const existing = fixture(choice, '/', true);
  assert.equal(existing.panel.hidden, choice === 'accepted' || choice === 'rejected');
  assert.equal(existing.events().length, choice === 'accepted' ? 1 : 0);
  existing.choices[1].listener();
  assert.equal(existing.ctx['ga-disable-G-NPE1Y88BDG'], true);
}
const homeMarkup = fs.readFileSync('index.html', 'utf8');
const bootstrap = homeMarkup.match(/<script id="nexaly-first-render-consent">([\s\S]*?)<\/script>/)[1];
for (const choice of [null, 'accepted', 'rejected']) {
  const panel = {hidden:true};
  vm.runInNewContext(bootstrap,{localStorage:{getItem:()=>choice},document:{getElementById:()=>panel}});
  assert.equal(panel.hidden, choice === 'accepted' || choice === 'rejected');
}
{const panel={hidden:true};vm.runInNewContext(bootstrap,{localStorage:{getItem(){throw Error('blocked');}},document:{getElementById:()=>panel}});assert.equal(panel.hidden,false);}
console.log('PASS first-render consent: saved choices, blocked storage, no duplicate/recreated markup, rejection and existing consent gate.');
