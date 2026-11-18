A=[]
def add(id,slug,title,desc,text,sources):A.append(dict(id=id,slug=slug,title=title,desc=desc,text=text,sources=sources))
SEC=['SEC: Beginners’ Guide to Financial Statements','https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements']
IRS=['IRS Publication 334: 2025 Tax Guide for Small Business','https://www.irs.gov/publications/p334']
CLA=['Laundry Association: designing a business plan','https://www.laundryassociation.org/wp-content/uploads/2021/02/WhitePaper_BusinessPlan_Vol5No11_final.pdf']
NP=['Propel Nonprofits: managing restricted funds','https://propelnonprofits.org/resources/managing-restricted-funds/']
add('F05','small-business-financial-statements','Small Business Financial Statements: Three Reports, One Worked Example','Understand the income statement, balance sheet and cash-flow statement with a reconciled small-business example and links to free working templates.', '''## Which financial statements does a small business need?
An income statement explains revenue and expenses for a period. A balance sheet reports assets, liabilities and equity at a date. A cash-flow statement explains how cash changed during a period. Read them together: profit can rise while cash falls, and a loan can increase cash without creating sales.
The SEC also describes a statement of shareholders’ equity. This guide focuses on three connected reports for a fictional sole-owner workshop and shows the equity movement explicitly. It is a simplified teaching model, not a complete filing package or a determination of your accounting basis. Confirm your actual reporting requirements with your accountant or intended recipient.
## Choose records before choosing a template
Use reconciled bank records, a sales ledger, supplier records, inventory counts, an asset schedule and equity records. Label the entity, reporting period, currency and basis. Do not combine one business’s receipts with another’s liabilities or compare a month of sales with a year of expenses.
| Report | Scope | Source and question |
| Income statement | One completed month | Earned sales and incurred costs: was the period profitable? |
| Balance sheet | Opening and closing dates | Supported balances: what is owned, owed and invested? |
| Cash-flow statement | The same completed month | Reconciled movements: why did cash change? |
| Cash forecast | Future dates | Assumptions: can upcoming bills be met? |
A forecast is a different task. Use the [13-week cash forecast](/journal/cash-flow-forecast-template-example/) for expected collection and payment dates, not as a replacement for historical accounts.
## The workshop’s opening position
Assume a fictional USD workshop starts the month with cash $10,000, receivables $2,000, inventory $3,000 and equipment at cost $8,000 less accumulated depreciation $2,000. Assets total $21,000. Accounts payable are $2,000, loan principal is $5,000 and equity is $14,000. Assets equal liabilities plus equity: $21,000 = $7,000 + $14,000.
All sales in this example are on credit. There are no taxes, interest, sales taxes, returns, write-offs, noncash purchases, foreign exchange or other accounts. Those exclusions make the arithmetic teachable; they do not imply those items are irrelevant in a real business.
## Record the month’s activity once
Earned revenue is $12,000; customer collections are $11,000. Inventory purchases are $5,000, the stock count is $2,500 and supplier payments are $4,500. Other operating costs of $3,000 are paid, and depreciation is $200. Equipment costing $1,000 is bought for cash. New borrowing is $2,000, principal repaid is $500 and the owner withdraws $600.
COGS is opening inventory $3,000 + purchases $5,000 − closing inventory $2,500 = $5,500. Net income in this bounded example is $12,000 − $5,500 − $3,000 − $200 = $3,300. The equipment purchase is not expensed again in this illustration; depreciation is already listed separately.
## Reconcile profit to cash and the closing position
| Record | Calculation | Closing amount |
| Receivables | 2,000 + 12,000 − 11,000 | $3,000 |
| Payables | 2,000 + 5,000 − 4,500 | $2,500 |
| Net equipment | 8,000 + 1,000 − 2,000 − 200 | $6,800 |
| Loan principal | 5,000 + 2,000 − 500 | $6,500 |
| Equity | 14,000 + 3,300 − 600 | $16,700 |
Operating cash is $11,000 receipts − $4,500 supplier payments − $3,000 other operating payments = $3,500. Investing cash is −$1,000. Financing cash is $2,000 − $500 − $600 = $900. Net cash increase is $3,400, so closing cash is $13,400.
The indirect operating bridge reaches the same $3,500: net income $3,300 + depreciation $200 − receivables increase $1,000 + inventory decrease $500 + payables increase $500. Do not add the full closing working-capital balances; use the changes and examine other adjustments in actual books.
Closing assets are $13,400 cash + $3,000 receivables + $2,500 stock + $6,800 net equipment = $25,700. Liabilities and equity are $2,500 payables + $6,500 loan + $16,700 equity = $25,700. Both the cash bridge and the balance-sheet equation reconcile independently.
## Use the right free resource
Use the [income statement template](/tools/income-statement-template/) for period profit inputs and the [historical cash-flow statement](/tools/cash-flow-statement-template/) for classified cash movements. The [balance-sheet workbook](/journal/small-business-balance-sheet-template/) records dated balances. They are separate resources and do not synchronize or automatically produce a complete statement set.
The future financial-statement builder is not being advertised as available here. A planned collection must reuse the component definitions and pass reconciliation tests before any integrated capability is promised.
## Review exceptions before sharing
If closing cash differs from the bank, investigate the opening balance, missing transactions, transfers and cutoff first. If the balance sheet does not tie, inspect balances and signs rather than using equity as an unexplained plug. If profit and operating cash differ, inspect timing, inventory and noncash expenses before assuming either is wrong.
Give each exception a source reference, owner and review date. A reconciled model can still contain misclassified transactions; arithmetic checks do not audit the books. Keep a dated reviewed copy and ask the recipient which presentation, basis and supporting schedules are required.
## Common questions
Is the income statement the same as a bank statement? No: a bank statement records account movements; this accrual-style example also includes unpaid sales, inventory consumption and depreciation.
Do owner withdrawals reduce profit? In this sole-owner example they reduce cash and equity, separately from expenses. Other entities and compensation arrangements require their own treatment.
Can these tools create statutory accounts? No. They organize a limited set of entered figures. They do not certify compliance, calculate tax, post journal entries or verify source records.
''',[SEC])
add('F09','operating-cash-flow-example','Operating Cash Flow Formula: Direct and Indirect Examples','Calculate operating cash flow using direct receipts and payments, then reconcile from profit with a transparent small-business example.', '''## What operating cash flow measures
Operating cash flow measures cash generated or used by operating activities over a stated period. It is a flow, not the amount currently in the bank. Keep financing and equipment transactions separately identified before deciding whether operations are funding the business.
A business can report profit yet struggle to collect invoices. It can also have positive bank cash because a loan arrived, even while operations consume cash. This guide demonstrates both routes to an operating figure; it does not infer a business’s health from one number.
## Use the direct method with actual cash movements
For this simplified USD workshop, customers paid $11,000, suppliers received $4,500 and other operating payments were $3,000. Direct operating cash flow is $11,000 − $4,500 − $3,000 = $3,500.
These are completed-period cash amounts, not invoices issued or bills received. Reconcile each account and eliminate transfers inside the declared cash-account scope. Review interest, taxes and other classifications for the actual accounting framework; this small example excludes them rather than imposing a universal presentation.
| Movement | Included here? | Reason |
| Customer collections $11,000 | Operating inflow | Cash received for sales |
| Supplier payments $4,500 | Operating outflow | Cash paid for operating purchases |
| Other operating payments $3,000 | Operating outflow | Stated period payments |
| Equipment purchase $1,000 | Separate investing outflow | Long-lived equipment in this example |
| Loan proceeds $2,000 | Separate financing inflow | Funding rather than a sale |
| Owner withdrawal $600 | Separate financing outflow | Sole-owner withdrawal in this example |
## Reconcile the same result from profit
Start with net income, add back applicable noncash expenses, remove applicable non-operating effects, and adjust operating working-capital changes. A common short formula is net income + noncash adjustments − increase in operating assets + increase in operating liabilities, but it must be adapted to the actual accounts and presentation.
The workshop earned $12,000 revenue, incurred $5,500 COGS, paid and incurred $3,000 other operating costs, and recorded $200 depreciation. With no other items in this model, net income is $3,300. Receivables rise by $1,000, inventory falls by $500 and payables rise by $500.
| Indirect bridge | Effect on operating cash |
| Net income | +$3,300 |
| Depreciation added back | +$200 |
| Receivables increase | −$1,000 |
| Inventory decrease | +$500 |
| Operating payables increase | +$500 |
| Operating cash flow | $3,500 |
Depreciation is added back because it reduced the example’s profit without being a current cash payment. Do not treat that add-back as new cash from a customer. The inventory decrease means consumption exceeds purchases; the payables increase means part of purchases remains unpaid.
## Test a collection delay without inventing a lost sale
If $1,000 of the $11,000 collections arrives next month instead, direct operating cash falls to $2,500. If the sale is still valid and no other records change, net income remains $3,300 while closing receivables increase by another $1,000. The indirect bridge also falls by $1,000.
Carry only the confirmed unpaid amount into a revised [cash forecast](/journal/cash-flow-forecast-template-example/). Do not enter a new sale when the older invoice is collected. A delayed collection is not automatically bad debt; document the evidence and uncertainty separately.
## Distinguish operating cash, net cash and free cash flow
Add this example’s investing outflow of $1,000 and financing inflow of $900 to $3,500 operating cash: net cash rises $3,400. Starting cash of $10,000 therefore becomes $13,400. Operating cash $3,500 is neither that closing balance nor the total increase.
One commonly used free-cash-flow calculation subtracts capital expenditure from operating cash. For these stated inputs, that gives $2,500. Definitions and capital-expenditure scope vary; label the calculation rather than presenting it as a standardized cash amount that is automatically available for distribution.
Use the [historical statement worksheet](/tools/cash-flow-statement-template/) to organize the three activity classes. Read the [connected statements example](/journal/small-business-financial-statements/) for the matching balance-sheet and equity checks.
## Turn the result into a review task
Compare matched periods with the same account scope. Check whether cash improved because collections became faster, supplier payments were delayed or the business sold less stock than usual. A temporary increase in unpaid bills is not proof of sustainable operating improvement.
Record the source, date, owner and outstanding balance for large receivables. Review actual supplier due dates before treating unpaid invoices as a financing strategy. Use the [invoice collection schedule](/tools/invoice-collection-schedule/) for follow-up and the [financial dashboard](/journal/financial-dashboard-example/) to place the movement beside margins and commitments.
## Questions before relying on the formula
Can operating cash be negative while profit is positive? Yes, including when working capital absorbs cash. The bridge must explain the specific accounts; the sign alone does not diagnose the cause.
Does a principal repayment belong in the operating calculation above? It is separately classified as financing here; interest is excluded. Split real loan payments using lender records and the applicable reporting rules.
Can I use closing receivables instead of the change? Not in this reconciliation. Use comparable opening and closing records and inspect noncash or acquisition-related changes where applicable.
''',[SEC])
add('F26','cost-of-goods-sold-example','Cost of Goods Sold Formula: Inventory and COGS Worked Example','Work through opening inventory, net purchases and closing stock to calculate COGS, gross profit and margin without double-counting purchases.', '''## The cost of goods sold formula
For a simple resale model, cost of goods sold equals opening inventory + net inventory purchases + applicable acquisition costs − closing inventory. Use inventory cost rather than selling price. The formula measures the cost assigned to goods sold during the period, not every payment made to suppliers.
Manufacturing, services, inventory methods and tax rules can require different cost boundaries. This article uses one fictional reseller and a simplified periodic inventory example in USD. The IRS resource is a US Schedule C reference, not a universal bookkeeping policy or evidence your business must use this exact method.
## Gather four records before calculating
Take the opening stock value from the reviewed closing inventory of the previous period. Reconcile purchase invoices, returns and discounts for the current period. Identify freight or other acquisition costs included under the chosen policy. Finish with a dated physical count, adjusted for ownership, condition and cutoff.
Do not value ending stock at retail ticket price. Inspect goods in transit, consigned stock and customer-owned items separately so ownership is not assumed merely because goods are physically on a shelf. Record the method and ask your accountant how returns, write-downs and freight should be treated.
## Original fictional reseller example
| Inventory component | Example amount | How it is used |
| Opening inventory | $4,000 | Cost carried into the month |
| Purchases before returns | $7,200 | Supplier invoices in the period |
| Purchase returns | $200 | Deducted from purchases |
| Net purchases | $7,000 | 7,200 − 200 |
| Included inbound freight | $300 | Included once under the stated policy |
| Goods available at cost | $11,300 | 4,000 + 7,000 + 300 |
| Closing inventory | $3,100 | Supported ending cost value |
| COGS | $8,200 | 11,300 − 3,100 |
Assume earned net sales are $13,000. Gross profit is $13,000 − $8,200 = $4,800. Gross margin is $4,800 ÷ $13,000 × 100 = 36.92%, rounded to two decimals. This is not net profit: rent, administration, interest, tax and other expenses remain outside that gross-profit calculation.
If sales are zero, do not display a made-up margin percentage. Report the gross-profit amount and explain that the percentage denominator is zero. If your closing stock exceeds goods available under the entered model, investigate missing purchases, cutoff or valuation before accepting a negative cost result.
## Purchases, cash paid and consumption differ
Suppose the $7,300 of net purchases and freight includes $1,500 still unpaid at the end of the month. Current-period cash paid for those purchases is $5,800, assuming none was prepaid and no other payments are included. That is not the $8,200 COGS.
COGS also releases cost from opening inventory. Accounts payable explain unpaid purchases; receivables explain unpaid sales. A [cash-flow statement](/tools/cash-flow-statement-template/) follows actual payments, while the [income statement](/tools/income-statement-template/) uses the reconciled period COGS figure you enter. Neither automatically counts or values inventory.
## Show the effect of a stock-count error
In a disposable copy, incorrectly enter closing stock as $3,600 instead of $3,100. COGS falls by $500 to $7,700, and gross profit rises by $500 to $5,300. The higher margin is an error in this scenario, not improved trading.
Restore the verified count. Keep count sheets, cost evidence and approved adjustments with reviewer and date. If shrinkage, damaged goods or valuation issues are present, use their actual evidence and correct treatment instead of silently changing the stock value to reach a target profit.
## Keep owner-use inventory and returns visible
Track goods taken for personal use separately from genuine business sales and expenses. The applicable accounting and tax treatment depends on the facts. For US Schedule C, Publication 334 discusses excluding merchandise withdrawn for personal or family use from the relevant purchase cost; confirm current instructions and your records before filing.
A supplier return reduces the applicable purchase amount; a customer return has its own sales and inventory effects. Do not subtract a purchase return twice through both net purchases and a second adjustment line. Retain a clear reference to the credit document and period.
## Use COGS in a practical stock decision
Compare gross margin over matched periods only after the count, valuation and product mix are reviewed. A falling margin can come from price changes, purchase costs, sales mix, discounts or inventory errors; the total does not identify the cause.
Link the review to the [retail business plan](/journal/retail-store-business-plan-example/) and [sales and inventory workflow](/journal/sales-inventory-tracking-small-business/). Restocking decisions also need demand, lead time, shelf life and available cash, not only a gross-margin percentage.
## Common questions
Is freight always included? No universal treatment is asserted here. This example explicitly includes $300 inbound freight once; actual policies and tax rules need review.
Can a service business use this exact inventory formula? It may have direct service costs with a different structure. Define the service cost boundary before using a merchandise model.
Does the tool calculate tax COGS? No. The income worksheet accepts your reviewed COGS as one input; it does not select an inventory method or prepare a tax return.
''',[IRS,['SEC: small-business glossary','https://www.sec.gov/resources-small-businesses/glossary']])
add('O087','owner-draw-cash-planning','Owner Draw Cash Planning: A Dated Withdrawal Example','Plan a sole-owner withdrawal against dated cash commitments, collection risk and an explicit reserve without confusing drawings with profit or salary.', '''## Start with payment dates, not the profit headline
An owner draw is a withdrawal of value by an owner in the arrangement described here. This guide models a sole proprietor taking cash out of the business. It is not a rule for payroll, corporate dividends, partnership distributions or the tax treatment of a particular entity.
A profitable month does not tell you whether a withdrawal can be made before payroll and suppliers are paid. Start with reconciled cash, known commitments and realistic receipt dates. Confirm the legal, tax and accounting treatment of the actual withdrawal separately.
## Define what the cash review covers
Choose a short horizon that includes the next material obligations. State which accounts are included, which funds cannot be freely used, the reconciliation date and any minimum operating balance chosen for this specific plan. A reserve is an owner’s planning assumption, not a universal recommended percentage.
Keep expected receipts outside opening cash until their actual collection date. Exclude transfers between included accounts from consolidated inflows and outflows. Review payments beyond the chosen horizon as well: moving the cutoff does not remove an obligation.
## Original fictional two-week example
The owner begins with $12,000 reconciled cash. Of that, $2,000 has been set aside for a known upcoming obligation and is excluded from this draw decision. The remaining review starts from $10,000. Planned customer receipts are $4,000; listed business payments are $7,500. The owner chooses a $4,000 internal floor for the remaining operating cash.
| Date | Listed movement | Available review balance before draw |
| Day 0 | 12,000 cash less 2,000 excluded | $10,000 |
| Day 3 | Supplier payment 3,000 | $7,000 |
| Day 5 | Payroll and related listed payment 2,500 | $4,500 |
| Day 9 | Expected customer collection 4,000 | $8,500 |
| Day 12 | Other business commitments 2,000 | $6,500 |
The ending headroom over the $4,000 floor is $2,500. But withdrawing $2,500 on day 1 makes day 5 fall to $2,000, below the stated floor. The lowest pre-collection baseline is $4,500, leaving only $500 above the floor before day 9. Ending headroom is not permission to withdraw early.
A proposed $1,000 draw on day 10 leaves $5,500 at day 12 if the day 9 receipt arrives and all listed amounts are complete. Treat that as a conditional scenario, not an authorization or a calculated entitlement.
## Run the collection downside before deciding
If the $4,000 receipt moves beyond day 12, the no-draw balance at the horizon is $2,500, already below the $4,000 floor. The plan does not support the proposed day 10 withdrawal under that case. Investigate the collection date, omitted commitments and other genuine options instead of assuming supplier payments can be skipped.
Record the decision as: proposed amount; proposed date; bank cutoff; excluded funds; dated obligations; collection evidence; lowest balance; review owner; and next review date. A new payment or collection delay should reopen the decision.
## Drawings, expenses and profit remain separate
In this sole-owner illustration, the draw reduces cash and owner equity; it is not entered again as an operating expense. The [income statement worksheet](/tools/income-statement-template/) therefore does not ask for owner draws as an expense line. The [historical cash-flow statement](/tools/cash-flow-statement-template/) records the entered cash withdrawal in its financing section under the stated teaching model.
A business can earn profit and still lack cash to withdraw because customers have not paid, inventory has increased or debt principal is due. A loan can create bank cash without making a draw sensible or legally permitted. Review loan restrictions and applicable obligations with the relevant adviser.
## Put the decision into the existing cash workflow
Use the [weekly commitments planner](/tools/weekly-cash-commitments-planner/) for dated near-term movements and the [13-week forecast](/journal/cash-flow-forecast-template-example/) for the wider horizon. These separate tools do not synchronize with bank accounts or with each other.
Once a real transfer occurs, retain its reference and record it appropriately in the books. Review the [bookkeeping workflow](/journal/small-business-bookkeeping-workflow/) and check whether the closing equity supplied to a [balance sheet](/journal/small-business-balance-sheet-template/) already includes drawings. Subtracting the same draw again would double-count it.
## Questions owners should resolve
Can I draw a fixed percentage of revenue? Revenue alone omits costs, tax obligations, debt and collection timing. This guide does not prescribe a withdrawal ratio.
Is a tax reserve calculated here? No. The fictional $2,000 exclusion is an entered amount for an obligation, not a tax-rate estimate or a tax payment recommendation.
Can a company use the same journal entry? Do not assume so. Entity type, ownership arrangements, payroll rules and local law determine actual treatment. This is a cash-planning example for the stated sole-owner model.
''',[IRS,['Michigan State University: financial statements and owner draw','https://openbooks.lib.msu.edu/financialmanagement1ed/chapter/financial-statements/']])
add('O090','nonprofit-dashboard-example','Nonprofit Dashboard Example: Cash, Funding and Program Capacity','Build a nonprofit board dashboard with clear cash restrictions, funding concentration, program capacity and decisions supported by an original worked example.', '''## Give the board a decision, not a wall of percentages
A nonprofit dashboard is a compact review of mission delivery, resources and exceptions. Start with the question the board or manager must answer: can the next period’s work be delivered with the funds, people and evidence available?
Label every measure with the reporting window, definition, source, owner and last refresh. This example uses fictional USD balances and program counts. It is a management teaching view, not financial statements, a grant report or a measure of demonstrated social impact.
## Separate bank cash from donor restrictions and internal designations
Assume total reconciled cash is $80,000. Supporting records identify $30,000 of cash associated with unspent purpose-restricted funding, leaving $50,000 before other limitations. Of that $50,000, the board has internally designated $10,000 as a reserve, leaving $40,000 in this explicitly defined planning view.
Donor restrictions and internal board designations are different. Restricted net assets do not necessarily equal restricted cash: receivables, timing, conditions and other records can differ. The example assumes a separately reconciled restricted-cash amount; do not obtain it by simply subtracting the net-assets line from the bank balance.
| Dashboard card | Fictional calculation | Review action |
| Total cash | Bank and ledger reconcile to 80,000 | Check cutoff and outstanding items |
| Purpose-restricted cash in this model | Supported fund schedule 30,000 | Verify eligible use and remaining obligation |
| Planning cash after designation | 80,000 − 30,000 − 10,000 = 40,000 | Explain internal policy and other limitations |
| Monthly cash outflow used for coverage | Listed recurring payments 20,000 | Check nonrecurring and upcoming items |
| Static coverage illustration | 40,000 ÷ 20,000 = 2 months | Replace with a dated cash forecast before spending |
Two months is a static ratio under these chosen inputs, not a forecast of closure, a recommended reserve target or evidence that all $40,000 is available today. Dated payroll, debt, grants and receipts can change the decision.
## Connect funding concentration with collection timing
Assume the current-year funding table totals $240,000 of recognized revenue under the example’s stated basis, with $120,000 from the largest source. Its share is 50%. That figure is concentration, not the probability the funder will leave or the percentage already collected.
Keep outstanding grant receivables in a separate schedule. A $15,000 payment expected next month is not cash in the $80,000 bank balance. Read the agreement before deciding what is recognized, restricted, conditional, reimbursable or overdue. The dashboard cannot make those accounting determinations automatically.
## Show capacity and participation with honest denominators
Suppose a six-week program planned 120 places, enrolled 108 people and recorded 90 distinct participants attending at least once. Enrolment against places is 108 ÷ 120 = 90%. Participation among enrolled people is 90 ÷ 108 = 83.33%. Those percentages answer different questions.
If there were 360 total visits, that is a count of visits, not 360 unique people. State whether repeat visits are counted and how duplicates are removed. Attendance alone does not establish learning, health or employment outcomes; use an appropriate outcome definition and collection method when making those claims.
| Capacity measure | Original assumption | Meaning |
| Staff delivery hours available | 160 | Capacity after the stated exclusions |
| Delivery hours planned | 184 | Same six-week window |
| Capacity gap | 24 hours | Work needing a changed plan |
| Recorded program spending | $18,000 | Declared cost boundary, not all organisational costs |
| Cost per enrolled person | 18,000 ÷ 108 = $166.67 | Not cost per visit or impact achieved |
Check staff availability, safeguarding requirements, volunteer suitability and programme obligations before treating additional people as interchangeable capacity. The example does not prescribe service ratios.
## Write one action beside each exception
The finance owner verifies the $30,000 fund schedule and updates the dated forecast. The program lead resolves the 24-hour delivery gap through a documented schedule change or another feasible option. The fundraising lead reviews the largest funding source’s next decision date and the actual collection evidence.
Choose thresholds with the board’s policy and actual programme needs. Do not import universal red/amber/green limits. Show “not available” for missing or unreliable data rather than treating blank cells as zero performance.
## Keep the dashboard distinct from the treasurer’s report
This dashboard supports choices; a treasurer’s period report reconciles receipts, payments and balances. A future treasurer-report resource should link here without duplicating this page’s reporting intent. The [nonprofit business plan](/journal/nonprofit-business-plan/) holds the wider mission, operating and funding assumptions.
Use the [KPI dashboard guide](/journal/kpi-dashboard-guide/) for definitions and the [cash forecast](/journal/cash-flow-forecast-template-example/) for forward payment timing. These are separate manual resources, not a connected grant-accounting platform.
## Review before circulating
Confirm cutoffs, fund eligibility, approved cost boundaries and denominator consistency. Keep personal beneficiary details outside the board summary. Include a refresh date and an owner for unanswered questions. An attractive graphic does not replace reconciled records or the organisation’s governance and reporting obligations.
''',[NP,['National Council of Nonprofits: financial literacy for boards','https://councilofnonprofits.org/running-nonprofit/governance-leadership/financial-literacy-nonprofit-boards']])
add('B08','laundromat-business-plan','Laundromat Business Plan: Machines, Turns, Costs and Cash','Write a laundromat business plan using an original machine-utilisation model, startup funding schedule, downside case and practical evidence checklist.', '''## Build the plan around the site and machine economics
A laundromat business plan should explain who will use the site, why they will choose it, which services can be delivered, what the equipment and lease require, and how receipts cover operating costs and financing. A generic business description is not enough when machine availability, utility capacity and opening delays determine cash needs.
This is an original fictional self-service laundromat example in USD, not a startup-cost benchmark, lender-approved plan or projected return. Obtain local quotes, inspect actual sites and verify applicable permissions before relying on the model.
## Define the customer and service boundary
The fictional business serves nearby renters who need access to larger machines and convenient opening hours. The base model includes self-service washing and drying only. It excludes wash-and-fold, pickup, delivery, vending and commercial contracts so their labour and costs are not quietly assumed to be free.
Collect evidence before committing to a lease: observed competitor availability at several dayparts, customer interviews, parking/access, nearby housing patterns and quoted utility terms. Treat a busy visit as one observation, not proof of stable monthly demand. Record dates, sources and what could invalidate the assumption.
## Write a compact machine-based revenue model
| Base assumption | Fictional value | Calculation |
| Available washers | 20 | Assumes all 20 usable throughout the month |
| Washer turns per machine per day | 3 | Paid cycles, not unique customers |
| Model month | 30 days | Fixed horizon for this scenario |
| Average washer price | $5 | Before omitted taxes/fees |
| Washer revenue | $9,000 | 20 × 3 × 30 × 5 |
| Dryer revenue assumption | 60% of washer revenue | $5,400 |
| Total model revenue | $14,400 | 9,000 + 5,400 |
Dryer revenue as a percentage is a placeholder assumption, not an industry ratio. Replace it with dryer capacity, paid minutes/cycles and actual pricing when evidence is available. Confirm that peak demand and dryer throughput can support the assumed washer use.
One turn is one paid washer cycle. Three turns per machine per day does not mean three customers per day for the whole store. Explain refunds, promotions, outages and payment-system records when replacing the simple averages.
## Convert revenue into contribution and operating cash
Assume variable utilities and consumables are 25% of revenue in this bounded model: $3,600. Contribution is $10,800. Monthly fixed operating payments are rent $3,000, staffing $2,000, insurance/admin $600 and routine maintenance provision $400: $6,000 in total.
The modeled operating cash remainder is $4,800 before omitted taxes, interest, capital spending and owner compensation. A separately entered $1,500 monthly principal payment leaves $3,300 before those omitted items. Principal is kept outside operating expenses here. Obtain the actual loan schedule and split interest and principal correctly before using this as a real forecast.
Do not call this accounting net profit. Depreciation, accrual timing, equipment replacement and other real expenses are not modeled. Maintenance provision is a planning payment assumption here, not a calculation of accounting provisions.
## Test a lower utilisation case
Reduce washer turns from 3 to 2, leaving all other stated assumptions unchanged. Washer revenue is $6,000; assumed dryer revenue is $3,600; total is $9,600. Variable cost is $2,400 and contribution is $7,200. After fixed operating payments, $1,200 remains; after the separately entered $1,500 principal payment, the model is $300 short before omitted items.
With the chosen 25% variable share, operating payment break-even is $6,000 ÷ 0.75 = $8,000 total monthly revenue. Including the listed principal payment raises the cash threshold to $7,500 ÷ 0.75 = $10,000. Under the same dryer ratio and 30-day assumptions, that is about 2.08 washer turns per machine per day. These are scenario thresholds, not guaranteed attainable demand or full economic break-even.
## Build startup uses and funding without counting cash twice
| Startup use | Fictional amount |
| Equipment and installation | $90,000 |
| Fit-out and site works | $25,000 |
| Deposits, opening checks and launch items | $10,000 |
| Retained opening cash reserve | $20,000 |
| Total uses including retained reserve | $145,000 |
Assume owner funds of $45,000 and loan proceeds of $100,000 are actually available for this scenario. Funding totals $145,000. Paying the first three uses of $125,000 leaves $20,000 in cash; the reserve is not an additional payment to a supplier. Match every real quote with payment stages and financing release conditions.
Use the [startup budget template](/tools/startup-budget-template/) to separate spending from retained cash, then a [dated cash forecast](/journal/cash-flow-forecast-template-example/) for opening delays and actual payment timing. If rent and other commitments start before trading, model those pre-opening months explicitly instead of assuming revenue begins immediately.
## Resolve operational and site risks before opening
Check the lease’s permitted use, term, renewal, repair obligations and any guarantees with appropriate advisers. Verify water, drainage, electrical/gas capacity, ventilation, accessibility and relevant local permissions with the responsible authorities and qualified contractors. This article does not provide a universal permit list or determine compliance.
Document cleaning, refunds, outages, servicing, cash/payment reconciliation and emergency responsibilities. A machine that is unavailable reduces usable capacity. Retain supplier service terms and a replacement plan rather than assuming the initial equipment lasts indefinitely.
## Turn the model into a complete plan
Use sections for executive summary, customer evidence, site and competition, service/pricing, operations, startup funding, monthly scenarios, risks and launch milestones. Attach quote references, machine schedules and the evidence behind assumptions. The [business-plan template](/tools/business-plan-template/) provides a general structure; this article supplies the industry-specific reasoning.
Link startup uses, revenue assumptions and the downside case consistently. Explain who will verify the lease, quotations and collection/payment records, and what must be true before each irreversible commitment. The [business-plan guide](/journal/business-plan-guide/) helps organise the wider document.
## Common questions
Can I replace the fictional equipment amount with a market average? Obtain a quote for the actual mix, installation and site; an average can omit essential work and payment timing.
Is two turns per day always unprofitable? No. The result here follows the exact prices, costs, debt and dryer assumption shown above. Different inputs produce different thresholds.
Does this include an acquisition valuation? No. Buying an existing laundry requires separate verification of revenue, equipment condition, lease rights, liabilities and financing terms.
''',[CLA,['US SBA: plan your business','https://www.sba.gov/business-guide/plan-your-business']])
