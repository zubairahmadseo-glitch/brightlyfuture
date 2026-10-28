"""Build ExerciseMenu workout plan pages as WordPress block content.

Each page is a series of Custom HTML blocks (<!-- wp:html -->):
  1. shared CSS  2. intro (hero, quick answer, takeaways, contents)
  3+. one block per section  ... FAQ, related plans, references, schema.
Editing in WordPress: open the Custom HTML block for the section you want.

Usage: python3 build.py            -> writes out/<slug>.html and preview/<slug>.html
"""
import html
import importlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "shared.css").read_text()
SITE = "https://exercisemenu.com"

PAGES = [
    "push_pull_legs", "full_body_beginners", "upper_lower", "five_by_five",
    "bro_split", "four_day_split", "three_day_full_body", "lean_bulk",
    "hypertrophy_program", "skinny_guys", "five_day_split", "ppl_hypertrophy",
    "beginner_strength", "women_strength", "powerlifting_beginners",
]

# Live exercise pages (verified 200 on 2026-10-28; not in the XML sitemap).
EXERCISE_LINKS = {
    "Barbell Bench Press": "/exercises/barbell-bench-press/",
    "Incline Barbell Bench Press": "/exercises/barbell-incline-bench-press/",
    "Dumbbell Bench Press": "/exercises/dumbbell-bench-press/",
    "Barbell Curl": "/exercises/barbell-curl/",
    "Dumbbell Biceps Curl": "/exercises/dumbbell-biceps-curl/",
    "Hammer Curl": "/exercises/dumbbell-hammer-curl/",
    "Dumbbell Romanian Deadlift": "/dumbbell-romanian-deadlift/",
    "Trap Bar Deadlift": "/how-to-trap-bar-deadlift/",
}

# All 15 batch-1 plans, for related-plan cards.
PLANS = {
    "push-pull-legs": ("Muscle Building", "Push Pull Legs Workout Plan", "6-day PPL with heavy A days and higher-rep B days.", "6 days · Intermediate–Advanced"),
    "full-body-workout-plan": ("Beginner", "Full Body Workout Plan for Beginners", "Three full-body gym days led by the squat, bench press and deadlift.", "3 days · Beginner"),
    "upper-lower-split": ("Muscle Building", "4-Day Upper Lower Split", "Upper and lower body twice a week with simple double progression.", "4 days · Beginner–Intermediate"),
    "5x5-workout": ("Strength", "5×5 Strength & Muscle Program", "Two alternating barbell workouts, adding weight every session.", "3 days · Beginner"),
    "bro-split": ("Muscle Building", "Bro Split 5-Day Workout Plan", "One muscle group per day, done the evidence-based way.", "5 days · Intermediate"),
    "4-day-workout-split": ("Muscle Building", "4-Day Workout Split", "Torso/Limbs split plus how every 4-day option compares.", "4 days · Intermediate"),
    "3-day-full-body-workout": ("Muscle Building", "3-Day Full Body Workout (Intermediate)", "Heavy, light and medium full-body days for busy lifters.", "3 days · Intermediate"),
    "lean-bulk-workout-plan": ("Muscle Building", "12-Week Lean Bulk Workout Plan", "Three training phases matched to a small calorie surplus.", "4 days · Intermediate"),
    "hypertrophy-program": ("Muscle Building", "4-Day Hypertrophy Program", "A 6-week mesocycle with set ramps and RIR targets.", "4 days · Intermediate"),
    "workout-plan-for-skinny-guys": ("Muscle Building", "Workout Plan for Skinny Guys", "Short compound-first sessions plus an eating plan that works.", "3 days · Beginner–Intermediate"),
    "5-day-workout-split": ("Muscle Building", "5-Day Workout Split", "Upper, Lower, Push, Pull, Legs: every muscle twice a week.", "5 days · Intermediate"),
    "ppl-hypertrophy-program": ("Advanced", "6-Day PPL Hypertrophy Program", "High-volume PPL with intensity techniques for experienced lifters.", "6 days · Advanced"),
    "beginner-strength-training-program": ("Strength", "Beginner Strength Training Program", "12 weeks of linear progression on the main lifts.", "3 days · Beginner"),
    "strength-training-for-women": ("Strength", "Strength Training Plan for Women", "Three full-body days with glute, posture and bone-health focus.", "3 days · Beginner–Intermediate"),
    "powerlifting-program-for-beginners": ("Strength", "Powerlifting Program for Beginners", "12 weeks of squat, bench and deadlift ending in a test day.", "3 days · Beginner–Intermediate"),
}

