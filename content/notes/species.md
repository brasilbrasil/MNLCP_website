# Notes: task `species` (At-Risk Species, Using the Plan, species.json)

Files written:
- `content/pages/species.md`
- `content/pages/using-the-plan.md`
- `content/data/species.json` (442 species)
- Parser, kept for rebuilds: `_source_extracts/species/parse_species.py` (reads the plan .txt) and `wrap.py` (adds `_source` and `fields`). `_source_extracts/species/full_layout.txt` is a `pdftotext -layout` copy of the PDF. It is identical in layout to the plan .txt.

Line numbers below refer to `MNLCP 9-30-2026 FINAL.txt`.

## 1. Count reconciliation

The species list in Appendix 3 (lines 6588-7078) has **442 rows**. Every group matches Ch 4 Table 1 (lines 982-999) and the Executive Summary Table 1.

| Group | App 3 rows | Plan Table 1 | Listed (data / Table 1) | Imminent (data / Table 1) | Interim | Full | Area surveys | Species surveys |
|---|---|---|---|---|---|---|---|---|
| Forest birds | 4 | 4 | 3 / 3 | 2 / 2 | 0 | 4 | 0 | 0 |
| Seabirds | 3 | 3 | 3 / 3 | 0 / 0 | 0 | 3 | 0 | 0 |
| Waterbirds | 5 | 5 | 5 / 5 | 0 / 0 | 2 | 3 | 0 | 0 |
| Plants | 197 | 197 | **174 / 175** | 102 / 102 | 0 | 195 | 0 | 2 |
| Terrestrial snails | 49 | 49 | 3 / 3 | 49 / 49 | 49 | 0 | 0 | 0 |
| Terrestrial arthropods | 172 | 172 | 8 / 8 | 9 / 9 | 31 | 1 | 82 | 58 |
| Aquatic invertebrates | 11 | 11 | 4 / 4 | 1 / 1 | 5 | 5 | 0 | 1 |
| Hawaiian hoary bat | 1 | 1 | 1 / 1 | 0 / 0 | 1 | 0 | 0 | 0 |
| **Total** | **442** | **442** | **201 / 202** | **163 / 163** | **88** | **211** | **82** | **61** |

The interim, full and survey columns match Table 1 exactly. The one mismatch is the number of listed Plants:
- **Listed Plants: App 4 gives 174, Table 1 gives 175.** The App 4 status column has 170 E and 4 T (its own totals rows, lines 7338-7339, agree), against 175 in Ch 4 Table 1 (line 994) and the Executive Summary Table 1. As a result the explorer's "listed" filter returns 201 species, against 202 in the text. This is already tracked as XP-07. **DOFAW: which plant is missing its status in App 4, or is 175 wrong?**
- Plant imminent extinction comes from the App 4 PEPP column. 102 rows are coded PEPP, which matches the App 4 legend (line 7340) and Table 1. Lines 1264-1266 equate PEPP plants with plants facing imminent extinction.
- Arthropod listed, imminent and category counts come from App 7. They match its totals rows (lines 7765-7770): 8 E, 9 imminent, 1 full, 31 interim, 82 area, 58 species-specific.

## 2. Parsing method and problems

- **App 3** (group, species, common name) was split on runs of two or more spaces. In two rows only one space separates the name from the common name, and these were special-cased: *Argyroxiphium sandwicense* subsp. *macrocephalum* / ʻAhinahina (line 6615) and *Pseudognaphalium sandwicensium* var. *molokaiense* / ʻEnaʻena (line 6770).
- **App 4** (Plants) was parsed by tokens. The status codes {E, T} and PEPP codes {PEPP, POP, ROI, NO} do not overlap, so blank cells cannot be misread. I checked page A4-1 against the rendered PDF (PDF p.194) and it matches the text layer. All 197 App 3 plants matched an App 4 row. The App 3 name "Tetramolopium sp. Nov 2" matches App 4 "Tetramolopium sp. nov. 2 (Mauna Kahalawai)" (line 7327). App 3 uses "subsp." where App 4 uses "ssp.".
- **App 6 / App 7 / Table 21** were parsed by column position. Each value was assigned to the nearest column header on its own page, because column offsets shift between pages. App 7 pages A7-3 and A7-5 (PDF pp.209, 211) were checked against the rendered PDF, including the area-survey versus species-survey X marks, and they match.
- **Vertebrates** (Forest birds, Seabirds, Waterbirds, bat) have no appendix table. I entered them by hand from Ch 6 Tables 5, 9, 13 and 23 and the species accounts (lines 1420-1484, 1655-1692, 1828-1866, 3122-3151). Their table rows wrap across lines, which makes automatic parsing unreliable. Each record carries `other.ch6_source`.
- **Aquatic invertebrates** were enriched from Ch 6g Table 21 (lines 2885-2899). This is outside the assigned appendices, but it is the only per-species table for the group.
- **Common and Hawaiian names.** The App 3 "Common Name" column mixes Hawaiian names (Haha, Koʻokoʻolau, ʻOha wai) with English ones (Round-leaved chaff-flower, Maui remya). I split them mechanically. An entry made up only of Hawaiian-alphabet letters went to `hawaiian_name`; anything else went to `common_name`. Two mixed entries were split by their "(=…)" pattern: Lanai sandalwood (=ʻiliahi) and (=Native yellow hibiscus) maʻo hau hele. The raw cell is kept in `other.app3_common_name_raw`. I checked the full list of splits by eye. "No common name" (56 rows) becomes null.
- **ʻokina.** Backticks were converted to ʻ (U+02BB). "Newell''s" (line 6827) was fixed to "Newell's". No kahakō were added to plant names. Bird and bat Hawaiian names use the Ch 6 spellings (ʻĀkohekohe, ʻAlae keʻokeʻo, Nēnē, ʻŌpeʻapeʻa), because App 3 drops the kahakō and some ʻokina, for example "`Akohekohe" and "alae ke`oke`o".
- **Islands are not in any species appendix.** `islands` is null except for the four Forest birds (currently East Maui only, lines 1428, 1436-1437, 1447, 1454) and the Hawaiian hoary bat (Maui, Molokaʻi, Lānaʻi, observed on Kahoʻolawe, lines 3122-3123). This means **the explorer cannot offer an island filter** unless DOFAW supplies island data, for example from the master species list.

