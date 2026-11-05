'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const m=require('../assets/js/day2-planning-tools.js'),P='business-plan-template',C='business-startup-checklist';
const clone=v=>JSON.parse(JSON.stringify(v));
assert.deepEqual(m.summary(m.validate(C,m.sampleCheck)),{total:6,required:5,done:2,open:3,blocked:1,notApplicable:1,overdue:1,progress:40});
for(const kind of [P,C]){let v=kind===P?m.samplePlan:m.sampleCheck;assert.deepEqual(m.unpack(kind,m.pack(kind,v)),v);assert.throws(()=>m.unpack(kind,JSON.stringify({kind:'another',version:1,data:v})));assert.throws(()=>m.unpack(kind,'x'.repeat(m.MAX+1)));}
let draft=clone(m.samplePlan);for(const k of Object.keys(m.labels))draft[k]='';assert.match(m.reportHTML(draft),/Draft: 8 sections/);
for(const asof of ['2026-02-30','2026-13-01','','bad'])assert.throws(()=>m.validate(P,{...m.samplePlan,asof}));
let x=clone(m.sampleCheck);x.rows[0].evidence='';assert.throws(()=>m.validate(C,x));x=clone(m.sampleCheck);x.rows[5].evidence='';assert.throws(()=>m.validate(C,x));
x=clone(m.sampleCheck);x.rows=[];assert.throws(()=>m.validate(C,x));x.rows=Array(31).fill(m.sampleCheck.rows[0]);assert.throws(()=>m.validate(C,x));
assert.throws(()=>m.unpack(P,'{"kind":"business-plan-template","version":1,"data":{"__proto__":{}}}'));
x=clone(m.sampleCheck);x.rows=x.rows.map(r=>({...r,importance:'optional'}));assert.equal(m.summary(x).progress,null);assert.equal(m.summary(x).required,0);
x=clone(m.sampleCheck);x.name=' =1+1';assert.match(m.csv(x),/"' =1\+1"/);
assert.ok(!m.reportHTML({...m.samplePlan,customer:'<script>alert(1)</script>'}).includes('<script>'));
assert.match(m.reportHTML({...m.samplePlan,customer:'<img src=x>'}),/&lt;img/);
const {JSDOM}=require(process.env.NEXALY_JSDOM_PATH||'jsdom');
(async()=>{
for(const kind of [P,C]){
 let dom=new JSDOM(fs.readFileSync(path.join(__dirname,'../tools',kind,'index.html'),'utf8'),{url:'https://nexalyplanner.com/tools/'+kind+'/',runScripts:'outside-only'}),w=dom.window,d=w.document,downloads=[],printed=0;
 w.TextEncoder=TextEncoder;w.URL.createObjectURL=()=> 'blob:test';w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){downloads.push(this.download);};w.print=()=>printed++;w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
 w.eval(fs.readFileSync(path.join(__dirname,'../assets/js/day2-planning-tools.js'),'utf8'));
 d.getElementById('d2-export').click();assert.equal(downloads.length,0);d.getElementById('d2-sample').click();d.getElementById('d2-form').dispatchEvent(new w.Event('submit',{bubbles:true,cancelable:true}));assert.match(d.getElementById('d2-result').textContent,kind===C?/40%/:/Eight sections/);
 d.getElementById('d2-print').click();assert.equal(printed,1);d.getElementById('d2-export').click();assert.equal(downloads.length,1);
 d.getElementById('d2-name').value='Changed';d.getElementById('d2-name').dispatchEvent(new w.Event('input',{bubbles:true}));d.getElementById('d2-export').click();assert.equal(downloads.length,1);assert.match(d.getElementById('d2-result').textContent,/Inputs changed/);
 const backup=w.Day2Planning.pack(kind,kind===P?w.Day2Planning.samplePlan:w.Day2Planning.sampleCheck),input=d.getElementById('d2-import');Object.defineProperty(input,'files',{configurable:true,value:[{size:backup.length,text:async()=>backup}]});await input.onchange({target:input});assert.ok(d.getElementById('d2-import-dialog').open);assert.equal(d.getElementById('d2-name').value,'Changed');d.getElementById('d2-confirm').click();assert.match(d.getElementById('d2-name').value,/Fictional/);assert.match(d.getElementById('d2-result').textContent,/Inputs changed/);
 d.getElementById('d2-clear').click();assert.ok(d.getElementById('d2-clear-dialog').open);d.getElementById('d2-clear-confirm').click();assert.equal(d.getElementById('d2-name').value,'');assert.equal(w.localStorage.length,0);dom.window.close();
}
console.log('PASS Day2: strict schema/date/size/evidence rules, denominator/zero cases, escaped HTML, CSV protection, backup/import confirmation, stale exports, print and clear controls.');
})().catch(e=>{console.error(e);process.exitCode=1;});
