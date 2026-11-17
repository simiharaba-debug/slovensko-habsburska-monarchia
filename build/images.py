# Fotografie z Wikimedia Commons – overené cez Commons API (autor, licencia).
from urllib.parse import quote

IMAGES = {
    "presburg": ("Presburg - Peeters Jacob - 1686.jpg", "Jacob Peeters", "Public domain",
                 "Prešporok (Bratislava) na rytine z roku 1686"),
    "merian": ("Bratislava (Posonium) by Matthaus Merian 1638.jpg", "Matthäus Merian", "Public domain",
               "Prešporok (Posonium) na rytine M. Meriana, 1638"),
    "devsirme": ("Janissary Recruitment in the Balkans-Suleymanname.jpg", "Ali Amir Beg", "Public domain",
                 "Odvod kresťanských chlapcov do janičiarskeho vojska, osmanská miniatúra (Süleymanname, 1558)"),
    "janissary": ("Melchior Lorck - A Janissary (Yeniceri).jpg", "Melchior Lorck", "Public domain",
                  "Janičiar na rytine Melchiora Lorcka (1570 – 1583)"),
    "mohacs": ("Battle of Mohacs 1526.png", "Bertalan Székely", "Public domain",
               "Bitka pri Moháči, obraz Bertalana Székelyho"),
    "suleiman": ("1526-Sultan Suleiman during the Battle of Mohacs-Suleymanname.jpg", "Matrakçı Nasuh", "Public domain",
                 "Sultán Sulejman počas bitky pri Moháči, osmanská miniatúra"),
    "vienna1529": ("Siegeofvienna1529.jpg", "Bartel Beham", "Public domain",
                   "Prvé obliehanie Viedne (1529), dobová rytina"),
    "zapolya": ("Szapolyai János fametszet.jpg", "Erhard Schön", "Public domain",
                "Ján Zápoľský na dobovom drevoreze"),
    "neuhausel": ("Neuhäusel1680.jpg", "Pogány Péter", "Public domain",
                  "Plán pevnosti Nové Zámky (okolo roku 1680)"),
    "nz1663": ("Ersekujvar ostroma (1663).JPG", "neznámy autor", "Public domain",
               "Obliehanie Nových Zámkov, dobové zobrazenie (17. storočie)"),
    "nz1685": ("NZ1685.jpg", "neznámy autor", "Public domain",
               "Obliehanie Nových Zámkov v roku 1685"),
    "vienna1683": ("Anonym Entsatz Wien 1683.jpg", "anonymný dobový maliar", "Public domain",
                   "Oslobodenie Viedne 12. septembra 1683 (Heeresgeschichtliches Museum, Viedeň)"),
    "sobieski": ("Juliusz Kossak Sobieski pod Wiedniem.jpeg", "Juliusz Kossak", "Public domain",
                 "Ján III. Sobieski pri Viedni, obraz Juliusza Kossaka"),
    "eugen": ("Prinz-Eugen-von-Savoyen1.jpg", "Jacob van Schuppen", "Public domain",
              "Eugen Savojský, portrét od Jacoba van Schuppena"),
    "rakoczi": ("Mányoki, Ádam - Portrait of Prince Ferenc Rákóczi II - Google Art Project.jpg", "Ádám Mányoki", "Public domain",
                "František II. Rákoci, portrét od Ádáma Mányokiho"),
    "kezmarok": ("Wooden church Kežmarok 9473.JPG", "Karl Gruber", "CC BY-SA 4.0",
                 "Drevený artikulárny kostol v Kežmarku"),
    "kezmarok2": ("Kežmarok Articular church 2015 1.jpg", "Karelj", "CC BY-SA 3.0",
                  "Artikulárny kostol v Kežmarku"),
    "trnava": ("Slovakia - Trnava - Univerzitny kostol - Katedrala Sv. Jana Krstitela RB05.jpg", "Radovan Bahna", "CC BY-SA 4.0",
               "Univerzitný kostol sv. Jána Krstiteľa v Trnave"),
    "haban": ("Jug, Slovakia, Haban, 1697, faience - Museum of Anthropology, University of British Columbia - DSC08920.jpg", "Daderot", "Public domain",
              "Habánsky džbán z roku 1697 (fajansa)"),
    "stiavnica": ("Old town - Banská Štiavnica - Slovakia - panoramio.jpg", "Marek Hrycak", "CC BY-SA 3.0",
                  "Historické centrum Banskej Štiavnice"),
    "mt_family": ("Maria Theresia im Kreise ihrer Familie.jpg", "Martin van Meytens", "Public domain",
                  "Mária Terézia s rodinou, obraz Martina van Meytensa (1754)"),
    "mt": ("Martin van Meytens - Portrait of Maria Theresa of Austria - 2003-17 - Princeton University Art Museum.jpg", "Martin van Meytens", "Public domain",
           "Mária Terézia, portrét od Martina van Meytensa"),
    "mt_ride": ("C. Hirsch d.J. - Der Krönungsritt Maria Theresias in Pressburg 1747.jpg", "C. Hirsch ml.", "Public domain",
                "Korunovačná jazda Márie Terézie v Prešporku"),
    "joseph": ("Joseph Hickel - Portrait Kaiser Joseph II.png", "Joseph Hickel", "Public domain",
               "Jozef II., portrét od Josepha Hickela"),
    "encyclopedie": ("Encyclopedie de D'Alembert et Diderot - Premiere Page - ENC 1-NA5.jpg", "prispievatelia Encyklopédie", "Public domain",
                     "Titulná strana Encyklopédie (1751)"),
    "rousseau": ("Jean-Jacques Rousseau (painted portrait).jpg", "Maurice Quentin de La Tour", "Public domain",
                 "Jean-Jacques Rousseau, portrét od M. Q. de La Toura"),
    "damel": ("Battle of Vienna 1683.PNG", "Jan Damel", "Public domain",
              "Bitka pri Viedni 1683, obraz Jana Damela"),
}

def url(key, width=1280):
    f = IMAGES[key][0].replace(" ", "_")
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(f)}?width={width}"

def page(key):
    f = IMAGES[key][0].replace(" ", "_")
    return f"https://commons.wikimedia.org/wiki/File:{quote(f)}"
