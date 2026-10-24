import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile,FileBlob} from '@oai/artifact-tool';
const root=process.env.NEXALY_SITE_ROOT||fileURLToPath(new URL('../../../',import.meta.url));
const out=root+'/docs/editorial/day7-three-forms/qa';
const configs=JSON.parse(await fs.readFile(root+'/assets/js/business-forms-configs.json','utf8'));
const tests=[];
for(const c of configs){
 const wb=Workbook.create();
 for(const name of ['Blank','Filled example']){
  const s=wb.worksheets.add(name),filled=name==='Filled example',sample=c.sample;
  s.showGridLines=false;s.tabColor=c.color;
  s.getRange('A1:J36').format={font:{name:'Arial',size:10,color:'#203D4A'},rowHeight:26};
  const widths=c.kind==='expense'?[15,24,30,18,15,15,15,19,3,25]:[18,28,24,14,18,18,24,22,3,25];
  widths.forEach((v,i)=>s.getRangeByIndexes(0,i,36,1).format.columnWidth=v);
  s.getRange('A1:H1').merge();s.getRange('A1').values=[[c.name+' | '+(filled?'Fictional example':'Blank form')]];s.getRange('A1:H1').format={fill:c.color,font:{name:'Arial',size:18,bold:true,color:'#FFFFFF'},rowHeight:42};
  s.getRange('A2:H2').merge();s.getRange('A2').values=[['NexalyPlanner | Yellow inputs, gray calculations | One currency per form']];
  const labels=c.kind==='expense'?['Report reference','Claimant','Issue date','Period end','Business','Purpose','Reviewer','Manual status','Review date','Related reference']:c.kind==='requisition'?['Request reference','Requester','Request date','Need-by date','Department','Justification','Reviewer','Manual status','Review date','Resulting PO ref']:['Order reference','Prepared by','Order date','Delivery / collection date','Customer','Agreed details','Reviewer','Manual status','Review date','Payment reference'];
  const keys=['reference','person','date','due','party','notes','reviewer','decision','reviewDate','related'];
  keys.forEach((key,i)=>{
   const row=3+Math.floor(i/2),left=i%2===0,label=left?'A':'E',cell=left?'C':'G';
   s.getRange(label+row).values=[[labels[i]]];s.getRange(label+row).format.font.bold=true;
   s.getRange(cell+row+':'+(left?'D':'H')+row).merge();
   let value=filled?sample[key]:key==='decision'?'Draft':null;
   if(['date','due','reviewDate'].includes(key)&&value)value=new Date(value+'T00:00:00Z');
   s.getRange(cell+row).values=[[value]];s.getRange(cell+row).format.fill='#FFF3CF';s.getRange(cell+row).format.font.color='#0000FF';s.getRange(cell+row).format.wrapText=true;
   if(['date','due','reviewDate'].includes(key))s.getRange(cell+row).setNumberFormat('yyyy-mm-dd');
  });
  s.getRange('A8').values=[['Currency']];s.getRange('C8').values=[['USD']];s.getRange('C8').format.fill='#FFF3CF';s.getRange('C8').dataValidation={rule:{type:'list',values:['USD','CAD','GBP','EUR','AUD','NZD']}};
  s.getRange('E8:H8').merge();s.getRange('E8').values=[['Manual statuses do not authorize or send anything.']];s.getRange('E8').format.wrapText=true;s.getRange('A8:H8').format.rowHeight=32;
  s.getRange('G6').dataValidation={rule:{type:'list',values:['Draft','In review','Approved','Declined','Confirmed']}};
  s.getRange('A10:H10').values=[c.headers];s.getRange('A10:H10').format={fill:c.color,font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:32,wrapText:true};
  s.getRange('J10').values=[['Input review']];s.getRange('J10').format.font.bold=true;
  for(let i=0;i<10;i++){
   const row=11+i,r=filled?sample.rows[i].map(x=>x===''?null:x):Array(8).fill(null);
   if(c.kind==='expense'){
    if(r[0])r[0]=new Date(r[0]+'T00:00:00Z');for(const col of [5,6])if(r[col]!==null)r[col]=Number(r[col]);
   }else{for(const col of [3,4])if(r[col]!==null)r[col]=Number(r[col]);}
   s.getRange(`A${row}:H${row}`).values=[r];s.getRange(`A${row}:H${row}`).format={fill:'#FFF3CF',font:{name:'Arial',size:10,color:'#0000FF'},wrapText:true,rowHeight:36,borders:{bottom:{style:'thin',color:'#D8E2E1'}}};
   const amount=col=>`AND(ISNUMBER(${col}${row}),${col}${row}>=0,${col}${row}<=1000000000,ABS(${col}${row}-ROUND(${col}${row},2))<0.00000001)`;
   if(c.kind==='expense'){
    s.getRange('A'+row).setNumberFormat('yyyy-mm-dd');s.getRange(`F${row}:G${row}`).setNumberFormat('#,##0.00;(#,##0.00);0.00');s.getRange('E'+row).dataValidation={rule:{type:'list',values:['Employee','Company']}};
    s.getRange('J'+row).formulas=[[`=IF(COUNTA(A${row}:H${row})=0,"Unused",IF(AND(ISNUMBER(A${row}),A${row}>=1,LEN(TRIM(B${row}))>0,LEN(TRIM(C${row}))>0,LEN(TRIM(D${row}))>0,OR(E${row}="Employee",E${row}="Company"),${amount('F')},${amount('G')},G${row}<=F${row},OR(E${row}="Employee",G${row}=0),LEN(TRIM(H${row}))>0),"Ready","Complete / correct row"))`]];
   }else{
    s.getRange(`D${row}:E${row}`).setNumberFormat('#,##0.00;(#,##0.00);0.00');s.getRange('D'+row).setNumberFormat('0.###');
    s.getRange('J'+row).formulas=[[`=IF(COUNTA(A${row}:E${row},G${row}:H${row})=0,"Unused",IF(AND(LEN(TRIM(B${row}))>0,LEN(TRIM(C${row}))>0,ISNUMBER(D${row}),D${row}>0,D${row}<=1000000,ABS(D${row}-ROUND(D${row},3))<0.00000001,${amount('E')},D${row}*E${row}<=1000000000),"Ready","Complete / correct row"))`]];
    s.getRange('F'+row).formulas=[[`=IF(J${row}="Ready",ROUND(D${row}*E${row},2),"")`]];s.getRange('F'+row).format.fill='#EEF2F3';s.getRange('F'+row).format.font.color='#203D4A';s.getRange('F'+row).setNumberFormat('#,##0.00;(#,##0.00);0.00');
   }
  }
  for(let row=11;row<=20;row++){const f=s.getRange('J'+row).formulas[0][0];s.getRange('J'+row).formulas=[['=IFERROR('+f.slice(1)+',"Complete / correct row")']];}
  const rowsOK='AND(COUNTIFS(J11:J20,"Complete / correct row")=0,COUNTIFS(J11:J20,"Ready")>0)';
  const extras={expense:[['E25','F25','Advance','advance'],['E26','F26','Prior reimbursement','prior']],requisition:[['E23','F23','Estimated shipping','shipping'],['E24','F24','Estimated tax','tax'],['E26','F26','Available budget','budget']],order:[['E23','F23','Shipping','shipping'],['E24','F24','Entered tax','tax'],['E25','F25','Discount','discount'],['E27','F27','Paid to date','paid']]}[c.kind];
  const guards=[];
  for(const [label,cell,title,key] of extras){s.getRange(label).values=[[title]];s.getRange(cell).values=[[filled?Number(sample[key]):null]];s.getRange(cell).format.fill='#FFF3CF';s.getRange(cell).format.font.color='#0000FF';guards.push(`AND(ISNUMBER(${cell}),${cell}>=0,${cell}<=1000000000,ABS(${cell}-ROUND(${cell},2))<0.00000001)`);}
  const guard=`IFERROR(AND(${rowsOK},${guards.join(',')}),FALSE)`;
  function formula(label,cell,title,f){s.getRange(label).values=[[title]];s.getRange(cell).formulas=[[f]];s.getRange(cell).format.fill='#EEF2F3';s.getRange(cell).format.font.bold=true;}
  if(c.kind==='expense'){
   formula('E23','F23','Recorded costs',`=IF(${guard},SUM(F11:F20),"")`);
   formula('E24','F24','Employee-paid eligible',`=IF(${guard},SUMIFS(G11:G20,E11:E20,"Employee"),"")`);
   formula('E27','F27','Net reimbursement',`=IF(${guard},ROUND(F24-F25-F26,2),"")`);
   formula('E28','F28','Review position',`=IF(NOT(${guard}),"Complete inputs",IF(F27<0,"Review return / balance",IF(F27=0,"Nothing outstanding","Payable after review")))`);
  }else if(c.kind==='requisition'){
   formula('E25','F25','Estimated request',`=IF(${guard},ROUND(SUM(F11:F20)+F23+F24,2),"")`);
   formula('E27','F27','Budget headroom',`=IF(${guard},ROUND(F26-F25,2),"")`);
   formula('E28','F28','Cost review',`=IF(NOT(${guard}),"Complete inputs",IF(F27<0,"Over entered budget","Within entered budget"))`);
  }else{
   const good=`AND(${guard},F25<=SUM(F11:F20)+F23+F24)`;
   formula('E26','F26','Order total',`=IF(${good},ROUND(SUM(F11:F20)+F23+F24-F25,2),"")`);
   formula('E28','F28','Balance remaining',`=IF(${good},ROUND(F26-F27,2),"")`);
   formula('E29','F29','Payment position',`=IF(NOT(${good}),"Complete / correct inputs",IF(F28<0,"Review overpayment",IF(F28=0,"No balance remaining","Balance remains")))`);
  }
  for(let row=23;row<=29;row++){const label=s.getRange('E'+row).values[0][0];if(label){s.getRange('D'+row+':E'+row).merge();s.getRange('D'+row).values=[[label]];s.getRange('D'+row).format.font.bold=true;}}
  s.getRange('F23:F27').setNumberFormat('#,##0.00;(#,##0.00);0.00');if(c.kind==='order')s.getRange('F28').setNumberFormat('#,##0.00;(#,##0.00);0.00');
  s.getRange('F28:H28').merge();if(c.kind==='order')s.getRange('F29:H29').merge();s.getRange('F28:H29').format.wrapText=true;
  s.getRange('A31:H31').merge();s.getRange('A31').values=[['Review header, evidence and manual status before sharing. Draft calculations are not approval.']];
  s.getRange('A32:H32').merge();s.getRange('A32').values=[['Ten rows. Use one currency. Enter 0 for no charge. No currency conversion, payments or submissions.']];
  s.getRange('A33:H33').merge();s.getRange('A33').values=[['Save a separate version. Print Selection A1:H33, landscape, fit one page; inspect preview.']];
  s.getRange('A31:H33').format={font:{name:'Arial',size:10,color:'#4D6368'},wrapText:true,rowHeight:27};s.freezePanes.freezeRows(10);
 }
 const inst=wb.worksheets.add('Instructions');inst.getRange('A1:B18').format={font:{name:'Arial',size:11,color:'#203D4A'},rowHeight:48,wrapText:true};inst.getRange('A1:A18').format.columnWidth=27;inst.getRange('B1:B18').format.columnWidth=110;
 const instructions=[['Resource',c.title],['Tabs','Blank is for your work. Filled example is fictional. Keep the original file.'],['Inputs','Yellow cells are editable; gray cells calculate. Do not overwrite formulas.'],['Row limit','Ten rows per form. Extra rows need formula and total-range checks; use another version instead.'],['Money','Nonnegative numbers, at most two decimals. Quantity accepts three decimals. Invalid or partial rows block final amounts.'],['Currency','One currency code labels all amounts; no conversion. Browser JSON backups do not import into this workbook.'],['Save and reopen','Save as a new .xlsx, reopen it, change one amount, and verify the total before operational use.'],['Printing','Select A1:H33 on the required form tab. Choose landscape, Print Selection, and fit one page. Check all text in print preview.'],['Native compatibility','Built and round-trip tested with Artifact Tool. Native Microsoft Excel and Google Sheets have not been certified. Keep original formulas when converting.'],['Review','Complete header and manual review fields yourself. Draft totals and typed status do not authorize a transaction.'],['Fictional example',c.example],...c.steps.map(x=>x),['Limits',c.unique[c.unique.length-1][1]],['Guide','https://nexalyplanner.com/tools/'+c.slug+'/']];
 instructions.slice(0,18).forEach((r,i)=>{inst.getRange('A'+(i+1)+':B'+(i+1)).values=[r];inst.getRange('A'+(i+1)).format.font.bold=true;});
 wb.recalculate();const s=wb.worksheets.getItem('Filled example');const read=a=>s.getRange(a).values[0][0];
 function check(label,fn){wb.recalculate();if(!fn())throw Error(c.kind+' '+label+' '+JSON.stringify({out:s.getRange('E23:H29').values,row:s.getRange('E11:J11').values}));tests.push({resource:c.kind,case:label,pass:true});}
 const result=c.kind==='expense'?'F27':c.kind==='requisition'?'F25':'F28';const expected=c.kind==='expense'?118:c.kind==='requisition'?170:48;
 check('baseline',()=>read(result)===expected);
 if(c.kind==='expense'){
  s.getRange('F11:G11').values=[[130,130]];check('increased employee cost',()=>read('F27')===128);s.getRange('F11:G11').values=[[120,120]];
  s.getRange('F14').values=[[60]];check('company paid excluded',()=>read('F27')===118);s.getRange('F14').values=[[50]];
  s.getRange('F25').values=[[200]];check('advance excess visible',()=>read('F27')===-22);s.getRange('F25').values=[[60]];
  s.getRange('G11').values=[[121]];check('eligible above receipt blocked',()=>read('F27')==='');s.getRange('G11').values=[[120]];
 }else{
  s.getRange('D11').values=[[c.kind==='requisition'?18:3]];check('quantity change',()=>read(result)===(c.kind==='requisition'?158:73));s.getRange('D11').values=[[c.kind==='requisition'?20:2]];
  s.getRange('D11').values=[[0]];check('zero quantity blocked',()=>read(result)==='');s.getRange('D11').values=[[c.kind==='requisition'?20:2]];
  if(c.kind==='order'){s.getRange('F27').values=[[80]];check('overpayment visible',()=>read('F28')===-2);s.getRange('F27').values=[[30]];s.getRange('F25').values=[[79]];check('excess discount blocked',()=>read('F28')==='');s.getRange('F25').values=[[0]];}
 }
 s.getRange(c.kind==='expense'?'F11':'E11').values=[['bad']];check('text amount blocked',()=>read(result)==='');s.getRange(c.kind==='expense'?'F11':'E11').values=[[c.kind==='expense'?120:c.kind==='requisition'?6:25]];
 check('restored baseline',()=>read(result)===expected);
 const blank=wb.worksheets.getItem('Blank');if(blank.getRange(result).values[0][0]!=='')throw Error('blank claims finished zero');tests.push({resource:c.kind,case:'blank incomplete',pass:true});
 for(const name of ['Blank','Filled example']){
  const im=await wb.render({sheetName:name,range:'A1:H33',scale:1.25,format:'png'});await fs.writeFile(out+'/'+c.slug+'-'+(name==='Blank'?'blank':'example')+'.png',new Uint8Array(await im.arrayBuffer()));
 }
 wb.recalculate();const path=root+'/assets/downloads/'+c.slug+'.xlsx';await(await SpreadsheetFile.exportXlsx(wb)).save(path);
 const imported=await SpreadsheetFile.importXlsx(await FileBlob.load(path));imported.recalculate();const is=imported.worksheets.getItem('Filled example');if(is.getRange(result).values[0][0]!==expected)throw Error('roundtrip '+c.kind);
 const errors=await imported.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10}});await fs.writeFile(out+'/'+c.slug+'-errors.ndjson',errors.ndjson);
 tests.push({resource:c.kind,case:'XLSX export/import baseline',pass:true});console.log('Built '+c.slug);
}
await fs.writeFile(out+'/workbook-tests.json',JSON.stringify(tests,null,2));console.log('PASS '+tests.length+' workbook checks');
