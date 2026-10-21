# Notes: Questions & Answers (task `faq`)

Outputs: `content/data/faq.json` (55 Q&As in 10 categories, with internal `origin_notes`) and
`content/pages/faq.md` (same Q&As, no origin notes; answers flagged for DOFAW carry a
`<!-- status: needs_dofaw_input -->` comment on the heading). Both files were generated from one
script so they stay identical. If you edit one, mirror the change in the other.

Plan line numbers below refer to `IMPORTANT/MNLCP 9-30-2026 FINAL.txt`.

## 1. Questions found in the demo and outreach record

Paraphrased, attributed by meeting and role only. "Plan?" says whether the final plan supports an
answer (Y = yes, P = partly, N = no). The FAQ entry ID is in brackets.

### NPS demo, 2026-09-10 (`20260910_MNLCP update and demo` summary + raw transcript; park staff questions at 15:51, 58:05, 1:01:57, 1:04:50, 1:11:55, 1:20:12)
1. How integrated is USFWS with this, and is it a first step toward compliance for reintroducing a species to a new site? P [`critical-habitat`, `historic-range`]
2. Is there a process for adding a species that is not on the list yet, for example one newly elevated to threatened status? P [`add-species`]
3. Neighboring units can carry similar numbers of targets while the actions that help them (rat, weed, cat control) differ. Has the team considered which actions to prioritize for each species? Y [`site-actions`]
4. Is it up to the manager whether to prioritize a core contiguous area or an outlying, disjunct unit? Y [`planning-units`]
5. How do you account for benefits from working in adjacent areas with fewer targets, given that the landscape is connected? Any examples where this was done? Y [`planning-units`]
6. For predator control, terrain may make trapping inside the mapped square impractical, so control goes next door to protect a bird that does not live in that square. Y (general principle) [`planning-units`]
7. Implied by the demo close: how do we get logins, and is there a handbook? P [`acp-access`, `what-acp`]

### USFWS show-and-tell, 2026-09-03 (summary + AI meeting notes; no verbatim transcript exists)
8. How old are the occurrence records, and how are separate populations distinguished? Y [`data-reliability`]
9. How is sensitive occurrence data protected (user access controls)? N [`sensitive-data`]
10. Why was one planning unit selected over another, and how could that be justified in a designation record? Y [`how-chosen`]
11. Critical habitat must be occupied at listing and cannot consider ownership or fencing. How do the footprints relate? N [`critical-habitat`]
12. How are data-deficient species (interim targets, host-plant mapping for arthropods) handled? Y [`no-footprint`, `interim-full`]
13. Can staff get logins? Can they import their own occurrence records and export to GeoPackage or Excel? P [`acp-access`, `export-use`]
14. Can we have the published methods and the written plan to cite? N (resources) [`get-plan`]

### USFWS critical-habitat follow-up (reported in core team 2026-09-09, spatial team 2026-09-08)
15. Why weren't other suitable ("green") areas included? Should units be expanded, or a second unit added? Y [`why-not-all-habitat`]

### Core team and spatial team meetings, Jul-Oct 2026 (demo debriefs and tool reviews)
16. Who should get access to the ACP, how broadly is "manager" defined, and should there be a view-only guest mode? (core 2026-09-09) P [`acp-access`]
17. How will cross-island targets for multi-island species be coordinated when Oʻahu planning begins? (core 2026-09-02) N; not used beyond [`other-islands`]
18. A demo attendee asked whether there are ideas for future additions. (core 2026-09-30) Y [`other-tools`]
19. TNC is interested in the maps and biodiversity reserves for land acquisition. TPL, HILT, and the Maui County open space program were named as potential users. (core 2026-09-09, 2026-09-30) Y [`acquisition`]
20. Can I save several named configurations in the ACP? (DOFAW user, 2026-09-28) Not in FAQ: too technical. Candidate for the tools page or handbook.
21. What do "priority targets" and "known populations" mean in exports, and why don't the export numbers match the screen? (core 2026-09-02) Not in FAQ: a bug and a definitions issue. The handbook should define these fields.
22. A request to change the fire-risk footprint: when would it take effect? (2026-09-28) Y (general) [`update-cadence`]
23. A new record turned up just outside, or on the boundary of, a selected unit. Shift units or add one? (core 2026-09-09) Y [`planning-units`, `field-changes`]

