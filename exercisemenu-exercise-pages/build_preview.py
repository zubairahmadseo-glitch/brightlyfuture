"""Build a single-file HTML preview of one exercise page with the new plugin sections.

Usage: python3 build_preview.py <exercise.md> <main.gif> <out.html> [alt-name=alt.gif ...]
"""
import base64
import html
import json
import re
import sys

md_path, gif_path, out_path = sys.argv[1:4]
alt_gifs = dict(a.split("=", 1) for a in sys.argv[4:])
t = open(md_path, encoding="utf-8").read()
E = html.escape
SITE = "https://exercisemenu.com"


def section(name):
    m = re.search(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=^## |^---\s*$|\Z)", t, re.S | re.M)
    return m.group(1).strip() if m else ""


def md_table(block):
    out = []
    for r in block.splitlines():
        if not r.startswith("|"):
            continue
        cells = [c.strip() for c in r.strip("|").split("|")]
        if not set("".join(cells)) <= set("-: "):
            out.append(cells)
    return out


def b64(path):
    return "data:image/gif;base64," + base64.b64encode(open(path, "rb").read()).decode()


name = re.search(r"^# (.+)", t, re.M).group(1).strip()
basics = dict((r[0], r[1]) for r in md_table(section("Exercise Basics"))[1:])
seo = section("SEO & Meta")
meta_title = re.search(r"Meta Title \(≤60\):\*\*\s*\n(.+)", seo).group(1).strip()
meta_desc = re.search(r"Meta Description \(≤160\):\*\*\s*\n(.+)", seo).group(1).strip()
alt_text = re.search(r"GIF Alt Text:\*\*\s*(.+)", t).group(1).strip()
qa = section("Quick Answer (AEO)")
mw = section("Muscles Worked").split("**Secondary Muscles")
code = lambda s: re.search(r"```\n(.*?)```", s, re.S).group(1).strip().splitlines()
primary, secondary = code(mw[0]), code(mw[1])
steps = md_table(section("How-To Steps"))[1:]
sets = md_table(section("Sets & Reps Table"))
mistakes = re.findall(r"^\d+\. \*\*(.+?):\*\* (.+)$", section("Common Mistakes"), re.M)
tips = re.findall(r"^\d+\. \*\*(.+?):\*\* (.+)$", section("Tips"), re.M)
mods = md_table(section("Modifications (Easier/Harder)"))[1:]
faqs = re.findall(r"\*\*Q: (.+?)\*\*\s*\n\s*A: (.+)", section("FAQs"))
cites = re.findall(r"\*\*Citation[^*]*\*\*\s*(.+)", t)

# Sources: numbered list; cite markers replace the inline study mention.
sources = []
for c in cites:
    url = re.search(r"https?://\S+", c).group(0)
    sources.append((c.replace(url, "").replace("*", "").strip(), url))


def cite_marks(text):
    if sources and ("Plotkin" in text or "study" in text.lower()):
        return E(text) + ' <sup class="cite"><a href="#sources">[1]</a></sup>'
    return E(text)


def split_muscle(line):
    n, _, d = line.partition(" — ")
    return n, d


# ---------------------------------------------------------------- page data that the new plugin fields would hold
tags = [s.strip() for s in basics["Tags"].split(",")]
related = [
    ("How Many Reps and Sets for Muscle Growth", "/how-many-reps-and-sets-for-muscle-growth/", "Reps & Sets"),
    ("What Is Progressive Overload", "/what-is-progressive-overload/", "Training Principles"),
    ("Reps and Sets for Women", "/reps-and-sets-for-woman/", "Reps & Sets"),
]
plans = [("Push Pull Legs Workout Plan", "/workout-plans/push-pull-legs/", "Legs B — Hypertrophy", "4 × 10–12 · Rest 2 min", "6 days/week · Intermediate")]
alternatives = [
    ("Barbell Romanian Deadlift", "/exercises/barbell-romanian-deadlift/", "Hamstrings, Glutes"),
    ("Barbell Back Squat", "/exercises/barbell-back-squat/", "Quads, Glutes"),
    ("Barbell Bulgarian Split Squat", "/exercises/barbell-bulgarian-split-squat/", "Quads, Glutes"),
]

# ---------------------------------------------------------------- schema (FAQPage + ImageObject + Article; no HowTo)
schema = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Article", "headline": name, "description": meta_desc, "dateModified": "2026-10-29",
         "image": {"@type": "ImageObject", "contentUrl": f"{SITE}/wp-content/uploads/2026/10/Barbell-Hip-Thrust.gif", "caption": alt_text}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ],
}

