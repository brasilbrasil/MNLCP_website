# Content guide for MNLCP website drafting

Read this before writing any content file. The site is a **DOFAW** public website documenting the
*Maui Nui Landscape Conservation Plan* (MNLCP), for partners and the public. See `../PLAN.md`.

## Sources

- **The plan (authoritative):** `/hdd/projects/maui_nui_scp/maui_nui_products/project_context_docs/IMPORTANT/MNLCP 9-30-2026 FINAL.txt`
  (8,152 lines; PDF alongside with the same name). Read your assigned line ranges in full with
  `sed -n 'A,Bp'`. Do not read the whole file. Printed page numbers appear as lone numbers
  (e.g. `vi`, `47`, `A1-3`) on their own lines; use them for citations.
- **Messaging rules (mandatory):** `/hdd/projects/maui_nui_scp/maui_nui_products/project_context_docs/IMPORTANT/MNLCP messaging guidelines.txt`
- **Discrepancy tracker:** `/hdd/projects/maui_nui_scp/maui_nui_products/project_context_docs/IMPORTANT/MNLCP_cross_product_discrepancies.md`
  — check before quoting any footprint or species number.
- Supporting knowledge base (use for clarity, never to contradict the plan):
  `/hdd/projects/maui_nui_scp/maui_nui_products/project_context_docs/topic_summaries/`, `taxon_synthesis/`.

## Non-negotiable rules

1. **The site mirrors the plan.** Use the plan's figures in text. Do not invent facts, numbers,
   quotes, dates, or people. If something a page needs is not in the plan, say so in your notes
   file rather than filling the gap.
2. **Cite every number** with an HTML comment right after it: `<!-- src: plan p.vi, Table 1 -->`
   or `<!-- src: plan lines 1040-1060 -->`. These are stripped from the public page but let DOFAW verify.
3. **Discrepancies:** if a plan number disagrees with the discrepancy tracker, or the plan is
   internally inconsistent (e.g. 374 vs 442 at-risk species in different places), keep the plan's
   main figure in text and record the issue in your notes file with line references.
4. **Messaging:** "prioritization" never "optimization"; "conservation footprints" (recovery
   footprints, priority footprints; snails keep "preventing extinction footprint" where the plan
   uses it); "recover species"/"prevent extinctions", never "save species"; "biodiversity
   reserves"; "team" = people, "group" = species; capitalize group names (Plants, Terrestrial
   arthropods, Terrestrial snails, Aquatic invertebrates, Forest birds, Seabirds, Waterbirds; also
   Hawaiian hoary bat); TFE-SCP is a "comprehensive planning process", not a framework;
   "Adaptive Conservation Planner" on first mention per page, then "ACP" or "Conservation Planner"
   (never "Footprint Manager"). Expert engagement: "DOFAW coordinated taxon expert teams; experts
   participated in collaborative review sessions"; never "survey", "questionnaire", "data collection"
   from experts.
5. **DOFAW voice.** The plan is DOFAW's. Partners are credited by role ("spatial prioritization,
   led by USGS"), but the site does not read as a USGS product.
6. **Hawaiian orthography:** keep ʻokina (ʻ, U+02BB) and kahakō exactly as the plan uses them
   (Molokaʻi, Lānaʻi, Kahoʻolawe, Haleakalā, ʻōpeʻapeʻa, kīpuka kāhuli). Fix obvious extraction
   artifacts (backticks used as ʻokina, broken ligatures like "ﬁ").
7. **Plain language.** Public readers first: short sentences, define jargon at first use (PU,
   PTM, SCP). Practitioner depth goes in "Details" sections.

## Page file format (`content/pages/<slug>.md`)

```markdown
---
title: Page title
slug: page-slug
nav_label: Short nav label
summary: One or two plain-language sentences (used in cards and meta description).
plan_sources: [Ch 5 a-f, App 5]
---

## Lead
Two to four plain-language sentences that open the page.

## Key numbers
- **442** | native species at risk of extinction across Maui Nui <!-- src: plan p.iv -->
- **163** | face imminent extinction within five years without emergency action <!-- src: … -->

## <Section heading>
Body text. Use ### for subsections. Keep paragraphs short.

> **Callout:** a key message worth pulling out visually.

:::details Title of an expandable practitioner section
Longer technical text that is collapsed by default.
:::

[figure: short description of the ideal image | suggested source: plan PDF p.vi Figure 1 | alt: alt text]

[table: caption]
| col | col |
|---|---|
```

Use only these constructs (plain Markdown + `## Lead`, `## Key numbers`, `> **Callout:**`,
`:::details … :::`, `[figure: …]`). The build step converts them to HTML.

## Data file formats (`content/data/`)

JSON, UTF-8, pretty-printed, with a top-level `"_source"` string naming the plan sections/lines.
Specific schemas are given in each task brief.

## Notes file

Each drafter writes `content/notes/<your-task-id>.md` listing: discrepancies found (with line
refs), gaps (things a page needs that the plan lacks), suggested images, and questions for DOFAW.
Never edit another task's files.