### ACP demo participant notes (`misc_files/ACP_demo_participants.txt`; 31 dated demos, 2026-07-23 to 09-22)
24. A forestry manager noted that some silversword populations may serve better as recovery units (manager fine-tuning). Y [`field-changes`]
25. Watershed partnership demo: "Not clear how MKWP will lead on private lands." N [`private-landowners`]
26. Kauaʻi and Oʻahu branch managers asked for follow-up to develop next-generation applications for their islands. P [`other-islands`]
27. Pūlama Lānaʻi asked for edit access to begin editing the Lānaʻi content (core 2026-08-19). P [`acp-access`, `who-edits`]

### Hawaiʻi Conservation Conference symposium Q&A (`HCC_transcripts`)
28. Talk 1: How do you define essential habitat, and how does funding affect it? Y [`how-chosen`]
29. Talk 3: How do you keep track of the snails in kīpuka kāhuli, and which species can share one? P [`kipuka-kahuli`] (the answer about hard-to-tell-apart juveniles is not in the plan, so it was not used)
30. Talk 4: How did the expert-led seabird process differ (no algorithm run)? Y [`how-chosen`]
31. Talk 5: How did you take climate change into account? Y [`climate`]
32. Talk 7: What is the process for getting from planning to implementation? Y [`sequence`, `what-success-requires`]
33. Talk 7: How will recommendations be carried across land boundaries? P [`private-landowners`]
34. Talk 7: What is the plan for data management and data sharing? N [`sensitive-data`]
35. Talk 7: What will plants need (which actions)? Y [`what-actions`]
36. Talk 7 (presenter): "If you had a pot of money, where would you put the next fence? It's a common question that we get." Y [`fencing`]
37. Talk 2 and Talk 6: "time for one question" but no question was transcribed.

### Participant feedback synthesis and lessons-learned v3.0 (converted copy: `_source_extracts/lessons_learned_v3.txt`)
38. Is implementation funded and staffed, and is it realistic? P [`what-success-requires`]
39. Were field practitioners, landowners, Native Hawaiian organizations, and communities involved? N [`community`, `private-landowners`]
40. Not enough attention to new management technologies. Y [`new-tools`]

### FM_revisions notes ("Taking the tool for a spin", "Footprint manager applications", notes.txt)
41. If a species shows only a few planning units, is it truly that rare, or is that a data limitation? Y [`no-footprint`]
42. How do I change or add or remove species names in a living plan? P [`add-species`]
43. Can a reserve manager look only at their own reserve? Use in management plans, EAs, ungulate control plans, land acquisition. Y [`export-use`, `acquisition`]
44. Data sensitivity: occurrences for admin users only, and NPS data sharing. N [`sensitive-data`]

Searched without further finds: the registry (`--text demo`, `FAQ`, `demo question`). The "existing
demo question list" Lucas mentioned on 2026-09-02 was not found in the repository. If it exists,
it should be checked against this list.

## 2. Answers marked `needs_dofaw_input` (12)

Each has a draft answer. Plan-supported sentences are cited; the uncited sentences come from the
demo record and need DOFAW to confirm them or cut them. `[TBD: …]` placeholders must be filled or
removed before launch.

