(function(){
'use strict';
const app=document.querySelector('.next-tool[data-tool]');
if(!app)return;
const add=document.getElementById('tool-add'),message=document.getElementById('tool-message'),heading=document.getElementById('report-heading');
if(add&&app.dataset.addLabel)add.textContent=app.dataset.addLabel;
if(heading)heading.tabIndex=-1;
app.addEventListener('click',function(event){
  if(event.target.closest('#tool-calculate')&&message.dataset.status==='success'&&heading){
    heading.focus({preventScroll:true});
    heading.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
  }
  if(event.target.closest('#tool-calculate')&&message.dataset.status==='error'){
    const invalid=Array.from(app.querySelectorAll('#tool-settings input,#tool-settings select,#tool-rows input,#tool-rows select')).find(input=>!input.checkValidity());
    if(invalid){invalid.setAttribute('aria-invalid','true');invalid.setAttribute('aria-errormessage','tool-message');invalid.focus();}
  }
});
app.addEventListener('input',function(event){if(event.target.matches('input,select')){event.target.removeAttribute('aria-invalid');event.target.removeAttribute('aria-errormessage');}});
app.addEventListener('change',function(event){if(event.target.matches('input,select')){event.target.removeAttribute('aria-invalid');event.target.removeAttribute('aria-errormessage');}});
})();
