# Changelog

## 0.3.0 (2026-11-02)

- Partner feedback from Loyal (2026-11-01): homepage headline now says "native plants and
  animals"; Polynesian fire wording corrected; the Priority Actions page opens its combined-actions
  section with highlights from plan Table 27 (each group's top three strategies), then sequencing.
- Map: in the recovery view, a unit is shown as priority only if it is in the priority footprint
  of a group currently shown. Before, the combined priority footprint was used, so single-group
  recovery maps showed too many priority units (e.g. 101 instead of 28 for Forest birds). The
  imagery basemap now hides the planning-unit grid and the island tint.
- Groups listed in one order sitewide: Plants, Terrestrial snails, Waterbirds, Seabirds, Terrestrial
  arthropods, Aquatic invertebrates, Forest birds, Hawaiian hoary bat.
- Build: table captions no longer print their source comment as visible text.

## 0.2.0 (2026-10-21)

- Footprint maps on the home, footprints, using-the-plan and group pages replaced with the
  standardized release-candidate maps from `all_taxon_footprints` (nested recovery/priority maps,
  species and group richness, reserves, ungulate management, small multiples). The plan figures
  stay in collapsed "as printed in the plan" sections.
- Terrestrial snails shown on the interactive map at planning-unit level (approved by the project lead).
- ACP screenshots added to the Tools page, cropped below the retired title bar.
- Media from past DOFAW and partner presentations and from openly licensed sources: page header
  photos, group thumbnails and a generated Photo credits list on the Resources page. Images with
  unclear rights are held back locally.
- Repository made public; GitHub Pages test site live at https://brasilbrasil.github.io/MNLCP_website/.

## 0.1.0 (2026-10-21): first draft for partner review

- Site plan (`PLAN.md`), content guide and editorial notes.
- Content distilled from the final MNLCP (version 2026-09-29): 15 pages, 8 taxonomic group pages,
  55 Q&As drawn from the demo record, glossary (28 terms), species list (442), PTM strategies
  (27 strategies, 17 species groups, 88 actions), references (49).
- DOFAW branding and a footer rebuilt from the MNLCP demo deck.
- Interactive pieces: megafootprint map (release-candidate footprints of 2026-09-25, Terrestrial
  snails and species names withheld), species explorer, strategy explorer, IMCP diagram, footprint
  walk-through, adaptive management cycle, sitewide search and glossary tooltips.
- Build (`tools/build.py`), map export (`tools/export_footprints.R`) and checker (`tools/check_site.py`).
