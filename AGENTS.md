# AGENTS.md

Guidance for Claude Code, Codex and other agents working in this repository. Read `README.md`
first for what the site is and how it is laid out.

## What this repo is

The public website of the *Maui Nui Landscape Conservation Plan* (MNLCP). **It is a DOFAW site**
(Hawaiʻi Division of Forestry and Wildlife), not a USGS product. Partners are credited by role.
The site documents the final plan (version 2026-09-29) and adds no new findings.

## Golden rules

1. **Never edit the built HTML** (`*.html`, `groups/*.html`, `assets/data/*.js`). Edit
   `content/` or `tools/`, then run `python3 tools/build.py` and `python3 tools/check_site.py`.
2. **The plan is the source of truth for text.** The authoritative plan is
   `../maui_nui_products/project_context_docs/IMPORTANT/MNLCP 9-30-2026 FINAL.txt`; grep it rather
   than reading it whole. Every number in `content/pages/*.md` carries a
   `<!-- src: plan p.X -->` comment. Keep these and add them for new numbers.
3. **Messaging guidelines are mandatory:**
   `../maui_nui_products/project_context_docs/IMPORTANT/MNLCP messaging guidelines.txt`. In short:
   - "prioritization", never "optimization";
   - "recovery footprints" and "priority footprints", not blueprints or solutions;
   - "recover species" and "prevent extinctions", never "save species";
   - "biodiversity reserves";
   - "team" for people, "group" for species;
   - capitalized group names;
   - "Adaptive Conservation Planner", then "ACP" (never "Footprint Manager");
   - PRA-safe expert language ("collaborative review sessions", never "survey" or "questionnaire").
   - `tools/check_site.py` flags retired terms.
4. **Numbers that differ between products:** check
   `../maui_nui_products/project_context_docs/IMPORTANT/MNLCP_cross_product_discrepancies.md` and
   `content/EDITORIAL_NOTES.md` §1.1 before changing a figure. The text uses plan figures; the
   map uses the 2026-09-25 release-candidate footprints.
5. **Location sensitivity.** Planning-unit footprints, including Terrestrial snails, are approved
   for the public site. Do not add species names per planning unit, point locations, or the
   footprint KMZ without DOFAW approval (`content/EDITORIAL_NOTES.md` §1.2).
6. **Hawaiian orthography:** use ʻokina U+02BB and kahakō exactly as the plan does.
7. **Portability:** plain HTML, CSS and vanilla JS. No framework, no CDN dependency, no fetch()
   of local files (data ship as `.js` so the site works from `file://`).

## Common tasks

| Task | How |
|---|---|
| Change page text | Edit `content/pages/<page>.md` and rebuild |
| Change the Q&A, glossary, species, strategies or groups | Edit `content/data/<name>.json` and rebuild (see `tools/extraction/README.md` before rerunning any extraction script) |
| Add an image | Put it in `assets/img/<category>/`, add it to `content/data/asset_catalog.json` with alt text, source and credit, and reference it in Markdown as `[figure: caption \| src: assets/img/... \| alt: ... \| credit: ...]` |
| Update the map after footprint changes | `Rscript tools/export_footprints.R`, then rebuild |
| Add a navigation item | `NAV` and `PAGES` in `tools/build.py` |
| Add an interactive widget | Builder in `tools/pages_special.py` (`WIDGETS`), behaviour in `assets/js/widgets.js`, marker `[[widget:name]]` in the Markdown |
| Public build | `python3 tools/build.py --release` (no draft banner, indexable, no review badges) |
| Visual check | Headless Chrome screenshots: `google-chrome --headless=new --screenshot=out.png --window-size=1440,4000 file://$PWD/index.html` |

## Before finishing a session

- Rebuild, run `tools/check_site.py`, and add a line to `CHANGELOG.md`.
- Record new open questions or discrepancies in `content/EDITORIAL_NOTES.md`.
- Commit with a short imperative message. The remote is
  `git@github.com:brasilbrasil/MNLCP_website.git`; run `git pull --rebase --autostash` before pushing.
