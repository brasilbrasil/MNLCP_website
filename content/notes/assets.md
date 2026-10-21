# Assets task: notes

Task id `assets`. Output is in `assets/img/{brand,logos,photos,figures,maps,screenshots}/`, and the full catalog (description, alt text, source, size, suggested use, credit) is in `content/data/asset_catalog.json`. All working files and scripts are in `_source_extracts/assets_work/`:

- `scripts/map_media2.py`: maps deck media to slides; output in `media_map.json`
- `scripts/extract_plan_figs.py`: crops plan figures; captions in `plan/figs_meta.json`
- `scripts/brand.py`: builds the brand files
- `scripts/build_catalog.py`: builds the catalog; rerun it after any change

Total size is about 24 MB for 145 files.

## What was produced

| Folder | Files | Notes |
|---|---|---|
| brand/ | 19 | DLNR and DOFAW seals, the deck's fern artwork (full and cropped as used), footer bands rebuilt from it, a tileable strip, the title-slide band, a hero composite, and a rendered reference of the deck footer |
| logos/ | 19 | 17 partner logos from the slide 1/16 strip, plus untrimmed DLNR and DOFAW seals |
| photos/ | 20 | Hero forest photo (JPG, WebP, 1000 px and banner crops) and 16 small species and threat photos from slides 3, 5 and 6 |
| figures/ | 52 | 38 plan figures, 5 USFWS recovery-plan covers (slide 4) and 9 synthesis charts |
| maps/ | 20 | Release-candidate (2026-09-25) recovery, priority and nested footprint maps, all-taxa and per group |
| screenshots/ | 15 | Cyanea mceldowneyi steps 01-05, 2 older deck app screenshots and 8 ACP documentation screenshots |

## Deck structure (for building the footer and header)

- **Content slides (2-15):** the background is solid `#24602B` and there is no texture image. The footer is a group made of a solid `#6CB146` rectangle (bottom 9.4% of the slide), fern corners (image26 left, image27 right, both cropped), small DLNR and DOFAW seals (image24, image25), "Forestry & Wildlife" at left, and "E mālama kākou i ka ʻāina / dlnr.hawaii.gov/dofaw" at right. All footer text is bold Calibri in `#24602B`. Body text is `#F8EBD1` (cream).
- **Title and closing slides (1, 16):** the full-bleed forest photo (image1) has a `#6CB146` rectangle at 70% opacity over its bottom 30%. Large fern clusters (image4 left, image2 right, image3 frond) sit at the band edges, with the seals and partner logos on top. In the deck the ferns are subtle, and the rebuild matches that. The title box is `#F8EBD1` at 80% opacity.
- The deck footer has no separate band image. The band is a vector rectangle plus two transparent PNG corners, which is why I rebuilt the footer files (`footer_band_*`) from those parts.
- **Tileable variant:** `footer_fern_tile_1294x300.png` is the right fern cluster plus its mirror image, so it tiles without seams in `repeat-x`. Because it is a mirrored derivative, the ʻiʻiwi-like silhouettes appear as a facing pair.
- **Suggested CSS tokens:** `--dofaw-green-dark:#24602B; --dofaw-green:#6CB146; --dofaw-cream:#F8EBD1`.
- **Orthography:** the deck footer types "ʻāina" with a left quote mark (‘), not the ʻokina. Use U+02BB on the site.

## Best hero candidates

1. `photos/hero_misty_ohia_forest.jpg` (2000×1117, WebP alongside; 3025 px original): misty montane wet forest with ʻōhiʻa canopy and hāpuʻu tree-fern understory. It is the only high-resolution photo in any source. `brand/hero_title_composite_2400.jpg` is the same photo with the deck's green fern band, ready for overlay text.
2. `maps/nested_all_taxa.png`: the clearest single image of the plan's idea (priority tier nested in the recovery footprint).
3. `figures/plan_fig_02_combined_recovery_footprint.jpg` (also Exec Summary Fig. 1), if the hero should show the plan's own map.

The species photos are all small (114-310 px wide), so use them only as thumbnails or cards.

## Plan figures

- Captions were matched from `pdftotext -layout`. The plan has three numbering series:
  - Executive Summary Figs 1-2
  - main text Figs 1-29
  - Appendix 2 (PTM report) Figs 1-6 and appendix Figs 1-3
- File names: `plan_fig_NN_*` for the main text, `plan_fig_app2_N_*` and `plan_fig_app2_sN_*` for Appendix 2.
- **Executive Summary figures:** ES Fig. 1 is the same embedded image as Fig. 2 (PDF object 570), and ES Fig. 2 is the same chart as Fig. 3. They were not duplicated, and the catalog notes the equivalence.
- **How the figures were made:** each was rendered from the PDF at 220 dpi, clipped to the figure (images, panel-letter overlays and vector charts), then scaled to ≤1600 px. Maps with basemaps were saved as JPG q85 and charts as PNG.
- **Figures that span two pages were merged into one image:**
  - Fig. 8: PDF pp. 53-54, stacked
  - Fig. 9: PDF pp. 60-61, 2×2 grid
  - Fig. 15: PDF pp. 81-82, stacked
