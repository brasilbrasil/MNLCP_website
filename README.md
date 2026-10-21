# Maui Nui Landscape Conservation Plan website (draft)

A static website documenting the *Maui Nui Landscape Conservation Plan* (MNLCP) for partners and
the public. It is a Hawaiʻi Division of Forestry and Wildlife (DOFAW) site. The content is
distilled from the final plan (version 2026-09-29).

- **Open it:** double-click `index.html`. Everything works from disk except basemap tiles, which
  need an internet connection.
- **Before release:** read `content/EDITORIAL_NOTES.md`, which lists the decisions DOFAW needs to make.
- **Build plan:** `PLAN.md`.

## What's here

| Path | What it is |
|---|---|
| `*.html`, `groups/*.html` | The built pages, which are what you host |
| `assets/` | CSS, JS, fonts, images, data (`assets/data/*.js`), vendored Leaflet, and the plan PDF |
| `content/pages/*.md` | **Page text.** Edit here, then rebuild |
| `content/data/*.json` | Structured content: species list, Q&A, glossary, strategies, groups, references, ecosystems, monitoring, IMCP diagram, asset catalog |
| `content/notes/` | Drafting notes per section (discrepancies, gaps, questions) |
| `content/CONTENT_GUIDE.md` | Format and messaging rules for content |
| `tools/build.py` | Builds the HTML from `content/` (plus `pages_special.py` and `home_page.py`) |
| `tools/export_footprints.R` | Exports the megafootprint GeoJSON for the map from `all_taxon_footprints` |
| `tools/check_site.py` | Checks for broken links and anchors, and retired terms in the built pages |
| `tools/extraction/` | One-time scripts that produced the data and images (provenance; see its README) |
| `scripts/publish_test_site.sh` | Makes the GitHub repo public and turns on GitHub Pages |
| `PLAN.md` | Site plan: design principles, site map, numbers policy |
| `AGENTS.md`, `CLAUDE.md` | Instructions for AI coding agents working in this repo |
| `CHANGELOG.md` | What changed, by version |
| `_source_extracts/` | Working files from drafting, local only (gitignored) |

## Pages

Home · About the Plan · The Approach (interactive IMCP diagram, footprint walk-through) · Partners
& Teams · At-Risk Species (searchable explorer of all 442 species, CSV download) · Taxonomic Groups
plus eight group pages · Conservation Footprints (interactive megafootprint map) · Priority
Actions (strategy explorer: persistence by species group, costs, actions) · Native Ecosystems ·
Using the Plan · Adaptive Conservation Planner & Tools · Monitoring & Adaptive Management
(interactive cycle) · Q&A (55 questions, searchable) · Glossary (also shown as hover tooltips
sitewide) · Resources. The site search opens with Ctrl+K or `/`.

## Editing

1. Edit the Markdown in `content/pages/` or the JSON in `content/data/`.
   - Every number carries an HTML comment `<!-- src: plan p.X -->`. Keep these; they power the
     "Show plan sources" review aid.
   - Content can use `## Lead`, `## Key numbers` (`- **442** | label`), `> **Callout:** …`,
     `:::details Title … :::`, `[figure: description | suggested source: plan PDF p.N Figure N]`
     (resolved to the extracted image automatically) and `[[widget:name]]`.
2. Rebuild: `python3 tools/build.py` (needs Python 3.8+ and `pip install markdown`).
3. Check: `python3 tools/check_site.py`.
4. When the footprints change: `Rscript tools/export_footprints.R` (needs R with `sf` and
   `data.table`), then rebuild.

Draft builds show a "DRAFT" banner, a `noindex` tag and review badges. For the public version run
`python3 tools/build.py --release`.

## Hosting

No server-side code and no build step on the host. Any static web host works.

**Repository:** `github.com/brasilbrasil/MNLCP_website`, created **private**.

**Test site with GitHub Pages:**

```bash
bash scripts/publish_test_site.sh
```

The script asks for confirmation, makes the repository public, enables Pages from `main` at the
repository root, and prints the URL (`https://brasilbrasil.github.io/MNLCP_website/`). The site
is live a minute or two later. To take it down again, run
`bash scripts/publish_test_site.sh --private`.

On a free GitHub account Pages needs a public repository, so the draft text and the plan PDF become
visible to anyone with the link. The draft build carries `noindex`, so search engines skip it.
GitHub Enterprise can keep Pages private to organization members.

**Other options:**

- Netlify Drop: drag the folder onto app.netlify.com/drop.
- Any State or DLNR web server: copy everything except `_source_extracts/`; `content/` and
  `tools/` are optional.
- Locally: run `python3 -m http.server` inside the folder and open http://localhost:8000.

## Data and sensitivity

The map shows the release-candidate megafootprint of 2026-09-25 with taxon-group counts and
planning criteria per planning unit. It deliberately leaves out species names and Terrestrial
snail units; see `content/EDITORIAL_NOTES.md` §1.2 before changing that.

## Credits

Content: *Maui Nui Landscape Conservation Plan*, Hawaiʻi Division of Forestry and Wildlife, 2026.
Map library: Leaflet 1.9.4 (BSD-2-Clause). Fonts: Noto Sans and Noto Serif Display (SIL Open Font
License). Basemaps: Esri, CARTO, OpenStreetMap contributors.
