# Notes for task `tools`

Files written:
- `content/pages/tools.md`: Adaptive Conservation Planner & Tools
- `content/pages/resources.md`: Resources
- `content/data/glossary.json`: 28 terms (all of Terms and Definitions, plan lines 4756-4912, pp. 120-123)
- `content/data/references.json`: 49 entries (all of Literature Cited, plan lines 4576-4755, pp. 115-119)

Plan line numbers below refer to `MNLCP 9-30-2026 FINAL.txt`.

## 1. ACP URL findings (decide before launch)

| Address | What it is | Source |
|---|---|---|
| `https://icculus.shinyapps.io/MauiNui-ConservationFootprintManager/` | The only address in the plan (App 5, line 7422, p.A5-2) and in `SO_web_tools.txt`. The repo calls it the **legacy** app. It will be replaced by a maintenance page and then a 10-second **redirect** to the AWS address. | ACP repo `docs/legacy-deployment.md`, `docs/aws-cutover-runbook.md` lines 42-43, `deploy/shinyapps/redirect/app.R` |
| `https://acp.fullstackeco.com` | **Planned AWS production address** (Cognito sign-in). The move from `mauinui-fm.fullstackeco.com` was committed 2026-10-15. | `docs/architecture.md` lines 76-81; commit "feat(deploy): move production address to acp.fullstackeco.com" (2026-10-15) |
| `https://dev.mauinui-fm.fullstackeco.com` | Development environment. **Do not publish.** | `docs/architecture.md` line 80 |
| `https://d3pjiqknx82e2v.cloudfront.net` | Public **preview** of the ACP user guide (Quarto). Gives no app access. | `docs/documentation-site.md` line 28 |

- **Cutover status is unknown.** The repo has no root README (only `docs/README.md`). The latest
  commits (2026-10-18) release ACP v1.0.2 on AWS, but the docs say cutover needs owner approval and
  that "current AWS state ... come[s] from the operator's private, revision-bound evidence." I could
  not tell from the repo whether the shinyapps address already redirects.
- **The draft uses the plan's URL** (it is the one the plan endorses), with an HTML comment
  `DOFAW TO CONFIRM` on it. Once cutover is done, switch to the permanent address. The old URL keeps
  working as a redirect either way.
- **Hosting and domain:** `acp.fullstackeco.com` is on a domain that belongs to the developer, not to
  the State (`docs/architecture.md`: "The owner retains `fullstackeco.com` registration/renewal
  through Hostinger"). On 2026-09-30 Peter Landon named permanent hosting on a specific server, with
  answers to security questions, as an ACP priority (topic summary). **Question for DOFAW:** will
  the long-term public link be on a hawaii.gov/DLNR domain or alias? Choose the address the site
  publishes so it does not change again.
- **Naming (XP-20):** the plan's URL and the repo still carry "ConservationFootprintManager". The
  page text uses only "Adaptive Conservation Planner"/"ACP"/"Conservation Planner"; the old name
  appears only inside the URL. The AWS address avoids the problem.
- **User guide link:** the CloudFront user guide is public, current, and written for users. The plan
  does not mention it and the address is a preview, so I left it off the page. **Question:** should
  the tools page link to it once it has a permanent address?

## 2. Access and permission questions for DOFAW

1. **How do partners get an account?** Neither the plan nor the docs say. The docs say only "Open
   the application link supplied by your administrator" and that admins create accounts (email,
   role, species point access). The page has a flagged placeholder for the request process and
   contact.
2. **Who is the ACP for?** The plan says it is "the internal, editable interface where DOFAW staff,
   taxon experts, and managers" work and that it is "not a public web map" (line 7364, p.A5-1). The
   user guide says it "is used by internal staff and external conservation partners." Will
   non-DOFAW managers (watershed partnerships, TNC, NPS, Pūlama Lānaʻi and others who had demos)
   get accounts? As read-only users or editors?
3. **Public read-only or guest access?** None exists. If DOFAW wants the public to see footprints,
   the site's own map page and KMZ cover that. Confirm the page wording is right that the public
   cannot sign in.
4. **Sensitive data:** point locations are restricted by a per-group permission. Who approves point
   access (PEPP for plants)? Is a data-sharing agreement or terms of use needed?
5. **Change governance (XP-19):** the page says approved edits become part of the footprint and that
   annual reviews can change PUs. No gatekeeper or change process for post-release edits has been
   agreed (2026-09-30 meeting). Confirm the page does not promise a process that does not exist yet.
