"""Rebuild the upload zip from the site folder.
Run this after editing anything in site/, then upload the zip to Cloudflare."""
import os, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
ZIP = os.path.join(ROOT, "aaina-space-upload.zip")

if os.path.exists(ZIP):
    os.remove(ZIP)

count = 0
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for folder, _, files in os.walk(SITE):
        for f in files:
            full = os.path.join(folder, f)
            z.write(full, os.path.relpath(full, SITE))  # site/ contents land at zip root
            count += 1

print(f"\n  Rebuilt: {os.path.basename(ZIP)}")
print(f"  {count} files, {os.path.getsize(ZIP)/1048576:.1f} MB")
print(f"  Location: {ZIP}\n")
print("  Next: Cloudflare > your project > Create deployment > upload this zip.\n")
