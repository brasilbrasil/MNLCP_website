# Notes: task groups1 (Forest birds, Seabirds, Waterbirds, Plants)

Files written:
- `content/pages/groups/forest-birds.md`
- `content/pages/groups/seabirds.md`
- `content/pages/groups/waterbirds.md`
- `content/pages/groups/plants.md`
- `content/data/groups_part1.json`

Sources read in full: plan lines 1390-2393 (Ch 6a-d), App 1 lines 5060-5280, App 2 lines 5278-6587
(results, Table 1, Table 2 strategy list), plus Ch 4 Table 1 (lines 980-1000), Ch 5b Table 2
(lines 1020-1056), Ch 5e Table 4 (lines 1245-1330), Ch 6i (lines 3240-3275), Ch 6j Tables 26-27
(lines 3310-3520), App 3 and App 4 rows for the example plants. Line numbers below refer to
`MNLCP 9-30-2026 FINAL.txt`. Printed page = PDF page - 9 for Ch 6 (for example Figure 5 is printed
p.34, PDF p.43).

## Discrepancies

### Plants
1. **Plant priority footprint: 155 vs 181 PUs (tracker XP-05, "Plan fix suggested").** Ch 5e
   (p.27, line 1257-1259 and Table 4 line 1288), Ch 6d (p.50, line 2164) and the glossary (line 4857)
   give 155 PUs. App 1 (p.A1-6, lines 5148-5149 and 5170-5171) gives 181, which matches the RC
   and the ACP. Per the numbers policy, the pages use 155 in text and Key numbers, with an HTML
   comment, and the plants practitioner block notes App 1's 181. **The map page will show 181 (RC), so
   the plants page and the map will disagree until DOFAW decides.** The JSON uses 155.
2. **PEPP-filtered priority footprint: 98 vs 110 PUs (XP-06).** Table 4 Option 3 gives 98 PUs
   (line 1289); App 1 gives 110 (line 5174); RC gives 125. Ch 5e also says 101 PEPP plants have
   habitat data (line 1263), against 102 PEPP species elsewhere. Neither PEPP figure is used in Key
   numbers; App 1's 110 appears only in the details block.
3. **Implementation footprint PU counts.** Ch 6d (lines 2167-2174) describes the secondary (36 PEPP
   species in three or fewer PUs) and primary (14 single-PU species) implementation footprints
   without PU counts. The page takes 39 and 12 PUs (and 83 and 26 km²) from Table 4 Options 4-5
   (lines 1290-1291), which were built on the 155-PU set (XP-05). Table 4's species columns are
   internally inconsistent (XP-07) and were not reproduced.
4. **1,444 potential plant populations (line 2219).** This is the sum of recovery PUs per species
   (taxon-PU assignments), not populations (XP-07). Quoted as the plan states it in the details block.
5. **685 used for two things.** "Maintain 685 existing populations" (line 2042) and "PEPP ... tracks
   the location and status of 685 known sites" (line 2098). Also 685 + 891 = 1,576 while App 4
   desired recovery populations sum to 1,578 (XP-07). Both statements kept as the plan gives them.
6. **Listed plants: 175 vs 174.** Ch 4 Table 1 (line 993) gives 175; App 4 totals give 170
   endangered + 4 threatened = 174 (lines 7337-7338). Pages and JSON use 175.
7. **PTM plant subgroups sum to 196** (42 + 23 + 30 + 75 + 13 + 13; lines 2246-2275) against 197
   at-risk plants (XP-07). Subgroup sizes are shown as printed.
8. **Plant persistence wording.** Ch 6d says plants reach under 50 percent and "45 percent when
   adjusted for feasibility" (lines 2235-2240); Table 17 caption says 42-48 percent by subgroup
   (line 2328); Table 26 S25 values are 42-48. The pages use 42-48 percent in Key numbers and
   quote the 45 percent sentence in Status and trends.
9. **Table 27, Plant Group 4 (line ~3505)** shows two rank-3 cells (S3 and S13) and no rank 2.
   Table 26 values (S8 27, S13 26, S3 23) imply S13 should be rank 2. Table 27 per-subgroup ranks
   were not reproduced on the page.
10. **Tool name.** Ch 6d (line 2233) and App 5 section 2 (line 7428) say "Find My Microhabitat Tool";
    the App 5 introduction (lines 7350, 7354) says "Find My Habitat". The page keeps the Ch 6d wording.
    Whoever writes the tools page should pick one.

### Forest birds
11. **Population table vs text (XP-24).** Table 6 (line 1490s) gives kiwikiu 150 and ʻākohekohe
    1,768; the text (lines 1427-1440) gives "fewer than 150" and "between 1,200 and 2,000". The
    Key number uses the text ("fewer than 150"); the table is reproduced as printed with a comment.
