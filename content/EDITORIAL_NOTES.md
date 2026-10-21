# MNLCP website: editorial notes for DOFAW review

Draft of 2026-10-21. This file collects the decisions DOFAW needs to make before the site is
public, the choices the draft already made, and the errors found in the plan while distilling
it. Detail, with plan line numbers, is in the per-section notes in `content/notes/`
(`core`, `species`, `groups1`, `groups2`, `actions`, `ecomon`, `tools`, `faq`, `assets`).

In the draft build, the **Show plan sources** button in the footer reveals the plan page or line
behind every number, and Q&A answers that need DOFAW input carry a yellow badge.

---

## 1. Decisions needed before public release

### 1.1 Which numbers the site quotes

The site text uses the plan's figures. The interactive map uses the 2026-09-25 release-candidate
footprints (the set loaded in the ACP), so for some figures the text and the map disagree. IDs
refer to `maui_nui_products/project_context_docs/IMPORTANT/MNLCP_cross_product_discrepancies.md`.

| Figure | Plan (site text) | Release candidate (map) | Tracker |
|---|---|---|---|
| Combined priority footprint | 216 PUs, 457 km², 267 species | 237 PUs, 505.6 km², 305 taxa | XP-04 |
| Plant priority footprint | 155 PUs (body, glossary); 181 in App 1 | 181 PUs, 182 taxa | XP-05 |
| PEPP-only plant view | 98 PUs (Table 4); 110 in App 1 | 125 PUs | XP-06 |
| Species in combined recovery footprint | 299 (Exec Summary); 250 (Ch 6i) | 330 taxa | XP-01 |
| Listed plants | 175 (Table 1) | 174 in App 4 | XP-07 |
| Aquatic invertebrate priority layer | shown in Figure 15 | none | XP-10 |
| Bird footprint sizes (FB, SB, WB) | not stated | 160/28, 226/18, 57/3 PUs | — |
| PTM species | 374 (Ch 3d, App 2) vs 442 everywhere else | — | — |
| PTM annual cost | $26M (App 2 abstract) vs ~$55M and ~$53M (App 2 body) | — | — |

**Options:** (a) keep plan figures in the text and label the map "release-candidate footprints,
September 25, 2026", as the draft does now; (b) update the text to the release-candidate values and
note that they supersede the plan; (c) issue a plan erratum and align both.

### 1.2 What can be public (location sensitivity)

The plan says the ACP "is not a public web map". The draft therefore holds back these items until
DOFAW decides:

- **Map, Terrestrial snails.** Approved by the project lead on 2026-10-21: snail footprints are
  shown at planning-unit level on the map and on the snail page. (They were withheld in the first
  draft; `withheld_groups` in `tools/export_footprints.R` controls this.)
- **Map, species names.** The map shows how many species of each group each planning unit
  supports, never which species. The ACP holds the species-level detail.
- **KMZ download.** Still not posted. The existing KMZ (`all_taxon_footprints/data/Maui_Nui_Conservation_Footprints.kmz`)
  has per-unit detail beyond the planning-unit footprints, so it needs its own review. The
  Resources page says it is pending approval.
- **Cyanea mceldowneyi walk-through** (Approach and Footprints pages). This is the deck's
  step-by-step example: one listed plant's habitat suitability and ten recovery units on windward
  East Maui. DOFAW presented it in its own demos, but please confirm it can be public.
- **ACP screenshots.** Approved by the project lead on 2026-10-21. All eight are used on the Tools
  page, cropped below the title bar that carried the retired "Footprint Manager" name and a user
  email. **Still to confirm:** `acp_species_layers` shows Haleakalā silversword known-location
  points (point locations, not planning units), and `acp_manage_aux_layers` shows internal layer
  names ("AO benefits", "Flagged Plant PUs"). Recapturing from the current ACP would also show the
  new name.
- **Footprint maps.** The site's footprint maps now come from `all_taxon_footprints`
  (standardized maps, release candidate of 2026-09-25), replacing the plan's figures. Each page keeps
  the plan figure in a collapsed "Map as printed in the plan" section. Their unit counts follow the
  release candidate, so they can differ from the plan text (see 1.1).
- **Plan figures.** Figure 11 (snail exclosure network) and other plan maps are shown because
  they are in the published plan. If the plan PDF itself is not public, revisit these.

