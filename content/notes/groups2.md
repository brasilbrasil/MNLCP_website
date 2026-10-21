# Notes for task groups2 (Terrestrial snails, Terrestrial arthropods, Aquatic invertebrates, Hawaiian hoary bat)

Files written:
- `content/pages/groups/terrestrial-snails.md`
- `content/pages/groups/terrestrial-arthropods.md`
- `content/pages/groups/aquatic-invertebrates.md`
- `content/pages/groups/hawaiian-hoary-bat.md`
- `content/data/groups_part2.json`

Sources read in full: plan lines 2394-3241 (Ch 6 e-h), 5040-5285 (App 1 criteria, footprints, expert-led and OptimTFE groups, snail and arthropod detail), 7470-7774 (App 6, App 7). I also read the relevant parts of Exec Summary Table 1, Ch 4 Table 1, Ch 5 b-c, Ch 6 i-j (Tables 26-27), App 2 (results, Table 1, species groups, strategies S6-S16) and App 3. Line numbers below refer to `MNLCP 9-30-2026 FINAL.txt`. Tracker IDs (XP-nn) refer to `MNLCP_cross_product_discrepancies.md`.

## Discrepancies

### Terrestrial snails
1. **Appendix 6 row count and totals (XP-14).** App 6 is headed "Total (49 species)" but lists 48 rows (lines 7482-7553). *Amastra goniops* is missing; it is in App 3 (line 7016). All 48 rows are marked imminent extinction, yet the totals row says "Facing Imminent Extinction 47" (line 7546). Ch 4 Table 1 (line 995), Ch 6 e (line 2403) and Exec Summary Table 1 (line 201) all give 49. **Site:** uses 49 everywhere. It reproduces the 48 App 6 rows in a collapsed table, with a footnote that *A. goniops* is missing.
2. **Persistence values (XP-15).** Ch 6 e Table 18 (lines 2565-2579, p.61) gives "up to 63 percent" under S25, with S10 44.0, S13 36.9, S8 35.0, S11 31.9, S7 31.0 and S12 30.5. Table 26 (line 3410, p.85) and App 2 Table 1 (line 5678) give S25 56, S10 39, S13 37, S8 34, S7 30, S11 28 and S12 28. **Site:** Key numbers avoid a headline percentage and use the plan text "over 50 percent if effective control measures are found" (lines 2557-2561). Table 18 is reproduced as printed. The Table 26 values appear in a Details block.
3. **Exclosure split.** "4-6 exclosures already planned for construction, with 26 to be constructed in the future" (lines 2508-2510) reaches 32 only at the upper bound. Its relation to App 2 S10 ("4 new predator exclusion fences per year ... 20 fences total", lines 6333-6334) is not explained (XP-14). The site repeats the plan sentence.
4. **Site-screen attribution.** Ch 6 e (lines 2502-2507) says the OptimTFE process used elevation, slope, ruggedness, native habitat status, fire risk, climate resilience and habitat structure. Per the snail synthesis (§10.13), candidate sites came from a separate GIS screen; fire risk and climate resilience were OptimTFE ranking criteria. The site follows the plan but frames these as the factors candidate sites were judged on. DOFAW may want to reword.
5. **"39 of the 49 species" within 2 km (line 2552).** The 2026-07-20 project record (snail synthesis §10.12) reports 39 OTUs with usable data, all within 2 km except three outliers. The plan figure may overstate the result. The site quotes the plan.
6. **Priority and initial-implementation subsets.** Ch 6 e gives no count for the Figure 11 yellow (priority) or red (initial implementation) sites. App 1 gives 14 priority sites (line 5215). The red set may be a 10-site tier agreed on 2026-09-23 that is not among the release-candidate files (synthesis §10.19). The site uses 14 from App 1 and gives no count for the red sites.
7. **Recovery category.** Ch 4 Table 1 and App 6 put all 49 snails under Interim Recovery. Ch 6 e says recovery habitat is "deferred" (line 2548). Ch 6 i counts the 49 as having exclosure sites but no recovery habitat (lines 3248-3250), which explains 250 vs 299 (XP-01). The site presents three exclosure populations as the interim recovery goal, consistent with lines 2538-2544.
8. **PTM snail group (XP-16).** App 2 defines the PTM "Terrestrial Snails" group by genus (*Auriculella*, *Elasmias*, *Newcombia*, *Partulina*; App 2 Table 1 p.A2-20). This is not the 49-species list, so persistence figures refer to a different set of taxa. This is noted in a Details block.

