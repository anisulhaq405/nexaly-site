"""Regression tests in an isolated copy; fixtures never reach the storefront."""
import json, shutil, subprocess, tempfile, re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='nexaly-seo-test-') as directory:
    target=Path(directory)/'site'
    shutil.copytree(root,target,ignore=shutil.ignore_patterns('.git','node_modules'))
    def run(ok=True,*args):
        result=subprocess.run(['python3',str(target/'scripts/seo-build.py'),*args],capture_output=True,text=True)
        assert (result.returncode==0)==ok,result.stdout+result.stderr
        return result
    protected={p.relative_to(target):p.read_bytes() for p in target.glob('planners/*/index.html') if p.parent.name not in {'digital-planners','business-operating-systems'}}
    def regions(source):
        return re.findall(r'<(?:header|footer)\b[\s\S]*?</(?:header|footer)>',source)
    regions_before={p.relative_to(target):regions(p.read_text()) for p in target.rglob('index.html')}
    js_before=(target/'assets/js/main.js').read_text()
    run();run(True,'--check')
    for p,value in protected.items():assert (target/p).read_bytes()==value,str(p)+' product changed'
    for p,value in regions_before.items():assert regions((target/p).read_text())==value,str(p)+' header/footer changed'
    js_after=(target/'assets/js/main.js').read_text()
    assert js_before.split('var heartSvg',1)[1]==js_after.split('var heartSvg',1)[1],'storefront or payment logic changed'
    def page(title,extra='',body=''):
        return '<html><head><title>'+title+'</title><meta name="description" content="Details for '+title+'"><meta property="og:image" content="https://nexalyplanner.com/images/og-default.jpg">'+extra+'</head><body><h1>'+title+'</h1><p>A meaningful introduction for this isolated publishing fixture.</p>'+body+'</body></html>'
    article=target/'journal/seo-test-article/index.html';article.parent.mkdir()
    article.write_text(page('Test article','<link rel="canonical" href="https://wrong.example/">'))
    run()
    assert 'https://nexalyplanner.com/journal/seo-test-article/' in article.read_text()
    assert '/journal/seo-test-article/' in (target/'index.html').read_text()
    article.write_text(page('Updated article','<meta property="og:image:alt" content="Accurate new image description">'))
    run();run(True,'--check')
    catalog=(target/'assets/js/main.js').read_text()
    assert '"title": "Updated article"' in catalog and '"alt": "Accurate new image description"' in catalog
    product=target/'planners/seo-test-product/index.html';product.parent.mkdir()
    good=page('Test product','<meta property="product:price:amount" content="12.50"><meta name="nexaly:category" content="Business Operating Systems">','<a href="https://buy.polar.sh/test-fixture-only">Buy</a>')
    for bad in [
        good.replace('<a href="https://buy.polar.sh/test-fixture-only">Buy</a>',''),
        good.replace('/images/og-default.jpg','/images/missing-fixture.png'),
        good.replace('content="12.50"','content="NaN"'),
        good.replace('</body>','<a href="/missing-fixture/">Broken</a></body>')]:
        product.write_text(bad)
        before=(target/'assets/js/main.js').read_text()
        run(False)
        assert before==(target/'assets/js/main.js').read_text(),'failed build wrote catalogue'
    product.write_text(good);run()
    assert '/planners/seo-test-product/' in (target/'planners/business-operating-systems/index.html').read_text()
    assert '"buyUrl": "https://buy.polar.sh/test-fixture-only"' in (target/'assets/js/main.js').read_text()
    product.write_text(good.replace('</head>','<meta name="robots" content="noindex"></head>'))
    run()
    assert '/planners/seo-test-product/' not in (target/'sitemap.xml').read_text()
    assert '/planners/seo-test-product/' not in (target/'planners/index.html').read_text()
    product.unlink();article.unlink();run();run(True,'--check')
    assert '/journal/seo-test-article/' not in (target/'sitemap.xml').read_text()
    assert '/journal/seo-test-article/' not in (target/'journal/index.html').read_text()
print('PASS: protected products/header/footer/payment logic; idempotence; journal refresh; product checkout/image/price; broken links; draft exclusion; deletion; failed-build isolation')
