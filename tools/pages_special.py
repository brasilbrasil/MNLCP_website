"""Custom page layouts and widgets for tools/build.py.

build.py calls init() with its globals, then page_overrides()/widgets_for() for each
markdown page, then build_special() for pages that are assembled from data
(home, groups index, footprints map, Q&A, glossary).
"""
import json
import math
import re

B = {}       # build.py globals (helpers, SITE, CONTENT, …)
DATA = {}
DRAFT = True


def init(build_globals, data, draft):
    global DRAFT
    B.update(build_globals)
    DATA.update(data)
    DRAFT = draft
    DATA["_cyanea_steps"] = CYANEA_STEPS
    catalog = load_catalog()
    logos = [(a["path"], (a.get("alt") or "").replace(" logo", "") or a.get("description", "")) for a in catalog
             if a.get("category") == "logo" and a.get("footer", True)
             and not any(k in a["path"] for k in ("dofaw", "dlnr_department", "unidentified"))]
    B["PARTNER_LOGOS"].extend(logos)


# How a recovery footprint is built: the Cyanea mceldowneyi example from the DOFAW MNLCP demo deck
# (slides 7-11 and their speaker notes). Plain-language captions; no facts beyond the deck.
CYANEA_STEPS = [
    {"src": "assets/img/screenshots/cyanea_step_01.png", "title": "Set an explicit recovery target",
     "text": "Planning starts with one species and its populations. For the plant Cyanea mceldowneyi, the recovery target is 10 populations of 400 individuals each: 4,000 plants in all.",
     "alt": "Plain basemap of Maui and Kahoʻolawe before any habitat is mapped"},
    {"src": "assets/img/screenshots/cyanea_step_02.png", "title": "Map suitable habitat",
     "text": "Species distribution models, checked on the ground, show where suitable habitat exists. Darker green planning units have higher modelled suitability.",
     "alt": "Windward East Maui planning units shaded light to dark green by modelled habitat suitability for Cyanea mceldowneyi"},
    {"src": "assets/img/screenshots/cyanea_step_03.png", "title": "Select recovery units",
     "text": "The best habitat is prioritized, and planning units are selected where management for each population would happen.",
     "alt": "The same suitability map with the selected recovery planning units hatched"},
    {"src": "assets/img/screenshots/cyanea_step_04.png", "title": "A recovery design tied to place",
     "text": "Ten selected units, one for each population, together meet the recovery target. Recovery is now linked to specific places on the map.",
     "alt": "Only the ten selected recovery units remain, outlined in black across windward East Maui"},
    {"src": "assets/img/screenshots/cyanea_step_05.png", "title": "Repeat for every species and integrate",
     "text": "The same steps are repeated for every at-risk species and integrated across all of them. The result is one recovery footprint where multi-species management can be planned efficiently.",
     "alt": "Recovery footprint for all at-risk plant species shown in green across Molokaʻi, Lānaʻi, Maui and Kahoʻolawe"},
]


def load_catalog():
    p = B["CONTENT"] / "data" / "asset_catalog.json"
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("assets", [])
    except json.JSONDecodeError:
        return []


def esc(s):
    return B["esc"](s)


def asset(path):
    return path if (B["SITE"] / path).exists() else None


DEFER = '<script defer src="assets/js/widgets.js"></script>'


def data_script(name):
    return f'<script src="assets/data/{name}.js"></script>'


def page_overrides(out):
    scripts = {
        "species.html": data_script("species") + DEFER,
        "approach.html": DEFER,
        "monitoring.html": DEFER,
        "actions.html": data_script("strategies") + '<script defer src="assets/js/actions.js"></script>',
        "resources.html": data_script("references") + DEFER,
        "tools.html": DEFER,
    }
    return {"scripts": scripts.get(out, DEFER)}


# ------------------------------------------------------------------ widgets
def w_species_explorer():
    return '<div data-species-explorer class="reveal is-visible"></div>'


