'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs');
const {webcrypto,createHash}=require('node:crypto');
const {JSDOM}=require(process.env.NEXALY_JSDOM_PATH||'jsdom');
const selected=['monthly-business-budget-variance','cash-flow-variance-report','marketing-campaign-budget-planner','one-page-business-plan-builder','freelancer-weekly-capacity-planner','stock-coverage-planner','supplier-quote-comparison','consignment-settlement-planner','physical-count-adjustment-worksheet','rental-booking-conflict-checker'];
const allowed=/^(small-tools-models|next-tools-models|keyword-workflows-models|oct16-planners-models|small-tools-ui|business-summary-copy)\.js$/;
const flush=()=>new Promise(resolve=>setImmediate(resolve));
async function check(slug){
 const source=fs.readFileSync('tools/'+slug+'/index.html','utf8'),dom=new JSDOM(source,{url:'https://nexalyplanner.com/tools/'+slug+'/',runScripts:'outside-only'}),w=dom.window,d=w.document,$=id=>d.getElementById(id);
 const expectedVersion=createHash('sha256').update(fs.readFileSync('assets/js/business-summary-copy.js')).digest('hex').slice(0,12);assert(source.includes('/assets/js/business-summary-copy.js?v='+expectedVersion),'summary script cache version');
 let copied=[],downloads=[],prints=0;
 w.confirm=()=>true;w.print=()=>prints++;w.Blob=Blob;
 w.URL.createObjectURL=blob=>{downloads.push(blob);return 'blob:fictional';};w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){};
 w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
 if(!w.crypto.randomUUID)w.crypto.randomUUID=()=>webcrypto.randomUUID();
 Object.defineProperty(w.navigator,'clipboard',{configurable:true,value:{writeText:async value=>copied.push(value)}});
 for(const script of d.querySelectorAll('script[src]')){const path=new URL(script.src).pathname,name=path.split('/').pop();if(allowed.test(name))w.eval(fs.readFileSync('.'+path,'utf8'));}
 assert($('tool-copy-summary').disabled,slug+' starts disabled');
 $('tool-sample').click();await flush();assert.equal($('tool-message').dataset.status,'success',slug);assert(!$('tool-copy-summary').disabled);
 $('tool-save').click();const key='nexaly-free-tool-v1-'+slug,saved=w.localStorage.getItem(key);assert(saved);
 $('tool-copy-summary').click();await flush();assert.equal(copied.length,1);assert(copied[0].includes('Calculated summary'));assert(copied[0].includes('Calculation and scope'));if(d.querySelector('.result-notes li'))assert(copied[0].includes('Review notes'));assert(copied[0].includes('JSON backup'));assert.equal($('tool-copy-text').value,copied[0]);assert(!$('tool-copy-fallback').hidden);assert($('tool-copy-status').textContent.includes('copied'));assert.equal(w.localStorage.getItem(key),saved,'copy must not change save');
 assert($('tool-copy-summary').closest('.no-print'));assert($('tool-copy-text').closest('.no-print'));
 $('tool-json').click();const backup=JSON.parse(await downloads.pop().text());assert.equal(backup.version,1);assert.equal(backup.tool,slug);
 $('tool-csv').click();await flush();const csv=await downloads.pop().text();assert(csv.includes('Calculation / limitations'));assert(!csv.includes('NaN'));
 $('tool-print').click();await flush();assert.equal(prints,1);
 const title=$('top-title');title.value='';title.dispatchEvent(new w.Event('input',{bubbles:true}));assert($('tool-copy-summary').disabled);assert.equal($('tool-copy-text').value,'');assert($('tool-copy-fallback').hidden);
 $('tool-calculate').click();await flush();assert.equal($('tool-message').dataset.status,'error');assert($('tool-copy-summary').disabled);assert.equal(copied.length,1);
 $('tool-restore').click();await flush();assert($('tool-copy-summary').disabled,'restored input needs recalculation');$('tool-calculate').click();await flush();assert(!$('tool-copy-summary').disabled);
 w.navigator.clipboard.writeText=async()=>{throw Error('NotAllowedError');};$('tool-copy-summary').click();await flush();assert(!$('tool-copy-fallback').hidden);assert($('tool-copy-text').value.includes('Calculated summary'));assert($('tool-copy-status').textContent.includes('unavailable'));assert(!$('tool-copy-status').textContent.includes('summary copied'));
 Object.defineProperty($('tool-import'),'files',{configurable:true,value:[{size:100,text:async()=>JSON.stringify({...backup,tool:'wrong-tool'})}]});await $('tool-import').onchange();await flush();assert($('tool-copy-summary').disabled);assert($('tool-copy-fallback').hidden);
 $('tool-sample').click();await flush();let resolveCopy;w.navigator.clipboard.writeText=()=>new Promise(resolve=>{resolveCopy=resolve;});$('tool-copy-summary').click();assert($('tool-copy-summary').disabled);title.value='Edited while copy was pending';title.dispatchEvent(new w.Event('input',{bubbles:true}));resolveCopy();await flush();assert($('tool-copy-summary').disabled);assert($('tool-copy-fallback').hidden);assert.equal($('tool-copy-text').value,'');assert(!$('tool-copy-status').textContent.includes('summary copied'));
 dom.window.close();console.log('PASS summary/copy fallback/stale result/save/backup/CSV/print:',slug);
}
function scenarios(){
 let api=require('../assets/js/small-tools-models.js');for(const name of ['next-tools-models','keyword-workflows-models','oct16-planners-models'])api=require('../assets/js/'+name+'.js');
 const fixture=slug=>{const c=api.configs.find(x=>x.slug===slug),s=structuredClone(c.sample);s.rows.forEach((r,i)=>r.id='r'+i);return{s,run:()=>api.evaluate(slug,s)};};
 const metric=(r,label)=>r.metrics.find(m=>m.label===label).value;
 {const{s,run}=fixture(selected[0]);s.rows.push({...s.rows[2],id:'extra',label:'Unexpected fixed cost',budget:'0',actual:'200'});const r=run();assert.equal(metric(r,'Actual operating remainder'),180000);assert.equal(metric(r,'Remainder variance'),-120000);assert(String(r.rows.at(-1)[5]).includes('zero'));}
 {const{s,run}=fixture(selected[1]);s.top.actualOpening='950';const r=run();assert.equal(metric(r,'Forecast closing cash'),170000);assert.equal(metric(r,'Actual closing cash'),125000);assert.equal(metric(r,'Closing cash difference'),-45000);}
 {const{s,run}=fixture(selected[2]);s.rows[0].inquiries='0';s.rows[0].customers='0';const r=run();assert(String(r.rows[0][6]).includes('zero'));assert(String(r.rows[0][7]).includes('zero'));assert.equal(metric(r,'Remaining actual budget'),10000);}
 {const{s,run}=fixture(selected[3]);s.rows[0].status='Supported';const r=run();assert.equal(metric(r,'Untested'),1);assert.equal(metric(r,'Supported'),1);assert.equal(metric(r,'Contradicted'),0);assert.equal(r.metrics.filter(m=>['Untested','Supported','Contradicted'].includes(m.label)).reduce((n,m)=>n+m.value,0),metric(r,'Assumptions entered'));}
 {const{s,run}=fixture(selected[4]);s.top.leave='8';s.rows.push({id:'new',label:'New project',hours:'4'});const r=run();assert.equal(metric(r,'Delivery capacity'),20);assert.equal(metric(r,'Free / overbooked'),-4);assert.equal(metric(r,'Capacity booked'),'120%');}
 {const{s,run}=fixture(selected[5]);s.rows[0].available='45';let r=run();assert.equal(r.rows[0][3],1.5);assert.equal(r.rows[0][4],10.5);assert.equal(metric(r,'Total unit gap across SKUs'),75);s.rows[0].weekly='0';r=run();assert.equal(metric(r,'Zero-demand rows'),1);}
 {const{s,run}=fixture(selected[6]);s.top.priceWeight='80';s.top.deliveryWeight='20';const r=run();assert.equal(metric(r,'Highest entered score'),74);assert(metric(r,'Top-scoring supplier(s)').includes(';'));s.top.priceWeight='0';s.top.deliveryWeight='0';assert.throws(run,/positive total score weight/);}
 {const{s,run}=fixture(selected[7]);s.rows[0].paid='120';const r=run();assert.equal(metric(r,'Consignor entitlement'),10000);assert.equal(metric(r,'Net settlement balance'),-2000);}
 {const{s,run}=fixture(selected[8]);s.rows[0].recount='0';const r=run();assert.equal(metric(r,'Net proposed unit change'),-50);assert.equal(metric(r,'Net proposed cost change'),-60000);}
 {const{s,run}=fixture(selected[9]);assert.equal(metric(run(),'Conflict intervals'),1);s.rows[1].start='2026-10-09T12:30';assert.equal(metric(run(),'Conflict intervals'),0);}
 console.log('PASS ten worked edge scenarios and all three assumption statuses');
}
(async()=>{scenarios();for(const slug of selected)await check(slug);const tagged=fs.readdirSync('tools',{withFileTypes:true}).filter(x=>x.isDirectory()).filter(x=>fs.existsSync('tools/'+x.name+'/index.html')&&fs.readFileSync('tools/'+x.name+'/index.html','utf8').includes('data-copy-summary="true"')).map(x=>x.name).sort();assert.deepEqual(tagged,[...selected].sort());console.log('PASS: feature activates on exactly ten selected planners');})().catch(error=>{console.error(error);process.exitCode=1;});
