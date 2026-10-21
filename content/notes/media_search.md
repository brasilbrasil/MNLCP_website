# Media search: notes (2026-10-21)

This pass looked for photos, video and graphics that are larger and better than the 114–310 px deck
photos found in the first assets pass (`content/notes/assets.md`).

**Result:** 79 new files.

- 64 photos in `assets/img/photos/`.
- 15 graphics in `assets/img/figures/`: 12 public-domain bird plates and 3 talk maps.
- All 79 are appended to `content/data/asset_catalog.json` with description, alt text, source, size, suggested page and credit.
- Nothing was overwritten, and no HTML, Markdown pages or build scripts were changed.

**Scratch files** are in `_source_extracts/media_search/`:

- `extract/`: raw media pulled from decks, Word files and PDFs, with a `_map.json` per deck mapping media to slides
- `sheets/`: contact sheets used for review
- `scripts/`: `extract_zip_media.py`, `contact_sheets.py` and `process_keepers.py`, which rebuilds every output
- `keepers_catalog.json`: the new catalog entries
- `asset_catalog.backup.json`: the catalog before this pass

## Where I searched

**Drives:**

| Drive | What it holds | How it was searched |
|---|---|---|
| `/hdd` (projects, `zotero_library`, `so_git_repos`) | Main project tree | Searched in full |
| `/hdd2/projects` | comfyUI and phenocam projects | Searched in full |
| `/home/pierc` | Home folders | Searched in full. Documents, Desktop, Pictures and Videos are empty or absent; Downloads has a few images |
| `/media/pierc/Elements2` | 19 TB backup | Decks and videos only. `projects_backup` mirrors `/hdd/projects`; `projects/` holds only lidar and image-generation models |
| `/media/pierc/0044-B059` | USB stick | Empty |

Skipped: `/hdd/rlib`, conda envs, `rosm.cache` and tile caches.

**What I ran:**

- `find` for `.pptx/.ppt/.key/.odp/.mp4/.mov/.m4v/.avi/.heic`: 3,011 hits, nearly all phenocam or AI-video frames.
- `find` for `.jpg/.jpeg/.png/.tif/.webp/.heic/.avif` over 40 KB: 935k hits. Climate rasters, phenocam frames and video-render frames were filtered out, leaving about 3,100 JPEG/HEIC photos to review by folder.
- `find` for `.pdf/.docx/.doc` (5,625), then a keyword filter on the names.

**Containers whose media were extracted and viewed** (all images at or above about 400 px; 1,100+ images on contact sheets):

- **Decks:**
  - ʻĀkohekohe PVA HCC 2026: `Fortini_HCC_2026_akohekohe_PVA_V3.pptx` and `HCC_2026_akohekohe_PVA_beautified.pptx`
  - `Kodama_HCC_2026.pptx`
  - `Paxton and Fortini Malaria prevalence modeling HCC 2023 1.pptx`
  - AMWS: `abridged.pptx`, `short presentation.pptx`, `20220519 Fortini AMWS3_sm_noExtras.pptx`, `culex…pptx`
  - Five Lānaʻi vegetation-mapping decks
  - OCP intro deck: `20261016_OCP_intro_PEPP_KS_draft.pptx`
  - `HIEO Species Selection Update 2026-10-20.pptx`
  - Nakula decks: `Nakula_update_20200904`, `update_20201030/1107/1113`, `Group_meeting_8.22.2018`
  - `GPI NDVI results.pptx`
  - Two ANRPO decks
  - `Lyon HRPP overview.pptx` (114 MB)
  - `Sofaer_CRB_CTAHR_12Aug2026.pptx`
  - `05_climatch_review_2…examples.pptx`
- **Word files:**
  - Two ʻĀkohekohe translocation plans
  - Nakula ecohydrology report and two manuscript drafts
  - Two Lānaʻi manuscripts
  - Two copies of `Maui_nui_conservation_prioritization_2pgr_2025.docx`
  - `06_Newcombia_review`
  - `MR rapid assessment` draft
  - FY26 PICASC proposal
  - Terrestrial arthropod criteria notes
  - `Plant_spatial_prioritization_footprints_V10` (no media)
  - `Battle_of_the_Hawaiian_giants`
