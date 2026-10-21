#!/usr/bin/env python3
"""Build content/data/faq.json and content/pages/faq.md for the MNLCP website (task: faq)."""
import json, re, sys
from pathlib import Path

ROOT = Path("/hdd/projects/maui_nui_scp/MNLCP_website/content")

SOURCE = ("MNLCP final plan, DOFAW version 2026-09-29 (MNLCP 9-30-2026 FINAL.txt): Executive Summary "
          "(pp. iv-ix), Ch 1-5 (pp. 1-30), Ch 6e and 6i (pp. 57-59, 81-84), Ch 7e-j (pp. 92-100), Ch 8a and 8f "
          "(pp. 101-103, 112-113), Terms and Definitions (pp. 120-123), App 1 (A1-1 to A1-8), App 2 (A2-1, A2-11, "
          "A2-16, A2-29, A2-30), App 5 (A5-1 to A5-4). Questions drawn from the ACP demonstration and outreach "
          "record (NPS demo 2026-09-10, USFWS show-and-tell 2026-09-03, core team meetings Jul-Oct 2026, 2025 HCC "
          "symposium Q&A, ACP demo participant notes, participant feedback synthesis, lessons-learned v3.0, "
          "FM_revisions notes); see content/notes/faq.md.")

def Q(id, q, a, audience, origin, origin_notes, plan_sources, status="ready"):
    return dict(id=id, q=q, a=a.strip(), audience=audience, origin=origin,
                origin_notes=origin_notes, plan_sources=plan_sources, status=status)

categories = []

# ---------------------------------------------------------------- basics
categories.append(dict(id="basics", title="The plan basics",
    description="What the Maui Nui Landscape Conservation Plan is, who made it, and why.",
    questions=[
Q("what-is-mnlcp", "What is the Maui Nui Landscape Conservation Plan?", """
The Maui Nui Landscape Conservation Plan (MNLCP) is the first islands-wide, landscape-scale roadmap showing where conservation actions can most effectively prevent extinctions, recover at-risk species, and restore native ecosystems across Maui, Molokaʻi, Lānaʻi, and Kahoʻolawe. <!-- src: plan p.iv --> It is a plan of the Hawaiʻi Division of Forestry and Wildlife (DOFAW). It covers native land and freshwater species and ecosystems, and for 442 at-risk species <!-- src: plan p.iv --> it answers three linked questions: where to work, what to do, and when to do it. <!-- src: plan p.v, p.29 --> See [About the Plan](plan.html).
""", "public", "standard", "Standard opener. Every demo began with this framing (NPS demo 2026-09-10; USFWS show-and-tell 2026-09-03; HCC Talk 1).",
  ["Exec Summary p.iv-v", "Ch 1 p.1", "Ch 5e p.29"]),

Q("who-developed", "Who developed the plan?", """
DOFAW Maui led the plan. Partners included USGS, USFWS, the University of Hawaiʻi at Mānoa and Hilo, the Bishop Museum, and other land managers and scientists. <!-- src: plan p.v --> More than 100 land managers, scientists, and species experts contributed. <!-- src: plan p.iv --> DOFAW coordinated the taxon expert teams and led the implementation and core teams. Spatial prioritization was led by USGS, action prioritization by UH Mānoa, and ecosystem prioritization by UH Hilo. <!-- src: plan pp.11-15 --> See [Partners & Teams](partners.html).
""", "public", "standard", "Standard. Demo audiences also asked how closely USFWS was involved (NPS demo 2026-09-10).",
  ["Exec Summary p.iv-v", "Ch 3 pp.11-15"]),

Q("why-needed", "Why is the plan needed?", """
Hawaiʻi has less than 0.2 percent of the nation's land area but 29 percent of its imperiled species, and more than 60 percent of its native ecosystems have been destroyed or badly degraded. <!-- src: plan p.iv --> Many good plans already exist, including recovery plans, the State Wildlife Action Plan, and site plans. But they are not connected at the landscape or management level, so managers have to reconcile dozens of documents built on different assumptions and scales. <!-- src: plan p.iv, p.3 --> The real question is where each species should be recovered and which actions will do the most good, so that the needs of all 442 species are met as efficiently as possible. <!-- src: plan p.iv -->
""", "public", "standard", "Standard. Scott's demo framing on why species-by-species recovery plans cannot be carried out one at a time (NPS demo 2026-09-10; USFWS 2026-09-03).",
  ["Exec Summary p.iv", "Ch 1a pp.2-4"]),

Q("goals-timeframe", "What are the plan's goals, and how long will it run?", """
The plan has three linked goals <!-- src: plan p.v -->:

1. Prevent the extinction of the most imperiled native plants and animals.
2. Recover all at-risk species to healthy, self-sustaining population levels.
3. Protect and restore native ecosystems so they provide habitat for all Maui Nui biodiversity and sustain clean water, cultural values, and local economies.

It is designed to be carried out over 20 years. <!-- src: plan p.v --> Because it is not possible to do everything, everywhere, at once, it starts with emergency actions for species facing imminent extinction and then works through recovery actions in sequence. <!-- src: plan p.viii, p.29 -->
""", "public", "standard", "Standard.",
  ["Exec Summary p.v, p.viii", "Ch 2a p.7", "Ch 5e p.29"]),

Q("how-different", "How is this different from earlier conservation plans?", """
Most earlier plans deal with one species or one site at a time. The MNLCP brings the recovery needs of all at-risk species together into one map-based plan. That plan identifies the set of places where actions do the most good for all species combined. <!-- src: plan p.4 --> It links three analyses (where to work, what to do, and ecosystem priorities) into one decision-support system. <!-- src: plan p.v --> It is also delivered as a living system that can be updated, not a one-time, static document. <!-- src: plan p.v, p.6 --> It draws on existing work: recovery targets come from existing recovery plans with added expert input, and the at-risk list draws on endangered species lists and the State Wildlife Action Plan. <!-- src: plan p.7, p.16 -->
""", "both", "both", "Demo framing (NPS demo 2026-09-10: contrast with traditional recovery plans that vary in form and exist for fewer than half the species; HCC Talk 1). Also a standard question.",
  ["Exec Summary p.v", "Ch 1a pp.3-4", "Ch 1c p.6", "Ch 2b p.7", "Ch 4a p.16"]),

Q("approach", "What planning approach does the plan use?", """
The plan uses an approach called Integrated Multi-Scale Conservation Planning (IMCP). It links three parts <!-- src: plan pp.8-10 -->:

- **Spatial prioritization** (where to work), done through the Transparent, Flexible, Expert-engaged Systematic Conservation Planning (TFE-SCP) process.
- **Action prioritization** (what to do), done through a modified Priority Threat Management (PTM) process.
- **Ecosystem prioritization**, which looks at the wider landscape.

TFE-SCP is a comprehensive planning process. It generates many possible footprints and lets experts and managers weigh the trade-offs among them. The result does not come from the algorithm alone. <!-- src: plan pp.12-13, A1-1, A1-3 --> See [The Approach](approach.html).
""", "both", "standard", "Standard. HCC Talk 2 and the USFWS show-and-tell covered how the algorithm and expert review fit together.",
  ["Ch 2d-e pp.8-10", "Ch 3c pp.12-13", "App 1 A1-1, A1-3"]),

Q("experts", "How were species experts and managers involved?", """
DOFAW coordinated taxon expert teams, and experts took part in collaborative review sessions throughout the process. <!-- src: plan p.11, A1-1 --> The teams helped decide which species to include and set recovery targets. They also identified known populations and suitable habitat, chose the most important actions, and identified species facing imminent extinction. <!-- src: plan pp.11-12 --> Experts reviewed and refined the draft footprints species by species and proposed changes with documented reasons. <!-- src: plan A1-2 --> For action prioritization, about 100 land managers and scientists shared their professional judgment in open-ended workshops. <!-- src: plan p.13 -->
""", "both", "both", "Standard; demos repeatedly stressed that algorithm outputs were reviewed and overridden by experts (USFWS 2026-09-03; NPS 2026-09-10). PRA-safe wording used.",
  ["Ch 3b pp.11-12", "Ch 3d p.13", "App 1 A1-1 to A1-2"]),
]))

