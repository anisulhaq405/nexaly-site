#!/usr/bin/env python3
"""Read-only local HTML/sitemap SEO checks for NexalyPlanner.
Run from repository root: python3 scripts/seo-growth-audit.py
Only checks local evidence; GSC metrics must be sourced separately.
"""
from __future__ import annotations
import csv
import html.parser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HOST = "nexalyplanner.com"

class PageParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.canonicals = []
        self.robots = []
        self.links = []
        self._title = False
        self.h1_count = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonicals.append(a.get("href", ""))
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots.append(a.get("content", "").lower())
        if tag == "a":
            self.links.append(a.get("href", ""))
    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False
    def handle_data(self, data):
        if self._title:
            self.title += data

def local_path(url):
    parsed = urlparse(url)
    if parsed.netloc != HOST or parsed.scheme != "https":
        return None
    path = parsed.path
    if path.endswith("/"):
        return ROOT / path.lstrip("/") / "index.html"
    return ROOT / path.lstrip("/")

def main():
    xml = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [e.text.strip() for e in xml.findall(".//s:loc", ns) if e.text]
    rows = []
    for url in urls:
        path = local_path(url)
        problems = []
        if path is None or not path.is_file():
            problems.append("missing_local_html_or_noncanonical_host")
            rows.append([url, "", "", "", "", ";".join(problems)])
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        if not parser.title.strip():
            problems.append("missing_title")
        if parser.h1_count != 1:
            problems.append("h1_count_"+str(parser.h1_count))
        if len(parser.canonicals) != 1 or parser.canonicals[0] != url:
            problems.append("canonical_mismatch")
        if any("noindex" in r.split(",") or "noindex" in r for r in parser.robots):
            problems.append("sitemap_page_noindex")
        for link in parser.links:
            parsed = urlparse(link)
            if parsed.scheme in ("mailto", "tel", "javascript") or link.startswith(("#", "?")):
                continue
            if parsed.netloc and parsed.netloc != HOST:
                continue
            if not parsed.path:
                continue
            target = local_path("https://"+HOST+parsed.path)
            if target is not None and not target.is_file():
                problems.append("potential_broken_internal_link:"+parsed.path)
                break
        rows.append([url, str(path.relative_to(ROOT)), parser.title.strip(), str(parser.h1_count),
                     "|".join(parser.canonicals), ";".join(problems)])
    report = ROOT / "seo-growth-audit.csv"
    with report.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["url", "file", "title", "h1_count", "canonical", "issues"])
        w.writerows(rows)
    flagged = sum(bool(row[-1]) for row in rows)
    print(f"Checked {len(rows)} sitemap URLs; {flagged} flagged. Report: {report.name}")
    print("Local diagnostics only: does NOT verify Google indexing, HTTP status or rankings.")

if __name__ == "__main__":
    main()