IMCP_LAYOUT = {  # id: (x, y, w, h, fill) in a 760 x 572 viewBox; rows follow plan Figure 1
    "core_team": (20, 16, 200, 66, "#2f7337"),
    "imcp": (240, 16, 280, 66, "#12301b"),
    "communications": (540, 16, 200, 66, "#2f7337"),
    "taxon_teams": (20, 116, 720, 58, "#245f2c"),
    "spatial": (20, 210, 230, 92, "#1c5cab"),
    "action": (265, 210, 230, 92, "#b85a1f"),
    "ecosystem": (510, 210, 230, 92, "#0f7a55"),
    "optimtfe": (45, 314, 180, 44, "#256abf"),
    "implementation": (20, 392, 720, 60, "#1a4126"),
    "acp": (110, 494, 250, 62, "#3d4c41"),
    "monitoring": (400, 494, 250, 62, "#3d4c41"),
}
IMCP_ARROWS = [  # (x1, y1, x2, y2)
    (220, 49, 238, 49), (540, 49, 522, 49),            # Core Team and Communications -> IMCP
    (380, 82, 380, 114),                                # IMCP -> taxonomic teams
    (135, 174, 135, 208), (380, 174, 380, 208), (625, 174, 625, 208),
    (135, 314, 135, 304),                               # OptimTFE -> spatial
    (330, 302, 330, 390), (625, 302, 625, 390), (238, 336, 238, 390),
    (235, 452, 235, 492), (525, 452, 525, 492),
    (400, 525, 362, 525),                               # monitoring -> ACP (updates priorities)
]
QUESTION_SHORT = {"spatial": "WHERE?", "action": "WHAT?", "implementation": "WHEN?", "taxon_teams": "WHO NEEDS HELP?",
                  "ecosystem": "WHICH LANDSCAPES?", "monitoring": "IS IT WORKING?", "acp": "THE LIVING PLAN"}


def _wrap(text, n):
    lines, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    return lines + [cur]


def w_imcp():
    d = DATA.get("imcp_diagram")
    if not d:
        return ""
    info = {n["id"]: n for n in d["nodes"]}
    parts = ['<svg viewBox="0 0 760 572" role="img" aria-label="Diagram of how the parts of the MNLCP fit together">',
             '<defs><marker id="imcp-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
             '<path d="M0,0 L10,5 L0,10 z" fill="currentColor" fill-opacity=".45"/></marker></defs>']
    for x1, y1, x2, y2 in IMCP_ARROWS:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="currentColor" stroke-opacity=".4" stroke-width="2" marker-end="url(#imcp-arrow)"/>')
    for nid, (x, y, w, h, fill) in IMCP_LAYOUT.items():
        n = info.get(nid)
        if not n:
            continue
        label = re.sub(r"\s*\((?:IMCP|Priority Threat Management|TFE-SCP)\)", "", n["label"])
        q = QUESTION_SHORT.get(nid, "")
        lines = _wrap(label, max(12, int(w / 8.2)))
        block = (len(lines) * 17) + (16 if q else 0)
        ty = y + (h - block) / 2 + 12
        txt = ""
        if q:
            txt += f'<text x="{x + w / 2}" y="{ty:.0f}" text-anchor="middle" fill="#ffffff" fill-opacity=".8" font-size="11" font-weight="800" letter-spacing="1.2">{esc(q)}</text>'
            ty += 18
        for i, l in enumerate(lines):
            txt += f'<text x="{x + w / 2}" y="{ty + i * 17 + 2:.0f}" text-anchor="middle" fill="#ffffff" font-size="14.5" font-weight="700">{esc(l)}</text>'
        parts.append(f'<g class="node" data-id="{nid}" aria-label="{esc(n["label"])}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/>{txt}</g>')
    parts.append("</svg>")
    return (f'<div class="imcp imcp-stack" data-imcp>{"".join(parts)}<div class="imcp-detail" aria-live="polite"></div>'
            f'<script type="application/json">{json.dumps(info, ensure_ascii=False)}</script></div>'
            '<p class="small muted">Select any box to see what it does, who led it and what it produced. Adapted from plan Figure 1.</p>')