toc = [("how-to", "How to Do It"), ("muscles", "Muscles Worked"), ("sets", "Sets & Reps"), ("mistakes", "Common Mistakes"),
       ("tips", "Tips"), ("mods", "Modifications"), ("plans", "Workout Plans"), ("alternatives", "Alternatives"),
       ("faq", "FAQs"), ("sources", "Sources")]

css = """
:root{--bg:#f8f7f5;--card:#fff;--subtle:#f0efed;--fg:#1a1917;--muted:#6b6860;--border:#e5e3de;--strong:#ccc9c2;
--accent:#c0392b;--accent-dark:#96291f;--accent-bg:#fdf1f0;--good:#1e7a4c;--good-bg:#eaf6ef;--new:#1d5fbf;--new-bg:#eaf1fc}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141312;--card:#1e1d1b;--subtle:#252320;--fg:#f0ede8;--muted:#a8a49d;
--border:#2e2c28;--strong:#3d3a34;--accent:#e04d3d;--accent-dark:#f06050;--accent-bg:#2a1513;--good:#5cc28d;--good-bg:#14261c;--new:#7fb0f5;--new-bg:#14203a}}
:root[data-theme="dark"]{--bg:#141312;--card:#1e1d1b;--subtle:#252320;--fg:#f0ede8;--muted:#a8a49d;--border:#2e2c28;--strong:#3d3a34;
--accent:#e04d3d;--accent-dark:#f06050;--accent-bg:#2a1513;--good:#5cc28d;--good-bg:#14261c;--new:#7fb0f5;--new-bg:#14203a}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 Inter,system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
a{color:var(--accent)}a:hover{color:var(--accent-dark)}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}
.preview-bar{background:var(--new-bg);color:var(--new);font-size:13px;padding:8px 16px;text-align:center;border-bottom:1px solid var(--border)}
.new{display:inline-block;font-size:10px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;background:var(--new-bg);color:var(--new);
border:1px solid currentColor;border-radius:4px;padding:1px 6px;margin-left:8px;vertical-align:middle}
.crumbs{font-size:13px;color:var(--muted);padding:18px 0 6px}.crumbs a{color:var(--muted);text-decoration:none}
h1{font-size:clamp(28px,4vw,40px);line-height:1.15;margin:4px 0 8px;letter-spacing:-.02em}
h2{font-size:24px;line-height:1.25;margin:0 0 16px;letter-spacing:-.01em}h3{font-size:17px;margin:0 0 6px}
.sub{color:var(--muted);font-size:17px;margin:0 0 14px;max-width:760px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 10px}
.chip{font-size:13px;padding:4px 12px;border-radius:999px;background:var(--subtle);border:1px solid var(--border);color:var(--fg);text-decoration:none}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.updated{font-size:13px;color:var(--muted);margin-bottom:22px}
.hero{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;margin-bottom:22px}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px}
.gif{padding:12px;display:flex;align-items:center;justify-content:center}
.gif img{width:100%;max-width:440px;height:auto;border-radius:10px;background:#fff}
.profile{padding:18px 20px}.profile h2{font-size:18px;margin-bottom:10px}
.profile dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:9px 14px;font-size:14px}
.profile dt{color:var(--muted)}.profile dd{margin:0;font-weight:600}
.profile dd a{color:var(--fg);text-decoration:none;border-bottom:1px dashed var(--strong)}
.note{display:block;font-weight:400;font-size:12px;color:var(--muted)}
.qa{background:var(--accent-bg);border-left:4px solid var(--accent);border-radius:10px;padding:16px 20px;margin:0 0 22px}
.qa b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:4px}
.layout{display:grid;grid-template-columns:220px 1fr;gap:28px;align-items:start}
.toc{position:sticky;top:16px;padding:16px;font-size:14px}.toc b{display:block;margin-bottom:8px}
.toc ol{margin:0;padding-left:18px}.toc li{margin:4px 0}.toc a{color:var(--fg);text-decoration:none}.toc a:hover{color:var(--accent)}
section{padding:24px;margin-bottom:20px}
.steps{list-style:none;margin:0;padding:0;counter-reset:s}
.steps li{display:grid;grid-template-columns:36px 1fr;gap:14px;padding:12px 0;border-top:1px solid var(--border)}
.steps li:first-child{border-top:0}
.num{width:36px;height:36px;border-radius:50%;background:var(--accent);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.steps p,.item p{margin:0;color:var(--muted)}
.mus{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.mus h3{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:8px}
.mus ul{list-style:none;margin:0;padding:0}.mus li{padding:8px 0;border-top:1px solid var(--border);font-size:15px}
.mus li b{display:block}.mus li span{color:var(--muted);font-size:14px}
.tbl{width:100%;border-collapse:collapse;font-size:15px}
.tbl th,.tbl td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--border)}
.tbl th{background:var(--subtle);font-size:13px;text-transform:uppercase;letter-spacing:.04em}
.tbl-note{font-size:13px;color:var(--muted);margin:10px 0 0}
.item{display:grid;grid-template-columns:28px 1fr;gap:12px;padding:12px 0;border-top:1px solid var(--border)}
.item:first-of-type{border-top:0}
.ic{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.ic.x{background:var(--accent-bg);color:var(--accent)}.ic.ok{background:var(--good-bg);color:var(--good)}
.mods{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.mod{border:1px solid var(--border);border-radius:12px;padding:14px 16px;background:var(--bg)}
.lvl{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.lvl.e{color:var(--good)}.lvl.h{color:var(--accent)}.mod p{margin:4px 0 0;color:var(--muted);font-size:15px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.ccard{display:block;border:1px solid var(--border);border-radius:12px;padding:14px;background:var(--bg);color:var(--fg);text-decoration:none}
.ccard:hover{border-color:var(--accent)}.ccard img{width:100%;aspect-ratio:1;object-fit:contain;background:#fff;border-radius:8px;margin-bottom:8px}
.ccard small{color:var(--muted);display:block}
.plan{display:flex;gap:16px;align-items:center;border:1px solid var(--border);border-radius:12px;padding:16px;background:var(--bg);color:var(--fg);text-decoration:none}
.plan:hover{border-color:var(--accent)}.plan .day{background:var(--accent);color:#fff;border-radius:8px;padding:8px 12px;font-weight:700;font-size:14px;white-space:nowrap}
.plan small{display:block;color:var(--muted)}
details{border-top:1px solid var(--border);padding:12px 0}details:first-of-type{border-top:0}
summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:12px}
summary::-webkit-details-marker{display:none}summary::after{content:"+";color:var(--accent);font-size:20px;line-height:1}
details[open] summary::after{content:"−"}details p{margin:8px 0 0;color:var(--muted)}
.src{margin:0;padding-left:20px;font-size:14px;color:var(--muted)}.src a{word-break:break-all}
sup.cite a{text-decoration:none;font-size:11px}
.disc{font-size:13px;color:var(--muted);padding:0 4px 30px}
.cta{text-align:center;padding:26px}.btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;padding:11px 22px;border-radius:999px;font-weight:600}
.btn:hover{background:var(--accent-dark);color:#fff}
@media (max-width:860px){.hero,.layout,.mus,.mods{grid-template-columns:1fr}.toc{position:static}.cards{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.cards{grid-template-columns:1fr}section{padding:18px}.plan{flex-direction:column;align-items:flex-start}}
"""

