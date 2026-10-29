"""Builds docs/*.html for Heli Service AB.

Run:  python3 scripts/build.py docs

All text, services, reviews and contact details live in this file. Services with confirmed=False and the
FAQ answers are suggestions that Heli Service should confirm or edit before launch.
"""
import html
import json
import pathlib
import sys
from urllib.parse import quote_plus

# Elevate Studio's credit under every footer: the mark and the name, the whole of it one link to elevatestudio.nu.
ELEVATE_CREDIT = '''<!-- elevate-credit -->
<style>.elevate-credit{max-width:1240px;margin:24px auto 0;padding:20px 16px 0;border-top:1px solid rgba(128,128,128,.25);display:flex;justify-content:center;box-sizing:border-box}.elevate-credit a{display:inline-flex;align-items:center;gap:8px;padding:8px 0;font:inherit;font-size:13px;line-height:1;color:inherit;opacity:.55;text-decoration:none;transition:opacity .2s}.elevate-credit a:hover,.elevate-credit a:focus-visible{opacity:1}.elevate-credit svg{width:16px;height:16px;flex:none;display:block}@media(min-width:1024px){.elevate-credit a{font-size:14px}}</style>
<div class="elevate-credit"><a href="https://elevatestudio.nu" target="_blank" rel="noopener"><svg viewBox="0 0 1884.3 1353.9" aria-hidden="true"><path d="M0.0 1353.9 L1218.7 0.0 L1218.7 329.1 L479.7 1136.4 L786.7 1132.4 L1215.5 687.4 L1884.3 1349.9 L1590.1 1349.9 L1218.6 994.7 L865.4 1349.9Z" fill="currentColor"/></svg>Byggd av Elevate Studio</a></div>
'''


OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")

# --- Verified company details (Google Maps, hitta.se) ---------------------------------------------------------------
NAME = "Heli Service AB"
SHORT = "Heli Service"
PHONE, TEL = "070-628 51 90", "+46706285190"
STREET, POSTAL, CITY = "Tegneby-Kärra 325", "473 97", "Henån"
AREA = "Orust"
ADDR = f"{STREET}, {POSTAL} {CITY}"
RATING, REVIEW_COUNT = "5,0", 8
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f"{NAME}, {ADDR}")
MAP_EMBED = "https://www.google.com/maps?q=" + quote_plus(ADDR) + "&z=12&hl=sv&output=embed"
# Google Maps only says the business closes at 17. Edit when the real hours are known.
HOURS = "Dagtid, till kl. 17"

EMAIL = "heliservice@telia.com"
ORG_NR = "556846-9596"
SINCE = 2005

# The quote form e-mails through FormSubmit. Elevate Studio receives the requests during the preview; at launch this
# becomes Heli Service's own address. The first request to a new address only sends an activation e-mail.
FORM_EMAIL = "elevate.studio018@gmail.com"

SITE_URL = "https://elevatestudio018.github.io/heliservice/"

