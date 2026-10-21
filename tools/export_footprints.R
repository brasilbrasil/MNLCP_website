# Export the 2026-09-25 release-candidate megafootprints (all taxon groups combined) to a
# browser-ready JS file for the site map.
# Output: assets/data/footprints.js (window.MNLCP_DATA.footprints = {meta, recovery, priority, islands})
# Run from MNLCP_website/:  Rscript tools/export_footprints.R
# Species names per planning unit are deliberately NOT exported (rare-species location sensitivity);
# the public map shows taxon-group counts and planning criteria per unit only.

suppressPackageStartupMessages({
  library(sf)
  library(data.table)
})
sf_use_s2(FALSE)

fp_dir <- "/hdd/projects/maui_nui_scp/all_taxon_footprints/data"
std_dir <- file.path(fp_dir, "4_standardized_outputs/20260925")
crit_gpkg <- "/hdd/projects/maui_nui_scp/solution_criteria/PU_vector_w_criteria_simple_20260528.gpkg"
out_js <- "assets/data/footprints.js"

# Groups withheld from the public map. Terrestrial snails: the project decided not to release
# snail range or exclosure-site locations publicly. Remove "ts" here to include them.
withheld_groups <- c("ts")

group_codes <- c(pl = "Plants", ta = "Terrestrial arthropods", ts = "Terrestrial snails",
                 ai = "Aquatic invertebrates", fb = "Forest birds", sb = "Seabirds",
                 wb = "Waterbirds")

bioregion_labels <- c(EMaui = "East Maui", WMaui = "West Maui", EMolokai = "East Molokaʻi",
                      WMolokai = "West Molokaʻi", Lanai = "Lānaʻi", Kahoolawe = "Kahoʻolawe")

# Land designation covering most of each unit (synthesis stats)
land <- fread(file.path(std_dir, "synthesis/stats/pu_land_status.csv"),
              colClasses = list(character = "uniqueID"))
desig_top <- land[, .(km2 = sum(km2)), by = .(uniqueID, desig)][order(-km2), .SD[1], by = uniqueID]

# Simplification can leave GeometryCollections with stray lines/points; keep polygon parts only
polygons_only <- function(x) {
  x <- st_make_valid(x)
  suppressWarnings(st_collection_extract(x, "POLYGON"))
}

read_mega <- function(kind) {
  x <- st_read(file.path(std_dir, kind, "stats/mega_footprint.gpkg"), quiet = TRUE)
  x <- st_transform(x, 4326)
  d <- st_drop_geometry(x)
  setDT(d)
  d[, uniqueID := as.character(uniqueID)]
  for (g in names(group_codes)) {
    col <- paste0(g, "__total_count")
    if (!col %in% names(d)) d[, (col) := 0L]
  }
  out <- d[, c(list(
    id = uniqueID,
    name = gsub("_", " ", elevpopref),
    bioregion = unname(bioregion_labels[bioregion]),
    n_species = overall_total_count,
    n_groups = taxon_group_count,
    hab_qual = hab_qual_index,
    climate = round(climate_resilience, 2),
    reserve_pct = round(top_consv_pct),
    consv_pct = round(all_consv_pct),
    ungulate_pct = round(UngManag_pct),
    access = round(accessibility, 1),
    fire = round(firerisk_max_value, 1)),
    lapply(setNames(paste0(names(group_codes), "__total_count"), names(group_codes)),
           function(col) get(col)))]
  # Drop withheld groups, recompute totals, and drop units that only serve withheld groups
  shown <- setdiff(names(group_codes), withheld_groups)
  out[, n_species := rowSums(.SD), .SDcols = shown]
  out[, n_groups := rowSums(.SD > 0), .SDcols = shown]
  keep <- out$n_species > 0
  out <- out[keep]
  for (g in withheld_groups) out[, (g) := NULL]
  out <- merge(out, desig_top[, .(uniqueID, desig)], by.x = "id", by.y = "uniqueID",
               all.x = TRUE, sort = FALSE)
  geom <- st_geometry(x)[match(out$id, d$uniqueID)]  # merge() keeps out's order with sort = FALSE
  geom <- st_simplify(geom, dTolerance = 0.0003, preserveTopology = TRUE)
  st_cast(polygons_only(st_sf(out, geometry = geom)), "MULTIPOLYGON")
}

recovery <- read_mega("recovery")
priority <- read_mega("priority")

# Island outlines from the planning-unit grid (offline context layer)
pu <- st_read(crit_gpkg, quiet = TRUE)
islands <- st_union(st_make_valid(st_transform(pu, 4326)))
islands <- st_simplify(st_cast(islands, "POLYGON"), dTolerance = 0.002, preserveTopology = TRUE)
islands <- polygons_only(st_sf(geometry = islands))
islands <- islands[as.numeric(st_area(islands)) > 1e6, ]

to_geojson <- function(x) {
  tmp <- tempfile(fileext = ".geojson")
  st_write(x, tmp, driver = "GeoJSON", quiet = TRUE,
           layer_options = c("COORDINATE_PRECISION=5", "RFC7946=YES"))
  paste(readLines(tmp, warn = FALSE), collapse = "")
}

meta <- sprintf(paste0(
  '{"version":"Release-candidate megafootprint, 2026-09-25","n_recovery_pus":%d,"n_priority_pus":%d,',
  '"groups":{%s},',
  '"criteria":{"hab_qual":"Habitat quality, 0-5 (native vegetation cover; 5 = nearly all native)",',
  '"climate":"Climate resilience, 0-3 (higher = more resilient)",',
  '"reserve_pct":"Percent of unit in biodiversity reserves (includes proposed reserves)",',
  '"ungulate_pct":"Percent of unit in ungulate-managed (fenced) areas",',
  '"access":"Accessibility, 1-5 (1 = easy, 5 = extremely challenging)",',
  '"fire":"Maximum dry-season fire probability in unit"},',
  '"withheld_groups":["%s"],',
  '"note":"Taxon-group counts per planning unit (~2 km2). Species names withheld."}'),
  nrow(recovery), nrow(priority),
  paste(sprintf('"%s":"%s"', setdiff(names(group_codes), withheld_groups),
                group_codes[setdiff(names(group_codes), withheld_groups)]), collapse = ","),
  paste(group_codes[withheld_groups], collapse = '","'))

js <- paste0(
  "/* Generated by tools/export_footprints.R from all_taxon_footprints megafootprints (2026-09-25). Do not edit by hand. */\n",
  "window.MNLCP_DATA = window.MNLCP_DATA || {};\n",
  "window.MNLCP_DATA.footprints = {\n",
  "meta: ", meta, ",\n",
  "recovery: ", to_geojson(recovery), ",\n",
  "priority: ", to_geojson(priority), ",\n",
  "islands: ", to_geojson(islands), "\n};\n")
writeLines(js, out_js, useBytes = TRUE)
cat(sprintf("Wrote %s (%.0f KB): %d recovery PUs, %d priority PUs, %d island polygons\n",
            out_js, file.size(out_js) / 1024, nrow(recovery), nrow(priority), nrow(islands)))
