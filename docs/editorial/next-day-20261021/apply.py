"""Apply reviewed drafts locally; never deploys or commits. Run from repository root."""
import argparse, datetime, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--date", required=True, help="Actual implementation date YYYY-MM-DD")
args = parser.parse_args()
day = datetime.date.fromisoformat(args.date)
label = day.strftime("%B") + " " + str(day.day) + ", " + str(day.year)
manifest = json.loads((HERE / "manifest.json").read_text())
writes = []
for item in manifest:
    target = ROOT / item["target"]
    raw = target.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if blob != item["base_blob"]:
        raise SystemExit("Source changed; rebase this draft before applying: " + item["target"])
    html = (HERE / item["draft"]).read_text()
    html, count = re.subn(r'(<meta property="article:modified_time" content=")[^"]+(">)', lambda m: m[1] + args.date + m[2], html)
    if count != 1:
        raise SystemExit("Expected one modified-time tag")
    html, count = re.subn(r'(Updated <time datetime=")[^"]+(">)[^<]+(</time>)', lambda m: m[1] + args.date + m[2] + label + m[3], html)
    if count != 1:
        raise SystemExit("Expected one updated date in header")
    html, count = re.subn(r'("dateModified":\s*")[^"]+(")', lambda m: m[1] + args.date + m[2], html)
    if count != 1:
        raise SystemExit("Expected one schema dateModified")
    writes.append((target, html))
csv_target = ROOT / "downloads/templates/sales-inventory-worked-example.csv"
if csv_target.exists():
    raise SystemExit("CSV already exists; review before replacing")
writes.append((csv_target, (HERE / "sales-inventory-worked-example.csv").read_text()))
for target, text in writes:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)
print("Drafts applied locally. Run SEO build, regression checks and browser review before committing.")