# --- Services -------------------------------------------------------------------------------------------------------
# confirmed=True: work Henrik describes on the Google profile ("Elinstallationer till fastigheter som stugor villor och
# industrier båtar maskiner, allt från nybyggnation till renovering, felsökning"). confirmed=False: a suggestion.
SERVICES = [
    dict(
        slug="elinstallation", title="Elinstallation i villor och stugor", confirmed=True,
        photo="villa", pos="50% 40%", alt="Rött trähus med vita fönster",
        short="Ny el, fler uttag, belysning och elcentraler i hus och fritidshus.",
        body=[
            "Vi gör elinstallationer i villor, sommarstugor och fritidshus på Orust med omnejd. Det kan vara ett par nya uttag i köket, ny belysning ute eller en komplett omdragning av elen i en äldre stuga.",
            "Vi går igenom vad som ska göras med dig innan start, och du har en och samma person att prata med hela vägen.",
        ],
        items=["Nya uttag och strömbrytare", "Belysning inne och ute", "Byte av elcentral", "Omdragning av el i äldre hus",
               "El i sommarstuga och fritidshus"],
    ),
    dict(
        slug="nybyggnation", title="El till nybyggnation", confirmed=True,
        photo="nybygge", pos="50% 50%", alt="Regelstomme av trä under uppförande",
        short="Elen i nya hus, tillbyggnader och attefallshus, från planering till färdig anläggning.",
        body=[
            "Ska du bygga nytt, bygga till eller sätta upp ett attefallshus? Vi drar elen från första planeringen till färdig anläggning.",
            "Det är enklast att få med oss tidigt, så att uttag, belysning och centralen hamnar rätt från början.",
        ],
        items=["Planering av el tillsammans med dig", "Inkommande el och elcentral", "Rördragning och kablage i stommen",
               "Uttag, brytare och belysning", "Tillbyggnader och attefallshus"],
    ),
    dict(
        slug="renovering", title="El vid renovering", confirmed=True,
        photo="renovering", pos="50% 50%", alt="Rum under renovering med stegar och verktyg",
        short="Ny el när du renoverar kök, badrum eller hela huset.",
        body=[
            "När väggarna ändå är öppna är det rätt läge att se över elen. Vi drar om, flyttar och kompletterar elen när du renoverar kök, badrum eller hela huset.",
            "Vi samordnar gärna med snickare och VVS, så att elen blir klar i rätt ordning.",
        ],
        items=["El i kök och badrum", "Flytt och komplettering av uttag", "Utbyte av gammal el", "Ny belysning",
               "Samordning med övriga hantverkare"],
    ),
    dict(
        slug="felsokning", title="Felsökning", confirmed=True,
        photo="elcentral", pos="50% 50%", alt="Hand som pekar på säkringar i en elcentral",
        short="Jordfelsbrytaren som löser ut eller lampan som blinkar – vi hittar felet.",
        body=[
            "Löser jordfelsbrytaren ut, går en säkring hela tiden eller fungerar något bara ibland? Vi felsöker det mesta i elväg, i hus, stugor, båtar och maskiner.",
            "Henrik är problemlösare och ger sig inte förrän felet är hittat och åtgärdat.",
        ],
        items=["Jordfelsbrytare som löser ut", "Säkringar som går", "Uttag och belysning som inte fungerar",
               "Fel i båtel och maskiner", "Kontroll av äldre anläggningar"],
    ),
    dict(
        slug="batar", title="El i båtar", confirmed=True,
        photo="batar", pos="50% 50%", alt="Segelbåt på blått vatten sedd ovanifrån",
        short="Landström, batterier, laddning och felsökning ombord.",
        body=[
            "Vi gör elarbeten i båtar – från landström och laddning till batterisystem, belysning och felsökning ombord.",
            "Vi utgår från Orust och tar jobb i hamnar och på varv i närheten.",
        ],
        items=["Landström och laddare", "Batterier och batterisystem", "Belysning och uttag ombord",
               "Felsökning av båtel", "Översyn inför säsongen"],
    ),
    dict(
        slug="industri", title="Industri och maskiner", confirmed=True,
        photo="industri", pos="50% 40%", alt="Montör i skyddsväst vid en stor maskin i en industrihall",
        short="Installation, service och reparation i lokaler, verkstäder och på maskiner.",
        body=[
            "Vi gör elinstallationer och service i industrilokaler, verkstäder och lantbruk, och reparerar el på maskiner.",
            "Berätta vad som behöver göras, så tittar vi på det på plats.",
        ],
        items=["Elinstallation i lokaler och verkstäder", "Kraftuttag och matning till maskiner", "Reparation av el på maskiner",
               "Felsökning och service"],
    ),
    dict(
        slug="fiber", title="Fiberinstallation", confirmed=False,
        photo="fiber", pos="50% 30%", alt="Elektriker i hjälm arbetar vid ett uttag på en vägg",
        short="Indragning och installation av fiber i hus och fritidshus.",
        body=[
            "Vi tar emot förfrågningar om fiberinstallation i villor och fritidshus.",
        ],
        items=["Indragning av fiber i huset", "Placering av mediaomvandlare", "Nätverksuttag i rummen"],
    ),
    dict(
        slug="laddbox", title="Laddbox för elbil", confirmed=False,
        photo="laddbox", pos="50% 50%", alt="Laddkabel ansluten till en elbil",
        short="Installation av laddbox hemma eller vid fritidshuset.",
        body=[
            "Vi tar emot förfrågningar om installation av laddbox för elbil, hemma eller vid fritidshuset.",
        ],
        items=["Installation av laddbox", "Kontroll av elcentral och huvudsäkring", "Ny matning till laddplatsen"],
    ),
]
DONE = [s for s in SERVICES if s["confirmed"]]
ASK = [s for s in SERVICES if not s["confirmed"]]
WORK_TYPES = [s["title"] for s in SERVICES] + ["Annat"]

