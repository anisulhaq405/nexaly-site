#!/usr/bin/env python3
"""Check crawlable pages for orphaned URLs and broken internal links."""
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href", ""))


def main():
    pages = {}
    for file in ROOT.rglob("index.html"):
        if ".git" in file.parts:
            continue
        url = "/" + str(file.parent.relative_to(ROOT)).replace(".", "").strip("/")
        url = url.rstrip("/") + "/"
        html = file.read_text(encoding="utf-8", errors="replace")
        if '<meta name="robots" content="noindex' not in html.lower():
            pages[url] = (file, html)

    incoming = defaultdict(set)
    broken = defaultdict(set)
    for source, (_, html) in pages.items():
        parser = Links()
        parser.feed(html)
        for href in parser.hrefs:
            parsed = urlparse(href)
            if parsed.netloc and parsed.netloc not in {"nexalyplanner.com", "www.nexalyplanner.com"}:
                continue
            if not parsed.path or (not parsed.netloc and not href.startswith("/")):
                continue
            path = unquote(parsed.path)
            target = path.rstrip("/") + "/"
            if target in pages:
                incoming[target].add(source)
            elif not (ROOT / path.lstrip("/")).exists() and not (ROOT / path.lstrip("/").rstrip("/")).exists():
                broken[path].add(source)

    orphans = sorted(url for url in pages if url != "/" and not incoming[url])
    print(f"Indexable pages: {len(pages)}; orphan pages: {len(orphans)}; broken internal URLs: {len(broken)}")
    for url in orphans:
        print("ORPHAN", url)
    for url, sources in sorted(broken.items()):
        print("BROKEN", url, "linked from", ", ".join(sorted(sources)))
    raise SystemExit(bool(orphans or broken))


if __name__ == "__main__":
    main()
