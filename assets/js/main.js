var $ = function(id){return document.getElementById(id);};

/* ===== PLANNERS DATA =====
   To publish a planner, fill these fields for it:
     img:    cover image path, e.g. "/images/products/daily-ritual.jpg"
     video:  YouTube EMBED url, e.g. "https://www.youtube.com/embed/VIDEOID"  (leave "" for none)
     buyUrl: Lemon Squeezy checkout link, e.g. "https://nexaly.lemonsqueezy.com/buy/xxxx"
     url:    dedicated product page, e.g. "/planners/offline-ai-business-copilot/" (card links there instead of the quick modal)
   Leave img/video/buyUrl as "" and a styled placeholder is shown until you add them. */
var products = [
  {title:"RepairBench OS — Small Engine Repair Shop Manager", cat:"Business Operating Systems", desc:"An offline small engine repair shop manager in one file — work orders and repair jobs, customers and machines, parts inventory and reorder, invoices, payments and profit, plus branded reports. No account, no subscription.", price:24.99, img:"/images/products/repairbench-os.jpg", video:"", buyUrl:"", url:"/planners/repairbench-os/", m1:"#D7E8E0", m2:"#CFE3DA"},
  {title:"AI Student Planner — Offline Study Planner, Assignment Tracker & Exam Planner", cat:"Digital Planners", desc:"An offline, all-in-one AI study OS for students — timetable, study planner, assignments, exams, focus timer, revision, grades, analytics and a built-in AI assistant in 16 modules. 7 languages, no subscription.", price:11.99, img:"/images/products/ai-student-planner.jpg", video:"", buyUrl:"", url:"/planners/ai-student-planner/", m1:"#E6E6FB", m2:"#DCE4F7"},
  {title:"Digital Homeschool Planner — Offline Multi-Kid Dashboard, Gradebook & Transcript", cat:"Digital Planners", desc:"A private, offline homeschool planner for multiple kids — command center, curriculum, lessons, calendar, assignments, gradebook, attendance, analytics and transcript, with a built-in AI assistant. 7 languages, no subscription.", price:14.99, img:"/images/products/digital-homeschool-planner.jpg", video:"", buyUrl:"", url:"/planners/digital-homeschool-planner/", m1:"#DDE8F5", m2:"#D5E5F0"},
  {title:"ADHD Digital Planner — Focus, Tasks, Routines & Goals", cat:"Digital Planners", desc:"A calm, interactive ADHD-friendly planner for adults with a daily focus dashboard, brain dump, tasks, routines, goals, habit and mood trackers, Pomodoro timer, analytics and an emergency reset. Works offline in your browser, 7 languages, no subscription.", price:14.99, img:"/images/products/adhd-digital-planner.png", fit:"contain", video:"", buyUrl:"", url:"/planners/adhd-digital-planner/", m1:"#EEEAFB", m2:"#DCE8F8"},
  {title:"Boutique Business Planner — Orders, Inventory, Pricing & Profit Dashboard", cat:"Digital Planners", desc:"An interactive boutique and small-business planner with a live dashboard, product pricing calculator, inventory, order and sales tracking, clients, income, expenses, automatic profit, marketing and goals. Works in any browser, saves locally and requires no subscription.", price:19.99, img:"/images/products/boutique-business-planner.png", fit:"contain", video:"", buyUrl:"", url:"/planners/boutique-business-planner/", m1:"#F8E6EE", m2:"#E6F1EC"},
  {title:"2026–2028 Small Business Planner — Goals, Tasks, Habits & Finance Tracker", cat:"Digital Planners", desc:"An all-in-one offline small business planner and live dashboard with a 2026–2028 calendar, goals, tasks, Kanban projects, habits, finance, P&L, orders, inventory, suppliers, ad ROAS, returns and analytics. Seven languages, private local data and no subscription.", price:27.99, img:"/images/products/small-business-planner-2026-2028.png", fit:"contain", video:"", buyUrl:"", url:"/planners/small-business-planner-2026-2028/", m1:"#EDE8F8", m2:"#E2ECF8"},
  {title:"Content Marketing Planner — for Fashion & E-Commerce Brands", cat:"Digital Planners", desc:"An all-in-one, offline content planner for fashion and e-commerce brands — visual calendar, sales analytics and 20 connected tools. Light & dark, 7 languages, no subscription.", price:29.99, img:"/images/products/content-marketing-planner.jpg", video:"", buyUrl:"", url:"/planners/content-marketing-planner/", m1:"#F7E4EF", m2:"#F3D9E5"},
  {title:"VendorPulse OS — Offline Supplier Management, Purchase Orders & Landed Cost", cat:"Business Operating Systems", desc:"A private supplier and purchasing OS for quotes, true landed cost, purchase orders, deliveries, quality, payables and supplier scorecards — with an evidence-based Insider Expert. 162 currencies, 7 languages, no subscription.", price:19.99, img:"/images/products/vendorpulse-os.png", video:"", buyUrl:"", url:"/planners/vendorpulse-os/", m1:"#DFF3E9", m2:"#CBE9DA"},
  {title:"Sales Management System — Offline Inventory, Orders & Profit Dashboard", cat:"Business Operating Systems", desc:"An all-in-one offline business system for sales, FIFO inventory, orders, profit and loss, expenses, invoices, ads ROAS, customers, suppliers, CRM and team management. 20+ connected modules, 7 languages, no subscription.", price:39.99, img:"/images/products/sales-management-system.png", fit:"contain", video:"", buyUrl:"", url:"/planners/sales-management-system/", m1:"#111827", m2:"#171D32"},
  {title:"RentFlow OS — Offline Equipment Rental Manager", cat:"Business Operating Systems", desc:"A private, offline manager for equipment and party rental businesses — bookings, availability, deposits, returns, maintenance and asset profitability in one browser app. No account, no subscription, works fully offline.", price:19.99, img:"/images/products/rentflow-os.jpg?v=2", video:"", buyUrl:"", url:"/planners/rentflow-os/", m1:"#DCE7E5", m2:"#CFE0DA"},
  {title:"Offline AI Business Copilot", cat:"Business Operating Systems", desc:"A private, offline business dashboard for cash flow, invoices, marketing ROAS and goals — with a built-in offline AI agent. No account, no subscription, works fully offline.", price:19.99, img:"/images/products/offline-ai-business-copilot.jpg?v=2", video:"", buyUrl:"", url:"/planners/offline-ai-business-copilot/", m1:"#EDE6D4", m2:"#DCE5D5"},
  {title:"Daily Ritual Planner", cat:"Digital Planners", desc:"A calm daily spread for priorities, rituals, and reflection.", price:12, img:"", video:"", buyUrl:"", m1:"#EDE6D4", m2:"#DCE5D5"},
  {title:"Focus & Flow Planner", cat:"Digital Planners", desc:"One page, one day. Top three priorities and a simple time block.", price:14, was:18, img:"", video:"", buyUrl:"", m1:"#F3E3CC", m2:"#EDE6D4"},
  {title:"Wellness Planner", cat:"Digital Planners", desc:"Track habits, mood, movement, and meals in one gentle place.", price:10, img:"", video:"", buyUrl:"", m1:"#DCE5D5", m2:"#EFE3CE"},
  {title:"Seasonal Planner", cat:"Digital Planners", desc:"Plan by season — goals, intentions, and a quarterly rhythm.", price:12, img:"", video:"", buyUrl:"", m1:"#EFE0D2", m2:"#E6D9BF"},
  {title:"Weekly Reset Planner", cat:"Digital Planners", desc:"A Monday-to-Sunday reset for a tidy, intentional week.", price:10, img:"", video:"", buyUrl:"", m1:"#E4D9C0", m2:"#DCE5D5"},
  {title:"Goals & Milestones Planner", cat:"Digital Planners", desc:"Break big goals into quarters, months, and simple weekly moves.", price:13, img:"", video:"", buyUrl:"", m1:"#DCE5D5", m2:"#EFE0D2"},
  {title:"Meal Plan & Grocery Planner", cat:"Digital Planners", desc:"Plan a week of meals and build your grocery list in minutes.", price:9, img:"", video:"", buyUrl:"", m1:"#EFE3CE", m2:"#E4D9C0"},
  {title:"Gratitude Journal Planner", cat:"Digital Planners", desc:"A gentle daily journal for gratitude, reflection, and calm.", price:8, img:"", video:"", buyUrl:"", m1:"#F3E3CC", m2:"#DCE5D5"}
];
var posts = [
  {tag:"Mindset", title:"5 morning rituals that set a positive tone", date:"Aug 2026 · 6 min", p1:"#EDE6D4", p2:"#DCE5D5"},
  {tag:"Planning", title:"How to choose the right digital planner for you", date:"Aug 2026 · 5 min", p1:"#F3E3CC", p2:"#EFE0D2"},
  {tag:"Lifestyle", title:"Building a week you don't need a break from", date:"Jul 2026 · 7 min", p1:"#DCE5D5", p2:"#E4D9C0"}
];
var heartSvg = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7-4.6-9.3-8.4C1 9.5 2.4 6 5.6 6c1.9 0 3.2 1.1 4.4 2.6C11.2 7.1 12.5 6 14.4 6c3.2 0 4.6 3.5 2.9 6.6C19 16.4 12 21 12 21z"/></svg>';
var sprigSvg = '<svg width="58" height="20" viewBox="0 0 58 20" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M2 18C16 18 24 10 32 2M32 2c-5 0-8 2-10 5M32 2c0 4-2 7-5 9"/></svg>';

