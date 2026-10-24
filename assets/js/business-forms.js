/* Original local business forms. No worksheet data is transmitted. */
(function(root){'use strict';
const currencies=['USD','CAD','GBP','EUR','AUD','NZD'];
const text=v=>typeof v==='string'&&v.length<=1000;
const money=v=>typeof v==='string'&&/^\d+(\.\d{1,2})?$/.test(v)&&Number(v)<=1e9;
const qty=v=>typeof v==='string'&&/^\d+(\.\d{1,3})?$/.test(v)&&Number(v)>0&&Number(v)<=1e6;
const cents=v=>Math.round(Number(v)*100);
const date=v=>/^\d{4}-\d{2}-\d{2}$/.test(v)&&!isNaN(Date.parse(v+'T00:00:00Z'))&&new Date(v+'T00:00:00Z').toISOString().slice(0,10)===v;
function evaluate(s){
 const errors=[],totals={};let count=0,items=0,eligible=0;
 if(!s||!['expense','requisition','order'].includes(s.kind)||!Array.isArray(s.rows)||s.rows.length!==10)return{errors:['Invalid worksheet'],totals:{},lines:[]};
 const lines=s.rows.map((r,i)=>{
  if(!Array.isArray(r)||r.length!==8||r.some(v=>!text(v))){errors.push('Row '+(i+1)+': invalid data');return null;}
  const used=r.some((v,j)=>(s.kind==='expense'||j!==5)&&v.trim()!=='');if(!used)return null;count++;
  if(s.kind==='expense'){
   if(!date(r[0])||!r[1].trim()||!r[2].trim()||!r[3].trim()||!['Employee','Company'].includes(r[4])||!money(r[5])||!money(r[6])||cents(r[6])>cents(r[5])||(r[4]==='Company'&&cents(r[6])!==0)||!r[7].trim()){errors.push('Row '+(i+1)+': complete date, merchant, purpose, category, payer, amounts and receipt; eligible cannot exceed cost, and company-paid eligible must be 0');return null;}
   items+=cents(r[5]);if(r[4]==='Employee')eligible+=cents(r[6]);return cents(r[6]);
  }
  if(!r[1].trim()||!r[2].trim()||!qty(r[3])||!money(r[4])){errors.push('Row '+(i+1)+': enter description, unit/variant, positive quantity (up to 3 decimals) and nonnegative price (up to 2 decimals)');return null;}
  const line=Math.round((Number(r[3])*cents(r[4]))+1e-7);if(line>1e11){errors.push('Row '+(i+1)+': line amount exceeds 1 billion');return null;}items+=line;return line;
 });
 if(!count)errors.push('Add at least one complete item.');
 const keys=s.kind==='expense'?['advance','prior']:s.kind==='requisition'?['shipping','tax','budget']:['shipping','tax','discount','paid'];
 keys.forEach(k=>{if(!money(s[k]))errors.push('Enter '+k+' as a nonnegative amount with up to two decimals; use 0 for none.');});
 if(errors.length)return{errors,totals:{},lines};
 if(s.kind==='expense')Object.assign(totals,{recorded:items,eligible,advance:cents(s.advance),prior:cents(s.prior),net:eligible-cents(s.advance)-cents(s.prior)});
 else if(s.kind==='requisition')Object.assign(totals,{items,shipping:cents(s.shipping),tax:cents(s.tax),total:items+cents(s.shipping)+cents(s.tax),budget:cents(s.budget),headroom:cents(s.budget)-items-cents(s.shipping)-cents(s.tax)});
 else{
  const before=items+cents(s.shipping)+cents(s.tax);if(cents(s.discount)>before)return{errors:['Discount cannot exceed items plus shipping and tax.'],totals:{},lines};
  Object.assign(totals,{items,shipping:cents(s.shipping),tax:cents(s.tax),discount:cents(s.discount),total:before-cents(s.discount),paid:cents(s.paid),balance:before-cents(s.discount)-cents(s.paid)});
 }
 return{errors,totals,lines};
}
const headerKeys=['reference','person','date','currency','party','due','notes','reviewer','decision','reviewDate','related'];
function validateBackup(data,kind){
 if(!data||data.version!==1||data.kind!==kind)throw Error('Choose a version 1 backup for this form.');
 const keys=[...headerKeys,...(kind==='expense'?['advance','prior']:kind==='requisition'?['shipping','tax','budget']:['shipping','tax','discount','paid'])];
 const clean={version:1,kind};keys.forEach(k=>{if(!text(data[k]))throw Error('Invalid field: '+k);clean[k]=data[k];});
 if(!['Draft','In review','Approved','Declined','Confirmed'].includes(clean.decision))throw Error('Unsupported review status.');
 if(!currencies.includes(clean.currency))throw Error('Unsupported currency.');
 if(!Array.isArray(data.rows)||data.rows.length!==10||data.rows.some(r=>!Array.isArray(r)||r.length!==8||r.some(v=>!text(v))))throw Error('Backup must contain ten rows of eight text fields.');
 clean.rows=data.rows.map(r=>r.slice());return clean;
}
function csvCell(v){const s=String(v??'');return '"'+(/^[\s]*[=+@-]/.test(s)?"'":'')+s.replace(/"/g,'""')+'"';}
function csv(s,headers){const result=evaluate(s);const rows=[['NexalyPlanner',s.kind],...headerKeys.map(k=>[k,s[k]]),[],headers,...s.rows.map((r,i)=>s.kind==='expense'?r:r.map((v,j)=>j===5?(result.lines[i]===null||result.lines[i]===undefined?'':(result.lines[i]/100).toFixed(2)):v)),[],['Calculation status',result.errors.join('; ')||'Calculated; manual review required'],['Currency',s.currency],...Object.entries(result.totals).map(([k,v])=>[k,(v/100).toFixed(2)])];return '\ufeff'+rows.map(r=>r.map(csvCell).join(',')).join('\r\n');}
const api={evaluate,validateBackup,csv,currencies};if(typeof module!=='undefined'&&module.exports)module.exports=api;if(root)root.NexalyBusinessForms=api;
if(typeof document==='undefined')return;
const app=document.querySelector('[data-business-form]');if(!app)return;
const config=JSON.parse(document.getElementById('business-form-config').textContent),kind=config.kind,key='nexaly-business-form-v1-'+kind;
const blank=()=>{const s=JSON.parse(JSON.stringify(config.sample));Object.keys(s).forEach(k=>{if(!['version','kind','rows'].includes(k))s[k]='';});s.currency='USD';s.decision='Draft';s.rows=Array.from({length:10},()=>Array(8).fill(''));return s;};
let state=blank();const status=app.querySelector('[data-status]'),resultBox=app.querySelector('[data-result]');
function message(s){status.textContent=s;}
function sync(){app.querySelectorAll('[data-field]').forEach(el=>state[el.dataset.field]=el.value);app.querySelectorAll('[data-row]').forEach(el=>state.rows[Number(el.dataset.row)][Number(el.dataset.col)]=el.value);}
function draw(){app.querySelectorAll('[data-field]').forEach(el=>el.value=state[el.dataset.field]||'');app.querySelectorAll('[data-row]').forEach(el=>el.value=state.rows[Number(el.dataset.row)][Number(el.dataset.col)]);calculate();}
const format=v=>state.currency+' '+(v/100).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
const names={recorded:'Recorded costs',eligible:'Employee-paid eligible',advance:'Advance',prior:'Prior reimbursement',net:'Net reimbursement',items:'Items subtotal',shipping:'Shipping',tax:'Entered tax',total:kind==='requisition'?'Estimated request':'Order total',budget:'Available budget',headroom:'Budget headroom',discount:'Discount',paid:'Paid to date',balance:'Balance remaining'};
function calculate(){
 sync();const result=evaluate(state);resultBox.replaceChildren();
 app.querySelectorAll('[data-line]').forEach((el,i)=>el.textContent=result.lines[i]===null||result.lines[i]===undefined?'—':format(result.lines[i]));
 const h=document.createElement('h3');h.textContent=result.errors.length?'Complete the worksheet':'Calculated amounts';resultBox.append(h);
 if(result.errors.length){const ul=document.createElement('ul');result.errors.forEach(t=>{const li=document.createElement('li');li.textContent=t;ul.append(li);});resultBox.append(ul);return;}
 const dl=document.createElement('dl');Object.entries(result.totals).forEach(([k,v])=>{const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=names[k];dd.textContent=format(v);dl.append(dt,dd);});resultBox.append(dl);
 const note=document.createElement('p');note.textContent=kind==='expense'?(result.totals.net<0?'Negative net: review the advance or prior reimbursement balance.':'Reimbursement remains subject to your manual review.'):kind==='requisition'?(result.totals.headroom<0?'Over the entered budget. Revise or obtain a separate budget decision.':'Within the entered budget. This does not approve the request.'):(result.totals.balance<0?'Overpayment: review the amount and payment record.':'Keep payment evidence separate from the order request.');resultBox.append(note);
 const missing=['reference','person','date','party','due','notes'].filter(k=>!state[k].trim());if(missing.length){const p=document.createElement('p');p.textContent='Draft header: complete '+missing.join(', ')+' before sharing.';resultBox.append(p);}
}
function makePrintCopy(){
 let block=app.querySelector('.form-print-copy');if(block)block.remove();block=document.createElement('section');block.className='form-print-copy';
 const add=(tag,value)=>{const el=document.createElement(tag);el.textContent=value;block.append(el);return el;};
 add('h2',config.name+' — '+(state.reference||'Draft'));
 add('p','NexalyPlanner | Currency: '+state.currency+' | Manual status: '+state.decision);
 const meta=document.createElement('dl');app.querySelectorAll('[data-field]').forEach(el=>{const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=el.closest('label').firstChild.textContent;dd.textContent=el.value||'Not entered';meta.append(dt,dd);});block.append(meta);
 const table=document.createElement('table'),tr=document.createElement('tr');config.headers.forEach(h=>{const th=document.createElement('th');th.textContent=h;tr.append(th);});table.append(tr);
 const result=evaluate(state);state.rows.forEach((r,i)=>{if(!r.some(v=>v.trim()))return;const row=document.createElement('tr');r.forEach((v,j)=>{const td=document.createElement('td');td.textContent=kind!=='expense'&&j===5?(result.lines[i]===null?'Incomplete':format(result.lines[i])):v;row.append(td);});table.append(row);});block.append(table);
 const summary=resultBox.cloneNode(true);summary.removeAttribute('data-result');summary.removeAttribute('aria-live');block.append(summary);add('p','Manual worksheet. Check source documents and review status before sharing.');app.append(block);
}
function download(contents,type,extension){const blob=new Blob([contents],{type}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=config.slug+'.'+extension;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);message('Download requested. Check your browser downloads; keep the file before closing this page.');}
app.addEventListener('input',calculate);app.addEventListener('change',calculate);
app.addEventListener('click',e=>{const button=e.target.closest('[data-action]');if(!button)return;const action=button.dataset.action;
 try{
  sync();
  if(action==='sample'){if(!confirm('Replace the current worksheet with fictional example data?'))return;state=JSON.parse(JSON.stringify(config.sample));draw();message('Fictional example loaded. It has not been saved over your device copy.');}
  if(action==='blank'){if(!confirm('Clear current entries? Your saved device copy stays available.'))return;state=blank();draw();message('Blank worksheet opened.');}
  if(action==='save'){localStorage.setItem(key,JSON.stringify(state));message('Saved in this browser on this device. Download a backup for another browser or device.');}
  if(action==='restore'){const raw=localStorage.getItem(key);if(!raw){message('No saved copy in this browser.');return;}const restored=validateBackup(JSON.parse(raw),kind);if(!confirm('Replace current entries with your saved device copy?'))return;state=restored;draw();message('Saved device copy restored.');}
  if(action==='backup')download(JSON.stringify(state,null,2),'application/json','json');
  if(action==='csv')download(csv(state,config.headers),'text/csv;charset=utf-8','csv');
  if(action==='print'){calculate();makePrintCopy();message('Opening browser print. Choose Save as PDF if your browser offers it.');window.print();}
 }catch(err){message('Could not complete the action: '+err.message+'. Try downloading a JSON backup if browser storage is unavailable.');}
});
app.querySelector('[data-import]').addEventListener('change',async e=>{const f=e.target.files[0];if(!f)return;try{if(f.size>200000)throw Error('Backup is too large');const next=validateBackup(JSON.parse(await f.text()),kind);if(!confirm('Replace current entries with this backup?'))return;state=next;draw();message('Backup restored. Save on this device if you want to keep this version here.');}catch(err){message('Backup not restored: '+err.message);}finally{e.target.value='';}});
draw();
})(typeof window==='undefined'?null:window);
