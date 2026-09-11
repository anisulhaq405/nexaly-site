var $ = function(id){return document.getElementById(id);};

/* ===== PLANNERS DATA =====
   To publish a planner, fill these fields for it:
     img:    cover image path, e.g. "/images/products/daily-ritual.jpg"
     video:  YouTube EMBED url, e.g. "https://www.youtube.com/embed/VIDEOID"  (leave "" for none)
     buyUrl: Lemon Squeezy checkout link, e.g. "https://nexaly.lemonsqueezy.com/buy/xxxx"
     url:    dedicated product page, e.g. "/planners/offline-ai-business-copilot/" (card links there instead of the quick modal)
   Leave img/video/buyUrl as "" and a styled placeholder is shown until you add them. */
var products = [
  {title:"RepairBench OS — Small Engine Repair Shop Manager", cat:"Business Operating Systems", desc:"Run a small engine repair shop from one private offline system. Manage work orders, repair jobs, customers, machines, parts inventory, reorder needs, invoices, payments, profit and branded business reports with no account or subscription.", price:11.99, img:"/images/products/repairbench-os.jpg", video:"", buyUrl:"", url:"/planners/repairbench-os/", m1:"#D7E8E0", m2:"#CFE3DA"},
  {title:"AI Student Planner — Offline Study Planner, Assignment Tracker & Exam Planner", cat:"Digital Planners", desc:"Plan school or college in one private offline study system with 16 connected modules for timetables, subjects, assignments, exams, revision, goals, habits, focus sessions, notes, grades, analytics and a built-in AI assistant.", price:11.99, img:"/images/products/ai-student-planner.jpg", video:"", buyUrl:"", url:"/planners/ai-student-planner/", m1:"#E6E6FB", m2:"#DCE4F7"},
  {title:"Digital Homeschool Planner — Offline Multi-Kid Dashboard, Gradebook & Transcript", cat:"Digital Planners", desc:"Organize homeschooling for multiple children with a private offline parent dashboard, curriculum and lesson planning, calendar, assignments, gradebook, attendance and learning hours, analytics, reports, transcripts and a built-in AI assistant.", price:11.99, img:"/images/products/digital-homeschool-planner.jpg", video:"", buyUrl:"", url:"/planners/digital-homeschool-planner/", m1:"#DDE8F5", m2:"#D5E5F0"},
  {title:"ADHD Digital Planner — Focus, Tasks, Routines & Goals", cat:"Digital Planners", desc:"A calm, interactive ADHD-friendly planner for adults with 15 connected tools for daily focus, brain dumps, tasks, routines, goals, time blocks, Pomodoro sessions, habits, mood, achievements and practical analytics. Private, offline and subscription-free.", price:11.99, img:"/images/products/adhd-digital-planner.png", fit:"contain", video:"", buyUrl:"", url:"/planners/adhd-digital-planner/", m1:"#EEEAFB", m2:"#DCE8F8"},
  {title:"Boutique Business Planner — Orders, Inventory, Pricing & Profit Dashboard", cat:"Digital Planners", desc:"Manage a boutique or small product business with connected tools for products, pricing, inventory, orders, sales, customers, income, expenses, profit, marketing, goals, notes and key dates in one private browser-based planner.", price:11.99, img:"/images/products/boutique-business-planner.png", fit:"contain", video:"", buyUrl:"", url:"/planners/boutique-business-planner/", m1:"#F8E6EE", m2:"#E6F1EC"},
  {title:"2026–2028 Small Business Planner — Goals, Tasks, Habits & Finance Tracker", cat:"Digital Planners", desc:"Plan and manage a small business across 2026, 2027 and 2028 with calendars, goals, tasks, Kanban projects, habits, bills, finance, orders, inventory, suppliers, advertising ROAS, returns, profit and loss, reports and live analytics.", price:11.99, img:"/images/products/small-business-planner-2026-2028.png", fit:"contain", video:"", buyUrl:"", url:"/planners/small-business-planner-2026-2028/", m1:"#EDE8F8", m2:"#E2ECF8"},
  {title:"Caregiver Planner for Aging Parents — Family Care, Medications & Appointments", cat:"Digital Planners", desc:"Coordinate family care for aging parents with 24 connected modules for care plans, routines, medications, appointments, care teams, tasks, calendars, daily logs, expenses, transportation, emergency information, family handoffs, documents and printable reports.", price:11.99, img:"/images/products/caregiver-planner-aging-parents.png", fit:"contain", video:"", buyUrl:"", url:"/planners/caregiver-planner-aging-parents/", m1:"#E6F1EE", m2:"#E9E5F5"},
  {title:"Offline Inventory & Procurement Planner — Standalone HTML Business System", cat:"Business Operating Systems", desc:"Control inventory and procurement offline with products and SKUs, suppliers, warehouses, stock movements, adjustments, transfers, purchase requests, approvals, purchase orders, partial receiving, GRNs, low-stock alerts, reorder planning, invoices and reports.", price:11.99, img:"/images/products/inventory-procurement-planner.jpg", fit:"contain", video:"", buyUrl:"", url:"/planners/inventory-procurement-planner/", m1:"#E5EDF2", m2:"#D8E5E8"},
  {title:"OwnerOS Core: Ultimate Offline Inventory & E-Commerce Manager", cat:"Business Operating Systems", desc:"Run e-commerce operations from one private offline command center for products, inventory, orders, sales, contribution profit, marketing campaigns, ROAS, customers, suppliers, purchasing, goals, projects, tasks, decisions, SOPs and reports.", price:11.99, img:"/images/products/owneros-core.jpg", fit:"contain", video:"", buyUrl:"", url:"/planners/owneros-core/", m1:"#F1E7D9", m2:"#E9DCCB"},
  {title:"Batch & Lot Traceability Software for Small Makers | Offline Inventory, Production and Recall Manager", cat:"Business Operating Systems", desc:"Trace supplier lots through recipes, production batches, quality checks, finished inventory, customer orders and destinations. Run forward and backward traces, mock recalls, cost and yield analysis, and branded reports in a private offline system for small makers.", price:11.99, img:"/images/products/batchtrace-os.png", fit:"contain", video:"", buyUrl:"", url:"/planners/batchtrace-os/", m1:"#E8F0F4", m2:"#DDE8EC"},
  {title:"Content Marketing Planner — for Fashion & E-Commerce Brands", cat:"Digital Planners", desc:"Plan and measure content for fashion and e-commerce brands with 20 connected offline tools, including a visual calendar, Content Hub, Idea Bank, drops and campaigns, sales tracking, AI prompt library, link-in-bio planning and analytics.", price:11.99, img:"/images/products/content-marketing-planner.jpg", video:"", buyUrl:"", url:"/planners/content-marketing-planner/", m1:"#F7E4EF", m2:"#F3D9E5"},
  {title:"VendorPulse OS — Offline Supplier Management, Purchase Orders & Landed Cost", cat:"Business Operating Systems", desc:"Manage suppliers, materials, quote comparisons, true landed cost, purchase orders, deposits, partial deliveries, backorders, rejects, quality, supplier invoices, payments and scorecards in a private offline purchasing system.", price:11.99, img:"/images/products/vendorpulse-os.png", video:"", buyUrl:"", url:"/planners/vendorpulse-os/", m1:"#DFF3E9", m2:"#CBE9DA"},
  {title:"Sales Management System — Offline Inventory, Orders & Profit Dashboard", cat:"Business Operating Systems", desc:"Manage sales, FIFO inventory, orders, purchases, suppliers, returns, expenses, cash, customer balances, invoices, profit and loss, advertising ROAS, CRM, employees, payroll, commissions and tasks in one private offline business system.", price:11.99, img:"/images/products/sales-management-system.png", fit:"contain", video:"", buyUrl:"", url:"/planners/sales-management-system/", m1:"#111827", m2:"#171D32"},
  {title:"RentFlow OS — Offline Equipment Rental Manager", cat:"Business Operating Systems", desc:"Run an equipment, party or event rental business offline with booking and availability tracking, deposits, returns, maintenance schedules, double-booking risk checks, quote-to-profit workflows and asset profitability insights.", price:11.99, img:"/images/products/rentflow-os.jpg?v=2", video:"", buyUrl:"", url:"/planners/rentflow-os/", m1:"#DCE7E5", m2:"#CFE0DA"},
  {title:"Offline AI Business Copilot", cat:"Business Operating Systems", desc:"Use a private offline business dashboard to monitor sales, cash, net position, overdue invoices, marketing ROAS and CAC, a 13-week cash outlook and business goals, then create structured decision briefs with the built-in offline AI copilot.", price:11.99, img:"/images/products/offline-ai-business-copilot.jpg?v=2", video:"", buyUrl:"", url:"/planners/offline-ai-business-copilot/", m1:"#EDE6D4", m2:"#DCE5D5"}
];
var posts = [
  {"tag":"Small Business Software","title":"The Best Offline Small Business Software in 2026 (No Subscription)","date":"Sep 11, 2026 · 7 min","url":"/journal/best-offline-small-business-software/","img":"/images/products/repairbench-os/repairbench-os-owner-dashboard.jpg","alt":"offline small business software dashboard showing revenue, gross profit and a job pipeline"},
  {"tag":"Digital Planners","title":"Digital Planners That Work Offline: A 2026 Buyer's Guide","date":"Sep 11, 2026 · 6 min","url":"/journal/offline-digital-planners-guide/","img":"/images/products/ai-student-planner/ai-student-planner-dashboard-analytics.jpg","alt":"offline digital planner dashboard with study time, tasks, streaks and analytics"},
  {"tag":"No Subscription","title":"Subscription Fatigue Is Real: Why One-Time-Purchase, Offline Apps Win","date":"Sep 11, 2026 · 6 min","url":"/journal/why-one-time-purchase-offline-apps/","img":"/images/products/digital-homeschool-planner/digital-homeschool-planner-parent-command-center.jpg","alt":"offline app dashboard that works without a monthly subscription, data stored on device"},
  {
    "tag": "Inventory",
    "title": "Boutique Inventory Spreadsheet: Track Sizes, Colors and Stock",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/boutique-inventory-spreadsheet/",
    "img": "/images/products/boutique-business-planner/03_fillable-type-anywhere.png?v=journal8",
    "alt": "boutique inventory spreadsheet template for tracking sizes colors SKUs stock levels and product variants",
    "excerpt": "Build a cleaner boutique inventory spreadsheet with separate rows for sizes, colors, SKUs, available stock and reserved units."
  },
  {
    "tag": "Order Tracking",
    "title": "How to Keep Track of Small Business Orders in One Place",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/track-small-business-orders/",
    "img": "/images/products/sales-management-system/9-inventory-orders.png?v=journal8",
    "alt": "small business order tracker dashboard for payments fulfillment customer orders and delivery status",
    "excerpt": "Organize order numbers, customer details, payment status, fulfillment progress and next actions in one reliable order log."
  },
  {
    "tag": "Inventory Software",
    "title": "Inventory Software Without a Subscription: What to Check Before Buying",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/inventory-software-without-subscription/",
    "img": "/images/products/inventory-procurement-planner/01_dashboard.jpg?v=journal8",
    "alt": "inventory software without subscription dashboard for local stock control purchase orders and reorder planning",
    "excerpt": "Compare offline inventory tools, spreadsheets and paid systems before choosing subscription-free software for your shop."
  },
  {
    "tag": "Sales Tracking",
    "title": "How to Connect Sales and Inventory Tracking for a Small Shop",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/sales-inventory-tracking-small-business/",
    "img": "/images/products/sales-management-system/8-dashboard-closeup.png?v=journal8",
    "alt": "sales and inventory tracking for small business dashboard showing orders stock profit and customer records",
    "excerpt": "Connect sales, stock movements, returns, payments and customer records so every fulfilled order updates the right business data."
  },
  {
    "tag": "Content Calendar",
    "title": "A 30-Day Content Calendar for a Clothing Brand",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/content-calendar-clothing-brand/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-visual-content-calendar.jpg?v=journal8",
    "alt": "30 day content calendar for clothing brand with weekly product posts reels campaigns and sales content plan",
    "excerpt": "Plan a month of product posts, reels, customer questions, selling angles and campaign content for a clothing brand."
  },
  {
    "tag": "Social Content",
    "title": "30 Boutique Social Media Post Ideas With Clear Sales CTAs",
    "date": "Sep 8, 2026 · 6 min",
    "url": "/journal/boutique-social-media-post-ideas/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-content-hub.jpg?v=journal8",
    "alt": "boutique social media post ideas content hub for product posts styling posts trust posts and sales CTAs",
    "excerpt": "Use practical boutique post ideas that answer buyer questions, show product details and guide shoppers toward the next step."
  },
  {
    "tag": "Marketing Plan",
    "title": "Black Friday Marketing Plan for a Small Clothing Business",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/black-friday-marketing-plan-small-business/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-analytics-what-sells.jpg?v=journal8",
    "alt": "Black Friday marketing plan for small clothing business with campaign calendar content analytics and sales tracking",
    "excerpt": "Prepare offer rules, stock checks, content phases, checkout tests and fulfillment routines before Black Friday traffic arrives."
  },
  {
    "tag": "Homeschool Schedule",
    "title": "Homeschool Schedule for Multiple Ages: Three Flexible Examples",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-schedule-multiple-ages/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-lesson-planner-calendar.jpg?v=journal8",
    "alt": "homeschool schedule for multiple ages with lesson calendar shared family blocks and individual child planning",
    "excerpt": "Create shared learning blocks, individual lesson rotations and flexible family schedules for multiple ages at home."
  },
  {
    "tag": "Attendance Tracker",
    "title": "Homeschool Attendance Tracker: A Simple Daily Record",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-attendance-tracker/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-reports-transcript.jpg?v=journal8",
    "alt": "homeschool attendance tracker for daily records child attendance reports and printable homeschool documentation",
    "excerpt": "Keep clear daily attendance records for each child, review duplicate entries and understand what your totals actually show."
  },
  {
    "tag": "Homeschool Planner",
    "title": "Choosing a Homeschool Planner for Multiple Children",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-planner-multiple-children/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-multiple-child-profiles.jpg?v=journal8",
    "alt": "homeschool planner for multiple children with separate child profiles lessons gradebook attendance and family schedule",
    "excerpt": "Choose a planner that shows the family day while keeping each child’s lessons, progress and records separate."
  },
  {
    "tag": "Student Planner",
    "title": "Assignment Tracker for College Students: Set Up Your Semester",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/college-assignment-tracker/",
    "img": "/images/products/ai-student-planner/ai-student-planner-plan-track-stay-ahead.jpg?v=journal8",
    "alt": "college assignment tracker for semester deadlines coursework priorities study tasks and student planning dashboard",
    "excerpt": "Turn assignment deadlines into start dates, weekly priorities, status updates and next actions for a clearer semester plan."
  },
  {
    "tag": "Study Schedule",
    "title": "Exam Study Schedule Template: Plan the Weeks Before Finals",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/exam-study-schedule-template/",
    "img": "/images/products/ai-student-planner/ai-student-planner-learning-os-dashboard.jpg?v=journal8",
    "alt": "exam study schedule template for finals revision practice sessions study blocks and student planner dashboard",
    "excerpt": "Plan study sessions, practice checks, revision blocks and recovery days before finals without filling a calendar with vague study time."
  }
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
  var media = p.img ? '<img src="'+p.img+'" alt="'+(p.alt||p.title)+'" loading="lazy" decoding="async">' : '<div class="pd"></div><span class="ptag">'+p.tag+'</span>';
  var href = p.url || '/journal/';
  return '<a class="pcard journal-card" href="'+href+'" aria-label="'+p.title+'"><div class="pcover">'+media+'</div><div class="pcard-body"><h3>'+p.title+'</h3><div class="pr" style="font-family:Inter,system-ui,sans-serif;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--terra)">'+p.tag+'</div><p style="font-size:13px;color:var(--faint);line-height:1.55;margin:8px 0 0">'+(p.excerpt||'')+'</p><div style="font-size:12px;color:var(--faint);margin-top:9px">'+p.date+'</div></div></a>';
}
function fill(id,h){var e=$(id);if(e)e.innerHTML=h;}
fill('featTrack', products.slice(0,15).map(cardHTML).join(''));
(function(){var ac=$('allCards');if(ac){var fc=ac.getAttribute('data-cat');var L=fc?products.filter(function(p){return p.cat===fc;}):products;ac.innerHTML=L.map(cardHTML).join('');}})();
fill('homePosts', posts.slice(0,3).map(postHTML).join(''));
fill('blogPosts', posts.map(postHTML).join(''));
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