function coverHTML(p){
  if(p.img) return '<img src="'+p.img+'" alt="'+p.title+'"'+(p.fit==='contain'?' style="object-fit:contain;object-position:center;background:#0f1726"':'')+'>';
  return '<div class="cover-mock" style="background:linear-gradient(155deg,'+p.m1+','+p.m2+')"><div class="md"></div><span class="mc">'+p.cat+'</span><span class="msprig">'+sprigSvg+'</span><div class="mt">'+p.title+'</div></div>';
}
function cardHTML(p,i){
  var price=(p.was?'<s>$'+p.was+'</s>':'')+'$'+p.price;
  var inner='<div class="pcover"><span class="heart">'+heartSvg+'</span>'+coverHTML(p)+'</div><div class="pcard-body"><h3>'+p.title+'</h3><div class="pr">'+price+'</div></div>';
  if(p.url) return '<a class="pcard" href="'+p.url+'" aria-label="'+p.title+'">'+inner+'</a>';
  return '<article class="pcard" data-cat="'+p.cat+'" data-idx="'+i+'" role="button" tabindex="0" aria-label="'+p.title+'">'+inner+'</article>';
}
function postHTML(p){
  return '<article class="post"><div class="post-media" style="background:linear-gradient(135deg,'+p.p1+','+p.p2+')"><div class="pd"></div><span class="ptag">'+p.tag+'</span></div><div class="post-body"><span class="date">'+p.date+'</span><h3>'+p.title+'</h3><a class="readmore" href="/journal/">Read article</a></div></article>';
}
function fill(id,h){var e=$(id);if(e)e.innerHTML=h;}
fill('featTrack', products.slice(0,9).map(cardHTML).join(''));
(function(){var ac=$('allCards');if(ac){var fc=ac.getAttribute('data-cat');var L=fc?products.filter(function(p){return p.cat===fc;}):products;ac.innerHTML=L.map(cardHTML).join('');}})();
fill('homePosts', posts.map(postHTML).join(''));
fill('blogPosts', posts.concat(posts).slice(0,6).map(postHTML).join(''));
function scrollTrack(id,dir){var e=$(id);if(e)e.scrollBy({left:dir*294,behavior:'smooth'});}

