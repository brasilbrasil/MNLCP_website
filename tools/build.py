#!/usr/bin/env python3
"""Build the MNLCP static website from content/ into plain HTML pages.

Usage (from MNLCP_website/):
    python3 tools/build.py            # draft build (draft banner, noindex, review aids)
    python3 tools/build.py --release  # public build (no banner, indexable)

Reads   content/pages/**/*.md, content/data/*.json, tools/templates/*.html
Writes  *.html, groups/*.html, assets/data/*.js (compiled data + search index)

The output needs no server or build step to host: copy the folder anywhere.
Requires Python 3.8+ and the `markdown` package (pip install markdown).
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

import markdown

SITE = Path(__file__).resolve().parent.parent
CONTENT = SITE / "content"
TEMPLATES = SITE / "tools" / "templates"
DATA_OUT = SITE / "assets" / "data"

SITE_NAME = "Maui Nui Landscape Conservation Plan"
SITE_SHORT = "MNLCP"
AGENCY = "Hawaiʻi Division of Forestry and Wildlife"
PLAN_VERSION = "Version September 29, 2026"

BRAND = {
    "seal_dofaw": "assets/img/brand/dofaw_seal_nene.png",
    "seal_dlnr": "assets/img/brand/dlnr_seal.png",
    "footer_band": "assets/img/brand/footer_band_2400x300.png",
}

# ---------------------------------------------------------------- navigation
NAV = [
    ("The Plan", [
        ("plan.html", "About the Plan", "Purpose, need and the three goals"),
        ("approach.html", "The Approach", "How where, what and when fit together"),
        ("partners.html", "Partners & Teams", "The people and organizations behind the plan"),
    ]),
    ("Species", [
        ("species.html", "At-Risk Species", "442 species and how they were identified"),
        ("groups.html", "Taxonomic Groups", "Recovery strategies for eight groups"),
    ]),
    ("Where & What", [
        ("footprints.html", "Conservation Footprints", "Interactive map of where to act"),
        ("actions.html", "Priority Actions", "What to do, and what it costs"),
        ("ecosystems.html", "Native Ecosystems", "Landscape-scale ecosystem priorities"),
    ]),
    ("Putting It to Work", [
        ("using-the-plan.html", "Using the Plan", "A practical guide for managers and partners"),
        ("tools.html", "Adaptive Conservation Planner", "The living-plan tool and other resources"),
        ("monitoring.html", "Monitoring & Adaptive Management", "Learning from what we do"),
    ]),
    ("faq.html", "Q&A", None),
    ("resources.html", "Resources", None),
]

GROUPS = [
    ("forest-birds", "Forest birds"),
    ("seabirds", "Seabirds"),
    ("waterbirds", "Waterbirds"),
    ("plants", "Plants"),
    ("terrestrial-snails", "Terrestrial snails"),
    ("terrestrial-arthropods", "Terrestrial arthropods"),
    ("aquatic-invertebrates", "Aquatic invertebrates"),
    ("hawaiian-hoary-bat", "Hawaiian hoary bat"),
]

# Page registry: out file -> settings. "md" is relative to content/pages.
PAGES = {
    "plan.html": {"md": "plan.md", "section": "The Plan", "hero": "assets/img/photos/hero_page_plan.jpg"},
    "approach.html": {"md": "approach.md", "section": "The Plan", "hero": "assets/img/photos/hero_page_approach.jpg"},
    "partners.html": {"md": "partners.md", "section": "The Plan", "hero": "assets/img/photos/hero_page_partners.jpg"},
    "species.html": {"md": "species.md", "section": "Species", "hero": "assets/img/photos/hero_page_species.jpg"},
    "using-the-plan.html": {"md": "using-the-plan.md", "section": "Putting It to Work", "hero": "assets/img/photos/hero_page_using.jpg"},
    "actions.html": {"md": "actions.md", "section": "Where & What", "hero": "assets/img/photos/hero_page_actions.jpg"},
    "ecosystems.html": {"md": "ecosystems.md", "section": "Where & What", "hero": "assets/img/photos/hero_page_ecosystems.jpg"},
    "monitoring.html": {"md": "monitoring.md", "section": "Putting It to Work", "hero": "assets/img/photos/hero_page_monitoring.jpg"},
    "tools.html": {"md": "tools.md", "section": "Putting It to Work", "hero": "assets/img/photos/hero_page_tools.jpg"},
    "resources.html": {"md": "resources.md", "section": None, "hero": None},
}
for slug, name in GROUPS:
    PAGES[f"groups/{slug}.html"] = {
        "md": f"groups/{slug}.md", "section": "Species", "group": slug,
        "hero": f"assets/img/photos/hero_group_{slug}.jpg",
        "parent": ("groups.html", "Taxonomic Groups"),
    }


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(str(s), quote=True)


def read(path):
    return Path(path).read_text(encoding="utf-8")


def fix_text(s):
    """Repair PDF-extraction artifacts that slip into drafted content."""
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff")
    s = re.sub(r"(?<=\w)`(?=\w)", "ʻ", s)          # backtick used as ʻokina inside a word
    s = re.sub(r"(?<![`\w])`(?=[A-Za-zāēīōūĀĒĪŌŪ])", "ʻ", s)  # leading ʻokina
    return s


def parse_front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip("\n")
            text = text[end + 4:].lstrip("\n")
            for line in block.splitlines():
                if ":" not in line or line.startswith(" "):
                    continue
                k, v = line.split(":", 1)
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
                else:
                    v = v.strip("\"'")
                meta[k.strip()] = v
    return meta, text


def split_sections(text):
    """Split markdown into (heading, body) by level-2 headings. Heading '' = preamble."""
    parts = re.split(r"^## +(.+?)\s*$", text, flags=re.M)
    out = [("", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out


SRC_RE = re.compile(r"\s*<!--\s*src:\s*(.*?)\s*-->", re.S)
COMMENT_RE = re.compile(r"<!--(?!\s*src:).*?-->", re.S)


def src_notes(text):
    """Turn <!-- src: … --> comments into hidden review markers; drop other comments."""
    text = SRC_RE.sub(lambda m: f'<span class="src-note" title="{esc(m.group(1))}">{esc(m.group(1))}</span>', text)
    return COMMENT_RE.sub("", text)


def strip_src(text):
    return COMMENT_RE.sub("", SRC_RE.sub("", text))


FIG_RE = re.compile(r"^\[figure:\s*(.+?)\]\s*(?:<!--.*?-->)?\s*$", re.M)


# ACP screenshots cleared for the public site (current app name; no internal layers, species points or snail locations).
SCREENSHOTS_OK = set()  # none until clean screenshots are recaptured from the current ACP
EXEC_SUMMARY_FIGS = {"1": "02", "2": "03"}  # Executive Summary figures reuse Ch 5/6 images


def resolve_figure(sugg):
    """Map a drafter's 'suggested source' to an extracted image, or None."""
    img = SITE / "assets" / "img"
    m = re.search(r"screenshots/([\w-]+)\.png", sugg)
    if m:
        name = m.group(1)
        f = img / "screenshots" / f"acp_{name.replace('-', '_')}_crop.png"
        return (f"assets/img/screenshots/{f.name}", None) if name in SCREENSHOTS_OK and f.exists() else None
    m = re.search(r"Figure\s+(\d+)", sugg)
    if not m or "rebuild as SVG" in sugg:
        return None
    n = m.group(1)
    if re.search(r"A2-\d+", sugg):
        pattern = f"plan_fig_app2_{n}_*"
    elif "Executive Summary" in sugg and "same chart" not in sugg:
        pattern = f"plan_fig_{EXEC_SUMMARY_FIGS.get(n, n.zfill(2))}_*"
    else:
        pattern = f"plan_fig_{n.zfill(2)}_*"
    hits = sorted((img / "figures").glob(pattern))
    return (f"assets/img/figures/{hits[0].name}", f"Plan Figure {n}" + (" (Appendix 2)" if "A2-" in sugg else "")) if hits else None


