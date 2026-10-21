(function(){'use strict';
const app=document.querySelector('[data-tool]');if(!app||!document.querySelector('script[src*="final-ten-models.js"]'))return;
const results=document.getElementById('tool-results'),name=window.NexalySmallTools.configs.find(c=>c.slug===app.dataset.tool).name;
function enhance(scope){for(const wrap of scope.querySelectorAll('.table-wrap')){const table=wrap.querySelector('table');if(!table||wrap.dataset.accessible==='true')continue;wrap.dataset.accessible='true';const previous=wrap.previousElementSibling;const label=table.caption?.textContent||previous?.textContent||'Worksheet table';if(!table.caption){const caption=table.createCaption();caption.textContent=label;caption.className='report-table-caption';}wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label',label+' — scroll horizontally for more columns');}}
enhance(app);new MutationObserver(()=>enhance(results)).observe(results,{childList:true});
// Make printed reports identifiable even when the user's worksheet label is vague.
const reportHeading=document.getElementById('report-heading');reportHeading.textContent=name+' report';
// Native required checks miss whitespace-only text and duplicate references.
app.addEventListener('click',function(event){
 if(!event.target.closest('#tool-calculate,#tool-csv,#tool-print'))return;
 const message=document.getElementById('tool-message');
 if(message.dataset.status!=='error')return;
 const controls=[...app.querySelectorAll('#tool-settings input,#tool-settings select,#tool-rows input,#tool-rows select')];
 let invalid=controls.find(input=>!input.checkValidity()||(input.required&&input.type==='text'&&!input.value.trim()));
 if(!invalid&&message.textContent.startsWith('Duplicate record reference:')){
  const seen=new Set();invalid=controls.filter(input=>input.dataset.field==='ref').find(input=>{const key=input.value.trim().toLowerCase();if(seen.has(key))return true;seen.add(key);return false;});
 }
 if(invalid){invalid.setAttribute('aria-invalid','true');invalid.setAttribute('aria-errormessage','tool-message');invalid.focus();}
});
})();