## 3. Discrepancies and oddities in the plan (with line refs)

1. **App 6 omits *Amastra goniops*.** App 3 lists it (line 7016), but App 6 has 48 rows (lines 7487-7541) under "Total (49 species)" (line 7544). The App 6 totals row also says 47 species face imminent extinction (line 7546), while all 48 rows carry the X and Ch 4 / Table 1 say 49 (lines 995, 1072). This is tracked as XP-14. In the JSON, *A. goniops* is flagged imminent (from Table 1) with `listing_status` null and no App 6 data.
2. **Plant listing: 174 vs 175.** See section 1 (XP-07).
3. **Table 4 (lines 1280-1289) does not add up.** It is reproduced in full inside a collapsed details block on Using the Plan, with a DOFAW REVIEW comment. Problems:
   - Option 2: 195 target species but 161 total.
   - Option 3: 101 PEPP + 78 non-PEPP = 179, against a total of 175, and 101 target species.
   - Option 4: 36 target species, but 68 PEPP and 120 total.
   - Option 5: 21 + 19 = 40, against a total of 50.
   - The 155-PU plant priority footprint (lines 1258, 1286) differs from App 1 and the release candidate, both 181 PUs.

   These are tracked as XP-05 and XP-07. **DOFAW: fix Table 4, or drop the species columns from the website version?**
4. **Table 2 terminology** (line 1051): it prints "Snails" and "Establish snail enclosures". The website table uses "Terrestrial snails" and "snail exclosures", following the group-name rules and the messaging guide (kīpuka kāhuli are exclosures). The plan should probably be fixed too.
5. **Footprint levels.** Ch 5e says "Each taxonomic group has at least two levels" (line 1248) and then lists three: full, priority and initial implementation (lines 1251-1254). The website lists the three without the count. Ch 5 also uses "Priority Recovery Footprint" where the messaging guide says "priority footprint".
6. **374 vs 442 species.** Ch 3d and App 2 (lines 791, 797, 5302, 5391, 5540, 5696) give 374 species for the PTM analysis. Both pages use 442, the plan's main figure. Tracked as XP-17.
7. **Area-survey map in the Conservation Planner.** Ch 4 (lines 962-963, 973-974) says data-deficient species and a separate area-survey map appear in the Conservation Planner. Tracker XP-09 says the search-priority product is not in the ACP. I left this claim **off** the species page. **DOFAW: confirm before adding it.**
8. **Survey category names differ.** Ch 4 and Table 1 use "Area Surveys" and "Species-specific Surveys". App 7 totals (lines 7769-7770) use "Focal Area Surveys" and "Basic Species-specific Surveys". The site uses the Ch 4 names.
9. **App 4 values that look odd** (printed values were kept):
   - *Argyroxiphium sandwicense* ssp. *macrocephalum* has 1 desired recovery population but 10 recovery PUs (line 7092). I confirmed this on the PDF.
   - Several plants have more recovery PUs than desired populations, for example *Tetramolopium rockii*, 5 vs 10 (lines 7325-7326). Planning units are not populations, so this may be correct.
   - *Sicyos hillebrandii* has 1 known occupied PU but 0 inside the recovery footprint (line 7301).