def w_cycle():
    d = DATA.get("monitoring")
    if not d:
        return ""
    steps = d["cycle_steps"]
    n = len(steps)
    cx = cy = 200
    r_out, r_in = 180, 108
    cols = ["#1a4126", "#245f2c", "#2f7337", "#4c8a37", "#6aab45", "#236c8e", "#3b5b8c", "#8b55a0"]
    gap = 0.03
    parts = ['<svg viewBox="0 0 400 400" role="img" aria-label="Adaptive management cycle">']
    for i, s in enumerate(steps):
        a0 = -math.pi / 2 + i * 2 * math.pi / n + gap
        a1 = -math.pi / 2 + (i + 1) * 2 * math.pi / n - gap
        def pt(r, a):
            return f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}"
        large = 1 if (a1 - a0) > math.pi else 0
        path = f"M{pt(r_out, a0)} A{r_out},{r_out} 0 {large} 1 {pt(r_out, a1)} L{pt(r_in, a1)} A{r_in},{r_in} 0 {large} 0 {pt(r_in, a0)} Z"
        am = (a0 + a1) / 2
        tx, ty = cx + (r_out + r_in) / 2 * math.cos(am), cy + (r_out + r_in) / 2 * math.sin(am)
        parts.append(f'<g class="seg-arc" style="opacity:.55"><path d="{path}" fill="{cols[i % len(cols)]}"/>'
                     f'<text x="{tx:.0f}" y="{ty + 7:.0f}" text-anchor="middle" fill="#fff" font-size="22" font-weight="800">{i + 1}</text></g>')
    parts.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" font-size="15" font-weight="700" fill="currentColor">Adaptive</text>'
                 f'<text x="{cx}" y="{cy + 14}" text-anchor="middle" font-size="15" font-weight="700" fill="currentColor">management</text></svg>')
    return (f'<div class="cycle" data-cycle>{"".join(parts)}<div class="imcp-detail" aria-live="polite"></div>'
            f'<script type="application/json">{json.dumps([{"title": s["title"], "description": s["description"]} for s in steps], ensure_ascii=False)}</script></div>')


def w_objective_cards():
    d = DATA.get("monitoring")
    if not d:
        return ""
    cards = "".join(
        f'<div class="card"><span class="card-tag">Objective type {i + 1}</span><h3>{esc(o["name"])}</h3>'
        f'<p><b>{esc(o["question"])}</b></p><p>{esc(o.get("example", ""))}</p></div>'
        for i, o in enumerate(d.get("objective_types", [])))
    return f'<div class="grid grid-3" style="margin:1.4em 0">{cards}</div>'


def w_eco_ladder():
    d = DATA.get("ecosystems")
    if not d:
        return ""
    items = []
    for p in sorted(d.get("priorities", []), key=lambda x: x["rank"]):
        areas = p.get("key_areas") or []
        area_txt = ""
        if areas:
            names = [a.get("name") if isinstance(a, dict) else str(a) for a in areas]
            area_txt = '<p class="small muted" style="margin-top:6px">Key areas: ' + esc("; ".join(n for n in names if n)) + "</p>"
        items.append(f'<li><div><h4>{esc(p["title"])}</h4><p class="small muted" style="margin:0 0 4px">{esc(p.get("category", ""))}</p>'
                     f'<p>{esc(p["description"])}</p>{area_txt}</div></li>')
    return '<ol class="ladder">' + "".join(items) + "</ol>"


def w_stepper():
    steps = DATA.get("_cyanea_steps")
    if not steps:
        return ""
    imgs = "".join(f'<img src="{esc(s["src"])}" alt="{esc(s["alt"])}" loading="lazy">' for s in steps)
    meta = json.dumps([{"title": s["title"], "text": s["text"]} for s in steps], ensure_ascii=False)
    return f"""<div class="stepper" data-stepper tabindex="0" aria-label="How a recovery footprint is built, step by step">
<div class="stepper-stage">{imgs}</div>
<div class="stepper-body"><div><h3></h3><p></p></div>
<div class="stepper-nav"><button class="round-btn" data-prev aria-label="Previous step">{B['ICON']['up'].replace('m6 15 6-6 6 6', 'm15 6-6 6 6 6')}</button><button class="round-btn" data-next aria-label="Next step">{B['ICON']['arrow']}</button></div></div>
<div class="stepper-dots"></div>
<script type="application/json">{meta}</script></div>"""


