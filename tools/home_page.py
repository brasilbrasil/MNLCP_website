"""Homepage layout for tools/build.py, assembled from content/pages/home.md."""
import re


def build(B, DATA, draft, group_cards_html):
    esc, md = B["esc"], B["md_to_html"]
    meta, text = B["parse_front_matter"]((B["CONTENT"] / "pages" / "home.md").read_text(encoding="utf-8"))
    sec = {h.lower(): body for h, body in B["split_sections"](text)}

    def body_of(key):
        for k, v in sec.items():
            if k.startswith(key):
                return v
        return ""

    def strip_links(t):
        """Drop the trailing 'Read more' link lines; the layout supplies its own buttons."""
        return re.sub(r"^\[[^\]]+\]\([^)]+\)(\s*·\s*\[[^\]]+\]\([^)]+\))*\s*$", "", t, flags=re.M)

    def split_callout(t):
        m = re.search(r"^> \*\*Callout:\*\*\s*(.+)$", t, flags=re.M)
        if not m:
            return t, ""
        return t.replace(m.group(0), ""), B["src_notes"](B["fix_text"](m.group(1)))

    hero_img = "assets/img/photos/hero_misty_ohia_forest.jpg"
    lede = B["strip_src"](B["fix_text"](sec.get("lead", ""))).strip()
    stats = B["stats_html"](sec.get("key numbers", ""))

    # Challenge
    ch_text, ch_call = split_callout(body_of("the challenge"))
    threats = [("threat_rat.jpg", "Rats"), ("threat_feral_goat.jpg", "Feral ungulates"),
               ("threat_rosy_wolfsnail_eating_native_snail.jpg", "Rosy wolfsnail"),
               ("threat_feral_cat_camera_trap.jpg", "Feral cats")]
    threat_imgs = "".join(
        f'<figure style="margin:0"><img src="assets/img/photos/{f}" alt="{esc(a)}" loading="lazy" style="aspect-ratio:1;object-fit:cover;width:100%;border-radius:12px;border:0">'
        f'<figcaption style="margin-top:6px;font-size:.8rem">{esc(a)}</figcaption></figure>'
        for f, a in threats if (B["SITE"] / "assets/img/photos" / f).exists())
    challenge = f"""<section class="section"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">The challenge</span><h2 class="mt-0">One of the most severe extinction crises in the nation</h2>
  <div class="prose" data-glossary>{md(strip_links(ch_text), draft)}</div></div>
  <div class="reveal"><div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">{threat_imgs}</div>
  {'<div class="callout" style="margin-top:20px"><p>' + ch_call + '</p></div>' if ch_call else ''}</div>
</div></section>"""

    # Goals
    goals_md = body_of("three integrated goals")
    goals = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*\s*(.+)$", goals_md, flags=re.M)
    goal_cards = "".join(f'<div class="card goal reveal"><h3>{esc(t)}</h3><p>{esc(B["fix_text"](d))}</p></div>' for t, d in goals)
    goals_html = f"""<section class="section band-soft"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What the plan sets out to do</span><h2>Three integrated goals</h2></div>
  <div class="grid grid-3 goals">{goal_cards}</div>
  <p style="margin-top:24px"><a class="btn btn-outline" href="plan.html">About the plan {B['ICON']['arrow']}</a></p>
</div></section>"""

    # Who / where / what / when
    wwh_md = body_of("who, where, what")
    intro = B["strip_src"](wwh_md.split("\n- ")[0]).strip()
    qs = re.findall(r"^- \*\*(.+?)\*\*\s*(.+)$", wwh_md, flags=re.M)
    eco = re.search(r"^Ecosystem prioritization.+$", wwh_md, flags=re.M)
    leads = {"who": "Taxonomic Teams · DOFAW", "where": "Spatial prioritization · USGS-led", "what": "Action prioritization · UH Mānoa-led", "when": "Implementation · DOFAW-led"}
    items = []
    for q, d in qs:
        key = q.split()[0].lower()
        d_clean = B["strip_src"](B["fix_text"](d))
        d_clean = re.sub(r"\s*This work was led by [^.]+\.", "", d_clean)
        items.append(f'<div class="wwh-item reveal"><div class="wwh-q">{esc(q.split()[0])}?</div><h3>{esc(q)}</h3><p>{esc(d_clean)}</p>'
                     f'<span class="wwh-lead">{esc(leads.get(key, ""))}</span></div>')
    wwh = f"""<section class="section band-forest"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Integrated Multi-Scale Conservation Planning</span><h2>Who, where, what and when</h2><p>{esc(B['fix_text'](intro))}</p></div>
  <div class="wwh">{''.join(items)}</div>
  {'<p style="margin-top:24px;max-width:760px">' + esc(B['strip_src'](B['fix_text'](eco.group(0)))) + '</p>' if eco else ''}
  <p style="margin-top:20px"><a class="btn btn-primary" href="approach.html">See how the approach works {B['ICON']['arrow']}</a></p>
</div></section>"""

    # Who needs help: chart + group cards
    groups = DATA.get("groups", {}).get("groups", [])
    chart = bar_chart(B, groups)
    who_md = body_of("who needs help")
    who_intro = who_md.split("[table:")[0]
    who = f"""<section class="section"><div class="wrap">
  <div class="split" style="align-items:start">
    <div class="reveal"><span class="eyebrow">Who needs help</span><h2 class="mt-0">442 at-risk species</h2><div class="prose">{md(who_intro, draft)}</div>
    <div class="btn-row"><a class="btn btn-solid" href="species.html">Explore the species</a><a class="btn btn-outline" href="groups.html">Taxonomic groups</a></div></div>
    <div class="chart reveal" style="position:relative">{chart}</div>
  </div>
  <div style="margin-top:48px">{group_cards_html()}</div>
</div></section>"""

    # Where to act
    where_md = body_of("where to act")
    where_md = re.sub(r"^\[figure:.*$", "", where_md, flags=re.M)
    fig = "assets/img/figures/plan_fig_02_combined_recovery_footprint.jpg"
    where = f"""<section class="section band-soft"><div class="wrap split">
  <div class="reveal"><span class="eyebrow">Where to act</span><h2 class="mt-0">Conservation footprints</h2><div class="prose" data-glossary>{md(strip_links(where_md), draft)}</div>
  <a class="btn btn-solid" href="footprints.html">Open the interactive map {B['ICON']['arrow']}</a></div>
  <figure class="zoomable reveal" style="margin:0"><img src="{fig}" alt="Map of Maui, Molokaʻi, Lānaʻi and Kahoʻolawe showing the combined recovery footprint in green and the priority footprint in yellow" loading="lazy">
  <figcaption>Combined recovery footprint for all taxonomic groups (green) and priority areas (yellow). Plan Executive Summary, Figure 1.</figcaption></figure>
</div></section>"""

    # What to do
    what_md = body_of("what to do")
    what_intro = what_md.split("\n- ")[0]
    pts = re.findall(r"^- \*\*(.+?)\*\*\s*(.+)$", what_md, flags=re.M)
    cards = "".join(f'<div class="card reveal"><h3>{esc(t)}</h3><p>{B["src_notes"](B["fix_text"](d))}</p></div>' for t, d in pts)
    what = f"""<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What to do</span><h2>Priority conservation actions</h2><div class="prose" style="max-width:none">{md(what_intro, draft)}</div></div>
  <div class="grid grid-3">{cards}</div>
  <p style="margin-top:24px"><a class="btn btn-outline" href="actions.html">Explore priority actions {B['ICON']['arrow']}</a></p>
</div></section>"""

    # When + living plan
    when_md = body_of("when to act")
    living_md = body_of("a living plan")
    when = f"""<section class="section band-soft"><div class="wrap grid grid-2">
  <div class="card reveal"><span class="eyebrow">When to act</span><h3 style="font-size:1.5rem">Emergency first, then sequenced recovery</h3><div class="prose">{md(when_md, draft)}</div>
  <span class="card-more"><a href="using-the-plan.html">Using the plan</a></span></div>
  <div class="card reveal"><span class="eyebrow">A living plan</span><h3 style="font-size:1.5rem">Updated as conditions, knowledge and funding change</h3><div class="prose">{md(strip_links(living_md), draft)}</div>
  <span class="card-more"><a href="tools.html">The Adaptive Conservation Planner</a> · <a href="monitoring.html">Monitoring</a></span></div>
</div></section>"""

    # What success requires
    succ_md, succ_call = split_callout(body_of("what success requires"))
    success = f"""<section class="section band-forest"><div class="wrap split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">A finite, solvable challenge</span><h2 class="mt-0">What success requires</h2>
  {'<p style="font-size:1.2rem">' + succ_call + '</p>' if succ_call else ''}
  <div class="btn-row"><a class="btn btn-primary" href="partners.html">Partners &amp; teams</a><a class="btn btn-ghost" href="faq.html">Questions &amp; answers</a></div></div>
  <div class="prose reveal" style="color:var(--cream)">{md(strip_links(succ_md), draft)}</div>
</div></section>"""

    islands = "".join(f"<span>{i}</span>" for i in ["Maui", "Molokaʻi", "Lānaʻi", "Kahoʻolawe"])
    hero = f"""<section class="hero">
  <div class="hero-media"><img src="{hero_img}" alt="Misty native ʻōhiʻa forest on Maui" fetchpriority="high"></div>
  <div class="wrap">
    <span class="hero-kicker">Hawaiʻi Division of Forestry and Wildlife</span>
    <h1>{esc(meta.get('hero_title', 'Maui Nui Landscape Conservation Plan'))}</h1>
    <div class="hero-islands">{islands}</div>
    <p class="lede">{esc(meta.get('hero_subtitle', ''))}</p>
    <div class="btn-row" style="margin-top:22px">
      <a class="btn btn-primary" href="footprints.html">Explore where to act {B['ICON']['arrow']}</a>
      <a class="btn btn-ghost" href="plan.html">About the plan</a>
    </div>
  </div>
</section>
<section class="section-tight"><div class="wrap hero-stats">{stats}</div></section>"""

    body = hero + challenge + goals_html + wwh + who + where + what + when + success
    B["index_for_search"]("Home", "index.html", challenge + who + where + what + when)
    return B["page_shell"]("index.html", B["SITE_NAME"], meta.get("summary", ""), body, draft, extra_scripts='<script defer src="assets/js/widgets.js"></script>')