### Terrestrial arthropods
9. **No PU counts in the plan (XP-08).** Ch 6 f and App 1 give no planning-unit count for the arthropod recovery or priority footprint. The release candidate (RC) has 61 recovery and 39 priority PUs. JSON uses `null`. The map will show RC layers, so the page text and the map will not agree on a number. The page says the plan does not state one.
10. **Priority footprint definition (XP-08).** The plan defines the arthropod priority footprint as "areas with populations of the nine arthropod species facing imminent extinction" (lines 2713-2715). The RC priority layer is a 39-PU, one-per-mauna subset holding all 64 footprint taxa. If the map shows the RC priority layer, its legend should not repeat the plan definition without a note.
11. **32 recovery species vs 64 taxa with targets (XP-03).** The plan's 32 (31 interim + 1 full) are the occurrence-driven taxa. The RC/ACP footprint holds targets for 64 taxa, including 25 Focal Area and 7 Basic Survey species. Map popups and species counts from the RC will exceed 32.
12. **Survey layer said to be in the ACP (XP-09).** Ch 4 (lines 972-974) says the Conservation Planner has a separate map of suggested area-survey PUs. App 1 (lines 5265-5267) refers to Focal Area Survey auxiliary layers. On 2026-09-30 the team said this product is not in the ACP. The arthropod page repeats App 1's "Using it" text in a Details block; confirm or soften before launch.
13. **Five imminent-extinction *Hylaeus* have no recovery habitat.** *H. facilis*, *hilaris*, *paumako*, *psammobius* and *volatilis* are in Focal Area Surveys (App 7) while having Table 19 emergency actions. This is consistent with the plan's note that some imminent-extinction species are in the survey category (lines 891-893). The site says so.
14. **Table 19 vs App 7 counts.** Table 19 "# Known Populations" (e.g., *H. anthracinus* 5, *H. longiceps* 3, *H. laetus* 1) differs from App 7 "All Known Occupied PUs" (15, 7, 7). These are different measures (populations vs PUs), but readers may be confused. The site labels each column as the plan does.
15. **Table 20 headers.** Table 20 headers (63/65/67 percent) are not the Table 26 S25 values (56/57/62). The text gives 65 percent unadjusted and 58 percent adjusted for the group (lines 2739-2742), which is consistent with Table 26. The headers are probably maximum-feasibility values, but the plan does not say.
16. **Spelling.** *Manduca blackburnii* (Ch 6 f, line 2703) vs *blackburni* (App 2, 3, 7); the site uses *blackburni*. *Rynchogonus* (5 rows) vs *Rhyncogonus* (4 rows) in App 7, probably one genus. App 3's common name "Anthricinan yellow-faced bee" looks like a typo for "Anthracinan"; it appears only in the JSON note.
17. ***Megalagrion* placement (XP-16).** Ch 6 f says *Megalagrion* is grouped with Aquatic invertebrates (lines 2746-2749). But App 3 and App 7 list *M. jugorum* and *M. molokaiense* as Terrestrial arthropods on Area Surveys, and App 2 includes them in the PTM damselfly group. This is noted on the aquatic page.

### Aquatic invertebrates
18. **Table 22 vs Table 26 (XP-15).** The *Megalagrion* column differs from Table 26 at 10 of 17 strategies (e.g., S6 43 vs 37, S12 47 vs 44). The headers 59/59/52 compare with Table 26 S25/S27 values of 54/53/47. The Lymnaeidae header of 52 percent contradicts Ch 6 j, which says freshwater snails fail 50 percent (lines 3324-3327). **Site:** Table 22 is reproduced as printed in a Details block, with the Table 26 values and the Ch 6 j statement beside it. The visible contradiction is deliberate so DOFAW can fix the plan.
19. **Priority areas (XP-10).** Figure 15 (p.73) maps priority (yellow) and initial implementation (red) areas. The July 2026 decision was not to create an aquatic priority subset, and the RC has none. JSON `priority_footprint_pus` is `null`. The page mentions the Figure 15 areas without a count.
20. **Table 21 recovery columns (XP-10).** The numbers under Interim/Full Recovery (e.g., *M. pacificum* 46, *M. xanthomelas* 40) are realized footprint PU counts, not population goals. The text says interim species have "goals of one population" (line 2933). The site labels these columns "the plan's entries" and does not interpret them.
21. **App 1 coverage statement.** App 1 says aquatic prioritization "covered 11 species" (line 5128), but the footprint covers 10 (Lymnaeidae lack data). It also says PUs "were then linked to named streams and diversions" (lines 5129-5130); no PU-to-stream file was found (XP-10). The site repeats the linking statement.
22. **Spelling of Lymnaeidae.** The plan uses "Lymnaeidea" (Table 21, App 3), "Limnaeidae" (Table 22) and "Lymnaeidae" (text). The site uses Lymnaeidae.