def w_references():
    d = DATA.get("references")
    if not d:
        return ""
    items = []
    for r in d["references"]:
        c = esc(r["citation"])
        if r.get("url"):
            c += f' <a href="{esc(r["url"])}">{esc(r["url"])}</a>'
        items.append(f'<li id="ref-{esc(r.get("id", ""))}">{c}</li>')
    return '<ol class="small" style="padding-left:1.4em">' + "".join(items) + "</ol>"


def w_group_cards():
    return group_cards_html()


def w_strategies():
    return '<div data-strategies></div>'


WIDGETS = {
    "strategies-explorer": w_strategies,
    "species-explorer": w_species_explorer,
    "imcp-diagram": w_imcp,
    "am-cycle": w_cycle,
    "objective-cards": w_objective_cards,
    "eco-ladder": w_eco_ladder,
    "footprint-stepper": w_stepper,
    "references": w_references,
    "group-cards": w_group_cards,
    "photo-credits": lambda: '<div data-widget="photo-credits"></div>',  # filled after all pages are built
}


def widgets_for(out):
    return WIDGETS


# ------------------------------------------------------------------ groups
def groups_data():
    g = DATA.get("groups", {}).get("groups", [])
    order = [s for s, _ in B["GROUPS"]]
    return sorted(g, key=lambda x: order.index(x["slug"]) if x.get("slug") in order else 99)


def fmt(v):
    if v is None:
        return "—"
    if isinstance(v, (int, float)):
        return f"{v:,.0f}"
    return str(v)


# Small deck photos (114-310 px) work only as thumbnails; species identifications are by eye (see asset notes).
GROUP_THUMBS = {
    "forest-birds": "assets/img/photos/bird_kiwikiu_banded_adult.jpg",
    "seabirds": "assets/img/figures/plate_uau_hawaiian_petrel_frohawk.jpg",
    "waterbirds": "assets/img/photos/bird_nene_portrait.jpg",
    "plants": "assets/img/photos/plant_clermontia_kakeana_flowers.jpg",
    "terrestrial-snails": "assets/img/photos/snail_tree_snail_on_leaf_underside.jpg",
    "terrestrial-arthropods": "assets/img/photos/arthropod_megalagrion_damselflies.jpg",
    "aquatic-invertebrates": "assets/img/photos/landscape_ohia_rocky_gulch.jpg",
}


def group_cards_html(limit_text=True):
    cards = []
    for g in groups_data():
        slug = g["slug"]
        img = asset(GROUP_THUMBS.get(slug, ""))
        cred = re.sub(r"<[^>]+>", "", B["credit_html"](img)) if img else ""
        media = f'<img class="group-thumb" src="{img}" alt="" title="{esc(cred)}" loading="lazy">' if img else ""
        path = {"expert-led": "Expert-led footprint", "algorithmic": "Algorithmic prioritization", "plan-only": "Plan strategy"}.get(g.get("prioritization_pathway"), "")
        cards.append(f"""<a class="card group-card reveal" data-group="{slug}" href="groups/{slug}.html">{media}
<span class="card-tag">{esc(path)}</span>
<h3>{esc(g['name'])}{(' <span class="muted" style="font-weight:400">· ' + esc(g['hawaiian_name']) + '</span>') if g.get('hawaiian_name') else ''}</h3>
<div class="group-stats"><div class="gs"><b>{fmt(g.get('at_risk'))}</b><span>at risk</span></div><div class="gs"><b>{fmt(g.get('listed'))}</b><span>listed</span></div><div class="gs"><b>{fmt(g.get('imminent_extinction'))}</b><span>imminent</span></div></div>
<p>{esc(g.get('one_line_summary', ''))}</p><span class="card-more">Explore the strategy {B['ICON']['arrow']}</span></a>""")
    return '<div class="grid grid-4">' + "".join(cards) + "</div>"


