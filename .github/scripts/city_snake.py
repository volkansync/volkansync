#!/usr/bin/env python3
"""city-snake — the snake that audits the year.

Builds one self-theming SVG from the real GitHub contribution calendar:
an isometric tower city (one tower per day, height ~ contributions), and a
snake that glides along the front edge; every week-column it reaches sinks
into the ground. At the end of the loop the snake resets and the city
regrows. Pure SMIL, no JS, day/night via prefers-color-scheme.

Usage:
  city_snake.py --json contrib.json --out city-snake.svg      # local
  GITHUB_TOKEN=... city_snake.py --user volkansync --out ...  # CI fetch
"""
import argparse, json, math, os, sys, urllib.request

# ---------------------------------------------------------------- palette --
DAY = dict(ink="#453A3E", sub="#715B60", prim="#6B585C", rose="#D77BA8",
           eye="#F7ECEF", shadow="#D8C2BD",
           levels=["#E7D4D0", "#DFB9CA", "#CF8FB3", "#B25E90"])
NIGHT = dict(ink="#ECDFE2", sub="#AE99A0", prim="#8A6E77", rose="#E5A3C0",
             eye="#262024", shadow="#382E33",
             levels=["#453941", "#63455A", "#8F5378", "#C97BA2"])

def hexlerp(h, target, f):
    a = [int(h[i:i+2], 16) for i in (1, 3, 5)]
    b = [int(target[i:i+2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * f):02X}" for x, y in zip(a, b))

def face_vars(pal):
    """per level: top (lighter), right (base), left (darker)"""
    out = {}
    for i, base in enumerate(pal["levels"]):
        out[f"t{i}"] = hexlerp(base, "#FFFFFF", 0.28)
        out[f"r{i}"] = base
        out[f"l{i}"] = hexlerp(base, "#000000", 0.22)
    return out

# -------------------------------------------------------------- geometry ---
AX, AY = 17.0, 4.0        # week axis step
BX, BY = -10.0, 5.0       # day axis step
UX, UY = 7.6, 3.3         # tower half-size along week axis
VX, VY = -4.6, 2.6        # tower half-size along day axis
OX, OY = 92.0, 52.0
W, H = 1000, 330

def pos(w, d):
    return OX + w * AX + d * BX, OY + w * AY + d * BY

def height(c):
    if c <= 0:
        return 0.0
    return min(6 + 9 * math.sqrt(c), 48)

def level(c):
    return 0 if c < 3 else 1 if c < 6 else 2 if c < 10 else 3

def poly(pts, fill, extra=""):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}"{extra}/>'

def tower(w, d, c):
    x, y = pos(w, d)
    h = height(c)
    lv = level(c)
    g1 = (x + UX + VX, y + UY + VY)
    g2 = (x + UX - VX, y + UY - VY)
    g3 = (x - UX - VX, y - UY - VY)
    g4 = (x - UX + VX, y - UY + VY)
    t1, t2, t3, t4 = ((px, py - h) for px, py in (g1, g2, g3, g4))
    return (poly([t1, t2, t3, t4], f"var(--t{lv})")
            + poly([g1, g2, t2, t1], f"var(--r{lv})")
            + poly([g1, g4, t4, t1], f"var(--l{lv})"))

