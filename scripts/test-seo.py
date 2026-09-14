"""Exercise future publishing in an isolated copy; never publish test products."""
import json, shutil, subprocess, tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='nexaly-seo-test-') as directory:
    target=Path(directory)/'site'
    shutil.copytree(root,target,ignore=shutil.ignore_patterns('.git','node_modules'))
    def run(ok=True,*args):
        result=subprocess.run(['python3',str(target/'scripts/seo-build.py'),*args],capture_output=True,text=True)
        assert (result.returncode==0)==ok,result.stdout+result.stderr
        return result
    run(True);run(True,'--check')
    article=target/'journal/seo-test-article/index.html';article.parent.mkdir()
    article.write_text('<html><head><title>Test article</title><link rel="canonical" href="https://wrong.example/"></head><body><h1>Test article</h1><p>A sufficiently detailed article introduction to derive its search description automatically.</p></body></html>')
    run(True)
    assert 'https://nexalyplanner.com/journal/seo-test-article/' in article.read_text()
    assert 'seo-test-article/' in (target/'sitemap.xml').read_text()
    assert '/journal/seo-test-article/' in (target/'index.html').read_text()
    run(True,'--check')
    product=target/'planners/seo-test-product/index.html';product.parent.mkdir()
    product.write_text('<html><head><title>Test product</title><meta property="product:price:amount" content="12.50"><meta name="nexaly:category" content="Business Operating Systems"></head><body><h1>Test product</h1><p>A detailed description of the test product with sufficient information for a search preview.</p></body></html>')
    run(True)
    assert '/planners/seo-test-product/' in (target/'planners/business-operating-systems/index.html').read_text()
    assert '$12.5' in (target/'planners/index.html').read_text()
    product.write_text(product.read_text().replace('</head>','<meta name="robots" content="noindex"></head>'))
    run(True)
    assert '/planners/seo-test-product/' not in (target/'sitemap.xml').read_text()
    assert '/planners/seo-test-product/' not in (target/'planners/index.html').read_text()
    article.unlink();run(True)
    assert '/journal/seo-test-article/' not in (target/'sitemap.xml').read_text()
    assert '/journal/seo-test-article/' not in (target/'journal/index.html').read_text()
    product.write_text('<html><head><title>Missing price</title></head><body><h1>Missing price</h1><p>This product deliberately omits its real price and must never be invented by automation.</p></body></html>')
    before=(target/'assets/js/main.js').read_text();run(False)
    assert (target/'assets/js/main.js').read_text()==before
print('PASS: repeatable build, new article, new product, draft exclusion, deletion, missing-price failure')