- **PDFs** (`pdfimages -all`):
  - Pacific Birds Hawaiʻi plan (`waterbird_REC_footprint_revision/knowledgebase/`)
  - Gallerani et al. 2024
  - Fortini 2013 HCSU TR-44
  - Judge et al. 2021
  - MFBRP Nakula Volunteer Packet 2015
  - PICASC `Results_Sep.2026.pdf`
  - Douglas 2026
  - Lānaʻi land-cover PDF
  - Amidon 2024 MNUI plant models
  - 2019 Oʻahu Army Drosophila/implementation report
- **Loose folders:**
  - `/hdd/projects/OCP/…/20261016_presentation/assets/`: extracts from the HCC 2025 decks; see `ASSETS.md` there
  - `random_errands/completed_assignments/maui_nui_ACP_video/{assets,style_frames,renders}`
  - `sd/input_images/` (`hawaii_landscapes`, `forest_bird_revival/plants/_library`, `plates`)
  - `sd/controlnet/…/landscape_pics`
  - `monitoring/nakula_repo/knowledgebase/field_media`
  - plantcam and HAVO dendrometer photo folders
  - `zotero_library/storage` images
  - `~/Downloads`
- **Maui Nui sibling repos** (`/hdd/projects/maui_nui_scp/*`): every non-output image folder, including docs, `www`, `inst` and vignettes. There are still no photos. They hold only analysis plots, ACP docs screenshots (already used), the ACP login header and the climatch figures.

## HCC 2025 talk decks

These are the talks summarised in `HCC_transcripts/`. **They are not on this machine.** The transcript shortcut points to `C:\Users\lfortini\OneDrive - DOI\maui_nui_project_folder\meeting notes and presentations\HCC 2025\…`. The OCP build script (`20261016_presentation/build/extract_assets.py`) reads them from a Windows `--hcc-dir`. The decks are:

- `2 Fortini TFE approach v2.pptx`
- `3 Wilhite Snails.pptx`
- `6 Melissa Price PTM AO.pptx`
- `7 Landon Implementation.pptx`
- one deck by Fretz

Only the subset copied into the OCP `assets/` folder exists locally, resized to at most 2,200 px. Those copies are what I used for the snail, aeʻo, kīpuka kāhuli, team and talk-map images. **Ask Lucas for the OneDrive folder:** the full decks almost certainly hold more and larger field photos, especially Wilhite (snails), Landon (implementation, fencing) and the Scott, Christina and Jon talks, which are not represented at all.

## What was kept

By file-name prefix: 11 `bird_`, 5 `snail_`, 18 `plant_`, 14 `landscape_`, 15 `work_`, 1 `collage_`, 12 `figures/plate_` and 3 `figures/hcc2025_`.

| Prefix | What it covers and where it came from |
|---|---|
| `bird_` (11) | ʻĀkohekohe ×3 (HCC 2026 PVA decks); kiwikiu ×2, ʻapapane, Hawaiʻi ʻamakihi and nēnē (MFBRP Nakula packet); aeʻo (M. Price, HCC 2025); ʻiʻiwi head banner (AMWS3 deck); Maui ʻalauahio crop (Price slide) |
| `snail_` (5) | Native tree snails on leaves and in canopy (Lilly Thomey, Wilhite HCC 2025 deck) |
| `plant_` (18) | 15 openly licensed (mostly Forest & Kim Starr: Maui, Kahoʻolawe; Eickhoff: Lānaʻi hala pepe); silversword (ANRPO deck); naupaka (DLNR); Nakula seedling (MFBRP) |
| `landscape_` (14) | Nakula and leeward Haleakalā (MFBRP, USGS); forest ridge (L. Thomey); 8 openly licensed: West Maui coast with Lānaʻi, Kahoʻolawe grassland, Haleakalā subalpine, ʻōhiʻa and koa forest, Hanaʻula wet forest, Auwahi māmane |
| `work_` (15) | Helicopter sling load, volunteers carrying, holding and planting seedlings, crew panorama (MFBRP); koa measurement, dendrometer, grass clearing, restoration strips (USGS Nakula); silversword outplanting; tissue culture and seed bank (Lyon HRPP); HCC 2025 team; kīpuka kāhuli aerial (DOFAW) |
| `collage_` (1) | Maui Nui taxa collage (Fortini HCC 2025 slide 16 and 2-pager) |
| `figures/plate_` (12) | Public-domain Frohawk and Keulemans plates: ʻākohekohe, kiwikiu, Maui ʻalauahio, ʻiʻiwi, nēnē, koloa, aeʻo, ʻalae keʻokeʻo, ʻuaʻu, ʻuaʻu kani, kākāwahie (extinct), black mamo (extinct) |
| `figures/hcc2025_` (3) | Ungulate-control priority map (Price), Maui target units on DOFAW lands (Landon), Waikolu addition webmap (Landon) |