### 1.3 Facts the plan does not supply

- **Plan PDF.** Can it be downloaded publicly? It is included at `assets/docs/MNLCP_2026-09-29.pdf`.
  Its PDF metadata has no title and lists Loyal Mehrhoff as author; fix before posting.
- **Contact.** The plan names no contact, so Resources and the Q&A have placeholders.
- **ACP access.** Who gets an account, how to request one, who approves access to sensitive
  layers. Which address to publish: the plan gives the shinyapps URL (legacy, to become a redirect);
  the AWS production address is `https://acp.fullstackeco.com`, on a developer domain rather than a
  State domain.
- **Regulatory status.** The plan never says that footprints are not regulatory designations and
  create no new rules. Strongly recommended, and needed for several Q&A answers (private land,
  critical habitat).
- **Recommended citation.** The plan gives none; the draft builds one from the title page.
- **Community and Native Hawaiian engagement.** Not described in the plan; one Q&A awaits text.

### 1.4 Q&A answers that need DOFAW input (12 of 55)

`add-species`, `cost`, `acp-access`, `update-cadence`, `sensitive-data`, `regulatory`, `my-land`,
`private-landowners`, `critical-habitat`, `share-info`, `community`, `get-plan`.
Each draft answer stays within what the plan supports. What DOFAW must confirm for each is in
`content/notes/faq.md`.

### 1.5 Images and rights

Photos now come from DOFAW and partner presentations and from openly licensed sources already on
disk (media search of 2026-10-21; details in `content/notes/media_search.md`). Every page header
shows a credit, and **Resources → Photo credits** lists every photo and plate used, generated from
`content/data/asset_catalog.json` at build time.

- **Forest and Kim Starr photos** (CC BY 3.0): attribution and a licence link are shown, as the
  licence requires.
- **Frohawk and Keulemans plates** (*Aves Hawaiienses*, 1890s): public domain. A plate stands in
  for the seabird photo nobody has supplied.
- **Maui Forest Bird Recovery Project photos** (2015 Nakula volunteer packet: kiwikiu, nēnē,
  outplanting crews, helicopter sling load, landscapes): no photographer is named and volunteers
  are identifiable. **Confirm with MFBRP**, and get originals and credits.
- **Lilly Thomey** snail and forest photos, and **Melissa Price**'s aeʻo, are credited from the source slides.
  Confirm permission with each.
