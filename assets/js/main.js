var $ = function(id){return document.getElementById(id);};

/* ===== PLANNERS DATA =====
   To publish a planner, fill these fields for it:
     img:    cover image path, e.g. "/images/products/daily-ritual.jpg"
     video:  YouTube EMBED url, e.g. "https://www.youtube.com/embed/VIDEOID"  (leave "" for none)
     buyUrl: Lemon Squeezy checkout link, e.g. "https://nexaly.lemonsqueezy.com/buy/xxxx"
     url:    dedicated product page, e.g. "/planners/offline-ai-business-copilot/" (card links there instead of the quick modal)
   Leave img/video/buyUrl as "" and a styled placeholder is shown until you add them. */
var products = [
  {
    "title": "RepairBench OS — Small Engine Repair Shop Manager",
    "cat": "Business Operating Systems",
    "desc": "Run a small engine repair shop from one private offline system. Manage work orders, repair jobs, customers, machines, parts inventory, reorder needs, invoices, payments, profit and branded business reports with no account or subscription.",
    "price": 11.99,
    "img": "/images/products/repairbench-os.jpg",
    "video": "",
    "buyUrl": "",
    "url": "/planners/repairbench-os/",
    "m1": "#D7E8E0",
    "m2": "#CFE3DA"
  },
  {
    "title": "AI Student Planner — Offline Study Planner, Assignment Tracker & Exam Planner",
    "cat": "Digital Planners",
    "desc": "Plan school or college in one private offline study system with 16 connected modules for timetables, subjects, assignments, exams, revision, goals, habits, focus sessions, notes, grades, analytics and a built-in AI assistant.",
    "price": 11.99,
    "img": "/images/products/ai-student-planner.jpg",
    "video": "",
    "buyUrl": "",
    "url": "/planners/ai-student-planner/",
    "m1": "#E6E6FB",
    "m2": "#DCE4F7"
  },
  {
    "title": "Digital Homeschool Planner — Offline Multi-Kid Dashboard, Gradebook & Transcript",
    "cat": "Digital Planners",
    "desc": "Organize homeschooling for multiple children with a private offline parent dashboard, curriculum and lesson planning, calendar, assignments, gradebook, attendance and learning hours, analytics, reports, transcripts and a built-in AI assistant.",
    "price": 11.99,
    "img": "/images/products/digital-homeschool-planner.jpg",
    "video": "",
    "buyUrl": "",
    "url": "/planners/digital-homeschool-planner/",
    "m1": "#DDE8F5",
    "m2": "#D5E5F0"
  },
  {
    "title": "ADHD Digital Planner — Focus, Tasks, Routines & Goals",
    "cat": "Digital Planners",
    "desc": "A calm, interactive ADHD-friendly planner for adults with 15 connected tools for daily focus, brain dumps, tasks, routines, goals, time blocks, Pomodoro sessions, habits, mood, achievements and practical analytics. Private, offline and subscription-free.",
    "price": 11.99,
    "img": "/images/products/adhd-digital-planner.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/adhd-digital-planner/",
    "m1": "#EEEAFB",
    "m2": "#DCE8F8"
  },
  {
    "title": "Boutique Business Planner — Orders, Inventory, Pricing & Profit Dashboard",
    "cat": "Digital Planners",
    "desc": "Manage a boutique or small product business with connected tools for products, pricing, inventory, orders, sales, customers, income, expenses, profit, marketing, goals, notes and key dates in one private browser-based planner.",
    "price": 11.99,
    "img": "/images/products/boutique-business-planner.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/boutique-business-planner/",
    "m1": "#F8E6EE",
    "m2": "#E6F1EC"
  },
  {
    "title": "2026–2028 Small Business Planner — Goals, Tasks, Habits & Finance Tracker",
    "cat": "Digital Planners",
    "desc": "Plan and manage a small business across 2026, 2027 and 2028 with calendars, goals, tasks, Kanban projects, habits, bills, finance, orders, inventory, suppliers, advertising ROAS, returns, profit and loss, reports and live analytics.",
    "price": 11.99,
    "img": "/images/products/small-business-planner-2026-2028.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/small-business-planner-2026-2028/",
    "m1": "#EDE8F8",
    "m2": "#E2ECF8"
  },
  {
    "title": "Caregiver Planner for Aging Parents — Family Care, Medications & Appointments",
    "cat": "Digital Planners",
    "desc": "Coordinate family care for aging parents with 24 connected modules for care plans, routines, medications, appointments, care teams, tasks, calendars, daily logs, expenses, transportation, emergency information, family handoffs, documents and printable reports.",
    "price": 11.99,
    "img": "/images/products/caregiver-planner-aging-parents.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/caregiver-planner-aging-parents/",
    "m1": "#E6F1EE",
    "m2": "#E9E5F5"
  },
  {
    "title": "Offline Inventory & Procurement Planner — Standalone HTML Business System",
    "cat": "Business Operating Systems",
    "desc": "Control inventory and procurement offline with products and SKUs, suppliers, warehouses, stock movements, adjustments, transfers, purchase requests, approvals, purchase orders, partial receiving, GRNs, low-stock alerts, reorder planning, invoices and reports.",
    "price": 11.99,
    "img": "/images/products/inventory-procurement-planner.jpg",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/inventory-procurement-planner/",
    "m1": "#E5EDF2",
    "m2": "#D8E5E8"
  },
  {
    "title": "OwnerOS Core: Ultimate Offline Inventory & E-Commerce Manager",
    "cat": "Business Operating Systems",
    "desc": "Run e-commerce operations from one private offline command center for products, inventory, orders, sales, contribution profit, marketing campaigns, ROAS, customers, suppliers, purchasing, goals, projects, tasks, decisions, SOPs and reports.",
    "price": 11.99,
    "img": "/images/products/owneros-core.jpg",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/owneros-core/",
    "m1": "#F1E7D9",
    "m2": "#E9DCCB"
  },
  {
    "title": "Batch & Lot Traceability Software for Small Makers | Offline Inventory, Production and Recall Manager",
    "cat": "Business Operating Systems",
    "desc": "Trace supplier lots through recipes, production batches, quality checks, finished inventory, customer orders and destinations. Run forward and backward traces, mock recalls, cost and yield analysis, and branded reports in a private offline system for small makers.",
    "price": 11.99,
    "img": "/images/products/batchtrace-os.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/batchtrace-os/",
    "m1": "#E8F0F4",
    "m2": "#DDE8EC"
  },
  {
    "title": "Content Marketing Planner — for Fashion & E-Commerce Brands",
    "cat": "Digital Planners",
    "desc": "Plan and measure content for fashion and e-commerce brands with 20 connected offline tools, including a visual calendar, Content Hub, Idea Bank, drops and campaigns, sales tracking, AI prompt library, link-in-bio planning and analytics.",
    "price": 11.99,
    "img": "/images/products/content-marketing-planner.jpg",
    "video": "",
    "buyUrl": "",
    "url": "/planners/content-marketing-planner/",
    "m1": "#F7E4EF",
    "m2": "#F3D9E5"
  },
  {
    "title": "VendorPulse OS — Offline Supplier Management, Purchase Orders & Landed Cost",
    "cat": "Business Operating Systems",
    "desc": "Manage suppliers, materials, quote comparisons, true landed cost, purchase orders, deposits, partial deliveries, backorders, rejects, quality, supplier invoices, payments and scorecards in a private offline purchasing system.",
    "price": 11.99,
    "img": "/images/products/vendorpulse-os.png",
    "video": "",
    "buyUrl": "",
    "url": "/planners/vendorpulse-os/",
    "m1": "#DFF3E9",
    "m2": "#CBE9DA"
  },
  {
    "title": "Sales Management System — Offline Inventory, Orders & Profit Dashboard",
    "cat": "Business Operating Systems",
    "desc": "Manage sales, FIFO inventory, orders, purchases, suppliers, returns, expenses, cash, customer balances, invoices, profit and loss, advertising ROAS, CRM, employees, payroll, commissions and tasks in one private offline business system.",
    "price": 11.99,
    "img": "/images/products/sales-management-system.png",
    "fit": "contain",
    "video": "",
    "buyUrl": "",
    "url": "/planners/sales-management-system/",
    "m1": "#111827",
    "m2": "#171D32"
  },
  {
    "title": "RentFlow OS — Offline Equipment Rental Manager",
    "cat": "Business Operating Systems",
    "desc": "Run an equipment, party or event rental business offline with booking and availability tracking, deposits, returns, maintenance schedules, double-booking risk checks, quote-to-profit workflows and asset profitability insights.",
    "price": 11.99,
    "img": "/images/products/rentflow-os.jpg?v=2",
    "video": "",
    "buyUrl": "",
    "url": "/planners/rentflow-os/",
    "m1": "#DCE7E5",
    "m2": "#CFE0DA"
  },
  {
    "title": "Offline AI Business Copilot",
    "cat": "Business Operating Systems",
    "desc": "Use a private offline business dashboard to monitor sales, cash, net position, overdue invoices, marketing ROAS and CAC, a 13-week cash outlook and business goals, then create structured decision briefs with the built-in offline AI copilot.",
    "price": 11.99,
    "img": "/images/products/offline-ai-business-copilot.jpg?v=2",
    "video": "",
    "buyUrl": "",
    "url": "/planners/offline-ai-business-copilot/",
    "m1": "#EDE6D4",
    "m2": "#DCE5D5"
  }
];
var posts = [
  {
    "url": "/journal/best-digital-planner-for-ipad/",
    "title": "Best Digital Planner for iPad: Full Breakdown",
    "excerpt": "Compare iPad digital planner formats, including Goodnotes PDFs, Notion, offline HTML, and free options, with a practical setup example.",
    "img": "/images/journal/best-digital-planner-for-ipad-20260919.jpg",
    "alt": "iPad beside an Apple Pencil showing a digital planner with monthly, weekly, and daily layouts",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/best-planner-app-for-ipad-2026/",
    "title": "Best Planner App for iPad in 2026: Formats Compared",
    "excerpt": "Compare Goodnotes PDF planners, Notion, offline HTML apps, and iPad tools to choose a planner that fits your routine.",
    "img": "/images/journal/best-planner-app-for-ipad-2026-20260919.jpg",
    "alt": "iPad displaying a weekly digital planner beside an Apple Pencil and handwritten planning notes",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/digital-planner-app-how-it-works/",
    "title": "Digital Planner App: How It Works and Best Options",
    "excerpt": "Compare PDF, Goodnotes, Notion, iPad, and offline HTML planner options. Learn how digital planners work and choose a practical setup.",
    "img": "/images/journal/digital-planner-app-how-it-works-20260919.jpg",
    "alt": "iPad showing a weekly digital planner beside a laptop with a typed planning workspace",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/digital-planner-for-ipad-setup/",
    "title": "Digital Planner for iPad: Setup Guide and Free Options",
    "excerpt": "Set up a digital planner for iPad with PDF, Goodnotes, Notion, or offline HTML options. Compare formats and test a free setup.",
    "img": "/images/journal/digital-planner-for-ipad-setup-20260919.jpg",
    "alt": "iPad showing a linked digital planner weekly layout beside an Apple Pencil and Files app",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/free-digital-planner-for-ipad/",
    "title": "Free Digital Planner for iPad: Where to Actually Get One",
    "excerpt": "Find a free digital planner for iPad and choose between PDF, Goodnotes, Notion, and offline HTML with practical setup and backup tips.",
    "img": "/images/journal/free-digital-planner-for-ipad-20260919.jpg",
    "alt": "iPad showing a handwritten weekly digital planner beside an Apple Pencil",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/ipad-digital-planner-setup-guide/",
    "title": "iPad Digital Planner: Complete Setup Guide",
    "excerpt": "Set up an iPad digital planner with PDF, Goodnotes, Notion, or offline HTML. Learn what you need, how to work offline, and how to back up files.",
    "img": "/images/journal/ipad-digital-planner-setup-guide-20260919.jpg",
    "alt": "iPad with Apple Pencil beside a digital weekly planner, Files folder, and notes for an offline setup",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/ipad-planner-app-buying-guide/",
    "title": "iPad Planner App: What to Look For Before You Buy",
    "excerpt": "Compare iPad planner apps, PDF planners, Goodnotes, Notion, and offline HTML options before you buy.",
    "img": "/images/journal/ipad-planner-app-buying-guide-20260919.jpg",
    "alt": "iPad showing a digital planner comparison with Apple Pencil, PDF, Goodnotes, Notion, and offline HTML options",
    "tag": "Planning Guides",
    "date": "Sep 23, 2026"
  },
  {
    "url": "/journal/2026-monthly-planner-free-layouts/",
    "title": "2026 Monthly Planner: Free Layouts and Where to Get One",
    "excerpt": "Find a 2026 monthly planner layout, compare free and paid formats, and learn how to set up a realistic month with a worked example.",
    "img": "/images/journal/2026-monthly-planner-free-layouts-20260918.jpg",
    "alt": "Open 2026 monthly planner showing a dated calendar grid, priorities, deadlines, and notes on a desk",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/best-2026-planners-digital-printable-options/",
    "title": "Best 2026 Planners: Digital and Printable Options",
    "excerpt": "Compare the best 2026 planner formats, including digital, printable, paper, daily, weekly, and monthly options for US readers.",
    "img": "/images/journal/best-2026-planners-digital-printable-options-20260918.jpg",
    "alt": "2026 digital and printable planner options arranged on a desk with monthly, weekly, and daily layouts",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/daily-planner-2026-free-layouts/",
    "title": "Daily Planner 2026: Free Layouts and Practical Picks",
    "excerpt": "Compare practical daily planner 2026 layouts, formats, and setup steps with a realistic worked example for US readers.",
    "img": "/images/journal/daily-planner-2026-free-layouts-20260918.jpg",
    "alt": "Open 2026 daily planner showing priorities, time blocks, appointments, and notes beside a tablet",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/monthly-planner-2026-best-layouts/",
    "title": "Monthly Planner 2026: Best Layouts to Use",
    "excerpt": "Compare the best monthly planner 2026 layouts, see a worked March example, and choose a calendar, dashboard, or two-page format.",
    "img": "/images/journal/monthly-planner-2026-best-layouts-20260918.jpg",
    "alt": "Open monthly planner 2026 showing a calendar grid, priorities, and notes for a realistic March planning example",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/planner-2026-what-to-look-for/",
    "title": "Planner 2026: What to Look For Before You Buy",
    "excerpt": "Choosing a planner 2026? Compare paper, PDF, digital, and app formats, then check layouts, dates, compatibility, and backup before buying.",
    "img": "/images/journal/planner-2026-what-to-look-for-20260918.jpg",
    "alt": "Open 2026 planner beside a tablet and handwritten weekly schedule",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/planners-2026-full-comparison/",
    "title": "Planners 2026: Full Comparison for Work, Study, and Life",
    "excerpt": "Compare planners 2026 formats for work, study, and life. Choose daily, weekly, monthly, paper, printable, or digital layouts.",
    "img": "/images/journal/planners-2026-full-comparison-20260918.jpg",
    "alt": "Open 2026 planner with monthly, weekly, and daily planning pages for work, study, and home life",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/weekly-planner-2026-free-templates/",
    "title": "Weekly Planner 2026: Free Templates That Are Easy to Use",
    "excerpt": "Build a practical weekly planner for 2026 with simple free layouts, a worked January example, format comparisons, and setup tips.",
    "img": "/images/journal/weekly-planner-2026-free-templates-20260918.jpg",
    "alt": "Open 2026 weekly planner showing priorities, appointments, daily tasks, and a short weekly review",
    "tag": "Planning Guides",
    "date": "Sep 22, 2026"
  },
  {
    "url": "/journal/a5-planner-sizes-layouts-digital-options/",
    "title": "A5 Planner: Sizes, Layouts and Best Digital Options",
    "excerpt": "Compare A5 planner dimensions, paper, printable PDF, offline HTML, GoodNotes, and Notion options to choose a practical layout for daily use.",
    "img": "/images/journal/a5-planner-sizes-layouts-digital-options-20260918.jpg",
    "alt": "Open A5 planner showing a weekly layout beside a tablet with a digital planner page",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/daily-digital-planner/",
    "title": "Daily Digital Planner: How It Works and Setup Guide",
    "excerpt": "Learn what a daily digital planner is, compare PDF, offline HTML, and cloud options, then set one up and back it up securely every day.",
    "img": "/images/journal/daily-digital-planner-20260918.jpg",
    "alt": "Open daily digital planner showing priorities, time blocks, notes, and a completed day",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/daily-planner-complete-guide/",
    "title": "Daily Planner: The Complete Guide to Planning Your Day",
    "excerpt": "Learn how to plan your day with three priorities, fixed commitments, realistic time blocks, useful buffers, and a short end-of-day review.",
    "img": "/images/journal/daily-planner-complete-guide-20260918.jpg",
    "alt": "Open daily planner with three priorities, fixed appointments, time blocks, and an end-of-day review",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/day-planner-vs-daily-planner/",
    "title": "Day Planner vs Daily Planner: What Is the Difference?",
    "excerpt": "Day planner or daily planner? Learn the real difference, compare calendars, hourly layouts, PDFs, offline HTML, and apps, and choose your fit.",
    "img": "/images/journal/day-planner-vs-daily-planner-20260918.jpg",
    "alt": "Open day planner beside a calendar with hourly schedule blocks and a digital tablet planner",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/hourly-planner-best-free-digital-layouts/",
    "title": "Hourly Planner: Paper, Printable and Digital Layouts",
    "excerpt": "Compare paper, printable PDF, offline HTML, and cloud hourly planners. See a realistic workday example and choose a simple daily layout that fits.",
    "img": "/images/journal/hourly-planner-best-free-digital-layouts-20260918.jpg",
    "alt": "Open hourly planner showing time blocks, priorities, and buffer space on a desk",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/monthly-planner-free-templates/",
    "title": "Monthly Planner: How to Set Up a Practical Monthly Layout",
    "excerpt": "Learn how to set up a practical monthly planner for commitments, goals, projects, dated actions, and an effective end-of-month review.",
    "img": "/images/journal/monthly-planner-free-templates-20260918.jpg",
    "alt": "Open monthly planner with commitments, goals, project milestones, and review notes arranged across one calendar spread.",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/minimalist-planner/",
    "title": "Minimalist Planner: Why Less Structure Works Better",
    "excerpt": "Learn how a minimalist planner works, who benefits, what to include, and how to set up a simple paper, PDF, offline, or digital planner layout.",
    "img": "/images/journal/minimalist-planner-20260918.jpg",
    "alt": "Open minimalist planner with three priorities, a short schedule, and a notes area on a clean desk",
    "tag": "Planning Guides",
    "date": "Updated Sep 21, 2026"
  },
  {
    "url": "/journal/adhd-planner-for-adults/",
    "title": "ADHD Planner for Adults: Build a System You Can Reuse",
    "excerpt": "Choose an ADHD planner for adults and set up a reusable daily system for task capture, time blocks, focus sessions, resets and weekly reviews.",
    "img": "/images/journal/adhd-planner-for-adults-20260915.jpg",
    "alt": "Adult using a short visual daily plan, capture inbox and focus timer under the heading ADHD Planner That Sticks",
    "tag": "Planning Guides",
    "date": "Sep 15, 2026"
  },
  {
    "url": "/journal/business-planner-weekly-review/",
    "title": "Business Planner for Small Business: What to Track Each Week",
    "excerpt": "Use a business planner to review sales, cash, orders, marketing and next actions each week, with a practical dashboard and worked small-business example.",
    "img": "/images/journal/business-planner-weekly-review-20260915.jpg",
    "alt": "Small-business owner reviewing goals, orders, weekly sales, cash and next actions under the heading Plan the Business Week",
    "tag": "Planning Guides",
    "date": "Sep 15, 2026"
  },
  {
    "url": "/journal/student-planner-guide/",
    "title": "Student Planner Guide: Organize Classes, Assignments and Exams",
    "excerpt": "Build a student planner that connects classes, assignments, exams and study sessions. Includes a semester setup, weekly routine and worked example.",
    "img": "/images/journal/student-planner-guide-20260915.jpg",
    "alt": "College student organizing classes, assignments, exams and focus sessions under the heading Build a Student Planner",
    "tag": "Planning Guides",
    "date": "Sep 15, 2026"
  },
  {
    "url": "/journal/supplier-quote-comparison/",
    "title": "Supplier Quote Comparison Template: Compare Total Costs",
    "excerpt": "Compare supplier quotes using a practical table, landed-cost example, accepted-unit costs, delivery dates and payment terms before you place an order.",
    "img": "/images/journal/supplier-quote-comparison-20260915.jpg",
    "alt": "Three supplier quote folders beside a parcel and calculator, with the heading Compare Supplier Quotes",
    "tag": "Planning Guides",
    "date": "Sep 15, 2026"
  },
  {
    "url": "/journal/reorder-point-small-business/",
    "title": "Reorder Point Calculation for Small Business: Worked Examples",
    "excerpt": "Calculate reorder points with daily demand, lead time and safety stock. Worked SKU examples explain open orders, case packs and weekly inventory reviews.",
    "img": "/images/journal/reorder-point-20260915.jpg",
    "alt": "Organized stockroom with parcels, a low-stock shelf marker and the heading When to Reorder",
    "tag": "Planning Guides",
    "date": "Sep 14, 2026"
  },
  {
    "tag": "Small Business Software",
    "title": "The Best Offline Small Business Software in 2026 (No Subscription)",
    "date": "Sep 11, 2026 · 7 min",
    "url": "/journal/best-offline-small-business-software/",
    "img": "/images/products/repairbench-os/repairbench-os-owner-dashboard.jpg",
    "alt": "offline small business software dashboard showing revenue, gross profit and a job pipeline",
    "excerpt": "Looking for small business software that works offline with no monthly subscription? Here is how one-time-purchase, offline apps work and what to check before you buy."
  },
  {
    "tag": "Digital Planners",
    "title": "Digital Planners That Work Offline: A 2026 Buyer's Guide",
    "date": "Sep 11, 2026 · 6 min",
    "url": "/journal/offline-digital-planners-guide/",
    "img": "/images/products/ai-student-planner/ai-student-planner-dashboard-analytics.jpg",
    "alt": "offline digital planner dashboard with study time, tasks, streaks and analytics",
    "excerpt": "A practical guide to offline digital planners — how browser-based, one-time-purchase planners work, who they suit, and how to choose the right one for you."
  },
  {
    "tag": "No Subscription",
    "title": "Subscription Fatigue Is Real: Why One-Time-Purchase, Offline Apps Win",
    "date": "Sep 11, 2026 · 6 min",
    "url": "/journal/why-one-time-purchase-offline-apps/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-parent-command-center.jpg",
    "alt": "offline app dashboard that works without a monthly subscription, data stored on device",
    "excerpt": "Tired of monthly software fees? Here is the case for one-time-purchase, offline apps — lower cost over time, real data ownership, and no lock-in."
  },
  {
    "tag": "Inventory",
    "title": "Boutique Inventory Spreadsheet: Track Sizes, Colors and Stock",
    "date": "Updated Sep 15, 2026 · 5 min",
    "url": "/journal/boutique-inventory-spreadsheet/",
    "img": "/images/journal/boutique-stock-20260915.jpg",
    "alt": "Tagged boutique clothing and folded knitwear with the heading Know Your Stock: Every Size, Every Color",
    "excerpt": "Build a boutique inventory spreadsheet with variant SKUs, stock formulas, reservations, returns and a worked clothing-store example."
  },
  {
    "tag": "Order Tracking",
    "title": "How to Keep Track of Small Business Orders in One Place",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/track-small-business-orders/",
    "img": "/images/products/sales-management-system/9-inventory-orders.png",
    "alt": "How to Keep Track of Small Business Orders in One Place",
    "excerpt": "Organize small-business orders with a free tracker. Separate payments, partial shipments and next actions so every confirmed order has a clear record."
  },
  {
    "tag": "Inventory Software",
    "title": "Inventory Software Without a Subscription: What to Check Before Buying",
    "date": "Updated Sep 14, 2026 · 5 min",
    "url": "/journal/inventory-software-without-subscription/",
    "img": "/images/journal/inventory-software-buying-checklist.png",
    "alt": "Inventory software buying checklist covering sale and return tests, backup recovery and license costs",
    "excerpt": "Considering inventory software without a subscription? Use this buying checklist to compare licenses, offline workflows, backups, returns and data exports."
  },
  {
    "tag": "Sales Tracking",
    "title": "How to Connect Sales and Inventory Tracking for a Small Shop",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/sales-inventory-tracking-small-business/",
    "img": "/images/products/sales-management-system/8-dashboard-closeup.png",
    "alt": "How to Connect Sales and Inventory Tracking for a Small Shop",
    "excerpt": "See how one small-shop sale connects order amounts, payments and stock. Download a worked example with formulas for fulfilled units and merchandise costs."
  },
  {
    "tag": "Content Calendar",
    "title": "A 30-Day Content Calendar for a Clothing Brand",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/content-calendar-clothing-brand/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-visual-content-calendar.jpg",
    "alt": "A 30-Day Content Calendar for a Clothing Brand",
    "excerpt": "Plan clothing-brand content with a free 30-day calendar. Get product-detail ideas, formats, clear CTAs and a practical routine for reviewing results."
  },
  {
    "tag": "Social Content",
    "title": "30 Boutique Social Media Post Ideas With Clear Sales CTAs",
    "date": "Sep 8, 2026 · 6 min",
    "url": "/journal/boutique-social-media-post-ideas/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-content-hub.jpg",
    "alt": "30 Boutique Social Media Post Ideas With Clear Sales CTAs",
    "excerpt": "Explore 30 boutique social media post ideas with hooks, visuals and CTAs. Download an editable idea bank for product details, styling, offers and questions."
  },
  {
    "tag": "Marketing Plan",
    "title": "Black Friday Marketing Plan for a Small Clothing Business",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/black-friday-marketing-plan-small-business/",
    "img": "/images/products/content-marketing-planner/content-marketing-planner-analytics-what-sells.jpg",
    "alt": "Black Friday Marketing Plan for a Small Clothing Business",
    "excerpt": "Build a 2026 Black Friday marketing plan for your small clothing business. Use a free workback checklist for content, stock, offer terms and checkout tests."
  },
  {
    "tag": "Homeschool Schedule",
    "title": "Homeschool Schedule for Multiple Ages: Three Flexible Examples",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-schedule-multiple-ages/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-lesson-planner-calendar.jpg",
    "alt": "Homeschool Schedule for Multiple Ages: Three Flexible Examples",
    "excerpt": "Plan a homeschool day for multiple ages with three flexible examples. Download schedules for shared activities, individual lessons and split-day routines."
  },
  {
    "tag": "Attendance Tracker",
    "title": "Homeschool Attendance Tracker: A Simple Daily Record",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-attendance-tracker/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-reports-transcript.jpg",
    "alt": "Homeschool Attendance Tracker: A Simple Daily Record",
    "excerpt": "Download a free homeschool attendance tracker. Keep separate daily records for each child, review duplicate entries and understand what the totals mean."
  },
  {
    "tag": "Homeschool Planner",
    "title": "Choosing a Homeschool Planner for Multiple Children",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/homeschool-planner-multiple-children/",
    "img": "/images/products/digital-homeschool-planner/digital-homeschool-planner-multiple-child-profiles.jpg",
    "alt": "Choosing a Homeschool Planner for Multiple Children",
    "excerpt": "Choose a homeschool planner for multiple children with a practical checklist. Compare shared schedules, separate records, rescheduling, exports and backups."
  },
  {
    "tag": "Student Planner",
    "title": "Assignment Tracker for College Students: Set Up Your Semester",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/college-assignment-tracker/",
    "img": "/images/products/ai-student-planner/ai-student-planner-plan-track-stay-ahead.jpg",
    "alt": "Assignment Tracker for College Students: Set Up Your Semester",
    "excerpt": "Organize college assignments with a free tracker. Record due dates, next actions and planned work, then use editable flags to review approaching deadlines."
  },
  {
    "tag": "Study Schedule",
    "title": "Exam Study Schedule Template: Plan the Weeks Before Finals",
    "date": "Sep 8, 2026 · 5 min",
    "url": "/journal/exam-study-schedule-template/",
    "img": "/images/journal/exam-prep-20260915.jpg",
    "alt": "Study desk with a planning notebook, textbooks and a clock under the heading Plan Your Exam Prep",
    "excerpt": "Download an exam study schedule template with an editable ten-day plan. Organize practice, review, flexible time and exam logistics before finals."
  },
  {
    "url": "/journal/how-to-run-a-one-person-business-with-ai/",
    "title": "How to run a one-person business with AI",
    "excerpt": "A practical guide to running a one-person business with AI: which work to hand off, which to keep, the tools that replace early hires, and the operations gap most solo founders miss.",
    "img": "/images/journal/one-person-business-ai-concept.jpg",
    "alt": "A solo business owner at a laptop with conceptual AI panels for research, writing, support and business records",
    "tag": "Planning Guides",
    "date": "Updated Sep 15, 2026"
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

/* product modal + secure checkout */
var curP=null;
function mediaHTML(p){if(p.video){return '<iframe src="'+p.video+'" title="'+p.title+' preview" allow="fullscreen" style="width:100%;height:100%;border:0;display:block;"></iframe>';}return coverHTML(p);}
function openProduct(i){var p=products[i];if(!p)return;curP=i;$('pmMedia').innerHTML=mediaHTML(p);$('pmCat').textContent=p.cat;$('pmTitle').textContent=p.title;$('pmPrice').innerHTML=(p.was?'<s>$'+p.was+'</s>':'')+'$'+p.price;$('pmDesc').textContent=p.desc;$('productModal').hidden=false;document.body.style.overflow='hidden';}
function closeProduct(){$('productModal').hidden=true;document.body.style.overflow='';}
function buyProduct(){var p=products[curP];if(p&&p.buyUrl){window.open(p.buyUrl,'_blank','noopener');}else{toast('Checkout opens as soon as this planner is published');}}

/* Header search + secure checkout launcher */
(function(){
  var checkoutByPath={
    '/planners/adhd-digital-planner/':'https://buy.polar.sh/polar_cl_le5cjYcPCBuMbje2Eol7ZrFw3kMLefDdiUVZF2lTFMS',
    '/planners/ai-student-planner/':'https://buy.polar.sh/polar_cl_l7wGLhCXODsUhcv88BY7IjI2IMouNPW4BUOdh0tfTRa',
    '/planners/batchtrace-os/':'https://buy.polar.sh/polar_cl_SplQ4BnMTDwB1YoZE5UNT7qYzQLB3Fkby3mqP3YQEMY',
    '/planners/boutique-business-planner/':'https://buy.polar.sh/polar_cl_CO8mXt7Ab8aYM2kccXirUTI4a1BWzGcF6TbFx2uw9OB',
    '/planners/caregiver-planner-aging-parents/':'https://buy.polar.sh/polar_cl_y97hHWsumJWw3ZWyAxJKfJsZtqIbhb3M3mZun3T5foJ',
    '/planners/content-marketing-planner/':'https://buy.polar.sh/polar_cl_56lsbzVx9DQaqUBAot4fNVuZRcNsHffSAhN8Y4EEEsg',
    '/planners/digital-homeschool-planner/':'https://buy.polar.sh/polar_cl_LMGTbcHUEl1VcR6tgXW7mr4pTknyjfrwekSXN01sVUV',
    '/planners/inventory-procurement-planner/':'https://buy.polar.sh/polar_cl_tMPiPWta5R773BRHnqicjiJaUBONiBoKPS7DD1KZ5dX',
    '/planners/offline-ai-business-copilot/':'https://buy.polar.sh/polar_cl_xqL0Mx8Vxk2IiMH9tENfft5QH6tZ4CQFLEPed24slVT',
    '/planners/owneros-core/':'https://buy.polar.sh/polar_cl_zNIc2hrZIsCWw83NWUZ7bWqEtlz9FMcsnXNxm1Np7Ub',
    '/planners/rentflow-os/':'https://buy.polar.sh/polar_cl_dPrYOPFXv04wbfBZDQ1gvEuwKQynkQicGRh091I6m6k',
    '/planners/repairbench-os/':'https://buy.polar.sh/polar_cl_LDfhqo384rYgSE1QMxqnNVTvf9jqYVQqYfUiL4Yx0Ps',
    '/planners/sales-management-system/':'https://buy.polar.sh/polar_cl_Mceh5y8KTYDhF2t5A1mLySmps5evEe1BRIecN2aE0dz',
    '/planners/small-business-planner-2026-2028/':'https://buy.polar.sh/polar_cl_7WUb0TgGBCv1JRqUwYsiuJZfyKS8US7dKJrhW4DXoKF',
    '/planners/vendorpulse-os/':'https://buy.polar.sh/polar_cl_MBJG9jLafpaZRIxWPco8gJKVNvcAyCwPJOBdI0eIqrG'
  };
  var escHtml=function(s){return String(s||'').replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});};
  var modal=document.createElement('div');
  modal.className='nx-util';modal.hidden=true;
  modal.innerHTML='<div class="nx-util-bg"></div><section class="nx-util-card" role="dialog" aria-modal="true" aria-labelledby="nxUtilTitle"><button class="nx-util-x" type="button" aria-label="Close">&times;</button><div id="nxUtilBody"></div></section>';
  document.body.appendChild(modal);
  var style=document.createElement('style');
  style.textContent='.nx-util{position:fixed;inset:0;z-index:220;display:grid;place-items:start center;padding:9vh 20px 28px}.nx-util[hidden]{display:none}.nx-util-bg{position:absolute;inset:0;background:rgba(2,12,27,.7);backdrop-filter:blur(5px)}.nx-util-card{position:relative;width:min(720px,100%);max-height:82vh;overflow:auto;background:#fff;border:1px solid #dce5f0;border-radius:20px;box-shadow:0 36px 90px rgba(2,12,27,.32);padding:30px}.nx-util-x{position:absolute;right:14px;top:12px;width:38px;height:38px;border:1px solid #dce5f0;border-radius:50%;background:#fff;color:#52627a;font-size:25px;cursor:pointer}.nx-util h2{font-family:Inter,system-ui,sans-serif;margin:0 44px 8px;color:#0b1f3a;font-weight:800}.nx-util-lead{margin:0 0 20px;color:#52627a}.nx-search-input{width:100%;padding:14px 16px;border:1.5px solid #c7d4e4;border-radius:11px;font:inherit;outline:none}.nx-search-input:focus{border-color:#60a5fa;box-shadow:0 0 0 4px rgba(37,99,235,.11)}.nx-util-list{display:grid;gap:10px;margin-top:16px}.nx-util-item{display:flex;align-items:center;gap:14px;padding:13px;border:1px solid #dce5f0;border-radius:12px;background:#f8fafc}.nx-util-item img{width:56px;height:56px;border-radius:9px;object-fit:cover;background:#eaf0f7}.nx-util-copy{min-width:0;flex:1}.nx-util-copy b{display:block;color:#10213a;line-height:1.3}.nx-util-copy small{display:block;color:#64748b;margin-top:4px}.nx-util-go{display:inline-flex;align-items:center;justify-content:center;padding:10px 14px;border-radius:9px;background:#2563eb;color:#fff;font-weight:700;font-size:13px;white-space:nowrap}.nx-util-empty{padding:24px;text-align:center;color:#64748b}.nx-util-note{margin-top:18px;padding:12px 14px;border-radius:10px;background:#eff6ff;color:#334155;font-size:13px}@media(max-width:600px){.nx-util{padding:5vh 12px 20px}.nx-util-card{padding:24px 16px}.nx-util-item{align-items:flex-start;flex-wrap:wrap}.nx-util-go{width:100%}}';
  document.head.appendChild(style);
  var body=modal.querySelector('#nxUtilBody'),lastFocus=null;
  function closeUtil(){modal.hidden=true;document.body.style.overflow='';if(lastFocus)lastFocus.focus();}
  function openUtil(){lastFocus=document.activeElement;modal.hidden=false;document.body.style.overflow='hidden';}
  modal.querySelector('.nx-util-bg').addEventListener('click',closeUtil);modal.querySelector('.nx-util-x').addEventListener('click',closeUtil);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!modal.hidden)closeUtil();});
  function productForPath(path){for(var i=0;i<products.length;i++)if(products[i].url===path)return products[i];return null;}
  function searchRows(q){
    q=(q||'').toLowerCase().trim();if(!q)return [];
    var words=q.split(/\s+/).filter(Boolean),rows=[];
    products.forEach(function(p){var hay=(p.title+' '+p.cat+' '+(p.desc||'')).toLowerCase(),score=0;words.forEach(function(w){if(hay.indexOf(w)>-1)score++;});if(score)rows.push({title:p.title,meta:p.cat+' · $'+Number(p.price).toFixed(2),url:p.url,img:p.img,score:score+2});});
    posts.forEach(function(p){var hay=(p.title+' '+(p.excerpt||'')+' '+(p.tag||'')).toLowerCase(),score=0;words.forEach(function(w){if(hay.indexOf(w)>-1)score++;});if(score)rows.push({title:p.title,meta:(p.tag||'Journal')+' · '+(p.date||''),url:p.url,img:p.img,score:score});});
    return rows.sort(function(a,b){return b.score-a.score;}).slice(0,10);
  }
  function renderSearch(q){var rows=searchRows(q),list=body.querySelector('.nx-util-list');if(!list)return;list.innerHTML=rows.length?rows.map(function(r){return '<div class="nx-util-item"><img src="'+escHtml(r.img)+'" alt=""><div class="nx-util-copy"><b>'+escHtml(r.title)+'</b><small>'+escHtml(r.meta)+'</small></div><a class="nx-util-go" href="'+escHtml(r.url)+'">View</a></div>';}).join(''):'<div class="nx-util-empty">'+(q?'No matching products or guides found.':'Start typing to search products and guides.')+'</div>';}
  function openSearch(){body.innerHTML='<h2 id="nxUtilTitle">Search NexalyPlanner</h2><p class="nx-util-lead">Find products, business systems and practical guides.</p><input class="nx-search-input" type="search" aria-label="Search products and guides" placeholder="Try “inventory”, “student” or “homeschool”"><div class="nx-util-list"><div class="nx-util-empty">Start typing to search products and guides.</div></div>';openUtil();var input=body.querySelector('input');input.addEventListener('input',function(){renderSearch(input.value);});input.focus();}
  function checkoutRows(){var current=productForPath(location.pathname),list=current?[current]:products.filter(function(p){return checkoutByPath[p.url];});return list.map(function(p){return '<div class="nx-util-item"><img src="'+escHtml(p.img)+'" alt=""><div class="nx-util-copy"><b>'+escHtml(p.title)+'</b><small>One-time purchase · $'+Number(p.price).toFixed(2)+'</small></div><a class="nx-util-go" href="'+checkoutByPath[p.url]+'" target="_blank" rel="noopener">Checkout</a></div>';}).join('');}
  function openCheckout(){var current=productForPath(location.pathname);body.innerHTML='<h2 id="nxUtilTitle">Secure checkout</h2><p class="nx-util-lead">'+(current?'Continue with this product on Polar secure checkout.':'Choose a product to continue to Polar secure checkout.')+'</p><div class="nx-util-list">'+checkoutRows()+'</div><div class="nx-util-note">Digital download · one-time payment · no subscription</div>';openUtil();}
  function wire(){document.querySelectorAll('button[aria-label="Search"]').forEach(function(b){b.removeAttribute('onclick');b.addEventListener('click',openSearch);});document.querySelectorAll('button[aria-label="Cart"]').forEach(function(b){b.removeAttribute('onclick');b.setAttribute('aria-label','Cart and checkout');b.addEventListener('click',openCheckout);var badge=b.querySelector('.cart-badge');if(badge)badge.textContent=productForPath(location.pathname)?'1':'0';});}
  wire();window.openSiteSearch=openSearch;window.openSiteCheckout=openCheckout;
})();
document.addEventListener('click',function(e){var c=e.target.closest('.pcard[data-idx]');if(c)openProduct(+c.dataset.idx);});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeProduct();if(e.key==='Enter'||e.key===' '){var c=e.target.closest('.pcard[data-idx]');if(c){e.preventDefault();openProduct(+c.dataset.idx);}}});

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
