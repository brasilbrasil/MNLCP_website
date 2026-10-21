---
title: Adaptive Conservation Planner & Tools
slug: tools
nav_label: Tools
summary: The Adaptive Conservation Planner is the online system that holds the plan's conservation footprints and keeps them current, so managers can build annual work plans and update priorities as conditions, knowledge, and funding change.
plan_sources: [App 5, Executive Summary, Ch 3c, Ch 5e-f, Ch 6i, Terms and Definitions]
---

## Lead
The MNLCP is not only a document. It is delivered as a living system, and at its center is the
Adaptive Conservation Planner, an online mapping tool that holds the plan's conservation footprints
and the species, habitat, and threat information behind them. <!-- src: plan p.v; p.12 Ch 3c -->
Managers use it to build annual work plans and to update priorities as conditions, knowledge, and
funding change. <!-- src: plan p.v -->
A second tool, Find My Microhabitat, helps field teams find the best spots on the ground within a
priority area, and three more tools are planned. <!-- src: plan p.A5-1, A5-3 -->

## Key numbers
- **7** | taxonomic groups whose conservation footprints can be viewed in the ACP, one at a time or overlaid <!-- src: plan p.A5-1 -->
- **1,400** | planning units, each about 2 km², the building blocks of every footprint shown in the ACP <!-- src: plan p.13 Ch 3c; Terms and Definitions p.122 -->
- **3** | export formats for footprint data: CSV, GeoPackage, and GeoJSON <!-- src: plan p.A5-1 -->
- **2** | tools available now (the ACP and Find My Microhabitat), with 3 more to be released <!-- src: plan p.A5-1 Introduction -->

## What the Adaptive Conservation Planner is
The Adaptive Conservation Planner (ACP, or "Conservation Planner" for short) is where the MNLCP's
final spatial products live. <!-- src: plan p.12 Ch 3c; Terms p.120 --> It holds the recovery
footprints for each taxonomic group, the planning units (PUs) that make them up, the species
targeted in each unit, and supporting information on species, habitats, and threats.

It is part of the TFE-SCP process, the comprehensive planning process used for the plan's spatial
prioritization. The ACP carries conservation footprints from draft prioritization results, through
fine-tuning by species experts, and into long-term care of the plan. <!-- src: plan p.A5-1 -->

> **Callout:** A conservation plan should not be a static document that goes out of date. The
> Conservation Planner is how the MNLCP stays current. <!-- src: plan p.A5-1 -->

## Who it is for
The ACP is a working tool for the people who carry out the plan: DOFAW staff, taxon experts, and
land managers. It is not a public web map and it is not a task tracker. <!-- src: plan p.A5-1 -->
Users sign in with an account, and what each person can do depends on their role:

- **Read-only users** can view footprints, map layers, and species targets.
- **Users** can also propose footprint edits and write notes.
- **Admins** review and approve proposed edits and manage accounts.

<!-- src: ACP user guide, docs/site/roles-and-permissions.qmd. Not in the plan; the plan says only "authorized users" (p.A5-1). -->

Sensitive information, such as exact locations of rare species, is shown only to accounts that
have been given permission for it. <!-- src: ACP user guide, roles-and-permissions.qmd -->

## What you can do with it

### Plan the year's work
The plan describes the ACP as the tool managers use to develop annual work plans, adjust strategies
based on results and new information, and explore different management scenarios.
<!-- src: plan p.13 Ch 3c(ii); Terms p.120 --> For example, managers can narrow a priority footprint
to the species in greatest need, such as plants facing imminent extinction that are known from only
one or a few planning units, to set a focused first round of work. <!-- src: plan p.27 Ch 5e -->
See [Using the Plan](using-the-plan.html) for the full worked example.

### View footprints by group or species
Choose one or more taxonomic groups and the ACP draws their conservation footprints on the map,
separately or overlaid. <!-- src: plan p.A5-1 --> With several groups loaded, you can show a
combined footprint, or a target richness map that colors each planning unit by how many at-risk
species are targeted there. The richness view helps find exceptional areas that support many
at-risk species or species facing imminent extinction. <!-- src: plan p.83 Ch 6i(iv), Figure 20; ACP user guide map-layers.qmd -->

Search for a single species to see its suitable habitat, its recovery and priority units, and its
known populations. <!-- src: ACP user guide species-layers.qmd -->

### See what is targeted in each planning unit
Select a planning unit to see which species are targeted there, their habitat suitability, the
evidence that they occur there, and whether their targets are met. <!-- src: plan p.A5-1 -->

### Add context layers
Overlay other maps, such as biodiversity reserves, fire risk, or climate resilience, to see how a
footprint relates to land status and threats. Users can upload their own layers as well.
<!-- src: ACP user guide map-layers.qmd; layer names from screenshots manage-aux-layers.png, map-layers.png -->

