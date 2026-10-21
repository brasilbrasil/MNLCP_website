"""Parse MNLCP Appendices 3, 4, 6, 7 (plus Ch 6 Tables 5, 9, 13, 21, 23) into species.json."""
import json, re, sys, collections

PLAN = "/hdd/projects/maui_nui_scp/maui_nui_products/project_context_docs/IMPORTANT/MNLCP 9-30-2026 FINAL.txt"
OUT = "/hdd/projects/maui_nui_scp/MNLCP_website/content/data/species.json"
L = open(PLAN, encoding="utf-8").read().split("\n")


def line(n):
    return L[n - 1]


def okina(s):
    s = s.replace("`", "ʻ").replace("''", "'")
    return s


def norm(name):
    """Normalise a name for cross-table matching."""
    n = name.lower().replace("subsp.", "ssp.").replace("  ", " ").strip()
    n = re.sub(r"\s+", " ", n)
    return n

# ---------------- Appendix 3 ----------------
GROUP_MAP = {
    "Aquatic Invertebrates": "Aquatic invertebrates",
    "Bats": "Hawaiian hoary bat",
    "Forest Birds": "Forest birds",
    "Plants": "Plants",
    "Seabirds": "Seabirds",
    "Terrestrial Arthropods": "Terrestrial arthropods",
    "Terrestrial Snails": "Terrestrial snails",
    "Waterbirds": "Waterbirds",
}
app3 = []
for n in range(6590, 7075):
    s = line(n)
    m = re.match(r"^(Aquatic Invertebrates|Bats|Forest Birds|Plants|Seabirds|Terrestrial Arthropods|Terrestrial Snails|Waterbirds)\s{2,}(.*)$", s)
    if not m:
        continue
    grp, rest = m.group(1), m.group(2).rstrip()
    parts = re.split(r"\s{2,}", rest, maxsplit=1)
    sci = parts[0]
    com = parts[1] if len(parts) > 1 else None
    # two rows where only one space separates name and common name (lines 6615, 6770)
    for full, tail in (("Argyroxiphium sandwicense subsp. macrocephalum", "`Ahinahina"),
                       ("Pseudognaphalium sandwicensium var. molokaiense", "`Ena`ena")):
        if sci.startswith(full + " "):
            sci, com = full, sci[len(full) + 1:]
    app3.append(dict(line=n, group_raw=grp, group=GROUP_MAP[grp], sci=sci.strip(), common_raw=com))

# ---------------- Appendix 4 (plants) ----------------
app4 = {}
for n in range(7084, 7335):
    s = line(n).rstrip()
    m = re.match(r"^(\S.*?)\s{2,}(\d+)\s+(.*)$", s)
    if not m or s.startswith("Appendix") or "Species" in s[:30] and "At-Risk" in s:
        continue
    name, occ, rest = m.group(1), int(m.group(2)), m.group(3).split()
    status = pepp = None
    if rest and rest[0] in ("E", "T"):
        status = rest.pop(0)
    if rest and rest[0] in ("PEPP", "POP", "ROI", "NO"):
        pepp = rest.pop(0)
    assert len(rest) == 3 and all(x.isdigit() for x in rest), (n, s)
    app4[norm(name)] = dict(line=n, name=name, occ=occ, status=status, pepp=pepp,
                            desired=int(rest[0]), rec_pus=int(rest[1]), occ_in_fp=int(rest[2]))

# ---------------- column-position parser (App 6, App 7, Tables) ----------------
def header_cols(hdr):
    """Return list of (label, centre) for the column header line."""
    cols = []
    for m in re.finditer(r"\S+", hdr):
        cols.append((m.group(0), (m.start() + m.end()) / 2))
    return cols