| ID | Question | What DOFAW needs to confirm |
|---|---|---|
| `add-species` | Adding a species not on the list | The workflow: enter targets, assign PUs, colleague review, rarely rerun the prioritization. It comes from the NPS demo and core team 2026-09-02, not the plan. The bug that crashed "new taxon" (NPS demo) may matter. |
| `cost` | Cost of carrying out the plan | Whether to publish dollar figures at all. App 2 is internally inconsistent (see §3). Figures used: ~$55M/yr average (A2-11), ~$67M upfront (A2-1, A2-16), ~$10M/yr savings (A2-11). |
| `acp-access` | Who can use the ACP, how to get access | Access policy, contact address, eligibility (managers, agencies, NGOs, land trusts, universities?), and whether a view-only guest mode will exist. The plan says only "not a public web map… authorized users" (A5-1). |
| `update-cadence` | How often footprints and plan are updated | The annual review cycle is described in demos but no process is agreed (tracker XP-19; Chad 2026-10-01). The "DOFAW expects to review… once a year" sentence is a draft. |
| `sensitive-data` | Does the ACP reveal rare species locations | Plan silent. Draft says occurrence records are admin-only and never default (core team 2026-09-02, 2026-09-09, spatial team 2026-08-12) and that partner data stay under data-sharing agreements (FM_revisions notes). Note that occupancy is visible at the PU level to map viewers (spatial team 2026-09-21). |
| `regulatory` | Is the MNLCP a regulation | "No new rules, permits, or land-use restrictions" is not stated in the plan. The plan says only decision support, flexible guidance, not prescriptive mandates (pp.8-9, 121). |
| `my-land` | Footprint on my land | "Places no requirement on a landowner" and "only through voluntary agreement" are draft statements. Needs a landowner contact. |
| `private-landowners` | How landowners can take part | Content is plan-supported. Needs the contact route, and a check that naming eastern Molokaʻi, above Makawao, and Kahikinui is acceptable on a public page (they are named in the plan Exec Summary p.ix). |
| `critical-habitat` | Relation to federal critical habitat and permitting | The plan never mentions critical habitat. Wording should be cleared with USFWS. The draft avoids saying footprints "should be" critical habitat (a demo opinion) and avoids the USFWS regulatory constraints. |
| `share-info` | How to share new information or get involved | Contact address and preferred format for observations (iNaturalist? direct email? the PEPP database?). |
| `community` | Community and Native Hawaiian engagement | The plan does not describe community or Native Hawaiian engagement. DOFAW should supply this or drop the question. Participant feedback flagged it as a gap. |
| `get-plan` | Where to get the plan and maps | Whether the PDF is public. Core team 2026-09-23: make it public-ready, with the USGS appendix constraint. Also which map files (KMZ, GeoJSON) can be downloaded. |

## 3. Discrepancies and number choices

- **Plant priority footprint 155 vs 181 PUs** (`narrow-footprint`). Text uses the plan body's Table 4 figures (317 / 155 / 98 / 39 / 12 PUs; plan lines 1285-1289, p.27). The plan's App 1 (line 5149, A1-6) and the release candidate give 181 PUs, and the App 1 PEPP filter gives 110 PUs (line 5174). The RC PEPP view is 125 PUs. Tracker XP-05, XP-06, XP-07. Table 4's species columns are also internally inconsistent (e.g., Option 4: 36 target species but 68 PEPP and 52 non-PEPP), so I quoted only PU counts.
- **Combined footprint species counts.** The plan gives 299 (Exec Summary p.vi) vs 250 (Ch6i line 3244, p.81) species in the full footprint, and 267 in the priority footprint, which exceeds 250. Tracker XP-01, XP-04. The FAQ quotes only PU and area figures (492 PUs, 1,050 km²; 216 PUs, 457 km²). Combined priority 216 PUs (plan) vs 237 PUs (RC) remains open (XP-04).
- **66 percent.** The plan calls this "conservation-oriented land" (p.vi, line 242; p.81, line 3255: 65.7 percent). Per tracker XP-26 (resolved), this figure is the biodiversity-reserve share, so the FAQ says "within biodiversity reserves" to follow the messaging rules.
- **Snails facing imminent extinction: 49 vs 47.** Plan Table 1 (p.19) and the Exec Summary say all 49 snails face imminent extinction. App 6's total row (line 7546, A6-2) says 47. The FAQ uses 49.
- **App 2 costs inconsistent.** The abstract (line 5307, A2-1) gives an "average annual cost of $26M". The body gives ~$55M/yr to secure all species (lines 5610-5618, A2-11) and ~$53M/yr to maintain fences and facilities (line 5713, A2-16). App 2 also says "374 species" and "over 300" (line 5297) where the plan says 442, and its title uses "optimally allocate" (line 5284). The FAQ uses $55M, $67M, and $10M only. The A2-16 page reference was derived from page-marker positions inside a table-heavy section; please verify against the PDF.
- **Tool name in App 5.** The intro says "Find My Habitat" (lines 7350, 7354), while Section 2 says "Find My Microhabitat" (line 7429). The FAQ uses "Find My Microhabitat". Lessons-learned v3.0 (2026-10-19) lists "Add Find My Habitat" to the Conservation Planner as unfinished, though App 5 says it is available. It is probably a standalone tool not yet integrated. Confirm.
- **ACP access URL.** App 5 (line 7422) gives a URL containing the tool's former name (tracker XP-20). It is not used in the FAQ. The tools page should decide how to link.
- **Arthropod survey map in the ACP.** The plan (p.18, A1-8) says the Conservation Planner has a separate map of area-survey PUs. Per tracker XP-09 it is not in the ACP. The FAQ avoids claiming it.
- **Retired term.** App 5 lists "modify preventing-extinction status" as an edit type (tracker XP-22). The FAQ omits that clause.