6. **Instructional video:** a five-minute DOFAW-produced video linked from the tool's help button was
   agreed on 2026-09-23 (topic summary). It is not in the plan. Embed it here once it exists?

## 3. Screenshots: problems to fix before publishing

All 8 screenshots in `MauiNui-ConservationFootprintManager/docs/site/assets/screenshots/`
(`home`, `app-layout`, `select-footprints`, `map-layers`, `species-layers`, `unit-targets`,
`manage-aux-layers`, `layer-style-modal`) were checked by eye:

- **Old app name.** The header reads "Maui Nui Conservation Footprint Manager" in every image,
  against the ACP naming rule. The app has since been retitled "Adaptive Conservation Planner"
  (changes.md, v1.0).
- **Personal email address.** Every header shows a developer's personal email (the signed-in
  account). The repo's own rule (`docs/documentation-site.md`) is "no real emails." **Recapture all
  8 from the current production app with a neutral demo account, or crop off the header bar.**
- **`manage-aux-layers.png`** shows internal shared-layer names: "AO benefits- ..." (an
  action-*optimization* label, which conflicts with the messaging rules) and "Flagged Plant PUs-
  incomp. species / Low target numbers". Crop to the "Climate resilience" and "Fire risk" rows,
  or recapture.
- **`species-layers.png`** shows known-location dots for Haleakalā silversword (*Argyroxiphium
  sandwicense macrocephalum*) on East Maui. These are coarse at that zoom, but confirm with
  DOFAW/PEPP that rare-plant locations can appear on a public site.
- **`select-footprints.png`** lists "Water Birds" (two words) in the group selector; the messaging
  rule is "Waterbirds". This is minor and is fixed by recapturing from the current app.
- The carousel order and captions in `tools.md` follow the user guide's flow (home → select groups →
  layout → map layers → species → unit targets → context layers → styling). The site's
  `assets/img/screenshots/` folder is empty. Copy the files as `acp-<name>.png` once they are fixed.

## 4. Plan text issues (Appendix 5, pp. A5-1 to A5-4)

- **Tool name inconsistent:** the App 5 introduction (line 7350) says "Find My **Habitat**", but the
  section heading (line 7428) and body say "Find My **Microhabitat**". The site uses Find My
  Microhabitat (it also matches the project tag dictionary).
- **Stray parentheses:** "The Conservation Planner) allows ..." (line 7368) and "The Conservation
  Planner) operationalizes ..." (line 7385).
- **Diacritics:** "kipuka kahuli" (line 7447). The site uses kīpuka kāhuli.
- **Retired terms (XP-22):** App 5 says "modify preventing-extinction status" and "nested footprint
  products (recovery, preventing extinction, implementation subsets)". Outside Terrestrial snails
  the messaging term is priority footprint. The page says "change whether a target is part of the
  priority footprint" and "recovery footprints, priority footprints, and narrower implementation
  subsets"; similarly "conflict detection between recovery and priority footprints". Confirm this
  paraphrase is acceptable.
