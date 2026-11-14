# Seasonal stock clearance update — November 14, 2026

Focused update to the existing free tool and its input guide. Preserves canonical, original publication date, cover images, shared scripts and storefront. New page-only model/UI/CSS adds explicit partial sales, unsold cost, selling window, per-unit selling costs, contribution floor and fixed-volume discount comparison. Reports use cards rather than horizontal tables. CSV retains complete detail; JSON remains editable and legacy version 1 backups migrate to original all-sold/zero-extra-cost assumptions.

Independent checks cover 99 fee-rounding/floor-minimality scenarios, partial and zero sales, 100% fees/markdowns, invalid quantities, duplicate references, legacy imports, save/restore, report invalidation, CSV and text escaping. Example: 20 units available, 10 sold at $24, $12 unit cost, 5% fee, $1 extra selling cost, $15 fixed costs = $203 proceeds before inventory and $83 contribution; remaining inventory $120. At 40% markdown, same volume gives $146 proceeds/$26 contribution. Floor $15.27, previous cent produces -$0.03.

Research: Shopify retail markdown guide https://www.shopify.com/blog/retail-markdowns and Shopify Help markdown/markup guidance. No industry discount target, demand prediction or performance gain is claimed. Scenario comparisons intentionally hold sold units constant. No GSC data was available for this task.

Publication requires exact-head rebuild success and live inspection. Local DOM checks are not physical-device certification. Live outcome is reported in the publishing session.
