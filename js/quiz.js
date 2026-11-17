(function () {
  "use strict";
  var DATA = window.QUIZ || [];
  var $ = function (id) { return document.getElementById(id); };
  var LETTERS = ["A", "B", "C", "D"];
  var order = [], idx = 0, score = 0, answers = [];

  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function show(id) { ["q-start", "q-play", "q-result"].forEach(function (s) { $(s).hidden = s !== id; }); }
  function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

  function start() {
    // poradie otázok ostáva podľa tém, premiešajú sa len odpovede
    order = DATA.map(function (q) {
      var opts = shuffle(q.o.map(function (text, i) { return { text: text, correct: i === q.a }; }));
      return { q: q, opts: opts };
    });
    idx = 0; score = 0; answers = [];
    show("q-play");
    render();
  }

  function render() {
    var item = order[idx], q = item.q, n = order.length;
    $("q-counter").textContent = (idx + 1) + "/" + n;
    $("q-topic").textContent = q.t;
    $("q-score").textContent = score;
    $("q-bar").style.width = (idx / n * 100) + "%";
    $("q-barwrap").setAttribute("aria-valuenow", idx);
    var fig = $("q-fig"), img = $("q-img");
    var oldFb = fig.querySelector(".img-fallback"); if (oldFb) oldFb.remove();
    if (q.img) {
      fig.hidden = false; img.style.display = ""; img.classList.remove("loaded");
      img.alt = q.alt || ""; img.src = q.img; $("q-cr").innerHTML = q.cr || "";
      if (window.__handleImg) window.__handleImg(img);
    } else { fig.hidden = true; img.removeAttribute("src"); }
    $("q-question").textContent = q.q;
    var box = $("q-options"); box.innerHTML = "";
    item.opts.forEach(function (o, i) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "q-opt";
      b.innerHTML = '<span class="q-letter">' + LETTERS[i] + "</span><span>" + esc(o.text) + "</span>";
      b.addEventListener("click", function () { choose(i); });
      box.appendChild(b);
    });
    $("q-feedback").hidden = true;
    $("q-next").hidden = true;
    var card = $("quiz");
    if (card.getBoundingClientRect().top < 0) card.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function choose(i) {
    var item = order[idx], btns = $("q-options").querySelectorAll(".q-opt");
    var correctIdx = item.opts.findIndex(function (o) { return o.correct; });
    var ok = i === correctIdx;
    if (ok) score++;
    answers.push({ q: item.q.q, ok: ok, chosen: item.opts[i].text, right: item.opts[correctIdx].text });
    btns.forEach(function (b, j) {
      b.disabled = true;
      if (j === correctIdx) b.classList.add("correct");
      else if (j === i) b.classList.add("wrong");
      else b.classList.add("dim");
    });
    var fb = $("q-feedback");
    fb.className = "q-feedback " + (ok ? "ok" : "bad");
    fb.innerHTML = "<h3>" + (ok ? "Správne!" : "Nesprávne") + "</h3>" +
      (ok ? "" : "<p><strong>Správna odpoveď: " + LETTERS[correctIdx] + ") " + esc(item.opts[correctIdx].text) + "</strong></p>") +
      "<p>" + esc(item.q.e) + "</p>";
    fb.hidden = false;
    $("q-score").textContent = score;
    $("q-bar").style.width = ((idx + 1) / order.length * 100) + "%";
    var nx = $("q-next");
    nx.hidden = false;
    nx.firstChild.textContent = idx === order.length - 1 ? "Zobraziť výsledok " : "Ďalšia otázka ";
    nx.focus({ preventScroll: true });
  }

  function next() { idx++; if (idx < order.length) render(); else finish(); }

  function finish() {
    show("q-result");
    var n = order.length, pct = Math.round(score / n * 100);
    $("q-final").textContent = score;
    $("q-percent").textContent = "Úspešnosť: " + pct + " %";
    var v, sub;
    if (score <= 7) { v = "Potrebuješ si zopakovať učivo."; sub = "Prejdi si tematické podstránky a skús to znova."; }
    else if (score <= 13) { v = "Priemerné vedomosti."; sub = "Základ máš, no niektoré témy si ešte zopakuj."; }
    else if (score <= 17) { v = "Veľmi dobré vedomosti."; sub = "Učivo ovládaš veľmi dobre, chýba už len kúsok."; }
    else { v = "Výborné, ovládaš tému!"; sub = "Gratulujeme – v dejinách Slovenska v Habsburskej monarchii sa vyznáš."; }
    $("q-verdict").textContent = v; $("q-verdict-sub").textContent = sub;
    var fg = $("q-ringfg"), C = 326.7;
    fg.style.stroke = score <= 7 ? "var(--bad)" : score <= 13 ? "var(--gold)" : "var(--ok)";
    fg.style.strokeDashoffset = C;
    requestAnimationFrame(function () { requestAnimationFrame(function () { fg.style.strokeDashoffset = C * (1 - score / n); }); });
    $("q-review").innerHTML = answers.map(function (a) {
      return "<li>" + esc(a.q) + "<br>" + (a.ok ? '<span class="r-ok">✓ ' + esc(a.chosen) + "</span>"
        : '<span class="r-bad">✗ ' + esc(a.chosen) + '</span> → <span class="r-ok">' + esc(a.right) + "</span>") + "</li>";
    }).join("");
    $("quiz").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  $("q-begin").addEventListener("click", start);
  $("q-next").addEventListener("click", next);
  $("q-restart").addEventListener("click", start);
})();
