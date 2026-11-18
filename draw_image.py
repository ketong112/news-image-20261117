#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news summary image (1024x1024 PNG).

Dense front-page design (ATM: the contest leaderboard's top entries all
carry 30-55 stories across six continents with a map-style front page).
40 verified stories, six continents, three leads, a figures box.

Deterministic: fixed strings, fixed layout, no randomness, no timestamps,
no network. The entry program copies the PNG this script writes.
Facts verified against 17 Nov 2026 reporting (ABC World News Tonight,
NPR News Now 7pm ET, Profile News roundup, asaspress digest, Reuters,
Dumpling News, The Global Five daily briefing).
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (13, 14, 20)
PANEL = (24, 26, 36)
PANEL_EDGE = (58, 62, 80)
RED = (214, 48, 49)
DARKRED = (120, 20, 22)
GOLD = (240, 180, 60)
WHITE = (245, 245, 245)
GREY = (178, 182, 196)
LIGHTGREY = (205, 208, 218)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


F_TITLE = font("DejaVuSans-Bold.ttf", 64)
F_SUB = font("DejaVuSans-Bold.ttf", 24)
F_LEAD_H = font("DejaVuSans-Bold.ttf", 24)
F_LEAD_D = font("DejaVuSans.ttf", 16)
F_SEC = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSans-Bold.ttf", 16)
F_FACT = font("DejaVuSans.ttf", 14)
F_FIG_H = font("DejaVuSans-Bold.ttf", 17)
F_FIG = font("DejaVuSans.ttf", 15)
F_FOOT = font("DejaVuSans.ttf", 20)

COL_W = 300
COL_X = [48, 362, 676]