- **The plan contains no species photos.** All 84 embedded rasters are figures, and the small ones are panel-letter labels and arrows. No `plan_p<page>_` photos could be produced.
- **Text problems found in the figures** (leave them as they are; they are logged here for DOFAW):
  - Fig. 1 says "OptimTCE", which is probably a typo for optimTFE.
  - Figs 23 and 24 use the legend label "Optimization footprint", which conflicts with the messaging guidelines.
  - The Fig. 9 caption says 195 plants, while the plan elsewhere says 196.

## Release-candidate maps vs the plan

The `maps/` files and `synthesis_*` charts come from the 2026-09-25 release candidate, the set loaded in the ACP. Their totals differ from some plan figures: priority is 237 PUs here, against 216 in the plan; recovery is 492 PUs in both. The synthesis charts are analysis that came after the plan and are not in the plan PDF, so use them only in "Details" sections and only if DOFAW agrees. Log the numbers in `content/EDITORIAL_NOTES.md` as PLAN.md §5 requires.

## Other image sources searched (step 5)

`find /hdd/projects/maui_nui_scp -iname '*.jpg' -o -iname '*.jpeg'` (also with `-L`) finds no JPEGs at all outside tile caches. I also checked the three other decks in the tree:

- `05_climatch_review_2_2024-05-23_examples.pptx`
- `velocity.pptx`
- `seabirds optimization process.pptx`

They hold only analysis maps (or no media). `optimTFE/dev/vignettes/vignette_images` holds analysis plots. **No field or species photos exist in the project tree**, so DOFAW and partners will need to supply them.

## Rights and credits to resolve (flagged)

1. **Unknown photographers:** all deck photos except two have no credit: the hero forest, rat, goat, feral cat camera trap, rosy wolfsnail, three tree-snail photos, three plant photos, ʻiʻiwi, ʻākohekohe, shearwater and damselflies. Some are probably DOFAW, USFWS or partner photos; get originals and credits before launch.
2. **Visible credits:**
   - `threat_jacksons_chameleon.jpg` carries a "©Warren Photographic" watermark. This looks like a commercial stock image, so get permission or replace it.
   - `plant_cyanea_mceldowneyi.jpg` is "© C. H. Lamoureux" (caption baked in).
3. **Third-party figures in the plan:**
   - Fig. 29 is "From Sutter et al. 2015".
   - App 2 Fig. 2 is adapted from Carwardine et al. 2019.
   - Fig. 17 has Esri/HERE/Garmin basemap credits and is styled "M6. Map 1", so it is likely from a CWRM or partner report.
   - Fig. 5 is in a different map style and gives no source.
   - App 2 Fig. 1 uses satellite imagery from an unnamed provider.
   - The ACP basemap tiles in the Cyanea steps and the ACP figures show no attribution.
4. **Logos:** these are low-resolution copies taken from the deck. Each partner should supply an official file and approve its use.
   - `unidentified_spiral_logo_possibly_sepp.png` (blue spiral on orange) is not identified. It may be the Snail Extinction Prevention Program, which is credited on slide 16. Confirm it.
   - The University of Hawaiʻi seal (99 px) and the PI-CASC mark (66 px) are too small for anything but tiny icons.
   - The DLNR and DOFAW seals are official state insignia; confirm DOFAW's usage rules.
5. **Personal emails redacted:** the older deck screenshots showed scott.fretz@…, and every ACP documentation screenshot showed devin.leopold@gmail.com. Both were blacked out in the copies.
6. **Messaging in screenshots:** every app screenshot's title bar still reads "Maui Nui Conservation Footprint Manager", but the guidelines say to use "Adaptive Conservation Planner" and never "Footprint Manager". The screenshots were not edited. I recommend new screenshots of the current ACP (ideally with a demo account). Until then, use the `acp_*` set with a caption naming the ACP, and use the `deck_footprint_manager_legacy_*` files only for history, if at all.
7. **Sensitive locations:** DOFAW should decide whether these may go on a public site:
   - `acp_species_layers.png` shows known-population points for the Haleakalā silversword.
   - `acp_unit_targets.png` lists the rare species targeted in one West Maui planning unit.
   - The Cyanea steps show where one rare plant's habitat is.
8. **Species names in descriptions:** where the deck gives no name, species were identified by eye and the descriptions hedge ("probably", "not labelled"): the shearwater, the Megalagrion damselflies, the native tree snails and the three plant photos. Have a biologist confirm them before captions go public.
