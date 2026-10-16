// DOM integration tests: do not claim these are device or browser rendering tests.
'use strict';const assert=require('node:assert/strict');const fs=require('node:fs');const {webcrypto}=require('node:crypto');
const {JSDOM}=require(process.env.NEXALY_JSDOM_PATH||'jsdom');
const configs=JSON.parse(fs.readFileSync('assets/js/oct16-planners-configs.json','utf8'));
async function test(c){
 const dom=new JSDOM(fs.readFileSync('tools/'+c.slug+'/index.html','utf8'),{url:'https://nexalyplanner.com/tools/'+c.slug+'/',runScripts:'outside-only'}),w=dom.window,d=w.document;const $=id=>d.getElementById(id);let downloads=[],prints=0;
 w.confirm=()=>true;w.print=()=>prints++;w.Blob=Blob;w.URL.createObjectURL=blob=>{downloads.push(blob);return 'blob:example';};w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){};
 w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
 if(!w.crypto.randomUUID)w.crypto.randomUUID=()=>webcrypto.randomUUID();
 for(const p of ['small-tools-models.js','oct16-planners-models.js','small-tools-ui.js','oct16-planners-ux.js',...(c.kind==='builder'?['keyword-workflows-preview.js']:[])])w.eval(fs.readFileSync('assets/js/'+p,'utf8'));
 $('tool-sample').click();await Promise.resolve();assert.equal($('tool-message').dataset.status,'success',c.slug);assert.equal(d.querySelectorAll('#tool-rows fieldset').length,c.sample.rows.length);assert($('tool-results').textContent.includes(c.sample.top.title));assert.equal($('report-heading').textContent,c.name+' report');for(const wrap of d.querySelectorAll('.table-wrap')){assert.equal(wrap.tabIndex,0);assert.equal(wrap.getAttribute('role'),'region');assert(wrap.getAttribute('aria-label'));assert(wrap.querySelector('caption'));}
 $('tool-save').click();const key='nexaly-free-tool-v1-'+c.slug;const saved=w.localStorage.getItem(key);assert(saved&&$('tool-saved').textContent.includes('Saved on this device'));assert.equal(JSON.parse(saved).state.rows.length,c.sample.rows.length);
 $('top-title').value='Changed name';$('top-title').dispatchEvent(new w.Event('input',{bubbles:true}));assert($('tool-results').textContent.includes('Inputs changed'));$('tool-restore').click();assert.equal($('top-title').value,c.sample.top.title);
 $('tool-json').click();let backup=JSON.parse(await downloads.pop().text());assert.equal(backup.tool,c.slug);assert.equal(backup.version,1);
 $('tool-csv').click();let csv=await downloads.pop().text();assert(csv.includes(c.name));assert(!csv.includes('NaN'));assert(csv.includes('Calculation / limitations'));
 $('tool-print').click();assert.equal(prints,1);if(c.kind==='builder'){assert(d.querySelector('.printable-page'));assert.equal(d.querySelectorAll('.print-slot').length,10);assert(d.getElementById('planner-paper-style').textContent.includes('letter'));}
 // A valid import shows a review dialog and only changes state when confirmed.
 backup.state.top.title='Imported fictional example';Object.defineProperty($('tool-import'),'files',{configurable:true,value:[{size:100,text:async()=>JSON.stringify(backup)}]});await $('tool-import').onchange();assert($('tool-import-dialog').open);assert.notEqual($('top-title').value,'Imported fictional example');$('tool-confirm-import').click();assert.equal($('top-title').value,'Imported fictional example');assert.equal(w.localStorage.getItem(key),saved,'import must not overwrite device save');
 backup.tool='wrong-tool';Object.defineProperty($('tool-import'),'files',{configurable:true,value:[{size:100,text:async()=>JSON.stringify(backup)}]});await $('tool-import').onchange();assert($('tool-message').textContent.includes('exact tool'));assert.equal($('top-title').value,'Imported fictional example');
 // Added/removed rows, CSV formula protection and text-only rendering.
 if(c.sample.rows.length===c.maxRows){$('tool-add').click();assert($('tool-message').textContent.includes('supports up to'));}else{$('tool-add').click();assert.equal(d.querySelectorAll('#tool-rows fieldset').length,c.sample.rows.length+1);d.querySelector('#tool-rows fieldset:last-child button').click();assert.equal(d.querySelectorAll('#tool-rows fieldset').length,c.sample.rows.length);}
 $('tool-sample').click();const first=c.rowFields.find(f=>f.type==='text');if(first){d.querySelector('#tool-rows [data-field="'+first.key+'"]').value='=HYPERLINK("x")';$('tool-csv').click();csv=await downloads.pop().text();assert(csv.includes("'=HYPERLINK"));d.querySelector('#tool-rows [data-field="'+first.key+'"]').value='<img src=x onerror=alert(1)>';$('tool-calculate').click();assert.equal(d.querySelectorAll('#tool-results img').length,0);assert($('tool-results').textContent.includes('<img src=x onerror=alert(1)>'));}
 // Browser storage failure must offer a backup and must not claim success.
 const oldSet=w.Storage.prototype.setItem;w.Storage.prototype.setItem=function(){throw Error('Blocked storage');};$('tool-save').click();assert($('tool-saved').textContent.includes('Device save failed'));w.Storage.prototype.setItem=oldSet;
 $('tool-reset').click();assert.equal(w.localStorage.getItem(key),null);assert.equal(d.querySelectorAll('#tool-rows fieldset').length,1);assert.equal($('top-title').value,'');
 dom.window.close();console.log('PASS DOM controls:',c.slug);
}
(async()=>{for(const c of configs)await test(c);console.log('PASS: 5 worksheets, calculation DOM, save/restore, import confirmation, wrong-tool rejection, backup, CSV escaping, print calls and storage failure');})().catch(e=>{console.error(e);process.exitCode=1;});
