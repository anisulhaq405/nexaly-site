(function(){
'use strict';
const app=document.querySelector('[data-tool][data-copy-summary="true"]');
if(!app)return;
const allowed=new Set(['monthly-business-budget-variance','cash-flow-variance-report','marketing-campaign-budget-planner','one-page-business-plan-builder','freelancer-weekly-capacity-planner','stock-coverage-planner','supplier-quote-comparison','consignment-settlement-planner','physical-count-adjustment-worksheet','rental-booking-conflict-checker']);
if(!allowed.has(app.dataset.tool))return;
const button=document.getElementById('tool-copy-summary'),status=document.getElementById('tool-copy-status'),fallback=document.getElementById('tool-copy-fallback'),text=document.getElementById('tool-copy-text'),report=document.getElementById('tool-results'),message=document.getElementById('tool-message');
if(!button||!status||!fallback||!text||!report||!message)return;
let revision=0,busy=false;
const ready=()=>message.dataset.status==='success'&&Boolean(report.querySelector('.metrics .metric'));
function refresh(){button.disabled=busy||!ready();}
function reset(){text.value='';fallback.hidden=true;status.textContent=ready()?'Current results are ready to copy.':'Calculate current results before copying a summary.';refresh();}
function invalidate(){revision++;reset();}
new MutationObserver(invalidate).observe(report,{childList:true,subtree:true,characterData:true});
new MutationObserver(invalidate).observe(message,{attributes:true,attributeFilter:['data-status'],childList:true,subtree:true,characterData:true});
app.addEventListener('input',event=>{if(event.target.closest('#tool-settings,#tool-rows'))invalidate();});
app.addEventListener('change',event=>{if(event.target.closest('#tool-settings,#tool-rows'))invalidate();});
function summary(){
 const lines=[document.querySelector('h1').textContent.trim(),report.querySelector('h3')?.textContent.trim()||''];
 const settings=Array.from(report.querySelectorAll('.report-settings > *'));
 for(let i=0;i+1<settings.length;i+=2)lines.push(settings[i].textContent.trim()+': '+settings[i+1].textContent.trim());
 lines.push('', 'Calculated summary');
 for(const card of report.querySelectorAll('.metrics .metric'))lines.push(card.querySelector('span').textContent.trim()+': '+card.querySelector('strong').textContent.trim());
 const notes=Array.from(report.querySelectorAll('.result-notes li')).map(item=>item.textContent.trim());
 if(notes.length)lines.push('', 'Review notes',...notes.map(note=>'- '+note));
 const rule=report.querySelector('.report-rule')?.textContent.trim();
 if(rule)lines.push('', 'Calculation and scope',rule);
 lines.push('', 'Summary only. Keep a JSON backup for editable entries; CSV contains the detailed report.');
 return lines.join('\n');
}
button.addEventListener('click',async()=>{
 if(!ready()||busy){reset();return;}
 const current=revision,value=summary();busy=true;refresh();
 try{
  if(!navigator.clipboard||typeof navigator.clipboard.writeText!=='function')throw Error('Clipboard unavailable');
  await navigator.clipboard.writeText(value);
  if(current!==revision)return;
  text.value=value;fallback.hidden=false;
  status.textContent='Result summary copied. Review notes and calculation limits are included; editable entries are not included.';
 }catch{
  if(current!==revision)return;
  text.value=value;fallback.hidden=false;text.focus();text.select();
  status.textContent='Automatic copy is unavailable. Select the summary below and copy it with your device’s copy command.';
 }finally{busy=false;refresh();}
});
reset();
})();
