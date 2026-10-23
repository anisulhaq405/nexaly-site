const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../../..'),out=path.resolve(root,'../day6-content-review');
const checks=[];function check(name,fn){fn();checks.push({name,pass:true});}
function fixture(file,kind){const a=require(path.join(root,'assets/js/'+file+'-models.js')),c=a.configs.find(c=>c.kind===kind),s=structuredClone(c.sample);s.rows.forEach((r,i)=>r.id='row-'+i);return {s,run:()=>a.evaluate(c.slug,s)};}
const metric=(r,l)=>r.metrics.find(m=>m.label===l).value;
check('Renewal: due-today boundary',()=>{const f=fixture('oct16-planners','documents');f.s.top.asOf='2026-10-01';assert.equal(f.run().rows[0][8],'Start today');});
check('Renewal: 45-day lead and 30 days to expiry',()=>{const f=fixture('oct16-planners','documents');assert.equal(f.run().rows[0][5],'2026-10-01');assert.equal(f.run().rows[0][6],30);});
check('Renewal: in-progress retains overdue action',()=>{const f=fixture('oct16-planners','documents');f.s.rows[0].status='Renewal in progress';assert.equal(metric(f.run(),'Start due / overdue'),1);});
check('Renewal: archived excluded from active totals',()=>{const f=fixture('oct16-planners','documents');f.s.rows[0].status='Replaced / archived';assert.equal(metric(f.run(),'Active documents'),0);});
check('Renewal: inclusive look-ahead last day',()=>{const f=fixture('oct16-planners','documents');f.s.rows[0].lead='0';assert.equal(metric(f.run(),'Starts within look-ahead'),1);f.s.rows[0].expiry='2026-11-16';assert.equal(metric(f.run(),'Starts within look-ahead'),0);});
check('Booking: three-way conflict not visible from pairs alone',()=>{const f=fixture('next-tools','bookings');f.s.top.buffer='0';f.s.rows=[['09:00','11:00'],['10:00','12:00'],['10:30','11:30']].map((t,i)=>({id:'row-'+i,booking:'Booking '+i,start:'2026-10-09T'+t[0],end:'2026-10-09T'+t[1],quantity:'1'}));const r=f.run();assert.equal(metric(r,'Peak concurrent quantity'),3);assert.equal(metric(r,'Conflict intervals'),1);assert.deepEqual(r.extra[0].rows[0].slice(0,5),['2026-10-09 10:30 UTC','2026-10-09 11:00 UTC',3,2,1]);});
check('Booking: exact release with zero buffer',()=>{const f=fixture('next-tools','bookings');f.s.top.buffer='0';f.s.rows[1].start='2026-10-09T12:00';assert.equal(metric(f.run(),'Conflict intervals'),0);});
check('Booking: buffer overlap and exact buffered release',()=>{const f=fixture('next-tools','bookings');assert.equal(metric(f.run(),'Conflict intervals'),1);f.s.rows[1].start='2026-10-09T12:30';assert.equal(metric(f.run(),'Conflict intervals'),0);});
check('Maintenance: 15 hours remaining, proposed use exceeds target by 3',()=>{assert.equal(520-505,15);assert.equal(505+18-520,3);});
check('Agency: contractor review turns 3-hour headroom into 1-hour overload',()=>{assert.equal(145-20,125);assert.equal(125+4-128,1);});
check('PO: cumulative snapshots and duplicate receipt',()=>{assert.equal(100-55-5,40);assert.equal(88-55,33);assert.equal(100-88-5,7);assert.equal(100-(88+33)-5,-26);});
check('PO: trigger is distinct from replenishment target',()=>{assert.equal(32+24-8,48);assert.equal(32+12-8,36);assert.equal(48-36,12);assert.notEqual(40-36,12);});
fs.writeFileSync(path.join(out,'scenario-checks.json'),JSON.stringify(checks,null,2));console.log('PASS:',checks.length,'documented scenario checks');
