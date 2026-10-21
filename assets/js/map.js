/* Conservation Footprints map (megafootprint). Requires Leaflet and assets/data/footprints.js. */
(function () {
  "use strict";
  var D = window.MNLCP_DATA && window.MNLCP_DATA.footprints;
  var el = document.getElementById("map");
  if (!D || !el || !window.L) return;
  var esc = window.MNLCP.escapeHtml;

  // Simplified geometries can arrive as GeometryCollections with stray points or lines;
  // keep only the polygon parts so Leaflet never draws markers.
  function polygonsOnly(fc) {
    fc.features.forEach(function (f) {
      var g = f.geometry;
      if (!g || g.type !== "GeometryCollection") return;
      var polys = [];
      (function collect(geoms) {
        geoms.forEach(function (m) {
          if (m.type === "Polygon") polys.push(m.coordinates);
          else if (m.type === "MultiPolygon") polys = polys.concat(m.coordinates);
          else if (m.type === "GeometryCollection") collect(m.geometries);
        });
      })(g.geometries);
      f.geometry = { type: "MultiPolygon", coordinates: polys };
    });
    return fc;
  }
  ["recovery", "priority", "islands", "grid"].forEach(function (k) { if (D[k]) polygonsOnly(D[k]); });

  var GROUPS = [
    { k: "fb", name: "Forest birds", color: "#e34948", page: "groups/forest-birds.html" },
    { k: "sb", name: "Seabirds", color: "#1baf7a", page: "groups/seabirds.html" },
    { k: "wb", name: "Waterbirds", color: "#eda100", page: "groups/waterbirds.html" },
    { k: "pl", name: "Plants", color: "#008300", page: "groups/plants.html" },
    { k: "ts", name: "Terrestrial snails", color: "#6250d6", page: "groups/terrestrial-snails.html" },
    { k: "ta", name: "Terrestrial arthropods", color: "#eb6834", page: "groups/terrestrial-arthropods.html" },
    { k: "ai", name: "Aquatic invertebrates", color: "#2a78d6", page: "groups/aquatic-invertebrates.html" }
  ];
  var GREENS = ["#c6e3ae", "#a3d183", "#7cbc5e", "#55a03f", "#35842f", "#1f6a2c", "#0f4a1d"];
  var BLUES = ["#cde2fb", "#9ec5f4", "#5598e7", "#256abf", "#0d366b"];
  var FIRE = ["#fff1c1", "#fdc66b", "#f58a3c", "#d9481f", "#8f1d0c"];
  var RECOVERY_GREEN = "#199e19", PRIORITY_MAGENTA = "#9e195e";  // same as the standardized footprint maps
  var COLOR_MODES = {
    nested: { label: "Footprint", type: "nested" },
    groups: { label: "Number of taxon groups", field: "n_groups", type: "classes", breaks: [1, 2, 3, 4, 5], ramp: ["#9ec5f4", "#5598e7", "#2a78d6", "#1c5cab", "#0d366b"], fmt: function (v) { return v + (v === 5 ? "+" : ""); } },
    species: { label: "Number of at-risk species (targets)", field: "n_species", type: "quantile", ramp: ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"] },
    hab_qual: { label: "Habitat quality (0–5, native cover)", field: "hab_qual", type: "linear", min: 0, max: 5, ramp: GREENS, lo: "Mostly non-native", hi: "Nearly all native" },
    climate: { label: "Climate resilience (0–3)", field: "climate", type: "linear", min: 0, max: 3, ramp: BLUES, lo: "Less resilient", hi: "More resilient" },
    reserve_pct: { label: "Share in biodiversity reserves", field: "reserve_pct", type: "linear", min: 0, max: 100, ramp: GREENS, lo: "0%", hi: "100%" },
    ungulate_pct: { label: "Share ungulate-managed (fenced)", field: "ungulate_pct", type: "linear", min: 0, max: 100, ramp: GREENS, lo: "0%", hi: "100%" },
    access: { label: "Accessibility (1 easy – 5 extremely challenging)", field: "access", type: "linear", min: 1, max: 5, ramp: BLUES, lo: "Easy", hi: "Very hard" },
    fire: { label: "Dry-season fire probability (max in unit)", field: "fire", type: "classes", breaks: [0, 1, 5, 10, 20], ramp: FIRE, fmt: function (v) { return v === 0 ? "0" : "≥" + v; } }
  };

  GROUPS = GROUPS.filter(function (g) { return !D.meta.groups || D.meta.groups[g.k]; });
  var state = { view: "recovery", color: "nested", groups: GROUPS.map(function (g) { return g.k; }), base: "none" };
  readHash();

  var map = L.map(el, { zoomControl: true, attributionControl: true, minZoom: 8, maxZoom: 15, zoomSnap: 0.25 });
  var bases = {
    topo: L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}", { attribution: "Basemap © Esri and contributors", maxZoom: 16 }),
    imagery: L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", { attribution: "Imagery © Esri, Maxar, Earthstar Geographics", maxZoom: 16 }),
    light: L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", { attribution: "© OpenStreetMap contributors © CARTO", subdomains: "abcd", maxZoom: 16 })
  };
  var islands = L.geoJSON(D.islands, { style: { color: "#3d3d3d", weight: 1, fillColor: "#faf9f4", fillOpacity: 0.85 }, interactive: false }).addTo(map);
  if (D.grid) L.geoJSON(D.grid, { style: { color: "#c9cec4", weight: 0.5, opacity: 0.9, fill: false }, interactive: false }).addTo(map);
  bases.none = L.layerGroup();  // "Clean": no tiles, matches the static maps and works offline
  function applyBase() {
    Object.keys(bases).forEach(function (k) { map.removeLayer(bases[k]); });
    bases[state.base].addTo(map);
    if (bases[state.base].bringToBack) bases[state.base].bringToBack();
    islands.setStyle({ fillOpacity: state.base === "none" ? 0.85 : 0.12 });
  }
  applyBase();
  map.fitBounds(islands.getBounds(), { padding: [10, 10] });

  var layer = null, selected = null;
  var scaleCache = {};

  function visibleFeature(p) {
    for (var i = 0; i < state.groups.length; i++) if (p[state.groups[i]] > 0) return true;
    return false;
  }
  function countFor(p) {
    var n = 0, s = 0;
    state.groups.forEach(function (k) { if (p[k] > 0) { n++; s += p[k]; } });
    return { groups: n, species: s };
  }
  function valueFor(p, mode) {
    if (mode.field === "n_groups") return countFor(p).groups;
    if (mode.field === "n_species") return countFor(p).species;
    return p[mode.field];
  }
  function quantileBreaks(values, n) {
    var v = values.filter(function (x) { return x != null; }).sort(function (a, b) { return a - b; });
    var out = [];
    for (var i = 0; i < n; i++) out.push(v[Math.floor(i / n * (v.length - 1))]);
    return out.filter(function (x, i, a) { return i === 0 || x > a[i - 1]; });
  }
  function interp(ramp, t) {
    t = Math.max(0, Math.min(1, t));
    var x = t * (ramp.length - 1), i = Math.floor(x), f = x - i;
    if (i >= ramp.length - 1) return ramp[ramp.length - 1];
    var a = hex(ramp[i]), b = hex(ramp[i + 1]);
    return "rgb(" + [0, 1, 2].map(function (j) { return Math.round(a[j] + (b[j] - a[j]) * f); }).join(",") + ")";
  }
  function hex(h) { h = h.replace("#", ""); return [0, 2, 4].map(function (i) { return parseInt(h.substr(i, 2), 16); }); }
  function colorFor(v, mode) {
    if (v == null || isNaN(v)) return "#bdbdbd";
    if (mode.type === "linear") return interp(mode.ramp, (v - mode.min) / (mode.max - mode.min));
    var breaks = mode.type === "quantile" ? scaleCache.q : mode.breaks;
    var idx = 0;
    for (var i = 0; i < breaks.length; i++) if (v >= breaks[i]) idx = i;
    var ramp = mode.ramp;
    if (breaks.length < ramp.length) ramp = breaks.map(function (_, i) { return mode.ramp[Math.round(i * (mode.ramp.length - 1) / Math.max(1, breaks.length - 1))]; });
    return ramp[idx];
  }

  function draw() {
    if (layer) map.removeLayer(layer);
    var fc = D[state.view];
    var mode = COLOR_MODES[state.color];
    if (mode.type === "quantile") {
      scaleCache.q = quantileBreaks(fc.features.filter(function (f) { return visibleFeature(f.properties); }).map(function (f) { return valueFor(f.properties, mode); }), mode.ramp.length);
    }
    var shown = 0;
    layer = L.geoJSON(fc, {
      filter: function (f) { var ok = visibleFeature(f.properties); if (ok) shown++; return ok; },
      style: function (f) {
        var fill = mode.type === "nested"
          ? (state.view === "priority" || f.properties.in_priority ? PRIORITY_MAGENTA : RECOVERY_GREEN)
          : colorFor(valueFor(f.properties, mode), mode);
        return { color: "#ffffff", weight: 0.5, opacity: 0.8, fillColor: fill, fillOpacity: 0.9 };
      },
      onEachFeature: function (f, lyr) {
        var p = f.properties;
        lyr.bindTooltip("<b>" + esc(p.name || "Planning unit " + p.id) + "</b><br>" + countFor(p).species + " species targets · " + countFor(p).groups + " groups", { sticky: true, direction: "top", opacity: 0.95 });
        lyr.on({
          mouseover: function () { lyr.setStyle({ weight: 2.2, color: "#12301b" }); lyr.bringToFront(); },
          mouseout: function () { if (selected !== lyr) layer.resetStyle(lyr); },
          click: function () { select(lyr, p); }
        });
      }
    }).addTo(map);
    document.getElementById("fp-shown").textContent = shown.toLocaleString();
    document.getElementById("fp-total").textContent = fc.features.length.toLocaleString();
    legend(mode);
    groupCounts();
    writeHash();
  }

  function select(lyr, p) {
    if (selected && layer.hasLayer(selected)) layer.resetStyle(selected);
    selected = lyr;
    lyr.setStyle({ weight: 3, color: "#e0ac1f" });
    lyr.bringToFront();
    var maxN = Math.max.apply(null, GROUPS.map(function (g) { return p[g.k] || 0; }).concat([1]));
    var bars = GROUPS.filter(function (g) { return p[g.k] > 0; }).map(function (g) {
      return '<div class="pu-bar"><a href="' + window.MNLCP.root + g.page + '">' + esc(g.name) + '</a><span class="b" style="--gc:' + g.color + ';width:' + Math.max(6, p[g.k] / maxN * 100) + '%"></span><b>' + p[g.k] + "</b></div>";
    }).join("");
    function fmt(v, suf) { return v == null ? "n/a" : v + (suf || ""); }
    document.getElementById("pu-card").innerHTML =
      '<div class="pu-card"><span class="card-tag">Planning unit ' + esc(p.id) + " · " + esc(p.bioregion || "") + "</span>" +
      "<h3>" + esc(p.name || "Planning unit") + "</h3>" +
      '<div class="small muted">' + esc(p.desig || "") + "</div>" +
      '<div class="pu-bars">' + bars + "</div>" +
      "<dl>" +
      "<dt>Habitat quality</dt><dd>" + fmt(p.hab_qual, " / 5") + "</dd>" +
      "<dt>Climate resilience</dt><dd>" + fmt(p.climate, " / 3") + "</dd>" +
      "<dt>In biodiversity reserves</dt><dd>" + fmt(p.reserve_pct, "%") + "</dd>" +
      "<dt>Ungulate-managed</dt><dd>" + fmt(p.ungulate_pct, "%") + "</dd>" +
      "<dt>Accessibility</dt><dd>" + fmt(p.access, " / 5") + "</dd>" +
      "<dt>Fire probability (max)</dt><dd>" + fmt(p.fire) + "</dd>" +
      "</dl></div>";
  }

  function legend(mode) {
    var box = document.getElementById("fp-legend");
    var h = "<div><b>" + esc(mode.label) + "</b></div>";
    if (mode.type === "nested") {
      if (state.view === "recovery") h += '<div class="legend-row"><i style="background:' + RECOVERY_GREEN + '"></i>Recovery footprint</div>';
      h += '<div class="legend-row"><i style="background:' + PRIORITY_MAGENTA + '"></i>Priority footprint' + (state.view === "recovery" ? " (nested inside recovery)" : "") + "</div>";
    } else if (mode.type === "linear") {
      h += '<div class="legend-ramp" style="background:linear-gradient(90deg,' + mode.ramp.join(",") + ')"></div>' +
        '<div class="legend-ends"><span>' + esc(mode.lo) + "</span><span>" + esc(mode.hi) + "</span></div>";
    } else {
      var breaks = mode.type === "quantile" ? scaleCache.q : mode.breaks;
      breaks.forEach(function (b, i) {
        var next = breaks[i + 1];
        var lab = mode.fmt ? mode.fmt(b) : (next != null && next - 1 > b ? b + "–" + (next - 1) : (next == null ? b + "+" : String(b)));
        h += '<div class="legend-row"><i style="background:' + colorFor(b, mode) + '"></i>' + esc(lab) + "</div>";
      });
    }
    h += '<div class="legend-row"><i style="background:#faf9f4;border:1px solid #9aa196"></i>Outside the footprint (light grid: planning units)</div>';
    box.innerHTML = h;
  }

  function groupCounts() {
    var fc = D[state.view];
    GROUPS.forEach(function (g) {
      var n = 0;
      fc.features.forEach(function (f) { if (f.properties[g.k] > 0) n++; });
      var c = document.querySelector('[data-count-for="' + g.k + '"]');
      if (c) c.textContent = n ? n + " units" : "none";
      var cb = document.querySelector('input[value="' + g.k + '"]');
      if (cb) cb.disabled = n === 0;
    });
  }

  /* Controls */
  function bindSeg(id, key) {
    var seg = document.getElementById(id);
    if (!seg) return;
    Array.prototype.forEach.call(seg.querySelectorAll("button"), function (b) {
      b.setAttribute("aria-pressed", b.value === state[key] ? "true" : "false");
      b.addEventListener("click", function () {
        state[key] = b.value;
        Array.prototype.forEach.call(seg.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        if (key === "base") { applyBase(); writeHash(); }
        else draw();
      });
    });
  }
  bindSeg("fp-view", "view");
  bindSeg("fp-base", "base");
  var colorSel = document.getElementById("fp-color");
  colorSel.value = state.color;
  colorSel.addEventListener("change", function () { state.color = colorSel.value; draw(); });

  var list = document.getElementById("fp-groups");
  list.innerHTML = GROUPS.map(function (g) {
    return '<li><label style="--gc:' + g.color + '"><input type="checkbox" value="' + g.k + '"' + (state.groups.indexOf(g.k) > -1 ? " checked" : "") + '><span class="swatch"></span>' + esc(g.name) + '<span class="count" data-count-for="' + g.k + '"></span></label></li>';
  }).join("");
  var withheld = (D.meta.withheld_groups || []).filter(Boolean);
  if (withheld.length) {
    list.insertAdjacentHTML("afterend", '<p class="small muted" style="margin:8px 0 0">' + esc(withheld.join(", ")) + " are not shown on this public map to protect sensitive locations.</p>");
  }
  list.addEventListener("change", function () {
    state.groups = Array.prototype.map.call(list.querySelectorAll("input:checked"), function (i) { return i.value; });
    draw();
  });
  document.getElementById("fp-all").addEventListener("click", function () {
    var boxes = list.querySelectorAll("input:not(:disabled)");
    var allOn = Array.prototype.every.call(boxes, function (b) { return b.checked; });
    Array.prototype.forEach.call(boxes, function (b) { b.checked = !allOn; });
    state.groups = Array.prototype.map.call(list.querySelectorAll("input:checked"), function (i) { return i.value; });
    draw();
  });

  function writeHash() {
    var h = "view=" + state.view + "&color=" + state.color + "&base=" + state.base + "&groups=" + state.groups.join(",");
    try { history.replaceState(null, "", "#" + h); } catch (e) { /* file:// in some browsers */ }
  }
  function readHash() {
    var h = (location.hash || "").replace(/^#/, "");
    h.split("&").forEach(function (kv) {
      var p = kv.split("=");
      if (p[0] === "view" && (p[1] === "recovery" || p[1] === "priority")) state.view = p[1];
      if (p[0] === "color" && COLOR_MODES[p[1]]) state.color = p[1];
      if (p[0] === "base" && /^(none|topo|imagery|light)$/.test(p[1])) state.base = p[1];
      if (p[0] === "groups" && p[1] !== undefined) state.groups = p[1].split(",").filter(function (k) { return GROUPS.some(function (g) { return g.k === k; }); });
    });
  }

  draw();
  setTimeout(function () { map.invalidateSize(); }, 200);
})();
