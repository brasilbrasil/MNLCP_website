# Notes: task `actions` (footprints.md, actions.md, strategies.json)

Plan = `MNLCP 9-30-2026 FINAL.txt` (DOFAW version 2026-09-29). RC = release-candidate footprints
of 2026-09-25 (`release_candidate_footprints_20260925.md`). XP-nn = items in
`MNLCP_cross_product_discrepancies.md`. PDF page = printed page + 9 for the main body (e.g. printed p.85 = PDF p.94).

Files written:
- `content/pages/footprints.md`
- `content/pages/actions.md`
- `content/data/strategies.json` (built by `_source_extracts/actions/build_strategies.py` from
  `_source_extracts/actions/app2_table1_persistence.txt` = plan lines 5664-5687; rerun with
  `python3 -I build_strategies.py app2_table1_persistence.txt ../../content/data/strategies.json`)
- Scratch: `_source_extracts/actions/` (page renders of Table 25-26, App 2 Figs 4-6 and Appendix Figs 1-3, word/line dumps of App 2 Appendix Table 1).

## 1. What the map will show that differs from the plan text

The map uses the RC footprints. The page text uses plan figures. These differences will be visible to anyone who clicks around, so they should be resolved or explained before launch. The footprints page has a callout saying counts on the map may differ slightly because footprints are living products. DOFAW should confirm that wording.

| Item | Plan (text) | RC / map | Notes |
|---|---|---|---|
| Combined recovery footprint PUs / area | 492 PUs, 1,050 km² (p.81 l.3244-3245; p.vi l.237) | 492 PUs, 1,050.32 km² | Match. |
| Combined recovery species | 299 (p.vi l.237) or 250 (p.81 l.3246) | 330 taxa (sum of per-group counts) | XP-01, Explained. 250 = 299 − 49 snails (snails have exclosure sites, not recovery habitat); 299 = 442 − 143. RC counts 64 arthropod taxa with targets vs the plan's 32 and has no bat. **Page text says "250 species with recovery habitat, plus exclosure sites for all 49 snails, 299 in all",** which is consistent with both plan figures. The map's PU pop-ups and richness view will count RC taxa, so totals will not add to 299. |
| Combined priority footprint | 216 PUs, 457 km², 267 species, "about 43 percent" (p.81 l.3267-3270; p.vi l.239-240) | 237 PUs, 505.64 km², 305 taxa (302 with a target), 48.2% | **XP-04, Open; the PU gap is unexplained.** Most visible difference on the map. The plan's 43% will not match a map showing 237/492. |
| Plant priority footprint | 155 PUs (Ch5e Table 4 / Fig 4b, Ch6d, glossary l.4857) vs 181 (App 1 l.5149) | 181 PUs, 182 taxa | XP-05. The plan body uses a superseded set. The footprints page does not quote any plant number. |
| Aquatic invertebrate priority | Plan Fig 15 shows priority and initial implementation areas | None (no ACP rows flagged) | XP-10. The map will have no Aquatic invertebrates priority layer. The legend entry for Aquatic invertebrates does not mention priority areas. |
| Seabird, Forest bird, Waterbird priority layers | Plan Figs 6-8 | 18, 28 and 3 PUs | XP-11, XP-12, XP-13 (seabird layer by visual reading differs; nēnē wording; forest bird caption). |
| Hawaiian hoary bat | Recovery footprint = six other groups combined, no priority footprint (Fig 18, l.3163-3175) | Not an SCP group; no layer | Legend says "no separate layer". If the build team creates the bat composite (the 2026-09-30 CG Weekly said it would become an ancillary ACP layer), update the legend. |
| Terrestrial snails | 32-site exclosure network, 14-site priority network (App 1 l.5214-5216) | 32 sites / 14 sites | Match. The snail "PUs" are candidate exclosure sites, not standard planning units. They are counted in the combined PU totals, so the map should draw them differently or explain this (legend does). |
| Planning-unit network | "1,400 medium-sized planning units" (l.763, l.4849) | Criteria layer has 1,417 PUs; five offshore-islet PUs (4098, 6149, 6152, 6161, 8039) are in footprints with NA criteria | Minor. Text says "about 1,400". Pop-ups for islet PUs will have no criteria values. |
| Land status | 65.7% "lands already oriented towards conservation" (l.3253-3255); exec summary "about 66 percent ... conservation-oriented land" | `top_consv_pct` 65.68 = biodiversity-reserve share (XP-26 resolved) | Page keeps the plan wording. Messaging prefers "biodiversity reserves" over "conservation lands". DOFAW could reword to "within biodiversity reserves" since XP-26 shows that is what 65.7 measures. |
| Fencing | "at least some degree of ungulate fencing (50 percent)" | 50.24% ungulate managed | Match. |
| Initial implementation areas | Fig 19c (combined), per-group initial implementation footprints | Not in the RC set | The map cannot show this level. The page describes it in text only. |
| Richness view | Fig 20: target richness across the priority footprint | RC `mega_footprint.gpkg` counts SCP taxa with targets | Will differ from plan counting (arthropods 64 vs 32). Max species per PU: RC recovery 48, priority 24. |
| Release dating | The plan text does not mention the RC | RC 2026-09-25 (plant priority rebuilt 2026-09-28) | Footprints-page callout says "the footprint release used in the Adaptive Conservation Planner (September 2026)". Also XP-18: the 181-PU plant priority footprint was not yet in the ACP as of 2026-09-30, so "used in the ACP" may be premature. |
| Late plan-map edits | Some late edits were made in plan maps only | Not in RC/ACP | XP-19. |