# ---------------------------------------------------------------- species
categories.append(dict(id="species", title="At-risk species",
    description="Which species the plan covers and how they were chosen.",
    questions=[
Q("how-many-at-risk", "How many species are at risk, and what does \"at risk\" mean?", """
The plan covers 442 native species <!-- src: plan p.iv, p.16 -->: birds, plants, invertebrates, and a bat. Experts consider each one likely to go extinct within the next 20 years without significant management. <!-- src: plan p.16 --> The main reasons are very low numbers, steep declines, climate change, newly arrived invasive species, and habitat loss. <!-- src: plan p.16 --> Browse them in the [At-Risk Species](species.html) explorer.
""", "public", "standard", "Standard.",
  ["Exec Summary p.iv-v", "Ch 4a p.16", "Terms p.120"]),

Q("why-unlisted", "Why does the plan include species that are not on endangered species lists?", """
Only 202 of the 442 species are listed under state or federal endangered species laws. <!-- src: plan p.v --> Species experts identified the other 240 because of very small or declining populations, restricted ranges, or vulnerability to climate change. <!-- src: plan p.v --> These unlisted species are treated the same way as listed ones: every species gets recommended actions, and where the data allow, a recovery footprint. <!-- src: plan p.20, p.26 -->
""", "public", "both", "Standard; also a core demo talking point (NPS demo 2026-09-10: fewer than half of species federally listed; USFWS 2026-09-03).",
  ["Exec Summary p.v", "Ch 4a p.16", "Ch 5a p.20", "Ch 5e p.26"]),

Q("imminent-extinction", "What does \"facing imminent extinction\" mean, and what are PEPP species?", """
In all, 163 of the 442 species could be lost within five years without immediate emergency action. <!-- src: plan p.iv, p.16 --> These include 102 plants, all 49 at-risk Terrestrial snails, 9 Terrestrial arthropods, 2 Forest birds, and 1 Aquatic invertebrate. <!-- src: plan p.19, Table 1 --> Emergency actions put speed and effectiveness first. Examples are seed banking, captive propagation, very small predator-proof exclosures, and close protection of the last wild populations. <!-- src: plan p.viii, p.16 -->

"PEPP species" are plants covered by Hawaiʻi's Plant Extinction Prevention Program, which works with native plants that have fewer than 50 individuals left in the wild. All 102 plants facing imminent extinction are already part of PEPP. <!-- src: plan p.48 -->
""", "both", "both", "Standard; PEPP filter and PEP targets featured in every demo (NPS 2026-09-10; USFWS 2026-09-03).",
  ["Exec Summary p.viii", "Ch 4b p.16", "Ch 4 Table 1 p.19", "Ch 6d p.48"]),

Q("groups-covered", "Which groups of species does the plan cover?", """
The plan covers eight taxonomic groups: Plants (197 species), Terrestrial arthropods (172), Terrestrial snails (49), Aquatic invertebrates (11), Waterbirds (5), Forest birds (4), Seabirds (3), and the Hawaiian hoary bat, or ʻōpeʻapeʻa (1). <!-- src: plan p.19, Table 1 --> Seven groups had their own taxon expert team. The bat, Hawaiʻi's only native land mammal, is the eighth group and did not have a dedicated team. <!-- src: plan p.11 --> For the bat, the top actions are reducing deaths at wind-energy facilities, protecting forests and wetlands, and developing population monitoring. <!-- src: plan p.vi, Table 1 --> See [Taxonomic Groups](groups.html).
""", "public", "standard", "Standard.",
  ["Ch 3b p.11", "Ch 4 Table 1 p.19", "Exec Summary Table 1 p.vi"]),

Q("no-footprint", "Why don't some species have a recovery footprint?", """
In all, 143 at-risk species still lack the data needed to map recovery habitat, and most of them are Terrestrial arthropods. <!-- src: plan p.vii --> Many arthropods have fewer than five occurrence records. <!-- src: plan p.18 --> For these species the plan sets up surveys instead. Area Surveys are based on where the species' host plants grow. Species-specific Surveys are for species where even that information is missing. <!-- src: plan p.18 --> As surveys find populations and habitat, species can be added to the recovery footprints. <!-- src: plan p.18, p.81 --> Terrestrial snails are a separate case. They have exclosure sites rather than recovery habitat, because their predators cannot yet be controlled across whole landscapes. <!-- src: plan p.21, p.81 -->
""", "both", "demo", "Data-deficient contrast case shown in the NPS demo (2026-09-10: PEP target with no habitat model and 9 of 10 units); USFWS asked about interim arthropod planning (Hylaeus assimulans, 2026-09-03). FM_revisions 'Taking the tool for a spin': is a narrow footprint real or a data limitation?",
  ["Exec Summary p.vii", "Ch 4c pp.18-19", "Ch 5c p.21", "Ch 6i p.81"]),

Q("interim-full", "What is the difference between \"interim\" and \"full\" recovery goals?", """
**Full recovery goals** were set for species with good data on habitat, threats, and effective actions. Reaching them is expected to mean the species is no longer at risk. Many of these goals come from federal recovery plans or from the Hawaiʻi and Pacific Plant Recovery Coordinating Committee. <!-- src: plan p.18 -->

**Interim recovery goals** were set where data are adequate but known locations are few, habitat restoration will take a long time, or key threats cannot yet be controlled. Interim goals create viable populations but are not enough to secure the species for the long term. <!-- src: plan pp.17-18 -->

Both kinds of goal come with recovery footprints. Of the 442 species, 211 have full goals and 88 have interim goals. <!-- src: plan p.19, Table 1 -->
""", "both", "demo", "USFWS show-and-tell (2026-09-03): interim targets for arthropods; core team 2026-09-09 noted USFWS had interim-target species.",
  ["Ch 4c pp.17-18", "Ch 4 Table 1 p.19"]),

Q("add-species", "What happens when a species not on the list becomes at risk, for example when it is newly listed or rediscovered?", """
The plan is built to take in new species and new information. Species that lack data are meant to be added to the plan as information becomes available. <!-- src: plan p.18 --> The Adaptive Conservation Planner lets authorized users propose new target locations for review and approval. <!-- src: plan A5-1 --> To add a new species, users enter its recovery targets and assign planning units, and colleagues then review the change. A newly found species known from one site might start with a single planning unit while the rest of its planning is worked out. The full multi-species prioritization would rarely be rerun, because management investment builds up over time and the overall layout should stay stable.
""", "partner", "demo", "Asked by NPS staff (2026-09-10): process for adding a species elevated to threatened status. Answer in demo (Scott, Lucas): add species, set targets, assign units through the editor, rarely rerun prioritization; core team 2026-09-02 discussed single-location new species. Plan supports only the general principle.",
  ["Ch 4c p.18", "App 5 A5-1"], "needs_dofaw_input"),
]))