# --- Reviews (copied exactly from Google; a text that Google cuts off ends there) -----------------------------------
REVIEWS = [
    dict(
        name="Torbjörn Öberg", stars=5,
        text="Henrik är lätt att få tag i och är på riktigt engagerad i sitt jobb. Han har koll på vilka produkter som gäller och gör allt från småjobb till nu senast komplett i …",
        truncated=True,
    ),
    dict(
        name="Anita Anger", stars=5,
        text="Tusen TACK Henrik för el jobbet i vår sommarstuga. Vi är helnöjda. Vi kommer tillbaka det vet du.",
    ),
    dict(
        name="Mikael Andersson", stars=5,
        text="Bra bemötande,snabb service",
    ),
]

FAQ = [
    ("Vilka jobb tar ni?",
     "Elinstallationer i stugor, villor, industrier, båtar och maskiner – allt från nybyggnation och renovering till felsökning. Inget jobb är för litet."),
    ("Kan jag få en offert?",
     f"Ja. Fyll i <a href=\"#offert\">formuläret</a> eller ring Henrik på <a href=\"tel:{TEL}\">{PHONE}</a>. Ofta behöver vi se jobbet innan vi kan ge ett pris som håller."),
    ("Var jobbar ni?",
     "Vi utgår från Henån på Orust. Ligger jobbet utanför ön, säg var, så svarar vi om vi kan ta det."),
    ("Gäller ROT-avdrag?",
     "ROT-avdraget gäller arbetskostnaden för många elarbeten i bostäder och fritidshus. Vi går igenom vad som gäller för ditt jobb i offerten."),
]

STEPS = [
    ("Du ringer eller skriver", "Berätta kort vad som ska göras."),
    ("Vi tittar på jobbet", "Gärna på plats, så att vi ser förutsättningarna."),
    ("Du får en offert", "Med vad som ingår och vad det kostar."),
    ("Vi gör jobbet", "Enligt det vi har kommit överens om."),
]

# --- Markup helpers -------------------------------------------------------------------------------------------------
E = html.escape
PHONE_ICON = ('<svg class="pi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<path d="M21 16.5v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 1.1 3.8 2 2 0 0 1 3.1 1.6h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L7.1 9.5a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'
              '<path d="M15 2.5a6.5 6.5 0 0 1 6.5 6.5M15 6a3 3 0 0 1 3 3"/></svg>')
STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="m10 1.6 2.6 5.4 5.9.8-4.3 4.1 1 5.9L10 15l-5.2 2.8 1-5.9L1.5 7.8l5.9-.8z"/></svg>'


def stars(n=5):
    return f'<span class="stars" role="img" aria-label="{n} av 5 stjärnor">{STAR * n}</span>'


def img(src, alt="", pos="50% 50%", sizes="100vw", lazy=True):
    return (f'<img src="img/{src}.jpg" srcset="img/{src}-s.jpg 800w, img/{src}.jpg 1800w" sizes="{sizes}" '
            f'alt="{E(alt)}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""} decoding="async" style="object-position:{pos}">')


