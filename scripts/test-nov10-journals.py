#!/usr/bin/env python3
"""Check the bounded GSC refresh, dates, contextual links and original arithmetic."""
import calendar
import json
import re
import sys
from datetime import date
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'docs/editorial/2026-11-10-gsc-journals'


def main():
    release_audit = '--release-audit' in sys.argv
    scope = json.loads((AUDIT / 'scope.json').read_text())
    original = json.loads((AUDIT / 'before-metadata.json').read_text())
    research = json.loads((AUDIT / 'competitors.json').read_text())
    assert len(scope) == 38 and len(research) == 38
    sections = {}
    for row in scope:
        slug = row['slug']
        source = (ROOT / 'journal' / slug / 'index.html').read_text()
        marker = 'id="nov10-' + slug + '"'
        assert source.count(marker) == 1, slug
        section = source.split(marker, 1)[1].split('</section>', 1)[0]
        assert source.index(marker) < source.index('</article>'), slug
        if release_audit:
            assert len(re.sub('<[^>]+>', ' ', section).split()) >= 150, slug
            assert len(re.findall('href="/(?!/)', section)) >= 2, slug
        assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"', source) == original[slug]['datePublished'], slug
        modified = {x[:10] for x in re.findall(r'"dateModified"\s*:\s*"([^"]+)"', source)}
        assert len(modified) == 1 and all(date.fromisoformat(x) >= date(2026,11,10) for x in modified), slug
        if release_audit:
            assert modified == {'2026-11-10'}, slug
            assert re.search(r'<title>(.*?)</title>', source, re.S)[1] == original[slug]['title'], slug
            assert re.search(r'<meta name="description" content="([^"]+)"', source)[1] == original[slug]['description'], slug
        assert len({c['url'].split('/')[2].removeprefix('www.') for c in research[slug]['competitors']}) == 3, slug
        sections[slug] = section

    def shown(slug, value):
        assert value in sections[slug], (slug, value)

    assert 30 * D('.4') * D('.5') * D('.5') == 3
    assert D(90) - 17 - D(90)*D('.03') == D('70.30')
    assert 6*D('70.30')-400 == D('21.80')
    shown('spa-business-plan', '$21.80')
    assert D(23760)*(1-D('.04'))-4356-15000 == D('3453.60')
    assert D(23760)*(1-D('.12'))-4356-15000 == D('1552.80')
    shown('hotel-business-plan', '$1,552.80')
    assert 61+9+10 == 80 and 100*D(61)/80 == D('76.25')
    shown('operations-dashboard-example', '76.25%')
    assert (1200-1000)*D('.20')*50 + 1200*(D('.18')-D('.20'))*50 == 800
    assert round(D(5900)/8100, 2) == D('.73')
    shown('nonprofit-business-plan', '0.73 months')
    assert round(D('139.7')/148*100, 2) == D('94.39')
    assert round(D('139.7')/148*210, 1) == D('198.2')
    shown('planner-sizes-chart-printable-inserts', '198.2 mm')
    assert 148-12-8 == 128 and 210-10-10 == 190
    assert 190-16*8-20 == 42
    assert 115+30*D('.4') == 127 and 115+30-128 == 17
    assert sum([12,8,5]) == 25
    assert 0+6000-5000 == 1000 and 0+6000-4000 == 2000
    assert 3000+2000+2400-3100 == 4300
    shown('cash-flow-forecast-template-example', '$4,300')
    assert 0+18-12 == 6 and 6+8-12 == 2
    assert 3000*(1-D('.1')) == 2700 and 200-300 == -100
    assert 4*60-60-30-15 == 135 and 90+60+30-135 == 45
    assert round(D(10)/15*100,2) == D('66.67')
    assert 2*1250-180-2*140 == 2040
    shown('freelance-business-plan-example', '$2,040')
    assert 4*2*30-4*45 == 60
    assert 12-3-2 == 7
    assert 18+12*3 == 54 and (18+12)*3 == 90
    assert date(2026,8,1).weekday() == calendar.SATURDAY
    assert 6+calendar.monthrange(2026,8)[1] == 37
    assert date(2026,11,1).weekday() == calendar.SUNDAY
    assert date(2026,12,1).weekday() == calendar.TUESDAY
    assert (date(2026,12,31)-date(2026,11,10)).days+1 == 52
    assert date(2026,11,20).weekday() == calendar.FRIDAY
    assert date(2026,11,18).weekday() == calendar.WEDNESDAY
    assert 10*12-(4*12+6)-12 == 54
    assert -10*(80-28)-90*(30-28)-(2900-2800) == -800
    shown('small-business-budget-example', '−$800')
    assert 60+90+30 == 180 and 180-(90+60) == 30
    scores_a=[4,5,4,3];scores_b=[5,4,3,5]
    for weights, expected in [([40,30,20,10],(D('4.2'),D('4.3'))),([20,50,20,10],(D('4.4'),D('4.1')))]:
        assert sum(weights)==100
        result=tuple(sum(D(s)*w/100 for s,w in zip(scores,weights)) for scores in [scores_a,scores_b])
        assert result==expected
    assert 160//16==10 and 160//20==8 and (10-8)*630==1260
    shown('trucking-company-business-plan-trip-cost', '$1,260')
    print('PASS 38 scoped updates, preserved publication dates, 114 competitor entries, worked arithmetic and date scenarios' + ('; release title/description/date/link audit' if release_audit else ''))


if __name__ == '__main__':
    main()