H = []
w = H.append
w(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(meta_title)}</title><meta name="description" content="{E(meta_desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<style>{css}</style></head><body>
<div class="preview-bar">Preview of the exercise page after the plugin update. Sections marked <span class="new">New</span> come from the new plugin fields.</div>
<div class="wrap">
<nav class="crumbs"><a href="{SITE}/">Home</a> › <a href="{SITE}/exercises/">Exercises</a> › {E(name)}</nav>
<h1>{E(name)}</h1><p class="sub">{E(basics['Subtitle'])}</p>
<div class="chips">""")
for tg in tags:
    w(f'<a class="chip" href="#">{E(tg)}</a>')
w('</div><div class="updated">Last updated: October 29, 2026 <span class="new">New</span></div>')

# hero
w(f'<div class="hero"><div class="card gif"><img src="{b64(gif_path)}" width="360" height="360" loading="eager" alt="{E(alt_text)}"></div>')
w('<div class="card profile"><h2>Exercise Profile</h2><dl>')
for label, key, link in [("Target Muscle", "Target Muscle (sidebar)", True), ("Body Part", "Body Part", True), ("Equipment", "Equipment", True),
                         ("Category", "Category", False), ("Skill Level", "Skill Level", True), ("Movement", "Movement Pattern", False),
                         ("Also Known As", "Also Known As", False)]:
    v = E(basics[key])
    dd = f'<a href="#">{v}</a>' if link else v
    w(f"<dt>{label}</dt><dd>{dd}</dd>")
w(f'<dt>Est. Calories</dt><dd>{E(basics["Approx. Calories per set"])} per set<span class="note">Estimate for a 70 kg person, 30–60 s set</span></dd>')
w("</dl></div></div>")
w(f'<div class="qa"><b>Quick Answer</b>{E(qa)}</div>')

# body
w('<div class="layout"><nav class="card toc" aria-label="Contents"><b>On this page</b><ol>')
for i, l in toc:
    w(f'<li><a href="#{i}">{l}</a></li>')
w("</ol></nav><main>")

w(f'<section id="how-to" class="card"><h2>How to Do the {E(name)}</h2><ol class="steps">')
for n, ti, de in steps:
    w(f'<li><span class="num">{n}</span><div><h3>{E(ti)}</h3><p>{E(de)}</p></div></li>')
w("</ol></section>")

w(f'<section id="muscles" class="card"><h2>What Muscles Does the {E(name)} Work?</h2><div class="mus">')
for title, lst in [("Primary", primary), ("Secondary", secondary)]:
    w(f"<div><h3>{title}</h3><ul>")
    for line in lst:
        n, d = split_muscle(line)
        w(f"<li><b>{E(n)}</b><span>{E(d)}</span></li>")
    w("</ul></div>")
w("</div></section>")

w('<section id="sets" class="card"><h2>How Many Sets and Reps Should You Do?</h2><div style="overflow-x:auto"><table class="tbl"><thead><tr>')
w("".join(f"<th>{E(c)}</th>" for c in sets[0]) + "</tr></thead><tbody>")
for r in sets[1:]:
    w("<tr>" + "".join(f"<td>{'<b>'+E(c)+'</b>' if i == 0 else E(c)}</td>" for i, c in enumerate(r)) + "</tr>")
w('</tbody></table></div><p class="tbl-note">Rest times follow the <a href="https://pubmed.ncbi.nlm.nih.gov/19204579/" target="_blank" rel="noopener">ACSM progression models position stand</a>.</p></section>')

w('<section id="mistakes" class="card"><h2>Common Mistakes That Reduce Results</h2>')
for ti, de in mistakes:
    w(f'<div class="item"><span class="ic x">✕</span><div><h3>{E(ti)}</h3><p>{E(de)}</p></div></div>')
w("</section>")

w('<section id="tips" class="card"><h2>Tips for Better Results</h2>')
for ti, de in tips:
    w(f'<div class="item"><span class="ic ok">✓</span><div><h3>{E(ti)}</h3><p>{cite_marks(de)}</p></div></div>')
w("</section>")

w('<section id="mods" class="card"><h2>Modifications and Progressions</h2><div class="mods">')
for ty, ti, de in mods:
    easy = "Easier" in ty
    w(f'<div class="mod"><span class="lvl {"e" if easy else "h"}">{"▼ Easier" if easy else "▲ Harder"}</span><h3>{E(ti)}</h3><p>{E(de)}</p></div>')
w("</div></section>")

w(f'<section id="plans" class="card"><h2>Workout Plans With the {E(name)}<span class="new">New</span></h2>')
for ti, url, day, presc, meta in plans:
    w(f'<a class="plan" href="{SITE}{url}"><span class="day">{E(day.split(" — ")[0])}</span><div><b>{E(ti)}</b><small>{E(day)} · {E(presc)}</small><small>{E(meta)}</small></div></a>')
w("</section>")

w(f'<section id="alternatives" class="card"><h2>{E(name)} Alternatives<span class="new">New</span></h2><div class="cards">')
for ti, url, mus in alternatives:
    img = f'<img src="{b64(alt_gifs[ti])}" width="180" height="180" alt="{E(ti)} exercise demonstration">' if ti in alt_gifs else ""
    w(f'<a class="ccard" href="{SITE}{url}">{img}<b>{E(ti)}</b><small>{E(mus)}</small></a>')
w("</div></section>")

w('<section id="faq" class="card"><h2>Frequently Asked Questions</h2>')
for q, a in faqs:
    w(f"<details><summary>{E(q)}</summary><p>{cite_marks(a)}</p></details>")
w("</section>")

w('<section id="sources" class="card"><h2>Sources<span class="new">New</span></h2><ol class="src">')
for txt, url in sources:
    w(f'<li>{E(txt)} <a href="{E(url)}" target="_blank" rel="noopener">{E(url)}</a></li>')
w("</ol></section>")

w('<section class="card"><h2>Related Training Articles<span class="new">New field</span></h2><div class="cards">')
for ti, url, cat in related:
    w(f'<a class="ccard" href="{SITE}{url}"><small>{E(cat)}</small><b>{E(ti)}</b></a>')
w("</div></section>")

w('<p class="disc">If you have an existing injury or medical condition, check with your doctor before adding this exercise to your training.</p>')
w(f'<div class="card cta"><h2>Looking for more exercises?</h2><p class="sub" style="margin:0 auto 14px">Browse the full exercise library, filtered by muscle group, equipment, and skill level.</p><a class="btn" href="{SITE}/exercises/">Browse All Exercises →</a></div>')
w("</main></div><div style=\"height:40px\"></div></div></body></html>")

open(out_path, "w", encoding="utf-8").write("".join(H))
print("saved", out_path)
