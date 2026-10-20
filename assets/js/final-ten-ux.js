(function(){'use strict';
const app=document.querySelector('[data-tool]');if(!app||!document.querySelector('script[src*="final-ten-models.js"]'))return;
const results=document.getElementById('tool-results'),name=window.NexalySmallTools.configs.find(c=>c.slug===app.dataset.tool).name;
function enhance(scope){for(const wrap of scope.querySelectorAll('.table-wrap')){const table=wrap.querySelector('table');if(!table||wrap.dataset.accessible==='true')continue;wrap.dataset.accessible='true';const previous=wrap.previousElementSibling;const label=table.caption?.textContent||previous?.textContent||'Worksheet table';if(!table.caption){const caption=table.createCaption();caption.textContent=label;caption.className='report-table-caption';}wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label',label+' — scroll horizontally for more columns');}}
enhance(app);new MutationObserver(()=>enhance(results)).observe(results,{childList:true});
// Make printed reports identifiable even when the user's worksheet label is vague.
const reportHeading=document.getElementById('report-heading');reportHeading.textContent=name+' report';
})();
