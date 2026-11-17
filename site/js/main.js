(function () {
  "use strict";
  var root = document.documentElement;

  // Svetlý / tmavý režim
  var tbtn = document.getElementById("theme-toggle");
  if (tbtn) tbtn.addEventListener("click", function () {
    var next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
  });

  // Mobilné menu
  var burger = document.getElementById("burger"), nav = document.getElementById("main-nav");
  function closeNav() { if (!nav) return; nav.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); document.body.style.overflow = ""; }
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = !nav.classList.contains("open");
      nav.classList.toggle("open", open);
      burger.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) closeNav(); });
    window.addEventListener("resize", function () { if (window.innerWidth > 860) closeNav(); });
  }

  // Rozbaľovacie menu Témy
  document.querySelectorAll(".dd").forEach(function (dd) {
    var btn = dd.querySelector(".dd-toggle");
    var hoverable = window.matchMedia("(hover:hover) and (min-width:861px)");
    function set(o) { dd.classList.toggle("open", o); btn.setAttribute("aria-expanded", String(o)); }
    btn.addEventListener("click", function (e) { e.stopPropagation(); set(!dd.classList.contains("open")); });
    dd.addEventListener("mouseenter", function () { if (hoverable.matches) set(true); });
    dd.addEventListener("mouseleave", function () { if (hoverable.matches) set(false); });
    document.addEventListener("click", function (e) { if (!dd.contains(e.target)) set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { set(false); closeNav(); } });
  });

  // Ošetrenie chýb pri načítaní obrázkov
  var fallbackSvg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 17-5-5-9 8"/></svg>';
  function handleImg(img) {
    function ok() { img.classList.add("loaded"); }
    function fail() {
      var box = img.closest(".fig-img, .topic-img, .q-fig");
      var bg = img.closest(".hero-bg, .page-hero-bg");
      if (bg) { bg.classList.add("failed"); return; }
      img.style.display = "none";
      if (box && !box.querySelector(".img-fallback")) {
        var d = document.createElement("div");
        d.className = "img-fallback";
        d.innerHTML = "<div>" + fallbackSvg + "<div>" + (img.alt || "Obrázok sa nepodarilo načítať") + "</div></div>";
        box.appendChild(d);
      }
    }
    if (img.complete) { img.naturalWidth ? ok() : fail(); }
    else { img.addEventListener("load", ok, { once: true }); img.addEventListener("error", fail, { once: true }); }
  }
  document.querySelectorAll("img").forEach(handleImg);
  window.__handleImg = handleImg;

  // Animácie pri posúvaní
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    reveals.forEach(function (el) { io.observe(el); });
  } else reveals.forEach(function (el) { el.classList.add("in"); });

  // Indikátor čítania + aktívna sekcia v obsahu
  var bar = document.getElementById("read-progress");
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  var sections = tocLinks.map(function (a) { return document.querySelector(a.getAttribute("href")); });
  var ticking = false;
  function onScroll() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
    var cur = -1;
    sections.forEach(function (s, i) { if (s && s.getBoundingClientRect().top < 200) cur = i; });
    tocLinks.forEach(function (a, i) { a.classList.toggle("is-current", i === cur); });
    if (cur >= 0 && tocLinks[cur] && tocLinks[cur].parentElement.scrollWidth > tocLinks[cur].parentElement.clientWidth) {
      var p = tocLinks[cur].parentElement, l = tocLinks[cur];
      var target = l.offsetLeft - p.clientWidth / 2 + l.clientWidth / 2;
      if (Math.abs(p.scrollLeft - target) > 40) p.scrollTo({ left: target, behavior: "smooth" });
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
  onScroll();
})();
