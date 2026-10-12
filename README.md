# Aaina — Lippan art portfolio

Live at **https://aaina.space**

A static website. No build step, no dependencies, no server.

- **Code:** https://github.com/shubhamsinha503/aaina
- **Hosting:** Vercel (free) — deploys automatically from GitHub
- **DNS:** Hostinger

---

## Updating the live site

Edit a file, then push. Vercel rebuilds and publishes on its own — usually
under a minute. There is no zip to build and nothing to upload.

```
git add -A
git commit -m "what you changed"
git push
```

Watch it deploy at https://vercel.com → the `aaina` project → Deployments.

**If something breaks:** Vercel keeps every past deployment. Open the
Deployments list, find the last good one, and use **Promote to Production**
(or "Instant Rollback"). You cannot permanently break the live site.

**To preview before pushing:** double-click `site/index.html` — it opens in any
browser, offline, exactly as it will look live.

---

## What to edit, for what

The site is two pages. **`index.html`** is the shopfront: hero, the priced
catalogue, bulk discounts, process, about, commission. **`gallery.html`** is
every photograph, filterable, with the lightbox. They share `style.css`.

| You want to change | Edit this |
|---|---|
| **A price** | `site/catalog.js` — one number per item |
| **Bulk discount tiers** | the `BULK` list at the bottom of `site/catalog.js` |
| What is for sale, and in which line | `site/catalog.js` |
| A title, category or caption in the gallery | `site/works.js` |
| Headline, About text, email | `site/index.html` |
| Colours, type, spacing — anything visual | `site/style.css` |
| Gallery order | move lines around in `site/works.js` |
| Remove a piece from the gallery | delete its line from `site/works.js` |

`works.js` and `catalog.js` are deliberately separate lists. The gallery shows
every photograph, including studio shots and second views of one object; the
catalogue shows one entry per sellable thing. Seven of the 59 photographs are
therefore not in the catalogue, on purpose.

Line totals and price ranges on the page are computed from `catalog.js`, so
they cannot drift out of step with the items. Change a price and the range in
that line's header, and the "from ₹…" row in the Commission panel, both follow.

### works.js — one line per piece

```js
{"s":"p08","t":"Radha Krishna Thali","c":"Thali","n":"Layered petal border...","r":0.75}
```

- `s` — which image file (**do not change**)
- `t` — title shown on the card
- `c` — category; this drives the filter buttons
- `n` — caption in the full-size view
- `r` — image shape (**do not change**)

Inventing a new category name on any piece makes a new filter button appear by
itself.

Page text — the studio name, headline, About section, commission list and email
address — is in `site/index.html`. Search for the text and type over it. The
email appears twice: the commission button and the footer.

---

## Adding new photos

1. Put them in `source-photos/`
2. Add a line to `site/works.js` for the new piece. Slugs follow the sorted
   filename order of `source-photos/` (`p01`, `p02`, …), so adding a file can
   shift them — check before assuming. **Name new files so they sort last** and
   nothing shifts: a leading lowercase letter does it, because lowercase sorts
   after both digits and capitals. That is why the newest files are named
   `new-YYYYMMDD-what-it-is.jpg`. `slug_map.json` records which file is which.
3. Run `python tools/build_images.py` — reads the originals (HEIC included) and
   regenerates every size and format the page needs
4. Commit and push

The page uses `<picture>` elements: modern browsers get WebP at the right width
for their screen, older ones fall back to JPEG. Nothing to configure.

Needs: `python -m pip install pillow pillow-heif`

---

## Folder layout

```
site/                   the website — this is what Vercel publishes
  index.html            home + the priced catalogue
  gallery.html          every photograph, filterable, with the lightbox
  style.css             all styling, shared by both pages
  catalog.js            what is for sale: 7 lines, 52 items, prices, bulk tiers
  works.js              the 59 photographs
  img/thumb/            grid images     — WebP 400/800px + a 600px JPEG fallback
  img/full/             lightbox images — WebP 1100/1800px + a 1200px JPEG fallback
  img/about/            the artist portrait in the About section. Hand-made, NOT
                        rebuilt by build_images.py — and not wiped by it either,
                        which is exactly why it lives outside thumb/ and full/
  og-image.jpg          link preview card for WhatsApp/Instagram
  favicon.ico, apple-touch-icon.png
  robots.txt, sitemap.xml
source-photos/          your original HEIC/JPG/MP4 files — NOT in git, see below
tools/                  build_images.py (rebuilds all image sizes),
                        build_works.py, convert.py (legacy)
```

**`source-photos/` is deliberately excluded from git** — 182 MB of HEIC and
video is too much for a repository, and the site only needs the converted
images. **This means GitHub is not backing up your originals.** Keep a copy on
an external drive or cloud storage; those are the only originals of your work.

---

## The setup, for reference

- **Domain**: aaina.space, registered at Hostinger — **renews ₹3,199/year.**
  Set a reminder ~11 months out. Transferring to a cheaper registrar after the
  first 60 days cuts that substantially.
- **DNS**: Hostinger nameservers (`aster` / `helios.dns-parking.com`), with two
  records pointing at Vercel:
  ```
  A      @     76.76.21.21
  CNAME  www   00e85b6bbeb2c3d7.vercel-dns-017.com
  ```
  Vercel would prefer `216.198.79.1` for the A record — swapping it clears the
  "DNS Change Recommended" notice. Both work.
- **Hosting**: Vercel, free tier, nothing to renew
- **Contact**: WhatsApp + phone (+91 89295 60625) and
  shubhamsinha5033@gmail.com

---

## Still placeholder

- **Every title and caption was written by Claude from looking at the photos** —
  sizes, mirror counts and dates included. They read plausibly but they are
  guesses, not records. Same for the About text.

- **Every price in `catalog.js` is an estimate, not a rate you set.** They were
  pitched against what comparable handmade lippan sells for online in India
  (roughly ₹640–1,300 small, ₹1,300–2,250 at 10–12in, ~₹2,550 at 14in, ₹3,000+
  above that) and then spread by how much work each piece looks like. No piece
  has been measured. The page says they are indicative and invites a message
  for an exact quote, but they are the first thing to replace with real numbers.

- The bulk discount tiers (10/15/20%) are likewise conventional, not yours.

- `Aaina` as the studio name is **approved** — confirmed 12 Oct 2026.

- The 10 videos in `source-photos/` are unused.

- **`p86`–`p101` have no original in `source-photos/` yet.** They were cropped
  from phone photos and written straight into `site/img/`. Until the sixteen
  `new-2025…`/`new-2026…` files are dropped into `source-photos/`, running
  `tools/build_images.py` will wipe their images and print `!! no original`.
  The files to add are the *cropped* masters, not the uncropped phone frames —
  that is what keeps the framing.

- `p88`, `p89` and `p90` were photographed through their packaging; the plastic
  shows. Worth reshooting unwrapped.

- `p101` came through at 899px wide, where everything else is 1450px or more.
  It is the softest image on the site — a sharper original would replace it
  cleanly. Its plastic planters crowd the frame too.
