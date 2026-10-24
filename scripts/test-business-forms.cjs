'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..'),api=require('../assets/js/business-forms.js'),configs=JSON.parse(fs.readFileSync(path.join(root,'assets/js/business-forms-configs.json'),'utf8'));let tests=0;
const check=(label,fn)=>{fn();tests++;};const copy=x=>JSON.parse(JSON.stringify(x));
for(const c of configs){
 const s=copy(c.sample);let r=api.evaluate(s);check(c.kind+' baseline',()=>{assert.equal(r.errors.length,0);assert.equal(r.totals[c.kind==='expense'?'net':c.kind==='requisition'?'total':'balance'],c.kind==='expense'?11800:c.kind==='requisition'?17000:4800);});
 check('backup roundtrip',()=>assert.deepEqual(api.validateBackup(JSON.parse(JSON.stringify(s)),c.kind),s));
 check('cross form backup rejected',()=>assert.throws(()=>api.validateBackup(s,c.kind==='order'?'expense':'order')));
 check('invalid dimensions rejected',()=>{const b=copy(s);b.rows.pop();assert.throws(()=>api.validateBackup(b,c.kind));});
 check('unknown version rejected',()=>assert.throws(()=>api.validateBackup({...s,version:2},c.kind)));
 for(const bad of ['-1','1.001','bad','1e3','Infinity','1000000001'])check('invalid amount '+bad,()=>{const b=copy(s);b.rows[0][c.kind==='expense'?5:4]=bad;assert(api.evaluate(b).errors.length);});
 check('partial new row blocks final',()=>{const b=copy(s);b.rows[9][1]='Incomplete';assert(api.evaluate(b).errors.length);assert.equal(Object.keys(api.evaluate(b).totals).length,0);});
 check('blank not a healthy zero',()=>{const b=copy(s);b.rows=Array.from({length:10},()=>Array(8).fill(''));assert(api.evaluate(b).errors.length);});
 check('CSV injection escaped',()=>{const b=copy(s);b.person='=HYPERLINK("bad")';assert(api.csv(b,c.headers).includes("'=HYPERLINK"));});
 check('no HTML interpreted by model',()=>{const b=copy(s);b.rows[0][1]='<img src=x onerror=alert(1)>';assert.equal(api.evaluate(b).errors.length,0);});
 if(c.kind==='expense'){
  check('company paid excluded',()=>{const b=copy(s);b.rows[3][5]='500';assert.equal(api.evaluate(b).totals.net,11800);});
  check('company eligible rejected',()=>{const b=copy(s);b.rows[3][6]='1';assert(api.evaluate(b).errors.length);});
  check('eligible above cost rejected',()=>{const b=copy(s);b.rows[0][6]='121';assert(api.evaluate(b).errors.length);});
  check('excess advance visible',()=>assert.equal(api.evaluate({...s,advance:'200'}).totals.net,-2200));
  check('prior reimbursement once',()=>assert.equal(api.evaluate({...s,prior:'18'}).totals.net,10000));
  check('bad calendar date rejected',()=>{const b=copy(s);b.rows[0][0]='2026-02-30';assert(api.evaluate(b).errors.length);});
 }else{
  for(const q of ['0','-1','1.0001'])check('invalid quantity '+q,()=>{const b=copy(s);b.rows[0][3]=q;assert(api.evaluate(b).errors.length);});
  check('fractional quantity rounded per line',()=>{const b=copy(s);b.rows[0][3]='2.5';b.rows[0][4]='4.01';assert.equal(api.evaluate(b).lines[0],1003);});
  check('free item valid with description',()=>{const b=copy(s);b.rows[0][4]='0';assert.equal(api.evaluate(b).errors.length,0);});
  check('line amount ceiling',()=>{const b=copy(s);b.rows[0][3]='1000000';b.rows[0][4]='1000000000';assert(api.evaluate(b).errors.length);});
  check('CSV has line amounts',()=>assert(api.csv(s,c.headers).includes(c.kind==='order'?'50.00':'120.00')));
  if(c.kind==='order'){
   check('overpayment visible',()=>assert.equal(api.evaluate({...s,paid:'80'}).totals.balance,-200));
   check('discount above gross blocked',()=>assert(api.evaluate({...s,discount:'79'}).errors.length));
  }else check('revised request stays draft',()=>{const b=copy(s);b.rows[0][3]='18';assert.equal(api.evaluate(b).totals.total,15800);assert.equal(api.evaluate(b).totals.headroom,200);assert.equal(b.decision,'Draft');});
 }
}
console.log('PASS '+tests+' business form calculation/backup/CSV checks');
