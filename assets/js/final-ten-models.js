(function(root){'use strict';
const api=typeof module!=='undefined'&&module.exports?require('./small-tools-models.js'):root.NexalySmallTools;
const configs=[
  {
    "slug": "dead-stock-review-planner",
    "name": "Dead Stock Review Planner",
    "kind": "dead",
    "category": "inventory",
    "color": "#315445",
    "pale": "#f4f3ec",
    "description": "Review stock with no recent sales. See inactivity days and inventory cost at risk using your own review threshold.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency (no conversion)",
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
        "key": "threshold",
        "label": "Review after inactive days",
        "type": "number",
        "min": 0,
        "max": 3650,
        "integer": true,
        "step": "1"
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "item",
        "label": "SKU / location",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "qty",
        "label": "On-hand units",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "cost",
        "label": "Unit cost",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "received",
        "label": "First receipt date",
        "type": "date",
        "optional": false
      },
      {
        "key": "sale",
        "label": "Last sale date (blank if none)",
        "type": "date",
        "optional": true
      },
      {
        "key": "action",
        "label": "Proposed next action",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional dead stock review planner",
        "asOf": "2026-10-21",
        "currency": "USD",
        "threshold": "90"
      },
      "rows": [
        {
          "ref": "STOCK-01",
          "item": "Blue scarf / Shelf A",
          "qty": "20",
          "cost": "8",
          "received": "2026-06-01",
          "sale": "2026-07-01",
          "action": "Review merchandising before reordering"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Inactivity days = review date minus last sale date, or first receipt date if no sale is entered. Flag when days are at least the chosen threshold and quantity is positive. Value = units \u00d7 entered cost.",
    "reportNote": "Inactivity days = review date minus last sale date, or first receipt date if no sale is entered. Flag when days are at least the chosen threshold and quantity is positive. Value = units \u00d7 entered cost. Inactivity is not proof that stock is obsolete. No sales forecast, accounting write-down or disposal decision is made. Dates must describe events on or before the review date.",
    "example": "20 scarves at $8 cost represent $160. July 1 to October 21 is 112 days; at a 90-day threshold the row needs review.",
    "limits": "Inactivity is not proof that stock is obsolete. No sales forecast, accounting write-down or disposal decision is made. Dates must describe events on or before the review date.",
    "steps": [
      "Set a review date, currency and inactivity threshold.",
      "Enter one SKU/location per reference with first receipt and latest sale dates.",
      "Leave last sale blank only if none has occurred.",
      "Review flagged lines individually and record a next action."
    ],
    "features": [
      "Review stock with no recent sales. See inactivity days and inventory cost at risk using your own review threshold.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "stock-coverage-planner",
        "Compare demand-based coverage"
      ]
    ],
    "journal": "boutique-inventory-spreadsheet",
    "visual": [
      "112 days inactive",
      "20 units \u00d7 $8",
      "$160 to review"
    ]
  },
  {
    "slug": "boutique-return-to-stock-log",
    "name": "Boutique Return to Stock Log",
    "kind": "returns",
    "category": "inventory",
    "color": "#7c3d50",
    "pale": "#f4f3ec",
    "description": "Separate returned clothing into inspected sellable, rejected and pending units. Keep condition notes and a reviewer with each return.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "item",
        "label": "SKU / variant",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "received",
        "label": "Return received date",
        "type": "date",
        "optional": false
      },
      {
        "key": "qty",
        "label": "Returned units",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "released",
        "label": "Inspected sellable units",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "rejected",
        "label": "Rejected units",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "reviewer",
        "label": "Reviewer / owner",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "note",
        "label": "Condition or next action",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional boutique return to stock log",
        "asOf": "2026-10-21"
      },
      "rows": [
        {
          "ref": "RETURN-01",
          "item": "TEE-BLK-M",
          "received": "2026-10-20",
          "qty": "5",
          "released": "3",
          "rejected": "1",
          "reviewer": "Example owner",
          "note": "Inspect one remaining unit"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Pending units = returned units \u2212 inspected sellable units \u2212 rejected units. Released plus rejected cannot exceed returned units.",
    "reportNote": "Pending units = returned units \u2212 inspected sellable units \u2212 rejected units. Released plus rejected cannot exceed returned units. This worksheet does not issue refunds or add stock. A refund and a physical return are separate events. Enter inspection decisions already made, not an assumed approval.",
    "example": "Five returned tees with three sellable and one rejected leave one pending. Only the three sellable units are candidates for a real stock return entry.",
    "limits": "This worksheet does not issue refunds or add stock. A refund and a physical return are separate events. Enter inspection decisions already made, not an assumed approval.",
    "steps": [
      "Enter the review date and a unique return reference.",
      "Record the exact variant and receipt date.",
      "Enter inspected sellable and rejected quantities; pending is calculated.",
      "Post approved stock movements once in your actual register."
    ],
    "features": [
      "Separate returned clothing into inspected sellable, rejected and pending units. Keep condition notes and a reviewer with each return.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "physical-count-adjustment-worksheet",
        "Reconcile physical stock"
      ]
    ],
    "journal": "boutique-inventory-spreadsheet",
    "visual": [
      "5 units returned",
      "3 sellable \u00b7 1 rejected",
      "1 pending review"
    ]
  },
  {
    "slug": "seasonal-stock-clearance-planner",
    "name": "Seasonal Stock Clearance Planner",
    "kind": "clearance",
    "category": "inventory",
    "color": "#9b4826",
    "pale": "#f4f3ec",
    "description": "Compare a clearance price with inventory cost and selling fees. See a transparent sell-through scenario before choosing a markdown.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency (no conversion)",
        "type": "select",
        "options": [
          "USD",
          "GBP",
          "CAD",
          "AUD",
          "EUR",
          "NZD"
        ]
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "item",
        "label": "SKU / style",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "qty",
        "label": "Units proposed for sale",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "price",
        "label": "Current unit price",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "markdown",
        "label": "Markdown percent",
        "type": "number",
        "min": 0,
        "max": 100,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "cost",
        "label": "Unit inventory cost",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "fee",
        "label": "Selling fee percent",
        "type": "number",
        "min": 0,
        "max": 100,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "fixed",
        "label": "Other scenario costs",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional seasonal stock clearance planner",
        "asOf": "2026-10-21",
        "currency": "USD"
      },
      "rows": [
        {
          "ref": "CLEAR-01",
          "item": "Seasonal tote",
          "qty": "10",
          "price": "30",
          "markdown": "20",
          "cost": "12",
          "fee": "5",
          "fixed": "15"
        }
      ]
    },
    "maxRows": 100,
    "formula": "New unit price = current price \u00d7 (1 \u2212 markdown/100), rounded to cents. Revenue = units \u00d7 new price. Contribution = revenue \u2212 item cost \u2212 percentage selling fees \u2212 other scenario costs.",
    "reportNote": "New unit price = current price \u00d7 (1 \u2212 markdown/100), rounded to cents. Revenue = units \u00d7 new price. Contribution = revenue \u2212 item cost \u2212 percentage selling fees \u2212 other scenario costs. Assumes every entered unit sells. Contribution excludes unentered overhead, taxes, returns and shipping. It is not a prediction of sales or net profit.",
    "example": "10 totes at $30 with a 20% markdown sell at $24. Revenue is $240, item cost $120, fees $12 and other costs $15, leaving $93 modeled contribution.",
    "limits": "Assumes every entered unit sells. Contribution excludes unentered overhead, taxes, returns and shipping. It is not a prediction of sales or net profit.",
    "steps": [
      "Choose one currency and a scenario label.",
      "Enter quantity and current price for each distinct style.",
      "Add markdown, unit cost, percentage fees and other costs.",
      "Review negative contributions and test another scenario before changing prices."
    ],
    "features": [
      "Compare a clearance price with inventory cost and selling fees. See a transparent sell-through scenario before choosing a markdown.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "dead-stock-review-planner",
        "Review inactive stock first"
      ]
    ],
    "journal": "boutique-inventory-spreadsheet",
    "visual": [
      "$30 \u2192 $24",
      "10 units \u00b7 $240 revenue",
      "$93 contribution"
    ]
  },
  {
    "slug": "shipment-cost-allocation-tool",
    "name": "Shipment Cost Allocation Tool",
    "kind": "allocation",
    "category": "inventory",
    "color": "#225f7b",
    "pale": "#f4f3ec",
    "description": "Allocate shared shipment charges across received SKUs by merchandise value or units. Review landed line totals and unit-cost estimates.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "currency",
        "label": "Currency (no conversion)",
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
        "key": "shared",
        "label": "Shared shipment charges",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      },
      {
        "key": "basis",
        "label": "Allocation basis",
        "type": "select",
        "options": [
          "Merchandise value",
          "Units"
        ]
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "item",
        "label": "SKU",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "qty",
        "label": "Received units",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "cost",
        "label": "Merchandise unit cost",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": false,
        "step": "0.01"
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional shipment cost allocation tool",
        "asOf": "2026-10-21",
        "currency": "USD",
        "shared": "30",
        "basis": "Merchandise value"
      },
      "rows": [
        {
          "ref": "LINE-A",
          "item": "Notebook A",
          "qty": "10",
          "cost": "5"
        },
        {
          "ref": "LINE-B",
          "item": "Notebook B",
          "qty": "20",
          "cost": "5"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Weights use merchandise value or units. Allocate shared charges in cents using largest fractional remainders; tied remainders follow row order. Landed line total = merchandise cost + allocation. Unit estimate = landed total / quantity.",
    "reportNote": "Weights use merchandise value or units. Allocate shared charges in cents using largest fractional remainders; tied remainders follow row order. Landed line total = merchandise cost + allocation. Unit estimate = landed total / quantity. Only entered charges are allocated. This is a planning estimate, not a customs, tax or accounting valuation rule. Rounded unit estimates may not multiply back to exact line totals.",
    "example": "With $30 shared charges and lines costing $50 and $100, value allocation gives $10 and $20. Landed totals are $60 and $120; both unit estimates are $6.",
    "limits": "Only entered charges are allocated. This is a planning estimate, not a customs, tax or accounting valuation rule. Rounded unit estimates may not multiply back to exact line totals.",
    "steps": [
      "Choose a currency, total shared charges and allocation basis.",
      "Enter positive received quantities and merchandise unit costs.",
      "Review how weights distribute the charges.",
      "Keep line totals as the cent-accurate record and document the chosen basis."
    ],
    "features": [
      "Allocate shared shipment charges across received SKUs by merchandise value or units. Review landed line totals and unit-cost estimates.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "supplier-quote-comparison",
        "Compare supplier quotes"
      ]
    ],
    "journal": "supplier-quote-comparison",
    "visual": [
      "$30 shared charges",
      "$10 to A \u00b7 $20 to B",
      "$6 per unit"
    ]
  },
  {
    "slug": "repair-job-handoff-planner",
    "name": "Repair Job Handoff Planner",
    "kind": "handoff",
    "category": "operations",
    "color": "#655034",
    "pale": "#f4f3ec",
    "description": "Prepare a small-engine repair handoff with ownership, next actions, approval records and parts blockers. Review overdue open jobs.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "machine",
        "label": "Machine / serial reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "owner",
        "label": "Assigned person",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "due",
        "label": "Next action date",
        "type": "date",
        "optional": false
      },
      {
        "key": "approval",
        "label": "Customer approval",
        "type": "select",
        "options": [
          "Pending",
          "Recorded",
          "Not required"
        ]
      },
      {
        "key": "parts",
        "label": "Parts status",
        "type": "select",
        "options": [
          "Waiting",
          "Ready",
          "Not required"
        ]
      },
      {
        "key": "status",
        "label": "Handoff status",
        "type": "select",
        "options": [
          "Open",
          "Handed over"
        ]
      },
      {
        "key": "action",
        "label": "Next action / evidence reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional repair job handoff planner",
        "asOf": "2026-10-21"
      },
      "rows": [
        {
          "ref": "JOB-01",
          "machine": "Example mower M-12",
          "owner": "Example technician",
          "due": "2026-10-20",
          "approval": "Pending",
          "parts": "Waiting",
          "status": "Open",
          "action": "Request approval before ordering the belt"
        }
      ]
    },
    "maxRows": 100,
    "formula": "An open job is overdue when its next action date is before the review date. Pending approval or waiting parts flags a blocker. Handed-over rows stay in the record but leave the open queue.",
    "reportNote": "An open job is overdue when its next action date is before the review date. Pending approval or waiting parts flags a blocker. Handed-over rows stay in the record but leave the open queue. This is an administrative handoff, not a repair procedure, safety inspection or permission to release equipment. It does not contact customers or order parts.",
    "example": "JOB-01 is due October 20 and reviewed October 21: one day overdue, with approval and parts still pending.",
    "limits": "This is an administrative handoff, not a repair procedure, safety inspection or permission to release equipment. It does not contact customers or order parts.",
    "steps": [
      "Give each job a unique reference and machine identifier.",
      "Assign the next owner and action date.",
      "Record actual approval and parts states.",
      "Review blockers together and mark handed over only after the handoff occurs."
    ],
    "features": [
      "Prepare a small-engine repair handoff with ownership, next actions, approval records and parts blockers. Review overdue open jobs.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "repair-parts-labour-worksheet",
        "Prepare a parts and labor estimate"
      ]
    ],
    "journal": "repair-shop-parts-inventory",
    "visual": [
      "JOB-01 \u00b7 mower",
      "Approval + parts pending",
      "Next owner and action"
    ]
  },
  {
    "slug": "rental-dispatch-return-checklist",
    "name": "Rental Dispatch Return Checklist",
    "kind": "rental",
    "category": "operations",
    "color": "#295b63",
    "pale": "#f4f3ec",
    "description": "Reconcile rental units dispatched, returned and held for inspection. Keep missing quantities and recorded inspection decisions separate.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asset",
        "label": "Asset / kit",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "due",
        "label": "Return due date",
        "type": "date",
        "optional": false
      },
      {
        "key": "out",
        "label": "Units dispatched",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "returned",
        "label": "Units physically returned",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "held",
        "label": "Returned units held for inspection",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "release",
        "label": "Inspection decision",
        "type": "select",
        "options": [
          "Pending",
          "Recorded"
        ]
      },
      {
        "key": "note",
        "label": "Condition / accessory note",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional rental dispatch return checklist",
        "asOf": "2026-10-21"
      },
      "rows": [
        {
          "ref": "HIRE-01",
          "asset": "Example lighting kit",
          "due": "2026-10-20",
          "out": "8",
          "returned": "7",
          "held": "2",
          "release": "Pending",
          "note": "One stand missing; inspect two returned lamps"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Outstanding = dispatched \u2212 returned. Potentially releasable = returned \u2212 held, but the release candidate remains zero while inspection decision is Pending. Overdue outstanding units require a return date before the review date.",
    "reportNote": "Outstanding = dispatched \u2212 returned. Potentially releasable = returned \u2212 held, but the release candidate remains zero while inspection decision is Pending. Overdue outstanding units require a return date before the review date. Counts do not establish fitness for use or customer liability. Use your approved equipment inspection procedure and actual asset records before release. No deposits or damage charges are calculated.",
    "example": "Eight units dispatched and seven returned leave one outstanding. Two returned units are held. While inspection is pending, the tool shows zero release candidates.",
    "limits": "Counts do not establish fitness for use or customer liability. Use your approved equipment inspection procedure and actual asset records before release. No deposits or damage charges are calculated.",
    "steps": [
      "Use one rental/asset reference per row.",
      "Enter dispatch and actual return quantities.",
      "Separate inspection holds from missing units.",
      "Record inspection only after the responsible person completes the required checks."
    ],
    "features": [
      "Reconcile rental units dispatched, returned and held for inspection. Keep missing quantities and recorded inspection decisions separate.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "rental-booking-conflict-checker",
        "Check booking overlaps"
      ]
    ],
    "journal": "rental-equipment-maintenance-log",
    "visual": [
      "8 out \u00b7 7 returned",
      "1 missing \u00b7 2 held",
      "Inspection still pending"
    ]
  },
  {
    "slug": "calibration-due-date-planner",
    "name": "Calibration Due Date Planner",
    "kind": "calibration",
    "category": "operations",
    "color": "#485489",
    "pale": "#f4f3ec",
    "description": "Review instrument calibration dates against a chosen date. Separate past-due, due-today and upcoming records using your approved schedule.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "window",
        "label": "Look-ahead days",
        "type": "number",
        "min": 0,
        "max": 3650,
        "integer": true,
        "step": "1"
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asset",
        "label": "Instrument identifier",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "last",
        "label": "Last calibration date",
        "type": "date",
        "optional": false
      },
      {
        "key": "due",
        "label": "Approved next due date",
        "type": "date",
        "optional": false
      },
      {
        "key": "status",
        "label": "Record status",
        "type": "select",
        "options": [
          "Active",
          "Out of service"
        ]
      },
      {
        "key": "source",
        "label": "Approved schedule / certificate reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional calibration due date planner",
        "asOf": "2026-10-21",
        "window": "30"
      },
      "rows": [
        {
          "ref": "CAL-01",
          "asset": "Example scale S-01",
          "last": "2026-04-18",
          "due": "2026-10-18",
          "status": "Active",
          "source": "Example approved schedule revision 2"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Days to due = approved next due date \u2212 review date in calendar days. Past due is negative; due today is zero; upcoming is positive and within the look-ahead. Out-of-service rows are shown separately.",
    "reportNote": "Days to due = approved next due date \u2212 review date in calendar days. Past due is negative; due today is zero; upcoming is positive and within the look-ahead. Out-of-service rows are shown separately. Enter an already approved due date. The tool does not recommend intervals, establish traceability, validate certificates or authorize equipment use.",
    "example": "An active instrument due October 18 is three days past due on October 21. The worksheet does not decide whether that instrument may be used.",
    "limits": "Enter an already approved due date. The tool does not recommend intervals, establish traceability, validate certificates or authorize equipment use.",
    "steps": [
      "Set the review date and look-ahead window.",
      "Enter an instrument and its last calibration date.",
      "Copy the approved next due date and source reference.",
      "Review overdue records with the responsible person and retain service evidence."
    ],
    "features": [
      "Review instrument calibration dates against a chosen date. Separate past-due, due-today and upcoming records using your approved schedule.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "equipment-maintenance-due-planner",
        "Plan maintenance separately"
      ]
    ],
    "journal": "equipment-calibration-log",
    "visual": [
      "Approved date only",
      "October 18 \u2192 October 21",
      "3 days past due"
    ]
  },
  {
    "slug": "batch-expiry-review-planner",
    "name": "Batch Expiry Review Planner",
    "kind": "expiry",
    "category": "operations",
    "color": "#77513b",
    "pale": "#f4f3ec",
    "description": "Sort lot dates for review while keeping released, held and disposed records distinct. See approaching dates without treating a date as permission to use stock.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "window",
        "label": "Look-ahead days",
        "type": "number",
        "min": 0,
        "max": 3650,
        "integer": true,
        "step": "1"
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "item",
        "label": "Item / lot",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "expiry",
        "label": "Recorded expiry date",
        "type": "date",
        "optional": false
      },
      {
        "key": "qty",
        "label": "Units physically held",
        "type": "number",
        "min": 0,
        "max": 1000000,
        "integer": true,
        "step": "1"
      },
      {
        "key": "status",
        "label": "Stock status",
        "type": "select",
        "options": [
          "Released",
          "Hold",
          "Disposed"
        ]
      },
      {
        "key": "action",
        "label": "Review owner / next action",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional batch expiry review planner",
        "asOf": "2026-10-21",
        "window": "14"
      },
      "rows": [
        {
          "ref": "LOT-01",
          "item": "Example craft supply lot",
          "expiry": "2026-10-25",
          "qty": "30",
          "status": "Released",
          "action": "Owner to review the recorded date and handling rules"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Days to recorded expiry = expiry date \u2212 review date. Before review is past date; same date requires today review; positive days within the window are approaching. Disposed records require zero held units.",
    "reportNote": "Days to recorded expiry = expiry date \u2212 review date. Before review is past date; same date requires today review; positive days within the window are approaching. Disposed records require zero held units. Expiry interpretation depends on the product, source and applicable rules. No safety, shelf-life extension, recall decision or sale authorization is provided.",
    "example": "A lot dated October 25 is four days away on October 21. Its 30 units stay in their entered stock status; the tool does not release them.",
    "limits": "Expiry interpretation depends on the product, source and applicable rules. No safety, shelf-life extension, recall decision or sale authorization is provided.",
    "steps": [
      "Set review date and look-ahead days.",
      "Record the exact item/lot and date from the authoritative record.",
      "Enter physically held units and their current status.",
      "Review earliest dates and hold records with the responsible owner."
    ],
    "features": [
      "Sort lot dates for review while keeping released, held and disposed records distinct. See approaching dates without treating a date as permission to use stock.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "physical-count-adjustment-worksheet",
        "Check physical quantities"
      ]
    ],
    "journal": "batch-lot-traceability-log",
    "visual": [
      "LOT-01 \u00b7 30 units",
      "October 25 recorded date",
      "4 days to review"
    ]
  },
  {
    "slug": "executive-function-task-breakdown",
    "name": "Executive Function Task Breakdown",
    "kind": "tasks",
    "category": "personal",
    "color": "#66518a",
    "pale": "#f4f3ec",
    "description": "Break a task into visible next steps, estimate remaining effort and compare unblocked work with your available time.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "budget",
        "label": "Available work minutes",
        "type": "number",
        "min": 0,
        "max": 10000,
        "integer": true,
        "step": "1"
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "task",
        "label": "One concrete next step",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "cue",
        "label": "Start cue / needed material",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "minutes",
        "label": "Estimated focused minutes",
        "type": "number",
        "min": 0,
        "max": 1440,
        "integer": true,
        "step": "1"
      },
      {
        "key": "status",
        "label": "Step status",
        "type": "select",
        "options": [
          "To do",
          "Done",
          "Blocked"
        ]
      },
      {
        "key": "note",
        "label": "Finish signal / blocker",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional executive function task breakdown",
        "asOf": "2026-10-21",
        "budget": "25"
      },
      "rows": [
        {
          "ref": "STEP-01",
          "task": "Gather five receipts",
          "cue": "Open the receipts envelope",
          "minutes": "10",
          "status": "To do",
          "note": "Five receipts on the desk"
        },
        {
          "ref": "STEP-02",
          "task": "Enter the five amounts",
          "cue": "Open the expense sheet",
          "minutes": "20",
          "status": "To do",
          "note": "Five rows recorded"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Remaining minutes sum all non-done steps. Ready minutes sum To do steps. Blocked minutes are reported separately. Ready time gap = max(0, ready minutes \u2212 available work minutes).",
    "reportNote": "Remaining minutes sum all non-done steps. Ready minutes sum To do steps. Blocked minutes are reported separately. Ready time gap = max(0, ready minutes \u2212 available work minutes). A planning aid, not treatment or diagnosis. Estimates do not guarantee completion. It does not choose priorities or send reminders.",
    "example": "Two ready steps taking 10 and 20 minutes need 30 minutes. A 25-minute work window leaves a five-minute ready-work gap.",
    "limits": "A planning aid, not treatment or diagnosis. Estimates do not guarantee completion. It does not choose priorities or send reminders.",
    "steps": [
      "Enter a realistic focused-work window, excluding breaks.",
      "Write one observable action per step with a start cue.",
      "Estimate minutes and identify blocked steps.",
      "Choose a manageable first step and update status after doing it."
    ],
    "features": [
      "Break a task into visible next steps, estimate remaining effort and compare unblocked work with your available time.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "leave-on-time-routine-planner",
        "Work backward from a departure time"
      ]
    ],
    "journal": "adhd-planner-for-adults",
    "visual": [
      "Gather \u00b7 10 minutes",
      "Enter \u00b7 20 minutes",
      "25 available \u00b7 5 short"
    ]
  },
  {
    "slug": "free-trial-cancellation-calendar",
    "name": "Free Trial Cancellation Calendar",
    "kind": "trials",
    "category": "cashflow",
    "color": "#356449",
    "pale": "#f4f3ec",
    "description": "Plan a manual trial-cancellation review before an entered trial end date. Track requested versus confirmed cancellation without claiming it is complete.",
    "fields": [
      {
        "key": "title",
        "label": "Worksheet label",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "asOf",
        "label": "Review date",
        "type": "date",
        "optional": false
      },
      {
        "key": "window",
        "label": "Look-ahead days",
        "type": "number",
        "min": 0,
        "max": 3650,
        "integer": true,
        "step": "1"
      }
    ],
    "rowFields": [
      {
        "key": "ref",
        "label": "Unique record reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "service",
        "label": "Trial / service",
        "type": "text",
        "maxLength": 160,
        "optional": false
      },
      {
        "key": "end",
        "label": "Trial end date",
        "type": "date",
        "optional": false
      },
      {
        "key": "buffer",
        "label": "Chosen action buffer days",
        "type": "number",
        "min": 0,
        "max": 3650,
        "integer": true,
        "step": "1"
      },
      {
        "key": "status",
        "label": "Cancellation status",
        "type": "select",
        "options": [
          "Open",
          "Requested",
          "Confirmed"
        ]
      },
      {
        "key": "source",
        "label": "Terms / confirmation reference",
        "type": "text",
        "maxLength": 160,
        "optional": false
      }
    ],
    "sample": {
      "top": {
        "title": "Fictional free trial cancellation calendar",
        "asOf": "2026-10-21",
        "window": "14"
      },
      "rows": [
        {
          "ref": "TRIAL-01",
          "service": "Example design app",
          "end": "2026-10-28",
          "buffer": "7",
          "status": "Open",
          "source": "Check actual account terms and cutoff time"
        }
      ]
    },
    "maxRows": 100,
    "formula": "Action date = trial end date \u2212 chosen buffer calendar days. Requested remains active until confirmed. An action date on or before review requires attention; confirmed rows leave the action queue.",
    "reportNote": "Action date = trial end date \u2212 chosen buffer calendar days. Requested remains active until confirmed. An action date on or before review requires attention; confirmed rows leave the action queue. No cancellations or reminders are sent. The action date is your planning choice, not a verified contractual deadline. Check time zones, billing cutoffs and confirmation in the provider account.",
    "example": "A trial ending October 28 with a seven-day buffer has an October 21 action date. A cancellation request is still pending until confirmation is recorded.",
    "limits": "No cancellations or reminders are sent. The action date is your planning choice, not a verified contractual deadline. Check time zones, billing cutoffs and confirmation in the provider account.",
    "steps": [
      "Copy the actual trial end date from your account.",
      "Choose a buffer after checking the service terms.",
      "Keep a reference to the terms or confirmation.",
      "Cancel through the provider when appropriate and mark Confirmed only with evidence."
    ],
    "features": [
      "Plan a manual trial-cancellation review before an entered trial end date. Track requested versus confirmed cancellation without claiming it is complete.",
      "Show record-level results with assumptions and review notes.",
      "Keep editable device saves and portable backups without an account."
    ],
    "workflow": "Check the record reference and scope before acting. Keep the original evidence alongside this worksheet, assign a next action and review it again after the real event. A saved plan does not update any external system.",
    "faq": [
      [
        "Does this take action for me?",
        "No. It calculates or organizes the information you enter. Decisions and updates to your real records remain manual."
      ],
      [
        "Can I restore a CSV or PDF?",
        "No. Use the JSON backup to restore editable fields. CSV and printed PDF are reports."
      ]
    ],
    "related": [
      [
        "software-renewal-decision-planner",
        "Review paid software renewals"
      ]
    ],
    "journal": "contract-renewal-workflow",
    "visual": [
      "Trial ends October 28",
      "7-day action buffer",
      "Review October 21"
    ]
  }
]
;
const prior=api.evaluate;api.configs.push(...configs);
const day=api.dateNumber,D=86400000,money=x=>({money:x}),round=x=>Math.round((x+Number.EPSILON)*100)/100;
api.evaluate=function(slug,state){const c=configs.find(c=>c.slug===slug);if(!c)return prior(slug,state);api.validateShape(slug,state,true);const t=state.top,rs=state.rows,now=day(t.asOf),metrics=[],warnings=[],extra=[];let headers=[],rows=[];const m=(label,value,format='number')=>metrics.push({label,value,format});const seen=new Set();for(const r of rs){const key=r.ref.trim().toLowerCase();if(seen.has(key))throw Error('Duplicate record reference: '+r.ref);seen.add(key);}
if(c.kind==='dead'){let flagged=0,value=0;headers=['Reference','SKU / location','Units','Inactivity days','Inventory cost','Review status','Next action'];rows=rs.map(r=>{const receipt=day(r.received),last=r.sale?day(r.sale):receipt;if(receipt>now||last>now||last<receipt)throw Error(r.ref+': receipt and last sale must be chronological and no later than review.');const days=(now-last)/D,v=+r.qty*api.cents(r.cost),flag=+r.qty>0&&days>=+t.threshold;if(flag){flagged++;value+=v;}return[r.ref,r.item,r.qty,days,money(v),flag?'Review inactive stock':+r.qty===0?'No stock held':'Below chosen threshold',r.action];});m('Flagged records',flagged);m('Flagged inventory cost',value,'money');}
if(c.kind==='returns'){let pending=0,released=0,rejected=0;headers=['Reference','SKU','Received','Returned','Inspected sellable','Rejected','Pending','Reviewer','Condition / action'];rows=rs.map(r=>{if(day(r.received)>now)throw Error(r.ref+': return receipt cannot be in the future.');const p=+r.qty-r.released-r.rejected;if(p<0)throw Error(r.ref+': sellable plus rejected exceeds returned units.');pending+=p;released+=+r.released;rejected+=+r.rejected;return[r.ref,r.item,r.received,r.qty,r.released,r.rejected,p,r.reviewer,r.note];});m('Pending units',pending);m('Recorded sellable units',released);m('Rejected units',rejected);}
if(c.kind==='clearance'){let rev=0,con=0;headers=['Reference','Item','Units','New unit price','Scenario revenue','Inventory cost','Selling fees','Other costs','Contribution'];rows=rs.map(r=>{const price=Math.round(api.cents(r.price)*(10000-api.cents(r.markdown))/10000),revenue=price*+r.qty,cost=api.cents(r.cost)*+r.qty,fee=Number((BigInt(revenue)*BigInt(api.cents(r.fee))+5000n)/10000n),fixed=api.cents(r.fixed),result=revenue-cost-fee-fixed;rev+=revenue;con+=result;if(result<0)warnings.push(r.ref+': negative contribution under these assumptions.');return[r.ref,r.item,r.qty,money(price),money(revenue),money(cost),money(fee),money(fixed),money(result)];});m('Scenario revenue',rev,'money');m('Scenario contribution',con,'money');}
if(c.kind==='allocation'){const shared=api.cents(t.shared);const lines=rs.map((r,i)=>{if(+r.qty<=0)throw Error(r.ref+': received quantity must be positive.');return{r,i,cost:api.cents(r.cost)*+r.qty,w:t.basis==='Units'?+r.qty:api.cents(r.cost)*+r.qty};});const total=lines.reduce((a,l)=>a+l.w,0);if(!Number.isSafeInteger(total))throw Error('Allocation scope is too large. Split the shipment.');if(total===0)throw Error('Allocation basis totals zero. Use units or enter merchandise costs.');let used=0;for(const l of lines){const numerator=BigInt(shared)*BigInt(l.w),denominator=BigInt(total);l.allocation=Number(numerator/denominator);l.rem=numerator%denominator;used+=l.allocation;}const ranked=[...lines].sort((a,b)=>a.rem===b.rem?a.i-b.i:a.rem>b.rem?-1:1);for(let i=0;i<shared-used;i++)ranked[i].allocation++;headers=['Reference','SKU','Received units','Merchandise total','Allocated charges','Landed line total','Rounded unit estimate'];rows=lines.map(l=>[l.r.ref,l.r.item,l.r.qty,money(l.cost),money(l.allocation),money(l.cost+l.allocation),money(Math.round((l.cost+l.allocation)/+l.r.qty))]);m('Allocated charges',lines.reduce((a,l)=>a+l.allocation,0),'money');m('Landed shipment total',lines.reduce((a,l)=>a+l.cost+l.allocation,0),'money');}
if(c.kind==='handoff'){let overdue=0,blocked=0,open=0;headers=['Job','Machine','Owner','Action date','Approval','Parts','Handoff','Days overdue','Review','Next action'];rows=rs.map(r=>{const active=r.status==='Open',late=active?Math.max(0,(now-day(r.due))/D):0,block=r.approval==='Pending'||r.parts==='Waiting';if(active){open++;if(late)overdue++;if(block)blocked++;}return[r.ref,r.machine,r.owner,r.due,r.approval,r.parts,r.status,late,active?(block?'Resolve blockers':'Review next action'):'Handoff recorded',r.action];});m('Open jobs',open);m('Overdue open jobs',overdue);m('Open jobs with blockers',blocked);}
if(c.kind==='rental'){let outstanding=0,overdue=0,hold=0,candidates=0;headers=['Rental reference','Asset','Return due','Dispatched','Returned','Outstanding','Held returned units','Inspection decision','Release candidates','Review note'];rows=rs.map(r=>{if(+r.returned>+r.out||+r.held>+r.returned)throw Error(r.ref+': returned must not exceed dispatched; held must not exceed returned.');const missing=+r.out-r.returned,release=r.release==='Recorded'?+r.returned-r.held:0;outstanding+=missing;if(day(r.due)<now)overdue+=missing;hold+=+r.held;candidates+=release;return[r.ref,r.asset,r.due,r.out,r.returned,missing,r.held,r.release,release,r.note];});m('Outstanding units',outstanding);m('Overdue outstanding units',overdue);m('Returned units on hold',hold);m('Release candidates after recorded inspection',candidates);}
if(c.kind==='calibration'||c.kind==='expiry'){let past=0,today=0,soon=0;headers=c.kind==='calibration'?['Reference','Instrument','Last calibration','Approved due date','Days to due','Record status','Date review','Schedule evidence']:['Reference','Item / lot','Recorded expiry','Days to date','Units held','Stock status','Date review','Next action'];rows=rs.map(r=>{const cal=c.kind==='calibration',dateValue=cal?r.due:r.expiry,n=day(dateValue),days=(n-now)/D,active=cal?r.status==='Active':r.status!=='Disposed';if(cal&&(day(r.last)>now||n<day(r.last)))throw Error(r.ref+': last calibration must not be future; due date must not precede it.');if(!cal&&r.status==='Disposed'&&+r.qty!==0)throw Error(r.ref+': disposed records must have zero held units.');const label=!active?'Inactive record':days<0?'Past recorded date':days===0?'Review today':days<=+t.window?'Within look-ahead':'Later';if(active){if(days<0)past++;else if(days===0)today++;else if(days<=+t.window)soon++;}return{n,data:cal?[r.ref,r.asset,r.last,r.due,days,r.status,label,r.source]:[r.ref,r.item,r.expiry,days,r.qty,r.status,label,r.action]};}).sort((a,b)=>a.n-b.n).map(x=>x.data);m('Active records past date',past);m('Active records due today',today);m('Active records within look-ahead',soon);warnings.push('A date status is not a safety or release decision. Verify the authoritative record and responsible approval.');}
if(c.kind==='tasks'){let ready=0,blocked=0,done=0;headers=['Step reference','Concrete step','Start cue','Minutes','Status','Finish signal / blocker'];rows=rs.map(r=>{if(r.status==='To do')ready+=+r.minutes;else if(r.status==='Blocked')blocked+=+r.minutes;else done++;return[r.ref,r.task,r.cue,r.minutes,r.status,r.note];});m('Ready work minutes',ready);m('Blocked work minutes',blocked);m('Remaining total minutes',ready+blocked);m('Ready work beyond window',Math.max(0,ready-+t.budget));m('Completed steps',done);}
if(c.kind==='trials'){let active=0,attention=0,upcoming=0;headers=['Reference','Service','Trial end','Chosen buffer days','Action date','Status','Review timing','Terms / confirmation'];rows=rs.map(r=>{const start=day(r.end)-+r.buffer*D;if(start<day('1900-01-01'))throw Error(r.ref+': action date must be in 1900 or later.');const open=r.status!=='Confirmed';if(open){active++;if(start<=now)attention++;else if(start<=now+ +t.window*D)upcoming++;}return{start,data:[r.ref,r.service,r.end,r.buffer,new Date(start).toISOString().slice(0,10),r.status,!open?'Confirmation recorded':start<now?'Action overdue':start===now?'Act today':start<=now+ +t.window*D?'Within look-ahead':'Later',r.source]};}).sort((a,b)=>a.start-b.start).map(x=>x.data);m('Trials without confirmed cancellation',active);m('Action due / overdue',attention);m('Upcoming actions',upcoming);}
for(const metric of metrics)if(metric.format==='money'&&!Number.isSafeInteger(metric.value))throw Error('Money total exceeds supported precision. Reduce the worksheet scope.');
return{metrics,headers,rows,extra,warnings,note:c.reportNote};};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
