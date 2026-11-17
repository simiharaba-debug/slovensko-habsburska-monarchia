import json, re, os, html
from images import IMAGES, url, page
from content import PAGES, STUDY
from quiz import QUIZ

OUT = os.path.join(os.path.dirname(__file__), "..", "site")
SITE = "Slovensko v Habsburskej monarchii"

ICONS = {
 "crescent": '<path d="M15 3a9 9 0 1 0 6 15.7A7.5 7.5 0 0 1 15 3z"/><path d="m18 8 .9 1.8 2 .3-1.5 1.4.4 2-1.8-1-1.8 1 .4-2L15.1 10l2-.3z"/>',
 "swords": '<path d="M14.5 17.5 3 6V3h3l11.5 11.5"/><path d="m13 19 6-6M16 16l4 4M19 21l2-2"/><path d="M9.5 6.5 21 18v3h-3L6.5 9.5"/><path d="m11 5-6 6M8 8 4 4M5 3 3 5"/>',
 "flag": '<path d="M4 22V4"/><path d="M4 4h12l-2 4 2 4H4"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
 "pick": '<path d="M14 6c4-2 7 1 7 1s-3-1-6 1"/><path d="M14 6c-2 4 1 7 1 7s-1-3 1-6"/><path d="M15 9 3 21"/>',
 "light": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>',
 "scroll": '<path d="M8 21h10a2 2 0 0 0 2-2V5"/><path d="M8 21a2 2 0 0 1-2-2V5a2 2 0 0 0-2-2h12a2 2 0 0 1 2 2"/><path d="M10 8h6M10 12h6M10 16h4"/>',
 "cannon": '<circle cx="7" cy="17" r="3"/><path d="m9 15 11-8-2-3L6 12"/><path d="M3 21h8"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "mountain": '<path d="m3 20 6-11 4 6 2-3 6 8z"/>',
 "crown": '<path d="m3 8 4 4 5-7 5 7 4-4-2 11H5z"/><path d="M5 21h14"/>',
 "coins": '<ellipse cx="9" cy="7" rx="6" ry="3"/><path d="M3 7v4c0 1.7 2.7 3 6 3s6-1.3 6-3V7"/><path d="M9 14v3c0 1.7 2.7 3 6 3s6-1.3 6-3v-4c0-1.7-2.7-3-6-3"/>',
 "castle": '<path d="M3 21V9h3V6h3v3h2V6h2v3h2V6h3v3h3v12z"/><path d="M10 21v-5h4v5"/>',
 "fire": '<path d="M12 22c4 0 7-3 7-7 0-5-5-8-5-13-3 2-4 5-4 7-1-1-2-2-2-4-2 2-3 5-3 8 0 5 3 9 7 9z"/>',
 "scale": '<path d="M12 3v18M7 21h10M5 7h14"/><path d="m5 7-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
 "down": '<path d="M3 6l7 7 4-4 7 7"/><path d="M15 16h6v-6"/>',
 "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6.5 7-6.5s7 2.5 7 6.5"/><circle cx="17.5" cy="9" r="2.5"/><path d="M17 14.5c3 0 5 2 5 5"/>',
 "map": '<path d="m9 4-6 2v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "wheat": '<path d="M12 22V10"/><path d="M12 10c-3 0-4-3-4-5 3 0 4 3 4 5zM12 10c3 0 4-3 4-5-3 0-4 3-4 5zM12 15c-3 0-4-3-4-5 3 0 4 3 4 5zM12 15c3 0 4-3 4-5-3 0-4 3-4 5z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "flask": '<path d="M9 3h6M10 3v6L4 20a1 1 0 0 0 1 1.5h14A1 1 0 0 0 20 20L14 9V3"/><path d="M7 15h10"/>',
 "factory": '<path d="M3 21V10l6 4V10l6 4V4h6v17z"/><path d="M7 18h2M12 18h2M17 18h2"/>',
 "cross": '<path d="M12 2v20M6 8h12"/>',
 "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "quiz": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
 "home": '<path d="m3 11 9-8 9 8"/><path d="M5 10v11h14V10"/>',
}

