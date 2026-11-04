'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const m=require('../assets/js/day1-planning-tools.js');
const C='adhd-cleaning-planner',B='business-plan-cover-page';
const clean={week:'Example',rows:[{day:'Monday',room:'Office',task:'Desk',minutes:5,status:'done'},{day:'Tuesday',room:'Kitchen',task:'Sink',minutes:10,status:'planned'},{day:'Friday',room:'Bedroom',task:'Fold',minutes:5,status:'skipped'}]};
assert.deepEqual(m.summarize(m.validate(C,clean)),{total:20,done:5,planned:10,skipped:5,count:3});assert.deepEqual(m.unpack(C,m.pack(C,clean)),clean);
for(const minutes of [0,181,1.5,NaN,Infinity])assert.throws(()=>m.validate(C,{...clean,rows:[{...clean.rows[0],minutes}]}));
assert.throws(()=>m.validate(C,{week:' ',rows:[]}));assert.throws(()=>m.validate(C,{...clean,rows:Array(21).fill(clean.rows[0])}));assert.throws(()=>m.validate(C,{...clean,unexpected:true}));
assert.throws(()=>m.unpack(C,'x'.repeat(16385)));assert.throws(()=>m.unpack(C,JSON.stringify({kind:B,version:1,data:clean})));assert.throws(()=>m.unpack(C,'{"kind":"adhd-cleaning-planner","version":1,"data":{"__proto__":{},"week":"x","rows":[]}}'));
assert.match(m.csv({...clean,week:' =2+2'}),/"' =2\+2"/);
let cover={company:'<img src=x onerror=alert(1)>',title:'Plan',subtitle:'<script>alert(1)</script>',author:'Owner',recipient:'',contact:'',version:'1',issued:'2026-11-04',classification:''};
let html=m.coverHTML(cover);assert.ok(!html.includes('<script>'));assert.ok(html.includes('&lt;script&gt;'));assert.ok(html.includes('&lt;img'));assert.deepEqual(m.unpack(B,m.pack(B,cover)),cover);
for(const issued of ['2026-02-30','2026-13-01','2026-1-1',''])assert.throws(()=>m.validate(B,{...cover,issued}));
const {JSDOM}=require(process.env.NEXALY_JSDOM_PATH||'jsdom');
for(const kind of [C,B]){
 const page=fs.readFileSync(path.join(__dirname,'../tools',kind,'index.html'),'utf8'),dom=new JSDOM(page,{url:'https://nexalyplanner.com/tools/'+kind+'/',runScripts:'outside-only'}),w=dom.window,d=w.document;let printed=0,downloads=[];
 w.TextEncoder=TextEncoder;w.URL.createObjectURL=()=> 'blob:test';w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){downloads.push(this.download);};w.print=()=>printed++;
 w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
 w.eval(fs.readFileSync(path.join(__dirname,'../assets/js/day1-planning-tools.js'),'utf8'));
 d.getElementById('d1-print').click();assert.equal(printed,0);assert.match(d.getElementById('d1-status').textContent,/Review current/);
 d.getElementById('d1-sample').click();d.getElementById('d1-form').dispatchEvent(new w.Event('submit',{bubbles:true,cancelable:true}));
 assert.match(d.getElementById('d1-result').textContent,kind===C?/20 estimated minutes/:/Capsule Collection Business Plan/);
 d.getElementById('d1-print').click();assert.equal(printed,1);d.getElementById('d1-export').click();assert.equal(downloads.length,1);
 d.querySelector('#d1-form input').dispatchEvent(new w.Event('input',{bubbles:true}));d.getElementById('d1-export').click();assert.equal(downloads.length,1);assert.match(d.getElementById('d1-result').textContent,/Inputs changed/);
 d.getElementById('d1-clear').click();assert.ok(d.getElementById('d1-clear-dialog').open);d.getElementById('d1-clear-confirm').click();assert.equal(d.getElementById('d1-clear-dialog').open,false);
 assert.equal(w.localStorage.length,0);dom.window.close();
}
console.log('PASS Day1: estimates, boundary validation, strict backup types, CSV injection protection, escaped cover HTML, stale results, download gating, print and clear controls.');