def photo(src, alt, pos="50% 50%", sizes="(min-width: 960px) 50vw, 100vw"):
    """A rounded photo with the note that it is a stock photo, not Heli Service's own."""
    return f'<figure class="ph">{img(src, alt, pos, sizes)}<figcaption>Illustrationsbild</figcaption></figure>'


# Wordmark: red square with a white bolt, white HELI and red SERVICE for the dark header and footer.
# assets-src/heli-service-logo-morkt.svg has dark letters for light backgrounds.
def logo():
    return '<img class="logo-img" src="img/heli-service-logo.svg" alt="Heli Service" width="683" height="104">'


def call_btn(label=None, cls=""):
    return f'<a class="pill pill-red {cls}" href="tel:{TEL}">{PHONE_ICON}<span>{label or "Ring " + PHONE}</span></a>'


NAV = [("tjanster", "Tjänster"), ("referens", "Referens"), ("om-oss", "Om oss"), ("fragor", "Frågor"), ("kontakt", "Kontakt")]


def header(home):
    pre = "" if home else "index.html"
    links = "".join(f'<a href="{pre}#{a}">{t}</a>' for a, t in NAV)
    rows = "".join(f'<li><a href="{pre}#{a}">{t}</a></li>' for a, t in NAV)
    svc = "".join(f'<li><a href="tjanst-{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    return f'''<a class="skip" href="#main">Hoppa till innehållet</a>
<header class="head">
  <div class="wrap bar">
    <a class="logo" href="{'#top' if home else 'index.html'}" aria-label="{NAME}, till startsidan">{logo()}</a>
    <nav class="nav" aria-label="Huvudmeny">{links}</nav>
    <a class="pill pill-red head-call" href="tel:{TEL}">{PHONE_ICON}<span>{PHONE}</span></a>
    <a class="round round-red head-round" href="tel:{TEL}" aria-label="Ring {PHONE}">{PHONE_ICON}</a>
    <button class="burger" id="menuBtn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Meny"><span></span><span></span></button>
  </div>
  <nav class="menu" id="menu" aria-label="Meny" hidden>
    <div class="wrap">
      <ul class="menu-main">{rows}</ul>
      <p class="menu-h">Tjänster</p><ul class="menu-svc">{svc}</ul>
      {call_btn()}
    </div>
  </nav>
</header>'''


def footer(home):
    pre = "" if home else "index.html"
    svc = "".join(f'<li><a href="tjanst-{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    mail = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>' if EMAIL else ""
    org = f"<p>Org.nr {ORG_NR}</p>" if ORG_NR else ""
    return f'''<footer class="foot">
  <div class="wrap">
    <a class="logo" href="{pre or '#top'}" aria-label="{NAME}, till startsidan">{logo()}</a>
    <div class="foot-grid">
      <div>
        <p class="foot-h">{NAME}</p>
        <p><b>{AREA}</b></p>
        <p>{STREET},<br>{POSTAL} {CITY}</p>
        <p><a href="tel:{TEL}">{PHONE}</a></p>{mail}{org}
      </div>
      <div><p class="foot-h">Tjänster</p><ul>{svc}</ul></div>
      <div><p class="foot-h">{SHORT}</p><ul>{"".join(f'<li><a href="{pre}#{a}">{t}</a></li>' for a, t in NAV)}<li><a href="{pre}#offert">Begär offert</a></li></ul></div>
    </div>
    <div class="foot-end">
      <span>© <span data-year>2026</span> {NAME} · Bilderna är stockfoton från Pexels</span>
    </div>
  </div>
{ELEVATE_CREDIT}</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def jsonld():
    data = {
        "@context": "https://schema.org", "@type": "Electrician", "name": NAME, "url": SITE_URL,
        "telephone": TEL, "image": SITE_URL + "img/hero-orust.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "postalCode": POSTAL.replace(" ", ""),
                    "addressLocality": CITY, "addressCountry": "SE"},
        "areaServed": {"@type": "Place", "name": AREA}, "foundingDate": str(SINCE),
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5", "reviewCount": REVIEW_COUNT},
    }
    if EMAIL:
        data["email"] = EMAIL
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def page(name, title, desc, main, home=False, image="hero-orust"):
    url = SITE_URL + ("" if name == "index.html" else name)
    doc = f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="sv_SE">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE_URL}img/{image}.jpg">
