/* Interactive page widgets: species explorer, IMCP diagram, cycle diagram, image stepper.
   Each widget initialises only if its container is on the page. Loaded with `defer`. */
(function () {
  "use strict";
  var M = window.MNLCP || {};
  var esc = M.escapeHtml || function (s) { return String(s); };
  var DATA = window.MNLCP_DATA || {};

  var GROUP_SLUG = {
    "Plants": "plants", "Terrestrial arthropods": "terrestrial-arthropods", "Terrestrial snails": "terrestrial-snails",
    "Aquatic invertebrates": "aquatic-invertebrates", "Forest birds": "forest-birds", "Seabirds": "seabirds",
    "Waterbirds": "waterbirds", "Hawaiian hoary bat": "hawaiian-hoary-bat"
  };
  function slugOf(name) {
    if (!name) return "";
    if (GROUP_SLUG[name]) return GROUP_SLUG[name];
    var k = Object.keys(GROUP_SLUG).filter(function (g) { return g.toLowerCase() === String(name).toLowerCase(); })[0];
    return k ? GROUP_SLUG[k] : String(name).toLowerCase().replace(/[^a-z]+/g, "-");
  }
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯʻ‘’'`]/g, ""); }

  /* ---------------- Species explorer ---------------- */
  var GROUP_ORDER = ["Forest birds", "Seabirds", "Waterbirds", "Plants", "Terrestrial snails", "Terrestrial arthropods", "Aquatic invertebrates", "Hawaiian hoary bat"];
  function statusClass(s) {
    if (!s) return "Unknown";
    if (/^endangered/i.test(s)) return "Endangered";
    if (/^threatened/i.test(s)) return "Threatened";
    if (/not listed/i.test(s)) return "Not listed";
    return "Other";
  }
  function speciesExplorer(root) {
    var S = DATA.species;
    if (!S || !S.species) { root.innerHTML = "<p class='muted'>Species list unavailable.</p>"; return; }
    var rows = S.species.slice().sort(function (a, b) {
      var ga = GROUP_ORDER.indexOf(a.group), gb = GROUP_ORDER.indexOf(b.group);
      return ga !== gb ? ga - gb : String(a.scientific_name).localeCompare(String(b.scientific_name));
    });
    var groups = GROUP_ORDER.filter(function (g) { return rows.some(function (r) { return r.group === g; }); });
    var goal = function (r) { return (r.other && r.other.recovery_category) || null; };
    var goals = [];
    rows.forEach(function (r) { var g = goal(r); if (g && goals.indexOf(g) < 0) goals.push(g); });
    var hasIslands = rows.filter(function (r) { return r.islands && r.islands.length; }).length > rows.length / 2;
    var hasImminent = rows.some(function (r) { return r.imminent_extinction === true; });

    root.innerHTML =
      '<div class="explorer"><div class="explorer-head">' +
      '<div class="explorer-controls">' +
      '<input class="input" type="search" placeholder="Search by scientific, common or Hawaiian name" aria-label="Search species">' +
      '<select class="select" data-f="group" aria-label="Taxonomic group"><option value="">All groups</option>' +
      groups.map(function (g) { return '<option value="' + esc(g) + '">' + esc(g) + "</option>"; }).join("") + "</select>" +
      '<select class="select" data-f="status" aria-label="Listing status"><option value="">Any listing status</option><option>Endangered</option><option>Threatened</option><option>Not listed</option></select>' +
      (goals.length ? '<select class="select" data-f="goal" aria-label="Recovery goal"><option value="">Any recovery goal</option>' + goals.map(function (g) { return "<option>" + esc(g) + "</option>"; }).join("") + "</select>" : "") +
      (hasIslands ? '<select class="select" data-f="island" aria-label="Island"><option value="">All islands</option><option>Maui</option><option>Molokaʻi</option><option>Lānaʻi</option><option>Kahoʻolawe</option></select>' : "") +
      (hasImminent ? '<label class="toggle"><input type="checkbox" data-f="imminent"> Facing imminent extinction</label>' : "") +
      "</div>" +
      '<div class="explorer-bars" aria-hidden="true"></div>' +
      '<div class="explorer-summary" aria-live="polite"></div>' +
      "</div>" +
      '<div class="explorer-table"><table><thead><tr><th>Species</th><th>Common / Hawaiian name</th><th>Group</th><th>Listing status</th>' +
      (hasImminent ? "<th>Imminent extinction</th>" : "") + (goals.length ? "<th>Recovery goal</th>" : "") + (hasIslands ? "<th>Islands</th>" : "") +
      "</tr></thead><tbody></tbody></table></div>" +
      '<div class="explorer-foot"><span>Source: MNLCP Appendices 3, 4, 6 and 7 and Chapter 6. Names and spellings as printed in the plan.</span><button class="pill" data-csv>Download list (CSV)</button></div></div>';

    var q = root.querySelector("input[type=search]");
    var f = {};
    ["group", "status", "goal", "island", "imminent"].forEach(function (k) { f[k] = root.querySelector('[data-f="' + k + '"]'); });
    var tbody = root.querySelector("tbody");
    var bars = root.querySelector(".explorer-bars");
    var summary = root.querySelector(".explorer-summary");
    var current = rows;

    var hm = /[#&]q=([^&]+)/.exec(location.hash);
    if (hm) q.value = decodeURIComponent(hm[1]);
    var gm = /[#&]group=([^&]+)/.exec(location.hash);
    if (gm) f.group.value = decodeURIComponent(gm[1]);

    function render() {
      var term = norm(q.value.trim());
      current = rows.filter(function (r) {
        if (f.group.value && r.group !== f.group.value) return false;
        if (f.status.value && statusClass(r.listing_status) !== f.status.value) return false;
        if (f.goal && f.goal.value && goal(r) !== f.goal.value) return false;
        if (f.island && f.island.value && !(r.islands || []).some(function (i) { return norm(i) === norm(f.island.value); })) return false;
        if (f.imminent && f.imminent.checked && r.imminent_extinction !== true) return false;
        if (term && norm([r.scientific_name, r.common_name, r.hawaiian_name].join(" ")).indexOf(term) < 0) return false;
        return true;
      });
      var counts = {};
      current.forEach(function (r) { counts[r.group] = (counts[r.group] || 0) + 1; });
      bars.innerHTML = groups.map(function (g) {
        return '<span data-group="' + slugOf(g) + '" style="flex-grow:' + (counts[g] || 0) + '" title="' + esc(g) + ": " + (counts[g] || 0) + '"></span>';
      }).join("");
      summary.innerHTML = "<b>" + current.length + "</b> of " + rows.length + " species · " +
        groups.filter(function (g) { return counts[g]; }).map(function (g) {
          return '<span class="chip chip-dot" data-group="' + slugOf(g) + '">' + esc(g) + " " + counts[g] + "</span>";
        }).join(" ");
      tbody.innerHTML = current.map(function (r) {
        var names = [r.common_name, r.hawaiian_name].filter(Boolean).filter(function (v, i, a) { return a.indexOf(v) === i; }).join(" · ");
        var sc = statusClass(r.listing_status);
        var st = r.listing_status ? '<span class="flag ' + (sc === "Not listed" ? "flag-grey" : "flag-green") + '" title="' + esc(r.listing_status) + '">' + esc(sc === "Other" ? r.listing_status : sc) + "</span>" : "—";
        return "<tr><td><em>" + esc(r.scientific_name) + "</em></td><td>" + esc(names || "—") + "</td>" +
          '<td><a class="chip chip-dot chip-sm" data-group="' + slugOf(r.group) + '" href="' + M.root + "groups/" + slugOf(r.group) + '.html">' + esc(r.group) + "</a></td>" +
          "<td>" + st + "</td>" +
          (hasImminent ? "<td>" + (r.imminent_extinction ? '<span class="flag flag-red">Yes</span>' : (r.imminent_extinction === false ? '<span class="muted">No</span>' : "—")) + "</td>" : "") +
          (goals.length ? "<td>" + esc(goal(r) || "—") + "</td>" : "") +
          (hasIslands ? "<td>" + esc((r.islands || []).join(", ") || "—") + "</td>" : "") + "</tr>";
      }).join("") || '<tr><td colspan="7" class="muted">No species match these filters.</td></tr>';
    }
    q.addEventListener("input", render);
    Object.keys(f).forEach(function (k) { if (f[k]) f[k].addEventListener("change", render); });
    root.querySelector("[data-csv]").addEventListener("click", function () {
      var head = ["group", "scientific_name", "common_name", "hawaiian_name", "listing_status", "imminent_extinction", "recovery_goal"];
      var lines = [head.join(",")].concat(current.map(function (r) {
        return head.map(function (h) {
          var v = h === "recovery_goal" ? goal(r) : r[h];
          if (Array.isArray(v)) v = v.join("; "); if (v == null) v = "";
          return '"' + String(v).replace(/"/g, '""') + '"';
        }).join(",");
      }));
      var blob = new Blob(["\ufeff" + lines.join("\n")], { type: "text/csv;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = "MNLCP_at_risk_species.csv";
      document.body.appendChild(a); a.click(); a.remove();
    });
    render();
  }

  /* ---------------- IMCP diagram ---------------- */
  function imcpDiagram(root) {
    var nodes = Array.prototype.slice.call(root.querySelectorAll(".node"));
    var detail = root.querySelector(".imcp-detail");
    var info = JSON.parse(root.querySelector("script[type='application/json']").textContent);
    function show(id) {
      var n = info[id];
      if (!n) return;
      nodes.forEach(function (x) { x.classList.toggle("is-active", x.getAttribute("data-id") === id); });
      detail.innerHTML = '<div class="q">' + esc(n.question || "") + '</div><h3>' + esc(n.label) + '</h3><div class="lead-by">' + esc(n.lead || "") + "</div>" +
        "<p>" + esc(n.description || "") + "</p>" +
        (n.outputs && n.outputs.length ? "<p><b>Outputs</b></p><ul>" + n.outputs.map(function (o) { return "<li>" + esc(o) + "</li>"; }).join("") + "</ul>" : "") +
        (n.page ? '<p><a class="btn btn-outline" href="' + M.root + n.page + '">Learn more</a></p>' : "");
    }
    nodes.forEach(function (n) {
      n.setAttribute("tabindex", "0");
      n.setAttribute("role", "button");
      n.addEventListener("click", function () { show(n.getAttribute("data-id")); });
      n.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(n.getAttribute("data-id")); } });
    });
    if (nodes[0]) show(nodes[0].getAttribute("data-id"));
  }

  /* ---------------- Cycle diagram ---------------- */
  function cycleDiagram(root) {
    var segs = Array.prototype.slice.call(root.querySelectorAll(".seg-arc"));
    var detail = root.querySelector(".imcp-detail");
    var steps = JSON.parse(root.querySelector("script[type='application/json']").textContent);
    function show(i) {
      segs.forEach(function (s, j) { s.classList.toggle("is-active", i === j); s.style.opacity = i === j ? 1 : 0.55; });
      var s = steps[i];
      detail.innerHTML = '<div class="q">' + (i + 1) + '</div><h3>' + esc(s.title) + "</h3><p>" + esc(s.description) + "</p>" +
        '<div class="stepper-nav"><button class="round-btn" data-d="-1" aria-label="Previous step">‹</button><button class="round-btn" data-d="1" aria-label="Next step">›</button></div>';
      detail.querySelectorAll("[data-d]").forEach(function (b) {
        b.addEventListener("click", function () { show((i + parseInt(b.getAttribute("data-d"), 10) + steps.length) % steps.length); });
      });
    }
    segs.forEach(function (s, i) {
      s.setAttribute("tabindex", "0"); s.setAttribute("role", "button");
      s.addEventListener("click", function () { show(i); });
      s.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(i); } });
    });
    show(0);
  }

  /* ---------------- Image stepper ---------------- */
  function stepper(root) {
    var imgs = Array.prototype.slice.call(root.querySelectorAll(".stepper-stage img"));
    var steps = JSON.parse(root.querySelector("script[type='application/json']").textContent);
    var title = root.querySelector(".stepper-body h3");
    var text = root.querySelector(".stepper-body p");
    var dots = root.querySelector(".stepper-dots");
    var prev = root.querySelector("[data-prev]"), next = root.querySelector("[data-next]");
    var i = 0;
    dots.innerHTML = steps.map(function (s, j) { return '<button aria-label="Step ' + (j + 1) + ": " + esc(s.title) + '"></button>'; }).join("");
    var dotBtns = Array.prototype.slice.call(dots.querySelectorAll("button"));
    function go(j) {
      i = Math.max(0, Math.min(steps.length - 1, j));
      imgs.forEach(function (im, k) { im.classList.toggle("is-active", k === i); });
      title.textContent = (i + 1) + ". " + steps[i].title;
      text.textContent = steps[i].text;
      dotBtns.forEach(function (d, k) { if (k === i) d.setAttribute("aria-current", "step"); else d.removeAttribute("aria-current"); });
      prev.disabled = i === 0; next.disabled = i === steps.length - 1;
    }
    dotBtns.forEach(function (d, k) { d.addEventListener("click", function () { go(k); }); });
    prev.addEventListener("click", function () { go(i - 1); });
    next.addEventListener("click", function () { go(i + 1); });
    root.addEventListener("keydown", function (e) { if (e.key === "ArrowRight") go(i + 1); if (e.key === "ArrowLeft") go(i - 1); });
    go(0);
  }

  /* ---------------- FAQ filter ---------------- */
  function faq(root) {
    var input = root.querySelector(".input");
    var pills = Array.prototype.slice.call(root.querySelectorAll(".pill[data-cat]"));
    var cats = Array.prototype.slice.call(document.querySelectorAll(".faq-cat"));
    var count = root.querySelector("[data-faq-count]");
    var cat = "";
    function apply() {
      var t = norm(input.value.trim());
      var shown = 0;
      cats.forEach(function (c) {
        var any = false;
        var catOk = !cat || c.id === cat;
        Array.prototype.forEach.call(c.querySelectorAll(".qa"), function (qa) {
          var ok = catOk && (!t || norm(qa.textContent).indexOf(t) > -1);
          qa.style.display = ok ? "" : "none";
          if (ok) { any = true; shown++; }
          if (t && ok) qa.open = true;
        });
        c.style.display = any ? "" : "none";
      });
      if (count) count.textContent = shown + (shown === 1 ? " question" : " questions");
    }
    input.addEventListener("input", apply);
    pills.forEach(function (p) {
      p.addEventListener("click", function () {
        cat = p.getAttribute("data-cat");
        pills.forEach(function (x) { x.setAttribute("aria-pressed", x === p ? "true" : "false"); });
        apply();
      });
    });
    if (location.hash) {
      var target = document.getElementById(location.hash.slice(1));
      if (target && target.tagName === "DETAILS") { target.open = true; }
    }
    apply();
  }

  /* ---------------- Glossary filter ---------------- */
  function glossary(root) {
    var input = root.querySelector(".input");
    var items = Array.prototype.slice.call(document.querySelectorAll(".gloss-entry"));
    var letters = Array.prototype.slice.call(document.querySelectorAll(".gloss-letter"));
    input.addEventListener("input", function () {
      var t = norm(input.value.trim());
      items.forEach(function (it) { it.style.display = !t || norm(it.textContent).indexOf(t) > -1 ? "" : "none"; });
      letters.forEach(function (l) {
        var sib = l.nextElementSibling, any = false;
        while (sib && !sib.classList.contains("gloss-letter")) { if (sib.style.display !== "none") any = true; sib = sib.nextElementSibling; }
        l.style.display = any ? "" : "none";
      });
    });
  }

  function init(sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); }
  init("[data-species-explorer]", speciesExplorer);
  init("[data-imcp]", imcpDiagram);
  init("[data-cycle]", cycleDiagram);
  init("[data-stepper]", stepper);
  init("[data-faq]", faq);
  init("[data-glossary-filter]", glossary);
})();