def build_groups_index():
    rows = []
    tot = {"at_risk": 0, "listed": 0, "imminent_extinction": 0}
    for g in groups_data():
        for k in tot:
            tot[k] += g.get(k) or 0
        threats = "; ".join(g.get("primary_threats", [])[:3])
        actions = "; ".join(g.get("top_actions", [])[:3])
        rows.append(f'<tr><td><a class="chip chip-dot" data-group="{g["slug"]}" href="groups/{g["slug"]}.html">{esc(g["name"])}</a></td>'
                    f'<td class="num">{fmt(g.get("at_risk"))}</td><td class="num">{fmt(g.get("listed"))}</td><td class="num">{fmt(g.get("imminent_extinction"))}</td>'
                    f'<td>{esc(threats)}</td><td>{esc(actions)}</td></tr>')
    rows.append(f'<tr><td><b>Total</b></td><td class="num"><b>{tot["at_risk"]}</b></td><td class="num"><b>{tot["listed"]}</b></td><td class="num"><b>{tot["imminent_extinction"]}</b></td><td></td><td></td></tr>')
    table = ('<div class="table-wrap"><table><thead><tr><th>Group</th><th class="num">At risk</th><th class="num">Listed</th><th class="num">Imminent extinction</th>'
             '<th>Primary threats</th><th>Highest-priority actions</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")
    body = (B["page_hero"]("Taxonomic Groups",
                           "Seven expert Taxonomic Teams, plus the Hawaiian hoary bat, shaped a recovery strategy for every group of at-risk species. Choose a group to see its species, threats, recovery footprint and priority actions.",
                           "Species", "assets/img/photos/landscape_native_forest_ridge_view.jpg", [(None, "Taxonomic Groups")])
            + f'<section class="section"><div class="wrap">{group_cards_html()}</div></section>'
            + f'<section class="section band-soft"><div class="wrap"><div class="section-head"><span class="eyebrow">At a glance</span><h2>All groups compared</h2>'
              f'<p>At-risk species by taxonomic group, the number listed under state and federal endangered species laws, the number facing imminent extinction, and the primary threats and highest-priority actions identified in the plan (Executive Summary, Table 1).</p></div>{table}</div></section>')
    for g in groups_data():
        B["SEARCH"].append({"page": "Taxonomic Groups", "title": g["name"], "url": f"groups/{g['slug']}.html", "text": g.get("one_line_summary", "")})
    return "groups.html", B["page_shell"]("groups.html", "Taxonomic Groups", "Recovery strategies for the eight taxonomic groups of at-risk species in the MNLCP.", body, DRAFT)


# ------------------------------------------------------------------ footprints map
def build_footprints():
    md = B["CONTENT"] / "pages" / "footprints.md"
    meta, text = B["parse_front_matter"](md.read_text(encoding="utf-8")) if md.exists() else ({}, "")
    sections = B["split_sections"](text)
    lede, stats, rest = "", "", []
    for head, body in sections:
        h = head.lower()
        if h == "lead":
            lede = B["strip_src"](B["fix_text"](body)).strip()
        elif h == "key numbers":
            stats = B["stats_html"](body)
        elif head:
            rest.append(f"## {head}\n{body}")
    body_html = B["md_to_html"]("\n\n".join(rest), DRAFT)
    for name, fn in WIDGETS.items():
        body_html = body_html.replace(f'<div data-widget="{name}"></div>', fn())
    B["index_for_search"]("Conservation Footprints", "footprints.html", body_html)
    colors = [("nested", "Footprint (recovery and priority)"), ("groups", "Number of taxon groups"), ("species", "Number of species targets"), ("hab_qual", "Habitat quality"),
              ("climate", "Climate resilience"), ("reserve_pct", "Share in biodiversity reserves"), ("ungulate_pct", "Share ungulate-managed"),
              ("access", "Accessibility"), ("fire", "Fire probability")]
    panel = f"""<div class="map-shell">
<aside class="map-panel" aria-label="Map controls">
  <span class="eyebrow">Where to act</span>
  <h1>Conservation Footprints</h1>
  <p>{B['md_to_html'](lede, DRAFT).replace('<p>', '').replace('</p>', '') if lede else 'Planning units (about 2 km² each) that hold the habitat needed to recover at-risk species.'}</p>
  <h2>Footprint</h2>
  <div class="seg" id="fp-view" role="group" aria-label="Footprint type">
    <button value="recovery">Recovery</button><button value="priority">Priority</button>
  </div>
  <p class="small muted" style="margin-top:8px">Showing <b id="fp-shown">0</b> of <span id="fp-total">0</span> planning units.</p>
  <h2>Colour units by</h2>
  <select class="select" id="fp-color" aria-label="Colour planning units by" style="width:100%">
    {''.join(f'<option value="{v}">{esc(l)}</option>' for v, l in colors)}
  </select>
  <div class="legend" id="fp-legend" style="margin-top:12px"></div>
  <h2>Taxon groups <button class="pill" id="fp-all" style="float:right;padding:3px 10px;font-size:.75rem">All / none</button></h2>
  <ul class="layer-list" id="fp-groups"></ul>
  <h2>Basemap</h2>
  <div class="seg" id="fp-base" role="group" aria-label="Basemap"><button value="none">Clean</button><button value="topo">Topo</button><button value="imagery">Imagery</button><button value="light">Light</button></div>
  <div id="pu-card"><p class="small muted" style="margin-top:18px">Select a planning unit on the map to see which groups it supports and how it scores on the planning criteria.</p></div>
  <p class="small muted" style="margin-top:18px">Data: MNLCP release-candidate footprints, September 25, 2026, as loaded in the Adaptive Conservation Planner. Species names are not shown on this public map. <a href="#about-the-map">About the map</a></p>
</aside>
<div id="map" role="region" aria-label="Interactive map of conservation footprints"></div>
</div>"""
    stats_block = f'<section class="section-tight band-soft"><div class="wrap">{stats}</div></section>' if stats else ""
    body = (panel + stats_block +
            f'<div class="page-body" id="about-the-map"><div class="wrap with-toc"><aside class="toc" aria-label="On this page"><h2>On this page</h2><ol></ol></aside>'
            f'<article class="prose" data-toc data-glossary>{body_html}</article></div></div>')
    head = '<link rel="stylesheet" href="assets/vendor/leaflet/leaflet.css">'
    scripts = ('<script src="assets/vendor/leaflet/leaflet.js"></script><script src="assets/data/footprints.js"></script>'
               '<script src="assets/js/map.js"></script>' + DEFER)
    return "footprints.html", B["page_shell"]("footprints.html", meta.get("title", "Conservation Footprints"),
                                              meta.get("summary", "Interactive map of MNLCP recovery and priority footprints."),
                                              body, DRAFT, extra_head=head, extra_scripts=scripts)


# ------------------------------------------------------------------ FAQ
def build_faq():
    d = DATA.get("faq")
    if not d:
        return None
    md = B["CONTENT"] / "pages" / "faq.md"
    meta, text = B["parse_front_matter"](md.read_text(encoding="utf-8")) if md.exists() else ({}, "")
    lede = ""
    for head, body in B["split_sections"](text):
        if head.lower() == "lead":
            lede = B["strip_src"](B["fix_text"](body)).strip()
    pills = ['<button class="pill" data-cat="" aria-pressed="true">All</button>'] + [
        f'<button class="pill" data-cat="{esc(c["id"])}" aria-pressed="false">{esc(c["title"])}</button>' for c in d["categories"]]
    cats = []
    total = 0
    for c in d["categories"]:
        qas = []
        for q in c["questions"]:
            total += 1
            ans = B["md_to_html"](q["a"], DRAFT)
            badge = '<div class="qa-meta"><span class="badge-review">Needs DOFAW input</span></div>' if (DRAFT and q.get("status") == "needs_dofaw_input") else ""
            qas.append(f'<details class="qa" id="{esc(q["id"])}"><summary>{esc(B["fix_text"](q["q"]))}</summary><div class="qa-body">{ans}{badge}</div></details>')
            B["SEARCH"].append({"page": "Q&A", "title": q["q"], "url": f"faq.html#{q['id']}", "text": B["plain"](ans)[:400]})
        cats.append(f'<section class="faq-cat" id="{esc(c["id"])}"><h2>{esc(c["title"])}</h2>'
                    f'<p>{esc(c.get("description", ""))}</p>{"".join(qas)}</section>')
    body = (B["page_hero"](meta.get("title", "Questions & Answers"), B["md_to_html"](lede, DRAFT).replace("<p>", "").replace("</p>", "") if lede else "",
                           "Q&A", "assets/img/photos/plant_native_seedling_in_mist_nakula.jpg", [(None, "Q&A")])
            + f'<div class="page-body"><div class="wrap wrap-narrow" data-faq>'
              f'<div class="faq-tools"><input class="input" type="search" placeholder="Search {total} questions" aria-label="Search questions"><span class="small muted" data-faq-count></span></div>'
              f'<div class="pill-row" style="margin-bottom:30px">{"".join(pills)}</div>'
              f'<div class="prose" style="max-width:none" data-glossary>{"".join(cats)}</div>'
              f'<div class="callout" style="margin-top:40px"><p><b>Have a question that is not answered here?</b> See <a href="resources.html">Resources</a> for how to contact the MNLCP team.</p></div>'
              f"</div></div>")
    return "faq.html", B["page_shell"]("faq.html", "Questions & Answers", meta.get("summary", "Common questions about the Maui Nui Landscape Conservation Plan."), body, DRAFT, extra_scripts=DEFER)


# ------------------------------------------------------------------ glossary
def anchor(s):
    return re.sub(r"[^\w]+", "-", s.lower()).strip("-")


def build_glossary():
    d = DATA.get("glossary")
    if not d:
        return None
    terms = sorted(d["terms"], key=lambda t: re.sub(r"[^a-z]", "", t["term"].lower().replace("ʻ", "")))
    out, letter = [], None
    for t in terms:
        L = re.sub(r"[^A-Z]", "", t["term"].upper().replace("ʻ", ""))[:1] or "#"
        if L != letter:
            letter = L
            out.append(f'<h2 class="gloss-letter" id="letter-{L}">{L}</h2>')
        tid = anchor(t["term"])
        also = ""
        if t.get("aliases"):
            also += f' <span class="muted small">({esc(", ".join(t["aliases"]))})</span>'
        see = ""
        if t.get("see_also"):
            see = '<p class="small muted">See also: ' + ", ".join(
                f'<a href="#{anchor(s)}">{esc(s)}</a>' for s in t["see_also"]) + "</p>"
        out.append(f'<div class="gloss-entry" id="{tid}"><h3>{esc(t["term"])}{also}</h3><p>{esc(t["definition"])}</p>{see}</div>')
        B["SEARCH"].append({"page": "Glossary", "title": t["term"], "url": f"glossary.html#{tid}", "text": t["definition"]})
    letters = sorted({re.sub(r"[^A-Z]", "", t["term"].upper().replace("ʻ", ""))[:1] for t in terms} - {""})
    az = '<div class="pill-row" style="margin-bottom:24px">' + "".join(f'<a class="pill" href="#letter-{l}">{l}</a>' for l in letters) + "</div>"
    body = (B["page_hero"]("Glossary", "Terms and definitions used in the Maui Nui Landscape Conservation Plan. Terms with a dotted underline elsewhere on the site show these definitions when you hover over or focus them.",
                           "Reference", None, [(None, "Glossary")])
            + f'<div class="page-body"><div class="wrap wrap-narrow" data-glossary-filter>'
              f'<div class="faq-tools"><input class="input" type="search" placeholder="Filter terms" aria-label="Filter glossary terms"></div>{az}'
              f'<div class="prose" style="max-width:none">{"".join(out)}</div></div></div>')
    return "glossary.html", B["page_shell"]("glossary.html", "Glossary", "Terms and definitions used in the MNLCP.", body, DRAFT, extra_scripts=DEFER)


# ------------------------------------------------------------------ home
def build_home():
    import home_page
    return "index.html", home_page.build(B, DATA, DRAFT, group_cards_html)


def build_special():
    out = []
    for fn in (build_groups_index, build_footprints, build_faq, build_glossary, build_home):
        try:
            r = fn()
        except ImportError as e:
            print(f"  - skip {fn.__name__}: {e}")
            continue
        if r:
            out.append(r)
    return out