<meta name="theme-color" content="#1d1d1d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
{jsonld() if home else ''}
</head>
<body>
{header(home)}
<main id="main">
{main}
</main>
{footer(home)}'''
    (OUT / name).write_text(doc, encoding="utf-8")


def card(s):
    return (f'<li class="card"><a href="tjanst-{s["slug"]}.html">{photo(s["photo"], s["alt"], s["pos"], "(min-width: 960px) 33vw, 100vw")}'
            f'<h3>{s["title"]}</h3><p>{s["short"]}</p><span class="more">Läs mer</span></a></li>')


def ask_pills(skip=None):
    return "".join(f'<a class="pill pill-dark" href="tjanst-{s["slug"]}.html">{s["title"]}</a>' for s in ASK if s["slug"] != skip)


def review_block(center=False):
    out = []
    for r in REVIEWS:
        more = (f' · <a href="{MAPS_LINK}" target="_blank" rel="noopener">Läs hela på Google</a>' if r.get("truncated") else "")
        reply = f'<p class="reply"><b>Svar från {SHORT}:</b> ”{E(r["reply"])}”</p>' if r.get("reply") else ""
        out.append(f'<figure class="review{" center" if center else ""}">{stars(r["stars"])}<blockquote><p>”{E(r["text"])}”</p></blockquote>'
                   f'<figcaption><b>{E(r["name"])}</b>, omdöme på Google{more}</figcaption>{reply}</figure>')
    return "".join(out)


def quote_form():
    opts = "".join(f"<option>{E(t)}</option>" for t in WORK_TYPES)
    req = '<span class="req" aria-hidden="true">*</span>'
    return f'''<form class="form" id="qform" novalidate data-endpoint="https://formsubmit.co/ajax/{FORM_EMAIL}">
  <p class="field"><label for="f-typ">Typ av jobb</label><select id="f-typ" name="Typ av jobb"><option value="">– Välj ett alternativ –</option>{opts}</select></p>
  <p class="field"><label for="f-namn">För- och efternamn{req}</label><input id="f-namn" name="Namn" autocomplete="name" required><span class="err" id="e-namn" hidden>Skriv ditt namn.</span></p>
  <p class="field"><label for="f-tel">Telefonnummer{req}</label><input id="f-tel" name="Telefon" type="tel" autocomplete="tel"><span class="err" id="e-tel" hidden>Skriv telefonnummer eller e-post.</span></p>
  <p class="field"><label for="f-epost">E-post</label><input id="f-epost" name="E-post" type="email" autocomplete="email"><span class="err" id="e-epost" hidden>Kontrollera e-postadressen.</span></p>
  <p class="field"><label for="f-besk">Beskriv jobbet</label><textarea id="f-besk" name="Beskrivning" rows="5" placeholder="Vad ska göras, var och när?"></textarea></p>
  <p class="hp" aria-hidden="true"><label for="f-web">Lämna tomt</label><input id="f-web" name="_honey" tabindex="-1" autocomplete="off"></p>
  <p class="small">{req} Telefonnummer eller e-post räcker. Uppgifterna används bara för att svara dig.</p>
  <p><button class="pill pill-dark" type="submit">Skicka förfrågan</button></p>
  <p class="send-err" id="send-err" role="alert" hidden>Det gick inte att skicka just nu. Försök igen, eller ring <a href="tel:{TEL}">{PHONE}</a>.</p>
</form>
<div class="done" id="qdone" tabindex="-1" hidden>
  <p class="done-h">Tack! Vi har fått din förfrågan.</p>
  <p>Vi hör av oss så snart vi kan. Brådskar det, ring <a href="tel:{TEL}">{PHONE}</a>.</p>
  <p><button class="link" type="button" id="qagain">Skicka en ny förfrågan</button></p>