### Propose changes and add notes
Authorized users can propose edits: move a species target to a different planning unit, add a new
target location, remove a target, or change whether a target is part of the priority footprint.
They can also attach notes to species or planning units to record field observations, access
concerns, land-tenure information, or revisions needed later. <!-- src: plan p.A5-1 -->

### Export the data
Download footprint data as CSV, GeoPackage, or GeoJSON for use in GIS or other planning systems.
Exports can be limited to selected groups, species, or planning units. <!-- src: plan p.A5-1; ACP user guide exports.qmd -->

## How the ACP keeps the plan current
The ACP keeps two things side by side: <!-- src: plan p.A5-1 to A5-2 -->

- **A versioned official footprint:** a stable, dated snapshot (for example, the 2026 official
  footprint) used for reporting, hand-off, and as the formal reference for implementation.
- **A living platform:** where ongoing edits, annual reviews, newly found populations, and changes
  in management conditions are added, with a record of how and why each change was made.

This means DOFAW can give partners a stable product to plan around while keeping the footprints up
to date as knowledge improves. Future annual reviews can change specific planning units, and the
change history stays traceable. <!-- src: plan p.A5-2 -->

Changes are never made in one step. A proposed edit is saved privately, then published for review
by the team, and only becomes part of the footprint once an administrator approves it.
<!-- src: plan p.A5-1; ACP user guide edits-and-review.qmd -->

[figure: Diagram of the edit cycle: Save (private draft) → Publish (team review) → Approve (admin) → Accepted footprint, with a loop back for annual review | suggested source: new simple SVG drawn from plan p.A5-1 and ACP user guide edits-and-review.qmd | alt: Four-step cycle showing how a proposed footprint edit moves from a private draft to team review to admin approval to the accepted footprint]

## Screenshot walkthrough
The images below follow a first session in the Conservation Planner. <!-- Screenshots from the ACP user guide (MauiNui-ConservationFootprintManager/docs/site/assets/screenshots/). All 8 must be recaptured or cropped before publishing: the header shows the old app name and a personal email address. See notes/tools.md. -->

[figure: 1. The main screen. Map Layers, Targets, and Edits tabs on the left; the map on the right. Here Plants, Terrestrial snails, and Terrestrial arthropods are loaded and the target richness map shows where targets cluster | suggested source: ACP repo docs/site/assets/screenshots/home.png | alt: Map of Molokaʻi, Lānaʻi, Maui, and Kahoʻolawe divided into planning units, shaded from pale yellow to dark red by number of species targets, with a layer list on the left]