# ---------------------------------------------------------------- where
categories.append(dict(id="where", title="Where: conservation footprints and planning units",
    description="How the plan maps where to work.",
    questions=[
Q("what-footprint", "What is a conservation footprint?", """
A conservation footprint is a map of the planning units chosen for species recovery. The plan uses footprints that nest inside each other <!-- src: plan p.27, A1-4 -->:

- **Recovery footprints** contain the existing or restorable habitat needed to reach recovery goals.
- **Priority footprints** are subsets of the recovery footprint. They mark the most important areas, where goals for both preventing extinction and recovery can be advanced.
- **Initial implementation footprints** suggest where to start.

For Terrestrial snails, the footprint is a network of predator-proof exclosure sites designed to prevent extinction. <!-- src: plan A1-6 --> Explore them on the [Conservation Footprints map](map.html).
""", "public", "standard", "Standard; core concept in every demo.",
  ["Ch 5c p.21", "Ch 5e pp.26-27", "App 1 A1-4, A1-6"]),

Q("footprint-size", "How big is the combined footprint, and where is it?", """
Across all groups, the recovery footprint covers 492 planning units, about 1,050 km². <!-- src: plan p.vi, p.81 --> The priority footprint narrows this to 216 planning units (457 km²), about 43 percent of the full footprint. <!-- src: plan p.vi, p.81 --> The footprints span all four islands, centered on upland Haleakalā, West Maui, East Molokaʻi, and Lānaʻihale. <!-- src: plan p.vi-vii, p.81 --> About 66 percent lies within biodiversity reserves, and about half already has some ungulate fencing. <!-- src: plan p.vi, p.81 -->
""", "public", "standard", "Standard. The 66 percent and 50 percent figures were confirmed for the plan in the 2026-09-28 Loyal and Chad check-in.",
  ["Exec Summary p.vi-vii", "Ch 6i p.81"]),

Q("planning-units", "What is a planning unit, and do its lines limit where managers can work?", """
A planning unit (PU) is the basic map unit of the plan. Maui Nui was divided into 1,400 planning units of about 2 km² each, drawn along watersheds, natural barriers, and elevation bands. Each is sized to support one population of an at-risk species. <!-- src: plan p.13, p.122 -->

Planning units are units of analysis, not property or management boundaries. The plan maps habitat and actions at the planning-unit level and leaves exact siting, such as where to outplant or fence, to field teams. <!-- src: plan p.29, p.122 --> Weed control, fencing, or predator control may well need to cross a unit's edge. When managers know something the maps missed, such as a better access route, they can feed it back into the footprints through the Adaptive Conservation Planner. <!-- src: plan p.30, A5-1 -->
""", "both", "both", "NPS demo (2026-09-10): two questions on adjacent and disjunct units and on placing predator control next to a unit; Lucas and Peter explained PUs are units of analysis. Core team 2026-09-09: an occurrence on a PU boundary.",
  ["Ch 3c p.13", "Ch 5f pp.29-30", "Terms p.122", "App 5 A5-1"]),

Q("how-chosen", "How were the footprint areas chosen?", """
Each species was given a recovery target: how many populations it needs and how they should be spread across islands and mountains. Targets came from existing recovery plans with added expert input. <!-- src: plan p.7 -->

For Plants, Terrestrial arthropods, and Terrestrial snails, a computer program (OptimTFE) generated many possible footprints that each met every species' targets. Experts and managers compared them on footprint area, habitat quality, habitat suitability, biodiversity reserves, ungulate management, accessibility, fire risk, climate resilience, and overlap with other groups. <!-- src: plan A1-3 to A1-4 --> Experts then fine-tuned the chosen footprint species by species. <!-- src: plan A1-2 --> For Forest birds, Seabirds, Waterbirds, and Aquatic invertebrates, specialists drew the areas directly through repeated map reviews. <!-- src: plan p.12, A1-2 -->
""", "both", "demo", "USFWS show-and-tell (2026-09-03): how to justify selecting one unit over another; HCC Talk 1 audience: how is essential habitat defined? HCC Talk 4 audience: how did the expert-led seabird process differ (no algorithm run)?",
  ["Ch 2b p.7", "Ch 3c pp.12-13", "App 1 A1-1 to A1-4"]),

Q("why-not-all-habitat", "Why isn't all suitable habitat included in the footprint?", """
A recovery footprint is built to meet each species' recovery targets, meaning the number and spread of populations it needs. It does not try to include every place a species could live. The goal is a set of planning units that together meet the targets of all species <!-- src: plan p.4 -->, and smaller footprints let managers concentrate their resources without giving up habitat quality or access. <!-- src: plan A1-3 -->

Habitat outside the footprints still matters. The ecosystem prioritization identifies the remaining good-quality native ecosystems across the wider landscape and the chances to protect and restore them, which also gives recovering species room to expand. <!-- src: plan p.viii, p.14 --> Protecting existing high-quality habitat is generally the top ecosystem priority. <!-- src: plan p.97 -->
""", "both", "demo", "USFWS (core team report 2026-09-09): why weren't other suitable ('green') areas included, and should areas be expanded? Loyal recalled early concerns that the process 'shrank' areas and that adjacent forest reserve lands were not being abandoned.",
  ["Ch 1a p.4", "App 1 A1-3", "Exec Summary p.viii", "Ch 3e p.14", "Ch 7h p.97"]),

Q("data-reliability", "How reliable are the species location data behind the footprints?", """
Taxon experts checked all occurrence data in collaborative review sessions and flagged errors, outdated records, and naming problems. <!-- src: plan A1-2 --> For Plants, mapped populations were used where available, and checked occurrence records otherwise. <!-- src: plan A1-2 --> Every footprint keeps species-level detail, including whether each choice rests on occurrence records or on model predictions <!-- src: plan A1-4 -->, and the Adaptive Conservation Planner shows this for each planning unit. <!-- src: plan A5-1 --> Data are still sparse for many Terrestrial snails and Terrestrial arthropods, so those footprints should be updated as surveys find more populations. <!-- src: plan A1-2, A1-7 -->
""", "partner", "demo", "USFWS show-and-tell (2026-09-03): vintage of occurrence records and how separate populations are distinguished.",
  ["App 1 A1-2, A1-4, A1-7", "App 5 A5-1"]),

Q("historic-range", "Will the plan move species to places where they never lived?", """
Recovery targets are placed within each species' historic range on Maui Nui. The rules for choosing footprints required spreading populations across the historic range. Snail exclosure targets sit within each species' historical range, and arthropod targets are spread across each species' historic range. <!-- src: plan A1-3, A1-7, A1-8 --> Returning species to places where they once lived is a normal recovery step and usually comes after fencing, ungulate removal, and weed control. <!-- src: plan p.26 --> The snail exclosures, for example, may later serve as bases for returning snails to known historic sites. <!-- src: plan pp.57-58 -->
""", "both", "demo", "NPS demo (2026-09-10): could this be a first step toward compliance for reintroducing a species to a new site? Scott: planning does not place species outside their natural range, but reintroduction where a species once occurred is central.",
  ["App 1 A1-3, A1-7, A1-8", "Ch 5d p.26", "Ch 6e pp.57-58"]),

Q("why-conservation-lands", "Why does the plan favor lands already managed for conservation?", """
Recovery needs long-term investment: fences, field crews, rodent control, and exclosures. So the plan focuses actions, when possible, on lands already managed or set aside for conservation or covered by conservation agreements with private landowners. <!-- src: plan p.1 --> One of the criteria for choosing footprints was overlap with **biodiversity reserves**: lands with a lasting conservation commitment, mainly the Forest Reserve System, where management infrastructure already exists. <!-- src: plan A1-3, A1-4 --> About 66 percent of the combined footprint falls within them. <!-- src: plan p.vi, p.81 --> Some species can only be recovered on other lands, so the plan also helps identify lands that should be managed under long-term protection. <!-- src: plan p.5 -->
""", "both", "demo", "NPS demo (2026-09-10) land-acquisition segment and USFWS (2026-09-03) land-ownership discussion: concentrate recovery on lands with legally binding commitments and avoid voluntary or private lands unless a species requires them. The demo statement that watershed-partnership private lands were deliberately excluded is NOT in the plan and is not used.",
  ["Ch 1 p.1", "Ch 1b p.5", "App 1 A1-3 to A1-4", "Ch 6i p.81"]),
]))

