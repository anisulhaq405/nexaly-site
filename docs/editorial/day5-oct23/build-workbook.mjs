import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root='/workspace/scratch/3fe6f21d7a25/nexaly-day5-draft';
const out='/workspace/scratch/3fe6f21d7a25/day5-content-review';
const wb=Workbook.create();
const inputs=[9,10,11,12,13,14,18,19,20,21,25,26,27,28];
const example={9:6000,10:2500,11:4000,12:3500,13:1000,14:0,18:2200,19:800,20:3000,21:0,25:7500,26:2000,27:500,28:0};
const labels={9:'Cash',10:'Accounts receivable, net',11:'Inventory',12:'Equipment at cost',13:'Less accumulated depreciation',14:'Other assets',18:'Accounts payable',19:'Current debt portion',20:'Long-term debt, excluding current',21:'Other liabilities',25:'Contributed capital',26:'Retained earnings or deficit',27:'Less owner withdrawals',28:'Other equity, signed'};
const refs={9:'Bank reconciliation',10:'Receivables listing',11:'Inventory records',12:'Equipment register',13:'Depreciation schedule',14:'No other assets in example',18:'Unpaid supplier bills',19:'Debt schedule, current portion',20:'Debt schedule, remaining balance',21:'No other liabilities in example',25:'Capital records',26:'Prior earnings and current results',27:'Owner withdrawal records',28:'No other equity in example'};
for(const name of ['Blank','Filled example']){
 const s=wb.worksheets.add(name),filled=name==='Filled example';
 s.showGridLines=false;s.tabColor=filled?'#536870':'#203D4A';
 s.getRange('B2:E44').format.font={name:'Arial',size:10,color:'#203D4A'};
 s.getRange('B2:E44').format.rowHeight=23;
 s.getRange('B2:B44').format.columnWidth=37;
 s.getRange('C2:C44').format.columnWidth=22;
 s.getRange('D2:D44').format.columnWidth=39;
 s.getRange('E2:E44').format.columnWidth=26;
 s.getRange('B2').values=[['Small business balance sheet']];s.getRange('B2').format.font={name:'Arial',size:14,bold:true};s.getRange('B2:E2').format.rowHeight=30;
 for(const [cell,value] of [['B3','Business'],['B4','As of date'],['B5','Currency'],['B34','Basis and scope']])s.getRange(cell).values=[[value]];
 s.getRange('C3').values=[[filled?'Example Workshop':null]];
 s.getRange('C4').values=[[filled?new Date('2026-10-23T00:00:00Z'):null]];s.getRange('C4').setNumberFormat('mm/dd/yy');
 s.getRange('C5').values=[['USD']];s.getRange('C34').values=[[filled?'Simplified accrual example':null]];
 s.getRange('C34').format.wrapText=true;s.getRange('B34:E34').format.rowHeight=32;
 for(const range of ['C3:C5','C34']){s.getRange(range).format.fill='#FFF3CF';s.getRange(range).format.font.color='#0000FF';}
 s.getRange('C5').dataValidation={rule:{type:'list',values:['USD','GBP','CAD','AUD','EUR','NZD']}};
 s.getRange('D3').values=[['Amounts use the selected currency; no conversion.']];s.getRange('D3').format.wrapText=true;s.getRange('B3:E3').format.rowHeight=31;
 s.getRange('E6').formulas=[['=IF(AND(LEN(TRIM(C3))>0,ISNUMBER(C4),C4>=1,C4<=109939,MOD(C4,1)=0,OR(C5="USD",C5="GBP",C5="CAD",C5="AUD",C5="EUR",C5="NZD"),LEN(TRIM(C34))>0),"Ready","Complete header")']];
 s.getRange('B7:E7').values=[['Account','Amount','Source reference','Input review']];s.getRange('B7:E7').format={fill:'#203D4A',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:26};
 for(const [row,label] of [[8,'ASSETS'],[17,'LIABILITIES'],[24,'EQUITY']]){s.getRange('B'+row).values=[[label]];s.getRange('B'+row+':E'+row).format.fill='#E8EFF3';s.getRange('B'+row).format.font.bold=true;}
 for(const row of inputs){
  s.getRange('B'+row).values=[[labels[row]]];s.getRange('C'+row).values=[[filled?example[row]:null]];s.getRange('D'+row).values=[[filled?refs[row]:null]];
  s.getRange('C'+row).format.fill='#FFF3CF';s.getRange('C'+row).format.font.color='#0000FF';
  s.getRange('D'+row).format.font.color='#0000FF';
  s.getRange('D'+row).setNumberFormat('  @');
  s.getRange('B'+row).setNumberFormat('  @');
  const negative=[26,28].includes(row)?'FALSE':`C${row}<0`;
  const ready=row===13?'IF(AND(ISNUMBER(C12),C13>C12),"Exceeds equipment cost","Ready")':'"Ready"';
  s.getRange('E'+row).formulas=[[`=IF(ISBLANK(C${row}),"Enter 0 or amount",IF(NOT(ISNUMBER(C${row})),"Use a number",IF(ABS(C${row}-ROUND(C${row},2))>0.00000001,"Use two decimals",IF(${negative},"Use a positive amount",${ready}))))`]];
  s.getRange('E'+row).conditionalFormats.add('notContainsText',{text:'Ready',format:{fill:'#FDE9E7',font:{color:'#A52222'}}});
 }
 const valid='AND(E6="Ready",COUNTIF(E9:E14,"Ready")=6,COUNTIF(E18:E21,"Ready")=4,COUNTIF(E25:E28,"Ready")=4)';
 const totals={15:['Total assets','SUM(C9:C12)-C13+C14'],22:['Total liabilities','SUM(C18:C21)'],29:['Total equity','SUM(C25:C26)-C27+C28'],31:['Liabilities plus equity','C22+C29'],32:['Difference: assets minus funding','ROUND(C15-C31,2)']};
 for(const [row,[label,f]] of Object.entries(totals)){
  s.getRange('B'+row).values=[[label]];s.getRange('C'+row).formulas=[[`=IF(${valid},${f},"")`]];
  s.getRange('B'+row+':C'+row).format.font.bold=true;s.getRange('B'+row+':C'+row).format.borders={bottom:{style:'thin',color:'#B8C6CE'}};
 }
 s.getRange('B33').values=[['Balance check']];s.getRange('C33').formulas=[[`=IF(NOT(${valid}),"Complete inputs",IF(C32=0,"Balanced","Check difference"))`]];
 s.getRange('C33').conditionalFormats.add('containsText',{text:'Check difference',format:{fill:'#FDE9E7',font:{color:'#A52222',bold:true}}});
 s.getRange('C32').conditionalFormats.add('cellIs',{operator:'notEqual',formula:0,format:{fill:'#FDE9E7',font:{color:'#A52222',bold:true}}});
 s.getRange('C9:C32').setNumberFormat('#,##0.00;(#,##0.00);"-"');s.getRange('C32').setNumberFormat('0.00;(0.00);0.00');
 s.getRange('B36').values=[['Use the worksheet']];s.getRange('B36').format.font.bold=true;
 const lines=[['Duplicate the blank tab before entering data.','Use one reporting date, currency and basis.'],['Enter every amount; enter 0 when not applicable.','Yellow cells are editable; formulas stay intact.'],['Use positive depreciation and withdrawal deductions.','A deficit or other equity adjustment may be signed.'],['Do not repeat current debt in long-term debt.','Keep evidence references with source records.'],['Print Selection B2:C34 in portrait.','Preview and fit to one page in your spreadsheet app.'],['Blank checks do not establish a balanced statement.','A zero difference does not prove completeness.'],['Example figures are fictional teaching inputs.','Definitions: SEC financial statement guide.']];
 lines.forEach((r,i)=>{s.getRange('B'+(37+i)).values=[[r[0]]];s.getRange('D'+(37+i)).values=[[r[1]]];s.getRange('B'+(37+i)+':E'+(37+i)).format.rowHeight=32;s.getRange('B'+(37+i)).format.wrapText=true;s.getRange('D'+(37+i)).format.wrapText=true;});
 wb.notes.add({id:name+':D43',target:{cell:{sheetName:name,sheetId:s.sheetId,address:'D43'}},authorId:'',createdAt:'',body:{plainText:'Source for basic statement definitions: SEC, Beginners’ Guide to Financial Statements, https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements . All example amounts are NexalyPlanner fictional teaching figures.'}});
}
const s=wb.worksheets.getItem('Filled example');
const read=cell=>s.getRange(cell).values[0][0];
const results=[];
function test(label,fn){wb.recalculate();const got=fn();if(!got)throw Error('Failed: '+label+' '+JSON.stringify({C4:read('C4'),E6:read('E6'),E9:read('E9'),E13:read('E13'),C15:read('C15'),C22:read('C22'),C29:read('C29'),C32:read('C32'),C33:read('C33')}));results.push({case:label,pass:true});}
test('15000 = 6000 + 9000',()=>read('C15')===15000&&read('C22')===6000&&read('C29')===9000&&read('C32')===0&&read('C33')==='Balanced');
s.getRange('C9').values=[[6100]];test('100 mismatch visible',()=>read('C32')===100&&read('C33')==='Check difference');s.getRange('C9').values=[[6000]];
s.getRange('C9').values=[[6000.01]];test('one cent mismatch visible',()=>read('C32')===0.01&&read('C33')==='Check difference');s.getRange('C9').values=[[6000]];
s.getRange('C10').values=[[null]];test('missing amount blocks totals',()=>read('C15')===''&&read('C33')==='Complete inputs');s.getRange('C10').values=[[2500]];
s.getRange('C10').values=[['2500']];test('text amount rejected',()=>read('C15')==='');s.getRange('C10').values=[[2500]];
s.getRange('C9').values=[[-1]];test('negative cash rejected',()=>read('C15')==='');s.getRange('C9').values=[[6000]];
s.getRange('C13').values=[[3501]];test('depreciation cannot exceed equipment cost',()=>read('C15')==='');s.getRange('C13').values=[[1000]];
s.getRange('C26').values=[[-500]];test('retained deficit remains signed',()=>read('C29')===6500&&read('C32')===2500);s.getRange('C26').values=[[2000]];
s.getRange('C9').values=[[6000.001]];test('hidden fractional cents rejected',()=>read('C15')==='');s.getRange('C9').values=[[6000]];
s.getRange('C34').values=[[null]];test('missing basis blocks totals',()=>read('C15')==='');s.getRange('C34').values=[['Simplified accrual example']];
s.getRange('C9').values=[[5000]];s.getRange('C20').values=[[2000]];test('1000 debt payment changes cash and debt equally',()=>read('C15')===14000&&read('C22')===5000&&read('C33')==='Balanced');s.getRange('C9').values=[[6000]];s.getRange('C20').values=[[3000]];
test('example restored',()=>read('C15')===15000&&read('C33')==='Balanced');
const b=wb.worksheets.getItem('Blank');if(b.getRange('C33').values[0][0]!=='Complete inputs')throw Error('Blank must not claim Balanced');results.push({case:'blank is incomplete, not healthy zero',pass:true});
wb.recalculate();
await fs.mkdir(out,{recursive:true});
await fs.writeFile(out+'/balance-sheet-tests.json',JSON.stringify(results,null,2));
const inspected=await wb.inspect({kind:'table',range:"'Filled example'!B8:E33",include:'values,formulas',tableMaxRows:28,tableMaxCols:4,maxChars:10000});await fs.writeFile(out+'/balance-sheet-inspect.ndjson',inspected.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},summary:'formula error scan'});await fs.writeFile(out+'/balance-sheet-errors.ndjson',errors.ndjson);
for(const [name,file] of [['Blank','balance-sheet-blank.png'],['Filled example','balance-sheet-example.png']]){
 const img=await wb.render({sheetName:name,range:'B2:E43',scale:1.4,format:'png'});await fs.writeFile(out+'/'+file,new Uint8Array(await img.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(wb)).save(root+'/assets/downloads/small-business-balance-sheet-template.xlsx');
const imported=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/assets/downloads/small-business-balance-sheet-template.xlsx'));
const checkSheet=imported.worksheets.getItem('Filled example');
imported.recalculate();
if(checkSheet.getRange('C15').values[0][0]!==15000||checkSheet.getRange('C33').values[0][0]!=='Balanced')throw Error('Export/import baseline changed');
checkSheet.getRange('C9').values=[[6100]];imported.recalculate();
if(checkSheet.getRange('C32').values[0][0]!==100||checkSheet.getRange('C33').values[0][0]!=='Check difference')throw Error('Export/import recalculation failed');
await fs.writeFile(out+'/balance-sheet-roundtrip.json',JSON.stringify({engine:'Artifact Tool XLSX export/import',baseline:15000,changed_difference:100,pass:true,native_excel_verified:false},null,2));
console.log(JSON.stringify({tests:results.length,file:'small-business-balance-sheet-template.xlsx',status:'draft only'}));