def icon(name, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def credit(key):
    f, a, lic, d = IMAGES[key]
    return f'Foto: <a href="{page(key)}" target="_blank" rel="noopener">{html.escape(a)}</a>, Wikimedia Commons ({lic})'

def fig(key, cls=""):
    f, a, lic, d = IMAGES[key]
    w = 960 if any(c in cls for c in ("portrait","tall","narrow")) else 1280
    return (f'<figure class="fig {cls}"><div class="fig-img"><img src="{url(key, w)}" alt="{html.escape(d)}" loading="lazy" decoding="async"></div>'
            f'<figcaption><span>{html.escape(d)}</span><small>{credit(key)}</small></figcaption></figure>')

def render(body):
    body = re.sub(r"\[\[fig:(\w+)(?:\|([^\]]*))?\]\]", lambda m: fig(m.group(1), m.group(2) or ""), body)
    body = re.sub(r"\[\[icon:(\w+)\]\]", lambda m: icon(m.group(1)), body)
    return body

def nav(active):
    items = "".join(
        f'<a href="{p["slug"]}.html" class="dd-item{" is-active" if active==p["slug"] else ""}"><span class="dd-num">{p["num"]}</span>{p["short"]}</a>'
        for p in PAGES)
    def cls(x): return ' class="is-active"' if active == x else ""
    return f'''<a class="skip" href="#main">Preskočiť na obsah</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a href="index.html" class="brand" aria-label="Domov">
      <span class="brand-mark">{icon("crown")}</span>
      <span class="brand-text"><strong>Slovensko</strong><em>v Habsburskej monarchii</em></span>
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Hlavná navigácia">
      <a href="index.html"{cls("index")}>Úvod</a>
      <div class="dd">
        <button class="dd-toggle" aria-expanded="false" aria-haspopup="true">Témy <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg></button>
        <div class="dd-menu">{items}</div>
      </div>
      <a href="kviz.html" class="nav-cta{" is-active" if active=="kviz" else ""}">{icon("quiz")} Kvíz</a>
      <a href="zdroje.html"{cls("zdroje")}>Zdroje</a>
    </nav>
    <div class="header-actions">
      <button class="theme-toggle" id="theme-toggle" aria-label="Prepnúť svetlý/tmavý režim" title="Svetlý / tmavý režim">
        <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
      </button>
      <button class="burger" id="burger" aria-label="Otvoriť menu" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="progress" id="read-progress"></div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <a href="index.html" class="brand footer-brand"><span class="brand-mark">{icon("crown")}</span><span class="brand-text"><strong>Slovensko</strong><em>v Habsburskej monarchii</em></span></a>
      <p class="muted">Vzdelávací web o dejinách Slovenska v 16. – 18. storočí. Obsah vychádza výhradne zo študijného materiálu, fotografie pochádzajú z Wikimedia Commons.</p>
    </div>
    <div class="footer-links">
      <h4>Témy</h4>
      {"".join(f'<a href="{p["slug"]}.html">{p["short"]}</a>' for p in PAGES)}
    </div>
    <div class="footer-links">
      <h4>Ďalej</h4>
      <a href="kviz.html">Vedomostný kvíz</a>
      <a href="zdroje.html">Zdroje a fotografie</a>
      <a href="#top" class="to-top">Späť hore ↑</a>
    </div>
  </div>
</footer>'''

def doc(title, desc, active, main, extra_js="", og_img="presburg"):
    full = title if title == SITE else f"{title} | {SITE}"
    return f'''<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="keywords" content="Slovensko, Habsburská monarchia, Osmanská ríša, protiturecké vojny, stavovské povstania, reformácia, Mária Terézia, Jozef II., dejepis">
<meta name="theme-color" content="#7a1a22">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{url(og_img, 1280)}">
<meta property="og:locale" content="sk_SK">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Source+Sans+3:wght@400;500;600;700&display=swap&subset=latin-ext" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("theme");if(!t)t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";document.documentElement.dataset.theme=t}}catch(e){{document.documentElement.dataset.theme="light"}}</script>
</head>
<body id="top">
{nav(active)}
<main id="main">
{main}
</main>
{FOOTER}
<script src="js/main.js" defer></script>
{extra_js}
</body>
</html>
'''

def topic_page(i, p):
    prev = PAGES[i-1] if i > 0 else None
    nxt = PAGES[i+1] if i < len(PAGES)-1 else None
    hero_img = url(p["hero"], 1920 if p["hero"] not in ("rakoczi","suleiman","encyclopedie") else 1280)
    toc = "".join(f'<a href="#{a}">{t}</a>' for a, t in p["toc"])
    pn = '<nav class="pager wrap" aria-label="Navigácia medzi témami">'
    pn += (f'<a class="pager-link prev" href="{prev["slug"]}.html"><small>← Predchádzajúca téma</small><strong>{prev["short"]}</strong></a>' if prev
           else '<a class="pager-link prev" href="index.html"><small>← Späť</small><strong>Úvodná stránka</strong></a>')
    pn += f'<a class="pager-home" href="index.html" aria-label="Domov">{icon("home")}</a>'
    pn += (f'<a class="pager-link next" href="{nxt["slug"]}.html"><small>Nasledujúca téma →</small><strong>{nxt["short"]}</strong></a>' if nxt
           else f'<a class="pager-link next" href="kviz.html"><small>Otestuj sa →</small><strong>Vedomostný kvíz</strong></a>')
    pn += '</nav>'
    main = f'''<section class="page-hero">
  <div class="page-hero-bg"><img src="{hero_img}" alt="" fetchpriority="high"></div>
  <div class="wrap page-hero-inner">
    <nav class="crumbs" aria-label="Omrvinková navigácia"><a href="index.html">Úvod</a><span>/</span><span>Téma {p["num"]}</span></nav>
    <div class="page-hero-badge">{icon(p["icon"])}<span>Téma {p["num"]} / 0{len(PAGES)}</span></div>
    <h1>{p["title"]}</h1>
    <p class="lead">{p["lead"]}</p>
    <p class="hero-credit">{credit(p["hero"])}</p>
  </div>
</section>
<div class="toc-bar"><div class="wrap toc">{toc}</div></div>
<article class="wrap content">
{render(p["body"])}
</article>
{pn}'''
    return doc(p["title"], p["desc"], p["slug"], main, og_img=p["hero"])

def index_page():
    cards = ""
    for p in PAGES:
        cards += f'''<a class="topic-card reveal" href="{p["slug"]}.html">
  <div class="topic-img"><img src="{url(p["hero"], 960)}" alt="{html.escape(IMAGES[p["hero"]][3])}" loading="lazy"></div>
  <div class="topic-body">
    <span class="topic-num">{p["num"]}</span>
    <h3>{p["short"]}</h3>
    <p>{p["desc"]}</p>
    <span class="topic-more">Čítať tému {icon("arrow")}</span>
  </div>
</a>'''
    tl = [("1526","Bitka pri Moháči"),("1541","Turci dobyli Budín"),("1549","Confessio Pentapolitana"),("1604","Povstanie Š. Bočkaja"),
          ("1635","Univerzita v Trnave"),("1681","Šopronský snem"),("1683","2. obliehanie Viedne"),("1711","Satmársky mier"),
          ("1717","Oslobodenie Uhorska"),("1777","Ratio educationis"),("1781","Tolerančný patent")]
    tlh = "".join(f'<li><span>{y}</span><p>{t}</p></li>' for y, t in tl)
    main = f'''<section class="hero">
  <div class="hero-bg"><img src="{url("presburg", 1920)}" alt="Prešporok na rytine z roku 1686" fetchpriority="high"></div>
  <div class="wrap hero-inner">
    <p class="eyebrow">Národné dejiny · 16. – 18. storočie</p>
    <h1>Slovensko v Habsburskej monarchii</h1>
    <p class="lead">Turecké vpády, stavovské povstania, reformácia a protireformácia, baníctvo, osvietenstvo a reformy Márie Terézie a Jozefa II. – tri storočia, ktoré formovali dnešné Slovensko.</p>
    <div class="hero-actions">
      <a href="{PAGES[0]["slug"]}.html" class="btn btn-primary">Začať čítať {icon("arrow")}</a>
      <a href="kviz.html" class="btn btn-ghost">{icon("quiz")} Vyskúšať kvíz</a>
    </div>
    <p class="hero-credit">{credit("presburg")}</p>
  </div>
</section>

<section class="stats wrap reveal">
  <div><strong>3</strong><span>storočia dejín</span></div>
  <div><strong>7</strong><span>tematických celkov</span></div>
  <div><strong>150</strong><span>rokov osmanskej nadvlády nad nížinami Uhorska</span></div>
  <div><strong>20</strong><span>otázok vo vedomostnom kvíze</span></div>
</section>

<section class="wrap section">
  <div class="section-head reveal"><p class="eyebrow">Tematické oblasti</p><h2>Vyber si tému</h2><p class="muted">Každá téma má vlastnú podstránku s prehľadným výkladom, časovými osami a dobovými obrazmi.</p></div>
  <div class="topics">{cards}</div>
</section>

<section class="band reveal">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Časová os</p><h2>Kľúčové medzníky</h2></div>
    <ol class="hscroll">{tlh}</ol>
  </div>
</section>

<section class="wrap section">
  <a class="quiz-teaser reveal" href="kviz.html">
    <div class="qt-icon">{icon("quiz")}</div>
    <div><p class="eyebrow">Vedomostný kvíz</p><h2>Koľko si zapamätáš?</h2><p>20 otázok strednej náročnosti zo všetkých tém. Po každej odpovedi uvidíš vysvetlenie.</p></div>
    <span class="btn btn-primary">Spustiť kvíz {icon("arrow")}</span>
  </a>
</section>'''
    return doc(SITE, "Interaktívny vzdelávací web o dejinách Slovenska v Habsburskej monarchii v 16. – 18. storočí: protiturecké vojny, stavovské povstania, reformácia, hospodárstvo, osvietenstvo a reformy Márie Terézie a Jozefa II. S kvízom.", "index", main)

def quiz_page():
    data = []
    for q in QUIZ:
        d = dict(t=q["t"], q=q["q"], o=q["o"], a=q["a"], e=q["e"])
        if q.get("img"):
            d["img"] = url(q["img"], 960); d["alt"] = "Ilustračný dobový obraz k otázke"; d["cr"] = credit(q["img"])
        data.append(d)
    main = f'''<section class="page-hero small">
  <div class="page-hero-bg"><img src="{url("damel", 1920)}" alt=""></div>
  <div class="wrap page-hero-inner">
    <nav class="crumbs"><a href="index.html">Úvod</a><span>/</span><span>Kvíz</span></nav>
    <h1>Vedomostný kvíz</h1>
    <p class="lead">Otestuj, čo vieš o Slovensku v Habsburskej monarchii.</p>
  </div>
</section>
<div class="wrap quiz-wrap">
  <div class="quiz-card" id="quiz" aria-live="polite">
    <div class="quiz-screen" id="q-start">
      <div class="q-badge">{icon("quiz")}</div>
      <h2>Slovensko v 16. – 18. storočí</h2>
      <ul class="rules">
        <li><strong>20 otázok</strong> zo všetkých tematických oblastí</li>
        <li>Každá otázka má <strong>4 možnosti</strong> (A – D), správna je vždy <strong>iba jedna</strong></li>
        <li>Po odpovedi hneď uvidíš, či si mal(a) pravdu, aj s vysvetlením</li>
        <li>Za každú správnu odpoveď získaš <strong>1 bod</strong> – maximum je 20</li>
      </ul>
      <button class="btn btn-primary btn-lg" id="q-begin">Začať kvíz {icon("arrow")}</button>
    </div>
    <div class="quiz-screen" id="q-play" hidden>
      <div class="q-top">
        <span class="q-counter" id="q-counter">1/20</span>
        <span class="q-topic" id="q-topic"></span>
        <span class="q-score">Body: <strong id="q-score">0</strong></span>
      </div>
      <div class="q-bar" role="progressbar" aria-valuemin="0" aria-valuemax="20" aria-valuenow="0" id="q-barwrap"><div id="q-bar"></div></div>
      <figure class="q-fig" id="q-fig" hidden><img id="q-img" alt=""><figcaption id="q-cr"></figcaption></figure>
      <h2 class="q-question" id="q-question"></h2>
      <div class="q-options" id="q-options"></div>
      <div class="q-feedback" id="q-feedback" hidden></div>
      <div class="q-actions"><button class="btn btn-primary" id="q-next" hidden>Ďalšia otázka {icon("arrow")}</button></div>
    </div>
    <div class="quiz-screen" id="q-result" hidden>
      <div class="ring" id="q-ring"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" class="ring-bg"/><circle cx="60" cy="60" r="52" class="ring-fg" id="q-ringfg"/></svg><div class="ring-txt"><strong id="q-final">0</strong><span>z 20</span></div></div>
      <p class="q-percent" id="q-percent"></p>
      <h2 id="q-verdict"></h2>
      <p class="muted" id="q-verdict-sub"></p>
      <div class="hero-actions center"><button class="btn btn-primary" id="q-restart">Zopakovať kvíz</button><a class="btn btn-ghost" href="index.html">Späť na úvod</a></div>
      <details class="review"><summary>Prehľad odpovedí</summary><ol id="q-review"></ol></details>
    </div>
  </div>
</div>'''
    js = '<script>window.QUIZ=' + json.dumps(data, ensure_ascii=False) + ';</script>\n<script src="js/quiz.js" defer></script>'
    return doc("Vedomostný kvíz", "Interaktívny kvíz s 20 otázkami o Slovensku v Habsburskej monarchii v 16. – 18. storočí.", "kviz", main, js, og_img="damel")

def sources_page():
    used = []
    for k in IMAGES:
        used.append(k)
    rows = "".join(f'<tr><td><img src="{url(k, 330)}" alt="" loading="lazy"></td><td>{html.escape(IMAGES[k][3])}</td><td>{html.escape(IMAGES[k][1])}</td><td>{IMAGES[k][2]}</td><td><a href="{page(k)}" target="_blank" rel="noopener">Commons</a></td></tr>' for k in used)
    study = "".join(f"<li>{html.escape(s)}</li>" for s in STUDY)
    main = f'''<section class="page-hero small plain">
  <div class="wrap page-hero-inner">
    <nav class="crumbs"><a href="index.html">Úvod</a><span>/</span><span>Zdroje</span></nav>
    <h1>Zdroje</h1>
    <p class="lead">Odkiaľ pochádza obsah a fotografie tohto webu.</p>
  </div>
</section>
<article class="wrap content">
  <section class="block">
    <h2>Obsah</h2>
    <p>Všetok vzdelávací text a otázky kvízu vychádzajú výhradne zo študijného materiálu <strong>„Slovensko v Habsburskej monarchii v 16. – 18. storočí“</strong>, ktorý uvádza tieto študijné zdroje:</p>
    <ul class="facts">{study}</ul>
  </section>
  <section class="block">
    <h2>Fotografie a obrazy</h2>
    <p>Všetky obrázky pochádzajú z <a href="https://commons.wikimedia.org" target="_blank" rel="noopener">Wikimedia Commons</a> a sú voľné dielo (Public domain) alebo pod licenciou Creative Commons. Obrázky sa načítavajú priamo z Wikimedia Commons.</p>
    <div class="table-wrap"><table class="src-table"><thead><tr><th>Náhľad</th><th>Popis</th><th>Autor</th><th>Licencia</th><th>Zdroj</th></tr></thead><tbody>{rows}</tbody></table></div>
  </section>
</article>'''
    return doc("Zdroje", "Zdroje obsahu a fotografií webu Slovensko v Habsburskej monarchii.", "zdroje", main)

def notfound():
    main = f'''<section class="page-hero small plain"><div class="wrap page-hero-inner"><h1>Stránka sa nenašla</h1><p class="lead">Táto stránka neexistuje. Skús začať od úvodu.</p><div class="hero-actions"><a class="btn btn-primary" href="index.html">Na úvodnú stránku</a></div></div></section>'''
    return doc("Stránka sa nenašla", "Stránka sa nenašla.", "", main)

def main():
    os.makedirs(OUT, exist_ok=True)
    w = lambda n, s: open(os.path.join(OUT, n), "w", encoding="utf-8").write(s)
    w("index.html", index_page())
    for i, p in enumerate(PAGES):
        w(p["slug"] + ".html", topic_page(i, p))
    w("kviz.html", quiz_page())
    w("zdroje.html", sources_page())
    w("404.html", notfound())
    w(".nojekyll", "")
    urls = ["index.html"] + [p["slug"]+".html" for p in PAGES] + ["kviz.html","zdroje.html"]
    print("ok", len(urls))

if __name__ == "__main__":
    main()