12. **Second ʻākohekohe population destination.** Ch 6a says translocation "to another suitable
    habitat area not on Maui" (line 1525); App 2 S14 (p.A2-34, line 6416) translocates 50 pairs
    of ʻākohekohe **and ʻalauahio** to "other Hawaiian Islands" (XP-24). Both are quoted where
    they occur.
13. **Two "all actions" persistence values (XP-15).** Ch 6a says 71.6 percent "if all actions are
    successfully implemented" (lines 1589-1591); Table 8 caption says 59 percent "if all actions
    associated with ... S27 are implemented" (lines 1603-1604). Pages present 59 as S27 adjusted for
    feasibility (matches Table 26) and 71.6 as maximum feasibility (Figure 3).
14. **Figure 6 caption vs mapped priority footprint (XP-12).** The caption defines the priority
    area as downslope mosquito-control habitat; by visual reading the map shows the RC 28-PU
    current-range priority footprint. The page attributes the description to the plan ("The plan
    describes it as...") rather than stating it as fact.
15. **Recovery targets for ʻiʻiwi and Maui ʻalauahio equal current totals.** Table 7 (50,000 and
    99,000, lines 1555-1556) equals Table 6's current East Maui totals, but spread across three
    areas. Not an error in itself, but readers may ask whether the target implies a decline on East
    Maui. Question for DOFAW.
16. **S15 and gene drives.** App 2 Table 2 S15 (p.A2-35, lines 6436-6440) includes developing
    genetically modified mosquitoes "via gene drive or gmo", but the App 2 discussion
    (p.A2-17, lines 5753-5757) says gene drives were left out of the formal process. The forest
    bird details block describes S15 as "genetically modified mosquitoes" from Table 2. DOFAW
    may want to confirm the public wording.
17. **Delineation method (XP-25).** The plan says the Forest Bird Team used "existing literature,
    recovery plans, and professional expertise" (line 1563) and App 1 says "web-map review"
    (line 5120). The forest bird synthesis records a scripted GIS rule set plus expert calibration
    (V1-V3). The page mirrors the plan only.
18. **App 3 name:** *Paroreomyza montana newtoni* (App 3, line 6605) vs *Paroreomyza montana*
    (Ch 6a). Page uses the Ch 6a name.

### Seabirds
19. **ʻUaʻu total (XP-24).** Table 10 prints 6,101-6,750 (line 1698); the island values sum to
    6,101-6,250. Printed value used in Key numbers and the table, with a comment.
20. **"Roughly double" (line 1717)** vs a target of 18,000 pairs against about 6,100-6,750 today
    (about threefold). The page quotes the plan's wording.
21. **"3 current populations" (Table 9, lines 1686-1690)** vs breeding pairs on four islands in
    Table 10. Table 9's population column was not reproduced.
22. **Kahoʻolawe targets.** Table 11 gives 600 ʻaʻo and 300 ʻakēʻakē pairs on Kahoʻolawe; XP-24
    notes those two species have no footprint habitat there. Shown as printed.
23. **S27 persistence: 58 vs 59 (XP-15).** Table 12 caption (line 1768) says 58; Table 26 and App 2
    Table 1 say 59. Pages use 59 and note 58 in a comment.
24. **PU 6195 vs 6095 (XP-11).** The plan's list of 11 additional seabird action PUs (line 1748-1749)
    includes 6195; the manager list has 6095. Reproduced as printed in the details block. Fig 7's
    priority layer also does not match the RC 18-PU priority footprint (visual reading, XP-11).
25. **Scientific name.** Ch 6b uses *Oceanodroma castro*; App 3 uses *Hydrobates castro*. Page uses
    Ch 6b. Tables print "aʻo" without the leading ʻokina; the page uses ʻaʻo as in the Ch 6b text.
26. **Section numbering.** Ch 6b goes from ii to iv (no iii). Cosmetic.

### Waterbirds
27. **Table 15 note vs table (XP-24).** The note says ʻalae ʻula targets "can be spread across any
    island" (lines 1908-1909), but the table puts all 250 on Molokaʻi, and the text says reintroduce
    on Molokaʻi. Page follows the table and text.
28. **Nēnē priority (XP-13).** Ch 6c says a subset of wetlands "(and uplands for nēnē)" are
    management priorities (lines 1904-1905); Fig 8b shows no priority PUs by visual reading, and the RC
    waterbird priority (3 PUs at Kanahā and Kealia) has no nēnē. The page repeats the plan's wording.
    Table 13 gives nēnē 2 current populations; Table 15 targets 3 (two on East Maui, one on
    Molokaʻi); the master list has four.
29. **PTM covers four of five waterbirds (XP-16).** App 2 waterbird group omits ʻalae ʻula
    (p.A2-19, lines 5819-5825). Stated neutrally in the waterbird details block.
30. **Common name.** Ch 6c uses "Hawaiian moorhen"; App 3 uses "Hawaiian common gallinule". Page uses
    Ch 6c.

### Cross-group
31. **Combined priority 216 vs RC 237 (XP-04)** affects the map page, not these pages.
32. Table 26 (p.85) column headers label the current-actions column "C Only Current" and the
    no-action column "S1 No Actions"; App 2 Table 1 uses B (baseline) and C (counterfactual). Values
    agree; the pages use "no action" and "current actions only".

## Gaps (needed for the pages but not in the plan)
- **Recovery and priority footprint PU counts and areas for Forest birds, Seabirds and Waterbirds**
  are not stated anywhere in the plan text. JSON fields are null. RC values (tracker reconciliation
  table): Forest birds 160 / 28 PUs, Seabirds 226 / 18, Waterbirds 57 / 3. DOFAW to decide whether the
  group pages may quote RC values, labelled as the ACP footprint.
- **Hawaiian group names.** The plan gives none for the groups; `hawaiian_name` is null.
- **Plants by island.** Ch 6d gives no island breakdown of plant species, footprint PUs or targets.
- **Seabird monitoring.** Ch 6b lists no group-specific monitoring or research needs; the page uses
  recruitment surveys from App 2 S9/S10 and the burrow-count example from Ch 8 (p.106).
- **ʻIʻiwi common name** is not given in the plan; left blank.
- **Example plants.** Ch 6d names no individual species. Examples on the plants page come from
  App 3 (Hawaiian names) and App 4 (status, tier, known occupied PUs).
- **Who does what.** Partners are named only where the plan names them (Maui Forest Bird Recovery
  Project, PEPP, HPPRCC, Hawaii Wildlife Center, Hawaiian Electric).

## Messaging and orthography decisions
- Group names capitalized (Forest birds, Seabirds, Waterbirds, Plants). The plan heading "Terrestrial
  Plants" is rendered as "Plants". "Team" is used only for people (Forest Bird Team, Plant Team).
- "Adaptive Conservation Planner (Conservation Planner)" on first mention per page.
- Expert engagement is phrased as "DOFAW coordinated the taxon expert team" and "web-map review
  sessions". The plan's "Expert Data Platform" and "spreadsheet review" are kept as the plan states
  them (App 1).
- The term "expert elicitation" (App 2) was not used.
- **Plant Hawaiian names lack kahakō in App 3:** "Haha", "`Oha wai", "`Ahinahina", "Koki`o",
  "Pua `ala". Backtick ʻokina were corrected, but kahakō were not added (per the rule to keep the
  plan's orthography). Flag for Hawaiian-language review (likely hāhā, ʻōhā wai, ʻāhinahina, kokiʻo).

## Suggested images
- Forest birds: kiwikiu hero (alternate ʻākohekohe); plan Figure 5 (PDF p.43) emergency mosquito
  areas; Figure 6 (PDF p.44) recovery footprint; Figure 3 (PDF p.34) group persistence chart (could be
  redrawn as SVG from Table 26).
- Seabirds: ʻuaʻu at a nesting burrow (alternate ʻaʻo); a predator-proof fence photo; Figure 7 (PDF p.48).
- Waterbirds: nēnē hero (alternate ʻaeʻo in a managed wetland); Figure 8a (PDF p.53) and 8b (PDF p.54).
- Plants: pua ʻala or a PEPP outplanting/seed collection photo (alternate ʻahinahina); Figure 9a-d
  (PDF pp.60-61); Figure 4a-e (PDF p.37) narrowing alternatives; Figure 10 (PDF p.63) subgroup chart.
- The interactive map page could link from each group page with that group's layer pre-selected.

## Questions for DOFAW
1. Plant priority footprint: show 155 (plan body) or 181 (App 1, RC, ACP)? (XP-05)
2. May the bird group pages quote RC footprint PU counts (160/28, 226/18, 57/3)?
3. Destination of the second ʻākohekohe population, "not on Maui" (Ch 6a) or "other Hawaiian Islands"
   (App 2), and is Maui ʻalauahio also to be translocated?
4. Is the S15 gene drive / GMO mosquito wording acceptable on a public page?
5. Should the list of 11 additional seabird PUs (with the 6195/6095 question) appear publicly?
6. Kahakō for plant Hawaiian names in App 3.
7. "Hawaiian moorhen" vs "Hawaiian common gallinule" for ʻalae ʻula.
