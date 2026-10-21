# Notes: task `ecomon` (Ecosystems + Monitoring pages)

Files written:
- `content/pages/ecosystems.md`
- `content/pages/monitoring.md`
- `content/data/ecosystems.json` (adds `islands`, `opportunities` from Table 30, `guidelines`, and `key_areas` per priority beyond the brief's minimum schema)
- `content/data/monitoring.json` (adds `src` per item and `in_core_program` on objective types)

Sources read in full: plan lines 3529-4575 (Ch 7, Ch 8) and 7775-8152 (App 8, App 9); also Ch 3e (lines 817-833) for the ecosystem team description. Tables 28 and 30 checked against PDF pp.99 and 105 (both match the text extract). Figures 27-28 viewed at PDF pp.108-109 to match map numbers to place names. Renders are in `_source_extracts/ecomon/`.

PDF page = printed page + 9 for Ch 7-8 (for example, printed p.99 = PDF p.108).

## Discrepancies and internal inconsistencies

1. **Montane Dry: Table 28 vs Table 30 vs text.** Table 28 (line 3606) gives 56.4% of the original extent remaining in high quality, with a goal of 56%. Table 30 (line 3835) gives 0 acres for Maintain, Initiate and Engage, and 0.6k acres (41.6%) for Restore. For every other ecosystem, Maintain + Initiate + Engage roughly equals Table 28's "% remaining". The text (lines 3639-3640) says "little native-dominated vegetation left", which fits Table 30, not Table 28's 56.4%. The page reproduces both tables as printed. DOFAW should confirm which is right.
2. **Anchialine pools and lava tubes: island distribution.** The text says both are "restricted to East Maui" (lines 3579, 3581-3582). Table 28 (lines 3612-3613; PDF p.99) marks both on Molokaʻi as well as Maui. The page reproduces the table and does not repeat "restricted to East Maui" in the feature list. DOFAW to confirm.
3. **Goal % for Montane Mesic.** Guideline i (lines 3851-3854) stresses ecosystems with less than 40% remaining, and the goal for Lowland Arid, Dry and Mesic is raised to 40%. Montane Mesic has 29.4% remaining but a goal of 29%, not 40%. The goal for other ecosystems equals the remaining percent rounded down (91.6 → 91, 83.9 → 83). Is this intended? The page states the 40% figure only for the "most reduced lowland ecosystems".
4. **"Long-term goals ... are provided in Table 30"** (line 3818). Table 30 gives opportunity acreage by category, while the goals ("MNLCP Goal % Managed") are in Table 28. The page doesn't repeat the sentence.
5. **Tables 29 and 31 duplicate each other.** They are identical except that Table 31 numbers Maintain/Initiate/Engage 1-3. The page shows one merged table.
6. **Figure 27 has five numbered areas, but the text names four** (windward Haleakalā, two areas on Molokaʻi, Lānaʻihale; lines 3926-3929). From the figure: 1 = windward/NE Haleakalā; 2 and 3 = two areas in central Molokaʻi; 4 = Lānaʻihale; 5 = an unnamed area on the southern/leeward flank of Haleakalā. `ecosystems.json` lists area 5 as "not named in plan text". **DOFAW needs to name area 5.**
7. **Figure 28 numbers vs names.** The text lists eastern Molokaʻi, above Makawao and Kahikinui (lines 3961-3963) without numbers. From the figure, 8 = eastern Molokaʻi, 6 = above Makawao (windward Haleakalā), 7 = Kahikinui. This matching is my reading of the map, so please confirm.
8. **"Lowland Arid" rounding.** Maintain + Initiate + Engage = 0.4% vs 0.5% remaining in Table 28. Minor rounding. Lava Pioneer acres vs % differ slightly (5.5/12.4 = 44.4% vs 44.9% printed). Both are reproduced as printed.
9. **App 9 definition of "Power" is incorrect** (line 7829): "Power is the risk of failing to detect a true change". That is the Type II error rate (β); power is 1 − β, the probability of detecting a true change. The page and JSON use "the ability of a sampling design to detect a true change", which matches the plan's own next sentence and Ch 8's power-analysis text. This is a plan fix for DOFAW.
10. **"442 at-risk species across eight taxonomic groups"** (line 4082) is consistent with the plan elsewhere (lines 1068, 1110): seven SCP groups plus the Hawaiian hoary bat. Not a discrepancy, but other pages say "seven groups". The monitoring page keeps "eight taxonomic groups" as the plan does.
11. **"442 taxa ... across 492 planning units"** (lines 4288-4289). 492 is the combined recovery footprint (line 237; tracker table row "RC recovery PUs 492"), not all PUs in Maui Nui (1,400). The page labels 492 as the combined recovery footprint. No conflict with the tracker. Nothing in the tracker covers Ch 7, Ch 8 or App 9.
12. **Ch 3e (line 823-824) says some ecosystems are below "two percent"; Ch 7g (line 3816) says below "one percent".** Both are true (Lowland Arid 0.5%, Lowland Dry 2.1%). Noted only for consistency of site messaging.

## Messaging and wording decisions

- **"Conservation lands"** (Priority 2, line 3922: "Initiate management on conservation lands"). The messaging rules retire "conservation lands" in favor of "biodiversity reserves". However, the plan here means lands in *conservation status / conservation-oriented management potential* (DLNR lands plus Watershed Partnership agreements, lines 3709-3718), which is broader than biodiversity reserves (durable nexus). Swapping in "biodiversity reserves" would change the meaning, so the page says "lands already in conservation status". DOFAW may also want to fix the plan wording.
- **"HCA Partner Lands"** (Table 29/31 row label, lines 3754, 3877). "HCA" is not defined anywhere in the plan. The page renders it as "Unmanaged, partner lands". **DOFAW to define HCA.**
- **"Adaptive Conservation Planning software tool"** (line 4107) is an inconsistent tool name. The page uses "Adaptive Conservation Planner".
- **"Integrated Multi-scale Conservation Planning (IMCP) process"** (line 4122). The messaging rules call IMCP an "approach". The page uses "approach".
- Extraction and typo fixes not carried into text: "principals of landscape ecology" → principles (line 3549); "dones" → drones (line 3585); "Elinga" → Elzinga (line 4387); "medium" → median (App 9 line 7817); "temporal allocated" (line 7860).
- Partner credit: "ecosystem prioritization, led by UH Hilo" (plan line 152, Ch 3e heading line 817).
- "Feral ungulates" is glossed as "non-native hoofed animals such as goats, deer and pigs", based on plan line 488.

## Gaps (needed or useful for the page but missing from the plan)

1. **Appendix 8 is empty:** "Reserved for the final version" (line 7777), yet Ch 7b points to it for the ten ecosystems (line 3558). The ecosystems page relies entirely on Ch 7. If App 8 content exists elsewhere (for example, from the UH Hilo team), it is not in this plan version.
2. **No drawn adaptive management cycle in the plan.** The plan describes three components (collect, evaluate, decide; lines 4026-4027) and gives a monitoring-project stage cycle (Figure 29, from Sutter et al. 2015). The seven `cycle_steps` are my synthesis of Ch 8a, 8d and 8e, each with a plan citation. DOFAW should approve the step names. Alternative: a three-step cycle (Monitor → Evaluate → Decide) that matches the plan's wording exactly.
3. **The implementation monitoring card has no concrete species example** in the plan, only the generic "where, when, how, who". The card uses that wording.
4. **No area or acre totals for the numbered opportunity areas (1-8)**, and none for Priority 4 restoration areas. The ladder graphic can show names only.
5. **No climate-vector method details** (data source, time horizon) for Figure 26. The page describes only the qualitative result.
6. **No ecosystem-specific monitoring targets.** Ch 8 links monitoring to species PU targets, but there are no equivalent targets for ecosystems beyond Table 28's goal %.
7. **Ch 7 does not say whether the ecosystem layers (Figures 21-28) are in the ACP.** Line 3914 says the Conservation Planner "can be used to highlight larger opportunity areas", which implies they are. Confirm before the site links to the ACP for these layers.
8. Ch 8 mentions an example annual accomplishment report (America's Longleaf, URL at lines 4521-4524). This was left off the page. Add it as an external link if DOFAW wants one.

## Suggested images

- Figure 21 (ecosystem map), PDF p.98: hero image for the ecosystems page.
- Figure 22 (habitat quality), PDF p.101; Figure 23 (management potential), PDF p.102.
- Figure 24 a/b (plant richness, all vs habitat-loss species), PDF p.104: side-by-side slider.
- Figure 25 (management opportunities), PDF p.105: pair with the ladder.
- Figure 26 (climate vectors), PDF p.107.
- Figures 27 and 28 (numbered opportunity areas), PDF pp.108-109: the numbered callouts suit clickable hotspots on the priority ladder (2 → areas 1-5; 3 → areas 6-8).
- Figure 29 (stages of a monitoring project, Sutter et al. 2015), PDF p.121: reproduce only with a permission/credit check, since it is a third-party figure.
- Field photos (fencing, outplanting, monitoring plots, bog, anchialine pool) from the demo deck, if available. The plan has none in these chapters.

## Questions for DOFAW

1. Montane Dry: is 56.4% remaining (Table 28) or 0 high-quality acres (Table 30) correct?
2. Do anchialine pools and lava tubes occur on Molokaʻi (Table 28) or only on East Maui (text)?
3. What is Figure 27's area 5, and are my matches for areas 6-8 correct?
4. What does "HCA" mean in Tables 29/31?
5. Should Montane Mesic's goal be 40% like the other ecosystems below 40%?
6. Is the seven-step adaptive management cycle acceptable, or should the site use the plan's three components only?
7. Will App 8 be filled in before launch? If so, the ecosystems page should be re-checked against it.
8. Can the plan's "Power" definition (App 9) be corrected?