# ---------------------------------------------------------------- actions
categories.append(dict(id="actions", title="What: conservation actions and costs",
    description="Which actions the plan recommends, in what order, and what they may cost.",
    questions=[
Q("what-actions", "What conservation actions does the plan recommend?", """
The action prioritization team compared the expected benefit, feasibility, and cost of 27 strategies (17 single-focus strategies and 10 combinations) for 17 species groups. <!-- src: plan p.vii --> The key results:

- **No single strategy is enough.** Two combinations, S25 (focused on plants and invertebrates) and S27 (focused on birds and the bat), come closest to meeting every group's needs when done together. Between them they use all 17 single actions. <!-- src: plan p.vii, p.23 -->
- **Groundwork pays off.** Ungulate fencing and removal, weed control, predator control, and wetland management help many species at once. <!-- src: plan p.vii -->
- The plan measures success as persistence: the chance that a species group keeps viable, self-sustaining populations over 20 years. The target is at least 50 percent. <!-- src: plan p.vii, p.23 --> Plants remain the hardest group to secure. <!-- src: plan p.vii -->

See [Priority Actions](actions.html).
""", "public", "standard", "Standard. HCC Talk 7 audience asked what plants need (Peter: nearly all actions, including fencing, weed control, propagation, hand pollination).",
  ["Exec Summary p.vii", "Ch 5d pp.22-25", "Terms p.121"]),

Q("new-tools", "Why are \"new tools\" such a big part of the plan?", """
Some of the most serious threats cannot yet be controlled across whole landscapes. Future tools for rare plant and invertebrate conservation (strategy S13) ranked among the top three actions for 13 of the 17 species groups. <!-- src: plan p.vii --> Forest birds depend on new ways to control mosquito-borne avian malaria, and Terrestrial snails depend on controlling the rosy wolfsnail across whole landscapes. <!-- src: plan p.vii --> The plan calls for investment in new tools against mosquitoes, predatory snails, rats, and other key threats, and in captive rearing and propagation of at-risk plants and invertebrates. <!-- src: plan p.ix -->
""", "public", "standard", "Standard; participant feedback synthesis flagged insufficient attention to new management technologies.",
  ["Exec Summary p.vii, p.ix"]),

Q("site-actions", "Does the plan say which actions to take in a particular planning unit?", """
Not directly. The action prioritization compared strategies for 17 species groups across Maui Nui as a whole, not for individual planning units. <!-- src: plan p.13, p.84 --> The footprints tell managers where to work. The group strategies, the action sequence, and the list of species facing imminent extinction tell them what to do and when. <!-- src: plan p.29 --> Choosing the right mix for a single site is still a manager's call. For example, a manager might weigh whether rat control, weed control, or a predator fence would help the most species targeted in a unit. That call draws on the unit's species list in the Adaptive Conservation Planner <!-- src: plan A5-1 --> and the [taxonomic group strategies](groups.html).
""", "partner", "demo", "NPS demo (2026-09-10): neighboring units with similar target counts but different beneficial actions (rat, weed, cat control); has the team considered which actions to prioritize per species? Scott: the PTM is landscape-level, not embedded in the ACP, and not specific enough to the unit level.",
  ["Ch 3d p.13", "Ch 5e p.29", "Ch 6j p.84", "App 5 A5-1"]),

Q("sequence", "In what order should actions happen?", """
Emergency actions for the 163 species facing imminent extinction come first. <!-- src: plan p.viii --> After that, taxon expert teams recommended a sequence for each group. Start with the highest-benefit actions and the groundwork, such as fencing, ungulate removal, and weed control, that sets the stage for later reintroductions. Take up cost-effective, field-ready actions as opportunities arise. <!-- src: plan p.viii, p.29 --> Some actions work much better together. Ungulate fencing combined with weed control, for example, delivers far more benefit than either one alone. <!-- src: plan p.29 -->
""", "public", "standard", "Standard. HCC Talk 7 audience: what is the process for getting from planning to implementation?",
  ["Exec Summary p.viii", "Ch 5d pp.25-26", "Ch 5e p.29"]),

Q("cost", "How much will carrying out the plan cost?", """
The action prioritization analysis estimates that preventing the extinction of all at-risk species in Maui Nui over the next 20 years would cost, on average, about $55 million a year. <!-- src: plan A2-11 --> A large share would come in the first year, for field vehicles, propagation and rehabilitation facilities, research and development, and fence building. <!-- src: plan A2-11 --> The analysis also estimates an upfront investment of about $67 million for measures that help only one or a few groups, such as predator exclusion fencing, mosquito control, and propagation facilities. <!-- src: plan A2-1, A2-16 --> Coordinating actions across species groups is estimated to save about $10 million a year. <!-- src: plan A2-11 -->
""", "both", "standard", "Standard. Demos cited the snail exclosure program (~$4.9M total; ~$1.4M request for the next eight) but those figures are NOT in the plan and are not used.",
  ["App 2 A2-1, A2-11, A2-16"], "needs_dofaw_input"),

Q("kipuka-kahuli", "What are kīpuka kāhuli?", """
Kīpuka kāhuli are snail exclosures: managed refuges, free of predators, enclosed by a predator-proof fence that keeps out invasive predators such as the rosy wolfsnail, rats, and chameleons. <!-- src: plan pp.57-58 --> The plan calls for a network of 32 kīpuka kāhuli across Maui Nui's range of climates, protecting at least three populations of each of the 49 at-risk snail species. <!-- src: plan p.58 --> A priority set of 14 sites gives every species at least one protected population. <!-- src: plan A1-7 --> The network limits how many species share an exclosure and keeps incompatible species apart. <!-- src: plan A1-7 --> An ex situ captive rearing program on Maui provides backup. <!-- src: plan pp.57-59 -->
""", "public", "both", "Snails were the showcase case in every demo (NPS 2026-09-10: 32 exclosures instead of a naive 147). HCC Talk 3 audience: how do you keep track of the snails, and which species go together?",
  ["Ch 6e pp.57-59", "App 1 A1-7"]),

Q("fencing", "How does the plan help decide where to build fences?", """
Ungulate fencing is groundwork for most groups <!-- src: plan p.vii -->, and about half of the combined recovery footprint already has some fencing. <!-- src: plan p.vi, p.81 --> By laying the footprints over existing fences, managers can see which recovery planning units are unfenced and which species a new or extended fence line would help. <!-- src: plan p.53 --> The ecosystem analysis also lists unfenced high-quality habitat already in conservation status as a priority for starting ungulate management. Examples include windward Haleakalā, two areas on Molokaʻi, and Lānaʻihale. <!-- src: plan pp.98-99 -->
""", "both", "demo", "HCC Talk 7: 'if you had a pot of money, where would you put the next fence? It's a common question that we get.' Fence-planning application shown in the NPS demo (2026-09-10) and USFWS show-and-tell (2026-09-03).",
  ["Exec Summary p.vii", "Ch 6i p.81", "Ch 6d p.53", "Ch 7j pp.98-99"]),
]))

