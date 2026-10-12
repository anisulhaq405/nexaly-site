"""Original, bounded worksheets for the October 13 keyword workflow release."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def text(k,label,optional=False): return dict(key=k,label=label,type='text',maxLength=160,optional=optional)
def note(k,label,optional=True): return dict(key=k,label=label,type='textarea',maxLength=600,optional=optional)
def num(k,label,max=1000000,integer=False): return dict(key=k,label=label,type='number',min=0,max=max,step='1' if integer else '0.01',integer=integer)
def date(k,label): return dict(key=k,label=label,type='date')
def select(k,label,options): return dict(key=k,label=label,type='select',options=options)
TITLE=text('title','Worksheet name')
CURRENCY=select('currency','Currency',['USD','GBP','CAD','AUD','EUR','NZD'])
CONFIGS=[]
def add(slug,kind,name,category,color,fields,rowFields,top,rows,reportNote,maxRows=100):
 CONFIGS.append(dict(slug=slug,kind=kind,name=name,category=category,theme='workflow-'+kind,color=color,fields=[TITLE]+fields,rowFields=rowFields,sample=dict(top=dict(title='Fictional example: '+name,**top),rows=rows),reportNote=reportNote,maxRows=maxRows))
add('cash-flow-variance-report','variance','Cash Flow Variance Report','cashflow','#175c67',
 [CURRENCY,text('period','Period covered'),num('forecastOpening','Forecast opening cash'),num('actualOpening','Actual opening cash')],
 [text('label','Cash movement'),select('direction','Direction',['Receipt','Payment']),num('forecast','Forecast amount'),num('actual','Actual amount'),select('cause','Reason to investigate',['Timing','Amount','Unclassified']),text('owner','Follow-up owner'),date('review','Follow-up date'),note('action','Evidence and next action')],
 dict(currency='USD',period='One completed week',forecastOpening='1000',actualOpening='1000'),
 [dict(label='Customer collection',direction='Receipt',forecast='1500',actual='1200',cause='Timing',owner='Owner',review='2026-10-16',action='Confirm whether the remaining 300 is still collectible.'),dict(label='Supplier payment',direction='Payment',forecast='800',actual='900',cause='Amount',owner='Owner',review='2026-10-16',action='Compare the final invoice with the quote.')],
 'Forecast closing = forecast opening + forecast receipts − forecast payments. Actual closing uses actual cash. Cash impact is actual minus forecast for receipts and forecast minus actual for payments. Reasons are entered manually; this is not a statutory cash flow statement.')
add('monthly-business-budget-variance','budget','Monthly Business Budget Variance','cashflow','#6a401e',
 [CURRENCY,text('period','Budget month')],
 [text('label','Budget line'),select('type','Line type',['Revenue','Variable cost','Fixed cost']),num('budget','Budget amount'),num('actual','Actual amount'),text('owner','Review owner'),date('review','Review date'),note('action','Explanation and next action')],
 dict(currency='USD',period='October 2026'),
 [dict(label='Sales',type='Revenue',budget='10000',actual='9000',owner='Owner',review='2026-11-02',action='Check orders and average order value separately.'),dict(label='Direct costs',type='Variable cost',budget='4000',actual='3800',owner='Owner',review='2026-11-02',action='Lower total cost does not establish lower unit cost.'),dict(label='Overhead',type='Fixed cost',budget='3000',actual='3200',owner='Owner',review='2026-11-02',action='Identify the additional 200 before renewing spending.')],
 'Amount variance = actual − budget. Percentage variance = amount variance ÷ budget × 100, undefined for a zero budget. Modeled operating remainder = revenue − variable costs − fixed costs. Cash dates, tax, financing and inventory valuation are outside this worksheet.')
add('printable-planner-builder','builder','Printable Planner Builder','personal','#714075',
 [select('paper','Paper size',['US Letter','A4','A5']),select('layout','Layout',['Daily','Weekly']),date('start','Date on daily page / date within week'),select('weekStart','Week starts on',['Monday','Sunday']),num('startHour','Daily start hour (0–23)',23,True),num('endHour','Daily end hour (0–23)',23,True)],
 [text('section','Writing section name'),num('lines','Writing lines',6,True)],
 dict(paper='US Letter',layout='Daily',start='2026-10-13',weekStart='Monday',startHour='8',endHour='18'),
 [dict(section='Three priorities',lines='3'),dict(section='Next actions',lines='3'),dict(section='Notes',lines='3')],
 'Builds one undated-style daily or dated weekly printable page. Daily ranges may cross midnight and are limited to 16 hourly slots; start and end must differ. Use one to three writing sections, one to six lines each, at most 12 lines overall. Browser PDF printing is not a GoodNotes file or reminder app.',3)
add('monthly-teacher-lesson-planner','teacher','Monthly Teacher Lesson Planner','homeschool','#335548',
 [text('month','Teaching month (YYYY-MM)'),date('asOf','Preparation review date')],
 [text('lesson','Lesson / group'),date('date','Lesson date'),date('prep','Preparation due date'),text('owner','Preparation owner'),note('materials','Materials / preparation task',False),select('status','Preparation status',['Not started','In progress','Ready'])],
 dict(month='2026-10',asOf='2026-10-13'),
 [dict(lesson='Grade 4 fractions',date='2026-10-16',prep='2026-10-12',owner='Teacher',materials='Print fraction strips and check the worked example.',status='In progress'),dict(lesson='Grade 4 number review',date='2026-10-19',prep='2026-10-16',owner='Teacher',materials='Prepare three practice questions.',status='Ready')],
 'Lists only lessons in the entered month. Preparation due date must be on or before the lesson date; earlier-month preparation is allowed. Overdue means prep date before review date and status not Ready. No curriculum approval, attendance compliance or reminders are provided.')
add('content-production-capacity-planner','production','Content Production Capacity Planner','content','#1d4d84',
 [text('objective','One content objective'),date('start','First production day'),date('end','Last production day'),num('daily','Production hours available each working day',24),select('days','Working days',['Weekdays','Every day'])],
 [text('item','Deliverable'),date('date','Production day'),num('hours','Production and review hours',24),text('owner','Production owner'),text('reviewer','Review owner'),select('status','Status',['Planned','In progress','Complete']),note('action','Destination / next action')],
 dict(objective='Explain one product and publish two useful demonstrations',start='2026-10-13',end='2026-10-16',daily='3',days='Weekdays'),
 [dict(item='Product explanation',date='2026-10-13',hours='2',owner='Writer',reviewer='Editor',status='Planned',action='Link to the relevant product page.'),dict(item='Short demonstration',date='2026-10-13',hours='2',owner='Creator',reviewer='Editor',status='In progress',action='Check the demonstration before posting.')],
 'Remaining planned load includes Planned and In progress hours, excludes Complete items, and groups by production date. It does not spread work automatically or publish content. Allocate a multi-day deliverable as separate dated work blocks. Completed hours remain visible for recordkeeping.')
add('marketing-campaign-budget-planner','campaign','Marketing Campaign Budget Planner','content','#7c342d',
 [CURRENCY,text('objective','One campaign objective'),num('ceiling','Total test budget'),date('review','Next review date')],
 [text('channel','Channel / test'),num('planned','Planned spend'),num('actual','Actual spend'),num('inquiries','Observed inquiries',100000,True),num('customers','Confirmed customers',100000,True),note('rule','Decision rule / attribution note',False)],
 dict(currency='USD',objective='Test one service offer with attributable inquiries',ceiling='600',review='2026-10-30'),
 [dict(channel='Email test',planned='200',actual='180',inquiries='12',customers='3',rule='Use a distinct inquiry tag; check lead quality.'),dict(channel='Search test',planned='300',actual='320',inquiries='8',customers='1',rule='Review actual inquiries before allocating the unassigned budget.')],
 'Unallocated planned budget = ceiling − planned spend. Remaining actual budget = ceiling − actual spend. Cost per inquiry/customer uses actual spend divided by that entered count, undefined at zero. Channel counts may overlap; no automatic attribution, ROI or sales forecast is inferred.')
add('one-page-business-plan-builder','lean','One-Page Business Plan Builder','agency','#4c496d',
 [text('customer','Specific customer'),note('problem','Problem and existing workaround',False),note('offer','Offer and service boundary',False),note('economics','Revenue and cost assumptions',False),date('review','Plan review date')],
 [text('assumption','Assumption to test'),note('evidence','Evidence observed'),note('test','Next test',False),text('owner','Test owner'),date('due','Test due date'),select('status','Evidence status',['Untested','Supported','Contradicted'])],
 dict(customer='Local service businesses launching a website',problem='Owners lose time assembling a clear landing-page brief.',offer='One landing-page design with two revision rounds; development excluded.',economics='Illustrative package 1250; 20 delivery hours; verify actual demand and cost.',review='2026-11-13'),
 [dict(assumption='A prospect will pay 1250 for this package',evidence='Three conversations; no paid sale yet.',test='Offer one paid pilot with written scope.',owner='Owner',due='2026-10-23',status='Untested'),dict(assumption='Delivery fits in 20 hours',evidence='No completed pilot time log.',test='Track the pilot delivery and revision hours.',owner='Designer',due='2026-11-06',status='Untested')],
 'Prints the core customer, problem, offer and economics with an evidence log. A one-page summary is compact with up to three short assumptions; additional or long entries can require more pages. Supported is a user-entered status, not independent proof. This is not a funding application.',20)
add('service-business-financial-projections','projections','Service Business Financial Projections','cashflow','#234b59',
 [CURRENCY,num('opening','Opening cash')],
 [date('month','Month starting (first day)'),num('sales','Billed service revenue'),num('expense','Operating expense incurred'),num('depreciation','Noncash depreciation'),num('receipts','Cash collected'),num('paid','Operating cash paid'),num('principal','Debt principal paid'),num('funding','New loan / owner capital received'),num('draw','Owner cash withdrawal')],
 dict(currency='USD',opening='2000'),
 [dict(month='2026-10-01',sales='6000',expense='4000',depreciation='200',receipts='5000',paid='4200',principal='300',funding='0',draw='1000'),dict(month='2026-11-01',sales='6500',expense='4200',depreciation='200',receipts='6000',paid='4000',principal='300',funding='0',draw='1000')],
 'Operating result = billed service revenue − incurred operating expenses − noncash depreciation. Closing cash = prior cash + collections + new funding − operating cash paid − debt principal − owner withdrawals. Months must be consecutive and start on day 1. Excludes inventory, tax, a balance sheet and loan approval; include applicable interest within operating expense and cash-paid inputs.',12)
add('coffee-shop-daily-operating-plan','coffee','Coffee Shop Daily Operating Plan','operations','#75492e',
 [CURRENCY,num('hours','Opening hours',24),num('capacity','Maximum feasible orders per hour',10000),num('orders','Expected daily orders',100000,True),num('ticket','Average order value'),num('unitCost','Ingredients / packaging per order'),num('other','Other daily operating cost'),num('slow','Slower-day orders',100000,True)],
 [text('role','Staffing role / shift'),num('hours','Paid shift hours',24),num('rate','Hourly employer cost')],
 dict(currency='USD',hours='8',capacity='20',orders='120',ticket='8',unitCost='2.5',other='180',slow='80'),
 [dict(role='Morning shift',hours='6',rate='20'),dict(role='Afternoon shift',hours='6',rate='20')],
 'Daily sales = orders × average order value. Remainder = sales − order ingredients/packaging − entered staffing − other costs. Capacity = opening hours × entered feasible orders/hour, a planning ceiling rather than proven throughput. Staffing is unchanged in the slower-day scenario. Not net profit, cash timing or a full cafe feasibility model.')
add('construction-milestone-cash-schedule','construction','Construction Milestone Cash Schedule','cashflow','#78521a',
 [CURRENCY,date('start','Project start date'),date('end','Project end date'),num('opening','Opening project cash')],
 [text('label','Milestone / payment'),date('date','Expected cash date'),select('direction','Direction',['Receipt','Payment']),num('amount','Cash amount'),select('certainty','Status',['Expected','Confirmed']),note('action','Dependency / next action')],
 dict(currency='USD',start='2026-10-13',end='2026-11-13',opening='1000'),
 [dict(label='Customer deposit',date='2026-10-13',direction='Receipt',amount='2000',certainty='Confirmed',action='Confirm collection before purchasing materials.'),dict(label='Materials',date='2026-10-14',direction='Payment',amount='2500',certainty='Confirmed',action='Supplier payment date.'),dict(label='Labour',date='2026-10-16',direction='Payment',amount='1200',certainty='Expected',action='Confirm the payroll date.'),dict(label='Milestone collection',date='2026-10-23',direction='Receipt',amount='3000',certainty='Expected',action='Confirm approval and collection timing.')],
 'Closing cash = opening + all entered receipts − all entered payments, including Expected records. The confirmed-only-receipts downside retains all payments. Lowest balance groups same-day movements and includes opening cash; it does not identify intraday shortages. No contract entitlement or legal payment right is inferred.')
add('trucking-trip-cost-worksheet','trucking','Trucking Trip Cost Worksheet','operations','#4b555e',
 [CURRENCY,num('loaded','Loaded miles'),num('empty','Empty miles'),num('revenue','Trip revenue excluding pass-through tax'),num('mpg','Expected miles per gallon',100),num('fuel','Fuel price per gallon'),num('maintenance','Maintenance allowance per total mile',100),date('paidOn','Expected customer collection date')],
 [text('label','Nonfuel trip cost'),num('amount','Cost amount'),date('date','Cash payment date')],
 dict(currency='USD',loaded='400',empty='100',revenue='1500',mpg='6.25',fuel='4',maintenance='0.2',paidOn='2026-10-30'),
 [dict(label='Driver cost',amount='300',date='2026-10-16'),dict(label='Tolls',amount='50',date='2026-10-16'),dict(label='Fixed operating allocation',amount='100',date='2026-10-16')],
 'Total miles = loaded + empty. Fuel cost = total miles ÷ mpg × fuel price. Modeled trip cost includes fuel, maintenance allowance and entered nonfuel costs. Cost/mile always uses total miles. Allowances and fixed allocations are not necessarily cash paid on this trip. The report dates only entered nonfuel payments, not fuel or maintenance cash timing.')
(ROOT/'assets/js/keyword-workflows-configs.json').write_text(json.dumps(CONFIGS,indent=2)+'\n')
print('Wrote',len(CONFIGS),'distinct worksheet configurations')