10. **Undefined App 4 codes.** The PEPP column uses "NO" for 17 species and is blank for 29. The legend (lines 7340-7342) defines only PEPP, POP and ROI. **DOFAW: what do "NO" and blank mean?**
11. **Snail current populations.** App 6 prints ranges ("5-10" for 9 taxa, "15+" for *Partulina redfieldi*, line 7515). These are kept as text in `other.current_populations`.
12. **Table 21 recovery values** (aquatic, lines 2888-2898) are numbers such as 46 and 40 in the recovery columns. They look like PU counts, not population goals (XP-10). They are stored as `other.table21_recovery_value`, and the website text does not present them as population goals.
13. **Name spellings and typos in App 3** (kept verbatim in `scientific_name`; DOFAW should decide whether to correct them in the plan and on the site):
    - "Lymnaeidea ssp" (line 6595). Table 21 has "Lymnaeidea spp." (line 2891) and the Ch 6g text has "Lymnaeidae spp." (lines 2944, 5860). The correct form is presumably Lymnaeidae spp.
    - "Rynchogonus" ×5 (lines 7003-7007) next to "Rhyncogonus" ×4 (lines 6999-7002). App 7 has the same split.
    - "Anthricinan yellow-faced bee" for *Hylaeus anthracinus* (line 6896).
    - "Anchialine pool Shrimp" and "Newcomb's Tree snail": odd capitalization (lines 6594, 7026).
    - "Hydrobates castro" (line 6825). The Ch 6b text uses *Oceanodroma castro* (line 1670).
    - *Gallinula galeata sandvicensis*: App 3 calls it "Hawaiian common gallinule" (line 7072), while Ch 6c calls it "Hawaiian moorhen" / ʻalae ʻula (lines 1837, 1863).
    - *Paroreomyza montana newtoni* (App 3 line 6605) appears as *P. montana* in Ch 6a (line 1450).
    - Plant Hawaiian names vary in capitalization ("haha" vs "Haha") and carry no kahakō (for example Popolo, Kolea, Kokiʻo). These need Hawaiian-language review; this is out of scope for the draft per PLAN.md §6.
14. **Entries that are not single described species** but are counted among the 442: "*Plagithmysus*" (genus only, line 6977), "*Nesotocus* spp." (6947), "*Philodoria* sp.", "*Philodoria* sp. 2", "… sp. n" (6966-6972), "*Proterhinus* sp." (6997), "*Rynchogonus* sp." (7005), "Lymnaeidea ssp" (6595), and several snail "ssp." and "sp. 1" entries (7027, 7038-7044, 7052, 7063, 7067-7068). The species page mentions this in one sentence.
15. **Two damselflies are counted as Terrestrial arthropods.** *Megalagrion jugorum* and *M. molokaiense* are listed as Terrestrial arthropods in App 3 and App 7 (lines 6927-6928, 7669-7670), while the other three *Megalagrion* are Aquatic invertebrates. PTM groups them with the aquatic damselflies (XP-16). This is kept as in App 3.
16. **The forest bird recovery goal "3"** in Table 5 (lines 1478-1483) is stored as `recovery_goal_populations` = 3. Tracker XP-24 notes other inconsistencies between the bird tables and the text. Population figures were not used on these pages.

## 4. Gaps (things the pages could use that the plan lacks)

- Island-level distribution for most species (see above).
- English common names for 56 rows marked "No common name", and for rows that give only a Hawaiian name.
- A definition of the Table 21 recovery-column numbers and the App 4 "NO" code.
- The plan gives no per-group split of the 240 not-listed species. It can be derived (Table 1 at-risk minus listed), but the pages do not show it.
- Ch 5 does not say outright that the recovery footprints can be viewed in the Conservation Planner, although App 5 presumably does. So step 3 of the manager walk-through does not say it either. The tools page should cover it.

## 5. Suggested images

- Plan PDF p.22, **Figure 2**: combined recovery footprint (green) and priority areas (yellow). For Using the Plan, "Where to work".
- Plan PDF p.25, **Figure 3**: expected persistence by group under four scenarios. For Using the Plan, "What the results show". It could be redrawn as SVG from App 2 values.
- Plan PDF p.28, **Figure 4 a-e**: plant footprint narrowing. This sits in the details block. Note the 155-PU caveat (XP-05).
- For the species page: photos of a species from each group facing imminent extinction (a PEPP plant, a *Partulina* tree snail, a *Hylaeus* bee, kiwikiu, *Megalagrion nesiotes*), if the demo deck or DOFAW has licensed images.

## 6. Questions for DOFAW

1. Listed Plants: is it 174 (App 4) or 175 (Table 1)? Which species is affected?
2. Should *Amastra goniops* be added to App 6? What are its current-population and listing values? Should the App 6 imminent total read 49?
3. Table 4: correct the species columns, or show only Option / PUs / Area on the site? Should the site show the 181-PU priority footprint instead of 155?
4. What do the App 4 PEPP-column values "NO" and blank mean?
5. Should spelling fixes (Lymnaeidae, Rhyncogonus, anthracinan, Hydrobates vs Oceanodroma, gallinule vs moorhen) be made on the site ahead of a plan revision, or should the site mirror the plan verbatim?
6. Can DOFAW supply island data per species, so the explorer can filter by island?
7. Is the area-survey map and the data-deficient species list in the Adaptive Conservation Planner now? (Ch 4 says yes; XP-09 says no.)
8. The silversword (*Argyroxiphium sandwicense* ssp. *macrocephalum*) shows 1 desired recovery population in App 4. Is that intended?