## 4. Sensitive topics: DOFAW should confirm the wording

1. **Private land and footprints** (`my-land`, `private-landowners`, `why-conservation-lands`, `acquisition`). The public map will show footprint PUs on private land. The FAQ says footprints are planning maps with no landowner requirement, but that is a draft. The demo record goes further than the plan: watershed-partnership private lands were "deliberately excluded" from recovery targeting (NPS demo 2026-09-10). The plan instead says it focuses on lands "covered by conservation agreements with private landowners" (p.1), and Ch7 treats Watershed Partnerships as conservation-oriented management potential (p.92-93). The FAQ follows the plan. DOFAW should settle which framing is right. The `why-conservation-lands` sentence "Some species can only be recovered on other lands" paraphrases the demo explanation that units outside reserves mean the algorithm had no other choice. Please confirm.
2. **Land acquisition** (`acquisition`). The plan names areas for landowner engagement. The demo named a specific single-landowner block as "the single most important acquisition target"; that is not used and should not appear publicly.
3. **Regulatory status and critical habitat** (`regulatory`, `critical-habitat`). Clear these with USFWS. The demos included DOFAW opinions on what critical habitat "should look like" and on USFWS constraints; none of that is used.
4. **Sensitive species data** (`sensitive-data`). Confirm that what the answer promises matches the live ACP permissions.
5. **Costs** (`cost`). Dollar figures on a public page will be quoted. Given the App 2 inconsistency, DOFAW may prefer to link to App 2 without numbers.
6. **Cultural values** (`cultural-values`, `community`). Plan-only wording; needs the Hawaiian-language and cultural-framing review that PLAN.md lists as out of scope.
7. **Editing rules** (`who-edits`). The demo said that moving a target onto a partner's land, or relocating it because habitat was lost, needs the affected partner's agreement before approval. That would reassure partners, but it is not in the plan. DOFAW could add it.

## 5. Gaps (useful answers the plan cannot support)

- ACP features shown in demos but not described in the plan: importing user layers and shapefiles; preloaded land ownership and fence layers; area queries by lasso or ownership; the editor suggesting the next-best alternative units; the "all possible targets" view; the notes function's history and resolution behavior. The tools page or Managers' Handbook should document these before the FAQ refers to them.
- Training: recorded demos and instructional videos are planned (core team 2026-09-09, 2026-09-23) but not in the plan.
- Oʻahu and other islands: the planning effort beginning on Oʻahu is not in the plan. The FAQ says only "model for other islands".
- SWAP: integration of the MNLCP into the State Wildlife Action Plan (Chapter 8) was discussed (core team 2026-09-02, 2026-09-09) but is not in the plan text.
- Peer-reviewed methods papers: the FAQ does not cite them. The resources page should list the Conservation Biology paper (plan Literature Cited).

## 6. Link targets used

`plan.html`, `partners.html`, `approach.html`, `species.html`, `groups.html`,
`footprints.html`, `actions.html`,
`tools.html`, `ecosystems.html`, `monitoring.html`, `resources.html`. I used `footprints.html` for the
footprints page per PLAN.md §2, although the task brief mentioned `footprints.html`. Align this at
build time.

## 7. Suggested images

- An ACP screenshot of a planning-unit click showing the species list (for `what-acp` and `site-actions`), from the ACP screenshot set.
- Plan Figure 4 a-e (PDF p.28), the plant footprint narrowed step by step, for `narrow-footprint`.
- Plan Figure 19 (PDF p.82), the combined recovery, priority, and initial implementation footprints, for `footprint-size`.
