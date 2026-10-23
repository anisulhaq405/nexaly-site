from pathlib import Path
import subprocess,json,os,concurrent.futures
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT.parent/'day6-content-review';OUT.mkdir(exist_ok=True)
jobs=[('models-'+x,['node',f'scripts/test-{x}.cjs']) for x in ['craft-fair','small-tools','next-tools','keyword-workflows','oct16-planners','final-ten']]
jobs += [('DOM-'+x,['node',f'scripts/test-{x}-ui.cjs']) for x in ['keyword-workflows','oct16-planners','final-ten']]
jobs += [('contact',['node','scripts/test-contact-flow.cjs']),('consent',['node','scripts/test-analytics-consent.cjs']),('social-fixtures',['python3','scripts/test-social.py']),('core',['python3','scripts/check-core-lock.py'])]
def run(job):
 name,cmd=job;env=dict(os.environ,NEXALY_JSDOM_PATH=str(ROOT.parent/'day6-test-deps/node_modules/jsdom'))
 p=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True);(OUT/(name+'.log')).write_text(p.stdout+p.stderr)
 return {'check':name,'returncode':p.returncode,'pass':p.returncode==0,'output':(p.stdout+p.stderr)[-1800:]}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(run,jobs))
(OUT/'runtime-checks.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
assert all(x['pass'] for x in results)
