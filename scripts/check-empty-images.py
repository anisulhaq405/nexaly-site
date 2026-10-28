#!/usr/bin/env python3
"""Fail CI if a tracked image asset is empty, preventing broken social media conversions."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE_EXTENSIONS = {".webp", ".png", ".jpg", ".jpeg", ".gif", ".avif", ".svg"}
folders = ("assets/img", "images")
empty = [
    str(path.relative_to(ROOT))
    for folder in folders
    for path in (ROOT / folder).rglob("*")
    if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS and path.stat().st_size == 0
]
if empty:
    raise SystemExit("FAIL: Empty image assets: " + ", ".join(sorted(empty)))
print("PASS: No empty image assets in assets/img or images.")
