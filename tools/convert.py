import os, json, glob
from PIL import Image, ImageOps
import pillow_heif
pillow_heif.register_heif_opener()

SRC="source-photos"; FULL="site/img/full"; THUMB="site/img/thumb"
os.makedirs(FULL,exist_ok=True); os.makedirs(THUMB,exist_ok=True)
files=sorted([f for f in os.listdir(SRC) if f.lower().endswith(('.heic','.jpg','.jpeg','.png'))])
meta=[]
for i,f in enumerate(files):
    try:
        im=Image.open(os.path.join(SRC,f))
        im=ImageOps.exif_transpose(im).convert("RGB")
    except Exception as e:
        print("SKIP",f,e); continue
    slug="p%02d"%(i+1)
    a=im.copy(); a.thumbnail((1500,1500), Image.LANCZOS)
    a.save(f"{FULL}/{slug}.jpg","JPEG",quality=82,optimize=True,progressive=True)
    b=im.copy(); b.thumbnail((760,760), Image.LANCZOS)
    b.save(f"{THUMB}/{slug}.jpg","JPEG",quality=78,optimize=True,progressive=True)
    meta.append({"slug":slug,"src":f,"w":im.width,"h":im.height,"ratio":round(im.width/im.height,3)})
json.dump(meta,open("manifest.json","w"),indent=1)
print("converted",len(meta))