### Hawaiian hoary bat
23. **Table 24 vs Table 26 (new; not in XP-15).** Table 24 (lines 3217-3238, p.80) gives S16 49.2, S11 48.4, S6 48.3, S7 46.6, S10 44.7, S5 41.9, S9 41.9, S3 41.2 and S2 40.9, and 63 percent under S27. Table 26 and App 2 Table 1 (line 5685) give S16 47, S11 46, S6 44, S7 46, S10 43, S5 41, S9 41, S3 41 and S2 41, and 58 percent under S27. The text calls 63 percent the value "if this strategy were fully implemented" (line 3186), so it is probably the maximum-feasibility value, but the plan does not say. The site uses 63 percent with that wording and gives the Table 26 values in Details. **Suggest adding this to XP-15.**
24. **S16 contents.** Ch 6 h says S16 "targets minimization of bat mortality at wind energy farms" (lines 3188-3190). App 2's S16 task list words the turbine task as reducing *avian* collisions (lines 6457-6458) and mentions bats only in lighting outreach. The site states what App 2 lists. DOFAW may want a bat-specific wind task in App 2.
25. **Scientific name.** *Lasiurus semotus* (App 2, App 3) vs *Lasiurus cinereus semotus* (Literature Cited). The site uses the App 3 name.
26. **Priority footprint wording.** The bat planning-process line names a "priority footprint" (line 3118), but Figure 18 says "There are no priority footprints for the bat" (line 3175). The site follows Figure 18.
27. **Populations.** Table 23 gives "Current Populations 3", while the text says it is unknown whether there are three, four or one metapopulation (lines 3123-3125). The site shows both as printed.

### Cross-group
28. **Combined footprint species (XP-01, XP-04).** These are not used on these pages, except to explain why snails are counted separately (Ch 6 i, lines 3245-3250).

## Gaps (things the pages could use that the plan does not provide)
- **Hawaiian names.** The plan uses "kāhuli" only inside "kīpuka kāhuli". It does not gloss kāhuli as the Hawaiian name for land snails. The front matter and JSON use `kāhuli` for snails as the brief suggested; this needs Hawaiian-language review. The plan gives no Hawaiian names for arthropods or aquatic invertebrates (for example, none for *Hylaeus* or *Halocaridina rubra*), so `hawaiian_names` is empty for those groups. DOFAW could add reviewed names.
- **Common names for arthropod genera** (e.g., *Plagithmysus*, *Philodoria*, *Nesosydne*) are not in the plan and were left out. Only picture-winged flies, yellow-faced bees, sphinx or hawk moths and leafhoppers are named (App 1 lines 5233-5235).
- **Footprint sizes.** There are no plan PU counts for the arthropod, aquatic or bat footprints. RC values exist (arthropods 61 recovery / 39 priority; aquatic 81 recovery / none) but were not used in text, per the numbers policy.
- **Trends and status.** The plan gives no population trends for snails beyond statewide decline, none for arthropods or aquatic invertebrates, and none for the bat (no reliable estimate).
- **Group-specific monitoring.** Ch 8 and App 9 have no group-specific monitoring protocols for these groups. The monitoring sections draw only on Ch 6 text and App 2.
- **Glossary candidates:** "lateral entrainment" (Ch 6 g, line 3044), used without definition; "incidental take" (glossed on the bat page as "accidental killing or harm"; please check); OTU; anchialine pool (the page uses the plan's own definition, p.89 lines 3577-3580); naiad; metapopulation; population viability analysis.
- **Snail location sensitivity.** The project decided not to release snail range maps or raw locations publicly (snail synthesis §1). The plan's Figure 11 publishes the exclosure network at map scale. DOFAW should decide whether the public map shows exclosure sites, and at what resolution. Occurrence points should never be shown. Rare arthropod and damselfly sites raise the same question; the plan itself names Olowalu, Kahue, Ilio Point and Papanalahoa for *Hylaeus* fencing.

## Suggested images
- Snails: a Maui Nui *Partulina* or *Newcombia* tree snail; a kīpuka kāhuli fence in native forest (DOFAW / SEPP photo library); plan Figure 11 (p.60) for the network map.
- Arthropods: a *Hylaeus* yellow-faced bee on native coastal vegetation; Blackburn's sphinx moth; a picture-winged *Drosophila*; plan Figures 12 (p.66), 13 (p.67) and 14 (p.69).
- Aquatic invertebrates: *Megalagrion* damselfly; an anchialine pool with ʻōpaeʻula-type red shrimp (the Hawaiian name needs review); plan Figures 15 (pp.72-73), 16 (p.74) and 17 (p.76).
- Bat: ʻōpeʻapeʻa roosting or in flight (USFWS or DOFAW, permissions needed); plan Figure 18 (p.79).

## Questions for DOFAW
1. Should the site quote the per-group PTM tables (Tables 18, 20, 22, 24) or only Table 26 values? Several disagree (items 2, 18, 23). The draft shows both, with the chapter tables as printed.
2. Is the snail priority network 14 sites (App 1), and what is the red "initial implementation" set in Figure 11b (how many sites, and is it 7 funded or 10)?
3. Can the plan's "4-6 planned + 26 future" exclosure wording be reconciled to exactly 32, and with S10's 20 fences?
4. Should *Amastra goniops* be added to App 6 and the totals corrected (49 species, 49 imminent)?
5. Is the arthropod Focal Area Survey layer going to be in the ACP at launch? If not, the "viewed in the Conservation Planner" sentences should be removed.
6. Which aquatic "priority" areas, if any, should appear on the public map, given that the RC has no aquatic priority layer?
7. Do you approve "kāhuli" as the Hawaiian name for Terrestrial snails in page headers, and would you like reviewed Hawaiian names added for any arthropod or aquatic species?
8. How should public maps treat snail exclosure sites and rare invertebrate sites?