- **Sections 3-5 are empty:** Potential Recovery Sites, Climate Vectors and Footprint Summarizer have
  headings only (lines 7474-7476). The page lists them as "coming soon" with no descriptions and
  quotes Ch 5f (p.29-30) for what within-unit tools will show. PRS gets a one-line description
  from Ch 6d (line 2234, p.53: "GIS polygon layers showing Potential Recovery Sites based on climate
  suitability and habitat quality"). Ch 6d also mentions "layers showing recent trends in climatic
  change", which may be Climate Vectors. The page does not make that link, because the plan does
  not. **Ask DOFAW for one-line descriptions of Climate Vectors and Footprint Summarizer.**
- **PRS and Microhabitat already in the ACP:** the plan calls PRS "TBA", but the ACP user guide
  (species-layers.qmd) and changes.md (v1.0) show Plant **Microhabitat** and **PRS** polygon
  overlays already enabled in production ("Provider definitions and interpretation ... remain under
  review"). The page follows the plan and does not call PRS available. **Question:** update the
  wording?
- **No link for Find My Microhabitat:** the plan gives no address, and the page says so.
- **Annual work plans:** the brief asked for "build annual work plans". The plan supports this
  (exec summary line 156, p.v; Ch 3c(ii) line 774, p.13; Terms p.120). App 5 itself does not
  mention work plans, and no ACP feature is specifically for building a work plan. The page frames
  this as using the ACP's views, narrowing and exports to plan the year's work. It gives the plant
  narrowing example only in words, because Ch 5e / Table 4 are built on the superseded 155-PU
  priority footprint (XP-05).

## 5. Glossary notes

- **All 28 plan terms are included.** Light edits:
  - Term labels: "Adaptive Conservation Planner (Conservation Planner)" became "(ACP)" with
    "Conservation Planner" as an alias; "Priority Threat Management" became "... (PTM)"; "Chapter 195D
    of the Hawaiʻi Revised Statutes" became "Chapter 195D, Hawaiʻi Revised Statutes"; "...
    (TFE-SCP) Process" lost the trailing "Process".
  - Group names capitalized per the messaging rules (Plants, Terrestrial arthropods, ...). Team
    names in the Taxonomic Team entry were rewritten as "forest bird, seabird, ... teams" (team =
    people).
  - "Terrestrial Plant recovery footprint" became "Plants recovery footprint". "(modified)" became
    "modified". "denoted" became "shown as".
  - Spatial Prioritization: the plan's "The comprehensive planning process—implemented through the
    TFE-SCP process" became "The planning effort, implemented through the TFE-SCP process". This
    removes the circular wording and keeps "comprehensive planning process" for TFE-SCP, as the
    messaging rules require.
- **XP-05 in the glossary:** the plan's Priority Footprint entry (line 4857) gives the plant example
  "317 planning units include a priority footprint of 155". The final plant priority footprint is
  181 PUs (App 1 line 5149; release candidate). I kept the plan's figure as the rules require.
  **DOFAW should update the example to 181 or drop the numbers.**
- **"Hundreds of thousands" of candidate footprints (OptimTFE entry)** is the plan's wording. XP-23
  notes the project record for plants is one million runs. Kept as in the plan.
- **"USGS-developed" (TFE-SCP entry)** and "USGS-led" (Spatial Prioritization Team) are the plan's
  wording and credit by role. They are fine under the DOFAW-voice rule.
- **Missing terms used across the site** (no plan definition, so none were invented; suggest DOFAW
  add them): conservation footprint, biodiversity reserve, kīpuka kāhuli / snail exclosure, PEPP,
  Ecosystem Prioritization Team (the other three effort teams are defined; this one is not),
  Managers' Handbook, imminent extinction / emergency actions, data-deficient species,
  fine-tuning, target richness, interim recovery, Hawaiian hoary bat (ʻōpeʻapeʻa), Watershed
  Partnership, HPPRCC.
- **Tooltip guidance:** generic terms (Recovery, Persistence, Maui Nui, Endangered Species,
  Threatened Species) have no lowercase aliases so tooltips do not fire on every ordinary use.
  Suggest the tooltip script match the first occurrence per page only and skip headings and links.

## 6. References notes

- **49 entries** in plan order. PDF line breaks, page numbers and form feeds were removed. A line
  that ended in an en dash was joined without a space (e.g. "487–500"). Nothing else was changed.
- **URLs:** only the 4 printed in the plan (Kellner & Swihart 2014 DOI, Leopold et al. 2024 DOI, and
  two Maui Forest Bird Recovery Project pages). No DOIs were added, even where they are well known.
- **Appendix 2 has its own "References" list** (lines 5781-5810: Camaclang, Carwardine, Hemming,
  Joseph, Kehoe), in a different style. All five also appear in Literature Cited. Not duplicated.
- **In-text citations that do not match Literature Cited** (for DOFAW's plan errata):
  - "Camaclang et al. 2020" (line 5379), but the list has 2021.
  - "Kehoe et al. 2020" (line 5379; App 2 list line 5807), but the list has 2021.
  - "Elinga et al. 2001" (line 4387) is a typo for Elzinga.
  - "Fortini et al. 2024" / "Berio Fortini et al. 2024" (lines 4970, 4974, 5053, 5100, 5144)
    should be Fortini et al. 2025 (XP-23). "Berio Fortini et al. in prep. b" (line 5149) is listed as
    "Fortini, L. B. ... In prep. b".
  - "Maui Forest Bird Recovery Project 2026" (lines 1431, 1439), but the list has n.d.a / n.d.b.
  - "USFWS 2026" (lines 123, 408) is **missing** from Literature Cited.
  - "Martin et al., 2012" (line 5457) is **missing** from Literature Cited.
- Holthuis 1973 keeps "Hawaii Islands" without the ʻokina because that is the published title.

## 7. Resources page notes

- **Citation:** the plan gives no recommended citation. The suggested one is built from the title
  page (p.i: title, subtitle "Maui, Molokaʻi, Lānaʻi, and Kahoʻolawe", "Hawaiʻi Division of
  Forestry and Wildlife (DOFAW)", "Version September 29, 2026"). The place of publication
  ("Honolulu: Hawaiʻi Department of Land and Natural Resources, Division of Forestry and
  Wildlife") is **not** on the title page. I borrowed it from the plan's own citation of ESRC and
  DOFAW 2024. DOFAW to confirm.
- **Version date:** the title page says September 29, 2026, while the file name says 9-30-2026. The
  page uses the title-page date and suggests the download name `MNLCP_2026-09-29.pdf`.
- **PDF metadata:** the PDF has an empty Title and Author "Loyal Mehrhoff" (223 pages, about 7.7 MB).
  Suggest setting Title to the plan title, and Author to DOFAW if preferred, before posting.
- **Contact:** the plan names no contact (the only "who to contact" is a generic monitoring
  checklist item, line 8133). A flagged placeholder is on the page.
- **KMZ:** not mentioned in the plan. The file is
  `all_taxon_footprints/data/Maui_Nui_Conservation_Footprints.kmz` (about 1 MB, 2026-09-28). The
  worklog says it was rebuilt from the 2026-09-25 release-candidate footprints and shows
  **recovery footprints only** (no priority footprints). Recovery mega-footprint PU totals match
  the plan (492), but per-group plant priority figures in the plan text do not (XP-05). The page
  avoids numbers for the KMZ. **DOFAW to approve posting it**, and decide whether to add a priority
  footprint layer.
- **Related plans:** only plans the MNLCP names are listed (recovery plans, SWAP, site management
  plans, HPPRCC recovery goals, species status assessments/recovery strategies/action plans, bat
  guidance and 5-year review, HIGAP, Managers' Handbook). The plan gives **no URLs** for any of
  them, so none were added. Suggest DOFAW supply official links (e.g. the DLNR SWAP page, the USFWS
  recovery plan listings).
- The Resources page links to `footprints.html`, `tools.html` and `glossary.html` per the site map.

## 8. Other tools in `SO_web_tools.txt`: not published

None of these are named or endorsed in the plan for partner or public use. All are internal,
draft or development tools (mostly on `rconnect.usgs.gov`, which also conflicts with the DOFAW-voice
rule). They are left off the site:

- Fine-tuning tool instructions and fine-tuning plans (Google Docs). Internal; the second is marked
  "for our internal use/development".
- Megafootprint map (`rconnect.usgs.gov/Maui_Nui_Conservation_Footprints_Map`) and app
  (`.../Maui_Nui_Conservation_Footprints_App/`). Labeled "draft plant footprint". The site's own
  map page replaces them. **Question:** does DOFAW want a public footprint web map beyond the site
  map? If so, it may need USGS software-release approval (tag dictionary).
- Criteria web map, integrated spatial and action results, expert feedback portal, and per-group
  trade-off explorers, suboptimal-PU tools, snail setting apps, footprint revision tools, and the
  accessibility map. These are process tools from the planning phase. Several use "optimization"
  in their names.
- "Final SO map" (`icculus.shinyapps.io/optimTFE-footprint/`). Marked "NEEDS REVISIONS- DO NOT USE".
- "Plant species optimization targets" spreadsheet (Google Sheets). Internal.

## 9. Suggested images

- A simple edit-cycle diagram (Save → Publish → Approve → Accepted, with an annual-review loop). This
  is a new SVG; the placeholder is in `tools.md`.
- Plan **Figure 20** (target richness heat map of the priority footprint, p.83) as a static
  companion to the ACP richness view.
- A two-scale illustration for Find My Microhabitat: a roughly 2 km² planning unit next to an
  outplanting site or exclosure measured in fractions of a hectare (p.A5-3). No figure exists; it
  would need to be made, or a PEPP field photo used.
- Recaptured ACP screenshots (section 3).

## 10. Numbers used (all from the plan)

7 taxonomic groups (p.A5-1); 1,400 planning units of about 2 km² (p.13; Terms p.122); 3 export
formats (p.A5-1); 2 tools available and 3 to come (p.A5-1); 442 at-risk species and 20-year period
(p.iv-v, resources lead). No discrepancies with the tracker affect these.
