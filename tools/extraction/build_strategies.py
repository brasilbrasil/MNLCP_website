import json, sys
src_rows = open(sys.argv[1], encoding="utf-8").read().splitlines()
out = sys.argv[2]

cols = ["B","C"] + [f"S{i}" for i in range(2,28)]
rows = {}
cost = None
for ln in src_rows:
    parts = ln.split()
    if not parts: continue
    if ln.strip().startswith("Total Cost"):
        vals = parts[4:]
        cost = vals
        continue
    if len(parts) > 28 and all(p.isdigit() for p in parts[-28:]):
        nums = parts[-28:]
        name = " ".join(parts[:-28])
        rows[name] = dict(zip(cols, map(int, nums)))
assert len(rows) == 17, rows.keys()
assert cost is not None and len(cost) == 28

gid = {
 "Waterbirds":"waterbirds","Forest Birds":"forest_birds","Seabirds":"seabirds",
 "Yellow-faced bees":"yellow_faced_bees","Picture-winged flies":"picture_winged_flies",
 "Damselflies":"damselflies","Blackburn’s sphinx moth":"blackburns_sphinx_moth",
 "Freshwater snails":"freshwater_snails","Anchialine Pool Shrimp":"anchialine_pool_shrimp",
 "Terrestrial Snails":"terrestrial_snails",
 "Plants Group 1":"plant_group_1","Plants Group 2":"plant_group_2","Plants Group 3":"plant_group_3",
 "Plants Group 4":"plant_group_4","Plants Group 5":"plant_group_5","Plants Group 6":"plant_group_6",
 "Hawaiian hoary bat":"hawaiian_hoary_bat"}
order = ["forest_birds","seabirds","waterbirds","plant_group_1","plant_group_2","plant_group_3",
 "plant_group_4","plant_group_5","plant_group_6","terrestrial_snails","yellow_faced_bees",
 "picture_winged_flies","blackburns_sphinx_moth","damselflies","anchialine_pool_shrimp",
 "freshwater_snails","hawaiian_hoary_bat"]
pv = {gid[k]: v for k, v in rows.items()}

groups_meta = {
 "forest_birds": ("Forest birds","Forest birds",4,None),
 "seabirds": ("Seabirds","Seabirds",3,None),
 "waterbirds": ("Waterbirds","Waterbirds",4,"App 2 Table 1 lists four waterbirds (Anas wyvilliana, Fulica alai, Branta sandvicensis, Himantopus mexicanus knudseni); the plan's fifth at-risk waterbird (gallinule) is not listed (tracker XP-16)."),
 "plant_group_1": ("Plant Group 1 (threatened by invasive invertebrates, invasive vertebrates, feral ungulates and loss of avian pollinators)","Plants",42,"Group size from the plant chapter (plan line 2255, 'Plant Group 1 (n = 42)'). App 2 Appendix Table 1 lists only 34 names for this group (pp.A2-21 to A2-22)."),
 "plant_group_2": ("Plant Group 2 (threatened by invasive invertebrates and feral ungulates)","Plants",23,None),
 "plant_group_3": ("Plant Group 3 (threatened by feral ungulates)","Plants",30,None),
 "plant_group_4": ("Plant Group 4 (threatened by invasive invertebrates, invasive vertebrates and feral ungulates)","Plants",75,"Matches the plant chapter (plan line 2271, 'Plant Group 4 (n = 75)')."),
 "plant_group_5": ("Plant Group 5 (threatened by invasive vertebrates and feral ungulates)","Plants",13,None),
 "plant_group_6": ("Plant Group 6 (long-lived species)","Plants",13,None),
 "terrestrial_snails": ("Terrestrial snails","Terrestrial snails",None,"App 2 Table 1 lists 22 genus-level entries (e.g. Partulina spp., Newcombia spp.), not species; the plan's 49 at-risk snail species are not enumerated in the PTM table."),
 "yellow_faced_bees": ("Yellow-faced bees (Hylaeus)","Terrestrial arthropods",10,None),
 "picture_winged_flies": ("Picture-winged flies (Drosophila)","Terrestrial arthropods",2,None),
 "blackburns_sphinx_moth": ("Blackburn’s sphinx moth","Terrestrial arthropods",1,None),
 "damselflies": ("Damselflies (Megalagrion)","Aquatic invertebrates",5,"Includes Megalagrion jugorum and M. molokaiense, which App 3 lists as Terrestrial arthropods (tracker XP-16)."),
 "anchialine_pool_shrimp": ("Anchialine pool shrimp","Aquatic invertebrates",None,"Listed as a single group entry ('Anchialine pool shrimp') in App 2 Table 1; App 3 lists six shrimp species."),
 "freshwater_snails": ("Freshwater snails (Lymnaeidae)","Aquatic invertebrates",None,"Listed as a single family-level entry ('Lymnaeidae spp.')."),
 "hawaiian_hoary_bat": ("Hawaiian hoary bat (ʻōpeʻapeʻa)","Hawaiian hoary bat",1,None),
}
species_groups = []
for g in order:
    name, tg, n, note = groups_meta[g]
    d = {"id": g, "name": name, "taxon_group": tg, "n_species": n,
         "baseline_persistence_pct": pv[g]["B"], "counterfactual_persistence_pct": pv[g]["C"]}
    if note: d["notes"] = note
    species_groups.append(d)

