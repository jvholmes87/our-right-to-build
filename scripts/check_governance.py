#!/usr/bin/env python3
"""No-dependency structural check for the ORB repository.

This cannot replace review of licensing, factual claims, accessibility,
privacy, security, or owner release authorization.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CONTENT_LICENSE.md", "CONTRIBUTING.md", "SECURITY.md", "CITATION.cff",
    "docs/EVIDENCE_POLICY.md", "docs/PROJECT_MANAGEMENT.md",
    "docs/RELEASE_GATES.md", "website/ARCHITECTURE.md",
    "website/index.html", "website/styles.css",
    "research/README.md", "brand/README.md",
    "visualizations/README.md", "visualizations/TOOL_REGISTER.md",
    ".github/pull_request_template.md", ".github/ISSUE_TEMPLATE/feature.yml",
]
errors = []
for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing expected file: {relative}")

class WebsiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.external_scripts = []
        self.ids = set()
        self.has_main = False
        self.has_title = False
        self.title_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "main":
            self.has_main = True
        if tag == "title":
            self.title_depth += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in ("a", "link", "script"):
            key = "href" if tag in ("a", "link") else "src"
            if attrs.get(key):
                self.links.append((tag, attrs[key]))
        if tag == "script" and attrs.get("src"):
            self.external_scripts.append(attrs["src"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_depth = max(0, self.title_depth - 1)

    def handle_data(self, data):
        if self.title_depth and data.strip():
            self.has_title = True

site = ROOT / "website" / "index.html"
if site.is_file():
    parser = WebsiteParser()
    parser.feed(site.read_text(encoding="utf-8"))
    if not parser.has_main:
        errors.append("Website missing semantic <main> element")
    if not parser.has_title:
        errors.append("Website missing a nonempty <title>")
    if parser.external_scripts:
        errors.append("External website scripts require specific owner approval")
    for tag, link in parser.links:
        url = urlsplit(link)
        if url.scheme in ("https", "http", "mailto", "tel"):
            continue
        if url.scheme or url.netloc:
            errors.append(f"Unexpected URI scheme in {tag}: {link}")
            continue
        if not url.path:
            if url.fragment and url.fragment not in parser.ids:
                errors.append(f"Broken in-page anchor: #{url.fragment}")
            continue
        local_path = (site.parent / unquote(url.path)).resolve()
        if not local_path.is_relative_to((ROOT / "website").resolve()):
            errors.append(f"Local website path escapes website/: {link}")
        elif not local_path.is_file():
            errors.append(f"Broken local link/resource: {link}")
        elif url.fragment and url.fragment not in parser.ids and local_path == site:
            errors.append(f"Broken in-page anchor: {link}")

if errors:
    for err in errors:
        print(f"FAIL: {err}", file=sys.stderr)
    sys.exit(1)
print("PASS: required ORB files exist; starter HTML structure and local links checked")
