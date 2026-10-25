const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('assets/js/analytics.js', 'utf8');
function fixture(choice, pathname = '/journal/monthly-planner-free-templates/', existing = false, referrer = '') {
  let click;
  const choices = ['accepted','rejected'].map(value=>({dataset:{choice:value},style:{},addEventListener(type,fn){this.listener=fn;}}));
  const element = ()=>({style:{},hidden:false,setAttribute(){},addEventListener(){},querySelectorAll:()=>choices});
  const panel = existing ? element() : null;
  if (panel) { Object.defineProperty(panel.style, 'cssText', {set(){throw new Error('First-render panel styles must not be reapplied');}}); choices.forEach(button=>Object.defineProperty(button.style, 'cssText', {set(){throw new Error('First-render button styles must not be reapplied');}})); panel.parentNode = {}; Object.defineProperty(panel, 'innerHTML', {set(){throw new Error('First-render consent markup must not be recreated');}}); }
  const ctx = {location:{protocol:'https:',hostname:'nexalyplanner.com',origin:'https://nexalyplanner.com',pathname},localStorage:{getItem:()=>choice,setItem(){}},document:{getElementById:()=>panel,cookie:'',referrer,title:'A public guide',createElement:element,head:{appendChild(){}},body:{appendChild(){}},addEventListener:(type,fn)=>{if(type==='click')click=fn;}},URL,Date};
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

// Free planner CTA clicks are product intent, not purchases, and remain consent-gated.
const toolProduct = fixture('accepted','/tools/boutique-return-to-stock-log/');
toolProduct.click('https://nexalyplanner.com/planners/boutique-business-planner/?ignored=secret');
toolProduct.click('https://nexalyplanner.com/planners/digital-planners/');
assert.deepEqual(toolProduct.events().map(x => x[0]), ['page_view','product_click']);
assert.equal(toolProduct.events()[1][1].product_id, 'boutique-business-planner');
assert.equal(toolProduct.events()[1][1].page_location, 'https://nexalyplanner.com/tools/boutique-return-to-stock-log/');
assert(!JSON.stringify(toolProduct.events()).includes('secret'));
assert(!toolProduct.events().some(x => x[0] === 'purchase'));
const rejectedToolProduct = fixture('rejected','/tools/boutique-return-to-stock-log/');
rejectedToolProduct.click('https://nexalyplanner.com/planners/boutique-business-planner/');
assert.equal(rejectedToolProduct.events().length,0);
console.log('PASS free planner product_click: proper destination, source path, consent gate and no purchase fabrication.');

// Checkout is purchase intent only: product attribution stays on our own page.
const checkoutProduct = fixture('accepted','/planners/adhd-digital-planner/');
checkoutProduct.click('https://buy.polar.sh/polar_cl_Example?private=secret');
assert.deepEqual(checkoutProduct.events().map(x => x[0]), ['page_view', 'checkout_click']);
assert.equal(checkoutProduct.events()[1][1].product_id, 'adhd-digital-planner');
assert.equal(checkoutProduct.events()[1][1].page_location, 'https://nexalyplanner.com/planners/adhd-digital-planner/');
assert(!JSON.stringify(checkoutProduct.events()).includes('secret'));
assert(!checkoutProduct.events().some(x => x[0] === 'purchase'));
const declinedCheckout = fixture('rejected','/planners/adhd-digital-planner/');
declinedCheckout.click('https://buy.polar.sh/polar_cl_Example');
assert.equal(declinedCheckout.events().length,0);
const collectionCheckout = fixture('accepted','/pricing/');
collectionCheckout.click('https://buy.polar.sh/polar_cl_Example');
assert.deepEqual(collectionCheckout.events().map(x=>x[0]), ['page_view','checkout_click']);
assert.equal(collectionCheckout.events()[1][1].product_id, undefined);
console.log('PASS Polar checkout product attribution: consent, product slug, no query strings, no fabricated purchases.');

const expanded = fixture('accepted','/tools/purchase-order-template/',false,'https://www.google.com/search?q=private-secret');
for(const file of ['boutique-inventory-worksheet.xlsx','small-business-order-tracker.csv','supplier-scorecard.xlsx','purchase-order-template.xlsx','purchase-order-template.pdf','one-page-marketing-plan-template.html','homeschool-attendance-sheet-A4.pdf']) expanded.click('https://nexalyplanner.com/assets/downloads/'+file+'?private=secret');
expanded.click('https://nexalyplanner.com/demos/inventory-procurement-planner/');
expanded.click('https://buy.polar.sh/polar_cl_Example?private=secret');
expanded.click('https://other.example/assets/downloads/fake.xlsx');
assert.equal(expanded.events().filter(x=>x[0]==='page_view').length,1);
assert.equal(expanded.events().filter(x=>x[0]==='template_download').length,6);
assert.equal(expanded.events().filter(x=>x[0]==='template_open').length,1);
assert.equal(expanded.events().filter(x=>x[0]==='demo_open').length,1);
assert.equal(expanded.events().filter(x=>x[0]==='checkout_click').length,1);
assert.equal(expanded.events()[0][1].page_referrer,'https://www.google.com/');
assert(!JSON.stringify(expanded.events()).includes('secret'));
assert(!expanded.events().some(x=>x[0]==='purchase'));
expanded.choices[0].listener();assert.equal(expanded.events().filter(x=>x[0]==='page_view').length,1);
console.log('PASS expanded resources, one consented pageview, referring domain only, demo/checkout intent and no purchase fabrication.');