**Format notes:**

- The plates are hand-coloured lithographs, so they are saved as JPG in `figures/`, not PNG. PNG would be about 10 MB each.
- One MFBRP photo was stored rotated in the PDF and has been rotated upright.
- The ʻalauahio image is a crop above a baked-in slide label.

## Ranked shortlist

The first file listed is the recommended choice; the rest are alternatives in order. All files are in `assets/img/photos/` unless marked `figures/`.

| Page | Hero / banner | Alternatives |
|---|---|---|
| `index.html` (home) | `landscape_leeward_west_maui_coast_lanai_view.jpg` (two islands in one frame) | `landscape_native_forest_ridge_view.jpg`; existing `hero_misty_ohia_forest_banner_2000x750.jpg` |
| `plan.html` | `landscape_nakula_leeward_haleakala.jpg` | `landscape_leeward_west_maui_coast_lanai_view.jpg`, `collage_maui_nui_taxa.jpg` |
| `approach.html` | `landscape_upland_grassland_above_clouds.jpg` | `landscape_native_forest_ridge_view.jpg` |
| `partners.html` | `work_volunteers_carrying_seedlings_nakula.jpg` | `work_mnlcp_team_hcc_2025.jpg` (needs consent), `work_volunteer_with_koa_seedlings.jpg` |
| `species.html` | `collage_maui_nui_taxa.jpg` | `bird_akohekohe_in_foliage.jpg` |
| `groups.html` (index) | `landscape_native_forest_ridge_view.jpg` | `collage_maui_nui_taxa.jpg` |
| `groups/forest-birds.html` | `bird_akohekohe_in_foliage.jpg` (crop to banner) | `bird_akohekohe_in_flowering_ohia.jpg`, `bird_iiwi_head_closeup.jpg` (strip) |
| `groups/seabirds.html` | No photo. Use `figures/plate_uau_hawaiian_petrel_frohawk.jpg` as a feature image, or the existing small `seabird_shearwater_on_rock.jpg` | `landscape_haleakala_subalpine_cinder.jpg` (ʻuaʻu nesting habitat, no bird) |
| `groups/waterbirds.html` | `bird_aeo_hawaiian_stilt_head.jpg` (empty right side suits text) | `figures/plate_nene_frohawk.jpg` |
| `groups/plants.html` | `plant_cyanea_hamatiflora_east_maui.jpg` (portrait, so crop) | `plant_haleakala_silversword_flowering.jpg`, `plant_clermontia_kakeana_flowers.jpg` |
| `groups/terrestrial-snails.html` | `snail_tree_snail_in_forest_canopy.jpg` | `work_kipuka_kahuli_snail_exclosure_aerial.jpg` (needs DOFAW approval) |
| `groups/terrestrial-arthropods.html` | No new photo. Use existing `arthropod_megalagrion_damselflies.jpg` (small) | `landscape_wet_forest_ridge_hanaula.jpg` (habitat) |
| `groups/aquatic-invertebrates.html` | No new photo. Use `landscape_wet_forest_ridge_hanaula.jpg` (forested gulch) | `landscape_ohia_rocky_gulch.jpg` (stream gulch) |
| `groups/hawaiian-hoary-bat.html` | No bat photo found. Use `landscape_ohia_in_fog.jpg` (night-forest mood) | `landscape_koa_forest_in_mist.jpg` |
| `footprints.html` | `landscape_nakula_panorama.jpg` (banner) | `landscape_upland_grassland_above_clouds.jpg` |
| `actions.html` | `work_outplanting_crew_panorama_nakula.jpg` (banner) | `work_helicopter_sling_load_nakula.jpg`, `work_restoration_spray_strips_nakula.jpg`, `figures/hcc2025_ungulate_control_priority_areas.png` |
| `ecosystems.html` | `landscape_koa_forest_in_mist.jpg` | `landscape_kahoolawe_dry_grassland.jpg`, `landscape_mamane_auwahi.jpg`, `landscape_haleakala_subalpine_cinder.jpg` |
| `using-the-plan.html` | `work_helicopter_sling_load_nakula.jpg` | `figures/hcc2025_maui_target_units_dofaw_lands.png`, `figures/hcc2025_waikolu_addition_webmap.png` |
| `tools.html` | No good photo. Keep the ACP screenshots | `work_dendrometer_on_tree_trunk.jpg` as a small accent |
| `monitoring.html` | `landscape_nakula_ridge_above_clouds.jpg` | `work_tree_growth_measurement_koa.jpg`, `work_dendrometer_on_tree_trunk.jpg` |
| `faq.html` | `plant_native_seedling_in_mist_nakula.jpg` | `figures/plate_kakawahie_extinct_keulemans.jpg` (lost Molokaʻi bird, for an extinction question) |