# ---------------------------------------------------------------- acp
categories.append(dict(id="acp", title="Using the plan and the Adaptive Conservation Planner",
    description="How managers use the plan's online tool, and who can change it.",
    questions=[
Q("what-acp", "What is the Adaptive Conservation Planner?", """
The Adaptive Conservation Planner (ACP, also called the Conservation Planner) is the online map tool that holds the plan's final map products: the recovery footprints plus information on species, habitats, and threats. <!-- src: plan p.12, p.120 --> Authorized users can view footprints for any group and click a planning unit to see which species are targeted there and whether their targets are met. They can also propose and review edits, attach notes, and export data. <!-- src: plan A5-1 --> Managers use it to build annual work plans and explore management options. <!-- src: plan p.13, p.120 --> A Managers' Handbook for DOFAW staff is being developed. <!-- src: plan p.15, A5-2 --> See [Tools](tools.html).
""", "both", "both", "Every demo; renamed from its earlier working name on 2026-09-02. Handbook in preparation (NPS demo 2026-09-10; core team 2026-09-02, 2026-09-09).",
  ["Ch 3c p.12-13", "Ch 3f p.15", "Terms p.120", "App 5 A5-1 to A5-2"]),

Q("acp-access", "Can anyone use the Adaptive Conservation Planner? How do I get access?", """
The ACP is not a public web map. It is the internal, editable tool where DOFAW staff, taxon experts, and managers inspect, refine, and maintain the conservation footprints, and it needs a user account. <!-- src: plan A5-1 --> Land managers and agency or partner staff who would use it for planning can ask DOFAW Maui for an account. DOFAW decides which level of access to grant. [TBD: contact address.] Members of the public can explore the footprints and species information on this website.
""", "both", "demo", "NPS demo (2026-09-10): logins offered by emailing Peter; USFWS (2026-09-03): logins need only an email address. Core team 2026-09-09: who counts as a 'manager', the sensitivity of the data, a possible view-only guest mode, and university classes. Plan supports only 'not a public web map; authorized users'.",
  ["App 5 A5-1"], "needs_dofaw_input"),

Q("who-edits", "Who can change the footprints, and how are changes approved?", """
Users can propose edits: move a species target to a different planning unit, add new target locations, or remove targets. Edits can be saved as private drafts, shared for team review, and then submitted for administrator approval. <!-- src: plan A5-1 --> The ACP keeps a record of how and why each change was made. <!-- src: plan A5-2 --> The ACP has been tested through full edit, review, and approval cycles, including expert fine-tuning of the plant footprint. <!-- src: plan A5-2 -->
""", "partner", "demo", "NPS demo (2026-09-10): Lucas explained that ordinary users propose and admins approve; easy approvals versus moves across partner boundaries that need the affected partner's agreement. That partner-agreement rule and the ACP's next-best-unit suggestions are not in the plan (see notes).",
  ["App 5 A5-1 to A5-2"]),

Q("field-changes", "What if conditions change, for example a new population is found or a site is lost to fire?", """
That is what the adaptive part of the planner is for. The plan is meant to be updated by managers as circumstances, funding, opportunities, and information change. <!-- src: plan p.30 --> In the ACP, users can propose moving or adding targets. They can also attach notes to species or planning units that record field observations, access problems, land-tenure information, or changes needed later. <!-- src: plan A5-1 --> The ACP keeps a dated official footprint for reporting alongside the living version. That way new populations and changed conditions can be added without losing the record of what changed and why. <!-- src: plan A5-2 -->
""", "partner", "demo", "Scott's 'adaptive' rationale for the name (core team 2026-09-02); NPS demo editing console (2026-09-10); Peter's Megalagrion and Hale Kukui[?] boundary cases and the notes function (core team 2026-09-09); demo participant note: a manager flagged silversword populations that may better serve as recovery units.",
  ["Ch 5f p.30", "App 5 A5-1 to A5-2"]),

Q("update-cadence", "How often will the footprints and the plan be updated?", """
The ACP is designed so that future annual reviews can change specific planning units while keeping a traceable record of changes. <!-- src: plan A5-2 --> The plan document itself is subject to periodic review and revision. <!-- src: plan p.i --> DOFAW expects to review proposed footprint changes once a year with partners and taxon experts, and to fold accepted changes into the official footprint. The plan's monitoring guidance suggests checking whether actions are working every year and reviewing recovery status every five to ten years. <!-- src: plan p.112 -->
""", "both", "demo", "NPS demo (2026-09-10): annual review cycle being designed. Core team 2026-09-09: the Maui branch may need to convene experts annually. Loyal 2026-09-28: a requested fire-risk change goes into the next draft and the ACP. Chad 2026-10-01: the review process is not yet fleshed out. Discrepancy tracker XP-19: no agreed post-release change process.",
  ["Front matter p.i", "Ch 8e p.112", "App 5 A5-2"], "needs_dofaw_input"),

Q("export-use", "Can I use ACP outputs in my own GIS work, management plans, or grant proposals?", """
Yes. Footprint data can be exported as CSV, GeoPackage, or GeoJSON for use in GIS and other planning systems. <!-- src: plan A5-1 --> The ACP is meant to work alongside DOFAW's Esri-based field systems, not replace them. <!-- src: plan A5-2 --> The plan is designed to help managers build work plans for individual sites, estimate costs, coordinate across agencies and landowners using shared data, and justify funding. <!-- src: plan p.5 --> For any area, the ACP shows which at-risk species are targeted in each planning unit. That gives a consistent species list for reserve management plans, project proposals, and annual work plans. <!-- src: plan p.13, A5-1 -->
""", "partner", "demo", "NPS demo (2026-09-10): exports to CSV, GeoPackage, JSON for ArcGIS; the park expects better proposal writing; DOFAW already uses it for forest reserve management plans; a funded 5-year field team package. USFWS (2026-09-03): export to GeoPackage and Excel; HCC Talk 7: funding applications. Importing user layers was demonstrated but is not in the plan (see notes).",
  ["Ch 1b p.5", "Ch 3c p.13", "App 5 A5-1 to A5-2"]),

Q("narrow-footprint", "My team can't work everywhere. How do I narrow the footprint to a starting point?", """
Use the nested footprints and filters. For Plants, the full recovery footprint has 317 planning units for 195 species. <!-- src: plan p.27, Table 4 --> The priority footprint narrows this to 155 units. Limiting it to PEPP species gives 98 units. PEPP species with three or fewer known occupied units need 39, and PEPP species with only one known occupied unit need 12. <!-- src: plan p.27, Table 4 --> The plan suggests starting with that last set and moving to the next level soon after. <!-- src: plan p.27 --> These narrower sets are where to start work, not the long-term recovery goal. <!-- src: plan p.28 --> The ACP can also show target richness, the number of at-risk species targeted in each planning unit, to find the most species-rich areas. <!-- src: plan p.83 -->
""", "partner", "demo", "NPS demo (2026-09-10): priority toggle 317 to 155, PEP filter to 98 units, 'approaching what a field team of 15-30 people could realistically reach'; USFWS (2026-09-03): 98 units; Loyal's narrowing options (2026-09-14, 2026-09-28).",
  ["Ch 5e pp.26-28, Table 4", "Ch 6i p.83"]),

Q("sensitive-data", "Does the ACP reveal where rare species occur?", """
Exact locations of rare species are sensitive. The plan maps habitat and actions at the level of planning units of about 2 km², not exact sites. <!-- src: plan p.29, p.122 --> Detailed occurrence records in the ACP are limited to a small number of administrator-level users and are never shown by default. Data shared by partners stay under the terms of their data-sharing agreements.
""", "both", "demo", "USFWS (2026-09-03): user access controls for sensitive occurrence data. HCC Talk 7 audience: what is the plan for data management and data sharing? Core team 2026-09-02 and 2026-09-09: occurrence layer for admin users only, never default; no public release of current-occurrence data. FM_revisions notes: data sharing agreements. Plan is silent on data access policy.",
  ["Ch 5f p.29", "Terms p.122"], "needs_dofaw_input"),

Q("other-tools", "Can the tools help pick exact planting or exclosure sites? What else is planned?", """
The plan includes **Find My Microhabitat**, a companion tool that zooms in from a planning unit to the specific spots best suited for outplanting, siting exclosures, surveys, or restoration. It uses fine-scale data such as vegetation structure, canopy cover, terrain, and moisture. <!-- src: plan A5-3 --> PEPP partners already use it to choose outplanting sites, and it is being documented for wider use. <!-- src: plan A5-3 --> Three more tools are planned for release: Potential Recovery Sites, Climate Vectors, and a Footprint Summarizer. <!-- src: plan A5-1 --> Planned ACP improvements include better display of occurrence data, detection of conflicting edits, custom species overlays, and documentation for use beyond Maui Nui. <!-- src: plan A5-2 -->
""", "partner", "demo", "A demo attendee asked whether the team had ideas for future additions (core team 2026-09-30). Core team 2026-09-02: PRS and microhabitat tools help managers home in within coarse PUs. Lessons-learned v3.0 lists PRS, Find My Habitat, bat layer, and mosquito layer as items to finish.",
  ["Ch 6d p.53", "App 5 A5-1 to A5-3"]),
]))

