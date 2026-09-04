# Aaina — Lippan art portfolio

Live at **https://aaina.space** (hosted free on Cloudflare Pages).

A static website. No build step, no dependencies, no server.

---

## Updating the live site — the three steps

1. **Edit** whatever you want to change inside the `site` folder (see below)
2. **Double-click `UPDATE SITE.bat`** — rebuilds `aaina-space-upload.zip`
3. **Upload it**: Cloudflare dashboard → your project → *Create deployment* →
   drop the zip in

Live in about a minute.

**If something breaks:** Cloudflare keeps every past deployment. Open the
deployment list, find the last good one, click **Rollback**. You cannot
permanently break the live site by uploading a bad version.

To preview a change before uploading, double-click `site/index.html` — it opens
in any browser, offline.

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
4. Then the three steps at the top

Needs: `python -m pip install pillow pillow-heif`

---

## Folder layout

```
site/                   the website — this is what gets published
  index.html            markup, styling, behaviour, head and social tags
  works.js              the 59 pieces
  img/thumb/            grid images     (~760px)
  img/full/             lightbox images (~1500px)
  og-image.jpg          link preview card for WhatsApp/Instagram
  favicon.ico, apple-touch-icon.png
  robots.txt, sitemap.xml
source-photos/          your original HEIC/JPG/MP4 files, untouched
tools/                  convert.py (photos), make_zip.py (packaging)
UPDATE SITE.bat         double-click to rebuild the upload zip
aaina-space-upload.zip  the file you upload to Cloudflare
```

---

## The setup, for reference

- **Domain**: aaina.space, registered at Hostinger — **renews at ₹3,199/year.**
  Set a reminder ~11 months out. Transferring to a cheaper registrar after the
  first 60 days cuts that substantially.
- **DNS**: Cloudflare — nameservers `dolly.ns.cloudflare.com` and
  `odin.ns.cloudflare.com`
- **Hosting**: Cloudflare Pages — free, nothing to renew
- **Email**: Cloudflare Email Routing, forwarding to Gmail — free

### A future upgrade

Connecting a GitHub repo would make deployment automatic: save a file, push, and
Cloudflare rebuilds itself — no zip, no upload. Worth doing if updates become
frequent.

---

## Still placeholder

- Titles and captions were written from looking at the photos. They read well
  but they are guesses — sizes, dates and names should be checked.
- `Aaina` as the studio name.
- The contact email, until Email Routing is set up.
- The 10 videos in `source-photos/` are unused.
