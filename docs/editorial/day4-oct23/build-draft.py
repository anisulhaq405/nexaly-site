from pathlib import Path
import re, json, textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('NexalySans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('NexalySansBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT.parent/'day4-content-review'
OUT.mkdir(exist_ok=True)
DL=ROOT/'assets/downloads'

def pdf_pack(filename,title,subtitle,fields,example):
    c=canvas.Canvas(str(DL/filename),pagesize=(612,792))
    c.setTitle(title);c.setAuthor('NexalyPlanner')
    for page,filled in enumerate([False,True],1):
        c.setFillColor(HexColor('#203d4a'));c.setFont('NexalySansBold',23)
        c.drawString(42,744,title)
        c.setFont('NexalySans',10);c.drawString(42,723,subtitle)
        c.setFont('NexalySansBold',9)
        c.drawString(42,700,'FICTIONAL FILLED EXAMPLE' if filled else 'BLANK WORKSHEET')
        y=680
        for label,height in fields:
            c.setFillColor(HexColor('#203d4a'));c.setFont('NexalySansBold',10)
            c.drawString(42,y,label)
            c.setStrokeColor(HexColor('#bbcace'));c.line(42,y-8,570,y-8)
            if filled:
                c.setFont('NexalySans',10);yy=y-24
                for line in simpleSplit(example.get(label,''),'NexalySans',10,515):
                    assert yy>y-height+5,(label,'field overflow')
                    c.drawString(45,yy,line);yy-=14
            else:
                for yy in range(int(y-29),int(y-height+10),-18):
                    c.setStrokeColor(HexColor('#e0e7e9'));c.line(45,yy,566,yy)
            y-=height
        assert y>=65,(filename,y)
        c.setFillColor(HexColor('#536870'));c.setFont('NexalySans',8)
        c.drawString(42,44,'NexalyPlanner | Free static worksheet | Print one page or annotate a copy in a compatible PDF app.')
        c.drawRightString(570,30,f'{page} / 2');c.showPage()
    c.save()

studyfields=[('Subject and topic',46),('Learning objective and source',60),('Key concepts',64),('Explain it in your own words',70),('Worked question and checked answer',80),('Recall questions without notes',65),('Weak area and correction',62),('Next revision date and task',55)]
studyexample={
'Subject and topic':'Mathematics | Adding fractions with different denominators',
'Learning objective and source':'Add 3/4 and 1/8 and explain the common denominator. Source: your assigned lesson and checked course examples.',
'Key concepts':'Equivalent fractions represent the same value. Use a common denominator before adding numerators.',
'Explain it in your own words':'Rename quarters as eighths: 3/4 = 6/8. The pieces must have the same size before their counts can be added.',
'Worked question and checked answer':'3/4 + 1/8 = 6/8 + 1/8 = 7/8. Check: 0.75 + 0.125 = 0.875, which equals 7/8.',
'Recall questions without notes':'Why use eighths here? What is 1/2 + 1/4? After trying: 1/2 = 2/4, so the sum is 3/4.',
'Weak area and correction':'First attempt added denominators. Correction: rename both fractions, keep the common denominator and add numerators.',
'Next revision date and task':'Choose your next available session. Solve 2/3 + 1/6 without notes, then check: 4/6 + 1/6 = 5/6.'}
pdf_pack('study-guide-template.pdf','Study guide template','One topic per sheet | Page 1 blank | Page 2 original worked example',studyfields,studyexample)
dailyfields=[('Date and fixed commitments',64),('Main outcome and first action',76),('Time blocks and transitions',100),('Up to two additional tasks',65),('Buffer and tasks to defer',70),('End of day and next action',80)]
dailyexample={
'Date and fixed commitments':'Fictional workday | Client call 11:00-11:30 | Leave desk at 12:00.',
'Main outcome and first action':'Send the revised quote. First action: open the draft and check the two missing line prices.',
'Time blocks and transitions':'09:00-10:00 quote; 10:00-10:15 break; 10:15-10:45 expense entry; 10:45-11:00 buffer; 11:00-11:30 call; 11:30-11:45 follow-up; 11:45-12:00 shutdown.',
'Up to two additional tasks':'Enter one batch of expenses (30 min). Send the call follow-up (15 min).',
'Buffer and tasks to defer':'Keep 15 minutes unassigned before the call. Defer the optional 45-minute filing task; it does not fit this morning.',
'End of day and next action':'Record actual progress. If the quote waits for a reply, note the question and follow-up time instead of marking it sent.'}
pdf_pack('daily-planner-template.pdf','Daily planner template','One day per sheet | Page 1 blank | Page 2 original worked example',dailyfields,dailyexample)
for filename,title,fields,ex in [('study-guide-template.txt','STUDY GUIDE TEMPLATE',studyfields,studyexample),('daily-planner-template.txt','DAILY PLANNER TEMPLATE',dailyfields,dailyexample)]:
    lines=[title,'Free plain-text worksheet. Save a working copy. No automatic calculations or reminders.','', 'BLANK COPY']
    for label,_ in fields:lines += [label+':','', '']
    lines+=['FICTIONAL FILLED EXAMPLE','']
    for label,_ in fields:lines += [label+':',ex[label],'']
    (DL/filename).write_text('\n'.join(lines))
(DL/'exam-study-schedule-template.txt').write_text('''EXAM STUDY SCHEDULE - MANUAL TEN-DAY STARTER
Exam subject/date/time/location:
Confirmed coverage and course source:
Other commitments and available time:

10 days before | Confirm coverage; attempt a short diagnostic | example 25 min
9 days before | Practice Topic A; check uncertain steps | example 30 min
8 days before | Practice Topic B; record questions | example 30 min
7 days before | Recall Topic A without notes, then correct | example 25 min
6 days before | Flexible catch-up or rest | optional
5 days before | Mix selected A/B questions | example 30 min
4 days before | Resolve specific gaps using course support | example 25 min
3 days before | Attempt an appropriate practice section | example 40 min
2 days before | Review errors and difficult steps | example 25 min
1 day before | Light review and confirm exam logistics | example 20 min

For each row add: actual date, start/end time, task, output, observed gap, next action.
The nine stated durations total 250 minutes, excluding optional catch-up, breaks and setup.
These are illustrative durations, not required study time or a grade prediction.
Fill dates manually; this text file does not recalculate, alert or synchronize.
Check all subjects together before assigning the same time twice.
''')

sections={
'daily-planner-complete-guide':('daily-template-download','''<section id="daily-template-download"><h2>Download a free daily planner template</h2><p><a href="/assets/downloads/daily-planner-template.pdf" download>Download the daily planner PDF: blank sheet and filled example</a> · <a href="/assets/downloads/daily-planner-template.txt" download>Download the editable text version</a></p><p>The PDF has two US Letter portrait pages. Print page one for a blank worksheet or page two for the fictional morning example. It has fixed commitments, a main outcome, time blocks, two optional tasks, buffer and a closing review. It is a static document, not a calendar app. The text copy can be edited in a plain-text editor; it does not set reminders.</p><p>Keep one clean original. Write your date and appointments before adding work. If you annotate the PDF, save a named copy and reopen it to check your notes before relying on it. Choose a <a href="/journal/hourly-planner-best-free-digital-layouts/">detailed hourly layout</a> when you need finer time slots; use the <a href="/journal/weekly-planner-2026-free-templates/">weekly planner</a> for work that does not belong today.</p><figure><img src="/assets/img/resource-previews/daily-planner-template.webp" alt="Actual blank daily planner worksheet with fixed commitments, first action, time blocks and review fields" width="850" height="1100" loading="lazy"><figcaption>Actual blank worksheet from page one of the download.</figcaption></figure></section>'''),
'monthly-planner-free-templates':('place-monthly-dates','''<section id="place-monthly-dates"><h2>Place dates correctly before planning the month</h2><p>The undated download starts on Sunday. Find the weekday of the first day in your calendar, write 1 in that column, then continue across the rows. Leave cells before day 1 and after the last date blank. A month with 31 days starting on Saturday needs six rows: day 1 uses Saturday, days 2–29 use four complete weeks, and days 30–31 use Sunday and Monday in the sixth row. The supplied sheet provides six rows; do not squeeze the last dates into the wrong week.</p><p>Use your own confirmed dates rather than copying the article's illustrative month. Put a presentation deadline on the month view, a draft review in the <a href="/journal/weekly-planner-2026-free-templates/">weekly plan</a>, and the next writing action in the <a href="/journal/daily-planner-complete-guide/">daily planner</a>. These paper/PDF views do not synchronize. If the deadline changes, inspect the related milestones rather than moving the final date alone.</p><h3>Check capacity before carrying a goal forward</h3><p>Suppose four available sessions are 45 minutes each: that gives 180 planned minutes. Two 60-minute draft sessions and one 30-minute review use 150 minutes, leaving 30. An additional 90-minute task does not fit the same allocation. Move it, reduce its scope or choose another window; adding its name to a goals box does not create the missing time.</p><p>At month-end, keep the outcome and next action distinct. “Portfolio not finished” is less useful than “Two samples selected; write the third caption in the next available session.” Keep the original deadline if it is still real, and flag any conflict that needs a decision.</p></section>'''),
'exam-study-schedule-template':('connect-study-guide','''<section id="connect-study-guide"><h2>Turn a study-guide gap into a scheduled task</h2><p><a href="/assets/downloads/exam-study-schedule-template.txt" download>Download the editable ten-day study schedule text</a>. Enter calendar dates and session times manually. The nine stated durations total 250 minutes before optional catch-up, setup and breaks; this is an example allocation, not a required preparation period.</p><p>A <a href="/tools/study-guide-template/">study guide template</a> holds the concept, your explanation, a worked question and what you still need to check. This schedule gives that work a time. Keep the confirmed topic in the guide and enter a specific action in the calendar instead of copying the entire guide into each time block.</p><p>For example, a fraction question reveals that you added denominators. Make the next task “rename two fraction pairs with a common denominator, solve them and check each answer.” After the session, record the actual result in the guide. If the method remains uncertain, write the question for course support; the fact that you spent 25 minutes does not establish understanding.</p><h3>Choose one place for each kind of record</h3><p>Keep assessed submission deadlines in the <a href="/journal/college-assignment-tracker/">assignment tracker</a>, exam dates in your calendar and remaining practice questions in the guide. Record actual session progress once, then update the next action. The downloadable text, PDF and site planners are separate resources; they do not exchange your entries automatically.</p></section>'''),
'adhd-planner-for-adults':('write-a-small-task','''<section id="write-a-small-task"><h2>Fill the to-do layout with an action you can recognize</h2><p>Use the existing <a href="/assets/downloads/adhd-daily-planning-layout.pdf" download>free daily planning PDF</a> to write one main task before adding optional work. “Sort everything” has no clear stopping point. “Open the receipts folder and identify the three missing receipts” gives you something observable to begin and a place to stop.</p><div class="table-wrap"><table><caption>Fictional entries in the existing worksheet</caption><thead><tr><th>Field</th><th>Example entry</th></tr></thead><tbody><tr><td>Main task</td><td>Prepare the receipts for the monthly review.</td></tr><tr><td>First action</td><td>Open the folder and list the missing receipt dates.</td></tr><tr><td>Fixed anchor</td><td>Call at 11:00; stop the task early enough to prepare.</td></tr><tr><td>Parking area</td><td>Replace printer ink later; it is not part of this action.</td></tr><tr><td>Restart step</td><td>Resume at the first unchecked date on the list.</td></tr></tbody></table></div><p>If a task is blocked by another person, write the request and follow-up point. Do not keep rewriting “finish receipts” when the next action is actually “ask for the missing invoice.” If the day changes, carry forward the next useful action rather than all unfinished notes.</p><p>The PDF and printable HTML are handwriting layouts; they do not run a timer, send reminders or save typed tasks. For one larger task, the <a href="/tools/executive-function-task-breakdown/">free task-breakdown worksheet</a> offers a separate editable planning workflow. Compare its actual controls before choosing it. These are organizational options, not treatment claims.</p></section>'''),
'homeschool-schedule-multiple-ages':('prepare-support-rotation','''<section id="prepare-support-rotation"><h2>Prepare the handoff between two supported lessons</h2><p>A rotation needs a finish instruction as well as a starting time. Before helping Child A, set out Child B's suitable familiar task, explain what to do if a question arises and confirm that the available supervision fits the activity. If that is not possible, change the arrangement rather than labeling the task independent on paper.</p><p>In a fictional 60-minute window, allow 20 minutes for Child A's supported lesson, five minutes to record the stopping point and switch materials, 20 minutes for Child B's lesson, and ten minutes for a shared closing review. That uses 55 minutes and leaves five minutes of buffer. These durations are scheduling examples; they do not prescribe a child's attention span, lesson length or legal attendance record.</p><p>If the first lesson takes 30 minutes, the original sequence would need 65 minutes. Before continuing, decide what can change. The closing review might move, or the second lesson may need a separate suitable window. Keep an accurate note of each child's attempted work and next step rather than silently marking the original plan complete.</p><h3>Keep three records separate</h3><p>The family schedule shows who needs support. A child's lesson note shows the objective, work attempted and next action. The <a href="/journal/homeschool-attendance-tracker/">attendance guide and printable sheet</a> record actual participation under the applicable requirements. A scheduled block alone does not establish attendance.</p><p>For an older learner preparing for an assessment, the <a href="/tools/study-guide-template/">study-guide worksheet</a> can hold a concept and practice questions; the <a href="/journal/exam-study-schedule-template/">exam schedule</a> can hold the practice time. Use only what fits the learner's course and support needs. The <a href="/planners/digital-homeschool-planner/">Digital Homeschool Planner</a> is a separate paid product to review if you need child-specific records.</p></section>'''),
'content-calendar-clothing-brand':('check-clothing-production','''<section id="check-clothing-production"><h2>Check production time before promising the next post</h2><p>A useful clothing calendar connects the product, customer question, asset, owner and publication date. Before committing a post, confirm that the garment is available, the measurements are checked and the destination page matches the product shown. A stock change can make an otherwise finished clip unsuitable.</p><div class="table-wrap"><table><caption>Fictional production budget for three clothing posts</caption><thead><tr><th>Work</th><th>Minutes</th><th>Output to check</th></tr></thead><tbody><tr><td>One shared filming setup</td><td>40</td><td>Measurement, fabric and styling clips</td></tr><tr><td>Edit three clips at 20 minutes each</td><td>60</td><td>Three reviewed video files</td></tr><tr><td>Caption, link and availability check at 10 minutes each</td><td>30</td><td>Three ready post records</td></tr><tr><td>Total</td><td>130</td><td>10 minutes remain in a 140-minute window</td></tr></tbody></table></div><p>A fourth post needing another 30 minutes would bring the total to 160, exceeding that window by 20. Reduce the commitment or find another genuine production slot. Reusing a setup saves work, but it does not make editing and product checks disappear. Use the <a href="/tools/content-production-capacity-planner/">free content-capacity planner</a> to test your own estimates.</p><h3>Give a changed product an explicit decision</h3><p>If the featured dress sells out before publication, hold the sales post until its destination is accurate. You might replace it with an available product or a clearly explained styling lesson, but do not keep a purchase CTA that suggests unavailable stock can be ordered. Record the changed asset, link and review owner before rescheduling.</p><p>Keep the clothing calendar focused on selected posts. Use the <a href="/journal/content-marketing-plan-template-capacity/">content marketing plan guide</a> for audience, objectives and capacity decisions, then check each selected post with the <a href="/tools/content-publishing-checklist/">publishing checklist</a>. The <a href="/planners/content-marketing-planner/">Content Marketing Planner</a> is a separate offline planning product; none of these article examples publishes to social accounts.</p></section>''')}

for slug,(sid,section) in sections.items():
    p=ROOT/'journal'/slug/'index.html';s=p.read_text().replace(section,'')
    # Add practical content before FAQ, keeping existing script behavior and anchors.
    anchor=re.search(r'<h2\b[^>]*>[^<]*(?:FAQs|[Ff]requently asked questions|Common questions)',s)
    if anchor:s=s[:anchor.start()]+section+s[anchor.start():]
    else:s=s.replace('</article>',section+'</article>',1)
    if slug=='daily-planner-complete-guide':
        s=s.replace('Imagine a weekday with a 9:00 a.m. start, a 30-minute commute, and a 5:00 p.m. finish.','Imagine a weekday with an 8:30 a.m. desk start after a 30-minute commute, and a 5:00 p.m. finish.')
        # Resource access belongs before the instructional essay.
        s=s.replace(section,'',1);s=s.replace('<h2',section+'<h2',1)
    if slug=='exam-study-schedule-template':
        s=s.replace('Use the ten-day schedule below as a starting point. Set your exam date to your own. The dates for the ten-day example recalculate from that input.','Use the ten-day schedule below as a starting point. Download the editable text schedule below and enter dates manually relative to your confirmed exam date. This page does not recalculate dates or send reminders.')
        s=s.replace('The workbook is a starter plan for one exam. Duplicate the sheet for another exam only after checking the combined workload on your main calendar.','The on-page table and downloadable text are starter plans for one exam. Make a separate copy for another exam only after checking the combined workload on your main calendar.')
        old='Download an exam study schedule template with an editable ten-day plan. Organize practice, review, flexible time and exam logistics before finals.'
        s=s.replace(old,'Use a ten-day exam study schedule with an editable text download, realistic time checks and missed-session examples. Enter dates manually for your course.')
        s=s.replace('to deadline-aware allocation within entered daily capacity.','for deadline-aware allocation within entered daily capacity.')
    if slug=='monthly-planner-free-templates':s=s.replace('a tax payment on April 15','a software renewal on April 15').replace('tax payment, family event','software renewal, family event')
    # A prepared draft retains historical publication/modification metadata until release.
    p.write_text(s)

studybody='''<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/tools/">Free planners</a> / Study guide template</nav><p>DRAFT RESOURCE · NOT PUBLISHED</p><h1>Free Study Guide Template With a Filled Example</h1>
<p>A study guide template organizes what you need to explain, practice and check for one topic. This free worksheet has a learning objective, key concepts, an explanation in your own words, a worked question, recall prompts, weak areas and a next revision task. Start with the blank PDF or editable text copy, then compare the filled fraction example.</p>
<p class="po-downloads"><a href="/assets/downloads/study-guide-template.pdf" download>Download PDF: blank and filled example</a><a href="/assets/downloads/study-guide-template.txt" download>Download editable text template</a></p><p>Two US Letter portrait PDF pages: page one is blank and page two is a fictional worked example. No signup. The PDF is static, without fillable form fields; the text file can be edited in a plain-text editor. No Excel, Word or native Google Sheets file is supplied.</p>
<figure><img src="/assets/img/resource-previews/study-guide-template.webp" alt="Actual blank study guide worksheet with learning objective, explanation, worked question, recall prompts and revision fields" width="850" height="1100" fetchpriority="high"><figcaption>Actual blank sheet from the PDF. The download also contains the completed fraction example.</figcaption></figure>
<nav aria-label="On this page"><ul><li><a href="#choose-format">Choose a format</a></li><li><a href="#fill-guide">Fill the study guide</a></li><li><a href="#worked-example">Worked fraction example</a></li><li><a href="#subject-choices">Adapt it to a subject</a></li><li><a href="#guide-vs-schedule">Guide or schedule?</a></li><li><a href="#save-print">Save and print</a></li><li><a href="#faq">Questions</a></li></ul></nav>
<h2 id="choose-format">Choose the blank PDF or editable text copy</h2><p>Choose the PDF when you want a repeatable handwriting layout. Print page one, or annotate a copy in an app that supports PDF markup. Choose the text file when you want to type, add more questions or enlarge a section. Its headings are the same, but a text editor does not preserve the PDF's page layout.</p><p>Keep a blank original and make one working copy per topic. Name it with the subject and topic so it can be found later. Neither file uploads your notes, generates answers, tracks progress automatically or synchronizes with another planner.</p>
<h2 id="fill-guide">How to fill out a study guide</h2><ol><li><strong>Confirm the topic and source.</strong> Use the syllabus, assigned material or instructor's current directions. Keep the scope narrow enough to explain and check.</li><li><strong>Write an observable learning objective.</strong> “Add two fractions with different denominators and explain the method” is more useful than “know fractions.”</li><li><strong>Select the concepts that support that objective.</strong> Keep definitions short and accurate. Include the source page or lesson reference so an uncertain point can be checked.</li><li><strong>Explain the idea in your own words.</strong> Try without notes, then compare with the assigned material. Mark uncertainty rather than polishing an explanation that you cannot yet support.</li><li><strong>Work a question and check the answer.</strong> Show the reasoning, units where relevant and the source used to check it. An answer without a method may hide the step you need to practice.</li><li><strong>Add recall prompts.</strong> Cover the explanation, attempt a prompt and check afterward. Keep a correction next to the specific error.</li><li><strong>Choose the next revision task.</strong> Put a realistic session in your calendar and name the question or explanation to revisit.</li></ol>
<p>Cornell's <a href="https://lsc.cornell.edu/how-to-study/studying-for-and-taking-exams/effective-study-strategies/" rel="noopener">Learning Strategies Center</a> describes recalling material from memory and returning to it across separate sessions. The worksheet provides room to record those attempts and corrections; it does not prescribe an interval or predict a grade.</p>
<h2 id="worked-example">Filled example: explain 3/4 + 1/8</h2><p>The original example uses one small mathematics topic. The objective is to add fractions with different denominators and explain why their units must match. The concept is equivalent fractions: 3/4 can be renamed 6/8 without changing its value.</p><div class="table-wrap"><table><thead><tr><th>Step</th><th>Working</th><th>What to check</th></tr></thead><tbody><tr><td>Rename</td><td>3/4 = 6/8</td><td>Multiply numerator and denominator by the same number.</td></tr><tr><td>Add</td><td>6/8 + 1/8 = 7/8</td><td>The denominator stays eight because the pieces are eighths.</td></tr><tr><td>Check</td><td>0.75 + 0.125 = 0.875 = 7/8</td><td>The original values and resulting fraction agree.</td></tr></tbody></table></div><p>A weak-area note might say, “I added denominators on my first attempt.” The correction is specific: rename the fractions, keep the common denominator and add the numerators. A later prompt is 2/3 + 1/6. Try it before checking the answer: 4/6 + 1/6 = 5/6.</p><p>The completed sheet also asks why eighths are useful and gives 1/2 + 1/4 as another practice question, with 3/4 as its checked answer. These examples illustrate how to record reasoning and errors. They are not a complete unit, an assessed answer key or a measure of mastery.</p>
<h2 id="subject-choices">Adapt the fields without copying a whole textbook</h2><p>For a history topic, the worked-question field can hold a claim supported by a course source, while recall prompts ask you to explain causes or compare interpretations. Keep dates and quotations tied to the assigned material. For science, use a labeled process or worked question with the units required by the course. For literature, record an argument and the passage that supports it rather than a list of unsupported themes.</p><p>If the topic will not fit, split it into distinct objectives. Do not shrink an entire chapter into unreadable text. Leave questions that need instructor clarification visible; an unanswered question is a useful next action.</p>
<h2 id="guide-vs-schedule">A study guide and a study schedule do different jobs</h2><p>The guide holds the material and your attempts to explain it. A <a href="/journal/exam-study-schedule-template/">study schedule</a> holds when you will work on it. The <a href="/journal/college-assignment-tracker/">assignment tracker</a> holds coursework due dates and next actions. Keep those references connected without treating them as synchronized files.</p><p>For example, the guide records an error in fraction addition; the schedule allocates a practice session; the tracker records a separate assessed worksheet due date. Completing the practice block does not submit that worksheet. If you want a broader offline system, review the <a href="/planners/ai-student-planner/">AI Student Planner</a> and its <a href="/guides/ai-student-planner/">user guide</a>. It is a separate paid product, and the free downloads do not depend on it.</p>
<h2 id="save-print">Save a working copy and check the print layout</h2><p>Download the PDF or text file to your device and confirm the filename before editing. For a blank paper copy, print PDF page one in portrait orientation on US Letter. Use the print preview for A4 or a different printer; scaling can change writing space. Page two is the completed example, not a blank form.</p><p>If you annotate a PDF, save a named copy, close it and reopen it to confirm your annotations remain. For text, save your edits as a separate .txt file. Keep a backup where you can find it. The site does not recover a deleted or unsaved local copy.</p>
<h2 id="faq">Frequently asked questions</h2><h3>Is this study guide template free?</h3><p>Yes. The PDF and text copy are direct downloads without a purchase or email signup. Paid student planners are separate.</p><h3>Can I type directly in the PDF?</h3><p>It has no fillable form fields. You can use a compatible annotation app, or type in the supplied text file. Save and reopen a test copy before using it for important notes.</p><h3>Is this a Google Docs or Word template?</h3><p>No native document or copy link is supplied. The editable download is plain text, and the formatted version is PDF. You can paste your text into your preferred editor, but its formatting will depend on that editor.</p><h3>How many topics belong on one sheet?</h3><p>Start with one objective that can be explained and checked. Split a broad topic when its concepts or questions need separate practice.</p><h3>Does completing it mean I am ready for the exam?</h3><p>No. Check your answers against the course material, inspect remaining gaps and follow the instructor's requirements. A filled page does not establish understanding or guarantee a result.</p>'''
template=(ROOT/'tools/packing-slip-template/index.html').read_text()
template=re.sub(r'<main\b[^>]*>.*?</main>',lambda _: '<main class="po-resource">'+studybody+'</main>',template,count=1,flags=re.S)
template=re.sub(r'<script id="nexaly-seo".*?</script>','',template,flags=re.S)
template=re.sub(r'<meta property="article:(?:published|modified)_time"[^>]*>','',template)
template=re.sub(r'(<link rel="canonical" href=")[^"]+',r'\g<1>https://nexalyplanner.com/tools/study-guide-template/',template)
template=re.sub(r'(<meta property="og:url" content=")[^"]+',r'\g<1>https://nexalyplanner.com/tools/study-guide-template/',template)
template=re.sub(r'<title>.*?</title>','<title>Free Study Guide Template PDF + Filled Example | NexalyPlanner</title>',template)
for tag in ['og:title','twitter:title']:
    template=re.sub(r'(<meta (?:property|name)="'+tag+r'" content=")[^"]+',r'\g<1>Free Study Guide Template PDF + Filled Example',template)
desc='Download a free study guide template in PDF or editable text. Includes a blank sheet, a filled fraction example, recall questions and revision instructions.'
for tag in ['description','og:description','twitter:description']:
    template=re.sub(r'(<meta (?:property|name)="'+tag+r'" content=")[^"]+',lambda m:m[1]+desc,template)
template=template.replace('packing-slip-template-cover.webp','study-guide-template.webp').replace('Actual packing slip workbook with fictional partial-shipment quantities','Actual blank study guide worksheet')
template=template.replace('<head>','<head><meta name="robots" content="noindex,follow">',1)
p=ROOT/'tools/study-guide-template/index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(template)
# Put the proposed resource in the draft Free Planners directory, preserving the 50 browser-planner count.
p=ROOT/'tools/index.html';s=p.read_text();needle='<li><a href="/tools/packing-slip-template/">'
assert needle in s
if 'href="/tools/study-guide-template/"' not in s:
    s=s.replace(needle,'<li><a href="/tools/study-guide-template/">Study guide template: PDF and editable text</a> — one topic, recall prompts, a blank sheet and a filled example.</li>'+needle,1)
p.write_text(s)
register=[]
for slug,(sid,_) in sections.items():register.append({'path':f'journal/{slug}/index.html','section':sid,'status':'draft only'})
register.append({'path':'tools/study-guide-template/index.html','section':'new resource','status':'draft only; noindex'})
(OUT/'content-register.json').write_text(json.dumps(register,indent=2))
print('Prepared six guide revisions, one noindex study-guide resource, two PDF packs and three text downloads. No remote write.')
