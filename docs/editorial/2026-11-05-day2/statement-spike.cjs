'use strict';
const assert=require('node:assert/strict');
const opening={cash:1200000,receivables:500000,stock:800000,equipment:1000000,payables:400000,loan:600000,equity:2500000};
function assets(v){return v.cash+v.receivables+v.stock+v.equipment;}
function balances(v){for(const n of Object.values(v))if(!Number.isSafeInteger(n)||n<0)throw Error('Use nonnegative integer cents.');return assets(v)===v.payables+v.loan+v.equity;}
assert.ok(balances(opening));const profit=1800000-1400000;
const closing={cash:opening.cash+1500000-1400000-200000-100000,receivables:opening.receivables+1800000-1500000,stock:opening.stock+1600000-1400000,equipment:opening.equipment+200000,payables:opening.payables+1600000-1400000,loan:opening.loan,equity:opening.equity+profit-100000};
assert.ok(balances(closing));assert.equal(assets(opening),3500000);assert.equal(assets(closing),4000000);assert.equal(closing.cash,1000000);assert.equal(closing.equity,2800000);assert.equal(balances({...closing,equity:closing.equity+1}),false);assert.throws(()=>balances({...opening,cash:NaN}));
console.log('PASS internal Day2 feasibility: opening/closing balance equation and operating/cash/equity bridge; no production builder claimed.');