- **ʻĀkohekohe header photo:** the slide carries two conflicting credits ("MFBRP" and "novvictan /
  Wikimedia Commons, CC BY 4.0"). Verify.
- **Credit still unknown:** the misty ʻōhiʻa forest on the homepage (from the DOFAW deck), the
  species-page collage, the USGS Nakula photos and the older small deck photos.
- **Held back** (kept locally in `_source_extracts/withheld_images/`): an ʻalauahio photo that is
  probably Jack Jeffrey's, the kīpuka kāhuli aerial (could reveal the site), the HCC 2025 team
  photo (consent), two Lyon Arboretum photos (permission), and the stock chameleon photo.
- **Still missing:** photos of the Hawaiian hoary bat, seabirds, ʻalae keʻokeʻo and koloa, aquatic
  invertebrates and arthropods; threats such as Euglandina, rats and fire; fencing crews,
  workshops, and Molokaʻi landscapes. The HCC 2025 talk decks (OneDrive) and the DOFAW and partner
  photo libraries are the next sources to try.
- **Partner logos** are low-resolution copies from the deck. Each partner should supply an official
  file and approve its use.
- **Third-party figures:** plan Figure 29 (Sutter et al. 2015) and Appendix 2 Figure 2 (after
  Carwardine et al. 2019).

### 1.6 Wording to confirm

- Homepage headline: three options are in a comment at the top of `content/pages/home.md`.
  The draft uses "A roadmap to prevent extinctions and recover Maui Nui's native species".
- Hawaiian-language review of diacritics and names. Plant Hawaiian names follow the plan, which
  prints them without kahakō. "kāhuli" is used as the Hawaiian name for Terrestrial snails. The
  deck motto uses ‘ for the ʻokina in "ʻāina"; the site uses ʻ.
- PRA framing in the PTM methods section. The plan's Appendix 2 uses "Data Collection",
  "elicited" and "optimal"; the site does not, but it does describe experts giving best, lowest and
  highest estimates.
- S15 includes gene-drive mosquitoes, while Appendix 2's discussion says gene drives were left out
  of the analysis. The public wording needs a decision.
- Private land: the demos said watershed-partnership private lands were left out of recovery
  targeting, but the plan says it focuses on lands under conservation agreements. The site follows
  the plan.

---

## 2. Choices the draft already made

- **DOFAW site.** DOFAW branding throughout. The footer is rebuilt from the MNLCP deck: green
  fern band, DLNR and DOFAW seals, "Forestry & Wildlife", "E mālama kākou i ka ʻāina",
  dlnr.hawaii.gov/dofaw. Partners are credited by role and in a logo strip.
- **Messaging guidelines applied.** "Prioritization", not "optimization"; recovery and priority
  footprints; "recover species" and "prevent extinctions"; group names capitalized; "team" for
  people; Adaptive Conservation Planner, never "Footprint Manager"; PRA-safe expert language.
  `tools/check_site.py` flags retired terms in the built pages.
- **Group colors** are fixed sitewide in the plan's chapter order and checked for color-vision
  separation. Every use is labelled, so color never carries meaning alone.
- **442 species** is the headline count. 374 appears only where the PTM analysis is described.
- **Reconciled 299 vs 250** on the Footprints page as "250 with recovery habitat plus exclosure
  sites for the 49 snails = 299". Please confirm this reading.
- **Plan tables reproduced as printed** where they conflict with Table 26 or Appendix 2 (snail,
  aquatic and bat persistence values). The Table 26 values are shown alongside in Details blocks.
- **Search engines are kept out** of the draft build (`noindex`); the release build
  (`python3 tools/build.py --release`) drops the banner, the noindex tag and the review badges.

---

## 3. Errors and inconsistencies found in the plan

For the plan's custodians. Each is logged with line numbers in the section notes. Items marked
(new) are not yet in the discrepancy tracker.

- Appendix 6 lists 48 snails under a 49-species heading (*Amastra goniops* is missing) and totals
  47 imminent (XP-14).
- Table 25 leaves S10 out of S25, though Table 3 and Appendix 2 include it; the components listed
  for S26 omit S8, though its name includes it. (new)
- Persistence tables per group disagree with Table 26: snails, aquatic invertebrates
  (*Megalagrion*) and the bat (Table 24, new; suggest adding it to XP-15).
- Appendix 2 says 10 groups reach 50–60%, but its table supports 9; it gives 20 waterbird fences
  in Table 2 and 14 in Figure 6b. (new)
- Montane Dry: Table 28 gives 56.4% remaining in high quality, yet Table 30 has no acres to
  maintain, initiate or engage. (new)
- Anchialine pools and lava tubes: the text says East Maui only; Table 28 also marks Molokaʻi. (new)
- Figure 27 has five numbered areas, but the text names four. (new)
- Appendix 9 defines statistical power backwards. (new)
- Appendix 8 is empty ("Reserved for the final version").
- Appendix 5: "Find My Habitat" vs "Find My Microhabitat"; sections 3–5 empty.
- Literature Cited: USFWS 2026 and Martin et al. 2012 are cited but missing; year mismatches for
  Camaclang, Kehoe and Fortini; "Elinga" should be Elzinga.
- Bird tables: kiwikiu and ʻākohekohe numbers differ between table and text; the ʻuaʻu total
  doesn't add up (6,750 printed, 6,250 from island values); seabird S27 persistence is 58% vs 59%.
- Figure text: "OptimTCE" in Figure 1; "Optimization footprint" legend labels in Figures 23–24.
- Spellings: *Lymnaeidea*, *Rynchogonus*/*Rhyncogonus*, *blackburnii*/*blackburni*,
  *Hydrobates*/*Oceanodroma*.

---

## 4. Still to do

1. Field photography and partner logo files (1.5).
2. Decisions in 1.1–1.4, then update the content files and rebuild.
3. Recapture the ACP screenshots and draw the ACP edit-cycle diagram (placeholder on the Tools page).
4. Hawaiian-language and accessibility review by DOFAW web staff.
5. Hosting decision, then `python3 tools/build.py --release`.
