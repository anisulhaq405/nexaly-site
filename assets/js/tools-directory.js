(function(){
'use strict';
const input=document.getElementById('tool-search'),status=document.getElementById('search-status');
if(!input||!status)return;
const cards=Array.from(document.querySelectorAll('.directory-tool')),groups=Array.from(document.querySelectorAll('.tool-category'));
const filters=Array.from(document.querySelectorAll('[data-filter]')),empty=document.getElementById('library-empty'),clear=document.getElementById('clear-search'),reset=document.getElementById('library-reset');
function normalize(value){return String(value).normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();}
const searchable=new Map(cards.map(card=>[card,normalize((card.dataset.search||'')+' '+card.querySelector('h3').textContent+' '+card.querySelector('.library-card-description').textContent)]));
const categoryNames=new Map(groups.map(group=>[group.id,group.querySelector('h2').textContent]));
let category=categoryNames.has(location.hash.slice(1))?location.hash.slice(1):'all';
function update(){
  const words=normalize(input.value).split(' ').filter(Boolean);let shown=0;
  cards.forEach(card=>{const inCategory=category==='all'||(category==='latest'?card.dataset.latest==='true':card.dataset.category===category);const match=inCategory&&words.every(word=>searchable.get(card).includes(word));card.hidden=!match;if(match)shown++;});
  groups.forEach(group=>{const count=Array.from(group.querySelectorAll('.directory-tool')).filter(card=>!card.hidden).length;group.hidden=count===0;group.dataset.visibleCount=String(count);const label=group.querySelector('.category-count');if(label)label.textContent=count+' planner'+(count===1?'':'s');});
  filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===category)));
  status.textContent=shown+' planner'+(shown===1?'':'s')+(category==='all'?'':category==='latest'?' · latest additions':' · '+categoryNames.get(category));
  if(empty)empty.hidden=shown!==0;
  if(clear)clear.hidden=input.value.length===0;
  if(reset)reset.hidden=category==='all'&&input.value.length===0;
  const caption=document.getElementById('active-filter');if(caption)caption.textContent=words.length?'Results for “'+input.value.trim()+'”':category==='latest'?'The latest eight additions to the collection.':'Browse the planners in this category.';
}
function resetAll(){input.value='';category='all';history.replaceState(null,'',location.pathname+location.search+'#browse');update();input.focus();}
input.addEventListener('input',update);
if(clear)clear.addEventListener('click',()=>{input.value='';update();input.focus();});
filters.forEach(button=>button.addEventListener('click',()=>{category=button.dataset.filter;history.replaceState(null,'',location.pathname+location.search+'#'+(categoryNames.has(category)?category:'browse'));update();}));
const resetButton=document.getElementById('reset-filters');if(resetButton)resetButton.addEventListener('click',resetAll);
const emptyReset=document.getElementById('empty-reset');if(emptyReset)emptyReset.addEventListener('click',resetAll);
window.addEventListener('hashchange',()=>{const hash=location.hash.slice(1);if(categoryNames.has(hash)){category=hash;update();}});
document.querySelectorAll('[data-directory-controls]').forEach(control=>control.hidden=false);
update();
})();
