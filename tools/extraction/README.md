# Extraction scripts (provenance)

One-time scripts that produced the structured content in `content/data/` and the images in
`assets/img/` from the MNLCP plan and the demo deck, in October 2026. They are kept so the
origin of every data file can be traced. **They are not part of the normal build.**

Most of them read intermediate files in `_source_extracts/`: PDF text extracts, page renders and
the unzipped deck. That folder is gitignored and exists only on the machine that made the draft.

| Script | Produced | Notes |
|---|---|---|
| `parse_species.py`, `wrap.py` | `content/data/species.json` | Parses Appendices 3, 4, 6 and 7 of the plan text; column assignment was checked against the rendered PDF |
| `build_strategies.py` | `content/data/strategies.json` | Priority Threat Management results from Ch 6j Table 26 and Appendix 2 Tables 1 and 2 |
| `build_faq.py` | `content/data/faq.json`, `content/pages/faq.md` | Q&A text was written in this script |
| `extract_plan_figs.py` | `assets/img/figures/plan_fig_*` | Crops figures from 220 dpi renders of the plan PDF |
| `brand.py` | `assets/img/brand/*` | Rebuilds the DOFAW footer band and fern art from the deck's media |
| `build_catalog.py` | `content/data/asset_catalog.json` | Image descriptions, alt text, sources and credits |

**Do not rerun `build_faq.py`, `parse_species.py` or `build_strategies.py` after editing the JSON
by hand.** They would overwrite the edits. Edit `content/data/*.json` directly instead. For the
Q&A, `faq.json` is the source the site is built from, and `faq.md` is a reading copy; update both,
or regenerate `faq.md` from the JSON.