[figure: 2. Choose taxonomic groups. The selector at the top loads one or more groups' footprints; each loaded group then appears as a layer you can switch on or off | suggested source: ACP repo docs/site/assets/screenshots/select-footprints.png | alt: Drop-down list of taxonomic groups open above the map, with Snails, Plants, and Terrestrial Arthropods selected and other groups listed]

[figure: 3. The layout with one group loaded. The Terrestrial snails footprint is shown in blue; hovering over a planning unit shows its ID | suggested source: ACP repo docs/site/assets/screenshots/app-layout.png | alt: Map with scattered blue planning units on Molokaʻi, Lānaʻi, and Maui, and a label reading Unit 6167]

[figure: 4. Map Layers. Toggle planning units, target richness, combined footprints, each group's footprint, and its priority units | suggested source: ACP repo docs/site/assets/screenshots/map-layers.png | alt: Layer panel with switches for Planning Units, Target Richness, Combined Footprint, Combined Priority Footprint, and Plants, Snails, and Terrestrial Arthropods footprints]

[figure: 5. Species layers. Searching for the Haleakalā silversword shows its suitable habitat (green shading) and known locations (blue dots), with a summary of its targets | suggested source: ACP repo docs/site/assets/screenshots/species-layers.png | alt: Map of East Maui with green-shaded planning units and blue dots near the summit of Haleakalā, and a species panel listing 10 targets and 1 known population]

[figure: 6. Targets in a planning unit. Selecting unit 4033 lists the plants, snails, and arthropods targeted there; markers flag known populations, priority locations, and species still short of their targets | suggested source: ACP repo docs/site/assets/screenshots/unit-targets.png | alt: List of species targeted in planning unit 4033 grouped under Plants, Snails, and Terrestrial Arthropods, beside a map of West and East Maui with the footprint in green]

[figure: 7. Context layers. The layer manager holds personal and shared map layers, such as fire risk and climate resilience, that can be added to the map | suggested source: ACP repo docs/site/assets/screenshots/manage-aux-layers.png (crop to hide internal layer names; see notes) | alt: Dialog titled Manage auxiliary map layers listing shared layers including Climate resilience and Fire risk]

[figure: 8. Styling a layer. Change line and fill color and transparency for any layer | suggested source: ACP repo docs/site/assets/screenshots/layer-style-modal.png | alt: Dialog titled Style Map Layer with line color, weight, and opacity and fill color and opacity settings]

## Getting access
The plan lists the following address for the Conservation Planner: <!-- src: plan p.A5-2 -->

[Open the Adaptive Conservation Planner](https://icculus.shinyapps.io/MauiNui-ConservationFootprintManager/) <!-- DOFAW TO CONFIRM: the ACP is moving to https://acp.fullstackeco.com and the address above will become a redirect. Use whichever DOFAW confirms as permanent before launch. See notes/tools.md. -->

An account is needed to sign in. Accounts are set up by an ACP administrator, who assigns each
person a role. <!-- src: ACP user guide getting-started.qmd, admin.qmd -->
**[PLACEHOLDER: how partners request an account, and whom to contact. Not stated in the plan; DOFAW to supply.]**

The ACP will be described in more detail in the Managers' Handbook being developed for DOFAW
staff. <!-- src: plan p.A5-2; p.15 Ch 3f -->

## Current status
The Conservation Planner is in operational use. It has been used to fine-tune the plant recovery
footprint (its most mature use), to review snail exclosure (kīpuka kāhuli) sites, and to review
arthropod targets. It handles footprints for several taxonomic groups at once and has been tested
through full edit, review, and approval cycles. <!-- src: plan p.A5-2 -->

Planned improvements include: <!-- src: plan p.A5-2 -->
- better display of occurrence data for some groups
- automatic detection of conflicting edits between recovery and priority footprints
- custom overlays for individual species
- clearer save and publish behavior
- documentation so the system can be used beyond Maui Nui

:::details How the ACP fits with DOFAW's other systems
The long-term design pairs two connected systems. The Conservation Planner handles the specialized
footprint logic of the TFE-SCP process: species targets, criteria, notes, and footprint versions.
DOFAW's Esri environment handles broader implementation tracking: field surveys, work orders, fence
status, and effort records. The Conservation Planner is meant to complement Esri-based field systems,
not replace them, by adding the species-level, multi-criteria footprint logic that standard GIS
platforms do not provide. <!-- src: plan p.A5-2 -->

The ACP also shows recovery footprints, priority footprints, and narrower implementation subsets
nested in a single view, so that a change made once carries through to every product that depends
on it. <!-- src: plan p.A5-1 -->
:::

:::details Roles and permissions in detail
| Feature | Admin | User | Read-only user |
|---|---|---|---|
| View map layers and targets | Yes | Yes | Yes |
| Manage personal map layers | Yes | Yes | Yes |
| Propose footprint edits | Yes | Yes | No |
| Create or reply to notes | Yes | Yes | No |
| Review and approve proposed edits | Yes | No | No |
| Manage users and download edit logs | Yes | No | No |
| View sensitive species point locations | Yes | If permitted | If permitted |

<!-- src: ACP user guide roles-and-permissions.qmd (not in the plan) -->
:::

## Other tools
The plan lists four companion tools. Only Find My Microhabitat is available now; the others will be
released in the near future. <!-- src: plan p.A5-1 Introduction -->

### Find My Microhabitat (available)
Conservation footprints answer the question "where should we focus?" at the scale of planning
units, which can be hundreds of hectares. But an outplanting site, survey transect, or exclosure
covers a fraction of a hectare. Find My Microhabitat bridges that gap: within a selected planning
unit, it combines high-resolution data on vegetation structure, canopy cover, topographic position,
moisture, and other local habitat variables to find the most suitable microsites for target
species. <!-- src: plan p.A5-3 -->

It is useful for:
- **Outplanting:** finding the spots within a footprint planning unit where rare plant
  reintroductions are most likely to succeed
- **Exclosure siting:** refining candidate kīpuka kāhuli (snail exclosure) locations within
  priority areas
- **Survey targeting:** sending field surveys to the most promising microsites for data-deficient
  species
- **Restoration planning:** finding where habitat restoration will most benefit target species

<!-- src: plan p.A5-3 -->

Plant Extinction Prevention Program (PEPP) partners already use the tool to choose outplanting sites
within plant footprint planning units. It is being documented so that more DOFAW staff and partners
can use it without developer support. <!-- src: plan p.A5-3 to A5-4 --> The plan gives no public
link for the tool.

### Coming soon
- **Potential Recovery Sites (PRS):** map layers of potential recovery sites based on climate
  suitability and habitat quality, to help managers focus field searches for suitable sites.
  <!-- src: plan p.53 Ch 6d(v); p.A5-1, A5-4 -->
- **Climate Vectors**
- **Footprint Summarizer**

<!-- src: plan p.A5-1, A5-4 (App 5 gives section headings only; Climate Vectors and Footprint Summarizer have no description in the plan) -->

The plan says these within-unit tools will let the Conservation Planner show managers where species
occur, where habitat quality is high, where potential recovery sites are, where climatic conditions
seem to be changing most rapidly, and where certain microhabitats might be found within a planning
unit. <!-- src: plan p.29-30 Ch 5f -->
