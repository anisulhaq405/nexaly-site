const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('assets/js/analytics.js', 'utf8');
function fixture(choice, pathname = '/journal/monthly-planner-free-templates/') {
  let click;
  const choices = ['accepted','rejected'].map(value=>({dataset:{choice:value},style:{},addEventListener(type,fn){this.listener=fn;}}));
  const element = ()=>({style:{},hidden:false,setAttribute(){},addEventListener(){},querySelectorAll:()=>choices});
  const ctx = {location:{protocol:'https:',hostname:'nexalyplanner.com',origin:'https://nexalyplanner.com',pathname},localStorage:{getItem:()=>choice,setItem(){}},document:{cookie:'',title:'A public guide',createElement:element,head:{appendChild(){}},body:{appendChild(){}},addEventListener:(type,fn)=>{if(type==='click')click=fn;}},URL,Date};
  ctx.window = ctx;
  vm.runInNewContext(source,ctx);
  return {ctx,choices,events:()=>Array.from(ctx.dataLayer||[]).filter(x=>x[0]==='event').map(x=>[x[1],x[2]]),click:href=>click({target:{closest:selector=>selector==='a[href]'?{href}:null}})};
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