def parse_positional(start, end, first_word, labels):
    """Rows between start..end. Header line begins with first_word; labels are the
    data-column names in order matching the header tokens after the row label."""
    rows = {}
    hdr = None
    for n in range(start, end + 1):
        s = line(n)
        if s.strip().startswith(first_word) and ("Surveys" in s):
            toks = header_cols(s)
            # drop leading label words (e.g. 'Terrestrial', 'Arthropods')
            toks = toks[len(first_word.split()):]
            assert len(toks) == len(labels), (n, toks)
            hdr = [(lab, c) for lab, (_, c) in zip(labels, toks)]
            continue
        if hdr is None or not s.strip() or s.startswith(" "):
            continue
        if re.match(r"^(Total|Endangered|Facing|Interim|Full|Recovery|Focal|Basic)", s):
            continue
        m = re.match(r"^(\S.*?)(\s{2,}|$)", s)
        if not m or s.startswith("Appendix"):
            continue
        name = m.group(1)
        vals = {}
        for t in re.finditer(r"\S+", s[m.end(1):]):
            c = m.end(1) + (t.start() + t.end()) / 2
            lab = min(hdr, key=lambda h: abs(h[1] - c))[0]
            assert lab not in vals, (n, s)
            vals[lab] = t.group(0)
        rows[norm(name)] = dict(line=n, name=name, **vals)
    return rows

app6 = parse_positional(7482, 7542, "Terrestrial Snails",
                        ["current_pop", "esa", "imminent", "interim", "full", "area", "species_survey"])
app7 = parse_positional(7554, 7763, "Terrestrial Arthropods",
                        ["occ", "esa", "imminent", "interim", "full", "area", "species_survey"])
t21 = parse_positional(2885, 2898, "Aquatic Invertebrates",
                       ["occ", "esa", "imminent", "interim", "full", "area", "species_survey"])

# ---------------- hand-entered vertebrate rows (Ch 6 tables; names wrap so parse by hand) ----------------
VERT = {
    # sci: (src, current_pops, listing, imminent, recovery_type, recovery_value, hawaiian, common, islands, extra)
    "Pseudonestor xanthophrys": ("Table 5, line 1478; text lines 1425-1432", 1, "Endangered", True, "Full recovery", "3",
                                 "Kiwikiu", "Maui parrotbill", ["Maui"], {}),
    "Palmeria dolei": ("Table 5, lines 1479-1481; text lines 1434-1441", 1, "Endangered", True, "Full recovery", "3",
                       "ʻĀkohekohe", "Crested honeycreeper", ["Maui"], {}),
    "Drepanis coccinea": ("Table 5, line 1482; text lines 1443-1448", 1, "Threatened (federal); State endangered on Oʻahu, Molokaʻi and Lānaʻi", False,
                          "Full recovery", "3", "ʻIʻiwi", None, ["Maui"], {}),
    "Paroreomyza montana newtoni": ("Table 5, line 1483; text lines 1450-1455", 1, "Not listed", False, "Full recovery", "3",
                                    "Maui ʻalauahio", "Maui creeper", ["Maui"], {}),
    "Pterodroma sandwichensis": ("Table 9, line 1685; text lines 1661-1663", 3, "Endangered", False, "Full recovery", None,
                                 "ʻUaʻu", "Hawaiian petrel", None, {}),
    "Puffinus newelli": ("Table 9, lines 1686-1688; text lines 1664-1666", 3, "Threatened", False, "Full recovery", None,
                         "ʻAʻo", "Newell's shearwater", None, {}),
    "Hydrobates castro": ("Table 9, lines 1689-1691; text lines 1670-1673", 3, "Endangered (Hawaiʻi distinct population segment)", False,
                          "Full recovery", None, "ʻAkēʻakē", "Band-rumped storm-petrel", None,
                          {"name_note": "Ch 6b text (line 1670) uses the synonym Oceanodroma castro."}),
    "Fulica alai": ("Table 13, lines 1856-1858; text lines 1830-1831", 3, "Endangered", False, "Full recovery", None,
                    "ʻAlae keʻokeʻo", "Hawaiian coot", None, {}),
    "Himantopus mexicanus knudseni": ("Table 13, line 1859; text lines 1832-1834", 3, "Endangered", False, "Full recovery", None,
                                      "ʻAeʻo", "Hawaiian stilt", None, {}),
    "Branta sandvicensis": ("Table 13, line 1860; text lines 1835-1836", 2, "Threatened (federal); Endangered (State)", False,
                            "Full recovery", None, "Nēnē", "Hawaiian goose", None, {}),
    "Gallinula galeata sandvicensis": ("Table 13, lines 1861-1863; text lines 1837-1839", 0, "Endangered", False, "Interim recovery", None,
                                       "ʻAlae ʻula", "Hawaiian common gallinule", None,
                                       {"distribution_note": "Currently not found on Maui Nui (plan line 1839).",
                                        "name_note": "Ch 6c calls it Hawaiian moorhen (lines 1837, 1863); App 3 calls it Hawaiian common gallinule."}),
    "Anas wyvilliana": ("Table 13, lines 1864-1866; text lines 1842-1844", 0, "Endangered", False, "Interim recovery", None,
                        "Kōloa maoli", "Hawaiian duck", None,
                        {"distribution_note": "All kōloa-like ducks in Maui Nui are apparently kōloa-mallard hybrids (plan lines 1843-1844)."}),
    "Lasiurus semotus": ("Table 23, line 3150; text lines 3122-3124", 3, "Endangered", False, "Interim recovery", None,
                         "ʻŌpeʻapeʻa", "Hawaiian hoary bat", ["Maui", "Molokaʻi", "Lānaʻi", "Kahoʻolawe"],
                         {"distribution_note": "Occurs on Maui, Molokaʻi and Lānaʻi and has been observed on Kahoʻolawe (plan lines 3122-3123)."}),
}