# ---------------------------------------------------------------- land
categories.append(dict(id="land", title="Land ownership, regulation, and private landowners",
    description="What the plan does and does not mean for landowners and for regulatory processes.",
    questions=[
Q("regulatory", "Is the MNLCP a regulation?", """
No. The MNLCP is a decision-support plan that gives flexible guidance to managers. It is built on partnership, not on prescriptive mandates. <!-- src: plan pp.8-9, p.121 --> It does not create new rules, permits, or land-use restrictions. Existing protections for listed species under state and federal law are unchanged, and the plan works within them. <!-- src: plan p.3, p.120 -->
""", "public", "standard", "Standard question for any large public plan. Plan supports 'decision-support orientation, flexible guidance' and 'rather than prescriptive mandates'. The plan does not explicitly say it creates no rules or restrictions, so that sentence needs DOFAW confirmation.",
  ["Ch 2d pp.8-9", "Terms pp.120-121", "Ch 1a p.3"], "needs_dofaw_input"),

Q("my-land", "Part of my land is inside a footprint. What does that mean for me?", """
A footprint shows where habitat that could help recover at-risk species exists or could be restored. It is a planning map, not a designation, and it places no requirement on a landowner. Most of the footprint, about 66 percent, is on biodiversity reserves. <!-- src: plan p.vi, p.81 --> Where footprint areas fall on other lands, the plan's approach is to build partnerships with private landowners, communities, and agencies to support recovery and habitat management. <!-- src: plan p.ix --> Any work on private land would happen only through voluntary agreement with the landowner. [TBD: DOFAW contact for landowners.]
""", "public", "standard", "Standard concern for a public footprint map. USFWS (2026-09-03) and NPS (2026-09-10) demos discussed land ownership; demo notes: unclear how the watershed partnership will lead on private lands. Plan does not state footprint implications for landowners.",
  ["Exec Summary p.vi, p.ix", "Ch 6i p.81"], "needs_dofaw_input"),

Q("private-landowners", "How can private landowners take part?", """
The plan calls for partnerships with private landowners, communities, and agencies to promote recovery and habitat management. <!-- src: plan p.ix --> Its ecosystem priorities include working with landowners and partners where high-quality native habitat lies outside conservation status. Examples include eastern Molokaʻi, the area above Makawao, and Kahikinui. <!-- src: plan p.ix, p.99 --> Recommended actions include working with private landowners on ungulate control and creating a landowner incentive program. <!-- src: plan A2-29 --> Watershed partnerships, which co-manage public and private lands for ecosystem health, are an important link. <!-- src: plan p.93 --> [TBD: how landowners can contact DOFAW.]
""", "public", "both", "HCC Talk 7 audience: how will recommendations be carried across land boundaries? Peter: watershed partnerships bridge that gap. Demo notes (2026-07-23): unclear how the watershed partnership will lead on private lands. Participant feedback: more involvement of landowners.",
  ["Exec Summary p.ix", "Ch 7e p.93", "Ch 7j p.99", "App 2 A2-29"], "needs_dofaw_input"),

Q("critical-habitat", "How does the plan relate to federal critical habitat or permitting?", """
The plan does not designate critical habitat. That is a separate federal process under the Endangered Species Act, and reintroductions still go through their usual reviews. USFWS was a partner in developing the plan. <!-- src: plan p.v --> The recovery footprints and the data behind them can inform federal and state recovery work. They were built for management, though, and weigh practical factors such as accessibility, existing fencing, and long-term conservation commitment of the land. <!-- src: plan A1-3 to A1-4 --> Lining up regulatory designations with the plan's recovery areas helps keep management and regulation consistent.
""", "partner", "demo", "NPS demo (2026-09-10): how integrated is USFWS, and is this a first hurdle toward compliance for a reintroduction? USFWS show-and-tell (2026-09-03) and core team 2026-09-09 / spatial team 2026-09-08: USFWS writing critical habitat for 46 species; critical habitat cannot consider ownership or fencing; the team advised alignment rather than adopting PUs directly. The plan does not mention critical habitat at all.",
  ["Exec Summary p.v", "App 1 A1-3 to A1-4"], "needs_dofaw_input"),

Q("acquisition", "Does the plan help guide land protection or acquisition?", """
Yes. One stated use of the plan is to help identify lands that should be managed under long-term protection. <!-- src: plan p.5 --> The ecosystem analysis maps where high-quality native habitat lies outside conservation status and is unfenced. It labels such areas "Engage: management possible if land is secured." <!-- src: plan p.94, p.99 --> For any parcel of interest, the ACP can list the at-risk species targeted in its planning units. That helps show its value for conservation. <!-- src: plan A5-1 -->
""", "partner", "demo", "NPS demo (2026-09-10) land-acquisition application; TNC demo (core team 2026-09-30) interest in ramping up acquisition; core team 2026-09-09: TPL, HILT, and Maui County open space program as potential users; FM_revisions 'applications' doc: use in land acquisition planning.",
  ["Ch 1b p.5", "Ch 7e p.94", "Ch 7j p.99", "App 5 A5-1"]),
]))

