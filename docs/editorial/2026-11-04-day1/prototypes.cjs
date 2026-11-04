/* Internal feasibility spike only. Not production or public financial statements. */
'use strict';
const assert=require('node:assert/strict');
function money(n){if(!Number.isSafeInteger(n)||n<0||n>1e12)throw Error('Use nonnegative integer cents within prototype limits.');return n;}
function bridge(v){for(const n of Object.values(v))money(n);return {operatingRemainder:v.revenue-v.consumedCosts,closingCash:v.openingCash+v.receipts-v.operatingPayments-v.equipment-v.ownerDraw,closingAR:v.openingAR+v.revenue-v.receipts,closingAP:v.openingAP+v.purchases-v.operatingPayments,stockIncrease:v.purchases-v.consumedCosts};}
const result=bridge({revenue:1800000,consumedCosts:1400000,openingCash:1200000,receipts:1500000,operatingPayments:1400000,equipment:200000,ownerDraw:100000,openingAR:500000,openingAP:400000,purchases:1600000});
assert.deepEqual(result,{operatingRemainder:400000,closingCash:1000000,closingAR:800000,closingAP:600000,stockIncrease:200000});assert.throws(()=>money(NaN));assert.throws(()=>money(0.1));
function flyer(v){const limits={business:100,offer:160,audience:100,action:160};for(const [key,max] of Object.entries(limits))if(typeof v[key]!=='string'||!v[key].trim()||v[key].length>max)throw Error('Required bounded flyer field.');return `${v.business.trim()}\n${v.offer.trim()}\nFor: ${v.audience.trim()}\nNext step: ${v.action.trim()}`;}
assert.equal(flyer({business:'Example studio',offer:'Book a fitting',audience:'local buyers',action:'Contact the studio'}),'Example studio\nBook a fitting\nFor: local buyers\nNext step: Contact the studio');assert.throws(()=>flyer({}));
console.log('PASS feasibility spikes: reconciled cents-based finance bridge and deterministic text-only flyer draft. Neither is a production builder or AI model.');
