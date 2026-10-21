/* Priority Threat Management strategy explorer. Requires assets/data/strategies.js. Loaded with `defer`. */
(function () {
  "use strict";
  var D = window.MNLCP_DATA && window.MNLCP_DATA.strategies;
  var root = document.querySelector("[data-strategies]");
  if (!D || !root) return;
  var esc = window.MNLCP.escapeHtml;
  var TARGET = (D.results_summary && D.results_summary.persistence_target_pct) || 50;
  var GROUP_SLUG = {
    "Plants": "plants", "Terrestrial arthropods": "terrestrial-arthropods", "Terrestrial snails": "terrestrial-snails",
    "Aquatic invertebrates": "aquatic-invertebrates", "Forest birds": "forest-birds", "Seabirds": "seabirds",
    "Waterbirds": "waterbirds", "Hawaiian hoary bat": "hawaiian-hoary-bat"
  };
  var groups = D.species_groups;
  var byId = {};
  D.strategies.forEach(function (s) { byId[s.id] = s; });
  var state = { a: "S25", b: "", show: "S25" };

  function shortName(s) {
    var n = s.name.replace(/\s*\(.*\)\s*$/, "");
    return n.length > 64 ? n.slice(0, 62) + "…" : n;
  }
  function money(v) { return v == null ? "n/a" : "$" + (v >= 100 ? Math.round(v) : v.toFixed(v < 10 ? 1 : 0)) + "M"; }

  root.innerHTML =
    '<div class="explorer">' +
    '<div class="explorer-head">' +
    '<div class="explorer-controls">' +
    '<label class="small" for="st-a"><b>Strategy</b></label>' +
    '<select class="select" id="st-a" style="max-width:100%"></select>' +
    '<label class="small" for="st-b"><b>Compare with</b></label>' +
    '<select class="select" id="st-b" style="max-width:100%"><option value="">Nothing</option></select>' +
    "</div>" +
    '<div class="stats" id="st-tiles" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr))"></div>' +
    "</div>" +
    '<div style="padding:20px;position:relative" id="st-chart"></div>' +
    '<div style="padding:0 20px 20px" id="st-detail"></div>' +
    '<div class="explorer-foot"><span>Persistence: expected probability, adjusted for feasibility, that a species group keeps viable, self-sustaining populations for 20 years. Source: MNLCP Ch 6j Table 26 and Appendix 2.</span></div>' +
    "</div>";

  var selA = root.querySelector("#st-a"), selB = root.querySelector("#st-b");
  function options(sel, withNone) {
    var singles = D.strategies.filter(function (s) { return s.type === "single"; });
    var combos = D.strategies.filter(function (s) { return s.type !== "single"; });
    var h = withNone ? '<option value="">Nothing</option>' : "";
    h += '<optgroup label="Single-focus strategies">' + singles.map(function (s) { return '<option value="' + s.id + '">' + s.id + " · " + esc(shortName(s)) + "</option>"; }).join("") + "</optgroup>";
    h += '<optgroup label="Combination strategies">' + combos.map(function (s) { return '<option value="' + s.id + '">' + s.id + " · " + esc(shortName(s)) + (s.in_mnlcp_selection && combos.indexOf(s) > -1 && (s.id === "S25" || s.id === "S27") ? " (selected in the plan)" : "") + "</option>"; }).join("") + "</optgroup>";
    sel.innerHTML = h;
  }
  options(selA, false); options(selB, true);
  selA.value = state.a;
  selA.addEventListener("change", function () { state.a = selA.value; render(); });
  selB.addEventListener("change", function () { state.b = selB.value; render(); });

  var tip = document.createElement("div");
  tip.className = "chart-tip"; tip.style.display = "none";
  root.querySelector("#st-chart").appendChild(tip);

  function chart() {
    var A = byId[state.a], Bs = state.b ? byId[state.b] : null;
    var W = 760, rowH = 30, left = 200, right = 56, top = 34;
    var H = top + groups.length * rowH + 30;
    var x = function (v) { return left + (W - left - right) * v / 100; };
    var s = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Persistence of each species group under ' + esc(A.id) + (Bs ? " compared with " + esc(Bs.id) : "") + '" style="width:100%;height:auto;font-family:inherit">';
    [0, 25, 50, 75, 100].forEach(function (t) {
      s += '<line x1="' + x(t) + '" x2="' + x(t) + '" y1="' + (top - 8) + '" y2="' + (H - 26) + '" stroke="var(--line)" stroke-width="1"' + (t === TARGET ? ' stroke-dasharray="0"' : "") + "/>";
      s += '<text x="' + x(t) + '" y="' + (H - 8) + '" text-anchor="middle" font-size="12" style="fill:var(--muted)">' + t + "%</text>";
    });
    s += '<line x1="' + x(TARGET) + '" x2="' + x(TARGET) + '" y1="' + (top - 14) + '" y2="' + (H - 26) + '" stroke="var(--ink)" stroke-width="2" stroke-dasharray="5 4"/>';
    s += '<text x="' + (x(TARGET) + 6) + '" y="' + (top - 16) + '" font-size="12" font-weight="700" style="fill:var(--ink)">' + TARGET + "% target</text>";
    groups.forEach(function (g, i) {
      var y = top + i * rowH;
      var va = A.benefit_by_group[g.id], vb = Bs ? Bs.benefit_by_group[g.id] : null;
      var slug = GROUP_SLUG[g.taxon_group] || "";
      var ok = va != null && va >= TARGET;
      var label = g.name.length > 28 ? g.name.replace(/\s*\(.*\)\s*$/, "") : g.name;
      s += '<g class="st-row" data-g="' + g.id + '" data-group="' + slug + '">' +
        '<rect x="0" y="' + (y - 2) + '" width="' + W + '" height="' + rowH + '" fill="transparent"/>' +
        '<text x="' + (left - 10) + '" y="' + (y + 17) + '" text-anchor="end" font-size="12.5" style="fill:var(--ink-2)">' + esc(label) + "</text>";
      if (va != null) {
        s += '<rect x="' + left + '" y="' + (y + 5) + '" width="' + Math.max(3, x(va) - left) + '" height="' + (Bs ? 9 : 16) + '" rx="4" style="fill:var(--gc)"' + (ok ? "" : ' fill-opacity=".55"') + "/>";
      }
      if (Bs && vb != null) {
        s += '<rect x="' + left + '" y="' + (y + 16) + '" width="' + Math.max(3, x(vb) - left) + '" height="9" rx="4" fill="none" style="stroke:var(--gc)" stroke-width="1.6"/>';
      }
      if (g.baseline_persistence_pct != null) {
        s += '<line x1="' + x(g.baseline_persistence_pct) + '" x2="' + x(g.baseline_persistence_pct) + '" y1="' + (y + 2) + '" y2="' + (y + 24) + '" stroke="var(--ink)" stroke-width="2" stroke-opacity=".55"/>';
      }
      var labelV = Bs ? (va != null ? va : "–") + " / " + (vb != null ? vb : "–") : (va != null ? va + "%" : "–");
      s += '<text x="' + (x(Math.max(va || 0, vb || 0)) + 6) + '" y="' + (y + 17) + '" font-size="12" font-weight="700" style="fill:var(--ink)">' + labelV + "</text></g>";
    });
    s += "</svg>";
    var legend = '<div class="legend" style="flex-direction:row;flex-wrap:wrap;gap:16px;margin-top:6px">' +
      '<span class="legend-row"><i style="background:var(--accent)"></i>' + esc(A.id) + " (faded = below target)</span>" +
      (Bs ? '<span class="legend-row"><i style="border:2px solid var(--accent);background:none"></i>' + esc(Bs.id) + "</span>" : "") +
      '<span class="legend-row"><i style="width:3px;background:var(--ink);opacity:.55"></i>Current actions only</span>' +
      '<span class="legend-row">Bars take each taxonomic group\'s colour.</span></div>';
    var rows = groups.map(function (g) {
      return "<tr><td>" + esc(g.name) + '</td><td class="num">' + (g.counterfactual_persistence_pct != null ? g.counterfactual_persistence_pct : "–") + '</td><td class="num">' + (g.baseline_persistence_pct != null ? g.baseline_persistence_pct : "–") +
        '</td><td class="num">' + (A.benefit_by_group[g.id] != null ? A.benefit_by_group[g.id] : "–") + "</td>" + (Bs ? '<td class="num">' + (Bs.benefit_by_group[g.id] != null ? Bs.benefit_by_group[g.id] : "–") + "</td>" : "") + "</tr>";
    }).join("");
    var table = '<details class="more"><summary>View as a table<span class="summary-tag">Data</span></summary><div class="details-body"><div class="table-wrap" style="margin:0"><table><thead><tr><th>Species group</th><th class="num">No action</th><th class="num">Current actions</th><th class="num">' + esc(A.id) + "</th>" + (Bs ? '<th class="num">' + esc(Bs.id) + "</th>" : "") + "</tr></thead><tbody>" + rows + "</tbody></table></div></div></details>";
    var box = root.querySelector("#st-chart");
    box.innerHTML = s + legend + table;
    box.appendChild(tip);
    Array.prototype.forEach.call(box.querySelectorAll(".st-row"), function (r) {
      r.addEventListener("mousemove", function (e) {
        var g = groups.filter(function (x) { return x.id === r.getAttribute("data-g"); })[0];
        var va = A.benefit_by_group[g.id], vb = Bs ? Bs.benefit_by_group[g.id] : null;
        tip.innerHTML = "<b>" + esc(g.name) + "</b>" + (g.n_species ? " (" + g.n_species + " species)" : "") + "<br>" +
          esc(A.id) + ": " + (va != null ? va + "%" : "n/a") + (Bs ? "<br>" + esc(Bs.id) + ": " + (vb != null ? vb + "%" : "n/a") : "") +
          "<br>Current actions: " + (g.baseline_persistence_pct != null ? g.baseline_persistence_pct + "%" : "n/a") +
          "<br>No action: " + (g.counterfactual_persistence_pct != null ? g.counterfactual_persistence_pct + "%" : "n/a");
        var rb = box.getBoundingClientRect();
        tip.style.display = "block";
        tip.style.left = Math.min(e.clientX - rb.left + 14, rb.width - 290) + "px";
        tip.style.top = (e.clientY - rb.top + 14) + "px";
      });
      r.addEventListener("mouseleave", function () { tip.style.display = "none"; });
    });
  }

  function tiles() {
    var A = byId[state.a], Bs = state.b ? byId[state.b] : null;
    function tile(num, label) { return '<div class="stat"><div class="stat-num" style="font-size:2rem">' + num + '</div><div class="stat-label">' + label + "</div></div>"; }
    var n = groups.length;
    var h = tile(A.groups_above_threshold.length + "<span style='font-size:1rem;color:var(--muted)'> / " + n + "</span>", "species groups reach the " + TARGET + "% target under " + esc(A.id)) +
      tile(money(A.cost_total), "estimated total cost over 20 years (" + esc(A.id) + ")");
    if (Bs) h += tile(Bs.groups_above_threshold.length + "<span style='font-size:1rem;color:var(--muted)'> / " + n + "</span>", "reach the target under " + esc(Bs.id)) + tile(money(Bs.cost_total), "estimated total cost (" + esc(Bs.id) + ")");
    root.querySelector("#st-tiles").innerHTML = h;
  }

  function detail() {
    var A = byId[state.a];
    var acts = (D.actions_list || []).filter(function (a) { return a.strategy === A.id; });
    var comps = (A.components || []).map(function (c) { return byId[c]; }).filter(Boolean);
    var h = "<h3 style='margin-top:0'>" + esc(A.id) + " · " + esc(shortName(A)) + "</h3>" +
      (A.in_mnlcp_selection && (A.id === "S25" || A.id === "S27") ? '<p><span class="flag flag-green">One of the two combinations the plan selects</span></p>' : "") +
      "<p>" + esc(A.description || "") + "</p>";
    if (comps.length) {
      h += "<p><b>Includes " + comps.length + " single strategies:</b></p><div class='pill-row'>" + comps.map(function (c) {
        return '<button class="pill" data-pick="' + c.id + '">' + c.id + " · " + esc(shortName(c)) + "</button>";
      }).join("") + "</div>";
    }
    if (acts.length) {
      h += '<details class="more" open><summary>Actions in this strategy (' + acts.length + ')<span class="summary-tag">Appendix 2</span></summary><div class="details-body"><ol>' +
        acts.map(function (a) {
          return "<li>" + esc(a.action) + (a.target || a.timeline ? '<div class="small muted">' + esc([a.target, a.timeline].filter(Boolean).join(" · ")) + "</div>" : "") + "</li>";
        }).join("") + "</ol></div></details>";
    }
    if (A.notes) h += '<p class="small muted">' + esc(A.notes) + "</p>";
    var box = root.querySelector("#st-detail");
    box.innerHTML = h;
    Array.prototype.forEach.call(box.querySelectorAll("[data-pick]"), function (b) {
      b.addEventListener("click", function () { state.a = b.getAttribute("data-pick"); selA.value = state.a; render(); root.scrollIntoView({ behavior: "smooth" }); });
    });
  }

  function render() { tiles(); chart(); detail(); }
  render();
})();