# Short labels for the "Jump to" chips (falls back to the H2 text).
CHIPS = {
    "workouts": "Workouts", "schedule": "Schedule", "volume": "Weekly sets", "progression": "Progression",
    "deload": "Deload", "nutrition": "Nutrition", "warmup": "Warm-up", "mistakes": "Mistakes",
    "comparison": "Compare splits", "compare": "Compare plans", "who": "Who it's for", "options": "Choose a split",
    "what-is": "What is it", "why": "Why it works", "phases": "12-week phases", "rules": "Competition rules",
    "rpe": "RPE scale", "rest": "Rest & warm-up", "taper": "Test day", "next": "After 12 weeks",
    "mesocycle": "6-week block", "split": "The split", "principles": "The science", "technique": "Technique",
    "techniques": "Drop sets & rest-pause", "specialization": "Weak points", "eating": "Eating plan",
    "cardio": "Cardio & sleep", "rate": "Rate of gain", "tracking": "Tracking", "after": "After 12 weeks",
    "program": "Program phases", "myths": "Will I get bulky?", "cycle": "Menstrual cycle", "bones": "Bone health",
    "subs": "Exercise swaps", "start": "Starting weights", "stalls": "When you stall", "accessories": "Accessories",
    "rest-days": "Rest days",
}

AUTHOR_BOX = """<aside class="emp-author" aria-label="About the author">
<div class="emp-author-av" aria-hidden="true">SB</div>
<div><p class="emp-author-n">Sadia Baloch</p>
<p class="emp-author-c">FISAF-certified fitness trainer</p>
<p>Sadia Baloch is a FISAF-certified fitness trainer who has personally coached hundreds of clients over the past 7 years. She specializes in strength training, fat loss, and workout programming for beginners through intermediate lifters. Every article on ExerciseMenu.com is based on the same methods she uses with her in-person clients daily.</p></div>
</aside>"""


def esc(s):
    return html.escape(s, quote=True)


def block(inner):
    return "<!-- wp:html -->\n" + inner.strip() + "\n<!-- /wp:html -->"


def ex_name(name):
    for key, url in EXERCISE_LINKS.items():
        if name == key or name.startswith(key + " ("):
            return f'<a href="{SITE}{url}">{esc(name)}</a>'
    return esc(name)


def workout_card(day):
    rows = []
    for i, ex in enumerate(day["exercises"], 1):
        name, target, sets, rest, effort = ex
        rows.append(
            f'<tr><td class="n">{i}</td><td class="x">{ex_name(name)}<span class="t">{esc(target)}</span></td>'
            f'<td class="s">{esc(sets)}</td><td class="r">{esc(rest)}</td><td class="e">{esc(effort)}</td></tr>'
        )
    total_sets = day.get("total_sets") or sum(_first_int(e[2]) for e in day["exercises"])
    meta = [f'⏱ {day["time"]}', f'🎯 {len(day["exercises"])} exercises', f'📊 {total_sets} working sets', f'💪 {day["focus"]}']
    notes = f'<div class="emp-wo-notes"><p><strong>Notes:</strong> {day["notes"]}</p></div>' if day.get("notes") else ""
    return f'''<div class="emp-wo">
<div class="emp-wo-h c{day.get("color", 1)}"><h3>{esc(day["title"])}</h3><span class="emp-tag">{esc(day["tag"])}</span></div>
<div class="emp-wo-meta">{"".join(f"<span>{m}</span>" for m in meta)}</div>
<div class="emp-tw"><table class="emp-ex"><thead><tr><th>#</th><th>Exercise</th><th>Sets × Reps</th><th>Rest</th><th>Effort</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody></table></div>
{notes}
</div>'''


def _first_int(s):
    m = re.match(r"\s*(\d+)", s)
    return int(m.group(1)) if m else 0


def tabs(days):
    inputs, labels, panels = [], [], []
    for i, d in enumerate(days, 1):
        chk = " checked" if i == 1 else ""
        inputs.append(f'<input type="radio" name="emp-day" id="emp-t{i}"{chk}>')
        labels.append(f'<label for="emp-t{i}">{esc(d["tab"])}<small>{esc(d["tab_sub"])}</small></label>')
        panels.append(f'<div class="emp-panel emp-p{i}">\n{workout_card(d)}\n</div>')
    inputs.append('<input type="radio" name="emp-day" id="emp-tall">')
    labels.append('<label for="emp-tall">All days<small>Show every workout</small></label>')
    return (
        '<div class="emp-tabs">\n' + "\n".join(inputs)
        + '\n<div class="emp-tabbar" role="group" aria-label="Choose a training day">' + "".join(labels) + "</div>\n"
        + '<div class="emp-panels">\n' + "\n".join(panels) + "\n</div>\n</div>"
    )


