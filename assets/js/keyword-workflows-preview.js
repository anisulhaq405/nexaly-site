(function(){'use strict';const app=document.querySelector('[data-tool="printable-planner-builder"]');if(!app)return;
const target=document.getElementById('tool-results');
function el(tag,text,cls){const n=document.createElement(tag);if(text)n.textContent=text;if(cls)n.className=cls;return n;}
function draw(){if(target.querySelector('.printable-page')||!target.querySelector('.metrics'))return;
try{const c=window.NexalySmallTools.configs.find(x=>x.kind==='builder'),top=Object.fromEntries(c.fields.map(f=>[f.key,document.getElementById('top-'+f.key).value])),rows=[...document.querySelectorAll('#tool-rows fieldset')].map((r,i)=>({id:'preview-'+i,...Object.fromEntries(c.rowFields.map(f=>[f.key,r.querySelector('[data-field="'+f.key+'"]').value]))})),p=window.NexalySmallTools.evaluate(c.slug,{top,rows}).preview;
const page=el('section',undefined,'printable-page');page.setAttribute('aria-label','Printable planner preview');page.dataset.paper=p.paper;page.append(el('h3',p.title),el('p',p.layout==='Daily'?p.date:p.slots[0]+' to '+p.slots[6]));
const schedule=el('div',undefined,p.layout==='Daily'?'daily-print-schedule':'weekly-print-schedule');for(const slot of p.slots){const cell=el('div',undefined,'print-slot');cell.append(el('b',slot));schedule.append(cell);}page.append(schedule);
const notes=el('div',undefined,'print-sections');for(const s of p.sections){const box=el('section');box.append(el('h4',s.name));for(let i=0;i<s.lines;i++)box.append(el('div',undefined,'writing-line'));notes.append(box);}page.append(notes);target.prepend(page);
let style=document.getElementById('planner-paper-style');if(!style){style=el('style');style.id='planner-paper-style';document.head.append(style);}style.textContent='@page{size:'+({'US Letter':'letter',A4:'A4',A5:'A5'}[p.paper])+' portrait;margin:10mm}';
}catch(e){document.getElementById('tool-message').textContent=e.message;}}
new MutationObserver(draw).observe(target,{childList:true});
// Printing must see the preview synchronously, before the browser snapshots the page.
const oldPrint=window.print.bind(window);window.print=function(){draw();oldPrint();};
})();
