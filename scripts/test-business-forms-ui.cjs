'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM}=require(process.env.NEXALY_JSDOM_PATH||'jsdom');const root=path.join(__dirname,'..');const configs=JSON.parse(fs.readFileSync(path.join(root,'assets/js/business-forms-configs.json'),'utf8'));let checks=0;
(async()=>{
for(const c of configs){
 const html=fs.readFileSync(path.join(root,'tools',c.slug,'index.html'),'utf8');const dom=new JSDOM(html,{url:'https://nexalyplanner.com/tools/'+c.slug+'/',runScripts:'outside-only'});const w=dom.window,d=w.document;w.confirm=()=>true;let printed=0,clicked=0;w.print=()=>printed++;w.URL.createObjectURL=()=> 'blob:test';w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){clicked++;};
 w.eval(fs.readFileSync(path.join(root,'assets/js/business-forms.js'),'utf8'));
 const click=a=>d.querySelector('[data-action="'+a+'"]').click(),result=()=>d.querySelector('[data-result]').textContent,status=()=>d.querySelector('[data-status]').textContent;
 assert(result().includes('Complete the worksheet'));checks++;
 click('sample');assert(result().includes(c.kind==='expense'?'118.00':c.kind==='requisition'?'170.00':'48.00'));checks++;
 const field=d.querySelector('[data-field="reference"]');field.value='<script>test</script>';field.dispatchEvent(new w.Event('input',{bubbles:true}));click('save');assert(status().includes('Saved in this browser'));checks++;
 click('blank');assert.equal(field.value,'');click('restore');assert.equal(field.value,'<script>test</script>');assert.equal(d.querySelectorAll('[data-result] script').length,0);checks++;
 click('backup');click('csv');assert.equal(clicked,2);checks++;
 click('print');assert.equal(printed,1);assert(d.querySelector('.form-print-copy').textContent.includes('NexalyPlanner'));assert(d.querySelector('.form-print-copy').textContent.includes('<script>test</script>'));checks++;
 const importer=d.querySelector('[data-import]');const restored=JSON.parse(JSON.stringify(c.sample));restored.reference='IMPORTED-42';Object.defineProperty(importer,'files',{configurable:true,value:[{size:100,text:async()=>JSON.stringify(restored)}]});importer.dispatchEvent(new w.Event('change',{bubbles:true}));await new Promise(resolve=>setImmediate(resolve));assert.equal(field.value,'IMPORTED-42');checks++;
 Object.defineProperty(importer,'files',{configurable:true,value:[{size:100,text:async()=>JSON.stringify({...restored,kind:'wrong'})}]});importer.dispatchEvent(new w.Event('change',{bubbles:true}));await new Promise(resolve=>setImmediate(resolve));assert(d.querySelector('[data-status]').textContent.includes('Backup not restored'));assert.equal(field.value,'IMPORTED-42');checks++;
 const input=d.querySelector('[data-row="0"][data-col="'+(c.kind==='expense'?5:4)+'"]');input.value='bad';input.dispatchEvent(new w.Event('input',{bubbles:true}));assert(result().includes('Complete the worksheet'));assert.equal(d.querySelector('[data-result] dl'),null);checks++;
 const labels=[...d.querySelectorAll('[data-row]')];assert(labels.every(x=>x.getAttribute('aria-label')));checks++;
 // Storage failure stays actionable; it must not claim save succeeded.
 Object.defineProperty(w,'localStorage',{get(){throw new Error('Storage disabled');}});click('save');assert(status().includes('Could not complete'));checks++;
 dom.window.close();
}
console.log('PASS '+checks+' business form DOM interaction checks; not a real-browser certification');
})().catch(e=>{console.error(e);process.exit(1);});
