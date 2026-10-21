# MNLCP Website — Build Plan

**Owner:** Hawaiʻi Division of Forestry and Wildlife (DOFAW). This is a DOFAW site: DOFAW/DLNR
branding, DOFAW-style footer (green fern band, DLNR + DOFAW seals, "E mālama kākou i ka ʻāina ·
dlnr.hawaii.gov/dofaw") taken from the MNLCP demo deck. Partners (USGS, UH Mānoa, UH Hilo, USFWS,
Bishop Museum, …) are credited as partners, not as owners.

**Audience:** conservation partners (land managers, agencies, funders) and the public.

**Source of truth:** *Maui Nui Landscape Conservation Plan*, DOFAW, version 2026-09-29
(`maui_nui_scp/maui_nui_products/project_context_docs/IMPORTANT/MNLCP 9-30-2026 FINAL.pdf`).
The site documents the plan; it does not add new findings.

## 1. Design principles

1. **Static and portable.** Plain HTML + CSS + vanilla JS. No build step, no server, no framework.
   Works from any web host (GitHub Pages, S3, state CMS file area, a USB stick) and when opened
   directly from disk (`file://`). Data are shipped as `.js` files (`window.MNLCP_DATA = …`) rather
   than fetched JSON, so nothing breaks offline or without a server.
2. **Vendored dependencies.** Leaflet (map) is copied into `assets/vendor/`; no CDN needed except
   basemap tiles. Charts are hand-built SVG.
3. **Content kept separate from layout.** Every page's text is drafted in Markdown in
   `content/pages/` (the editorial source that DOFAW reviews), and structured data (species,
   taxa, strategies, FAQ, glossary) live in `content/data/` and are compiled to `assets/data/*.js`.
4. **Plain language first, depth on demand.** Each page opens with a short plain-language
   summary, then expandable detail for practitioners.
5. **Messaging rules.** Follow the MNLCP messaging guidelines (prioritization not optimization;
   conservation footprints; recover species / prevent extinctions; biodiversity reserves; team vs
   group; PRA-safe expert-engagement language; ACP naming).
6. **Accessible and responsive.** Semantic HTML, keyboard navigation, alt text, AA contrast,
   readable at phone width, prefers-reduced-motion respected.

## 2. Site map

| Page | File | Plan source | Interactive elements |
|---|---|---|---|
| Home | `index.html` | Executive Summary | Animated key numbers, three goals, "where/what/when" explainer, explore cards |
| About the Plan | `plan.html` | Ch 1 (purpose & need, applications, path forward), Ch 2 a–c | Challenge infographic, timeline |
| The Approach (IMCP) | `approach.html` | Ch 2 d–e, Ch 3, App 1 | Clickable IMCP diagram (where/what/when), TFE-SCP step-through |
| At-Risk Species | `species.html` | Ch 4, App 3, 4, 6, 7 | Searchable/filterable species explorer (442 species) |
| Taxonomic Groups | `groups.html` + `groups/<group>.html` (8) | Ch 6 a–h | Group cards → detail pages with stats, threats, strategy, footprint, actions |
| Conservation Footprints (map) | `footprints.html` | Ch 6 i, App 1 | Leaflet map: recovery & priority footprints by group, richness view |
| Priority Actions | `actions.html` | Ch 5 d, Ch 6 j, App 2 | Strategy explorer (benefit/cost/feasibility), emergency actions |
| Ecosystems | `ecosystems.html` | Ch 7, App 8 | Ecosystem priorities ladder, hotspot figures |
| Using the Plan | `using-the-plan.html` | Ch 5 (a–f) | Step-by-step "how a manager uses the MNLCP" |
| Adaptive Conservation Planner & Tools | `tools.html` | App 5 | Screenshot carousel, links |
| Monitoring & Adaptive Management | `monitoring.html` | Ch 8, App 9 | Adaptive management cycle diagram |
| Partners & Teams | `partners.html` | Ch 3, acknowledgments | Team structure diagram, partner logos |
| Questions & Answers | `faq.html` | Whole plan + demo/meeting record | Searchable, categorized accordion |
| Glossary | `glossary.html` | Terms and Definitions | Searchable, A–Z, term tooltips sitewide |
| Resources | `resources.html` | Literature Cited, downloads | Plan PDF, KMZ, references |

## 3. Directory layout

```
MNLCP_website/
  index.html, plan.html, …            pages
  groups/<group>.html                 taxon pages
  assets/css/site.css                 one stylesheet (tokens, light/dark)
  assets/js/site.js                   header/footer injection, nav, search, glossary tooltips, counters
  assets/js/<feature>.js              species explorer, map, actions explorer, faq
  assets/data/*.js                    compiled data (window.MNLCP_DATA.*)
  assets/img/                         photos, figures, logos (from deck, plan PDF, repos)
  assets/vendor/leaflet/              vendored Leaflet
  assets/docs/                        plan PDF, KMZ downloads
  content/pages/*.md                  editorial source text per page (review here)
  content/data/*.json|csv             structured content
  content/EDITORIAL_NOTES.md          open questions, number discrepancies, items for DOFAW review
  _source_extracts/                   working extracts (not deployed)
  PLAN.md, README.md
```

## 4. Workflow

1. **Distill** the plan into page content (parallel agents by plan section) → `content/pages/`.
2. **Q&A** from the demo record (ACP demos, FWS show-and-tell, MNLCP update & demo, HCC talks,
   participant feedback) cross-checked against the plan → `content/pages/faq.md`.
3. **Assets**: extract logos/photos from the demo deck, figures from the plan PDF, footprint maps
   and synthesis figures from `all_taxon_footprints`, ACP screenshots; export simplified GeoJSON
   of recovery and priority footprints (R/sf).
4. **Build** the static pages from the content; wire interactive components.
5. **Review**: link check, number consistency against the plan, messaging-guideline pass,
   mobile/dark-mode check.
6. **Hand-off**: README (how to edit, how to host), EDITORIAL_NOTES (decisions for DOFAW).

## 5. Numbers policy

The site mirrors the plan, so text uses the plan's figures. The interactive map uses the
release-candidate footprints of 2026-09-25 (the set loaded in the ACP). Where the two differ
(e.g. combined priority footprint: plan 216 PUs vs release candidate 237 PUs), the difference is
logged in `content/EDITORIAL_NOTES.md` for DOFAW to resolve before launch.

## 6. Out of scope for the draft

Hawaiian-language review of diacritics and cultural framing, photo permissions/credits beyond what
the deck and plan already carry, ADA audit by DOFAW web staff, hosting decision.
