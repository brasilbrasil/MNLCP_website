#!/usr/bin/env python3
"""Check the built site: broken internal links and anchors, missing assets, and retired terms.

Usage (from MNLCP_website/): python3 tools/check_site.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
# Messaging guidelines: terms that should not appear in public text
RETIRED = [r"\boptimi[sz]ation\b", r"Footprint Manager", r"\bsave (?:the )?species\b", r"\bblueprints?\b",
           r"\bconservation lands\b", r"\bquestionnaires?\b", r"OptimTCE"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.text, self._skip = set(), [], [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


pages = {}
for f in sorted(SITE.glob("*.html")) + sorted(SITE.glob("groups/*.html")):
    if f.name.startswith("_"):
        continue
    c = Collector()
    c.feed(f.read_text(encoding="utf-8"))
    pages[f] = c

problems = 0
for f, c in pages.items():
    rel = f.relative_to(SITE)
    for link in c.links:
        if re.match(r"^(https?:|mailto:|tel:|data:|javascript:)", link):
            continue
        path, _, frag = link.partition("#")
        target = (f.parent / path).resolve() if path else f
        if not target.exists():
            print(f"{rel}: missing file {link}")
            problems += 1
        elif frag and target.suffix == ".html":
            tc = pages.get(target)
            if tc is not None and frag not in tc.ids:
                print(f"{rel}: missing anchor {link}")
                problems += 1
    text = " ".join(c.text)
    for pat in RETIRED:
        for m in re.finditer(pat, text, flags=re.I):
            ctx = text[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")
            print(f"{rel}: retired term '{m.group(0)}': …{ctx}…")
            problems += 1

print(f"{len(pages)} pages checked, {problems} problem(s).")
sys.exit(1 if problems else 0)