### Best thumbnail per group

| Group | Thumbnail |
|---|---|
| Forest birds | `bird_kiwikiu_banded_adult.jpg` (or `bird_akohekohe_perched_on_snag.jpg`) |
| Seabirds | `figures/plate_uau_hawaiian_petrel_frohawk.jpg` (or existing `seabird_shearwater_on_rock.jpg`) |
| Waterbirds | `bird_nene_portrait.jpg` |
| Plants | `plant_clermontia_kakeana_flowers.jpg` |
| Terrestrial snails | `snail_tree_snail_on_leaf_underside.jpg` |
| Terrestrial arthropods | existing `arthropod_megalagrion_damselflies.jpg` (still small) |
| Aquatic invertebrates | `landscape_ohia_rocky_gulch.jpg` (habitat; no animal photo found) |
| Hawaiian hoary bat | none found; `landscape_ohia_in_fog.jpg` as a habitat stand-in |

## Rights and credit concerns

These are ordered by risk.

1. **No permission on file for any partner photo.** The MFBRP volunteer packet (Nakula) supplies 15 files, with no photographer named. Ask MFBRP for originals and credits. The photos show identifiable volunteers, so confirm consent too.
2. **Maui ʻalauahio crop** (`bird_maui_alauahio_crop.jpg`): the photographer is unknown. The adjacent panel on the same slide carries a **"Jack Jeffrey Photography"** watermark, so this is probably a professional's photo. Get permission or replace it. The ʻākohekohe panel with the watermark was not taken.
3. **ʻĀkohekohe photos:**
   - `bird_akohekohe_in_foliage.jpg`: slide 2 has two credit lines, "Photo: MFBRP" and a probably stale "novvictan / Wikimedia Commons, CC BY 4.0". Confirm which applies.
   - `bird_akohekohe_in_flowering_ohia.jpg`: credited to novvictan, CC BY 4.0 (verify on Commons).
   - `bird_akohekohe_perched_on_snag.jpg`: "NPS / Haleakalā NP (public domain)", taken from the slide text.
4. **Lyon Arboretum HRPP deck** (tissue culture and seed bank): a third-party deck, so ask HRPP. Most of that deck's other photos were not used: species and islands are unknown, and many are lab shots.
5. **HCC 2025 copies:**
   - Snail photos: credited to Lilly Thomey on the slide.
   - Aeʻo: Melissa Price.
   - Naupaka: DLNR.
   - Kīpuka kāhuli aerial and Landon maps: DOFAW.

   Ask for originals, since these are 2,200 px copies. **The kīpuka kāhuli aerial may reveal a snail-site location**, which is subject to EDITORIAL_NOTES §1.2. Do not pair any snail photo with a place name.
6. **Unknown credit:**
   - `bird_iiwi_head_closeup.jpg` (AMWS3 title slide)
   - Silversword and silversword-outplanting photos (ANRPO deck; probably Krushelnycky or USGS)
   - The HCC 2025 team photo (needs consent from the people shown)
   - The six-tile taxa collage