S = {
 "S1": ("No action (counterfactual)", "No conservation actions are taken; existing ungulate and predator fences are no longer maintained.", []),
 "S2": ("Existing ungulate fences", "Goal: remove ungulates from inside fences to minimize impacts to sensitive species. Maintain existing ungulate fences and remove ungulates within and next to them.", []),
 "S3": ("Future ungulate fences", "Goal: remove ungulates from inside fences to minimize impacts to sensitive species. Build and maintain two new ungulate fences per year and remove ungulates within and next to them.", []),
 "S4": ("Ungulate control outside fences", "Goal: minimize impacts to sensitive species from wild ungulates. Hunting programs, landowner partnerships and incentives, corral traps and aerial shooting where fences will not be built within 20 years.", []),
 "S5": ("Terrestrial habitat management", "Goal: improve habitat for sensitive species. Outplanting and seeding of common native plants, removal of invasive plants, firebreaks, and early response to incipient invasive species.", []),
 "S6": ("Stream / wetland habitat management", "Goal: improve habitat for sensitive species. Stream barrier modification, invasive species removal in streams, wetlands and anchialine ponds, sediment removal, bioshields, hydrology systems, loʻi partnerships and habitat protection.", []),
 "S7": ("Invasive vertebrate predator control", "Goal: minimize impacts to sensitive species from predators. Localized trapping of rodents, cats, mongoose and feral dogs outside predator exclusion fences; cattle egret and barn owl control; cat eradication on Kahoʻolawe; rodent-free islets; a predator control response team.", []),
 "S8": ("Invasive invertebrate pest control", "Goal: minimize impacts to sensitive species from invertebrate pests. Surveys to detect and eradicate or control little fire ants, bighead ants, Argentine ants and western yellowjackets.", []),
 "S9": ("Existing predator exclusion fences", "Goal: minimize impacts to sensitive species from predators. Maintain existing snail and seabird predator exclusion fences, seabird translocation and social attraction, rare invertebrate translocation, weed removal, and snail soft-release boxes.", []),
 "S10": ("Future predator exclusion fences", "Goal: minimize impacts to sensitive species from predators. New predator exclusion fences for snails, seabirds and waterbirds, cat-proof fences for waterbirds, and translocations into new fences.", []),
 "S11": ("Landscape-scale rodent suppression", "Goal: minimize impacts to sensitive species from rodents. Rodent eradication on Kahoʻolawe and regional aerial rodenticide on Maui, Lānaʻi and Molokaʻi. Does not include cats or mongoose.", []),
 "S12": ("Existing tools for rare plants & invertebrates", "Goal: increase populations of rare plants and invertebrates. Outplanting rare plants, maintaining existing propagation and plant pathology facilities, artificial insect habitat, and arthropod reintroduction.", []),
 "S13": ("Future tools for rare plants & invertebrates", "Goal: increase populations of rare plants and invertebrates. Cryopreservation, genomics, tissue culture and pollen storage research; new propagation facilities on Maui, Molokaʻi and Lānaʻi; methods to control invasive pests such as naio thrips, slugs, black twig borer and coconut rhinoceros beetle.", []),
 "S14": ("Avian disease prevention", "Goal: prevent the spread of avian diseases. Maintain and expand forest bird breeding facilities, translocate ʻākohekohe and ʻalauahio to disease-safe habitat, Wolbachia IIT mosquito releases, BTI larvicide, and an avian botulism response network.", []),
 "S15": ("Future tools for avian malaria", "Goal: prevent the spread of avian malaria. A preventative vaccine or probiotic for forest birds, and genetically engineered mosquitoes developed with partners outside Hawaiʻi.", []),
 "S16": ("Modification & minimization of infrastructure", "Goal: reduce impacts to native birds from energy infrastructure and car strikes. Lighting legislation and outreach, powerline diverters, wind turbine modification, speed bumps in Haleakalā, roadside management, and Habitat Conservation Plan staffing.", []),
 "S17": ("Vertebrate health recovery & rehabilitation", "Goal: recover downed and injured wildlife. Support for the Hawaiʻi Wildlife Center and satellite rehabilitation facilities on Maui and Molokaʻi.", []),
 "S18": ("Current tools", "Combination of existing (current) management tools.", ["S2","S4","S5","S6","S7","S9","S12","S14"]),
 "S19": ("Existing ungulate control", "Combination.", ["S2","S4"]),
 "S20": ("Existing & future ungulate control", "Combination.", ["S2","S3","S4"]),
 "S21": ("Existing ungulate control + existing predator control", "Combination.", ["S2","S4","S7","S9"]),
 "S22": ("Existing & future ungulate control + existing & future predator control", "Combination.", ["S2","S3","S4","S7","S9","S10","S11"]),
 "S23": ("Existing & future ungulate control + existing & future predator control + invertebrate pest control", "Combination.", ["S2","S3","S4","S7","S8","S9","S10","S11"]),
 "S24": ("Existing ungulate control + existing predator control + habitat management + invertebrate pest control + existing tools for rare plants & invertebrates", "Combination.", ["S2","S4","S5","S6","S7","S8","S9","S12"]),
 "S25": ("Plant- and invertebrate-focused combination (existing & future ungulate control + existing & future predator control + invertebrate pest control + habitat management + existing & future tools for rare plants & invertebrates)", "One of the two combinations the MNLCP selects. A 'kitchen sink' approach addressing all major threats to plants and invertebrates.", ["S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]),
 "S26": ("Existing ungulate control + existing predator control + habitat management + invertebrate pest control + avian disease prevention", "Combination.", ["S2","S4","S5","S6","S7","S8","S9","S14"]),
 "S27": ("Bird- and bat-focused combination (existing & future ungulate control + existing & future predator control + invertebrate pest control + habitat management + avian disease prevention + future tools for avian malaria + infrastructure modification + vertebrate rehabilitation)", "One of the two combinations the MNLCP selects. A 'kitchen sink' approach addressing all major threats to vertebrates.", ["S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S14","S15","S16","S17"]),
}
notes = {
 "S1": "Counterfactual. Table 26 (Ch 6j) labels this column 'S1 No Actions'; App 2 Table 1 labels it 'C'. Values here are the counterfactual persistence, not a benefit.",
 "S10": "App 2 Table 2 S10 lists 20 seabird and 20 waterbird fences; the App 2 Figure 6b cost breakdown lists 20 snail exclosures, 20 seabird and 14 waterbird predator fences.",
 "S11": "Does not include cats or mongoose because aerial rodenticide regulations for them have not been developed for Hawaiʻi (App 2 Discussion).",
 "S13": "Ranked in the top three single strategies for 13 of 17 species groups, the single most important individual action (Ch 6j, Table 27).",
 "S15": "Gene drives were excluded from the formal process (App 2 Discussion); this strategy refers to genetically engineered mosquitoes developed with partners outside Hawaiʻi.",
 "S25": "Components per App 2 Table 2 and Ch 5d Table 3 (S2-S13). Ch 6j Table 25 does not mark S10 in the S25 column (checked on rendered PDF p.85); treat as a table error to confirm with DOFAW. Average annual cost ~$45M per year (App 2 p.A2-10).",
 "S26": "App 2 Table 2 strategy name includes 'Invertebrate Pest Control' but its component list omits S8; Ch 6j Table 25 marks S8 in S26. S8 is included here following Table 25 and the strategy name.",
 "S27": "Plan calls S27 'bird-focused' (Ch 5d, Table 25), 'bird- and bat-focused' (Executive Summary) and focused 'on birds and the bat' (Table 3 caption). Average annual cost ~$40M per year (App 2 p.A2-10).",
 "S18": "Named 'Current Tools' in App 2 Table 2.",
}
strategies = []
for i in range(1, 28):
    sid = f"S{i}"
    name, desc, comps = S[sid]
    key = "C" if sid == "S1" else sid
    c = cost[cols.index(key)]
    ct = None if c == "-" else int(c)
    vals = {g: pv[g][key] for g in order}
    above = [g for g in order if vals[g] >= 50]
    strategies.append({
        "id": sid, "name": name,
        "type": "single" if i <= 17 else "combination",
        "components": comps,
        "description": desc,
        "cost_total": ct,
        "cost_annual": None if ct is None else round(ct/20, 2),
        "cost_units": "cost_total: total cost over the 20-year planning period, millions of US dollars (App 2 Table 1, 'Total Cost (M $)'). cost_annual: cost_total divided by 20, millions of US dollars per year; derived for the explorer, not printed in the plan (the plan gives only approximate annual figures, e.g. ~$45M/yr for S25 and ~$40M/yr for S27).",
        "feasibility": None,
        "benefit_by_group": vals,
        "groups_above_threshold": above,
        "in_mnlcp_selection": sid in S["S25"][2] + S["S27"][2] + ["S25","S27"],
        "notes": notes.get(sid),
    })

for st in strategies:
    if st["type"] == "combination":
        names = "; ".join(f"{c} {S[c][0]}" for c in st["components"])
        base = "" if st["description"] in ("Combination.", "Combination of existing (current) management tools.") else st["description"] + " "
        st["description"] = base + "Combines: " + names + "."
# actions list
A = []
def a(s, n, action, target=None, timeline=None):
    A.append({"strategy": s, "number": n, "action": action, "target": target, "timeline": timeline})

a("S1",None,"No conservation actions are taken; existing ungulate and predator fences are no longer maintained.","All species groups (counterfactual scenario)","20-year planning period")
a("S2",1,"Conduct maintenance checks twice per year and after major storm events on existing ungulate fences that are complete or will be complete by Dec. 2023 (see M2 map). Perform maintenance as needed, including repairing, replacing, or retrofitting/improving fence design, and fence-corridor vegetation removal.","Existing ungulate fences across Maui Nui","Twice per year and after major storms")
a("S2",2,"Conduct ungulate control via trapping or aerial shooting within and adjacent to existing fences (see M2 map). Deploy snares and snare warning signs along fencelines to minimize incursions and remove animals that enter fenced areas. Maintain and check traps next to fences with high ungulate activity.","Areas within and adjacent to existing ungulate fences","Ongoing")
a("S3",1,"Build and maintain two new ungulate fences per year across Maui Nui (see M3 map) that are not yet funded and not under construction. Conduct maintenance checks twice per year and after major storm events; repair, replace, or retrofit fences as needed and remove fence-corridor vegetation.","New ungulate fences across Maui Nui","Two new fences per year; checks twice per year and after major storms")
a("S3",2,"Conduct ungulate control via trapping or aerial shooting within and adjacent to newly built fences (see M3 map). Deploy snares and warning signs along fencelines; maintain and check traps next to fences with high ungulate activity.","Areas within and adjacent to new ungulate fences","Ongoing")
a("S4",1,"Conduct education and outreach on management of wild ungulates on private lands.","Private lands",None)
a("S4",2,"Work with private landowners to create new ungulate control units to increase hunting opportunities on private lands.","Private lands",None)
a("S4",3,"Continue to promote public hunting through hunter training courses, the \"Go Hunt Hawaiʻi\" website and newsletter, and road access maintenance. Evaluate permits issued, animals removed, population numbers and vital rates using hunter, camera trap and/or drone data, and revise bag limits and seasons as needed.","Public hunting program","Ongoing")
a("S4",4,"Issue permits for commercial wildlife removal services.","Commercial wildlife removal services",None)
a("S4",5,"Create a landowner incentive program that pays private landowners based on the number of animals removed (deer tails) to encourage access, hunting, and removal of axis deer. Funds are capped at 10% of land acreage for lands over 1,500 acres and at 100 animals for lands under 1,500 acres.","Private landowners; axis deer",None)
a("S4",6,"Create an ungulate control implementation guide for private and public landowners, including zones for ungulate tolerance (zero-tolerance areas, public hunting areas, other lands) based on carrying capacity and land designation goals.","Private and public landowners",None)
a("S4",7,"Deploy and maintain corral traps to remove ungulates outside ungulate fences where fences will not be built within the next 20 years but immediate ungulate control is needed (see M4 map).","Unfenced areas needing immediate ungulate control","Areas without fences planned within 20 years")
a("S4",8,"Conduct aerial shooting 6-12 hours per week outside ungulate fences within designated shoot zones where fences will not be built within the next 20 years but immediate ungulate control is needed (see M4 map).","Designated shoot zones outside fences","6-12 hours per week")
for n, txt in [(1,"Outplant non-coastal matrix (common) plants and seeds from propagation or the wild"),
               (2,"High-volume broadcast seeding of non-coastal matrix plants"),
               (3,"Remove invasive localized monoculture stands (e.g., strawberry guava)"),
               (4,"Remove invasive grasses (biofuel)"),
               (5,"Remove invasive understory shrubs and herbs"),
               (6,"Remove invasive canopy species")]:
    a("S5",n,txt+" across Maui Nui within currently known habitat for sensitive species, and habitat being prepared for them, in areas without predator exclusion fences (see M5 map).","Known and prepared habitat for sensitive species outside predator exclusion fences",None)
a("S5",7,"Create firebreaks (fuel breaks and/or 'green' breaks) in areas across Maui Nui with a high risk of wildfire that have at-risk species, and in adjacent areas.","High wildfire-risk areas with or next to at-risk species",None)
a("S5",8,"Identify and address incipient or potentially explosive populations of invasive species (e.g., pines, albizia, African tulip) in currently known habitat for sensitive species and habitat being prepared for them (see M5 map).","Known and prepared habitat for sensitive species",None)
a("S6",1,"Modify stream barriers/diversions in East Maui where stream flow is reduced and lateral entrainment is possible (see M6 Map 1).","East Maui streams",None)
a("S6",2,"Remove invasive species from lowland streams below 1,200 ft across Maui Nui, with continuous monitoring to keep streams free of invasive species (see M6 Map 1).","Lowland streams below 1,200 ft","Continuous monitoring")
a("S6",3,"Remove invasive plants in wetland habitats outside predator exclusion fences that provide essential habitat for the entire life cycle of native waterbirds (see M6 map).","Waterbird wetlands outside predator exclusion fences",None)
a("S6",4,"Identify and remove sediment from wetlands with high sediment accumulation that affects the natural flow of water in critical waterbird habitat (see M6 Map 2).","Critical waterbird wetlands",None)
a("S6",5,"Create forested bioshields around critical waterbird habitat across Maui Nui (see M6 Map 2).","Critical waterbird habitat",None)
a("S6",6,"Identify and protect (through planning, zoning or other mechanisms) future waterbird habitat from urban development and climate change impacts.","Future waterbird habitat",None)
a("S6",7,"Build pumping and diking systems for wetlands and drill new wells to extract groundwater, monitor salinity, and maintain hydrological conditions that avoid or minimize disease outbreaks (e.g., botulism) in critical waterbird habitat (see M6 Map 2).","Critical waterbird wetlands",None)
a("S6",8,"Support restoration and management of loʻi for waterbird habitat, sustainable food and ecosystem services through partnerships with loʻi farmers.","Loʻi (taro fields) and farmers",None)
a("S6",9,"Protect anchialine ponds across Maui Nui (see M6 Map 3) by including them in protected areas or precluding development through zoning or other means, and remove invasive species from them.","Anchialine ponds",None)
a("S7",1,"Perform localized removal of invasive rodents in known and prepared habitat for sensitive species without a predator exclusion fence (see M7 map). Deploy A24 traps and tracking tunnels, check them every 3 months, establish two new trap grids each year, and monitor efficacy continuously.","Sensitive species habitat without predator exclusion fences","Checks every 3 months; two new trap grids per year")
a("S7",2,"Trap and remove feral dogs on state, federal and private lands managed for sensitive species (see M7 map) when feral dogs become an issue.","Lands managed for sensitive species","As needed")
a("S7",3,"Use a combination of trapping methods (A24, DOC250, Timms and leg-hold traps) to remove invasive rats, cats and mongoose locally on Maui, Molokaʻi and Lānaʻi in sensitive species habitat without a predator exclusion fence; establish one new trap site each year and check traps for one week every other week. Eradicate cats from Kahoʻolawe using trapping and pesticides (see M7 map).","Maui, Molokaʻi and Lānaʻi sensitive species habitat; Kahoʻolawe (cats)","One new trap site per year; checks one week every other week")
a("S7",4,"Control cattle egrets as roosts are identified in wetlands managed for seabirds and waterbirds (see M7 map).","Wetlands managed for seabirds and waterbirds","As roosts are identified")
a("S7",5,"Control barn owls as individuals are identified in areas managed for sensitive species (see M7 map).","Areas managed for sensitive species","As individuals are identified")
a("S7",6,"Maintain rodent-free offshore islets by conducting annual trapping surveys for one week, checking traps every 2 days.","Offshore islets","Annually")
a("S7",7,"Create a predator control response team to provide technical assistance and trapping support for private landowners, nonprofits and farmers.","Private landowners, nonprofits and farmers",None)
for n, pest, verb in [(1,"little fire ants","detect and eradicate"),(2,"bighead ants","detect and control"),(3,"Argentine ants","detect and control"),(4,"western yellowjackets","detect and control")]:
    a("S8",n,f"Survey sensitive species habitat across Maui Nui (see M8 map), and habitat being prepared for sensitive species, to {verb} {pest}.","Known and prepared sensitive species habitat",None)
a("S9",1,"Maintain existing predator exclusion fences for snails that are complete or will be complete by Dec. 2023 (see M9 map): yearly maintenance and repair, fence-corridor vegetation removal, and traps and bait boxes for rats, mice, mongoose and cats inside the fences.","Existing snail predator exclusion fences","Yearly")
a("S9",2,"Maintain existing predator exclusion fences for seabirds that are complete or will be complete by Dec. 2023 (see M9 map): yearly maintenance and repair, fence-corridor vegetation removal, and traps and bait boxes for rats, mice, mongoose and cats inside the fences.","Existing seabird predator exclusion fences","Yearly")
a("S9",3,"Translocate seabird chicks into existing seabird fences (see M9 map) and conduct yearly surveys of recruitment.","Existing seabird fences","Yearly surveys")
a("S9",4,"Use social attraction equipment to encourage adult seabirds to nest inside existing seabird fences (see M9 map), with yearly surveys of recruitment.","Existing seabird fences","Yearly surveys")
a("S9",5,"Translocate rare invertebrates into existing predator exclusion fences (see M9 map) and conduct yearly surveys of recruitment.","Existing predator exclusion fences","Yearly surveys")
a("S9",6,"Remove invasive plants inside existing predator exclusion fences (see M9 map) when identified and replace them with common native plants.","Existing predator exclusion fences","As identified")
a("S9",7,"Construct and deploy soft-release snail boxes/grow boxes in unpopulated snail exclosures that need regular maintenance.","Unpopulated snail exclosures",None)
a("S10",1,"Build and maintain 4 new predator exclusion fences per year for snails within the next 5 years (20 fences total), each about 1/4-1/2 acre, with yearly maintenance, fence-corridor vegetation removal, and traps and bait boxes for rats, mice, mongoose and cats inside the fences.","Terrestrial snails (kīpuka kāhuli exclosures)","4 per year for 5 years (20 total)")
a("S10",2,"Build and maintain two new predator exclusion fences per year for seabirds within the next ten years (20 fences total), each supporting 500 adult nesting seabirds, with yearly maintenance and traps and bait boxes inside.","Seabirds","2 per year for 10 years (20 total)")
a("S10",3,"Build and maintain two new predator exclusion fences per year for waterbirds within the next ten years (20 fences total), with yearly maintenance and traps and bait boxes inside.","Waterbirds","2 per year for 10 years (20 total)")
a("S10",4,"Build and maintain new cat-proof (but not rodent-proof) fences for waterbirds in habitats where feral cats are the main predators and/or full predator exclusion fences are hard to build.","Waterbirds","Complete within 10 years")
a("S10",5,"Translocate rare invertebrates into newly built predator exclusion fences and conduct yearly surveys of recruitment.","New predator exclusion fences","Yearly surveys")
a("S10",6,"Remove invasive plants inside newly built predator exclusion fences when identified and replace them with common native plants.","New predator exclusion fences","As identified")
a("S11",1,"Eradicate rodents (rats and mice) on the entire island of Kahoʻolawe (see M11 map).","Kahoʻolawe",None)
a("S11",2,"Suppress rats regionally at landscape scale on Maui, Lānaʻi and Molokaʻi by deploying aerial rodenticide once per year in remote, hard-to-access areas outside predator exclusion fences, away from urban areas, managed for sensitive species, and where localized predator control is under way (see M11 map).","Remote sensitive species areas on Maui, Lānaʻi and Molokaʻi","Once per year")
a("S12",1,"Outplant rare plants and seeds from propagation or the wild (see M12 map) inside ungulate-free areas (ungulate fences or areas ungulates cannot reach) and unfenced coastal areas, outside predator exclusion fences.","Ungulate-free areas and unfenced coastal areas",None)
a("S12",3,"Maintain captive plant propagation facilities built by Dec 31, 2023.","Existing plant propagation facilities","Ongoing")
a("S12",4,"Maintain existing plant pathology diagnostic facilities built by Dec 31, 2023.","Existing plant pathology facilities","Ongoing")
a("S12",5,"Maintain captive invertebrate propagation facilities built on Oʻahu by Dec 31, 2023.","Existing invertebrate propagation facilities (Oʻahu)","Ongoing")
a("S12",6,"Create and maintain artificial habitat for insects (e.g., bee blocks, pond liners) outside predator exclusion fences in areas that provide habitat for rare insects (see M12 map).","Rare insect habitat",None)
a("S12",7,"Reintroduce arthropods outside predator exclusion fences in dry forest and coastal habitats up to 2,000 ft.","Dry forest and coastal habitats up to 2,000 ft",None)
a("S13",1,"Develop cryopreservation techniques to preserve rare plants at a university in Hawaiʻi.","Rare plants",None)
a("S13",2,"Develop cryopreservation techniques to preserve rare invertebrates at a university in Hawaiʻi.","Rare invertebrates",None)
a("S13",3,"Conduct genomics research to develop genetic bar-code readers and examine phylogenetics for rare plants and invertebrates at a university in Hawaiʻi.","Rare plants and invertebrates",None)
a("S13",4,"Conduct research to improve plant tissue culture techniques to maintain or grow plant cells at a university in Hawaiʻi.","Rare plants",None)
a("S13",5,"Develop pollination and pollen storage techniques for rare plants at a university in Hawaiʻi.","Rare plants",None)
a("S13",6,"Build and maintain one captive invertebrate propagation facility on Maui.","Rare invertebrates (Maui)","By Dec 31, 2025")
a("S13",7,"Build and maintain one rare plant propagation facility on Maui, Molokaʻi and Lānaʻi.","Rare plants (Maui, Molokaʻi, Lānaʻi)","By Dec 31, 2025")
a("S13",8,"Develop effective methods to control invasive pests (e.g., naio thrips, slugs, black twig borers and coconut rhinoceros beetles).","Rare plants",None)
a("S14",1,"Maintain existing captive forest bird breeding facilities built by Dec 31, 2023.","Forest birds","Ongoing")
a("S14",2,"Translocate 50 pairs of ʻākohekohe and ʻalauahio from habitats within Maui Nui (see M14 Maps 1 and 2) into forest bird habitat safe from avian disease on other Hawaiian Islands.","ʻĀkohekohe and ʻalauahio",None)
a("S14",2,"Continue to release Wolbachia IIT mosquitoes (or SIT in the future) in locations identified by the East Maui environmental assessment (see M14 Map 3).","Forest bird habitat (East Maui)","Ongoing")
a("S14",3,"Expand existing forest bird breeding facilities on land already owned by the state.","Forest birds","Within 10 years")
a("S14",4,"Aerially broadcast BTI in streams near forest bird habitat where mosquitoes are breeding (see M14 Map 3).","Streams near forest bird habitat",None)
a("S14",5,"Create a response network to survey and remove bird carcasses in wetlands and report potential outbreaks of avian botulism.","Wetland birds",None)
a("S15",1,"Administer a one-time preventative vaccine or probiotic to forest birds across their current ranges (see M15 Maps 1-3) to prevent the spread of avian malaria.","Forest birds","One-time")
a("S15",2,"Collaborate with partners outside Hawaiʻi to develop genetically engineered mosquitoes (via gene drive or GMO); release them in critical forest bird habitat on Maui (see M15 Map 4), or perform island-wide population replacement if regional suppression does not work.","Critical forest bird habitat on Maui",None)
a("S16",1,"Draft and introduce state-wide legislation to reduce anthropogenic lighting from all state-owned facilities (streetlights, buildings, schools, etc.), including in Maui Nui; after passage, hire contractors to assess and plan for all state buildings in Maui Nui.","State-owned facilities",None)
a("S16",2,"Advocate and conduct outreach for reduced lighting at county, federal, state and commercial facilities across Maui Nui.","County, federal, state and commercial facilities",None)
a("S16",3,"Conduct public outreach to reduce lighting in residential areas across Maui Nui; educate the public about lighting impacts on birds and bats through flyers; work with vendors to offer products at reasonable cost.","Residents of Maui Nui",None)
a("S16",4,"Work with Hawaiian Electric Company to construct diverters that minimize take of waterbirds and seabirds from powerline collisions in areas designated by the Habitat Conservation Plan and all areas where T&E species may be affected (see M16 Map 1).","Powerlines",None)
a("S16",5,"Work with wind energy companies to modify wind turbines to reduce avian collisions in areas designated by the Habitat Conservation Plan.","Wind turbines",None)
a("S16",6,"Construct speed bumps within Haleakalā to minimize car strikes to seabirds and nēnē (see M16 Maps 2 and 3); monitor efficacy every year for three years, then every three years. Work with the Department of Transportation to change roadside management so it attracts fewer nēnē.","Haleakalā roads; seabirds and nēnē","Annual monitoring for 3 years, then every 3 years")
a("S16",7,"Conduct community outreach about car strikes/roadkill in residential and commercial areas; educate the public on not feeding wildlife; work with the Department of Transportation to reduce appealing roadside habitat for sensitive bird species.","Communities across Maui Nui",None)
a("S16",8,"Dedicate staffing for reviewing and updating existing Habitat Conservation Plans.","Habitat Conservation Plans",None)
a("S17",1,"Provide financial support to the Hawaiʻi Wildlife Center on Hawaiʻi Island for transporting and rehabilitating injured birds from Maui Nui.","Injured birds",None)
a("S17",2,"Construct satellite rehabilitation facilities on Maui and Molokaʻi to provide temporary facilities for examining and stabilizing downed or injured birds.","Downed or injured birds (Maui, Molokaʻi)",None)

maxima = {g: max(v for k, v in pv[g].items() if k not in ("B",)) for g in order}
best = {g: [k for k, v in pv[g].items() if k not in ("B","C") and v == maxima[g]] for g in order}
never = [g for g in order if maxima[g] < 50]
both = {g: max(pv[g]["S25"], pv[g]["S27"]) for g in order}

data = {
 "_source": "Maui Nui Landscape Conservation Plan (DOFAW, version 2026-09-29), plan .txt lines 1088-1224 (Ch 5d, pp.22-26, Table 3, Figure 3), 3313-3528 (Ch 6j, pp.84-87, Tables 25-27), 5278-6587 (Appendix 2, pp.A2-1 to A2-41: Table 1 persistence and cost, Table 2 strategies and actions, Appendix Table 1 species groups, Figures 5-6 and Appendix Figures 1-3). Group species counts were counted from App 2 Appendix Table 1 on the rendered PDF (pp.A2-19 to A2-27). Persistence values checked against the rendered PDF (Table 26, p.85).",
 "value_definitions": {
   "benefit_by_group": "Expected probability of persistence (percent) of the species group over 20 years under the strategy: best-guess expert estimate, adjusted for feasibility, computed as counterfactual persistence + (benefit x feasibility) (App 2 Equation 3; App 2 Table 1 and Ch 6j Table 26). It is a persistence level, not the gain over no action. For S1 it is the counterfactual (no action) persistence.",
   "baseline_persistence_pct": "Persistence under current management only ('B' baseline in App 2 Table 1; 'C Only Current Actions' in Ch 6j Table 26).",
   "counterfactual_persistence_pct": "Persistence with no management action ('C' counterfactual in App 2 Table 1; 'S1 No Actions' in Table 26).",
   "groups_above_threshold": "Species groups with persistence of 50 percent or more under the strategy (the MNLCP target; values of exactly 50 are shaded as meeting it in Table 26).",
   "feasibility": "Strategy feasibility (average of action implementation probability x success probability). Not reported per strategy in the plan, so null.",
   "n_species": "Number of species in the group: count of names in App 2 Appendix Table 1 (pp.A2-19 to A2-27), except Plant Group 1, which uses the plant chapter's n = 42 (plan lines 2255-2279 give n for all six plant groups). Null where the table lists genera or a single group entry instead of species. The plan's total of 374 PTM species cannot be reproduced from the table."
 },
 "species_groups": species_groups,
 "strategies": strategies,
 "results_summary": {
   "persistence_target_pct": 50,
   "persistence_definition": "Probability that a species group has viable, self-sustaining populations over a 20-year period (Ch 5d p.23; App 2 p.A2-6).",
   "planning_period_years": 20,
   "n_species_ptm": 374,
   "n_species_groups": 17,
   "n_strategies": 27, "n_single": 17, "n_combination": 10,
   "experts_participating": "about 100 land managers and scientists in workshops and focus groups, August 2022 - March 2023; 40 experts provided persistence estimates (App 2 pp.A2-4, A2-6; Ch 3d p.13)",
   "selected_strategies": ["S25", "S27"],
   "selected_rationale": "No single strategy reaches 50 percent for every group. S25 and S27 together come closest, are the only combinations that include S3, S5 and S6, and together implement all 17 single strategies (Ch 5d pp.23-24, Table 3; Ch 6j p.84).",
   "max_persistence_by_group": maxima,
   "best_strategy_by_group": best,
   "max_of_S25_S27_by_group": both,
   "groups_never_reaching_target": never,
   "groups_never_reaching_target_note": "Seven groups (all six plant subgroups and freshwater snails) do not reach 50 percent under any strategy after feasibility adjustment (Table 26 caption p.85; Ch 6j p.84).",
   "most_important_single_strategy": {"id": "S13", "groups_with_in_top_three": 13, "source": "Ch 6j p.86, Table 27 p.87"},
   "top_three_single_strategies_count": {"S2":0,"S3":5,"S4":0,"S5":4,"S6":3,"S7":6,"S8":7,"S9":0,"S10":3,"S11":4,"S12":3,"S13":13,"S14":1,"S15":1,"S16":1,"S17":0, "_note": "Number of species groups ranking each strategy in their top three (Table 27, 'Groups selecting' row, p.87). Plant Group 4 lists rank 3 twice (S3 and S13)."},
   "groups_reaching_target_without_future_tools": ["seabirds", "waterbirds", "hawaiian_hoary_bat"],
   "costs": {
     "all_species_average_annual_musd": 55,
     "all_species_average_annual_note": "~$55M per year on average to get all 17 groups to at least 40 percent persistence by considering complementarity across all groups (App 2 pp.A2-10 to A2-11, Figure 5). The App 2 abstract also cites 'average annual cost of $26M' in connection with efficiencies from management collaboration, without saying what it covers; the Discussion gives ~$53M per year to maintain fences and facilities and implement landscape-scale actions (App 2 pp.A2-1, A2-16). Unreconciled; see notes.",
     "upfront_nonrecurring_musd": 67,
     "upfront_nonrecurring_breakdown_pct": {"Ungulate and predator fences (20 snail exclosures, 20 seabird predator fences, 14 waterbird predator fences, 30 miles of ungulate fencing)": 44, "Field vehicles": 17, "Kahoʻolawe predator eradication": 16, "Disease R&D": 13, "Propagation and rehabilitation facilities": 9, "Policy development": 1},
     "upfront_note": "Read from App 2 Figure 6b (p.A2-13). Year one carries most non-recurring costs; fence construction continues in years 2-10 and field vehicles are replaced in years 11 and 16.",
     "recurring_annual_musd": 53,
     "recurring_breakdown_pct": {"Salaries": 56, "Materials": 44},
     "complementarity_savings_annual_musd": 10,
     "by_taxonomic_set": [
       {"set": "Vertebrates (forest birds, seabirds, waterbirds, bat)", "threshold_pct": 50, "strategy": "S27", "annual_cost_musd": 40, "note": "All four vertebrate groups secured at >50% for ~$40M per year (App 2 p.A2-10, Appendix Figure 1)."},
       {"set": "Invertebrates (7 groups)", "threshold_pct": 40, "strategy": "S27", "annual_cost_musd": 40, "note": "All invertebrate groups secured at >40% for ~$40M per year (App 2 p.A2-10, Appendix Figure 2)."},
       {"set": "Plants (6 groups)", "threshold_pct": 40, "strategy": "S25", "annual_cost_musd": 45, "note": "S25 is the only strategy that gets any plant group to 40% (App 2 p.A2-10, Appendix Figure 3)."},
       {"set": "All 17 groups", "threshold_pct": 40, "strategy": "S25 + S27", "annual_cost_musd": 55, "note": "App 2 p.A2-11, Figure 5."}
     ]
   },
   "cost_curve_all_groups_40pct": {
     "_note": "Steps read from App 2 Figure 5 (p.A2-12); annual costs are approximate visual readings of the chart, not printed values.",
     "steps": [
       {"strategies": "Counterfactual", "groups_secured": 0},
       {"strategies": "S17", "groups_secured": 1},
       {"strategies": "S2", "groups_secured": 2},
       {"strategies": "S2 + S6", "groups_secured": 3},
       {"strategies": "S13", "groups_secured": 5},
       {"strategies": "S6 + S13", "groups_secured": 6},
       {"strategies": "S6 + S7 + S13", "groups_secured": 8},
       {"strategies": "S6 + S23", "groups_secured": 9},
       {"strategies": "S27", "groups_secured": 11},
       {"strategies": "S25", "groups_secured": 16},
       {"strategies": "S25 + S27", "groups_secured": 17}
     ]
   },
   "uncertainty": "Using experts' most pessimistic estimates, all groups can be secured only at a >30% threshold; using the most optimistic, at >60% (App 2 p.A2-14). S7 (predator control outside fences) may harm terrestrial snails where predatory Euglandina snails are present, because rodents prey on Euglandina (App 2 pp.A2-14, A2-16)."
 },
 "actions_list": A,
}
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("groups", len(species_groups), "strategies", len(strategies), "actions", len(A))
print("never", never)
for s in strategies:
    print(s["id"], s["cost_total"], len(s["groups_above_threshold"]))
print(maxima)