/* active nav by path */
(function(){var p=location.pathname;if(p.charAt(p.length-1)!=='/')p+='/';var links=document.querySelectorAll('nav.links a');for(var i=0;i<links.length;i++){var h=links[i].getAttribute('href')||'';if(h.charAt(0)==='/'&&h!=='/'&&p.indexOf(h)===0)links[i].setAttribute('aria-current','true');}})();

/* mobile menu */
var menu=$('menu'),burger=$('burger');
function closeMenu(){if(menu)menu.classList.remove('open');if(burger)burger.setAttribute('aria-expanded','false');}
if(burger)burger.addEventListener('click',function(){var o=menu.classList.toggle('open');burger.setAttribute('aria-expanded',o?'true':'false');});

/* auth (front-end UI — connect to your provider later) */
var currentUser=null;
function openAuth(t){switchAuthTab(t||'signin');$('authModal').hidden=false;document.body.style.overflow='hidden';setTimeout(function(){$('authEmail').focus();},50);}
function closeAuth(){$('authModal').hidden=true;document.body.style.overflow='';}
function switchAuthTab(t){var tabs=document.querySelectorAll('.auth-tab');for(var i=0;i<tabs.length;i++)tabs[i].classList.toggle('on',tabs[i].dataset.tab===t);var s=(t==='signup');var so=document.querySelectorAll('.signup-only');for(var j=0;j<so.length;j++)so[j].hidden=!s;$('authTitle').textContent=s?'Create your account':'Welcome back';$('authSub').textContent=s?'Save your planners and get instant downloads.':'Sign in to access your planners and downloads.';$('authSubmit').textContent=s?'Create account':'Sign in';$('authFoot').innerHTML=s?'Already have an account? <a href="#" onclick="switchAuthTab(\'signin\');return false;">Sign in</a>':'New here? <a href="#" onclick="switchAuthTab(\'signup\');return false;">Create an account</a>';}
function doAuth(){var e=($('authEmail').value||'').trim();if(!e||e.indexOf('@')<0){$('authEmail').focus();$('authEmail').style.borderColor='#B23B3B';return;}var n=($('authName').value||'').trim();var d=n||e.split('@')[0];setUser(d);closeAuth();toast('Signed in as <b>'+d+'</b>');}
function setUser(n){currentUser=n;$('signinBtn').hidden=true;$('account').hidden=false;$('avatar').textContent=(n[0]||'N').toUpperCase();$('accountName').textContent=n;$('menuSignin').hidden=true;$('menuSignout').hidden=false;}
function signOut(){currentUser=null;$('signinBtn').hidden=false;$('account').hidden=true;$('accountMenu').hidden=true;$('menuSignin').hidden=false;$('menuSignout').hidden=true;closeMenu();toast('Signed out');}
if($('accountBtn'))$('accountBtn').addEventListener('click',function(e){e.stopPropagation();var m=$('accountMenu');m.hidden=!m.hidden;$('accountBtn').setAttribute('aria-expanded',String(!m.hidden));});
document.addEventListener('click',function(e){if(!e.target.closest('.account')){var m=$('accountMenu');if(m)m.hidden=true;}});
function goDownloads(){var m=$('accountMenu');if(m)m.hidden=true;toast('Your downloads will show here once you buy a planner');return false;}