</div>'''


# --- Start page -----------------------------------------------------------------------------------------------------
def index():
    cards = "".join(card(s) for s in DONE)
    steps = "".join(f"<li><b>{t}</b> {d}</li>" for t, d in STEPS)
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    done_links = " ".join(f'<a class="pill pill-dark" href="tjanst-{s["slug"]}.html">{s["title"]}</a>' for s in DONE)

    main = f'''<section class="hero" id="top" aria-labelledby="hero-h">
  <div class="hero-ph">{img("hero-orust", "Röda bodar vid vattnet", "50% 55%", lazy=False)}</div>
  <div class="wrap hero-in">
    <h1 id="hero-h">Elektriker på Orust sedan {SINCE}</h1>
    <p>{NAME} gör elinstallationer i stugor, villor, industrier, båtar och maskiner – från nybyggnation och renovering till felsökning.</p>
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="#offert">Begär offert</a></div>
  </div>
  <span class="hero-note">Illustrationsbild</span>
</section>

<section class="sec tint" aria-labelledby="intro-h">
  <div class="wrap split">
    {photo("elektriker", "Elektriker i hjälm arbetar i ett elskåp", "50% 35%")}
    <div>
      <h2 id="intro-h">Allt i elväg, stora som små jobb</h2>
      <p class="lead">Ny el i sommarstugan, en laddplats vid villan, landström i båten eller felet som ingen annan hittar. Henrik har gjort elinstallationer på Orust med omnejd sedan {SINCE}.</p>
      <div class="btns">{done_links}</div>
    </div>
  </div>
</section>

<section class="sec" id="tjanster" aria-labelledby="tj-h">
  <div class="wrap">
    <h2 id="tj-h">Våra tjänster</h2>
    <ul class="cards">{cards}</ul>
    <h3 class="also-h">Vi tar också förfrågningar om</h3>
    <div class="btns">{ask_pills()}</div>
  </div>
</section>

<section class="sec tint" id="referens" aria-labelledby="ref-h">
  <div class="wrap narrow center">
    <h2 id="ref-h">Vad kunderna säger</h2>
    <p class="lead">{RATING} av 5 på Google och Infobel ({REVIEW_COUNT} omdömen).</p>
    {review_block(center=True)}
  </div>
</section>

<section class="sec" id="om-oss" aria-labelledby="om-h">
  <div class="wrap split">
    {photo("glodlampa", "Händer som håller en glödlampa", "50% 45%")}
    <div>
      <h2 id="om-h">Henrik – mångsidig och problemlösare</h2>
      <p class="lead">Henrik startade företaget {SINCE} och har sedan dess gjort elinstallationer i fastigheter som stugor, villor och industrier, i båtar och maskiner. ”Jag är mångsidig och problemlösare, tveka inte att kontakta mig.”</p>
      <h3>Så går det till</h3>
      <ol class="steps">{steps}</ol>
      <div class="btns">{call_btn()}</div>
    </div>
  </div>
</section>

<section class="sec tint" id="kontakt" aria-labelledby="kt-h">
  <div class="wrap narrow">
    <h2 id="kt-h">Bli kontaktad av {SHORT}</h2>
    <p class="lead">Fyll i formuläret så hör vi av oss. Vill du hellre ringa går det bra, vi svarar {HOURS[0].lower() + HOURS[1:]}.</p>
    <div class="btns">{call_btn()}</div>
    <div id="offert">{quote_form()}</div>
  </div>
</section>