# ---------------------------------------------------------------- climate
categories.append(dict(id="climate", title="Climate change and fire",
    description="How the plan accounts for a changing climate and for wildfire.",
    questions=[
Q("climate", "How does the plan account for climate change?", """
In several ways. Climate resilience was one of the criteria for choosing footprints. It was estimated from how fast temperature and rainfall have actually changed in the past, rather than from uncertain future projections. <!-- src: plan A1-3 --> Plant recovery areas were built with climate-suitability models, and snail habitat with climate-similarity models. <!-- src: plan p.50, A1-2 --> The resulting footprints generally have better-than-average climate resilience. <!-- src: plan p.vii, p.81 --> The ecosystem analysis found that most high-quality native habitat is changing more slowly than the Maui Nui average, but it is still changing. Managers should watch for these changes and adjust their strategies if needed. <!-- src: plan pp.97-98 -->
""", "public", "both", "HCC Talk 5 audience: 'the world is changing, how have you incorporated that reality into this assessment?' Standard question. Lessons-learned v3.0 notes the climate synthesis could have gone further.",
  ["App 1 A1-2 to A1-3", "Ch 6d p.50", "Exec Summary p.vii", "Ch 6i p.81", "Ch 7i pp.97-98"]),

Q("fire", "Does the plan consider wildfire?", """
Yes. Fire risk was one of the criteria for choosing footprints, because lower fire risk reduces the chance of losing conservation investments. <!-- src: plan A1-3 to A1-4 --> Fire management is among the highest-priority actions for Plants. <!-- src: plan p.v, Table 1 --> Building firebreaks is one of the recommended habitat management actions <!-- src: plan A2-30 -->, and firebreaks can be one of the first steps before reintroducing a species. <!-- src: plan p.26 -->
""", "public", "standard", "Standard. Fire risk was named as a criterion in every demo (NPS 2026-09-10; USFWS 2026-09-03).",
  ["App 1 A1-3 to A1-4", "Exec Summary Table 1 p.v", "Ch 5d p.26", "App 2 A2-30"]),
]))

# ---------------------------------------------------------------- ecosystems
categories.append(dict(id="ecosystems", title="Ecosystems and cultural values",
    description="How the plan looks beyond individual species.",
    questions=[
Q("why-ecosystems", "Why does the plan include ecosystems as well as species?", """
Healthy native ecosystems keep more species from becoming at risk and give recovering species room to expand. <!-- src: plan p.viii --> They provide connections between populations, buffers against threats, backup populations, and space to grow. <!-- src: plan p.14 --> The plan maps ten ecosystems, plus special features such as anchialine pools, lava tubes, bogs, and cliffs. <!-- src: plan p.viii --> Some ecosystems are nearly gone: lowland dry forest, once the most extensive type, keeps only about two percent of its original area. <!-- src: plan p.viii --> See [Ecosystems](ecosystems.html).
""", "public", "standard", "Standard.",
  ["Exec Summary p.viii", "Ch 3e p.14"]),

Q("ecosystem-priorities", "What are the plan's ecosystem priorities?", """
The plan sets four ecosystem priorities, in order <!-- src: plan pp.viii-ix, pp.98-100 -->:

1. Maintain high-quality habitat that is already fenced and managed.
2. Start ungulate management on unfenced high-quality land already in conservation status, such as windward Haleakalā, two areas of Molokaʻi, and Lānaʻihale.
3. Work with landowners and partners where high-quality habitat lies outside conservation status, including eastern Molokaʻi, the area above Makawao, and Kahikinui.
4. Restore degraded habitats that matter most for species recovery, connectivity, diversity, and climate resilience.
""", "public", "standard", "Standard.",
  ["Exec Summary pp.viii-ix", "Ch 7h-j pp.97-100"]),

Q("cultural-values", "How does the plan consider cultural values?", """
The plan recognizes that Hawaiʻi's native species and habitats are closely tied to the state's biocultural heritage. These ecosystems are the foundation of cultural practices, natural resource management, and local economies. <!-- src: plan pp.5-6 --> The plan's third goal is to protect and restore native ecosystems so they keep sustaining clean water, cultural values, and local economies. <!-- src: plan p.v --> Its planning approach is built on partnership and on respect for local communities and cultures. <!-- src: plan p.9 -->
""", "public", "standard", "Standard. Participant feedback recommended greater involvement of Native Hawaiian organizations and community stakeholders.",
  ["Exec Summary p.v", "Ch 1c pp.5-6", "Ch 2d p.9"]),
]))

