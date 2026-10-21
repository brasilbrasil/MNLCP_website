/* Maui Nui Landscape Conservation Plan — shared site behaviour.
   Vanilla JS, no dependencies. Works from file:// and any static host. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var ROOT = doc.getAttribute("data-root") || "";

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      if (val === null) localStorage.removeItem(key); else localStorage.setItem(key, val);
    } catch (e) { return null; }
  }
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function loadScript(src, cb) {
    var s = document.createElement("script");
    s.src = ROOT + src; s.onload = cb; s.onerror = cb;
    document.head.appendChild(s);
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  window.MNLCP = { $: $, $$: $$, loadScript: loadScript, escapeHtml: escapeHtml, root: ROOT, store: store };

  /* ---------- Theme ---------- */
  var savedTheme = store("mnlcp-theme");
  if (savedTheme) doc.setAttribute("data-theme", savedTheme);
  var themeBtn = $("[data-theme-toggle]");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var dark = doc.getAttribute("data-theme") === "dark" ||
        (!doc.getAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
      var next = dark ? "light" : "dark";
      doc.setAttribute("data-theme", next);
      store("mnlcp-theme", next);
      document.dispatchEvent(new CustomEvent("mnlcp:theme", { detail: next }));
    });
  }

  /* ---------- Navigation ---------- */
  var nav = $(".nav");
  var menuBtn = $(".menu-toggle");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
  }
  $$(".nav button.nav-top").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var li = btn.parentElement;
      var wasOpen = li.classList.contains("open");
      $$(".nav li.open").forEach(function (o) { o.classList.remove("open"); o.firstElementChild.setAttribute("aria-expanded", "false"); });
      if (!wasOpen) { li.classList.add("open"); btn.setAttribute("aria-expanded", "true"); }
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav")) $$(".nav li.open").forEach(function (o) { o.classList.remove("open"); o.firstElementChild.setAttribute("aria-expanded", "false"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      $$(".nav li.open").forEach(function (o) { o.classList.remove("open"); o.firstElementChild.setAttribute("aria-expanded", "false"); });
      closeSearch(); closeLightbox();
    }
  });

  /* ---------- Search ---------- */
  var panel = $(".search-panel");
  var input = panel && $("input", panel);
  var results = panel && $(".search-results", panel);
  var activeIdx = -1;
  function openSearch() {
    if (!panel) return;
    panel.classList.add("is-open");
    input.value = ""; results.innerHTML = ""; activeIdx = -1;
    setTimeout(function () { input.focus(); }, 20);
    if (!(window.MNLCP_DATA && window.MNLCP_DATA.search)) loadScript("assets/data/search.js", function () { runSearch(); });
  }
  function closeSearch() { if (panel) panel.classList.remove("is-open"); }
  function norm(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯʻ‘’'`]/g, ""); }
  function runSearch() {
    var q = norm(input.value.trim());
    var data = (window.MNLCP_DATA && window.MNLCP_DATA.search) || [];
    if (!q) { results.innerHTML = '<li class="search-empty">Search pages, species groups, actions, questions and terms.</li>'; return; }
    var terms = q.split(/\s+/).filter(Boolean);
    var scored = [];
    data.forEach(function (d) {
      var t = d._t || (d._t = norm(d.title));
      var b = d._b || (d._b = norm(d.text));
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var inT = t.indexOf(terms[i]) > -1, inB = b.indexOf(terms[i]) > -1;
        if (!inT && !inB) return;
        score += (inT ? 10 : 0) + (inB ? 2 : 0);
      }
      if (t.indexOf(q) > -1) score += 15;
      scored.push([score, d]);
    });
    scored.sort(function (a, b) { return b[0] - a[0]; });
    if (!scored.length) { results.innerHTML = '<li class="search-empty">No matches. Try another word, such as "fence", "rats" or "nēnē".</li>'; return; }
    results.innerHTML = scored.slice(0, 25).map(function (s, i) {
      var d = s[1];
      var snip = snippet(d.text, terms);
      return '<li><a href="' + ROOT + d.url + '"' + (i === 0 ? ' class="is-active"' : "") + '><span class="sr-page">' + escapeHtml(d.page) + '</span><span class="sr-title">' + escapeHtml(d.title) + '</span><span class="sr-snip">' + snip + "</span></a></li>";
    }).join("");
    activeIdx = 0;
  }
  function snippet(text, terms) {
    var n = norm(text), pos = -1;
    for (var i = 0; i < terms.length && pos < 0; i++) pos = n.indexOf(terms[i]);
    var start = Math.max(0, pos - 60);
    var s = (start > 0 ? "…" : "") + text.substr(start, 180) + (text.length > start + 180 ? "…" : "");
    var out = escapeHtml(s);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      out = out.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>");
    });
    return out;
  }
  if (panel) {
    $$("[data-search-open]").forEach(function (b) { b.addEventListener("click", openSearch); });
    panel.addEventListener("click", function (e) { if (e.target === panel) closeSearch(); });
    input.addEventListener("input", runSearch);
    input.addEventListener("keydown", function (e) {
      var links = $$("a", results);
      if (!links.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        activeIdx = (activeIdx + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach(function (l, i) { l.classList.toggle("is-active", i === activeIdx); });
        links[activeIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && links[activeIdx]) {
        window.location.href = links[activeIdx].href;
      }
    });
    document.addEventListener("keydown", function (e) {
      var tag = (e.target.tagName || "").toLowerCase();
      if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && tag !== "input" && tag !== "textarea" && tag !== "select")) {
        e.preventDefault(); openSearch();
      }
    });
  }

  /* ---------- Table of contents + scrollspy ---------- */
  var toc = $(".toc ol");
  var prose = $(".prose[data-toc]");
  if (toc && prose) {
    var heads = $$("h2[id]", prose);
    if (heads.length < 2) { toc.closest(".toc").style.display = "none"; }
    toc.innerHTML = heads.map(function (h) {
      return '<li><a href="#' + h.id + '">' + escapeHtml(h.textContent) + "</a></li>";
    }).join("");
    var tocLinks = $$("a", toc);
    if ("IntersectionObserver" in window) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            tocLinks.forEach(function (a) { a.classList.toggle("is-active", a.getAttribute("href") === "#" + en.target.id); });
          }
        });
      }, { rootMargin: "-20% 0px -70% 0px" });
      heads.forEach(function (h) { spy.observe(h); });
    }
  }

  /* ---------- Animated counters ---------- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    if (isNaN(target)) return;
    var dur = 1400, t0 = null;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) { el.textContent = target.toLocaleString() + suffix; return; }
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString() + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = $$(".reveal, [data-count]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute("data-count")) animateCount(el); else el.classList.add("is-visible");
        io.unobserve(el);
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Lightbox for figures ---------- */
  var lb = document.createElement("div");
  lb.className = "lightbox"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-label", "Enlarged figure");
  lb.innerHTML = "<img alt=''><p></p>";
  document.body.appendChild(lb);
  function closeLightbox() { lb.classList.remove("is-open"); }
  lb.addEventListener("click", closeLightbox);
  $$("figure.zoomable img").forEach(function (img) {
    img.setAttribute("tabindex", "0");
    function open() {
      $("img", lb).src = img.getAttribute("data-full") || img.src;
      $("img", lb).alt = img.alt;
      var cap = img.closest("figure").querySelector("figcaption");
      $("p", lb).textContent = cap ? cap.textContent : "";
      lb.classList.add("is-open");
    }
    img.addEventListener("click", open);
    img.addEventListener("keydown", function (e) { if (e.key === "Enter") open(); });
  });

  /* ---------- Glossary tooltips ---------- */
  var glossTargets = $$(".prose[data-glossary]");
  if (glossTargets.length) {
    loadScript("assets/data/glossary.js", function () {
      var g = window.MNLCP_DATA && window.MNLCP_DATA.glossary;
      if (!g || !g.terms) return;
      var entries = [];
      g.terms.forEach(function (t) {
        [t.term].concat(t.aliases || []).forEach(function (name) {
          if (name && name.length >= 3) entries.push({ name: name, term: t });
        });
      });
      entries.sort(function (a, b) { return b.name.length - a.name.length; });
      var used = {};
      var tip = document.createElement("div");
      tip.className = "gloss-tip"; tip.style.display = "none"; tip.setAttribute("role", "tooltip");
      document.body.appendChild(tip);
      glossTargets.forEach(function (root) {
        var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
          acceptNode: function (n) {
            var p = n.parentElement;
            if (!p || p.closest("a, h1, h2, h3, h4, summary, .gloss, code, th, figcaption, .stat, .callout, svg, button, select, label, [data-imcp], [data-cycle], [data-stepper], [data-strategies], [data-species-explorer]")) return NodeFilter.FILTER_REJECT;
            return n.nodeValue.trim().length > 3 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
          }
        });
        var nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach(function (node) {
          for (var i = 0; i < entries.length; i++) {
            var en = entries[i];
            if (used[en.term.term]) continue;
            var esc = en.name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
            var re = new RegExp("(^|[^\\wʻ])(" + esc + ")(?=[^\\w]|$)", en.name === en.name.toUpperCase() ? "" : "i");
            var m = re.exec(node.nodeValue);
            if (!m) continue;
            used[en.term.term] = true;
            var start = m.index + m[1].length;
            var after = node.splitText(start);
            after.splitText(m[2].length);
            var span = document.createElement("span");
            span.className = "gloss"; span.tabIndex = 0;
            span.setAttribute("data-term", en.term.term);
            span.setAttribute("data-def", en.term.definition);
            span.textContent = after.nodeValue;
            after.parentNode.replaceChild(span, after);
            break;
          }
        });
      });
      function show(e) {
        var el = e.target.closest(".gloss");
        if (!el) return;
        tip.innerHTML = "<b>" + escapeHtml(el.getAttribute("data-term")) + "</b>" + escapeHtml(el.getAttribute("data-def"));
        tip.style.display = "block";
        var r = el.getBoundingClientRect();
        var w = tip.offsetWidth;
        var left = Math.min(Math.max(8, r.left + window.scrollX + r.width / 2 - w / 2), window.scrollX + document.documentElement.clientWidth - w - 8);
        var top = r.bottom + window.scrollY + 8;
        if (r.bottom + tip.offsetHeight + 16 > window.innerHeight) top = r.top + window.scrollY - tip.offsetHeight - 8;
        tip.style.left = left + "px"; tip.style.top = top + "px";
      }
      function hide(e) { if (e.target.closest(".gloss")) tip.style.display = "none"; }
      document.addEventListener("mouseover", show);
      document.addEventListener("focusin", show);
      document.addEventListener("mouseout", hide);
      document.addEventListener("focusout", hide);
    });
  }

  /* ---------- Plan-source notes (review aid) ---------- */
  var srcToggle = $("[data-sources-toggle]");
  function setSources(on) {
    doc.classList.toggle("show-sources", on);
    if (srcToggle) srcToggle.setAttribute("aria-pressed", on ? "true" : "false");
  }
  if (srcToggle) {
    setSources(store("mnlcp-sources") === "1");
    srcToggle.addEventListener("click", function () {
      var on = !doc.classList.contains("show-sources");
      setSources(on); store("mnlcp-sources", on ? "1" : null);
    });
  }

  /* ---------- Back to top ---------- */
  var bt = $(".back-top");
  if (bt) {
    window.addEventListener("scroll", function () { bt.classList.toggle("is-visible", window.scrollY > 900); }, { passive: true });
    $("button", bt).addEventListener("click", function () { window.scrollTo({ top: 0 }); });
  }
})();
