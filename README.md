# Heli Service AB – webbplats

Webbplats för Heli Service AB (elektriker i Henån på Orust), byggd med exakt samma design och struktur som
S-Bygg-sidan (ElevateStudio018/S-Bygg): mörkt sidhuvud och sidfot, röda ”Ring”-knappar, piller-knappar,
Plus Jakarta Sans, stora foton med rundade hörn och enkla staplade sektioner.

## Logga

Ordmärket är gjort för sidan (Heli Service har ingen logga på nätet): rött kvadratiskt märke med vit blixt,
HELI i vitt och SERVICE i rött.

- `docs/img/heli-service-logo.svg` – för mörk bakgrund (sidhuvud och sidfot)
- `assets-src/heli-service-logo-morkt.svg` – mörk text, för ljus bakgrund
- `docs/img/favicon.svg` – blixtmärket

## Sidor

Allt ligger i [`docs/`](docs/) och kräver inga verktyg – öppna `docs/index.html` i en webbläsare.

- `index.html` – startsidan: hero, intro, tjänster, omdömen, om Henrik med arbetsgång, kontakt med
  offertformulär, vanliga frågor, SEO-text med interna länkar och karta
- åtta tjänstesidor: `tjanst-elinstallation.html`, `tjanst-nybyggnation.html`, `tjanst-renovering.html`,
  `tjanst-felsokning.html`, `tjanst-batar.html`, `tjanst-industri.html`, `tjanst-fiber.html`, `tjanst-laddbox.html`
- `404.html`, `sitemap.xml`, `robots.txt`

## Ändra text

Sidorna genereras av `scripts/build.py`, där all text, alla tjänster, omdömen och kontaktuppgifter finns. Ändra där och kör:

```bash
python3 scripts/build.py docs
```

## Fakta och förslag – gå igenom före lansering

**Verifierat** (Google Maps, hitta.se, Eniro): företagsnamn, telefon 070-628 51 90, Tegneby-Kärra 325, 473 97 Henån,
e-post heliservice@telia.com, org.nr 556846-9596, startat 2005 (Henriks egen text på Google), betyg 5,0
(5 omdömen på Infobel, 3 på Google) och de tre Google-omdömena. Torbjörn Öbergs omdöme slutar där Google klipper det.

**Förslag (genererad text) som Heli Service bör bekräfta eller ändra:**

- Tjänsterna *Fiberinstallation* och *Laddbox för elbil* (`confirmed=False` i `SERVICES`). Fiber finns som kategori
  på Eniro; laddbox är ett förslag. De sex andra tjänsterna bygger på Henriks egen beskrivning på Google.
- Listorna ”Det kan ingå” på tjänstesidorna, arbetsprocessen och svaren i Vanliga frågor.
- Tiderna (`HOURS`): Google Maps säger bara att företaget stänger kl. 17.

## Offertformuläret

Formuläret skickar e-post via [FormSubmit](https://formsubmit.co) (gratis) och visar ett tackmeddelande när det
gått fram. Under förhandsvisningen går förfrågningarna till Elevate Studio; byt `FORM_EMAIL` i `scripts/build.py`
till heliservice@telia.com vid lansering. Första förfrågan till en ny adress skickar bara ett aktiveringsmejl.
En tjänstesidas ”Begär offert” fyller i typen av jobb automatiskt (`index.html?typ=…#offert`).

## Bilder

Alla foton i `docs/img/` är tillfälliga stockbilder från [Pexels](https://www.pexels.com) (fria att använda) och
märks på sidan som illustrationsbilder. De ska bytas mot Heli Services egna bilder (t.ex. från Facebook-sidan) –
ersätt filerna med samma namn (både `namn.jpg`, ca 1800 px, och `namn-s.jpg`, ca 800 px).

| Fil | Används till | Pexels-ID |
| --- | --- | --- |
| `hero-orust.jpg` | startsidans hero | [19073324](https://www.pexels.com/photo/19073324/) |
| `elektriker.jpg` | intro | [8005397](https://www.pexels.com/photo/8005397/) |
| `glodlampa.jpg` | om Henrik | [4792509](https://www.pexels.com/photo/4792509/) |
| `villa.jpg` | elinstallation | [19278570](https://www.pexels.com/photo/19278570/) |
| `nybygge.jpg` | nybyggnation | [8830259](https://www.pexels.com/photo/8830259/) |
| `renovering.jpg` | renovering | [3990359](https://www.pexels.com/photo/3990359/) |
| `elcentral.jpg` | felsökning | [257736](https://www.pexels.com/photo/257736/) |
| `batar.jpg` | båtar | [1295036](https://www.pexels.com/photo/1295036/) |
| `industri.jpg` | industri och maskiner | [2760241](https://www.pexels.com/photo/2760241/) |
| `fiber.jpg` | fiber | [8005368](https://www.pexels.com/photo/8005368/) |
| `laddbox.jpg` | laddbox | [9800009](https://www.pexels.com/photo/9800009/) |

## Publicera

Sidan publiceras automatiskt av `.github/workflows/deploy-pages.yml` vid varje push (GitHub Pages, källa *GitHub Actions*).
Byt `SITE_URL` i `scripts/build.py` om sidan får en egen domän.