7. **Openly licensed photos** (23 plant and landscape files): CC BY 2.0, CC BY 3.0 US or CC BY 4.0, with exact attribution text in each catalog entry. They come from Forest & Kim Starr, David Eickhoff and Kevin Faccenda (iNaturalist), via Wikimedia Commons and iNaturalist. The site must show the attribution and a licence link. Metadata are in `/hdd/projects/sd/forest_bird_revival/research/plants/library/*.json`.
8. **Public-domain plates** (12): Frohawk (Wilson & Evans, *Aves Hawaiienses*, 1890–99) and Keulemans (Rothschild, 1893–1900), via BHL and Commons. They are public domain; credit them as a courtesy. They are illustrations, so label them that way and not as current photos.
9. **No EXIF Artist or Copyright fields** were present in any kept file. A few carry only the camera model and date, which are recorded in the catalog.

## Promising media not used

| Media | Path | Why not used |
|---|---|---|
| **ACP infomercial video** (1920×1080, 3 min 11 s) | `/hdd/projects/random_errands/completed_assignments/maui_nui_ACP_video/renders/acp_infomercial.mp4` and `acp_infomercial_share.mp4` | Parody tone, and the style frames are AI-generated; check the messaging guidelines before using it on `tools.html` |
| **Nakula field videos** (5 clips, 22–61 s, 1080p, 2019-05-02 stemflow/throughfall work) | `/hdd/projects/monitoring/nakula_repo/knowledgebase/field_media/stemflow_throughfall_20190502/*.mp4` | Not reviewed frame by frame; possible b-roll for `monitoring.html` |
| ACP full-map stills | `maui_nui_ACP_video/assets/acp_alltaxa.png`, `acp_edits.png`; OCP `demo_s12_image54.png` | The header shows the retired name "Maui Nui Conservation Footprint Manager"; use the existing ACP docs screenshots instead |
| **Pacific Birds Hawaiʻi plan** | `waterbird_REC_footprint_revision/knowledgebase/PB-Hawaii-Plan-FINAL-2.27.24-reduced.pdf`; extracts in `extract/pdf_PB_Hawaii_Plan…/` | Good waterbird photos (nēnē with koloa, nēnē portrait, aeʻo chick, wetlands) and clean island basemaps, but no credits in the PDF text and many shots are from Kauaʻi or Oʻahu; ask Pacific Birds if wanted |
| ʻĀkohekohe range and land-manager maps | `AKOH_translocation_plan_NearlyFullDraft.docx` media | Draft translocation plan, and not an MNLCP product |
| Snail exclosure network map | OCP `derived_wilhite_s37_snail_network.png` | Shows snail exclosure sites, which are location-sensitive |
| Plant and climate photos © J. K. Obata, © G. D. Carr, © M. LeGrande | PICASC `Results_Sep.2026.pdf`, 2020 IT meeting deck | Copyrighted |
| Oʻahu Army report and ANRPO, plantcam, HAVO dendrometer, CRB and OCP field photos | Various | Oʻahu or Hawaiʻi Island, not Maui Nui. They include a Drosophila photo, Oʻahu *Achatinella* snails and fencing crews |
| Personal and AI images | `~/Downloads`, `sd/input_images/historical_images`, `fotos_cathy`, `controlnet/landscape_pics` (Brazil trips), `ai_flux/ComfyUI` and `sd/forest_bird_revival` videos (AI-generated extinct birds) | Personal or not real photos |

## Gaps that remain

No usable photo was found for:

- ʻōpeʻapeʻa (Hawaiian hoary bat)
- seabirds (ʻuaʻu, ʻaʻo)
- ʻalae keʻokeʻo and koloa (photos)
- aquatic invertebrates
- Native arthropods other than the existing small damselfly image
- Euglandina, rats and fire
- ungulates other than the existing small goat
- fence-building crews or workshops on Maui Nui
- Molokaʻi landscapes (only Kahoʻolawe, Lānaʻi and Maui are covered)

The HCC 2025 OneDrive folder and DOFAW and partner photo libraries are the next places to ask.
