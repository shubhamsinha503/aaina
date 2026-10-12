/* The catalogue: what is actually for sale, grouped into lines.
 *
 * Written by the studio dashboard (studio.html). Safe to edit by hand too —
 * it is plain data. The gallery list lives separately in works.js.
 *
 *   s  slug (which image)   t  name   p  price in rupees   k  optional set label
 *
 * Prices are the studio's own. Edit freely; the page recomputes every range.
 */
const CATALOG = [
  {
    id: "panels",
    name: "Framed Panels",
    blurb: "The largest work: a single motif worked over a full board, inside a carved and mirrored frame. Weeks, not days.",
    items: [
      { s: "p98", t: "Peacock Triptych · Indigo", p: 25000, k: "Three panels" },
      { s: "p97", t: "Peacock Panel · Cream and Green", p: 23000 },
      { s: "p99", t: "Peacock Panel · Indigo", p: 11000 },
      { s: "p45", t: "Mounted Panel with Torans", p: 3200 },
      { s: "p100", t: "Tulip Border Panel", p: 4000, k: "Single panel" }
    ]
  },
  {
    id: "mandalas",
    name: "Mirror Mandalas",
    blurb: "Unpainted, or nearly so. These are the pieces that live or die on how the mirrors are seated.",
    items: [
      { s: "p44", t: "Mirror Mandala · Full Face", p: 4500 },
      { s: "p38", t: "Mirror Mandala · Navy", p: 4200 },
      { s: "p81", t: "Sunset Mandala", p: 3600 },
      { s: "p26", t: "Krishna Silhouette · Indigo", p: 3200 },
      { s: "p48", t: "Turquoise Ring Mirror", p: 2400 },
      { s: "p49", t: "Silver Lippan Mirror", p: 2400 },
      { s: "p69", t: "White Lippan Mirror", p: 2400 }
    ]
  },
  {
    id: "thalis",
    name: "Wall Thalis",
    blurb: "Painted plates, figurative and otherwise. The everyday heart of the studio and the usual first commission.",
    items: [
      { s: "p47", t: "Ganesh Thali with Matki Set", p: 3800, k: "Thali and three pots" },
      { s: "p91", t: "Lotus Thali · Maroon and Green", p: 2800 },
      { s: "p31", t: "Ganesh Thali · Silver Mirror", p: 2600 },
      { s: "p64", t: "Golden Ganesh Thali", p: 2600 },
      { s: "p50", t: "Swastik Round · Pair", p: 2600, k: "Pair" },
      { s: "p08", t: "Radha Krishna Thali", p: 2400 },
      { s: "p07", t: "Radha Krishna · Marigold Field", p: 2400 },
      { s: "p06", t: "Ganesh Thali · Cobalt", p: 2400 },
      { s: "p88", t: "Ganesh Thali · Indigo and Rose", p: 2400 },
      { s: "p89", t: "Shri Ram Thali", p: 2400 },
      { s: "p67", t: "Ganesh Relief Thali", p: 2400 },
      { s: "p11", t: "Bal Gopal", p: 2200 },
      { s: "p12", t: "Bal Gopal · Blue Border", p: 2200 },
      { s: "p90", t: "Sunflower Thali", p: 2200 },
      { s: "p59", t: "Swastik Thali", p: 1800 },
      { s: "p61", t: "Swastik Thali · Orange Band", p: 1800 }
    ]
  },
  {
    id: "torans",
    name: "Torans & Door Hangings",
    blurb: "Shubh–labh pairs, bead torans and diya drops. These go above a doorway rather than on a wall.",
    items: [
      { s: "p51", t: "Ganesh Toran Set", p: 2400, k: "Set" },
      { s: "p53", t: "Toran Set · Laid Out", p: 2400, k: "Set" },
      { s: "p16", t: "Shubh–Labh Hanging", p: 1900, k: "Pair" },
      { s: "p18", t: "Shubh–Labh · Mounted", p: 1900, k: "Pair" },
      { s: "p52", t: "Diya Drop Hangings", p: 1600 },
      { s: "p17", t: "Bead Toran", p: 1400 }
    ]
  },
  {
    id: "festive",
    name: "Festive & Rangoli Sets",
    blurb: "Diwali work: floor rangoli sets, diya rounds and Lakshmi charan. Made to order from around August.",
    items: [
      { s: "p22", t: "Diya Rangoli · Six Piece", p: 1800, k: "Six pieces" },
      { s: "p24", t: "Rangoli Set · Assorted", p: 1800, k: "Set" },
      { s: "p80", t: "Rangoli Set · Gold", p: 1800, k: "Set" },
      { s: "p21", t: "Diya Rangoli Set", p: 1600, k: "Set" },
      { s: "p23", t: "Rangoli Set · Lit", p: 1600, k: "Set" },
      { s: "p57", t: "Rangoli with Satellites", p: 1600, k: "Set" },
      { s: "p86", t: "Lakshmi Charan · Three Pairs", p: 1400, k: "Three pairs" },
      { s: "p25", t: "Marigold Rangoli Round", p: 900 },
      { s: "p55", t: "Orange Rangoli Round", p: 900 }
    ]
  },
  {
    id: "matkis",
    name: "Matkis & Planters",
    blurb: "Terracotta pots carrying mirror work, sold singly or as a graduated set. They take a plant happily.",
    items: [
      { s: "p79", t: "Matki Set of Four", p: 3200, k: "Set of four" },
      { s: "p78", t: "Matki Trio", p: 2500, k: "Set of three" },
      { s: "p101", t: "Mirror Handi · Yellow", p: 1200 },
      { s: "p96", t: "Mirror Matki · Red and Gold", p: 1100 },
      { s: "p20", t: "Matki as Planter", p: 1100 },
      { s: "p73", t: "Turquoise Matki", p: 950 }
    ]
  },
  {
    id: "coasters",
    name: "Coasters & Tableware",
    blurb: "Four coasters and a painted holder. The easiest thing here to buy several of, and the usual choice for favours.",
    items: [
      { s: "p93", t: "Coaster Sets · Five Colourways", p: 3800, k: "All five sets" },
      { s: "p87", t: "Mirror Coaster Set", p: 850, k: "Set of four" },
      { s: "p94", t: "Coaster Set · Indigo", p: 850, k: "Set of four" }
    ]
  }
];

/* Bulk pricing. Shown as a table and used nowhere else. */
const BULK = [
  {
    "q": "3 – 5 pieces",
    "d": "10% off"
  },
  {
    "q": "6 – 10 pieces",
    "d": "15% off"
  },
  {
    "q": "11 – 24 pieces",
    "d": "20% off"
  },
  {
    "q": "25+ · weddings, corporate gifting",
    "d": "Quoted individually"
  }
];