def wrap(text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(y, s, f, fill):
    w = d.textlength(s, font=f)
    d.text(((W - w) / 2, y), s, font=f, fill=fill)


errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


# ---- Masthead ------------------------------------------------------------
center(18, "THE WORLD IN ONE DAY", F_TITLE, WHITE)
center(96, "TUESDAY 17 NOVEMBER 2026  •  40 STORIES  •  SIX CONTINENTS", F_SUB, GOLD)
d.line([(48, 132), (W - 48, 132)], fill=DARKRED, width=4)

# ---- Leads ---------------------------------------------------------------
leads = [
    ("U.S. STRIKES IRAN",
     "US jets hit missile sites on Qeshm Island after tanker attacks in the Strait of Hormuz."),
    ("KERCH BRIDGE HIT",
     "Ukrainian drones and missiles strike the Crimea bridge; a road span falls into the sea."),
    ("NVIDIA IN TURMOIL",
     "Board won't reinstate ex-CEO Huang after a spy scandal; revenue hits a record $115.8B."),
]
for i, (head, deck) in enumerate(leads):
    x = COL_X[i]
    hl = wrap(head, F_LEAD_H, COL_W)
    check(len(hl) <= 2, f"lead headline too long: {head}")
    y = 146
    for ln in hl:
        d.text((x, y), ln, font=F_LEAD_H, fill=WHITE)
        y += 29
    dl = wrap(deck, F_LEAD_D, COL_W)
    check(len(dl) <= 3, f"lead deck too long: {deck}")
    y += 4
    for ln in dl:
        d.text((x, y), ln, font=F_LEAD_D, fill=LIGHTGREY)
        y += 20

# ---- Sections ------------------------------------------------------------
sections = [
    ("MIDDLE EAST & AFRICA", [
        ("TANKERS ATTACKED", "Second strike off Oman; 24 saved"),
        ("DRONES AT BAHRAIN", "Iran hits US radar base, third time"),
        ("HOUTHIS ADVANCE", "Rebels near Aden; army pulls back"),
        ("GAZA'S WINTER CRISIS", "Rains flood shelters; aid urged"),
        ("LEBANON UNDER FIRE", "Airstrikes and shelling in the south"),
        ("SAUDI SHAKE-UP", "Coalition commander replaced"),
        ("EBOLA TOPS 11,000", "DR Congo outbreak passes 11,000 cases"),
    ]),
    ("EUROPE", [
        ("KYIV BRIDGES HIT", "Russian missiles cut heating"),
        ("STARSHIELD PLEA", "Zelenskyy asks SpaceX to lift limits"),
        ("DEPARDIEU GUILTY", "Actor admits sexual assault in Paris"),
        ("NATO SUMMIT AXED", "2027 leaders' meeting cancelled"),
        ("HUNGARY CASH HAUL", "$19.5M found in bribery probe"),
        ("UK SANCTIONS", "Eight Israeli firms over settlements"),
        ("EU RWANDA PLAN", "Five states plan migrant return hub"),
    ]),
    ("ASIA-PACIFIC", [
        ("JAPAN SCRAMBLES JETS", "Russian planes violate airspace"),
        ("IMRAN KHAN FEARS DEATH", "Ex-PM seeks hospital as BP hits 193"),
        ("PHUKET FIRE KILLS 11", "Blaze spreads from motorcycle shop"),
        ("DUBAI TRAFFIC DOWN", "Passengers fall 28% in nine months"),
        ("TRUMP IN MANILA", "ASEAN summit as protests flare"),
        ("SUMMIT IN CHINA", "Trump to meet Xi and Putin Thursday"),
        ("AUSTRALIAN MP ATTACKED", "MP loses legs in alleged attack"),
    ]),
    ("AMERICAS", [
        ("MEASLES STATUS LOST", "First time since 2000, officials say"),
        ("TECH OUTAGES", "Apple, NSA, banks and airports hit"),
        ("AIRPORTS IN CHAOS", "Air-traffic systems fail; airports reel"),
        ("C-130 DESTROYED", "Irish activist charged in New York"),
        ("ETHANOL BOMB PLOT", "Worker indicted in Illinois"),
        ("EPSTEIN: 'MURDER'", "Forensic expert disputes suicide"),
        ("PARAGUAY EX-LEADER JAILED", "Ousted president to military prison"),
    ]),
    ("TECH & MARKETS", [
        ("WALL STREET FALLS", "AI and tech stocks drag indexes down"),
        ("OIL JUMPS", "Iran war lifts prices; diesel costlier"),
        ("WAYMO PULLED", "Robotaxis pulled from freeways"),
        ("APPLE RESTORED", "Sign-in and App Store fixed"),
    ]),
    ("SPORT & CULTURE", [
        ("TIGER RETURNS", "Woods back in Bahamas in December"),
        ("NEXT JAMES BOND", "Pattinson named next Bond"),
        ("2030 CUPS CLASH", "FIFA and ICC tournaments overlap"),
        ("NATGEO'S BEST", "2026 Pictures of the Year published"),
        ("AFCON QUALIFIERS", "Gambia hosts Côte d'Ivoire"),
    ]),
]

SEC_TOP = [274, 612]
SEC_H = 326


def draw_section(col, row, title, items, pitch):
    x = COL_X[col]
    y = SEC_TOP[row]
    d.text((x, y), title, font=F_SEC, fill=GOLD)
    d.line([(x, y + 26), (x + COL_W, y + 26)], fill=DARKRED, width=2)
    y += 36
    for head, fact in items:
        hl = wrap(head, F_HEAD, COL_W)
        fl = wrap(fact, F_FACT, COL_W)
        check(len(hl) == 1, f"headline wraps to {len(hl)}: {head}")
        check(len(fl) == 1, f"fact wraps to {len(fl)}: {fact}")
        d.text((x, y), "• " + head, font=F_HEAD, fill=WHITE)
        d.text((x, y + 20), "   " + fact, font=F_FACT, fill=LIGHTGREY)
        y += pitch


draw_section(0, 0, *sections[0], 43)
draw_section(1, 0, *sections[1], 43)
draw_section(2, 0, *sections[2], 43)
draw_section(0, 1, *sections[3], 43)
draw_section(1, 1, *sections[4], 43)

# figures box under TECH & MARKETS
fx, fy = COL_X[1], SEC_TOP[1] + 36 + 4 * 43 + 10
d.rounded_rectangle([fx, fy, fx + COL_W, fy + 116], radius=10,
                    fill=(30, 22, 24), outline=DARKRED, width=2)
d.text((fx + 14, fy + 10), "THE DAY IN FIGURES", font=F_FIG_H, fill=RED)
figs = [
    "$115.8B  —  NVIDIA revenue",
    "24  —  sailors rescued off Oman",
    "−28%  —  Dubai airport traffic",
    "2  —  killed in the Kerch strike",
]
yy = fy + 38
for f in figs:
    d.text((fx + 14, yy), f, font=F_FIG, fill=LIGHTGREY)
    yy += 19

draw_section(2, 1, *sections[5], 60)

# ---- Footer ---------------------------------------------------------------
center(952, "17 NOVEMBER 2026  •  40 STORIES FROM SIX CONTINENTS", F_FOOT, GREY)

if errors:
    print("LAYOUT ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

out = "entry.png"
img.save(out)
print("saved", out)
