"""Exercise illustrations for Issue 03 (medicine ball), drawn as inline SVG.

Each pose is a set of joint coordinates in a 100-wide frame with the floor at
y=100. A card shows two frames (start -> finish) side by side.
"""

INK = "#1A1A1A"
FAR = "#A3A3A3"
RED = "#C82323"
FLOOR = "#D6D6D6"


def ball(x, y, r=7, fill=RED):
    return (
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
        f'<path d="M{x - r * .92} {y - r * .35}Q{x} {y + r * .35} {x + r * .92} {y - r * .35}" '
        f'fill="none" stroke="#fff" stroke-width="1.3" opacity=".85"/>'
        f'<path d="M{x - r * .35} {y - r * .92}Q{x + r * .3} {y} {x - r * .35} {y + r * .92}" '
        f'fill="none" stroke="#fff" stroke-width="1.3" opacity=".6"/>'
    )


def seg(a, b, color, w):
    return (f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round"/>')


def limb(points, color, w):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return (f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def figure(p, dx=0, ink=INK, far=FAR, ball_fill=RED):
    """Draw one pose. p: dict of joints. Far-side limbs are grey."""
    o = [f'<g transform="translate({dx} 0)">']
    o.append(p.get("props", ""))
    far_ink = ink if p.get("far_ink") == INK else far
    # far limbs
    if "knee_f" in p:
        o.append(limb([p.get("hip_f", p["hip"]), p["knee_f"], p["foot_f"]], far_ink, 7.5))
        if "toe_f" in p:
            o.append(seg(p["foot_f"], p["toe_f"], far_ink, 6))
    if "elbow_f" in p:
        o.append(limb([p.get("sh_f", p["sh"]), p["elbow_f"], p["hand_f"]], far_ink, 6))
    if p.get("ball_behind") and p.get("ball"):
        o.append(ball(*p["ball"], fill=ball_fill))
    # torso + head (optionally curved, to show a rounded back)
    if "spine_ctrl" in p:
        c = p["spine_ctrl"]
        o.append(f'<path d="M{p["hip"][0]} {p["hip"][1]}Q{c[0]} {c[1]} {p["neck"][0]} {p["neck"][1]}" '
                 f'fill="none" stroke="{ink}" stroke-width="11" stroke-linecap="round"/>')
    else:
        o.append(seg(p["neck"], p["hip"], ink, 11))
    o.append(f'<circle cx="{p["head"][0]}" cy="{p["head"][1]}" r="7" fill="{ink}"/>')
    # near limbs
    o.append(limb([p.get("hip_n", p["hip"]), p["knee"], p["foot"]], ink, 8))
    if "toe" in p:
        o.append(seg(p["foot"], p["toe"], ink, 6.5))
    if not p.get("ball_behind") and p.get("ball"):
        o.append(ball(*p["ball"], fill=ball_fill))
    o.append(limb([p.get("sh_n", p["sh"]), p["elbow"], p["hand"]], ink, 6.5))
    o.append(p.get("fx", ""))
    o.append("</g>")
    return "".join(o)


def arrow_between(x=113, y=48):
    return (f'<g stroke="{RED}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x - 9} {y}H{x + 9}"/><path d="M{x + 3} {y - 6}L{x + 9} {y}L{x + 3} {y + 6}"/></g>')


def card_svg(a, b, label_a="Start", label_b="Finish", floor=True):
    floor_svg = (f'<line x1="2" y1="101.5" x2="98" y2="101.5" stroke="{FLOOR}" stroke-width="2.5" stroke-linecap="round"/>'
                 f'<line x1="130" y1="101.5" x2="226" y2="101.5" stroke="{FLOOR}" stroke-width="2.5" stroke-linecap="round"/>'
                 ) if floor else ""
    labels = (f'<g font-family="Archivo, Arial, sans-serif" font-size="8.5" font-weight="700" letter-spacing="1.4" '
              f'text-anchor="middle" fill="#8A8A8A"><text x="50" y="114">{label_a.upper()}</text>'
              f'<text x="178" y="114" fill="{RED}">{label_b.upper()}</text></g>')
    return (f'<svg viewBox="-4 -16 236 134" role="img" aria-hidden="true">{floor_svg}'
            f'{figure(a)}{arrow_between()}{figure(b, 128)}{labels}</svg>')


def motion(d):
    return (f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="1.6" stroke-dasharray="3 3" '
            f'stroke-linecap="round"/>')


# ---------- Poses (side view faces right unless noted) ----------

STAND_CHEST = dict(
    head=(52, 20), neck=(50, 31), sh=(50, 34), hip=(50, 59),
    knee=(52, 80), foot=(51, 99), toe=(58, 100),
    knee_f=(48, 80), foot_f=(47, 99), toe_f=(54, 100),
    elbow=(55, 48), hand=(62, 41), elbow_f=(52, 48), hand_f=(59, 42),
    ball=(66, 40),
)

OVERHEAD = dict(
    head=(48, 20), neck=(50, 31), sh=(50, 34), hip=(50, 59),
    knee=(52, 80), foot=(51, 99), toe=(58, 100),
    knee_f=(48, 80), foot_f=(47, 99), toe_f=(54, 100),
    elbow=(56, 20), hand=(55, 5), elbow_f=(53, 21), hand_f=(52, 6),
    ball=(54, -3),
)

SQUAT_CHEST = dict(
    head=(59, 33), neck=(55, 43), sh=(55, 46), hip=(40, 70),
    knee=(63, 82), foot=(52, 99), toe=(59, 100),
    knee_f=(60, 82), foot_f=(49, 99), toe_f=(56, 100),
    elbow=(61, 59), hand=(68, 49), elbow_f=(58, 59), hand_f=(65, 50),
    ball=(72, 47),
)

SLAM_BOTTOM = dict(
    head=(74, 48), neck=(64, 52), sh=(63, 55), hip=(39, 66),
    knee=(58, 83), foot=(49, 99), toe=(56, 100),
    knee_f=(55, 83), foot_f=(45, 99), toe_f=(52, 100),
    elbow=(67, 69), hand=(71, 83), elbow_f=(64, 70), hand_f=(68, 84),
    ball=(74, 93),
    fx=(f'<g stroke="{RED}" stroke-width="1.8" stroke-linecap="round">'
        '<line x1="84" y1="98" x2="90" y2="95"/><line x1="85" y1="90" x2="92" y2="88"/>'
        '<line x1="64" y1="98" x2="58" y2="96"/></g>'),
)

# Front view: Russian twist, seated
_twist_left = dict(
    head=(38, 55), neck=(43, 65), sh=(37, 68), sh_f=(49, 68), hip=(50, 91),
    hip_n=(46, 91), knee=(36, 75), foot=(28, 98),
    hip_f=(54, 91), knee_f=(64, 75), foot_f=(72, 98), far_ink=INK,
    elbow=(28, 78), hand=(22, 88), elbow_f=(40, 82), hand_f=(26, 90),
    ball=(19, 86),
)


def mirror(p):
    q = {}
    for k, v in p.items():
        if isinstance(v, tuple):
            q[k] = (100 - v[0], v[1])
        else:
            q[k] = v
    return q


TWIST_L = _twist_left
TWIST_R = mirror(_twist_left)

# Front view: woodchop
CHOP_HIGH = dict(
    head=(52, 20), neck=(51, 31), sh=(45, 34), sh_f=(57, 34), hip=(50, 59),
    hip_n=(46, 59), knee=(40, 80), foot=(36, 99),
    hip_f=(54, 59), knee_f=(60, 80), foot_f=(64, 99), far_ink=INK,
    elbow=(62, 22), hand=(73, 10), elbow_f=(66, 26), hand_f=(74, 12),
    ball=(78, 5),
)
CHOP_LOW = dict(
    head=(40, 33), neck=(44, 43), sh=(38, 46), sh_f=(50, 46), hip=(49, 67),
    hip_n=(45, 67), knee=(34, 83), foot=(34, 99),
    hip_f=(53, 67), knee_f=(63, 84), foot_f=(65, 99), far_ink=INK,
    elbow=(32, 60), hand=(28, 76), elbow_f=(40, 64), hand_f=(30, 78),
    ball=(24, 82),
)

LUNGE_TWIST = dict(
    head=(53, 32), neck=(51, 43), sh=(51, 46), hip=(49, 71),
    knee=(71, 79), foot=(69, 99), toe=(76, 100),
    knee_f=(37, 93), foot_f=(24, 99), toe_f=(21, 94),
    elbow=(59, 58), hand=(67, 63), elbow_f=(56, 58), hand_f=(64, 64),
    ball=(72, 62),
)

# Wall chest pass (wall on the right)
_wall = f'<line x1="98" y1="-6" x2="98" y2="101" stroke="{FLOOR}" stroke-width="4" stroke-linecap="round"/>'
PASS_START = dict(
    head=(52, 21), neck=(50, 32), sh=(50, 35), hip=(47, 60),
    knee=(55, 80), foot=(56, 99), toe=(63, 100),
    knee_f=(42, 80), foot_f=(38, 99), toe_f=(45, 100),
    elbow=(52, 49), hand=(60, 42), elbow_f=(49, 49), hand_f=(57, 43),
    ball=(64, 41), props=_wall,
)
PASS_END = dict(
    head=(55, 21), neck=(52, 32), sh=(52, 35), hip=(47, 60),
    knee=(55, 80), foot=(56, 99), toe=(63, 100),
    knee_f=(42, 80), foot_f=(38, 99), toe_f=(45, 100),
    elbow=(65, 36), hand=(78, 36), elbow_f=(62, 37), hand_f=(75, 37),
    ball=(89, 35), props=_wall,
    fx=(f'<g stroke="{RED}" stroke-width="1.6" stroke-linecap="round">'
        '<line x1="79" y1="30" x2="72" y2="30"/><line x1="79" y1="40" x2="72" y2="40"/></g>'),
)

# Dead bug (lying on back, head on the left)
DEADBUG_A = dict(
    head=(15, 91), neck=(24, 93), sh=(26, 93), hip=(54, 94),
    knee=(56, 72), foot=(76, 72), knee_f=(59, 73), foot_f=(79, 73),
    elbow=(28, 79), hand=(30, 66), elbow_f=(31, 80), hand_f=(33, 67),
    ball=(31, 59),
)
DEADBUG_B = dict(
    head=(15, 91), neck=(24, 93), sh=(26, 93), hip=(54, 94),
    knee=(74, 90), foot=(94, 86), knee_f=(59, 73), foot_f=(79, 73),
    elbow=(13, 85), hand=(1, 80), elbow_f=(15, 87), hand_f=(3, 82),
    ball=(-5, 80),
)

# Sit-to-stand with a chair behind
_chair = (f'<g stroke="{FLOOR}" stroke-width="3.5" stroke-linecap="round" fill="none">'
          '<path d="M14 42V78H42"/><path d="M17 78V100"/><path d="M40 78V100"/></g>')
SIT = dict(
    head=(41, 36), neck=(38, 47), sh=(38, 50), hip=(33, 74),
    knee=(55, 75), foot=(57, 99), toe=(64, 100),
    knee_f=(52, 75), foot_f=(54, 99), toe_f=(61, 100),
    elbow=(45, 62), hand=(53, 54), elbow_f=(42, 62), hand_f=(50, 55),
    ball=(57, 53), props=_chair,
)
STAND_CHAIR = dict(
    head=(59, 20), neck=(57, 31), sh=(57, 34), hip=(55, 59),
    knee=(58, 80), foot=(57, 99), toe=(64, 100),
    knee_f=(55, 80), foot_f=(54, 99), toe_f=(61, 100),
    elbow=(62, 48), hand=(69, 41), elbow_f=(59, 48), hand_f=(66, 42),
    ball=(73, 40), props=_chair,
)

# Picking the ball up: wrong (rounded back, straight legs) vs right (squat, flat back)
PICKUP_WRONG = dict(
    head=(80, 80), neck=(73, 72), sh=(72, 74), hip=(46, 58), spine_ctrl=(66, 46),
    knee=(50, 79), foot=(50, 99), toe=(57, 100),
    knee_f=(47, 79), foot_f=(47, 99), toe_f=(54, 100),
    elbow=(74, 85), hand=(75, 93), elbow_f=(71, 86), hand_f=(72, 94),
    ball=(79, 93),
)
PICKUP_RIGHT = dict(
    head=(64, 41), neck=(59, 51), sh=(59, 54), hip=(40, 74),
    knee=(64, 81), foot=(52, 99), toe=(59, 100),
    knee_f=(61, 81), foot_f=(49, 99), toe_f=(56, 100),
    elbow=(64, 68), hand=(69, 85), elbow_f=(61, 69), hand_f=(66, 86),
    ball=(73, 92),
)


def compare_svg(bad, good, label_bad="Rounded back", label_good="Flat back"):
    floor = (f'<line x1="2" y1="101.5" x2="98" y2="101.5" stroke="{FLOOR}" stroke-width="2.5" stroke-linecap="round"/>'
             f'<line x1="130" y1="101.5" x2="226" y2="101.5" stroke="{FLOOR}" stroke-width="2.5" stroke-linecap="round"/>'
             f'<line x1="114" y1="10" x2="114" y2="104" stroke="{FLOOR}" stroke-width="1.5" stroke-dasharray="3 4"/>')
    labels = (f'<g font-family="Archivo, Arial, sans-serif" font-size="8.5" font-weight="800" letter-spacing="1.2" text-anchor="middle">'
              f'<text x="50" y="115" fill="{RED}">✕ {label_bad.upper()}</text>'
              f'<text x="178" y="115" fill="{INK}">✓ {label_good.upper()}</text></g>')
    return (f'<svg viewBox="-4 20 236 100" role="img" aria-hidden="true">{floor}'
            f'{figure(bad)}{figure(good, 128)}{labels}</svg>')


CARDS = {
    "squat_press": (SQUAT_CHEST, OVERHEAD),
    "slam": (OVERHEAD, SLAM_BOTTOM),
    "twist": (TWIST_L, TWIST_R),
    "woodchop": (CHOP_HIGH, CHOP_LOW),
    "lunge": (STAND_CHEST, LUNGE_TWIST),
    "chest_pass": (PASS_START, PASS_END),
    "deadbug": (DEADBUG_A, DEADBUG_B),
    "sit_stand": (SIT, STAND_CHAIR),
}

LABELS = {
    "twist": ("Left", "Right"),
    "chest_pass": ("Load", "Throw"),
}


def card(name):
    a, b = CARDS[name]
    la, lb = LABELS.get(name, ("Start", "Finish"))
    return card_svg(a, b, la, lb)


def hero_figure():
    """White slam figure drawn over the big red ball on the cover."""
    arc = ('<path d="M64 -6 C 92 8, 98 52, 80 92" fill="none" stroke="#fff" stroke-width="1.8" '
           'stroke-dasharray="3.5 3.5" stroke-linecap="round" opacity=".8"/>')
    return (f'<svg viewBox="0 -18 110 124" aria-hidden="true">{arc}'
            f'{figure(OVERHEAD, ink="#fff", far="rgba(255,255,255,.5)", ball_fill="#000")}'
            f'</svg>')


if __name__ == "__main__":
    import sys
    out = ["<html><head><link href='fonts.css' rel='stylesheet'><style>body{background:#F7F7F7;font-family:Archivo}"
           "div{display:inline-block;width:460px;margin:10px;background:#fff;border-radius:12px;padding:10px}"
           "svg{width:100%}</style></head><body>"]
    for k in CARDS:
        out.append(f"<div><b>{k}</b>{card(k)}</div>")
    out.append(f"<div style='width:240px'>{hero_figure()}</div></body></html>")
    open(sys.argv[1], "w").write("".join(out))
