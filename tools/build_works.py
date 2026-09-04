import json

meta = {m["slug"]: m for m in json.load(open("manifest.json"))}

# slug: (title, category, caption)
C = [
    ("p08", "Radha Krishna Thali", "Thali", "Layered petal border in indigo, ochre and turquoise, with the couple hand-painted at the centre."),
    ("p02", "Ganesh in Progress", "Studio", "The outer ring going on last — the centre figure is always painted before the mirrors are seated."),
    ("p06", "Ganesh Thali · Cobalt", "Thali", "Eleven concentric bands, each a different motif, closing on a scalloped cobalt edge."),
    ("p07", "Radha Krishna · Marigold Field", "Thali", "Yellow ground chosen so the mirrors read warm rather than silver."),
    ("p09", "Small Ganesh Round", "Thali", "A twelve-inch piece — the same grammar as the large thalis, compressed."),
    ("p11", "Bal Gopal", "Thali", "Krishna as a child, on a yellow field ringed with white lippan dots."),
    ("p12", "Bal Gopal · Blue Border", "Thali", "Deep blue outer band with fine white relief, photographed in the afternoon."),
    ("p31", "Ganesh Thali · Silver Mirror", "Thali", "Densely mirrored — this one throws light across a whole wall."),
    ("p47", "Ganesh Thali with Matki Set", "Thali", "Sold as a set: one thali and three mirror-worked pots."),

    ("p15", "Krishna Silhouette", "Mirror Work", "A flute-playing silhouette on turquoise, ringed by four bands of mirror and white relief."),
    ("p26", "Krishna Silhouette · Indigo", "Mirror Work", "The same subject worked cool — navy, white, and nothing else."),
    ("p38", "Mirror Mandala · Navy", "Mirror Work", "Central mirror left bare so the piece reflects whatever room it hangs in."),
    ("p39", "Mirror Mandala · Wide Band", "Mirror Work", "Chalk-white relief on navy, six rings deep."),
    ("p41", "Mirror Mandala · Garden Light", "Mirror Work", "Photographed outdoors to show how the surface changes with the sun."),
    ("p43", "Mirror Mandala · Detail", "Mirror Work", "Every dot raised by hand. No stencil, no cast."),
    ("p44", "Mirror Mandala · Full Face", "Mirror Work", "The largest of the navy series."),
    ("p48", "Turquoise Ring Mirror", "Mirror Work", "Navy outer, turquoise inner, silver centre."),
    ("p49", "Silver Lippan Mirror", "Mirror Work", "Unpainted white relief on a mirrored ground — the most traditional palette here."),
    ("p69", "White Lippan Mirror", "Mirror Work", "All-white relief, all-silver mirror. Lit only by the room."),
    ("p71", "White Lippan Mirror · Fine Border", "Mirror Work", "Two hundred and forty individual raised dots on the outer ring alone."),
    ("p72", "Bronze Ring Mirror", "Mirror Work", "A warmer variant, finished in bronze rather than silver."),
    ("p81", "Sunset Mandala", "Mirror Work", "Red through orange to yellow, ring by ring, with a mirror centre."),

    ("p59", "Swastik Thali", "Festive", "Made for a doorway at Diwali — vermilion swastik on chalk white, orange border."),
    ("p61", "Swastik Thali · Orange Band", "Festive", "The border carries lotus motifs in raised white."),
    ("p62", "Swastik Thali · Close", "Festive", "Mirror chips run the full circumference."),
    ("p64", "Golden Ganesh Thali", "Festive", "Ganesh raised in gold relief rather than painted — the relief itself does the drawing."),
    ("p65", "Golden Ganesh · Wide", "Festive", "Same piece, showing the orange-and-mirror outer band."),
    ("p67", "Ganesh Relief Thali", "Festive", "Olive and gold, raised high enough to cast its own shadow."),
    ("p50", "Swastik Round · Pair", "Festive", "Two small rounds, orange and red, for either side of a door."),
    ("p16", "Shubh–Labh Hanging", "Hangings", "Pom-poms, beads and a raised lotus at the foot of each string."),
    ("p18", "Shubh–Labh · Mounted", "Hangings", "Hung as they are meant to be — one either side of the entrance."),
    ("p19", "Shubh–Labh · Red", "Hangings", "The red-and-white version, with brass lotus drops."),
    ("p17", "Bead Toran", "Hangings", "A long bead-and-pom toran for a doorframe."),
    ("p51", "Ganesh Toran Set", "Hangings", "Yellow rounds with red tassels, sold as a five-piece set."),
    ("p52", "Diya Drop Hangings", "Hangings", "Square tops, swastik rounds, and a working clay diya at the bottom of each."),
    ("p53", "Toran Set · Laid Out", "Hangings", "The full set before it goes up."),
    ("p45", "Mounted Panel with Torans", "Hangings", "A framed panel flanked by two bead strings, installed."),

    ("p21", "Diya Rangoli Set", "Festive", "Five rounds in red, pink and blue, each holding a tea light."),
    ("p22", "Diya Rangoli · Six Piece", "Festive", "Pom-pom edges, mirror centres."),
    ("p23", "Rangoli Set · Lit", "Festive", "Photographed lit, which is the only way to judge the mirror placement."),
    ("p24", "Rangoli Set · Assorted", "Festive", "Mixed palette — the blue and white piece is the odd one out on purpose."),
    ("p25", "Marigold Rangoli Round", "Festive", "Red velvet ground, yellow pom border, five mirror flowers."),
    ("p55", "Orange Rangoli Round", "Festive", "Concentric orange, red and gold with a diya seat at the centre."),
    ("p57", "Rangoli with Satellites", "Festive", "One large round, four small ones — they can be spread as wide as the floor allows."),
    ("p80", "Rangoli Set · Gold", "Festive", "Gold-rimmed satellites around a red and orange centre."),
    ("p13", "Pink Rangoli Round", "Festive", "An early piece, pink on pink."),

    ("p73", "Turquoise Matki", "Matki", "Terracotta pot in turquoise, mirror chips, jute-wrapped rim."),
    ("p74", "Turquoise Matki · Detail", "Matki", "Three mirror bands with painted petals between."),
    ("p75", "Turquoise Matki · Standing", "Matki", "Roughly fourteen inches tall."),
    ("p77", "Matki Trio", "Matki", "White ground with red, black and silver chips."),
    ("p78", "Matki Trio · Front", "Matki", "Each pot has a jute collar and a different chip pattern."),
    ("p79", "Matki Set of Four", "Matki", "Sold together as a floor grouping."),
    ("p20", "Matki as Planter", "Matki", "Working piece — mirror-worked pot, living plant."),

    ("p01", "At the Table", "Studio", "Where most of it happens: a folding table, a plate, and hours."),
    ("p14", "Base Coat", "Studio", "The flat ground going on before any relief."),
    ("p35", "Marking Out", "Studio", "White relief laid down around a bare mirror, ring by ring."),
    ("p36", "Board and Mirror", "Studio", "The starting point of every mirror piece."),
    ("p28", "Packed for Diwali", "Studio", "A season's worth of orders, wrapped and sorted."),
    ("p37", "Holding the Work", "Studio", "For scale — this one is close to twenty inches across."),
]

works = []
for slug, title, cat, cap in C:
    m = meta[slug]
    works.append({"s": slug, "t": title, "c": cat, "n": cap, "r": m["ratio"]})

with open("site/works.js", "w", encoding="utf-8") as f:
    f.write("const WORKS=" + json.dumps(works, ensure_ascii=False, indent=0) + ";\n")
print(len(works), "works")
print(sorted({w["c"] for w in works}))