def week(schedule):
    cells = []
    for dayname, label, cls in schedule:
        cells.append(f'<div class="emp-wd {cls}"><b>{esc(dayname)}</b><span>{esc(label)}</span></div>')
    return '<div class="emp-week">' + "".join(cells) + "</div>"


def wrap(inner):
    return f'<div class="emp">\n{inner.strip()}\n</div>'


def render(p):
    blocks = [block("<style>\n" + CSS.strip() + "\n</style>")]

    hero = f'''<div class="emp-hero">
<span class="emp-badge">{esc(p["badge"])}</span>
<p class="emp-hero-lead">{p["hero_lead"]}</p>
<ul class="emp-hero-meta">{"".join(f"<li>{m}</li>" for m in p["hero_meta"])}<li>📄 Last reviewed: October 2026</li></ul>
<a class="emp-jump" href="#workouts">See the workouts ↓</a>
</div>
<div class="emp-stats">{"".join(f'<div class="emp-stat"><div class="emp-stat-v">{esc(v)}</div><div class="emp-stat-l">{esc(l)}</div></div>' for v, l in p["stats"])}</div>
<div class="emp-answer"><span class="emp-label">Quick answer</span><p>{p["quick_answer"]}</p></div>
{p["intro"]}
<nav class="emp-chips" aria-label="Jump to a section"><span>Jump to:</span>{"".join(f'<a href="#{sid}">{esc(CHIPS.get(sid, t))}</a>' for sid, t, _ in p["sections"])}<a href="#faq">FAQ</a></nav>'''
    blocks.append(block(wrap(hero)))

    for sid, title, body in p["sections"]:
        body = body.replace("{{WEEK}}", week(p["schedule"])).replace("{{TABS}}", tabs(p["days"]))
        blocks.append(block(wrap(f'<section class="emp-section" id="{sid}">\n<h2>{esc(title)}</h2>\n{body.strip()}\n</section>')))

    faq_html = "".join(
        f'<details><summary>{esc(q)}</summary><div class="emp-faq-a"><p>{a}</p></div></details>\n' for q, a in p["faqs"]
    )
    blocks.append(block(wrap(f'<section class="emp-section emp-faq" id="faq">\n<h2>{esc(p["faq_title"])}</h2>\n{faq_html}</section>')))
    blocks.append(block(wrap(AUTHOR_BOX)))

    cards = []
    for slug in p["related"]:
        tag, title, desc, meta = PLANS[slug]
        cards.append(
            f'<a class="emp-card" href="{SITE}/workout-plans/{slug}/"><span class="emp-card-tag">{esc(tag)}</span>'
            f'<span class="emp-card-t">{esc(title)}</span><span class="emp-card-d">{esc(desc)}</span><span class="emp-card-m">{esc(meta)}</span></a>'
        )
    refs = "".join(f'<li>{r[0]} <a href="{r[1]}" rel="noopener" target="_blank">{esc(r[1].replace("https://", ""))}</a></li>' for r in p["refs"])
    tail = f'''<section class="emp-section" id="related-plans">
<h2>Related Workout Plans</h2>
<div class="emp-related">{"".join(cards)}</div>
</section>
<div class="emp-refs"><h3>References</h3><ol>{refs}</ol></div>
<p class="emp-disclaimer">{p["disclaimer"]}</p>'''
    blocks.append(block(wrap(tail)))

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in p["faqs"]
        ],
    }
    blocks.append(block('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>"))
    return "\n\n".join(blocks) + "\n"


def preview(p, content):
    body = re.sub(r"<!-- /?wp:html -->", "", content)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(p["meta_title"])}</title><meta name="description" content="{esc(p["meta_desc"])}">
<style>body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;margin:0;background:#fff}}.wrap{{max-width:860px;margin:0 auto;padding:16px}}h1.pt{{font-size:2rem;color:#1a1a2e;line-height:1.2}}</style></head>
<body><div class="wrap"><p style="font-size:.8rem;color:#6b7280">Home › Workout Plans › {esc(p["title"])}</p><h1 class="pt">{esc(p["title"])}</h1>
{body}</div></body></html>'''


def main():
    out, prev = ROOT / "out", ROOT / "preview"
    out.mkdir(exist_ok=True)
    prev.mkdir(exist_ok=True)
    manifest = []
    for mod_name in [m for m in PAGES if (ROOT / "content" / (m + ".py")).exists()]:
        p = importlib.import_module("content." + mod_name).PAGE
        content = render(p)
        (out / f'{p["slug"]}.html').write_text(content)
        (prev / f'{p["slug"]}.html').write_text(preview(p, content))
        manifest.append({k: p[k] for k in ("num", "slug", "title", "meta_title", "meta_desc", "focus_kw")})
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"built {len(manifest)} pages")


if __name__ == "__main__":
    main()
