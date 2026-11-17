# Obsah webu – výhradne podľa dokumentu „Slovensko v Habsburskej monarchii v 16. – 18. storočí“.
# Značky: [[fig:kľúč|trieda]] = fotografia s popisom a zdrojom.

PAGES = [
# ---------------------------------------------------------------- 1
dict(
slug="osmanska-risa", num="01", short="Osmanská ríša",
title="Osmanská ríša",
icon="crescent", hero="suleiman",
lead="Od turkických kmeňov pri Kaspickom mori až po vznik Tureckej republiky – vzostup a pád veľmoci, ktorá na stáročia ovplyvnila osud Uhorska aj Slovenska.",
desc="Vznik a expanzia Osmanskej ríše, janičiari, delostrelectvo, Sulejman I. Nádherný, obliehania Viedne a zánik ríše.",
toc=[("vznik","Vznik ríše"),("vojsko","Vojenská sila"),("expanzia","Expanzia"),("upadok","Vrchol a úpadok")],
body="""
<section id="vznik" class="block reveal">
  <h2><span class="h-num">1</span>Vznik ríše</h2>
  <div class="split">
    <div>
      <p>Turkické kmene od <strong>Kaspického mora</strong> vpadli na Blízky východ a do Byzancie už v <strong>11. storočí</strong> – boli to <strong>Seldžuckí Turci</strong>. Ich príbuzní sa usadili južne od Carihradu v meste <strong>Bursa</strong>.</p>
      <p>Koncom <strong>13. storočia</strong> založil ich vodca <strong>Osman I.</strong> novú dynastiu – podľa neho dostala ríša meno <strong>Osmanská ríša</strong>.</p>
      <div class="callout"><span class="callout-ico">i</span><div><strong>Pre študentov:</strong> materiál upozorňuje, že k tejto téme si treba povinne naštudovať aj prezentáciu v angličtine.</div></div>
    </div>
    [[fig:devsirme|tall]]
  </div>
</section>

<section id="vojsko" class="block reveal">
  <h2><span class="h-num">2</span>Vyspelé vojenstvo</h2>
  <p>Rýchlu územnú expanziu osmanských Turkov umožnilo <strong>vyspelé vojenstvo</strong>.</p>
  <div class="cards two">
    <article class="card">
      <div class="card-ico">[[icon:cannon]]</div>
      <h3>Strelné zbrane</h3>
      <p>Muškety a najmä <strong>prvé masové nasadenie delostrelectva</strong>.</p>
    </article>
    <article class="card">
      <div class="card-ico">[[icon:shield]]</div>
      <h3>Janičiari</h3>
      <p>Z tureckého <em>jeni çeri</em> = „cudzie vojsko“. Elitné pechotné zbory z <strong>odmala vycvičených kresťanských chlapcov</strong> – fanatickí a oddaní strelci.</p>
    </article>
  </div>
  [[fig:janissary|center narrow]]
</section>

<section id="expanzia" class="block reveal">
  <h2><span class="h-num">3</span>Územná expanzia</h2>
  <ol class="timeline">
    <li><span class="t-date">14. stor.</span><div>Osmani dobyli <strong>Anatóliu, Grécko, Srbsko</strong> (bitka na Kosovom poli 1389), <strong>Bulharsko</strong> (bitka pri Nikopole 1396), Blízky východ a severnú Afriku.</div></li>
    <li><span class="t-date">1389</span><div><strong>Bitka na Kosovom poli</strong> – podrobenie Srbska.</div></li>
    <li><span class="t-date">1396</span><div><strong>Bitka pri Nikopole</strong> – podrobenie Bulharska.</div></li>
    <li><span class="t-date">1453</span><div>Dobytie <strong>Carihradu</strong> (materiál uvádza Murada II.) – mesto sa stalo novým hlavným mestom <strong>Istanbul</strong>.</div></li>
    <li><span class="t-date">15. stor.</span><div>Vojny s <strong>Uhorskom</strong> – Varna, Belehrad; podriadenie si vazalského <strong>Valašska</strong> (Vlad Tepeș) a <strong>Moldavska</strong>; boje s krymskými Tatármi proti Poľsko-Litovskej únii a kozákom.</div></li>
  </ol>
</section>

<section id="upadok" class="block reveal">
  <h2><span class="h-num">4</span>Vrchol, porážky a zánik</h2>
  <div class="split rev">
    [[fig:suleiman|tall]]
    <div>
      <ol class="timeline compact">
        <li><span class="t-date">16. stor.</span><div><strong>Vrchol ríše za Sulejmana I. Nádherného</strong> – zákonník, dobytie Uhorska (1521 – 1526 – 1541), 1. obliehanie Viedne (1529).</div></li>
        <li><span class="t-date">1571</span><div><strong>Námorná bitka pri Lepante</strong> proti katolíckej koalícii – <strong>1. porážka</strong> Osmanov.</div></li>
        <li><span class="t-date">1683</span><div><strong>2. obliehanie Viedne</strong> – kľúčová porážka od koalície Habsburgovcov a Poliakov.</div></li>
        <li><span class="t-date">1717</span><div>Vyhnanie Osmanov z Uhorska.</div></li>
        <li><span class="t-date">19. stor.</span><div>Úpadok – povstania janičiarov, úpadok dvora, tlak Rusov na Balkáne.</div></li>
        <li><span class="t-date">1920</span><div>Po porážke v 1. svetovej vojne <strong>zánik Osmanskej dynastie</strong>.</div></li>
        <li><span class="t-date">1923</span><div>Vznik <strong>Tureckej republiky</strong>.</div></li>
      </ol>
    </div>
  </div>
</section>
"""),
# ---------------------------------------------------------------- 2
dict(
slug="proturecke-vojny", num="02", short="Protiturecké vojny",
title="Protiturecké vojny",
icon="swords", hero="mohacs",
lead="Moháč, rozdelenie Uhorska na tri časti, život na pohraničí plnom rabovania a napokon víťazstvo pri Viedni – takmer dve storočia bojov o strednú Európu.",
desc="Bitka pri Moháči 1526, rozdelenie Uhorska, Prešporok ako hlavné mesto, život na pohraničí, sandžaky, 2. obliehanie Viedne 1683 a oslobodenie Uhorska.",
toc=[("pociatky","Počiatky"),("mohac","Moháč 1526"),("rozdelenie","Rozdelenie Uhorska"),("pohranicie","Život na pohraničí"),("viden","Viedeň 1683"),("oslobodenie","Oslobodenie")],
body="""
<blockquote class="verse reveal">
  <p>„Ide Turek pri Dunaji, šabľa sa mu blýska,<br>ide Nemec vedľa neho, len plecima stíska,<br>ide Maďar vedľa neho, vykrúca si fúzy,<br>ide Slovák proti nemu, Turek utiecť musí!“</p>
  <cite>ľudová pieseň uvedená v študijnom materiáli</cite>
</blockquote>

<section id="pociatky" class="block reveal">
  <h2><span class="h-num">1</span>Počiatky bojov</h2>
  <ul class="facts">
    <li>Uhorsko viedlo vojnu proti Osmanským Turkom <strong>od 15. storočia</strong> – bránilo osmanskej expanzii na Balkán (<strong>Žigmund Luxemburský, Vladislav I. Jagellovský, Matej Korvín</strong>).</li>
    <li>Za vlády <strong>Jagellovcov</strong> sa Uhorsko oslabilo – Turci to využili.</li>
    <li><strong>1521</strong> – Turci dobyli <strong>Belehrad</strong>.</li>
  </ul>
</section>

<section id="mohac" class="block reveal">
  <h2><span class="h-num">2</span>Bitka pri Moháči</h2>
  <div class="highlight-date"><span>29. 8. 1526</span><p>Po bitke <strong>Sulejman I. Nádherný</strong> vyplienil <strong>Budín</strong> a z Uhorska odtiahol.</p></div>
  [[fig:mohacs|wide]]
</section>

<section id="rozdelenie" class="block reveal">
  <h2><span class="h-num">3</span>Rozdelenie Uhorska na tri časti</h2>
  <div class="split">
    <div>
      <p>Trón pripadol <strong>Ferdinandovi I. Habsburgovi</strong>, no časť šľachty zvolila za kráľa uhorského veľmoža a sedmohradské knieža <strong>Jána Zápoľského</strong> (János Zápolyi), ktorého podporovali Turci. Nasledovali <strong>boje o trón</strong> – korunovaný bol aj Ferdinand.</p>
      <p><strong>1529</strong> – nová výprava Turkov do Uhorska: <strong>200-tisícová armáda obliehala Viedeň</strong>. Obliehanie bolo neúspešné <strong>iba kvôli počasiu</strong>; cestou späť Turci rabovali Slovensko.</p>
      <p>Keď Zápoľský napokon uznal nárok Habsburgovcov na trón, Turci vtrhli do Uhorska a <strong>dobyli Budín (1541)</strong>.</p>
    </div>
    [[fig:vienna1529|tall]]
  </div>
  <div class="cards three">
    <article class="card tone-red">
      <div class="card-ico">[[icon:crescent]]</div>
      <h3>Budínsky pašalik</h3>
      <p>Celé nížinaté oblasti Uhorska sa na <strong>150 rokov</strong> stali súčasťou Osmanskej ríše.</p>
    </article>
    <article class="card tone-gold">
      <div class="card-ico">[[icon:mountain]]</div>
      <h3>Sedmohradsko</h3>
      <p>Transylvánia, Potisie, Podkarpatská Rus – de facto <strong>samostatné kniežatstvo</strong>, vazal Osmanskej ríše, usilujúce sa o celouhorský odboj voči Habsburgovcom.</p>
    </article>
    <article class="card tone-ink">
      <div class="card-ico">[[icon:crown]]</div>
      <h3>Kráľovské Uhorsko</h3>
      <p>Územia pod vládou Habsburgovcov – <strong>Slovensko, Západné Maďarsko a Chorvátsko</strong>.</p>
    </article>
  </div>
  <div class="split rev">
    [[fig:merian]]
    <div class="callout big"><span class="callout-ico">★</span><div><strong>Prešporok (Bratislava)</strong> sa stal hlavným a korunovačným mestom Uhorska – po dobytí Budína a Stoličného Belehradu (Székesfehérvár). Po dobytí Ostrihomu sa hlavný arcibiskup presťahoval do <strong>Trnavy</strong>.</div></div>
  </div>
</section>

<section id="pohranicie" class="block reveal">
  <h2><span class="h-num">4</span>Vojenské operácie a život na pohraničí</h2>
  <ul class="facts">
    <li>Rýchlejšiemu postupu Turkov bránili <strong>vojny s Perziou</strong>; obdobia prímeria sa striedali s otvorenými konfliktami – napr. <strong>15-ročná vojna (1591 – 1606)</strong>. (Téme sa venuje aj Červenákova knižná séria Stein &amp; Barbarič.)</li>
    <li>Vojenské ťaženia Turci často viedli na <strong>podporu protestantov v 30-ročnej vojne</strong> a uhorskej šľachty v protihabsburských povstaniach.</li>
    <li>Pohraničie bolo takmer neustále vystavené <strong>rabovaniu, útokom, vraždám, vypaľovaniu dedín</strong>, vymáhaniu daní za mier (daň z dieťaťa) – výhražné listy, vydieranie, výpalné, únosy obyvateľstva do otroctva, háremov a janičiarskeho vojska.</li>
    <li><strong>Línia plienenia:</strong> Považie po Púchov – Horná Nitra – Turiec – Banská Bystrica – Gemer.</li>
  </ul>

  <h3 class="sub">Ako sa krajina bránila</h3>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:coins]]</div><h3>Slabá obrana</h3><p>Habsburgovci mali <strong>žoldniersku armádu</strong> z nemeckých a českých krajín, Talianska a Španielska – rabovala a znásilňovala rovnako. Šľachta nemala chuť bojovať, búrila sa.</p></article>
    <article class="card"><div class="card-ico">[[icon:castle]]</div><h3>Mestá a domobrana</h3><p>Obranu organizovali mestá (<strong>Zväz stredoslovenských banských miest, Banský kapitanát</strong>); vidiecke obyvateľstvo organizovalo milície, domobranu.</p></article>
    <article class="card"><div class="card-ico">[[icon:fire]]</div><h3>Výstražný systém</h3><p><strong>Vartovky</strong> (Krupina), <strong>vatrári</strong> na kopcoch. Niektoré mestá sa nanovo opevnili podľa návrhov talianskych architektov (Banská Štiavnica).</p></article>
  </div>
  <div class="split">
    <div>
      <p>Boli vystavané <strong>nové moderné pevnosti</strong> – <strong>Komárno</strong> a <strong>Nové Zámky</strong>.</p>
      <p>Turci postupne dobyli časť južného Slovenska a zriadili tam svoju štátnu správu – <strong>sandžaky</strong> (ostrihomský, novohradský, sečiansky, fiľakovský). Život tam bol pre poddaných niekedy <strong>znesiteľnejší</strong> ako v pohraničí.</p>
      <div class="two-lists">
        <div class="mini red"><h4>Dobyté mestá</h4><p>Ostrihom – Štúrovo, Komárno, Nové Zámky, Nitra, Levice, Pukanec, Šahy, Fiľakovo, Sečany, Muráň na Gemeri</p></div>
        <div class="mini green"><h4>Nikdy nedobyté</h4><p>Banská Štiavnica, Krupina, Zvolen – rabovanie siahalo až po Poniky pri Banskej Bystrici</p></div>
      </div>
    </div>
    [[fig:neuhausel]]
  </div>
</section>

<section id="viden" class="block reveal">
  <h2><span class="h-num">5</span>Druhé obliehanie Viedne (1683)</h2>
  <p>V roku <strong>1677</strong> vypuklo povstanie <strong>Imricha Tököliho</strong>, ktorý obsadil celé Slovensko. Na pomoc mu v roku 1683 prišla <strong>200-tisícová osmanská armáda Kara Mustafu</strong>, ktorá obliehala Viedeň <strong>3 mesiace</strong>.</p>
  <p>Viedeň bránilo už len <strong>pár stoviek obrancov</strong>, keď dorazili spojenecké vojská zo západnej Európy pod velením <strong>Eugena Savojského</strong> a <strong>Karola Lotrinského</strong> a <strong>poľsko-litovská jazda Jána III. Sobieskeho</strong> – a Turkov porazili.</p>
  [[fig:vienna1683|wide]]
</section>

<section id="oslobodenie" class="block reveal">
  <h2><span class="h-num">6</span>Oslobodenie Uhorska</h2>
  <div class="split rev">
    [[fig:nz1685]]
    <ol class="timeline compact">
      <li><span class="t-date">1685</span><div>Spojenecké vojská rýchlo vyhnali Turkov zo Slovenska – <strong>padli Nové Zámky</strong>; neskôr dobyli Budín.</div></li>
      <li><span class="t-date">1697</span><div>Rozhodujúce víťazstvo <strong>pri Zente</strong>, Srbsko.</div></li>
      <li><span class="t-date">1699</span><div><strong>Karlovacký mier</strong>.</div></li>
      <li><span class="t-date">1717</span><div>Dobytie <strong>Belehradu</strong> a <strong>definitívne oslobodenie Uhorska</strong> spod osmanskej nadvlády.</div></li>
    </ol>
  </div>
</section>
"""),
# ---------------------------------------------------------------- 3
dict(
slug="povstania", num="03", short="Stavovské povstania",
title="Protihabsburské stavovské povstania",
icon="flag", hero="rakoczi",
lead="Kuruci proti labancom: päť povstaní uhorskej šľachty za stavovské práva a náboženskú slobodu – od Štefana Bočkaja po Františka II. Rákociho.",
desc="Príčiny stavovských povstaní, kuruci a labanci, povstania Bočkaja, Betlena, Juraja I. Rákociho, Tököliho a Františka II. Rákociho, Satmársky mier a následky.",
toc=[("priciny","Príčiny"),("armady","Kuruci a labanci"),("povstania","Päť povstaní"),("mier","Satmársky mier"),("nasledky","Následky")],
body="""
<section id="priciny" class="block reveal">
  <h2><span class="h-num">1</span>Prečo sa šľachta búrila</h2>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:crown]]</div><h3>Mocná šľachta</h3><p>Uhorsko malo vplyvnú šľachtu: vyššiu – <strong>magnátov</strong> a nižšiu – <strong>zemanov</strong>. Nechceli sa zmieriť s vládou Habsburgovcov, ktorí vládli pevnou rukou.</p></article>
    <article class="card"><div class="card-ico">[[icon:scale]]</div><h3>Absolutizmus</h3><p>Habsburgovci potláčali stavovské práva a slobody šľachty, aby vybudovali <strong>silnú absolutistickú a centralizovanú monarchiu</strong>; podporovali rekatolizáciu.</p></article>
    <article class="card"><div class="card-ico">[[icon:book]]</div><h3>Náboženstvo</h3><p>Šľachta boli <strong>protestanti</strong> (kalvíni a evanjelici) – odboj mal <strong>stavovské aj náboženské</strong> dôvody.</p></article>
  </div>
</section>

<section id="armady" class="block reveal">
  <h2><span class="h-num">2</span>Kuruci a labanci</h2>
  <div class="versus">
    <div class="side kuruc">
      <h3>Povstalci – kuruci</h3>
      <ul>
        <li>Na čele povstania stálo <strong>sedmohradské knieža</strong>.</li>
        <li>Armádu okrem šľachty tvorili sedliaci, poddaní a nepravidelné vojsko – <strong>kuruci, hajdúsi</strong>.</li>
        <li>Etnickí Maďari, Valasi-Rumuni, Rusíni, Slováci – evanjelici, kalvíni, pravoslávni.</li>
        <li>Kuruci boli <strong>spojenci Turkov</strong>; centrá – <strong>Košice, Užhorod, Mukačevo</strong>.</li>
      </ul>
    </div>
    <div class="vs">VS</div>
    <div class="side labanc">
      <h3>Kráľovské armády – labanci</h3>
      <ul>
        <li>Na čele <strong>habsburský cisár</strong> (uhorský kráľ a rakúsky arcivojvoda).</li>
        <li>Žoldnierska armáda z Nemecka, Čiech, talianskych krajín a <strong>miestnych katolíkov</strong>.</li>
      </ul>
    </div>
  </div>
</section>

<section id="povstania" class="block reveal">
  <h2><span class="h-num">3</span>Päť povstaní</h2>
  <div class="uprisings">
    <article class="uprising"><div class="u-years">1604 – 1606</div><h3>Štefan Bočkaj <small>(Bocskay István)</small></h3><p>Proti rekatolizačnej politike <strong>Rudolfa II.</strong>; vybojoval <strong>náboženskú slobodu pre šľachtu</strong>.</p></article>
    <article class="uprising"><div class="u-years">1619 – 1629</div><h3>Gabriel Betlen <small>(Bethlen Gábor)</small></h3><p>V rámci <strong>podpory českých stavov v 30-ročnej vojne</strong>, až pri Viedni; získal náboženské slobody.</p></article>
    <article class="uprising"><div class="u-years">1644 – 1645</div><h3>Juraj I. Rákoci <small>(Rákóczi György)</small></h3><p>Podporoval <strong>Švédov a Francúzov</strong> v 30-ročnej vojne.</p></article>
    <article class="uprising"><div class="u-years">1677 – 1687</div><h3>Imrich Tököli</h3><p>Pochádzal z <strong>Kežmarku</strong>, nazývaný „tóth királyi“; obsadil celé Slovensko. Povstanie padlo po porážke Turkov pri Viedni. <strong>1687</strong> – Tököli ušiel k Turkom, ostatní vodcovia boli popravení – <strong>Prešovské jatky</strong>.</p></article>
    <article class="uprising big"><div class="u-years">1703 – 1711</div><h3>František II. Rákoci <small>(Rákóczi Ferenc)</small></h3>
      <div class="split">
        <div>
          <p><strong>Posledné a najväčšie povstanie</strong>, s podporou poddaných.</p>
          <ul class="facts">
            <li>Heslo <strong>„Pro Libertate“</strong> (Za slobodu); razil medené mince – <strong>libertáše</strong>.</li>
            <li>Nespokojnosť roľníkov viedla k strate podpory.</li>
            <li><strong>1707</strong> – turčianski zemani protestovali proti forme boja povstalcov – boli povraždení.</li>
            <li><strong>1708 – bitka pri Trenčíne</strong> – povstalci porazení.</li>
          </ul>
        </div>
        [[fig:rakoczi|portrait]]
      </div>
    </article>
  </div>
</section>

<section id="mier" class="block reveal">
  <div class="peace">
    <div class="peace-year">1711</div>
    <div>
      <h2>Satmársky mier</h2>
      <p class="muted">maď. Szatmár, rum. Satu Mare</p>
      <p>Šľachta <strong>uznala dedičné právo Habsburgovcov na uhorský trón</strong> a Habsburgovci šľachte sľúbili <strong>zachovať jej práva a výsady</strong>.</p>
    </div>
  </div>
</section>

<section id="nasledky" class="block reveal">
  <h2><span class="h-num">4</span>Následky protitureckých vojen a povstaní</h2>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:fire]]</div><h3>Rabovanie a zbojníctvo</h3><p>Slovensko rabovali <strong>tri armády</strong>; rozmach zbojníctva (<strong>Juraj Jánošík</strong>, popravený 1713).</p></article>
    <article class="card"><div class="card-ico">[[icon:down]]</div><h3>Úpadok</h3><p>Hospodársky, sociálny a kultúrny úpadok – územie Slovenska <strong>zaostalo</strong> oproti vyspelejším krajinám západnejšie (rovnako Maďarsko či Chorvátsko).</p></article>
    <article class="card"><div class="card-ico">[[icon:people]]</div><h3>Etnická skladba</h3><p>Etnická skladba Slovenska sa zmenila.</p></article>
    <article class="card"><div class="card-ico">[[icon:castle]]</div><h3>Opustené hrady</h3><p>Hrady boli opustené (šľachta si stavala luxusné <strong>kaštiele na rovine</strong>) alebo zničené, aby nemohli byť využité na protihabsburský odboj.</p></article>
    <article class="card"><div class="card-ico">[[icon:crown]]</div><h3>Absolutistický štát</h3><p>Habsburgovci definitívne získali vládu nad Uhorskom – mohli budovať <strong>absolutistický štát</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:map]]</div><h3>Balkán</h3><p>Mier s Turkami im umožnil okupovať <strong>Balkán</strong> až do 19. – 20. storočia.</p></article>
  </div>
</section>
"""),
# ---------------------------------------------------------------- 4
dict(
slug="reformacia", num="04", short="Reformácia a protireformácia",
title="Reformácia a protireformácia",
icon="book", hero="kezmarok",
lead="Kníhtlač, evanjelické mestá, habáni, jezuiti, Trnavská univerzita a artikulárne kostoly – náboženský život na Slovensku v 16. a 17. storočí.",
desc="Šírenie reformácie na Slovensku, Confessio Pentapolitana, Žilinská synoda, habáni, rekatolizácia, Trnavská univerzita, artikulárne kostoly, Užhorodská únia a humanistickí učenci.",
toc=[("reformacia","Reformácia"),("rekatolizacia","Rekatolizácia"),("uvolnenie","Artikulárne kostoly"),("ucenci","Humanistickí učenci")],
body="""
<section id="reformacia" class="block reveal">
  <h2><span class="h-num">1</span>Šírenie reformácie</h2>
  <ul class="facts">
    <li><strong>Kníhtlač</strong> rozvíjala vzdelanosť a gramotnosť všetkých vrstiev; národné jazyky rozvíjali národné uvedomenie.</li>
    <li>Reformácia sa šírila z <strong>nemeckých krajín</strong> prostredníctvom kupcov, študentov a pobielohorských českých emigrantov.</li>
    <li>Centrami reformácie boli <strong>banské a spišské mestá</strong> – nemeckí a slovenskí kazatelia. V 70. rokoch 16. storočia vznikla <strong>Kralická biblia</strong> (biblická čeština).</li>
    <li><strong>Maďarské obyvateľstvo</strong> zväčša prijalo <strong>kalvinizmus</strong>.</li>
  </ul>
  <ol class="timeline">
    <li><span class="t-date">1549</span><div>Päť východoslovenských miest (Košice, Prešov, Bardejov, Levoča, Sabinov) vydalo spoločné vyznanie viery – <strong>Confessio Pentapolitana</strong>. Prihlásili sa k evanjelickému vierovyznaniu; neskôr aj banské a spišské mestá.</div></li>
    <li><span class="t-date">1608</span><div><strong>Bratislavský snem</strong> schválil náboženskú slobodu aj pre poddaných a mešťanov.</div></li>
    <li><span class="t-date">1610</span><div><strong>Synoda v Žiline</strong> – luteráni sa oddelili od katolíckej cirkvi a zriadili vlastnú správu v rámci evanjelickej cirkvi – <strong>ECAV</strong>.</div></li>
  </ol>
  <div class="split">
    <div class="callout big"><span class="callout-ico">✦</span><div><strong>Habáni</strong> – novokrstenci (anabaptisti), ktorí sa zo Švajčiarska a z Moravy usadili na západnom Slovensku na <strong>200 rokov</strong>. Odmietali krst v ranom veku, žili v spoločných domoch, boli remeselníci. Neskôr odišli cez Ukrajinu do Severnej Ameriky.</div></div>
    [[fig:haban|portrait]]
  </div>
</section>

<section id="rekatolizacia" class="block reveal">
  <h2><span class="h-num">2</span>Rekatolizácia</h2>
  <div class="split">
    <div>
      <ul class="facts">
        <li>Nebola taká násilná ako v nemeckých a českých krajinách – <strong>Ferdinand I. a Maximilián II.</strong> boli tolerantní voči protestantom.</li>
        <li>Podľa záverov <strong>Tridentského koncilu</strong> sa za <strong>Rudolfa II.</strong> spustila rekatolizácia – ostrihomský arcibiskup <strong>Mikuláš Oláh</strong>, centrom bola <strong>Trnava</strong>.</li>
        <li><strong>1635</strong> – <strong>Peter Pazmáň</strong> založil v Trnave <strong>katolícku univerzitu</strong>; Trnava sa nazývala <strong>„slovenský Rím“</strong>.</li>
        <li><strong>Jezuiti</strong> získali budovy a školy – spočiatku boli mierni, neskôr násilne odoberali majetky protestantov, čo viedlo k vzburám a nepokojom.</li>
        <li><strong>Vrchol násilnej rekatolizácie</strong> za Leopolda I. (1657 – 1705) – protestantskí kňazi išli do väzenia alebo na <strong>galeje</strong> (nútené práce). Všeobecný odpor však donútil katolíkov rokovať.</li>
      </ul>
    </div>
    [[fig:trnava|tall]]
  </div>
</section>

<section id="uvolnenie" class="block reveal">
  <h2><span class="h-num">3</span>Uvoľnenie a nové cirkvi</h2>
  <div class="split rev">
    [[fig:kezmarok2]]
    <div>
      <div class="highlight-date"><span>1681</span><p><strong>Snem v Šoproni</strong> povolil evanjelikom <strong>dva drevené chrámy (artikulárne kostoly) v každej stolici</strong> a bohoslužby v slobodných kráľovských mestách. Evanjelici neboli rovnoprávni s katolíkmi, ale nastalo uvoľnenie.</p></div>
      <div class="highlight-date"><span>1646</span><p><strong>Užhorodská únia</strong> – časť pravoslávnych veriacich uznala zvrchovanosť pápeža a založila <strong>Gréckokatolícku cirkev</strong> (Slováci a Rusíni).</p></div>
      <p>V tomto období sa na Slovensku rozvíjal <strong>barok</strong>.</p>
    </div>
  </div>
</section>

<section id="ucenci" class="block reveal">
  <h2><span class="h-num">4</span>Humanistickí učenci</h2>
  <p>Významní slovenskí humanistickí učenci boli <strong>katolíci aj protestanti</strong>; pôsobilo tu aj množstvo evanjelických kňazov.</p>
  <div class="people">
    <div class="person"><span class="avatar">JS</span><h3>Ján Sambucus</h3><p>Dvorný historik Maximiliána II.</p></div>
    <div class="person"><span class="avatar">MS</span><h3>Martin Szentiványi</h3><p>(Svätojánsky) – rektor Trnavskej univerzity, encyklopédia.</p></div>
    <div class="person"><span class="avatar">JJ</span><h3>Ján Jesenius</h3><p>Rektor univerzít v Prahe a Wittenbergu.</p></div>
    <div class="person"><span class="avatar">JAK</span><h3>Ján Amos Komenský</h3><p>Pôsobil na Slovensku.</p></div>
  </div>
</section>
"""),
# ---------------------------------------------------------------- 5
dict(
slug="hospodarstvo-spolocnost", num="05", short="Hospodárstvo a spoločnosť",
title="Hospodárstvo, etnické pomery a panovníci",
icon="pick", hero="stiavnica",
lead="Meď z Banskej Bystrice, zlato a striebro zo Štiavnice, majere a poddaní, prisťahovalci z celej Európy – a habsburskí panovníci, ktorí vtedy vládli.",
desc="Baníctvo (Banská Štiavnica, Banská Bystrica), remeslá, poľnohospodárstvo, ľudové povstania a zbojníctvo, etnické zmeny na Slovensku a prehľad panovníkov 16. – 18. storočia.",
toc=[("banictvo","Baníctvo"),("polnohospodarstvo","Poľnohospodárstvo"),("vzbury","Vzbury a zbojníci"),("etnika","Etnické pomery"),("panovnici","Panovníci")],
body="""
<section id="banictvo" class="block reveal">
  <h2><span class="h-num">1</span>Baníctvo a remeslá</h2>
  <div class="split">
    <div>
      <div class="cards one">
        <article class="card tone-copper"><div class="card-ico">[[icon:pick]]</div><h3>Meď – Banská Bystrica</h3><p>Medené bane v okolí Banskej Bystrice. S meďou obchodovala <strong>Turzovsko-Fuggerovská spoločnosť</strong>, neskôr bane prevzal cisársky úrad – <strong>Banská komora</strong>.</p></article>
        <article class="card tone-gold"><div class="card-ico">[[icon:coins]]</div><h3>Zlato a striebro – Banská Štiavnica</h3><p><strong>1627</strong> – prvý odstrel <strong>pušným prachom</strong>; budovanie <strong>tajchov</strong>.</p></article>
      </div>
    </div>
    [[fig:stiavnica]]
  </div>
  <ol class="timeline compact">
    <li><span class="t-date">1579</span><div><strong>Banský poriadok Maximiliána II.</strong>, rozvoj lesníctva.</div></li>
    <li><span class="t-date">1627</span><div>Prvý odstrel pušným prachom v Banskej Štiavnici.</div></li>
    <li><span class="t-date">18. stor.</span><div>Rozvoj manufaktúr, baníctva a obchodu.</div></li>
    <li><span class="t-date">1762</span><div><strong>Banská akadémia</strong> v Banskej Štiavnici.</div></li>
  </ol>
  <p><strong>Remeslá:</strong> v mestách sa rozvíjali <strong>cechy</strong>, nastal rozmach obchodu.</p>
</section>

<section id="polnohospodarstvo" class="block reveal">
  <h2><span class="h-num">2</span>Poľnohospodárstvo</h2>
  <ul class="facts">
    <li><strong>Úpadok</strong> kvôli vojnám a <strong>ochladeniu v 17. storočí</strong>.</li>
    <li>Opustené hospodárstva obsadila šľachta – vznikali <strong>majere</strong>.</li>
  </ul>
  <div class="cards two">
    <article class="card"><div class="card-ico">[[icon:crown]]</div><h3>Dominikál</h3><p>Šľachtická pôda, na ktorej museli pracovať poddaní.</p></article>
    <article class="card"><div class="card-ico">[[icon:wheat]]</div><h3>Rustikál</h3><p>Malé roľnícke hospodárstva.</p></article>
  </div>
  <p>Plodiny z <strong>Nového sveta</strong> sa rozšírili až v 18. storočí. Rozmach hospodárstva nastal až po porážke stavovských povstalcov a Turkov v 18. storočí – najmä za <strong>Márie Terézie</strong>.</p>
</section>

<section id="vzbury" class="block reveal">
  <h2><span class="h-num">3</span>Ľudové povstania a zbojníctvo</h2>
  <p>Proti útlaku šľachty a zlým podmienkam vypukali časté ľudové povstania a rozmáhalo sa zbojníctvo. Ich vodcov čakali kruté tresty.</p>
  <div class="rebels">
    <div><span>1631</span><strong>Peter Császár</strong><em>rozštvrtený</em></div>
    <div><span>1672</span><strong>Gašpar Pika</strong><em>napichnutý na kôl</em></div>
    <div><span>1707</span><strong>Banícka vzbura v Banskej Štiavnici</strong><em>vzbúrenci zastrelení</em></div>
    <div><span>1713</span><strong>Juraj Jánošík</strong><em>zavesený na hák</em></div>
  </div>
</section>

<section id="etnika" class="block reveal">
  <h2><span class="h-num">4</span>Etnické pomery</h2>
  <p>Etnické zloženie Slovenska sa v tomto období výrazne menilo.</p>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:arrow]]</div><h3>Pred Turkami</h3><p><strong>Chorváti, Bulhari, Srbi</strong> (roľníci) a <strong>maďarská šľachta</strong> utekali pred Turkami na Slovensko.</p></article>
    <article class="card"><div class="card-ico">[[icon:mountain]]</div><h3>Valašská kolonizácia</h3><p>Pokračovala v hornatých oblastiach – <strong>Rusíni a Valasi-Rumuni</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:book]]</div><h3>Česi</h3><p>Prichádzali na Slovensko po <strong>bielohorskej bitke</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:coins]]</div><h3>Kupci</h3><p>Ako kupci prichádzali <strong>Gréci, Bulhari a najmä Židia</strong> (zo Španielska a z Poľska-Litvy).</p></article>
    <article class="card"><div class="card-ico">[[icon:people]]</div><h3>Mestá</h3><p>Úbytok <strong>Nemcov</strong> a nárast počtu <strong>Slovákov</strong> v mestách.</p></article>
    <article class="card"><div class="card-ico">[[icon:map]]</div><h3>Dolná zem</h3><p>Po vyhnaní Turkov sa Slováci sťahovali na <strong>„Dolnú zem“</strong> (Vojvodina, Banát).</p></article>
  </div>
</section>

<section id="panovnici" class="block reveal">
  <h2><span class="h-num">5</span>Významní panovníci</h2>
  <div class="rulers">
    <div class="ruler"><span>1526 – 1540</span><strong>Ján Zápoľský</strong></div>
    <div class="ruler"><span>1526 – 1564</span><strong>Ferdinand I.</strong></div>
    <div class="ruler"><span>1564 – 1576</span><strong>Maximilián II.</strong></div>
    <div class="ruler"><span>1576 – 1608</span><strong>Rudolf II.</strong></div>
    <div class="ruler"><span>1608 – 1619</span><strong>Matej II.</strong></div>
    <div class="ruler"><span>1619 – 1637</span><strong>Ferdinand II.</strong></div>
    <div class="ruler"><span>1657 – 1705</span><strong>Leopold I.</strong></div>
    <div class="ruler"><span>1711 – 1740</span><strong>Karol VI. (III.)</strong></div>
    <div class="ruler"><span>1740 – 1780</span><strong>Mária Terézia</strong></div>
    <div class="ruler"><span>1780 – 1790</span><strong>Jozef II.</strong></div>
  </div>
  [[fig:zapolya|center narrow]]
</section>
"""),
# ---------------------------------------------------------------- 6
dict(
slug="osvietenstvo", num="06", short="Osvietenstvo",
title="Osvietenstvo",
icon="light", hero="encyclopedie",
lead="Rozum namiesto dogiem, experiment namiesto povier. Myšlienkový prúd 18. storočia, ktorý zmenil vedu, politiku aj panovníkov – a dal Slovensku významné osobnosti.",
desc="Osvietenstvo (Enlightenment), racionalizmus a empirizmus, filozofi, Encyklopédia, osvietenskí absolutistickí panovníci a slovenské vedecké osobnosti 18. storočia.",
toc=[("pojem","Čo je osvietenstvo"),("filozofi","Filozofi a Encyklopédia"),("panovnici","Osvietení panovníci"),("osobnosti","Osobnosti vedy")],
body="""
<section id="pojem" class="block reveal">
  <h2><span class="h-num">1</span>Čo je osvietenstvo (Enlightenment)</h2>
  <p><strong>Kultúrne hnutie a filozofický smer</strong>, ktorý sa snažil nahradiť vtedajšie náboženské a politické predstavy názormi vychádzajúcimi z ľudského rozumu a zo skúsenosti overenej experimentom.</p>
  <div class="cards two">
    <article class="card tone-gold"><div class="card-ico">[[icon:light]]</div><h3>Racionalizmus</h3><p>Z lat. <em>ratio</em> = rozum. Poznanie vychádza z <strong>ľudského rozumu</strong>.</p></article>
    <article class="card tone-ink"><div class="card-ico">[[icon:flask]]</div><h3>Empirizmus</h3><p>Z lat. <em>empiria</em> = skúsenosť. Poznanie vychádza zo <strong>skúsenosti z experimentu</strong>.</p></article>
  </div>
  <ul class="facts">
    <li>Vedecká pravda sa dokazovala <strong>metodickým postupom</strong> – od <strong>hypotézy</strong> cez <strong>experimenty</strong> po <strong>syntézu</strong>.</li>
    <li>„Osvietení“ rozumom a poznaním odhaľovali temnotu stredovekého nepoznania a náboženského zastierania – <strong>osvietenci / ilumináti</strong> (enlightened scholars).</li>
    <li>Osvietenstvo nahradilo vieru v boha <strong>vierou v ľudský rozum, vedu a pokrok</strong>.</li>
  </ul>
</section>

<section id="filozofi" class="block reveal">
  <h2><span class="h-num">2</span>Filozofi a Encyklopédia</h2>
  <div class="split">
    <div>
      <p>Osvietenstvo vychádzalo z diel filozofov:</p>
      <div class="chips">
        <span>Immanuel Kant</span><span>René Descartes</span><span>Denis Diderot</span><span>Jean-Jacques Rousseau</span><span>François-Marie Voltaire</span><span>Charles-Louis de Montesquieu</span>
      </div>
      <div class="callout big"><span class="callout-ico">📖</span><div>Vo <strong>Francúzsku</strong> sa osvietenci združili okolo tvorby <strong>Encyklopédie vied, umení a remesiel (1751)</strong>, ktorá mala zhromaždiť dovtedajšie ľudské poznanie – nazývali sa preto <strong>encyklopedisti</strong>.</div></div>
    </div>
    [[fig:rousseau|portrait]]
  </div>
</section>

<section id="panovnici" class="block reveal">
  <h2><span class="h-num">3</span>Osvietenskí absolutistickí panovníci</h2>
  <p>V niektorých krajinách šírili túto ideológiu aj panovníci – tzv. <strong>osvietenskí absolutisti</strong>:</p>
  <div class="rulers">
    <div class="ruler"><span>Prusko</span><strong>Fridrich II. Veľký</strong></div>
    <div class="ruler"><span>Rusko</span><strong>Katarína Veľká</strong></div>
    <div class="ruler"><span>Rakúsko</span><strong>Mária Terézia</strong></div>
    <div class="ruler"><span>Rakúsko</span><strong>Jozef II.</strong></div>
  </div>
</section>

<section id="osobnosti" class="block reveal">
  <h2><span class="h-num">4</span>Osobnosti vedy na Slovensku</h2>
  <p>Obdobie osvietenstva je bohaté na osobnosti vo vede:</p>
  <div class="people">
    <div class="person"><span class="avatar">MB</span><h3>Matej Bel</h3><p>Polyhistor, dielo <strong>„Notície o novom Uhorsku“</strong>.</p></div>
    <div class="person"><span class="avatar">AFK</span><h3>Adam František Kollár</h3><p>Dvorský radca Márie Terézie.</p></div>
    <div class="person"><span class="avatar">SM</span><h3>Samuel Mikovíni</h3><p>Kartograf.</p></div>
    <div class="person"><span class="avatar">MKH</span><h3>Matej Kornel Hell</h3><p>Banský konštruktér.</p></div>
    <div class="person"><span class="avatar">MH</span><h3>Maximilián Hell</h3><p>Astronóm.</p></div>
  </div>
</section>
"""),
# ---------------------------------------------------------------- 7
dict(
slug="reformy", num="07", short="Reformy Márie Terézie a Jozefa II.",
title="Reformy Márie Terézie a Jozefa II.",
icon="scroll", hero="mt_family",
lead="Pragmatická sankcia, tereziánsky urbár, Ratio educationis, Tolerančný patent – reformy, vďaka ktorým zostala Habsburská monarchia veľmocou až do 20. storočia.",
desc="Pragmatická sankcia Karola VI., reformy Márie Terézie (urbár, Ratio educationis, manufaktúry) a patenty Jozefa II. (Tolerančný patent, zrušenie nevoľníctva).",
toc=[("karol","Karol VI."),("mt","Mária Terézia"),("jozef","Jozef II."),("dosledky","Dôsledky")],
body="""
<section id="karol" class="block reveal">
  <h2><span class="h-num">1</span>Karol VI. a pragmatická sankcia</h2>
  <p>Za <strong>Karola VI.</strong> (1685 – 1740) sa z Habsburskej monarchie stala <strong>veľmoc</strong> – vďaka víťazstvám proti Turkom a v protihabsburských povstaniach. Nemal však mužského dediča, preto vydal zákon, ktorý zaručoval nástupníctvo aj po ženskej línii („po praslici“).</p>
  <div class="highlight-date"><span>1713</span><p><strong>Pragmatická sankcia</strong> – vydaná v roku 1713, schválená v roku <strong>1723</strong>.</p></div>
</section>

<section id="mt" class="block reveal">
  <h2><span class="h-num">2</span>Mária Terézia (1740 – 1780)</h2>
  <div class="split">
    <div>
      <p>Útok Prusov na <strong>Sliezsko</strong> a <strong>7-ročná vojna (1756 – 1763)</strong>: porážka Rakúšanov ukázala, že krajina je taká zaostalá, že nie je schopná zásobovať armádu. Vznikla potreba <strong>rýchlych a veľkých reforiem</strong> – v duchu myšlienok osvietenstva.</p>
      <blockquote class="quote">„Ovcu musíme kŕmiť, ak ju chceme strihať.“</blockquote>
    </div>
    [[fig:mt|portrait]]
  </div>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:factory]]</div><h3>Manufaktúry</h3><p>Zakladanie manufaktúr – <strong>Prešporok, Banská Štiavnica, Šaštín, Holíč</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:book]]</div><h3>Úradný jazyk</h3><p>Úradným jazykom sa stala <strong>nemčina</strong> → germanizácia.</p></article>
    <article class="card"><div class="card-ico">[[icon:wheat]]</div><h3>Nové plodiny</h3><p>Zavádzanie nových plodín a plemien – <strong>zemiaky, kukurica, tabak, ďatelina</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:scale]]</div><h3>Súdnictvo</h3><p>Formálna <strong>rovnosť občanov pred súdom</strong>, <strong>zákaz procesov s čarodejnicami</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:cross]]</div><h3>Jezuiti</h3><p><strong>1773</strong> – zrušila jezuitský rád.</p></article>
    <article class="card"><div class="card-ico">[[icon:scroll]]</div><h3>Tereziánsky urbár</h3><p>Súpis pôdy a povinností poddaných → dávky <strong>neboli znížené</strong>, ale boli <strong>jednotne uzákonené</strong>. Platil až do zrušenia poddanstva v roku <strong>1848</strong>.</p></article>
  </div>
  <div class="feature reveal">
    <div class="feature-badge">Najvýznamnejšia reforma</div>
    <h3>Ratio educationis (1777)</h3>
    <ul class="facts">
      <li>Zavedenie <strong>školskej sústavy</strong>.</li>
      <li><strong>Triviálne školy</strong> – čítanie, písanie, počítanie.</li>
      <li>Na nižších školách <strong>vyučovanie v materinskom jazyku</strong>.</li>
      <li>Zakladanie vyšších škôl; Vyššiu banícku školu (1735) povýšila na univerzitu – <strong>Banská akadémia (1762)</strong>.</li>
    </ul>
  </div>
  [[fig:mt_ride|center narrow]]
</section>

<section id="jozef" class="block reveal">
  <h2><span class="h-num">3</span>Jozef II. (1780 – 1790)</h2>
  <div class="split rev">
    [[fig:joseph|portrait]]
    <div>
      <ul class="facts">
        <li><strong>Najstarší syn Márie Terézie</strong>, od roku <strong>1765 spoluvládca</strong>.</li>
        <li>Vzdelaný, despotický, no <strong>proti šľachte a cirkvi</strong>; odmietal prepych.</li>
        <li>Odmietol korunováciu za uhorského kráľa – preto <strong>„klobúkový kráľ“</strong>.</li>
        <li>Pokračoval v reformách – vydal tzv. <strong>patenty</strong>, až <strong>6 000</strong>.</li>
      </ul>
    </div>
  </div>
  <ol class="timeline">
    <li><span class="t-date">1781</span><div><strong>Tolerančný patent</strong> – vyhlásil náboženskú slobodu, povolil príchod Židom (→ rozmach), zatvoril polovicu kláštorov a zrušil rády, ktoré nepomáhali ľuďom.</div></li>
    <li><span class="t-date">1781</span><div>Zrušil <strong>nevoľníctvo</strong> v rakúskej časti monarchie (Čechy).</div></li>
    <li><span class="t-date">1785</span><div>Po veľkom sedliackom povstaní v Sedmohradsku zrušil nevoľníctvo aj v <strong>Uhorsku</strong>.</div></li>
  </ol>
  <div class="cards three">
    <article class="card"><div class="card-ico">[[icon:book]]</div><h3>Školstvo a štatistika</h3><p>Zaviedol <strong>povinnú školskú dochádzku</strong> a <strong>sčítanie obyvateľstva</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:arrow]]</div><h3>Centralizácia</h3><p>Centralizácia – z <strong>Bratislavy do Viedne</strong>.</p></article>
    <article class="card"><div class="card-ico">[[icon:eye]]</div><h3>Tajná polícia</h3><p>Vybudoval <strong>tajnú políciu</strong> a byrokratický aparát.</p></article>
    <article class="card"><div class="card-ico">[[icon:scale]]</div><h3>Ďalšie reformy</h3><p>Reformy súdnictva, zdravotníctva, rušenie kláštorov.</p></article>
    <article class="card"><div class="card-ico">[[icon:map]]</div><h3>Halič</h3><p>Po <strong>treťom delení Poľska</strong> pripojil Halič (juh Poľska, západ Ukrajiny).</p></article>
    <article class="card"><div class="card-ico">[[icon:scroll]]</div><h3>Odvolanie patentov</h3><p>Na smrteľnej posteli sa dozvedel o revolučných udalostiach vo Francúzsku – odvolal väčšinu patentov okrem <strong>tolerančného</strong>; ostatné šľachta po jeho smrti odmietla.</p></article>
  </div>
</section>

<section id="dosledky" class="block reveal">
  <div class="peace">
    <div class="peace-year">∞</div>
    <div>
      <h2>Ďalekosiahle dôsledky</h2>
      <p>Reformy mali ďalekosiahle dôsledky – Habsburská monarchia bola napriek hospodárskej zaostalosti vo svojej východnej časti <strong>až do 20. storočia jednou z veľmocí</strong>.</p>
    </div>
  </div>
</section>
"""),
]

STUDY = [
 "BARTL, J., KAMENICKÝ, M., VALACHOVIČ, P.: DEJEPIS pre 2. ročník gymnázií. Národné dejiny. SPN : Bratislava, 2000. s. 5 – 68.",
 "BADA, M., BOCKOVÁ, A. et al.: DEJEPIS pre 1. ročník gymnázií a stredných škôl. SPN : Bratislava, 2013. s. 220 – 269.",
 "KRŠÁK, P. et al.: Ottov historický atlas – Slovensko. Ottovo nakladateľstvo : Praha, 2015. s. 176 – 250.",
]