# ----------------------------------------------------------------- build ---
def build(weeks, total):
    nW = len(weeks)
    EAT0, STEP, TAIL, HOLD = 2.2, 0.55, 1.6, 4.0
    T = EAT0 + nW * STEP + TAIL + HOLD
    css_day = ";".join(f"--{k}:{v}" for k, v in {**face_vars(DAY),
               **{k: v for k, v in DAY.items() if k != "levels"}}.items())
    css_night = ";".join(f"--{k}:{v}" for k, v in {**face_vars(NIGHT),
               **{k: v for k, v in NIGHT.items() if k != "levels"}}.items())
    out = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
           f'role="img" aria-label="A snake audits the contribution city: towers for every day of the '
           f'year sink as it passes, then the city grows back. {total} contributions.">',
           f'<defs><style>:root{{{css_night}}}'
           f'@media (prefers-color-scheme: light){{:root{{{css_day}}}}}'
           f'text{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}</style></defs>']

    # ground shadow ribbon
    gpts = [pos(-1, -0.8), pos(nW, -0.8), pos(nW, 7.0), pos(-1, 7.0)]
    out.append(poly(gpts, "var(--shadow)", ' opacity="0.55"'))

    # week columns, back row (d=6) first for painter order
    for w, week in enumerate(weeks):
        tw = (EAT0 + w * STEP) / T
        sink = min(tw + 0.014, 0.999)
        back = 0.955
        towers = "".join(tower(w, d, c) for d, c in
                         sorted(enumerate(week), key=lambda t: -t[0]) if c > 0)
        if not towers:
            continue
        kt = f"0;{tw:.4f};{sink:.4f};{back:.4f};1"
        out.append(
            f'<g><animateTransform attributeName="transform" type="translate" '
            f'keyTimes="{kt}" values="0 0;0 0;0 30;0 30;0 0" dur="{T:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" keyTimes="{kt}" values="1;1;0;0;1" '
            f'dur="{T:.1f}s" repeatCount="indefinite"/>{towers}</g>')

    # snake: glides along the front edge (d = 7 lane)
    sx0, sy0 = pos(-4, 7.6)
    sx1, sy1 = pos(nW + 2, 7.6)
    t_start = (EAT0 - 4 * STEP)
    t_end = EAT0 + (nW + 2) * STEP
    kt = f"0;{max(t_start,0.01)/T:.4f};{t_end/T:.4f};{(T-HOLD*0.25)/T:.4f};1"
    vals = (f"0 0;0 0;{sx1-sx0:.0f} {sy1-sy0:.0f};"
            f"{sx1-sx0:.0f} {sy1-sy0:.0f};0 0")
    seg = []
    for k in range(7, 0, -1):
        f = 1 - k * 0.055
        cxk, cyk = -k * 9.8, -k * 2.3
        seg.append(
            f'<g transform="translate({cxk},{cyk})">'
            f'<animateTransform attributeName="transform" type="translate" additive="sum" '
            f'values="0 0;0 {-2.4*f:.1f};0 0" dur="1.1s" begin="{-k*0.14:.2f}s" repeatCount="indefinite"/>'
            f'<ellipse cx="0" cy="0" rx="{10.2*f:.1f}" ry="{5.5*f:.1f}" fill="var(--prim)"/></g>')
    head = ('<g><animateTransform attributeName="transform" type="translate" additive="sum" '
            'values="0 0;0 -2.8;0 0" dur="1.1s" repeatCount="indefinite"/>'
            '<ellipse cx="2" cy="-0.5" rx="12" ry="6.6" fill="var(--rose)"/>'
            '<circle cx="6.5" cy="-3.9" r="1.8" fill="var(--eye)"/>'
            '<circle cx="11" cy="-1.9" r="1.8" fill="var(--eye)"/>'
            '<path d="M14.5 0.6 l7 1.8 m-7 -1.8 l5.8 3.9" stroke="var(--rose)" stroke-width="1.1" fill="none" stroke-linecap="round">'
            '<animate attributeName="opacity" values="0;0;1;0;0" keyTimes="0;0.55;0.65;0.8;1" dur="2.3s" repeatCount="indefinite"/></path></g>')
    out.append(
        f'<g transform="translate({sx0:.0f},{sy0:.0f})">'
        f'<animateTransform attributeName="transform" type="translate" additive="sum" '
        f'calcMode="linear" keyTimes="{kt}" values="{vals}" dur="{T:.1f}s" repeatCount="indefinite"/>'
        + "".join(seg) + head + "</g>")

    out.append(f'<text x="{W-24}" y="{H-16}" font-size="12.5" fill="var(--sub)" '
               f'text-anchor="end">{total} contributions · eaten yearly</text>')
    out.append("</svg>")
    return "\n".join(out)

# ------------------------------------------------------------------ main ---
def fetch(user, token):
    q = ('{"query":"query { user(login: \\"%s\\") { contributionsCollection '
         '{ contributionCalendar { totalContributions weeks { contributionDays '
         '{ contributionCount } } } } } }"}' % user)
    req = urllib.request.Request("https://api.github.com/graphql",
                                 data=q.encode(),
                                 headers={"Authorization": f"bearer {token}",
                                          "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--user", default="volkansync")
    ap.add_argument("--out", default="city-snake.svg")
    a = ap.parse_args()
    data = json.load(open(a.json)) if a.json else fetch(a.user, os.environ["GITHUB_TOKEN"])
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [[d["contributionCount"] for d in w["contributionDays"]]
             for w in cal["weeks"]]
    svg = build(weeks, cal["totalContributions"])
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    open(a.out, "w").write(svg)
    print(f"{a.out}: {len(svg)//1024}KB, {len(weeks)} weeks", file=sys.stderr)
