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

| You want to change | Edit this |
|---|---|
| A title, category or caption | `site/works.js` |
| Headline, About text, prices, email | `site/index.html` |
| Gallery order | move lines around in `site/works.js` |
| Remove a piece | delete its line from `site/works.js` |

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
2. Run `python tools/convert.py` — handles HEIC, writes both image sizes
3. Add a line to `site/works.js` for each new piece, using the slug the
   converter assigned
4. Commit and push

Needs: `python -m pip install pillow pillow-heif`

---

## Folder layout

```
site/                   the website — this is what Vercel publishes
  index.html            markup, styling, behaviour, head and social tags
  works.js              the 59 pieces
  img/thumb/            grid images     (~760px)
  img/full/             lightbox images (~1500px)
  og-image.jpg          link preview card for WhatsApp/Instagram
  favicon.ico, apple-touch-icon.png
  robots.txt, sitemap.xml
source-photos/          your original HEIC/JPG/MP4 files — NOT in git, see below
tools/                  convert.py (photos), make_zip.py (legacy packaging)
```

**`source-photos/` is deliberately excluded from git** — 182 MB of HEIC and
video is too much for a repository, and the site only needs the converted
images. **This means GitHub is not backing up your originals.** Keep a copy on
an external drive or cloud storage; those are the only originals of your work.

`UPDATE SITE.bat` and `tools/make_zip.py` are leftovers from the old
upload-a-zip workflow. Harmless, and no longer needed.

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
- **Email**: not set up. The site's contact buttons still point at a
  placeholder address.

---

## Still placeholder

- **Every title and caption was written by Claude from looking at the photos** —
  sizes, mirror counts and dates included. They read plausibly but they are
  guesses, not records. Same for the About text.
- **`Aaina`** as the studio name.
- **`hello@example.com`** in the commission button and footer — this address
  does not exist, so enquiries sent to it go nowhere. Replace it with a real
  address (Gmail works; Zoho Mail has a free tier for a custom domain).
- The 10 videos in `source-photos/` are unused.