def bar_chart(B, groups):
    """Horizontal bar chart: at-risk species per group, with listed and imminent as marks."""
    esc = B["esc"]
    rows = [g for g in groups if g.get("at_risk")]
    if not rows:
        return ""
    rows.sort(key=lambda g: -g["at_risk"])
    W, rowh, left, right = 560, 40, 178, 44
    H = len(rows) * rowh + 54
    mx = max(g["at_risk"] for g in rows)
    sx = lambda v: (W - left - right) * v / mx
    parts = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="chart-t chart-d" style="width:100%;height:auto">'
             '<title id="chart-t">At-risk species by taxonomic group</title>'
             '<desc id="chart-d">Bars show the number of at-risk species in each group; the darker inner bar shows how many face imminent extinction.</desc>']
    for i, g in enumerate(rows):
        y = 10 + i * rowh
        w_all = max(4, sx(g["at_risk"]))
        w_imm = sx(g.get("imminent_extinction") or 0)
        tip = f'{g["name"]}: {g["at_risk"]} at risk, {g.get("listed") or 0} listed, {g.get("imminent_extinction") or 0} facing imminent extinction'
        parts.append(f'<g data-group="{g["slug"]}" class="bar-row"><title>{esc(tip)}</title>'
                     f'<rect x="0" y="{y - 4}" width="{W}" height="{rowh}" fill="transparent"/>'
                     f'<text x="{left - 10}" y="{y + 17}" text-anchor="end" font-size="13">{esc(g["name"])}</text>'
                     f'<rect x="{left}" y="{y + 4}" width="{w_all:.1f}" height="20" rx="4" style="fill:var(--gc)" fill-opacity=".35"/>'
                     + (f'<rect x="{left}" y="{y + 4}" width="{max(4, w_imm):.1f}" height="20" rx="4" style="fill:var(--gc)"/>' if w_imm else "")
                     + f'<text x="{left + w_all + 6:.1f}" y="{y + 19}" font-size="13" font-weight="700" style="fill:var(--ink)">{g["at_risk"]}</text></g>')
    ly = len(rows) * rowh + 26
    parts.append(f'<g font-size="12"><rect x="{left}" y="{ly}" width="14" height="12" rx="3" fill="#6b7d70" fill-opacity=".35"/>'
                 f'<text x="{left + 20}" y="{ly + 10}">At risk</text>'
                 f'<rect x="{left + 90}" y="{ly}" width="14" height="12" rx="3" fill="#6b7d70"/>'
                 f'<text x="{left + 110}" y="{ly + 10}">Facing imminent extinction</text></g></svg>')
    table = "".join(f'<tr><td>{esc(g["name"])}</td><td class="num">{g["at_risk"]}</td><td class="num">{g.get("listed") or 0}</td><td class="num">{g.get("imminent_extinction") or 0}</td></tr>' for g in rows)
    return ("".join(parts) +
            '<details class="more" style="margin:12px 0 0"><summary>View as a table<span class="summary-tag">Data</span></summary><div class="details-body">'
            '<div class="table-wrap" style="margin:0"><table><thead><tr><th>Group</th><th class="num">At risk</th><th class="num">Listed</th><th class="num">Imminent</th></tr></thead>'
            f'<tbody>{table}</tbody></table></div></div></details>'
            '<p class="small muted" style="margin:10px 0 0">Source: plan Table 1 (Executive Summary).</p>')