# ---------------------------------------------------------------- monitoring
categories.append(dict(id="monitoring", title="Monitoring, updates, and what comes next",
    description="How progress will be tracked and how the plan will change over time.",
    questions=[
Q("measure-progress", "How will progress be measured?", """
Each species has population targets assigned to specific planning units. So monitoring can ask the same question everywhere: is the population in each targeted unit moving toward the numbers and spread the plan calls for? <!-- src: plan pp.102-103 --> The answers feed adaptive management, a learning cycle of collecting monitoring data, evaluating it, and using the results to decide whether the location, type, or intensity of management should change. <!-- src: plan p.101, p.103 --> The plan suggests checking whether actions are working every year and reviewing recovery status every five to ten years. It also calls for an annual accomplishment report and a current status dashboard. <!-- src: plan p.112, p.113 --> See [Monitoring](monitoring.html).
""", "public", "standard", "Standard. Core team 2026-09-09: linking monitoring data to the ACP (e.g., which plants were planted in which units and survive).",
  ["Ch 8a pp.101-103", "Ch 8e p.112", "Ch 8f p.113"]),

Q("is-final", "Is this the final plan? Will it change?", """
The plan document is a dated version, September 29, 2026, and is subject to periodic review and revision. <!-- src: plan p.i --> The conservation footprints in the Adaptive Conservation Planner are the living version that managers use day to day. A stable, dated official footprint is kept alongside them for reporting. <!-- src: plan A5-1 to A5-2 --> The plan is meant to be updated as conditions, funding, opportunities, and knowledge change. <!-- src: plan p.30 -->
""", "public", "both", "Core team 2026-09-28 (Loyal): the published plan is a snapshot in time, and the footprints in the ACP are what people will actually use; NPS demo (2026-09-10) closing: a tool that can't be edited would be outdated within a year.",
  ["Front matter p.i", "Ch 5f p.30", "App 5 A5-1 to A5-2"]),

Q("what-success-requires", "Is the plan funded? What will it take to succeed?", """
The plan sets out what is needed. Carrying it out depends on sustained funding, staff, and partnerships. It calls on leaders and partners to <!-- src: plan p.ix -->:

- fund emergency actions now for the 163 species that could be lost within five years;
- invest in new tools for the hardest threats and for captive rearing and propagation;
- sustain and expand groundwork such as fencing, ungulate removal, weed and predator control, wetland and stream flow management, and fire prevention;
- build partnerships with private landowners, communities, and agencies;
- protect, manage, and restore native ecosystems;
- fill data gaps for the 143 species that cannot yet be mapped; and
- use the plan as a living system to guide annual work plans and budgets.
""", "public", "both", "Participant feedback synthesis: implementation feasibility, funding, staffing, and long-term sustainability were the main concerns. HCC Talk 7: getting from planning to implementation is 'a funding process at this point'.",
  ["Exec Summary p.ix"]),

Q("other-islands", "Will this approach be used on other islands?", """
The plan is meant to serve as a model for other islands and programs. <!-- src: plan p.103 --> The action prioritization process was designed so it can be applied to other islands in the state. <!-- src: plan A2-1 --> Planned improvements to the ACP include documentation for use beyond Maui Nui. <!-- src: plan A5-2 -->
""", "both", "demo", "USFWS show-and-tell (2026-09-03): the same process is beginning on Oʻahu. Demo participant notes: the Kauaʻi and Oʻahu branch managers want next-generation applications. Core team 2026-09-02: how will cross-island targets talk to each other? The Oʻahu effort is not in the plan, so it is not named.",
  ["Ch 8a p.103", "App 2 A2-1", "App 5 A5-2"]),
]))

# ---------------------------------------------------------------- involved
categories.append(dict(id="involved", title="Getting involved",
    description="How to share information, get the plan, and contact DOFAW.",
    questions=[
Q("share-info", "I have new information about an at-risk species. How can I share it or get involved?", """
New observations matter. The footprints are designed to take in new population discoveries, field knowledge, and changed conditions. <!-- src: plan A5-2 --> Records of at-risk species, especially populations not yet known, can help fill data gaps for the 143 species that cannot yet be mapped. <!-- src: plan p.ix --> Please send observations to DOFAW Maui Branch. [TBD: contact address and preferred format.] Land managers and partner organizations interested in using the plan can ask about access to the Adaptive Conservation Planner.
""", "both", "demo", "Core team 2026-09-09 (Peter): new records reach the team haphazardly, such as an iNaturalist post. NPS demo (2026-09-10): managers should feed adjustments back. Core team 2026-09-28: seeing the tool motivates experts to supply data.",
  ["Exec Summary p.ix", "App 5 A5-2"], "needs_dofaw_input"),

Q("community", "How were communities and Native Hawaiian organizations involved?", """
DOFAW Maui developed the plan with a broad coalition of public and private agencies, organizations, landowners, and technical experts. <!-- src: plan p.4 --> The approach is built on partnership and on respect for local communities and cultures <!-- src: plan p.9 -->, and the plan calls for building partnerships with communities as it is carried out. <!-- src: plan p.ix --> [TBD: describe community and Native Hawaiian engagement to date and how it will continue during implementation.]
""", "public", "standard", "Participant feedback synthesis: suggestions for greater involvement of watershed partnerships, landowners, Native Hawaiian organizations, field practitioners, and community stakeholders. Plan does not describe community engagement.",
  ["Ch 1a p.4", "Ch 2d p.9", "Exec Summary p.ix"], "needs_dofaw_input"),

Q("get-plan", "Where can I get the full plan and the maps?", """
The full plan is available from the [Resources](resources.html) page. The combined footprints can be explored on the [Conservation Footprints map](map.html), and the species on the [At-Risk Species](species.html) page. [TBD: confirm the plan PDF is cleared for public download, and which map files (such as the KMZ) can be shared.]
""", "public", "standard", "Standard. USFWS (2026-09-03) asked for the written plan; core team 2026-09-23: the document will be made public-ready, with the USGS review constraint on the appendix.",
  [], "needs_dofaw_input"),
]))

# ---------------------------------------------------------------- build
data = {"_source": SOURCE, "categories": categories}

# checks
banned = [r"\boptimi[sz]", r"footprint manager", r"\bsav(e|ing) species", r"\bsurvey(s|ed)? of experts", r"questionnaire", r"blueprint", r"conservation lands"]
nq = 0
for c in categories:
    for q in c["questions"]:
        nq += 1
        txt = re.sub(r"<!--.*?-->", "", q["a"])
        words = len(re.findall(r"\b\w[\w'’ʻ-]*\b", txt))
        if not (40 <= words <= 155):
            print(f"WORDS {q['id']}: {words}", file=sys.stderr)
        for b in banned:
            if re.search(b, q["q"] + " " + q["a"], re.I):
                print(f"BANNED {b} in {q['id']}", file=sys.stderr)
        if "`" in q["a"]:
            print(f"BACKTICK in {q['id']}", file=sys.stderr)
print(f"{nq} questions; needs_dofaw_input: " + ", ".join(q["id"] for c in categories for q in c["questions"] if q["status"] != "ready"), file=sys.stderr)

(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "data" / "faq.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# markdown
md = []
md.append("""---
title: Questions & Answers
slug: faq
nav_label: Q&A
summary: Answers to common questions about the Maui Nui Landscape Conservation Plan and the Adaptive Conservation Planner, including questions partners raised when the plan and the tool were first demonstrated.
plan_sources: [Exec Summary, Ch 1-8, Terms and Definitions, App 1, App 2, App 5]
---

## Lead
These are the questions people ask most often about the Maui Nui Landscape Conservation Plan (MNLCP). Many came from land managers, agency staff, and scientists when DOFAW and its partners first demonstrated the plan and its online tool, the Adaptive Conservation Planner. Each answer is drawn from the plan itself. Search or browse by topic below.
""")
for c in categories:
    md.append(f"## {c['title']}\n\n{c['description']}\n")
    for q in c["questions"]:
        flag = " <!-- status: needs_dofaw_input -->" if q["status"] != "ready" else ""
        md.append(f"### {q['q']}{flag}\n\n{q['a']}\n")
(ROOT / "pages" / "faq.md").write_text("\n".join(md), encoding="utf-8")
print("wrote faq.json and faq.md", file=sys.stderr)