def figure_html(spec, draft):
    parts = [p.strip() for p in spec.split("|")]
    desc = parts[0]
    kv = {}
    for p in parts[1:]:
        if ":" in p:
            k, v = p.split(":", 1)
            kv[k.strip().lower()] = v.strip()
    src = kv.get("src")
    if not src and kv.get("suggested source"):
        hit = resolve_figure(kv["suggested source"])
        if hit:
            src = hit[0]
            if "caption" not in kv:
                kv["caption"] = esc(desc[0].upper() + desc[1:]) + (f'. <span class="muted">{esc(hit[1])}.</span>' if hit[1] else ".")
    alt = kv.get("alt", desc)
    caption = kv.get("caption", "")
    credit = kv.get("credit", "")
    if src:
        cap = caption + (f' <span class="muted">{esc(credit)}</span>' if credit else "")
        cls = "zoomable" if kv.get("zoom", "yes") != "no" else ""
        return (f'\n<figure class="{cls}"><img src="{esc(src)}" alt="{esc(alt)}" loading="lazy">'
                + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>\n")
    if not draft:
        return ""
    sugg = kv.get("suggested source", "")
    return (f'\n<div class="figure-placeholder"><b>Image to come: {esc(desc)}</b>'
            + (f"Suggested source: {esc(sugg)}" if sugg else "") + "</div>\n")


DETAILS_RE = re.compile(r"^:::details\s+(.+?)\s*\n(.*?)^:::\s*$", re.M | re.S)
WIDGET_RE = re.compile(r"^\[\[widget:([\w-]+)\]\]\s*$", re.M)
TABLECAP_RE = re.compile(r"^\[table:\s*(.+?)\]\s*(<!--.*?-->)?\s*$", re.M)

MD_EXT = ["tables", "attr_list", "md_in_html", "sane_lists", "toc"]
MD_CFG = {"toc": {"permalink": False, "slugify": lambda v, sep: re.sub(r"[^\w]+", sep, v.lower(), flags=re.U).strip(sep)}}


def md_to_html(text, draft=True):
    text = fix_text(text)
    text = FIG_RE.sub(lambda m: figure_html(m.group(1), draft), text)
    text = TABLECAP_RE.sub(lambda m: f'\n<p class="table-caption">{esc(m.group(1))} {m.group(2) or ""}</p>\n\n', text)

    def details(m):
        inner = md_to_html(m.group(2), draft)
        return (f'\n<details class="more"><summary>{esc(m.group(1))}<span class="summary-tag">Details</span></summary>'
                f'<div class="details-body">{inner}</div></details>\n')
    text = DETAILS_RE.sub(details, text)
    text = WIDGET_RE.sub(lambda m: f'\n<div data-widget="{m.group(1)}"></div>\n', text)
    text = src_notes(text)
    out = markdown.markdown(text, extensions=MD_EXT, extension_configs=MD_CFG)
    # callouts
    out = re.sub(r"<blockquote>\s*<p><strong>Callout:?</strong>:?\s*(.*?)</blockquote>",
                 lambda m: '<div class="callout"><p>' + m.group(1).strip() + "</div>", out, flags=re.S)
    out = re.sub(r"<blockquote>", '<blockquote class="callout">', out)
    # tables
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    out = re.sub(r"<td>([\s$~≈<>]*[\d,.]+\s*[%+]?\s*(?:<span class=\"src-note\".*?</span>)?)</td>", r'<td class="num">\1</td>', out)
    return out


def stats_html(body):
    items = []
    for line in body.splitlines():
        m = re.match(r"^\s*[-*]\s+\*\*(.+?)\*\*\s*\|?\s*(.*)$", line)
        if not m:
            continue
        num, label = m.group(1).strip(), m.group(2).strip()
        label_html = src_notes(fix_text(label))
        label_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", label_html)
        label_html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", label_html)
        nm = re.match(r"^([~≈<>]?)([\d,]+(?:\.\d+)?)\s*([%+]?|\s*\w*)$", num)
        if nm and not nm.group(1):
            val = nm.group(2).replace(",", "")
            items.append(f'<div class="stat reveal"><div class="stat-num" data-count="{val}" data-suffix="{esc(nm.group(3))}">{esc(num)}</div>'
                         f'<div class="stat-label">{label_html}</div></div>')
        else:
            cls = "stat-num" + (" stat-num-text" if len(num) > 6 else "")
            items.append(f'<div class="stat reveal"><div class="{cls}">{esc(num)}</div><div class="stat-label">{label_html}</div></div>')
    return '<div class="stats">' + "".join(items) + "</div>" if items else ""


def plain(html_text):
    t = re.sub(r'<span class="src-note".*?</span>', "", html_text, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def rebase(html_text, root):
    """Prefix site-relative links with root (for pages in subfolders)."""
    if not root:
        return html_text
    def fix(m):
        attr, q, url = m.group(1), m.group(2), m.group(3)
        if re.match(r"^(https?:|mailto:|tel:|#|/|\.\./|data:|javascript:)", url):
            return m.group(0)
        return f"{attr}={q}{root}{url}"
    return re.sub(r'\b(href|src|data-full)=(["\'])([^"\']+)', fix, html_text)


# ---------------------------------------------------------------- page shell
ICON = {
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    "theme": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "chev": '<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="m2 3.5 3 3 3-3"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="m6 15 6-6 6 6"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
}


CUR = ' aria-current="page"'


def nav_html(current):
    items = []
    for entry in NAV:
        if isinstance(entry[1], list):
            label, links = entry
            has_cur = any(href == current or (href == "groups.html" and current.startswith("groups/")) for href, _, _ in links)
            sub = "".join(
                f'<li><a href="{href}"{CUR if href == current else ""}>{esc(t)}<span class="dd-desc">{esc(d)}</span></a></li>'
                for href, t, d in links)
            items.append(f'<li class="{"has-current" if has_cur else ""}"><button class="nav-top" aria-expanded="false">{esc(label)} {ICON["chev"]}</button>'
                         f'<ul class="dropdown">{sub}</ul></li>')
        else:
            href, label, _ = entry
            items.append(f'<li><a href="{href}"{CUR if href == current else ""}>{esc(label)}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def header_html(current, draft):
    bar = ('<div class="draft-bar">DRAFT for partner review. Content is distilled from the MNLCP '
           f'({esc(PLAN_VERSION)}) and is not yet approved for public release.</div>') if draft else ""
    return f"""<a class="skip-link" href="#main">Skip to content</a>
{bar}
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{esc(SITE_NAME)} home">
      <img src="{BRAND['seal_dofaw']}" alt="" width="44" height="44">
      <span class="brand-text"><span class="brand-title">Maui Nui Landscape Conservation Plan</span><span class="brand-sub">Division of Forestry and Wildlife</span></span>
    </a>
    <nav class="nav" aria-label="Main">{nav_html(current)}</nav>
    <div class="header-tools">
      <button class="icon-btn" data-search-open aria-label="Search the site (Ctrl+K)">{ICON['search']}</button>
      <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">{ICON['theme']}</button>
      <button class="icon-btn menu-toggle" aria-label="Menu" aria-expanded="false">{ICON['menu']}</button>
    </div>
  </div>
</header>
<div class="search-panel" role="dialog" aria-label="Search">
  <div class="search-box">
    <label class="sr-only" for="site-search">Search</label>
    <input id="site-search" type="search" placeholder="Search the plan: species, actions, places, questions…" autocomplete="off">
    <ul class="search-results"></ul>
    <div class="search-hint">Enter to open · ↑ ↓ to move · Esc to close</div>
  </div>
</div>"""


PARTNER_LOGOS = []  # filled from the asset catalog: [(path, name)]


def footer_html(draft):
    cols = []
    for entry in NAV:
        if isinstance(entry[1], list):
            label, links = entry
            cols.append((label, [(h, t) for h, t, _ in links]))
    explore = cols[0][1] + cols[1][1]
    act = cols[2][1] + cols[3][1]
    more = [("faq.html", "Questions & Answers"), ("glossary.html", "Glossary"), ("resources.html", "Resources & Downloads"),
            ("groups.html", "Taxonomic Groups")]
    def ul(links):
        return "<ul>" + "".join(f'<li><a href="{h}">{esc(t)}</a></li>' for h, t in links) + "</ul>"
    logos = "".join(f'<img src="{esc(p)}" alt="{esc(n)}" title="{esc(n)}" loading="lazy">' for p, n in PARTNER_LOGOS)
    partners = (f'<div class="footer-partners"><div class="wrap"><p>Developed with our partners</p>'
                f'<div class="logo-wall">{logos}</div></div></div>') if logos else ""
    review = ('<button class="pill" data-sources-toggle aria-pressed="false" style="font-size:.75rem;padding:4px 10px">Show plan sources</button>'
              if draft else "")
    return f"""<footer class="site-footer">
  <div class="footer-main"><div class="wrap footer-grid">
    <div class="footer-about">
      <h2>{esc(SITE_NAME)}</h2>
      <p>A landscape-scale roadmap to prevent extinctions, recover at-risk species and restore native ecosystems across Maui, Molokaʻi, Lānaʻi and Kahoʻolawe. Led by the {esc(AGENCY)}.</p>
      <p class="small">Plan {esc(PLAN_VERSION)}. Subject to periodic review and revision.</p>
    </div>
    <div><h2>The plan</h2>{ul(explore)}</div>
    <div><h2>Taking action</h2>{ul(act)}</div>
    <div><h2>More</h2>{ul(more)}</div>
  </div></div>
  {partners}
  <div class="footer-band">
    <div class="wrap">
      <div class="footer-seals">
        <img src="{BRAND['seal_dlnr']}" alt="Department of Land and Natural Resources, State of Hawaiʻi seal">
        <img src="{BRAND['seal_dofaw']}" alt="Division of Forestry and Wildlife seal">
        <span class="agency">Forestry &amp; Wildlife</span>
      </div>
      <div class="footer-motto"><span class="motto">E mālama kākou i ka ʻāina</span><a href="https://dlnr.hawaii.gov/dofaw/">dlnr.hawaii.gov/dofaw</a></div>
    </div>
  </div>
  <div class="footer-legal"><div class="wrap">
    <span>© State of Hawaiʻi, Department of Land and Natural Resources, Division of Forestry and Wildlife</span>
    {review}
  </div></div>
</footer>
<div class="back-top"><button class="round-btn" aria-label="Back to top">{ICON['up']}</button></div>"""


def page_shell(out, title, description, body, draft, extra_head="", extra_scripts="", body_class=""):
    root = "../" * out.count("/")
    robots = '<meta name="robots" content="noindex, nofollow">' if draft else ""
    full_title = f"{title} | {SITE_SHORT}" if title != SITE_NAME else SITE_NAME
    doc = f"""<!doctype html>
<html lang="en" class="no-js" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#1a4126">
<link rel="icon" href="{BRAND['seal_dofaw']}">
<link rel="stylesheet" href="assets/css/site.css">
{extra_head}
</head>
<body class="{body_class}">
{header_html(out, draft)}
<main id="main">
{body}
</main>
{footer_html(draft)}
<script src="assets/js/site.js"></script>
{extra_scripts}
</body>
</html>
"""
    return rebase(doc, root)


def page_hero(title, lede, kicker=None, hero=None, crumbs=None):
    media = ""
    cls = "page-hero"
    if hero and (SITE / hero).exists():
        media = f'<div class="page-hero-media"><img src="{esc(hero)}" alt=""></div>'
        cls += " has-image"
    crumb = ""
    if crumbs:
        crumb = '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a>' + "".join(
            f'<span aria-hidden="true">/</span><a href="{h}">{esc(t)}</a>' if h else f'<span aria-hidden="true">/</span><span>{esc(t)}</span>'
            for h, t in crumbs) + "</nav>"
    k = f'<span class="kicker">{esc(kicker)}</span>' if kicker else ""
    return f"""<section class="{cls}">{media}<div class="wrap">{crumb}{k}<h1>{esc(title)}</h1>{'<p class="lede">' + lede + '</p>' if lede else ''}</div></section>"""


# ---------------------------------------------------------------- generic page
SEARCH = []


def index_for_search(page_title, url, html_body):
    chunks = re.split(r'(<h[23][^>]*id="[^"]+"[^>]*>.*?</h[23]>)', html_body, flags=re.S)
    current_title, current_id, buf = page_title, "", []
    def flush():
        text = plain(" ".join(buf))
        if text:
            SEARCH.append({"page": page_title, "title": current_title, "url": url + (f"#{current_id}" if current_id else ""), "text": text[:600]})
    for c in chunks:
        m = re.match(r'<h[23][^>]*id="([^"]+)"[^>]*>(.*?)</h[23]>', c, flags=re.S)
        if m:
            flush()
            current_id, current_title, buf = m.group(1), plain(m.group(2)), []
        else:
            buf.append(c)
    flush()


def render_markdown_page(out, cfg, draft, widgets):
    meta, text = parse_front_matter(read(CONTENT / "pages" / cfg["md"]))
    sections = split_sections(text)
    lede, stats, body_parts = "", "", []
    for head, body in sections:
        h = head.lower()
        if h == "lead":
            lede_md = strip_src(fix_text(body)).strip()
            lede = markdown.markdown(lede_md).replace("<p>", "").replace("</p>", " ").strip()
        elif h in ("key numbers", "at a glance numbers"):
            stats = stats_html(body)
        elif head:
            body_parts.append(f"## {head}\n{body}")
        elif body.strip():
            body_parts.append(body)
    body_html = md_to_html("\n\n".join(body_parts), draft)
    for name, fn in widgets.items():
        body_html = body_html.replace(f'<div data-widget="{name}"></div>', fn())
    title = meta.get("title", out)
    crumbs = []
    if cfg.get("parent"):
        crumbs.append(cfg["parent"])
    crumbs.append((None, meta.get("nav_label", title)))
    kicker = cfg.get("section")
    if cfg.get("group"):
        hn = meta.get("hawaiian_names")
        kicker = "Taxonomic group" + (f" · {hn if isinstance(hn, str) else ', '.join(hn)}" if hn else "")
    hero = page_hero(title, lede, kicker, cfg.get("hero"), crumbs)
    stats_block = f'<section class="section-tight band-soft"><div class="wrap">{stats}</div></section>' if stats else ""
    group_attr = f' data-group="{cfg["group"]}"' if cfg.get("group") else ""
    body = f"""{hero}
{stats_block}
<div class="page-body"><div class="wrap with-toc">
  <aside class="toc" aria-label="On this page"><h2>On this page</h2><ol></ol></aside>
  <article class="prose" data-toc data-glossary{group_attr}>{body_html}</article>
</div></div>"""
    index_for_search(meta.get("nav_label", title), out, body_html)
    scripts = cfg.get("scripts", "")
    return page_shell(out, title, meta.get("summary", ""), body, draft, extra_scripts=scripts), meta


# ---------------------------------------------------------------- data
def compile_data():
    DATA_OUT.mkdir(parents=True, exist_ok=True)
    data = {}
    for f in sorted((CONTENT / "data").glob("*.json")):
        try:
            data[f.stem] = json.loads(read(f))
        except json.JSONDecodeError as e:
            print(f"  ! {f.name}: invalid JSON ({e})", file=sys.stderr)
    groups = []
    for k in ("groups_part1", "groups_part2"):
        groups += data.get(k, {}).get("groups", [])
    if groups:
        data["groups"] = {"_source": "content/data/groups_part1.json + groups_part2.json", "groups": groups}
    for k in ("groups_part1", "groups_part2", "asset_catalog"):
        data.pop(k, None)
    for name, obj in data.items():
        js = (f"/* Generated by tools/build.py from content/data. Do not edit by hand. */\n"
              f"window.MNLCP_DATA = window.MNLCP_DATA || {{}};\n"
              f"window.MNLCP_DATA[{json.dumps(name)}] = {json.dumps(obj, ensure_ascii=False)};\n")
        (DATA_OUT / f"{name}.js").write_text(js, encoding="utf-8")
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", action="store_true", help="public build: no draft banner or review aids")
    args = ap.parse_args()
    draft = not args.release

    sys.path.insert(0, str(Path(__file__).parent))
    import pages_special as special  # page builders that need custom layouts

    data = compile_data()
    special.init(globals(), data, draft)
    built = []
    for out, cfg in PAGES.items():
        if not (CONTENT / "pages" / cfg["md"]).exists():
            print(f"  - skip {out}: missing content/pages/{cfg['md']}")
            continue
        cfg = dict(cfg, **special.page_overrides(out))
        html_out, _ = render_markdown_page(out, cfg, draft, special.widgets_for(out))
        (SITE / out).parent.mkdir(parents=True, exist_ok=True)
        (SITE / out).write_text(html_out, encoding="utf-8")
        built.append(out)
    for out, html_out in special.build_special():
        (SITE / out).write_text(html_out, encoding="utf-8")
        built.append(out)

    search_js = ("/* Generated by tools/build.py. */\nwindow.MNLCP_DATA = window.MNLCP_DATA || {};\n"
                 f"window.MNLCP_DATA.search = {json.dumps(SEARCH, ensure_ascii=False)};\n")
    (DATA_OUT / "search.js").write_text(search_js, encoding="utf-8")
    print(f"Built {len(built)} pages ({'draft' if draft else 'release'}), {len(SEARCH)} search entries.")


if __name__ == "__main__":
    main()
