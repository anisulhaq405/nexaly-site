(function(root){'use strict';
const api=typeof module!=='undefined'&&module.exports?require('./small-tools-models.js'):root.NexalySmallTools;
const configs=[
  {
    "slug": "cash-flow-variance-report",
    "kind": "variance",
    "name": "Cash Flow Variance Report",
    "category": "cashflow",
    "theme": "workflow-variance",
    "color": "#175c67",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "period",
        "label": "Period covered",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "forecastOpening",
        "label": "Forecast opening cash",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "actualOpening",
        "label": "Actual opening cash",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      }
    ],
    "rowFields": [
      {
        "key": "label",
        "label": "Cash movement",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "direction",
        "label": "Direction",
        "type": "select",
        "options": [
          "Receipt",
          "Payment"
        ]
      },
      {
        "key": "forecast",
        "label": "Forecast amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "actual",
        "label": "Actual amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "cause",
        "label": "Reason to investigate",
        "type": "select",
        "options": [
          "Timing",
          "Amount",
          "Unclassified"
        ]
      },
      {
        "key": "owner",
        "label": "Follow-up owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "review",
        "label": "Follow-up date",
        "type": "date"
      },
      {
        "key": "action",
        "label": "Evidence and next action",
        "type": "textarea",
        "maxLength": 600,
        "optional": true
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Cash Flow Variance Report",
        "currency": "USD",
        "period": "One completed week",
        "forecastOpening": "1000",
        "actualOpening": "1000"
      },
      "rows": [
        {
          "label": "Customer collection",
          "direction": "Receipt",
          "forecast": "1500",
          "actual": "1200",
          "cause": "Timing",
          "owner": "Owner",
          "review": "2026-10-16",
          "action": "Confirm whether the remaining 300 is still collectible."
        },
        {
          "label": "Supplier payment",
          "direction": "Payment",
          "forecast": "800",
          "actual": "900",
          "cause": "Amount",
          "owner": "Owner",
          "review": "2026-10-16",
          "action": "Compare the final invoice with the quote."
        }
      ]
    },
    "reportNote": "Forecast closing = forecast opening + forecast receipts \u2212 forecast payments. Actual closing uses actual cash. Cash impact is actual minus forecast for receipts and forecast minus actual for payments. Reasons are entered manually; this is not a statutory cash flow statement.",
    "maxRows": 100
  },
  {
    "slug": "monthly-business-budget-variance",
    "kind": "budget",
    "name": "Monthly Business Budget Variance",
    "category": "cashflow",
    "theme": "workflow-budget",
    "color": "#6a401e",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "period",
        "label": "Budget month",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "rowFields": [
      {
        "key": "label",
        "label": "Budget line",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "type",
        "label": "Line type",
        "type": "select",
        "options": [
          "Revenue",
          "Variable cost",
          "Fixed cost"
        ]
      },
      {
        "key": "budget",
        "label": "Budget amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "actual",
        "label": "Actual amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "owner",
        "label": "Review owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "review",
        "label": "Review date",
        "type": "date"
      },
      {
        "key": "action",
        "label": "Explanation and next action",
        "type": "textarea",
        "maxLength": 600,
        "optional": true
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Monthly Business Budget Variance",
        "currency": "USD",
        "period": "October 2026"
      },
      "rows": [
        {
          "label": "Sales",
          "type": "Revenue",
          "budget": "10000",
          "actual": "9000",
          "owner": "Owner",
          "review": "2026-11-02",
          "action": "Check orders and average order value separately."
        },
        {
          "label": "Direct costs",
          "type": "Variable cost",
          "budget": "4000",
          "actual": "3800",
          "owner": "Owner",
          "review": "2026-11-02",
          "action": "Lower total cost does not establish lower unit cost."
        },
        {
          "label": "Overhead",
          "type": "Fixed cost",
          "budget": "3000",
          "actual": "3200",
          "owner": "Owner",
          "review": "2026-11-02",
          "action": "Identify the additional 200 before renewing spending."
        }
      ]
    },
    "reportNote": "Amount variance = actual \u2212 budget. Percentage variance = amount variance \u00f7 budget \u00d7 100, undefined for a zero budget. Modeled operating remainder = revenue \u2212 variable costs \u2212 fixed costs. Cash dates, tax, financing and inventory valuation are outside this worksheet.",
    "maxRows": 100
  },
  {
    "slug": "printable-planner-builder",
    "kind": "builder",
    "name": "Printable Planner Builder",
    "category": "personal",
    "theme": "workflow-builder",
    "color": "#714075",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "paper",
        "label": "Paper size",
        "type": "select",
        "options": [
          "US Letter",
          "A4",
          "A5"
        ]
      },
      {
        "key": "layout",
        "label": "Layout",
        "type": "select",
        "options": [
          "Daily",
          "Weekly"
        ]
      },
      {
        "key": "start",
        "label": "Date on daily page / date within week",
        "type": "date"
      },
      {
        "key": "weekStart",
        "label": "Week starts on",
        "type": "select",
        "options": [
          "Monday",
          "Sunday"
        ]
      },
      {
        "key": "startHour",
        "label": "Daily start hour (0\u201323)",
        "type": "number",
        "min": 0,
        "max": 23,
        "step": "1",
        "integer": true
      },
      {
        "key": "endHour",
        "label": "Daily end hour (0\u201323)",
        "type": "number",
        "min": 0,
        "max": 23,
        "step": "1",
        "integer": true
      }
    ],
    "rowFields": [
      {
        "key": "section",
        "label": "Writing section name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "lines",
        "label": "Writing lines",
        "type": "number",
        "min": 0,
        "max": 6,
        "step": "1",
        "integer": true
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Printable Planner Builder",
        "paper": "US Letter",
        "layout": "Daily",
        "start": "2026-10-13",
        "weekStart": "Monday",
        "startHour": "8",
        "endHour": "18"
      },
      "rows": [
        {
          "section": "Three priorities",
          "lines": "3"
        },
        {
          "section": "Next actions",
          "lines": "3"
        },
        {
          "section": "Notes",
          "lines": "3"
        }
      ]
    },
    "reportNote": "Builds one undated-style daily or dated weekly printable page. Daily ranges may cross midnight and are limited to 16 hourly slots; start and end must differ. Use one to three writing sections, one to six lines each, at most 12 lines overall. Browser PDF printing is not a GoodNotes file or reminder app.",
    "maxRows": 3
  },
  {
    "slug": "monthly-teacher-lesson-planner",
    "kind": "teacher",
    "name": "Monthly Teacher Lesson Planner",
    "category": "homeschool",
    "theme": "workflow-teacher",
    "color": "#335548",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "month",
        "label": "Teaching month (YYYY-MM)",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Preparation review date",
        "type": "date"
      }
    ],
    "rowFields": [
      {
        "key": "lesson",
        "label": "Lesson / group",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "date",
        "label": "Lesson date",
        "type": "date"
      },
      {
        "key": "prep",
        "label": "Preparation due date",
        "type": "date"
      },
      {
        "key": "owner",
        "label": "Preparation owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "materials",
        "label": "Materials / preparation task",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      },
      {
        "key": "status",
        "label": "Preparation status",
        "type": "select",
        "options": [
          "Not started",
          "In progress",
          "Ready"
        ]
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Monthly Teacher Lesson Planner",
        "month": "2026-10",
        "asOf": "2026-10-13"
      },
      "rows": [
        {
          "lesson": "Grade 4 fractions",
          "date": "2026-10-16",
          "prep": "2026-10-12",
          "owner": "Teacher",
          "materials": "Print fraction strips and check the worked example.",
          "status": "In progress"
        },
        {
          "lesson": "Grade 4 number review",
          "date": "2026-10-19",
          "prep": "2026-10-16",
          "owner": "Teacher",
          "materials": "Prepare three practice questions.",
          "status": "Ready"
        }
      ]
    },
    "reportNote": "Lists only lessons in the entered month. Preparation due date must be on or before the lesson date; earlier-month preparation is allowed. Overdue means prep date before review date and status not Ready. No curriculum approval, attendance compliance or reminders are provided.",
    "maxRows": 100
  },
  {
    "slug": "content-production-capacity-planner",
    "kind": "production",
    "name": "Content Production Capacity Planner",
    "category": "content",
    "theme": "workflow-production",
    "color": "#1d4d84",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "objective",
        "label": "One content objective",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "start",
        "label": "First production day",
        "type": "date"
      },
      {
        "key": "end",
        "label": "Last production day",
        "type": "date"
      },
      {
        "key": "daily",
        "label": "Production hours available each working day",
        "type": "number",
        "min": 0,
        "max": 24,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "days",
        "label": "Working days",
        "type": "select",
        "options": [
          "Weekdays",
          "Every day"
        ]
      }
    ],
    "rowFields": [
      {
        "key": "item",
        "label": "Deliverable",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "date",
        "label": "Production day",
        "type": "date"
      },
      {
        "key": "hours",
        "label": "Production and review hours",
        "type": "number",
        "min": 0,
        "max": 24,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "owner",
        "label": "Production owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "reviewer",
        "label": "Review owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "status",
        "label": "Status",
        "type": "select",
        "options": [
          "Planned",
          "In progress",
          "Complete"
        ]
      },
      {
        "key": "action",
        "label": "Destination / next action",
        "type": "textarea",
        "maxLength": 600,
        "optional": true
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Content Production Capacity Planner",
        "objective": "Explain one product and publish two useful demonstrations",
        "start": "2026-10-13",
        "end": "2026-10-16",
        "daily": "3",
        "days": "Weekdays"
      },
      "rows": [
        {
          "item": "Product explanation",
          "date": "2026-10-13",
          "hours": "2",
          "owner": "Writer",
          "reviewer": "Editor",
          "status": "Planned",
          "action": "Link to the relevant product page."
        },
        {
          "item": "Short demonstration",
          "date": "2026-10-13",
          "hours": "2",
          "owner": "Creator",
          "reviewer": "Editor",
          "status": "In progress",
          "action": "Check the demonstration before posting."
        }
      ]
    },
    "reportNote": "Remaining planned load includes Planned and In progress hours, excludes Complete items, and groups by production date. It does not spread work automatically or publish content. Allocate a multi-day deliverable as separate dated work blocks. Completed hours remain visible for recordkeeping.",
    "maxRows": 100
  },
  {
    "slug": "marketing-campaign-budget-planner",
    "kind": "campaign",
    "name": "Marketing Campaign Budget Planner",
    "category": "content",
    "theme": "workflow-campaign",
    "color": "#7c342d",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "objective",
        "label": "One campaign objective",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "ceiling",
        "label": "Total test budget",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "review",
        "label": "Next review date",
        "type": "date"
      }
    ],
    "rowFields": [
      {
        "key": "channel",
        "label": "Channel / test",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "planned",
        "label": "Planned spend",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "actual",
        "label": "Actual spend",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "inquiries",
        "label": "Observed inquiries",
        "type": "number",
        "min": 0,
        "max": 100000,
        "step": "1",
        "integer": true
      },
      {
        "key": "customers",
        "label": "Confirmed customers",
        "type": "number",
        "min": 0,
        "max": 100000,
        "step": "1",
        "integer": true
      },
      {
        "key": "rule",
        "label": "Decision rule / attribution note",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Marketing Campaign Budget Planner",
        "currency": "USD",
        "objective": "Test one service offer with attributable inquiries",
        "ceiling": "600",
        "review": "2026-10-30"
      },
      "rows": [
        {
          "channel": "Email test",
          "planned": "200",
          "actual": "180",
          "inquiries": "12",
          "customers": "3",
          "rule": "Use a distinct inquiry tag; check lead quality."
        },
        {
          "channel": "Search test",
          "planned": "300",
          "actual": "320",
          "inquiries": "8",
          "customers": "1",
          "rule": "Review actual inquiries before allocating the unassigned budget."
        }
      ]
    },
    "reportNote": "Unallocated planned budget = ceiling \u2212 planned spend. Remaining actual budget = ceiling \u2212 actual spend. Cost per inquiry/customer uses actual spend divided by that entered count, undefined at zero. Channel counts may overlap; no automatic attribution, ROI or sales forecast is inferred.",
    "maxRows": 100
  },
  {
    "slug": "one-page-business-plan-builder",
    "kind": "lean",
    "name": "One-Page Business Plan Builder",
    "category": "agency",
    "theme": "workflow-lean",
    "color": "#4c496d",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "customer",
        "label": "Specific customer",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "problem",
        "label": "Problem and existing workaround",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      },
      {
        "key": "offer",
        "label": "Offer and service boundary",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      },
      {
        "key": "economics",
        "label": "Revenue and cost assumptions",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      },
      {
        "key": "review",
        "label": "Plan review date",
        "type": "date"
      }
    ],
    "rowFields": [
      {
        "key": "assumption",
        "label": "Assumption to test",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "evidence",
        "label": "Evidence observed",
        "type": "textarea",
        "maxLength": 600,
        "optional": true
      },
      {
        "key": "test",
        "label": "Next test",
        "type": "textarea",
        "maxLength": 600,
        "optional": false
      },
      {
        "key": "owner",
        "label": "Test owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "due",
        "label": "Test due date",
        "type": "date"
      },
      {
        "key": "status",
        "label": "Evidence status",
        "type": "select",
        "options": [
          "Untested",
          "Supported",
          "Contradicted"
        ]
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: One-Page Business Plan Builder",
        "customer": "Local service businesses launching a website",
        "problem": "Owners lose time assembling a clear landing-page brief.",
        "offer": "One landing-page design with two revision rounds; development excluded.",
        "economics": "Illustrative package 1250; 20 delivery hours; verify actual demand and cost.",
        "review": "2026-11-13"
      },
      "rows": [
        {
          "assumption": "A prospect will pay 1250 for this package",
          "evidence": "Three conversations; no paid sale yet.",
          "test": "Offer one paid pilot with written scope.",
          "owner": "Owner",
          "due": "2026-10-23",
          "status": "Untested"
        },
        {
          "assumption": "Delivery fits in 20 hours",
          "evidence": "No completed pilot time log.",
          "test": "Track the pilot delivery and revision hours.",
          "owner": "Designer",
          "due": "2026-11-06",
          "status": "Untested"
        }
      ]
    },
    "reportNote": "Prints the core customer, problem, offer and economics with an evidence log. A one-page summary is compact with up to three short assumptions; additional or long entries can require more pages. Supported is a user-entered status, not independent proof. This is not a funding application.",
    "maxRows": 20
  },
  {
    "slug": "service-business-financial-projections",
    "kind": "projections",
    "name": "Service Business Financial Projections",
    "category": "cashflow",
    "theme": "workflow-projections",
    "color": "#234b59",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "opening",
        "label": "Opening cash",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      }
    ],
    "rowFields": [
      {
        "key": "month",
        "label": "Month starting (first day)",
        "type": "date"
      },
      {
        "key": "sales",
        "label": "Billed service revenue",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "expense",
        "label": "Operating expense incurred",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "depreciation",
        "label": "Noncash depreciation",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "receipts",
        "label": "Cash collected",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "paid",
        "label": "Operating cash paid",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "principal",
        "label": "Debt principal paid",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "funding",
        "label": "New loan / owner capital received",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "draw",
        "label": "Owner cash withdrawal",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Service Business Financial Projections",
        "currency": "USD",
        "opening": "2000"
      },
      "rows": [
        {
          "month": "2026-10-01",
          "sales": "6000",
          "expense": "4000",
          "depreciation": "200",
          "receipts": "5000",
          "paid": "4200",
          "principal": "300",
          "funding": "0",
          "draw": "1000"
        },
        {
          "month": "2026-11-01",
          "sales": "6500",
          "expense": "4200",
          "depreciation": "200",
          "receipts": "6000",
          "paid": "4000",
          "principal": "300",
          "funding": "0",
          "draw": "1000"
        }
      ]
    },
    "reportNote": "Operating result = billed service revenue \u2212 incurred operating expenses \u2212 noncash depreciation. Closing cash = prior cash + collections + new funding \u2212 operating cash paid \u2212 debt principal \u2212 owner withdrawals. Months must be consecutive and start on day 1. Excludes inventory, tax, a balance sheet and loan approval; include applicable interest within operating expense and cash-paid inputs.",
    "maxRows": 12
  },
  {
    "slug": "coffee-shop-daily-operating-plan",
    "kind": "coffee",
    "name": "Coffee Shop Daily Operating Plan",
    "category": "operations",
    "theme": "workflow-coffee",
    "color": "#75492e",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "hours",
        "label": "Opening hours",
        "type": "number",
        "min": 0,
        "max": 24,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "capacity",
        "label": "Maximum feasible orders per hour",
        "type": "number",
        "min": 0,
        "max": 10000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "orders",
        "label": "Expected daily orders",
        "type": "number",
        "min": 0,
        "max": 100000,
        "step": "1",
        "integer": true
      },
      {
        "key": "ticket",
        "label": "Average order value",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "unitCost",
        "label": "Ingredients / packaging per order",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "other",
        "label": "Other daily operating cost",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "slow",
        "label": "Slower-day orders",
        "type": "number",
        "min": 0,
        "max": 100000,
        "step": "1",
        "integer": true
      }
    ],
    "rowFields": [
      {
        "key": "role",
        "label": "Staffing role / shift",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "hours",
        "label": "Paid shift hours",
        "type": "number",
        "min": 0,
        "max": 24,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "rate",
        "label": "Hourly employer cost",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Coffee Shop Daily Operating Plan",
        "currency": "USD",
        "hours": "8",
        "capacity": "20",
        "orders": "120",
        "ticket": "8",
        "unitCost": "2.5",
        "other": "180",
        "slow": "80"
      },
      "rows": [
        {
          "role": "Morning shift",
          "hours": "6",
          "rate": "20"
        },
        {
          "role": "Afternoon shift",
          "hours": "6",
          "rate": "20"
        }
      ]
    },
    "reportNote": "Daily sales = orders \u00d7 average order value. Remainder = sales \u2212 order ingredients/packaging \u2212 entered staffing \u2212 other costs. Capacity = opening hours \u00d7 entered feasible orders/hour, a planning ceiling rather than proven throughput. Staffing is unchanged in the slower-day scenario. Not net profit, cash timing or a full cafe feasibility model.",
    "maxRows": 100
  },
  {
    "slug": "construction-milestone-cash-schedule",
    "kind": "construction",
    "name": "Construction Milestone Cash Schedule",
    "category": "cashflow",
    "theme": "workflow-construction",
    "color": "#78521a",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "start",
        "label": "Project start date",
        "type": "date"
      },
      {
        "key": "end",
        "label": "Project end date",
        "type": "date"
      },
      {
        "key": "opening",
        "label": "Opening project cash",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      }
    ],
    "rowFields": [
      {
        "key": "label",
        "label": "Milestone / payment",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "date",
        "label": "Expected cash date",
        "type": "date"
      },
      {
        "key": "direction",
        "label": "Direction",
        "type": "select",
        "options": [
          "Receipt",
          "Payment"
        ]
      },
      {
        "key": "amount",
        "label": "Cash amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "certainty",
        "label": "Status",
        "type": "select",
        "options": [
          "Expected",
          "Confirmed"
        ]
      },
      {
        "key": "action",
        "label": "Dependency / next action",
        "type": "textarea",
        "maxLength": 600,
        "optional": true
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Construction Milestone Cash Schedule",
        "currency": "USD",
        "start": "2026-10-13",
        "end": "2026-11-13",
        "opening": "1000"
      },
      "rows": [
        {
          "label": "Customer deposit",
          "date": "2026-10-13",
          "direction": "Receipt",
          "amount": "2000",
          "certainty": "Confirmed",
          "action": "Confirm collection before purchasing materials."
        },
        {
          "label": "Materials",
          "date": "2026-10-14",
          "direction": "Payment",
          "amount": "2500",
          "certainty": "Confirmed",
          "action": "Supplier payment date."
        },
        {
          "label": "Labour",
          "date": "2026-10-16",
          "direction": "Payment",
          "amount": "1200",
          "certainty": "Expected",
          "action": "Confirm the payroll date."
        },
        {
          "label": "Milestone collection",
          "date": "2026-10-23",
          "direction": "Receipt",
          "amount": "3000",
          "certainty": "Expected",
          "action": "Confirm approval and collection timing."
        }
      ]
    },
    "reportNote": "Closing cash = opening + all entered receipts \u2212 all entered payments, including Expected records. The confirmed-only-receipts downside retains all payments. Lowest balance groups same-day movements and includes opening cash; it does not identify intraday shortages. No contract entitlement or legal payment right is inferred.",
    "maxRows": 100
  },
  {
    "slug": "trucking-trip-cost-worksheet",
    "kind": "trucking",
    "name": "Trucking Trip Cost Worksheet",
    "category": "operations",
    "theme": "workflow-trucking",
    "color": "#4b555e",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet name",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      },
      {
        "key": "loaded",
        "label": "Loaded miles",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "empty",
        "label": "Empty miles",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "revenue",
        "label": "Trip revenue excluding pass-through tax",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "mpg",
        "label": "Expected miles per gallon",
        "type": "number",
        "min": 0,
        "max": 100,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "fuel",
        "label": "Fuel price per gallon",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "maintenance",
        "label": "Maintenance allowance per total mile",
        "type": "number",
        "min": 0,
        "max": 100,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "paidOn",
        "label": "Expected customer collection date",
        "type": "date"
      }
    ],
    "rowFields": [
      {
        "key": "label",
        "label": "Nonfuel trip cost",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "amount",
        "label": "Cost amount",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "step": "0.01",
        "integer": false
      },
      {
        "key": "date",
        "label": "Cash payment date",
        "type": "date"
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional example: Trucking Trip Cost Worksheet",
        "currency": "USD",
        "loaded": "400",
        "empty": "100",
        "revenue": "1500",
        "mpg": "6.25",
        "fuel": "4",
        "maintenance": "0.2",
        "paidOn": "2026-10-30"
      },
      "rows": [
        {
          "label": "Driver cost",
          "amount": "300",
          "date": "2026-10-16"
        },
        {
          "label": "Tolls",
          "amount": "50",
          "date": "2026-10-16"
        },
        {
          "label": "Fixed operating allocation",
          "amount": "100",
          "date": "2026-10-16"
        }
      ]
    },
    "reportNote": "Total miles = loaded + empty. Fuel cost = total miles \u00f7 mpg \u00d7 fuel price. Modeled trip cost includes fuel, maintenance allowance and entered nonfuel costs. Cost/mile always uses total miles. Allowances and fixed allocations are not necessarily cash paid on this trip. The report dates only entered nonfuel payments, not fuel or maintenance cash timing.",
    "maxRows": 100
  }
];
const previous=api.evaluate;
api.configs.push(...configs);
const n=v=>Number(v),cent=api.cents,day=api.dateNumber,round=v=>Math.round((v+Number.EPSILON)*100)/100;
const mul=(units,price)=>Math.round(n(units)*cent(price));
const iso=v=>new Date(v).toISOString().slice(0,10),money=v=>({money:v});
const percent=(difference,base)=>base?round(difference/base*100)+'%':'Not defined (zero base)';
api.evaluate=function(slug,state){
 const c=configs.find(x=>x.slug===slug);if(!c)return previous(slug,state);
 api.validateShape(slug,state,true);const t=state.top,rs=state.rows;
 const metrics=[],rows=[],extra=[],warnings=[];let headers=[],preview=null;
 const metric=(label,value,format='number')=>metrics.push({label,value,format});
 if(c.kind==='variance'){
  let fc=cent(t.forecastOpening),ac=cent(t.actualOpening),impact=0;headers=['Cash movement','Direction','Forecast','Actual','Cash impact','Entered cause','Owner','Follow-up date','Evidence / action'];
  for(const r of rs){const f=cent(r.forecast),a=cent(r.actual),sign=r.direction==='Receipt'?1:-1,v=sign*(a-f);fc+=sign*f;ac+=sign*a;impact+=v;rows.push([r.label,r.direction,money(f),money(a),money(v),r.cause,r.owner,r.review,r.action||'No evidence entered']);if(v&&!r.action.trim())warnings.push(r.label+': add evidence or a follow-up action.');}
  metric('Forecast closing cash',fc,'money');metric('Actual closing cash',ac,'money');metric('Closing cash difference',ac-fc,'money');metric('Opening balance difference',cent(t.actualOpening)-cent(t.forecastOpening),'money');
  extra.push({title:'Reconciled forecast-to-actual bridge',headers:['Bridge step','Cash amount'],rows:[['Forecast closing',money(fc)],['Opening cash difference',money(cent(t.actualOpening)-cent(t.forecastOpening))],['Net movement cash impact',money(impact)],['Actual closing',money(ac)]]});
  warnings.push('Check the actual closing balance against your bank/cash records. A Timing label does not prove the missing money will arrive.');
 }
 if(c.kind==='budget'){
  let b=0,a=0;headers=['Budget line','Type','Budget','Actual','Amount variance','Variance %','Effect on remainder','Owner','Review date','Explanation / action'];
  for(const r of rs){const bv=cent(r.budget),av=cent(r.actual),diff=av-bv,sign=r.type==='Revenue'?1:-1;b+=sign*bv;a+=sign*av;rows.push([r.label,r.type,money(bv),money(av),money(diff),percent(diff,bv),money(sign*diff),r.owner,r.review,r.action||'No explanation entered']);}
  metric('Budget operating remainder',b,'money');metric('Actual operating remainder',a,'money');metric('Remainder variance',a-b,'money');
  warnings.push('A lower expense can reflect less activity, a delayed bill or a genuine saving. Check units and timing before describing it as an improvement.');
 }
 if(c.kind==='builder'){
  const lines=rs.reduce((a,r)=>a+n(r.lines),0);if(rs.some(r=>n(r.lines)<1)||lines>12)throw Error('Use at least one line per section and no more than 12 writing lines overall.');
  let slots=[];if(t.layout==='Daily'){let span=(n(t.endHour)-n(t.startHour)+24)%24;if(!span||span>16)throw Error('Use a daily range of 1 to 16 hours; start and end must differ.');slots=Array.from({length:span},(_,i)=>{const raw=n(t.startHour)+i;return String(raw%24).padStart(2,'0')+':00'+(raw>=24?' (+1 day)':'');});}else{const d=day(t.start),weekday=new Date(d).getUTCDay(),first=t.weekStart==='Monday'?1:0,offset=(weekday-first+7)%7;slots=Array.from({length:7},(_,i)=>iso(d-offset*86400000+i*86400000));if(slots[0]<'1900-01-01'||slots[6]>'2200-12-31')throw Error('The full week must stay within 1900–2200.');}
  headers=['Section','Writing lines'];rs.forEach(r=>rows.push([r.section,r.lines]));metric('Paper',t.paper,'text');metric('Layout',t.layout,'text');metric('Writing sections',rs.length);metric('Schedule slots',slots.length);
  preview={paper:t.paper,layout:t.layout,title:t.title,date:t.start,slots,sections:rs.map(r=>({name:r.section,lines:n(r.lines)}))};
  warnings.push('In the print dialog, select the same paper size, portrait orientation and disable browser headers/footers. Check the preview before printing.');
 }
 if(c.kind==='teacher'){
  if(!/^\d{4}-\d{2}$/.test(t.month)||!Number.isFinite(day(t.month+'-01')))throw Error('Use a valid teaching month in YYYY-MM format.');
  let overdue=0,ready=0;headers=['Lesson / group','Lesson date','Preparation due','Owner','Materials / preparation','Status','Review flag'];
  for(const r of [...rs].sort((a,b)=>a.date.localeCompare(b.date))){if(!r.date.startsWith(t.month+'-'))throw Error(r.lesson+': lesson date must be in the entered month.');if(r.prep>r.date)throw Error(r.lesson+': preparation due date must not be after the lesson.');const flag=r.status==='Ready'?'Ready':r.prep<t.asOf?'Preparation overdue':r.prep===t.asOf?'Preparation due today':'Upcoming preparation';if(flag==='Preparation overdue')overdue++;if(r.status==='Ready')ready++;rows.push([r.lesson,r.date,r.prep,r.owner,r.materials,r.status,flag]);}
  metric('Lessons entered',rs.length);metric('Preparation ready',ready);metric('Preparation overdue',overdue);metric('Not yet ready',rs.length-ready);
 }
 if(c.kind==='production'){
  const span=(day(t.end)-day(t.start))/86400000+1;if(span<1||span>62)throw Error('Use a production horizon of 1 to 62 days.');
  const dates=new Map();for(let d=day(t.start);d<=day(t.end);d+=86400000){const w=new Date(d).getUTCDay();if(t.days==='Every day'||w!==0&&w!==6)dates.set(iso(d),0);}
  let load=0,complete=0;headers=['Deliverable','Production day','Hours','Production owner','Review owner','Status','Destination / action'];
  for(const r of rs){if(!dates.has(r.date))throw Error(r.item+': production day must be a working day in the selected horizon.');if(r.status!=='Complete'){load+=n(r.hours);dates.set(r.date,dates.get(r.date)+n(r.hours));}else complete+=n(r.hours);rows.push([r.item,r.date,r.hours,r.owner,r.reviewer,r.status,r.action||'No action entered']);}
  const overloaded=[...dates.values()].filter(v=>round(v)>n(t.daily)).length;metric('Remaining planned hours',round(load),'hours');metric('Window capacity',round(dates.size*n(t.daily)),'hours');metric('Over-capacity days',overloaded);metric('Completed entered hours',round(complete),'hours');
  extra.push({title:'Remaining production load by date',headers:['Date','Available hours','Remaining load','Free / overbooked hours'],rows:[...dates].map(([d,v])=>[d,t.daily,round(v),round(n(t.daily)-v)])});
  if(overloaded)warnings.push('Total window capacity can look sufficient while a particular date is overloaded. Move a work block or reduce scope.');
 }
 if(c.kind==='campaign'){
  let planned=0,actual=0;headers=['Channel / test','Planned spend','Actual spend','Spend variance','Inquiries','Customers','Cost / inquiry','Cost / customer','Decision rule / attribution'];
  for(const r of rs){const p=cent(r.planned),a=cent(r.actual);planned+=p;actual+=a;rows.push([r.channel,money(p),money(a),money(a-p),r.inquiries,r.customers,n(r.inquiries)?money(Math.round(a/n(r.inquiries))):'Not defined (zero inquiries)',n(r.customers)?money(Math.round(a/n(r.customers))):'Not defined (zero customers)',r.rule]);}
  metric('Planned spend',planned,'money');metric('Actual spend',actual,'money');metric('Unallocated planned budget',cent(t.ceiling)-planned,'money');metric('Remaining actual budget',cent(t.ceiling)-actual,'money');
  if(planned>cent(t.ceiling)||actual>cent(t.ceiling))warnings.push('At least one spend total exceeds the test budget. Review commitments before continuing.');warnings.push('Do not sum channel customers as unique customers unless you have removed duplicate attribution.');
 }
 if(c.kind==='lean'){
  headers=['Assumption','Evidence observed','Next test','Owner','Due','Entered evidence status'];for(const r of rs)rows.push([r.assumption,r.evidence||'No evidence recorded',r.test,r.owner,r.due,r.status]);
  metric('Assumptions entered',rs.length);metric('Untested',rs.filter(r=>r.status==='Untested').length);metric('Contradicted',rs.filter(r=>r.status==='Contradicted').length);metric('Review date',t.review,'text');
  if(rs.length>3)warnings.push('The evidence log contains more than three assumptions and can print across multiple pages.');warnings.push('Use evidence and actual customer behavior to revise the plan. This worksheet does not validate an offer automatically.');
 }
 if(c.kind==='projections'){
  const sorted=[...rs].sort((a,b)=>a.month.localeCompare(b.month));let balance=cent(t.opening),low=balance,operating=0,last=null;headers=['Month','Billed revenue','Incurred operating expense','Depreciation','Operating result','Cash collected','Operating cash paid','Debt principal','New funding','Owner withdrawal','Closing cash'];
  for(const r of sorted){if(!r.month.endsWith('-01'))throw Error('Each projection month must start on day 1.');const ordinal=n(r.month.slice(0,4))*12+n(r.month.slice(5,7));if(last!==null&&ordinal!==last+1)throw Error('Enter consecutive, unique months without a gap.');last=ordinal;const result=cent(r.sales)-cent(r.expense)-cent(r.depreciation);operating+=result;balance+=cent(r.receipts)+cent(r.funding)-cent(r.paid)-cent(r.principal)-cent(r.draw);low=Math.min(low,balance);rows.push([r.month,money(cent(r.sales)),money(cent(r.expense)),money(cent(r.depreciation)),money(result),money(cent(r.receipts)),money(cent(r.paid)),money(cent(r.principal)),money(cent(r.funding)),money(cent(r.draw)),money(balance)]);}
  metric('Modeled operating result',operating,'money');metric('Closing cash',balance,'money');metric('Lowest opening / month-end cash',low,'money');metric('Projection months',rs.length);if(low<0)warnings.push('At least one opening/month-end cash balance is negative. Check actual payment dates with a shorter cash schedule.');warnings.push('Keep billed revenue separate from collections and incurred expenses separate from cash paid. Debt principal and new capital affect cash, not this operating result.');
 }
 if(c.kind==='coffee'){
  const staff=rs.reduce((a,r)=>a+mul(r.hours,r.rate),0),capacity=round(n(t.hours)*n(t.capacity));headers=['Role / shift','Paid hours','Hourly employer cost','Shift cost'];rs.forEach(r=>rows.push([r.role,r.hours,money(cent(r.rate)),money(mul(r.hours,r.rate))]));
  const result=orders=>{const sales=mul(orders,t.ticket),ingredients=mul(orders,t.unitCost);return [orders,money(sales),money(ingredients),money(staff),money(cent(t.other)),money(sales-ingredients-staff-cent(t.other))];};
  metric('Daily capacity ceiling',capacity);metric('Expected daily sales',mul(t.orders,t.ticket),'money');metric('Entered staffing cost',staff,'money');metric('Base operating remainder',mul(t.orders,t.ticket)-mul(t.orders,t.unitCost)-staff-cent(t.other),'money');
  extra.push({title:'Base and slower-day operating comparison',headers:['Orders','Sales','Ingredients / packaging','Staffing','Other operating cost','Operating remainder'],rows:[result(t.orders),result(t.slow)]});
  if(n(t.slow)>n(t.orders))throw Error('Slower-day orders cannot exceed base expected orders.');if(n(t.orders)>capacity)warnings.push('Expected orders exceed your entered capacity ceiling. Revise volume or confirm throughput.');warnings.push('Remainder excludes financing, tax and any costs you have not entered. It is not net profit or bank cash.');
 }
 if(c.kind==='construction'){
  const span=(day(t.end)-day(t.start))/86400000;if(span<0||span>730)throw Error('Use a project horizon from 1 to 731 calendar days.');
  const grouped=new Map();headers=['Cash date','Milestone / payment','Direction','Status','Amount','Dependency / action'];
  for(const r of [...rs].sort((a,b)=>a.date.localeCompare(b.date))){if(r.date<t.start||r.date>t.end)throw Error(r.label+': cash date is outside the project horizon.');if(!grouped.has(r.date))grouped.set(r.date,{incoming:0,outgoing:0,confirmed:0});const g=grouped.get(r.date),v=cent(r.amount);if(r.direction==='Receipt'){g.incoming+=v;if(r.certainty==='Confirmed')g.confirmed+=v;}else g.outgoing+=v;rows.push([r.date,r.label,r.direction,r.certainty,money(v),r.action||'No dependency entered']);}
  let balance=cent(t.opening),down=balance,low=balance,downLow=balance;const schedule=[];for(const[d,g]of grouped){balance+=g.incoming-g.outgoing;down+=g.confirmed-g.outgoing;low=Math.min(low,balance);downLow=Math.min(downLow,down);schedule.push([d,money(g.incoming),money(g.outgoing),money(balance),money(down)]);}
  metric('Closing project cash',balance,'money');metric('Lowest opening / day-end cash',low,'money');metric('Confirmed-receipts closing',down,'money');metric('Confirmed-receipts lowest cash',downLow,'money');extra.push({title:'Milestone cash schedule',headers:['Date','All receipts','All payments','Base closing','Confirmed receipts only closing'],rows:schedule});if(low<0||downLow<0)warnings.push('A negative balance appears in at least one scenario. Review collection dependencies before committing spending.');
 }
 if(c.kind==='trucking'){
  const miles=n(t.loaded)+n(t.empty);if(!miles)throw Error('Enter at least one total mile.');if(!n(t.mpg))throw Error('Miles per gallon must be greater than zero.');
  const gallons=miles/n(t.mpg),fuelCost=Math.round(gallons*cent(t.fuel)),maintenance=mul(miles,t.maintenance),other=rs.reduce((a,r)=>a+cent(r.amount),0),cost=fuelCost+maintenance+other,rev=cent(t.revenue);headers=['Nonfuel cost','Amount','Entered cash date'];rs.forEach(r=>rows.push([r.label,money(cent(r.amount)),r.date]));
  metric('Total miles',round(miles));metric('Modeled trip cost',cost,'money');metric('Cost per total mile',Math.round(cost/miles),'money');metric('Trip operating remainder',rev-cost,'money');
  extra.push({title:'Consistent trip economics',headers:['Measure','Value'],rows:[['Loaded miles',t.loaded],['Empty miles',t.empty],['Expected fuel gallons',round(gallons)],['Modeled fuel cost',money(fuelCost)],['Maintenance allowance',money(maintenance)],['Nonfuel entered costs',money(other)],['Revenue / total mile',money(Math.round(rev/miles))],['Revenue / loaded mile',n(t.loaded)?money(Math.round(rev/n(t.loaded))):'Not defined (zero loaded miles)'],['Expected collection date',t.paidOn]]},{title:'Entered nonfuel payments before collection',headers:['Cost','Cash date','Amount'],rows:rs.filter(r=>r.date<t.paidOn).map(r=>[r.label,r.date,money(cent(r.amount))])});warnings.push('Fuel and maintenance cash dates are not modeled. Use a dated cash planner to check the full payment gap. All rates are your assumptions, not industry benchmarks.');
 }
 return {metrics,headers,rows,extra,warnings,note:c.reportNote,preview};
};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
