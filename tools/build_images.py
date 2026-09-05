"""Regenerate the site's images from the originals in source-photos/.

Produces WebP at several widths plus a JPEG fallback, so the page can serve a
small file to phones and a sharp one to desktops. Run from the project root:

    python tools/build_images.py
"""
import json, os, sys
from PIL import Image, ImageOps
import pillow_heif

pillow_heif.register_heif_opener()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source-photos")
OUT = os.path.join(ROOT, "site", "img")

# grid images (cards) and lightbox images, by width
GRID = [400, 800]
FULL = [1100, 1800]
JPEG_GRID, JPEG_FULL = 600, 1200      # fallbacks for anything without WebP
Q_WEBP, Q_JPEG = 80, 84

def variants(im, widths, folder, slug, jpeg_width):
    made = []
    for w in widths:
        if w > im.width:                      # never upscale
            w = im.width
        v = im.copy()
        v.thumbnail((w, w * 10), Image.LANCZOS)
        p = f"{OUT}/{folder}/{slug}-{w}.webp"
        v.save(p, "WEBP", quality=Q_WEBP, method=5)
        made.append(p)
    j = im.copy()
    j.thumbnail((jpeg_width, jpeg_width * 10), Image.LANCZOS)
    p = f"{OUT}/{folder}/{slug}.jpg"
    j.save(p, "JPEG", quality=Q_JPEG, optimize=True, progressive=True)
    made.append(p)
    return made

def main():
    works = json.loads(open(f"{ROOT}/site/works.js", encoding="utf-8").read()
                       .replace("const WORKS=", "").rstrip().rstrip(";"))
    files = sorted(f for f in os.listdir(SRC)
                   if f.lower().endswith((".heic", ".jpg", ".jpeg", ".png")))
    slug_map = {"p%02d" % (i + 1): f for i, f in enumerate(files)}

    for d in ("thumb", "full"):
        os.makedirs(f"{OUT}/{d}", exist_ok=True)
        for f in os.listdir(f"{OUT}/{d}"):
            os.remove(f"{OUT}/{d}/{f}")

    total = 0
    for w in works:
        slug = w["s"]
        original = slug_map.get(slug)
        if not original:
            print(f"  !! no original for {slug}", file=sys.stderr)
            continue
        im = ImageOps.exif_transpose(Image.open(f"{SRC}/{original}")).convert("RGB")
        variants(im, GRID, "thumb", slug, JPEG_GRID)
        variants(im, FULL, "full", slug, JPEG_FULL)
        total += 1

    size = sum(os.path.getsize(os.path.join(r, f))
               for r, _, fs in os.walk(OUT) for f in fs)
    print(f"{total} pieces rebuilt")
    print(f"widths: grid {GRID} + {JPEG_GRID}px jpeg, lightbox {FULL} + {JPEG_FULL}px jpeg")
    print(f"total image weight: {size/1e6:.1f} MB")

if __name__ == "__main__":
    main()