## 2. Discrepancies in the plan's action-prioritization material

1. **Table 25 omits S10 from S25.** Ch6j Table 25 (printed p.85, PDF p.94, checked on the rendered page) has no X for S10 (future predator exclusion fences) in the S25 column. Ch5d Table 3 (l.1141-1162) and App 2 Table 2 (l.6522-6535) both include S10 in S25. The JSON follows Table 3 / App 2 and notes the conflict.
2. **S26 composition.** The App 2 Table 2 name for S26 includes "Invertebrate Pest Control", but its component list (l.6543-6546) omits it. Table 25 marks S8 in S26. The JSON includes S8.
3. **Column labels.** Table 26 labels the current-status column "C (Only Current Actions)" and no action "S1". App 2 Table 1 labels current status "B" (baseline) and no action "C" (counterfactual). The values are identical. The JSON uses `baseline_persistence_pct` and `counterfactual_persistence_pct`.
4. **App 2 Table 1 caption** cites "Equation (4)" for persistence. The persistence formula is Equation (3); Equation (4) is the complementarity objective. The extracted Equation (4) is also missing its budget constraint (text mentions C_i and y_i that do not appear in the formula; l.5508-5512).
5. **Groups reaching 50%.** App 2 (l.5550-5553) says that after feasibility, one group (Blackburn's sphinx moth) exceeds 60% and "10 species groups" have a maximum between 50 and 60%, which would make 11 groups at 50% or more. App 2 Table 1 / Table 26 show 9 groups at 50-60% plus the moth, so 10 groups, with 7 failing. Table 26's caption ("Seven groups did not reach the 50 percent level") and Ch6j (six plant groups plus freshwater snails) agree with the table. The page uses "10 of 17", derived as 17 − 7 from Table 26.
6. **Fence counts.** App 2 Table 2 S10 lists 20 waterbird predator exclusion fences (l.6351-6353). The App 2 Figure 6b cost breakdown lists 20 snail exclosures, 20 seabird predator fences, **14** waterbird predator fences and 30 miles of ungulate fencing (read from the figure, PDF p.154).
7. **Annual cost figures.** The App 2 abstract says "for average annual cost of $26M efficiencies may be gained across groups by increasing management collaboration" (l.5306-5308). It is unclear what the $26M covers, and it appears nowhere else. The Results and Discussion give ~$55M/yr to secure all groups at 40% (l.5610, 5617-5618), ~$53M/yr recurring plus ~$67M upfront (l.5712-5714). Figure 5 places "S25 + S27" at roughly $51M/yr (visual reading). The site uses $55M, $67M and $53M and does not quote $26M. **Ask DOFAW what $26M refers to.**
8. **Cost units.** App 2 Table 1 gives "Total Cost (M $)" without stating the period. The values are consistent with 20-year totals (S25 $895M ≈ $45M/yr; S27 $773M ≈ $39M/yr ≈ "~$40M per year"). `cost_annual` in the JSON is total ÷ 20, labeled as derived. Combination costs are not the sum of their components (S25's components sum to $948M against $895M; S18's sum to $783M against $730M), and the plan does not explain why. Possibly shared costs; ask the PTM team.
9. **Plant Group 1 size.** The plant chapter gives Group 1 n = 42 (l.2255), but App 2 Appendix Table 1 lists only 34 names for it (counted from the PDF table cells, pp.A2-21 to A2-22). The other five plant groups match (23, 30, 75, 13, 13). With 42, plants total 196 (XP-07). The JSON uses 42 and notes the conflict.
10. **374 PTM species cannot be reconstructed.** App 2 Appendix Table 1 lists 242 entries: terrestrial snails as 22 genera, and freshwater snails and anchialine shrimp as one entry each. With Group 1 = 42 it would be 250. Also XP-17: the PTM manuscript draft gives 372 species in 15 groups. App 2 Background still says "more than 300 species" (l.5333, 5340). The site uses the plan's 374 / 17 groups.
11. **PTM group membership** (XP-16): the waterbird PTM group omits the gallinule (4 of 5 at-risk waterbirds), and the damselfly group includes *Megalagrion jugorum* and *M. molokaiense*, which App 3 lists as Terrestrial arthropods. Noted in JSON `species_groups[].notes`.
12. **Per-group persistence values** (XP-15): several taxon-chapter tables report values that differ from Table 26 / App 2 Table 1 (e.g. snails 63% vs 56% under S25; aquatic headers 59/59/52 vs 54/53/47). The site quotes only Table 26 / App 2 Table 1 values. Taxon-page drafters should be warned.
13. **S27 naming**: "bird-focused" (Ch5d l.1118, Table 25), "bird- and bat-focused" (exec summary l.257-258), "more focused on birds and the bat" (Table 3 caption l.1135-1136). The site uses "birds and the bat".
14. **Purpose framing.** Ch3d says PTM strategies were "aimed at recovering 374" species (l.791). App 2 frames the work as preventing extinction over 20 years and says future processes are needed for recovery (l.5768-5770). The actions page follows App 2 ("prevent extinctions over the next 20 years").
15. **Ch5d vs Figure 3.** Ch5d says all groups "had the potential to reach a 50 percent likelihood of persistence" if all actions were implemented and effective (l.1161-1163). Ch5 Figure 3 shows Plants at about 50% at maximum feasibility. App 2 (not feasibility-adjusted, all strategies) says at least 40% for all groups. These statements are roughly consistent, but "potential to reach 50%" for Plants rests on the red (less feasible) bar alone.
16. **Table 27** lists two rank-3 strategies for Plant Group 4 (S3 and S13). The "Groups selecting" totals (S13 = 13, S8 = 7, S7 = 6, …) are copied into the JSON as printed.
17. **App 2 Table 2 numbering quirks** kept as printed in `actions_list.number`: S12 has no item 2; S14 has two items numbered 2.

## 3. Messaging / PRA issues in the source

- App 2 is the UH Mānoa report reproduced as is. It uses "Data Collection", "Data were elicited from land managers", "structured elicitation approach", "focus groups", "we asked experts", "modified Delphi elicitation protocol", "optimal/optimize", "spatial optimization component" (l.5747, XP-22) and "a blueprint for successful conservation" (l.5366). The website does not reuse that language. Expert engagement follows Ch3d (l.787-792): "DOFAW and UH Mānoa convened collaborative workshops in which roughly 100 land managers and scientists contributed professional judgment through open-ended discussions". The methods digest describes the estimating process plainly, without "elicitation". **DOFAW should check that the methods digest is acceptable for PRA purposes**, since PTM is inherently a structured estimation exercise and the digest still describes experts giving best/lowest/highest estimates.
- Footprints page credits "spatial prioritization, led by USGS" once, per CONTENT_GUIDE. The actions page credits "Action Prioritization Team, led by UH Mānoa".
- "Footprint" terms: the plan never uses the phrase "preventing extinction footprint" for snails (grep found none). It calls them the "exclosure network" and "priority network", so the site uses those terms.

## 4. Gaps (things the pages need that the plan lacks)

- **"Not regulatory" statement.** The plan says the MNLCP is decision support "rather than ... top-down prescriptive mandates" (l.619-620, 4825), but never says footprints are not regulatory designations or critical habitat, or that they create no obligations for landowners. The footprints page says only what the plan supports. **Recommend DOFAW add an explicit sentence,** since landowners viewing a public map will ask.
- **Data sensitivity on a public map.** The plan and App 5 say the Conservation Planner "is not a public web map" (l.7363). Showing species-level PU information publicly (rare plant and snail locations) may need DOFAW approval. Consider showing only group-level footprints and richness without species names.
- Per-strategy **feasibility** values are not reported (JSON `feasibility: null`).
- Per-strategy **annual costs** are not printed (JSON derives total ÷ 20; plan gives approximate annual values only for S25, S27 and the overall program).
- App 2 Table 2 refers to maps M2-M17 ("see M3 Map") that are not in the plan. Ask whether they exist and can be linked.
- No numeric climate-resilience figure for the footprints ("greater-than-average", l.3261-3262). The RC mean is 2.44 on an unstated scale and is not used.
- The plan has no spatial "combined priority actions" product. App 2 and the topic summary say combining PTM benefits with footprints is future work. The actions page presents combined actions as S25 + S27 plus sequencing, which is what Ch5d/Ch6j provide.
- Emergency-action detail beyond Ch5b Table 2 lives in the taxon chapters (not in this task's ranges). The actions page links conceptually to group pages.

## 5. Suggested images

- Footprints page: plan Figure 19 a-c (printed p.82, PDF p.91); Figure 20 richness heat map (p.83, PDF p.92); Executive Summary Figure 1 (p.vi). Better: render fresh maps from the RC GeoPackages so they match the interactive map, or skip static figures since the Leaflet map is on the page.
- Actions page: Ch5 Figure 3 / Exec Summary Figure 2, persistence under S25/S27 (p.25, PDF p.34). Better rebuilt as an SVG chart from `strategies.json` (no action / current / S25 / S27 per group), since the plan figure aggregates to eight groups without printed values. App 2 Figure 6 cost breakdown (p.A2-13, PDF p.154). App 2 Figure 5 cost curve (p.A2-12, PDF p.153), which could be rebuilt as SVG from `results_summary.cost_curve_all_groups_40pct` (step labels are exact; x-values would need the PTM team's numbers). Table 25 strategy-composition grid (p.85, PDF p.94) as an interactive matrix, after fixing the S10/S25 cell.
- Photos: fence construction, kīpuka kāhuli exclosure, propagation facility, mosquito-control release (from the deck, if credited).

## 6. Questions for DOFAW

1. Combined priority footprint: keep the plan's 216 PUs / 267 species in text while the map shows 237 / 305, or update the plan (XP-04)?
2. Is S10 part of S25 (Table 3 / App 2) or not (Table 25)? Is S8 part of S26?
3. What does the App 2 abstract's "$26M average annual cost" refer to?
4. Are the App 2 Table 1 costs 20-year totals? Why are combination costs lower than the sum of their components?
5. Waterbird predator fences: 20 (Table 2) or 14 (Figure 6b)?
6. Plant Group 1: 42 species (Ch6d) or the 34 listed in App 2?
7. May the public map show species-level information per planning unit?
8. Will DOFAW add a sentence that footprints are not regulatory designations and create no landowner obligations?
9. Is the methods digest's description of expert estimates acceptable under the PRA guidance?
10. Should the 65.7% figure be phrased as "within biodiversity reserves" (XP-26)?
11. Should the map include the bat composite layer and the initial implementation areas (neither is in the RC set)?