<section class="sec" id="fragor" aria-labelledby="fq-h">
  <div class="wrap narrow">
    <h2 id="fq-h">Vanliga frågor</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sec tint seo" aria-labelledby="seo-h">
  <div class="wrap narrow">
    <h2 id="seo-h">Elektriker i Henån på Orust</h2>
    <p>{NAME} är en elfirma i Henån på Orust. Vi gör <a href="tjanst-elinstallation.html">elinstallationer i villor och stugor</a>, drar <a href="tjanst-nybyggnation.html">el till nybyggen</a> och ser över elen när du <a href="tjanst-renovering.html">renoverar</a>.</p>
    <p>Strular något hjälper vi till med <a href="tjanst-felsokning.html">felsökning</a>, och vi jobbar även med <a href="tjanst-batar.html">el i båtar</a> och <a href="tjanst-industri.html">industri och maskiner</a>. Ring {PHONE} eller <a href="#offert">begär en offert</a>, så tittar vi på jobbet.</p>
    <h3>Hitta hit</h3>
    <p>{NAME}, {ADDR}.</p>
    <div class="btns"><a class="pill pill-red" href="{MAPS_LINK}" target="_blank" rel="noopener">Öppna i Google Maps</a></div>
  </div>
</section>

<section class="map" aria-label="Karta">
  <iframe src="{MAP_EMBED}" title="Karta: {ADDR}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>'''
    page("index.html", "Elektriker på Orust – elinstallation, felsökning, båtel | Heli Service AB",
         "Heli Service AB i Henån gör elinstallationer i stugor, villor, industrier, båtar och maskiner på Orust. Ring Henrik på 070-628 51 90 eller begär offert.",
         main, home=True)


# --- Service pages --------------------------------------------------------------------------------------------------
def service_page(s):
    items = "".join(f"<li>{i}</li>" for i in s["items"])
    body = "".join(f"<p>{p}</p>" for p in s["body"])
    review = f'<h2>Omdömen</h2>{review_block()}' if s["confirmed"] else ""
    others = "".join(card(o) for o in DONE if o["slug"] != s["slug"])
    main = f'''<section class="hero hero-small" aria-labelledby="ph-h">
  <div class="hero-ph">{img(s["photo"], s["alt"], s["pos"], lazy=False)}</div>
  <div class="wrap hero-in">
    <nav class="crumbs" aria-label="Brödsmulor"><a href="index.html">Start</a> / <a href="index.html#tjanster">Tjänster</a> / <span aria-current="page">{s["title"]}</span></nav>
    <h1 id="ph-h">{s["title"]} på Orust</h1>
    <p>{s["short"]}</p>
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="index.html?typ={quote_plus(s["title"])}#offert">Begär offert</a></div>
  </div>
  <span class="hero-note">Illustrationsbild</span>
</section>
<section class="sec">
  <div class="wrap narrow prose">
    <h2>{s["title"]} med {SHORT}</h2>
    {body}
    <h3>Det kan ingå</h3>
    <ul class="list">{items}</ul>
    {review}
    <div class="btns">{call_btn()}<a class="pill pill-dark" href="index.html?typ={quote_plus(s["title"])}#offert">Begär offert</a></div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <h2>Fler tjänster</h2>
    <ul class="cards">{others}</ul>
    <h3 class="also-h">Vi tar också förfrågningar om</h3>
    <div class="btns">{ask_pills(skip=s["slug"])}</div>
  </div>
</section>'''
    desc = f'{s["title"]} på Orust. {s["short"]} {NAME}, telefon {PHONE}.'
    page(f'tjanst-{s["slug"]}.html', f'{s["title"]} på Orust | {NAME}', desc, main, image=s["photo"])


def not_found():
    main = f'<section class="sec"><div class="wrap narrow"><h1>Sidan finns inte</h1><div class="btns"><a class="pill pill-dark" href="index.html">Till startsidan</a>{call_btn()}</div></div></section>'
    page("404.html", f"Sidan finns inte | {NAME}", "Sidan kunde inte hittas.", main)


def seo_files():
    urls = ["index.html"] + [f'tjanst-{s["slug"]}.html' for s in SERVICES]
    locs = "".join(f"<url><loc>{SITE_URL}{'' if u == 'index.html' else u}</loc></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{locs}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    index()
    for s in SERVICES:
        service_page(s)
    not_found()
    seo_files()
    print("Byggde", len(list(OUT.glob("*.html"))), "sidor i", OUT)