/* product modal + Lemon Squeezy checkout */
var curP=null;
function mediaHTML(p){if(p.video){return '<iframe src="'+p.video+'" title="'+p.title+' preview" allow="fullscreen" style="width:100%;height:100%;border:0;display:block;"></iframe>';}return coverHTML(p);}
function openProduct(i){var p=products[i];if(!p)return;curP=i;$('pmMedia').innerHTML=mediaHTML(p);$('pmCat').textContent=p.cat;$('pmTitle').textContent=p.title;$('pmPrice').innerHTML=(p.was?'<s>$'+p.was+'</s>':'')+'$'+p.price;$('pmDesc').textContent=p.desc;$('productModal').hidden=false;document.body.style.overflow='hidden';}
function closeProduct(){$('productModal').hidden=true;document.body.style.overflow='';}
function buyProduct(){var p=products[curP];if(p&&p.buyUrl){window.open(p.buyUrl,'_blank','noopener');}else{toast('Checkout opens as soon as this planner is published');}}
document.addEventListener('click',function(e){var c=e.target.closest('.pcard[data-idx]');if(c)openProduct(+c.dataset.idx);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeAuth();closeProduct();}if(e.key==='Enter'||e.key===' '){var c=e.target.closest('.pcard[data-idx]');if(c){e.preventDefault();openProduct(+c.dataset.idx);}}});

/* toast + forms */
var tt;function toast(m){var t=$('toast');if(!t)return;t.innerHTML=m;t.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('show');},3200);}
function subscribeNews(e){e.preventDefault();var v=($('newsEmail').value||'').trim();if(v){$('newsEmail').value='';toast('Subscribed — thanks!');}return false;}
function sendContact(e){e.preventDefault();var n=($('cName').value||'').trim(),em=($('cEmail').value||'').trim();if(!n||!em)return false;$('cName').value='';$('cEmail').value='';$('cMsg').value='';toast('Thanks '+n.split(' ')[0]+" — we'll reply within a day");return false;}

/* reveal */
function runReveal(){var els=document.querySelectorAll('.reveal:not(.seen)');for(var i=0;i<els.length;i++){if(els[i].getBoundingClientRect().top<window.innerHeight*0.92)els[i].classList.add('seen');}}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('seen');io.unobserve(en.target);}});},{threshold:0.12});var rv=document.querySelectorAll('.reveal');for(var k=0;k<rv.length;k++)io.observe(rv[k]);}
window.addEventListener('scroll',runReveal,{passive:true});
window.addEventListener('load',runReveal);
runReveal();