/* ===== NexalyPlanner AI Assistant (auto-injected, appears on every page) ===== */
/* ============================================================
   NexalyPlanner AI Assistant  (auto · multilingual · human)
   - Appears on every page (loaded via main.js)
   - Reads the LIVE products[] and posts[] arrays, so it always
     knows new products/blogs with zero manual feeding.
   - Talks to a free Cloudflare Worker (set WORKER_URL below).
   - If the Worker isn't set yet, it still helps in "local" mode.
   ============================================================ */
(function () {
  if (window.__nexlyAI) return; window.__nexlyAI = 1;

  /* ---------- 1) CONFIG — paste your Worker URL after setup ---------- */
  var WORKER_URL = "PASTE-YOUR-CLOUDFLARE-WORKER-URL-HERE"; // e.g. https://nexaly-ai.yourname.workers.dev
  var CFG = {
    title: "Nexaly Assistant",
    subtitle: "Here to help — ask me anything",
    accent: "#c06a3f",
    dark: "#2c2117",
    greeting: "Hi! 👋 I'm the Nexaly assistant. I can help you find the right planner or business app, explain how they work, or answer any question. What are you looking for today?"
  };

  /* ---------- 2) Static company knowledge (rarely changes) ---------- */
  var KNOWLEDGE =
    "About NexalyPlanner (nexalyplanner.com): an online store selling two kinds of digital products — (1) Digital Planners and (2) Business Operating Systems. " +
    "Every product is an interactive HTML app you open in your web browser. Key facts true for all products: works fully OFFLINE; ONE-TIME purchase (no monthly subscription); your data stays PRIVATE on your own device (no account/login needed); INSTANT digital download (a ZIP with the app + a quick-start guide + license); many support 7 languages including Arabic and light & dark mode; you can print or export reports (PDF/CSV, some to Word/Excel) and save your own backups. " +
    "To buy: open a product's page and click the Buy button. Nothing is shipped (digital only). " +
    "Helpful pages: all products /planners/, Digital Planners /planners/digital-planners/, Business Operating Systems /planners/business-operating-systems/, FAQ /faq/, Refund policy /refund/, Contact /contact/, Journal (guides) /journal/.";

  /* ---------- 3) Live catalogue from the site's own data ---------- */
  function catalogue() {
    var out = "CURRENT PRODUCTS (auto-updated from the live site):\n";
    try {
      (window.products || (typeof products !== "undefined" ? products : [])).forEach(function (p) {
        if (p && p.url) out += "• " + p.title + " — category: " + (p.cat || "") + " — $" + p.price +
          " — " + (p.desc || "") + " — https://nexalyplanner.com" + p.url + "\n";
      });
    } catch (e) {}
    out += "\nGUIDES / BLOG:\n";
    try {
      (window.posts || (typeof posts !== "undefined" ? posts : [])).forEach(function (p) {
        var t = p.title || ""; var u = p.url || "";
        if (t) out += "• " + t + " — https://nexalyplanner.com" + u + "\n";
      });
    } catch (e) {}
    return out;
  }

  /* ---------- 4) Local fallback (works with no Worker) ---------- */
  function prods() { try { return (window.products || (typeof products !== "undefined" ? products : [])).filter(function (p) { return p && p.url; }); } catch (e) { return []; } }
  function localAnswer(q) {
    q = (q || "").toLowerCase();
    if (/^(hi|hello|hey|salam|assalam|hola|bonjour)\b/.test(q)) return CFG.greeting;
    var faq = [
      [/subscri|monthly|recurring/, "Great news — there are no subscriptions. Every product is a one-time purchase you keep forever. 🙂"],
      [/offline|internet|wifi/, "Yes! All our products work fully offline in your browser. Once downloaded, you don't need the internet, and your data stays on your device."],
      [/refund|return|money back/, "You can read our refund policy here: https://nexalyplanner.com/refund/ . Since everything is an instant digital download, please check it before buying."],
      [/download|install|how do i get|after (i )?(buy|pay)/, "After you buy, you get an instant download — a ZIP file with the app plus a quick-start guide. Just unzip and open the HTML file in your browser. No installation needed."],
      [/language|arabic|spanish|french/, "Many of our products support 7 languages (including Arabic, with right-to-left support) and light & dark mode."],
      [/price|cost|how much/, "Prices vary by product (a one-time payment). Tell me what you need and I'll share the exact price and a link."],
      [/private|data|secure|safe/, "Your data stays private on your own device — there's no account and nothing is uploaded to a cloud."],
      [/contact|support|email|help/, "You can reach the team here: https://nexalyplanner.com/contact/ . I'm happy to help right now too!"]
    ];
    for (var i = 0; i < faq.length; i++) if (faq[i][0].test(q)) return faq[i][1];
    // product search
    var words = q.split(/[^a-z0-9]+/).filter(function (w) { return w.length > 2; });
    var hits = prods().map(function (p) {
      var hay = (p.title + " " + p.cat + " " + (p.desc || "")).toLowerCase(); var s = 0;
      words.forEach(function (w) { if (hay.indexOf(w) > -1) s++; });
      return { p: p, s: s };
    }).filter(function (x) { return x.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 3);
    if (hits.length) {
      var r = "Here are a few that might fit:\n";
      hits.forEach(function (h) { r += "\n• **" + h.p.title + "** — $" + h.p.price + "\n  https://nexalyplanner.com" + h.p.url; });
      r += "\n\nWant more detail on any of these?";
      return r;
    }
    return "I can help you find the right digital planner or business app. You can browse everything here: https://nexalyplanner.com/planners/ — or tell me what you're trying to do (e.g. \"homeschool\", \"repair shop\", \"student\", \"inventory\") and I'll point you to the best one.";
  }

  /* ---------- 5) Ask the AI (Worker) with local fallback ---------- */
  var history = []; // {role, content}
  function ask(userText, cb) {
    history.push({ role: "user", content: userText });
    var configured = WORKER_URL && WORKER_URL.indexOf("PASTE-") === -1;
    if (!configured) { var a = localAnswer(userText); history.push({ role: "assistant", content: a }); cb(a); return; }
    fetch(WORKER_URL, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: history.slice(-12), catalogue: KNOWLEDGE + "\n\n" + catalogue() })
    }).then(function (r) { return r.json(); }).then(function (d) {
      var a = (d && d.reply) ? d.reply : localAnswer(userText);
      history.push({ role: "assistant", content: a }); cb(a);
    }).catch(function () { var a = localAnswer(userText); history.push({ role: "assistant", content: a }); cb(a); });
  }

  /* ---------- 6) UI ---------- */
  var css = "" +
    ".nx-btn{position:fixed;right:20px;bottom:20px;width:60px;height:60px;border-radius:50%;background:" + CFG.accent + ";color:#fff;border:0;cursor:pointer;box-shadow:0 10px 30px -8px rgba(44,33,23,.5);z-index:99998;display:flex;align-items:center;justify-content:center}" +
    ".nx-btn svg{width:28px;height:28px}" +
    ".nx-panel{position:fixed;right:20px;bottom:92px;width:370px;max-width:calc(100vw - 32px);height:560px;max-height:calc(100vh - 120px);background:#fff;border:1px solid #e6ddc9;border-radius:18px;box-shadow:0 24px 60px -18px rgba(44,33,23,.45);z-index:99999;display:none;flex-direction:column;overflow:hidden;font-family:'Inter',system-ui,sans-serif}" +
    ".nx-panel.on{display:flex}" +
    ".nx-head{background:" + CFG.dark + ";color:#fff;padding:14px 16px}" +
    ".nx-head b{font-family:'Fraunces',serif;font-size:1.05rem;display:block}" +
    ".nx-head small{opacity:.8;font-size:.8rem}" +
    ".nx-head .nx-x{position:absolute;top:12px;right:14px;background:none;border:0;color:#fff;font-size:1.3rem;cursor:pointer;opacity:.85}" +
    ".nx-msgs{flex:1;overflow-y:auto;padding:16px;background:#fbf6ec;display:flex;flex-direction:column;gap:10px}" +
    ".nx-m{max-width:85%;padding:10px 13px;border-radius:14px;font-size:.92rem;line-height:1.5;white-space:pre-wrap;word-wrap:break-word}" +
    ".nx-m a{color:" + CFG.accent + ";font-weight:600}" +
    ".nx-bot{background:#fff;border:1px solid #ece3d0;color:#2c2117;align-self:flex-start;border-bottom-left-radius:4px}" +
    ".nx-user{background:" + CFG.accent + ";color:#fff;align-self:flex-end;border-bottom-right-radius:4px}" +
    ".nx-typing{align-self:flex-start;color:#8a7a5f;font-size:.85rem;padding:4px 6px}" +
    ".nx-in{display:flex;gap:8px;padding:12px;border-top:1px solid #eee;background:#fff}" +
    ".nx-in input{flex:1;border:1px solid #e0d6c0;border-radius:10px;padding:11px 12px;font-size:.92rem;outline:none;font-family:inherit}" +
    ".nx-in button{background:" + CFG.accent + ";color:#fff;border:0;border-radius:10px;padding:0 15px;cursor:pointer;font-weight:600}" +
    ".nx-foot{font-size:.68rem;color:#b3a versa;text-align:center;color:#a99;padding:0 0 8px;background:#fff}";
  var st = document.createElement("style"); st.textContent = css.replace('#b3a versa','#a99'); document.head.appendChild(st);

  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function fmt(s) {
    s = esc(s);
    s = s.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>");
    s = s.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
    return s;
  }

  var btn = el("button", "nx-btn");
  btn.setAttribute("aria-label", "Chat with Nexaly Assistant");
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.5 8.5 0 0 1 21 11.5z"/></svg>';
  var panel = el("div", "nx-panel");
  panel.innerHTML =
    '<div class="nx-head" style="position:relative"><b>' + CFG.title + '</b><small>' + CFG.subtitle + '</small><button class="nx-x" aria-label="Close">&times;</button></div>' +
    '<div class="nx-msgs" id="nxMsgs"></div>' +
    '<div class="nx-foot">Nexaly Assistant · answers may occasionally be imperfect</div>' +
    '<div class="nx-in"><input id="nxIn" type="text" placeholder="Type your message…" autocomplete="off"><button id="nxSend">Send</button></div>';
  document.body.appendChild(btn); document.body.appendChild(panel);

  var msgs = panel.querySelector("#nxMsgs");
  function add(text, who) { var m = el("div", "nx-m " + (who === "user" ? "nx-user" : "nx-bot"), fmt(text)); msgs.appendChild(m); msgs.scrollTop = msgs.scrollHeight; return m; }
  var greeted = false;
  function openP() { panel.classList.add("on"); if (!greeted) { greeted = true; add(CFG.greeting, "bot"); } panel.querySelector("#nxIn").focus(); }
  function closeP() { panel.classList.remove("on"); }
  btn.addEventListener("click", function () { panel.classList.contains("on") ? closeP() : openP(); });
  panel.querySelector(".nx-x").addEventListener("click", closeP);

  function send() {
    var inp = panel.querySelector("#nxIn"); var t = inp.value.trim(); if (!t) return;
    inp.value = ""; add(t, "user");
    var typing = el("div", "nx-typing", "typing…"); msgs.appendChild(typing); msgs.scrollTop = msgs.scrollHeight;
    ask(t, function (reply) { typing.remove(); add(reply, "bot"); });
  }
  panel.querySelector("#nxSend").addEventListener("click", send);
  panel.querySelector("#nxIn").addEventListener("keydown", function (e) { if (e.key === "Enter") send(); });
})();