HAW_LETTERS = set("aeiouhklmnpwāēīōū ʻ'")


def is_hawaiian(word):
    w = word.lower().replace("ʻ", "")
    return bool(w) and all(ch in HAW_LETTERS for ch in w)


def split_common(raw):
    """Return (common_name, hawaiian_name) from an App 3 'Common Name' cell."""
    if raw is None:
        return None, None
    r = okina(raw.strip())
    if r == "No common name":
        return None, None
    m = re.match(r"^\(=(.+?)\)\s*(.+)$", r)           # (=Native yellow hibiscus) maʻo hau hele
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^(.+?)\s*\(=(.+?)\)$", r)            # Lanai sandalwood (=ʻiliahi)
    if m:
        return m.group(1), m.group(2)
    if is_hawaiian(r):
        return None, r
    return r, None


species = []
used4, used6, used7, used21 = set(), set(), set(), set()
for a in app3:
    g = a["group"]
    sci = a["sci"]
    common, haw = split_common(a["common_raw"])
    rec = dict(group=g, scientific_name=okina(sci), common_name=common, hawaiian_name=haw,
               listing_status=None, imminent_extinction=None, islands=None, other={})
    o = rec["other"]
    o["app3_line"] = a["line"]
    o["app3_common_name_raw"] = okina(a["common_raw"]) if a["common_raw"] else None
    o["recovery_category"] = None
    key = norm(sci)
    if g == "Plants":
        k = key
        if key == "tetramolopium sp. nov 2":
            k = "tetramolopium sp. nov. 2 (mauna kahalawai)"
        p = app4.get(k)
        if p:
            used4.add(k)
            o.update(app4_line=p["line"], app4_name=p["name"], known_occupied_pus=p["occ"],
                     pepp_category=p["pepp"] or None, desired_recovery_populations=p["desired"],
                     recovery_pus_in_mnlcp=p["rec_pus"], known_occupied_pus_in_recovery_footprint=p["occ_in_fp"])
            rec["listing_status"] = {"E": "Endangered", "T": "Threatened", None: "Not listed"}[p["status"]]
            rec["imminent_extinction"] = (p["pepp"] == "PEPP")
            o["recovery_category"] = "Insufficient data (species-specific survey)" if p["rec_pus"] == 0 else "Full recovery"
        else:
            print("NO APP4 MATCH", sci, file=sys.stderr)
    elif g == "Terrestrial snails":
        p = app6.get(key)
        rec["imminent_extinction"] = True   # Ch 4 Table 1 (line 995) and line 1072: all 49 snails
        o["recovery_category"] = "Interim recovery"  # Table 1 line 995: 49 interim
        if p:
            used6.add(key)
            o.update(app6_line=p["line"], current_populations=p.get("current_pop"),
                     interim_recovery_goal_populations=int(p["interim"]) if p.get("interim") else None)
            rec["listing_status"] = "Endangered" if p.get("esa") == "E" else "Not listed"
            o["app6_imminent_flag"] = p.get("imminent") == "X"
        else:
            o["app6_note"] = "Not listed in Appendix 6 (row missing from the plan's App 6 table)."
            print("NO APP6 MATCH", sci, file=sys.stderr)
    elif g == "Terrestrial arthropods":
        p = app7.get(key)
        if p:
            used7.add(key)
            occ = p.get("occ")
            o.update(app7_line=p["line"], known_occupied_pus=int(occ) if occ else None)
            rec["listing_status"] = "Endangered" if p.get("esa") == "E" else "Not listed"
            rec["imminent_extinction"] = p.get("imminent") == "X"
            cats = [c for c in ("interim", "full", "area", "species_survey") if p.get(c)]
            assert len(cats) == 1, (sci, p)
            c = cats[0]
            o["recovery_category"] = {"interim": "Interim recovery", "full": "Full recovery",
                                      "area": "Insufficient data (area survey)",
                                      "species_survey": "Insufficient data (species-specific survey)"}[c]
            if c in ("interim", "full"):
                o["recovery_goal_populations"] = int(p[c])
        else:
            print("NO APP7 MATCH", sci, file=sys.stderr)
    elif g == "Aquatic invertebrates":
        k = key
        if key == "lymnaeidea ssp":
            k = "lymnaeidea spp."
        p = t21.get(k) or t21.get(k + "*")
        if p:
            used21.add(k if k in t21 else k + "*")
            occ = p.get("occ")
            o.update(table21_line=p["line"], known_occupied_pus=int(occ) if occ else None,
                     anchialine_pool=p["name"].endswith("*"))
            rec["listing_status"] = "Endangered" if p.get("esa") == "E" else "Not listed"
            rec["imminent_extinction"] = p.get("imminent") == "X"
            cats = [c for c in ("interim", "full", "area", "species_survey") if p.get(c)]
            assert len(cats) == 1, (sci, p)
            c = cats[0]
            o["recovery_category"] = {"interim": "Interim recovery", "full": "Full recovery",
                                      "area": "Insufficient data (area survey)",
                                      "species_survey": "Insufficient data (species-specific survey)"}[c]
            if c in ("interim", "full"):
                o["table21_recovery_value"] = int(p[c])
        else:
            print("NO T21 MATCH", sci, file=sys.stderr)
    else:  # vertebrates
        v = VERT[sci]
        src, pops, lst, imm, rtype, rval, hname, cname, isl, extra = v
        rec.update(listing_status=lst, imminent_extinction=imm, hawaiian_name=hname, common_name=cname, islands=isl)
        o.update(ch6_source=src, current_populations=pops, recovery_category=rtype)
        if rval:
            o["recovery_goal_populations"] = int(rval)
        o.update(extra)
    species.append(rec)

for nm, d, u in (("app4", app4, used4), ("app6", app6, used6), ("app7", app7, used7), ("t21", t21, used21)):
    left = set(d) - u
    if left:
        print("UNUSED", nm, sorted(left), file=sys.stderr)

json.dump(species, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cnt = collections.Counter(s["group"] for s in species)
print(len(species), dict(cnt))
