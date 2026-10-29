"""Build the /exercises/ hub page design (single HTML file, GIF thumbnails embedded for the preview).

Usage: python3 build_hub.py <exercises.json> <gif-zip-root> <out.html>
"""
import base64
import glob
import html
import json
import sys

ex_json, gif_root, out_path = sys.argv[1:4]
E = html.escape
SITE = "https://exercisemenu.com"

GROUPS = [
    ("chest", "Chest", "Chest Exercises", "Presses on flat and incline benches that build the chest, front shoulders and triceps.",
     ["barbell-bench-press", "barbell-incline-bench-press", "dumbbell-bench-press", "dumbbell-incline-bench-press"]),
    ("back", "Back", "Back Exercises", "Rows that build the lats and upper back and balance all the pressing you do.",
     ["barbell-bent-over-row", "dumbbell-one-arm-row"]),
    ("shoulders", "Shoulders", "Shoulder Exercises", "Overhead presses for the front delts and lateral raises for the side delts.",
     ["barbell-overhead-press", "dumbbell-seated-shoulder-press", "dumbbell-lateral-raise"]),
    ("biceps", "Biceps & Forearms", "Biceps and Forearm Exercises", "Curls with a barbell, EZ bar and dumbbells. Hammer curls add more work for the brachialis and forearms.",
     ["barbell-curl", "ez-bar-curl", "dumbbell-biceps-curl", "dumbbell-hammer-curl", "barbell-preacher-curl"]),
    ("triceps", "Triceps", "Triceps Exercises", "A heavy compound press and a lying extension that trains all three triceps heads.",
     ["barbell-close-grip-bench-press", "barbell-lying-triceps-extension"]),
    ("quads", "Quads & Legs", "Leg Exercises for Quads and Glutes", "Squats and single-leg exercises that build the quads, glutes and adductors.",
     ["barbell-back-squat", "barbell-bulgarian-split-squat", "dumbbell-lunge"]),
    ("glutes", "Glutes & Hamstrings", "Glute and Hamstring Exercises", "Hip hinges and hip thrusts that train the glutes, hamstrings and lower back.",
     ["barbell-deadlift", "barbell-romanian-deadlift", "barbell-hip-thrust"]),
    ("calves", "Calves", "Calf Exercises", "Standing and seated calf raises through a full range of motion.",
     ["barbell-standing-calf-raise", "barbell-seated-calf-raise"]),
]
GIF_KEY = {
    "barbell-back-squat": "Barbell-Full-Squat", "barbell-bench-press": "Barbell-Bench-Press_", "barbell-bent-over-row": "Bent-Over-Row",
    "barbell-bulgarian-split-squat": "Single-Leg-Split-Squat", "barbell-close-grip-bench-press": "Close-Grip", "barbell-curl": "00311301-Barbell-Curl",
    "barbell-deadlift": "00321301", "barbell-hip-thrust": "Hip-Thrust", "barbell-incline-bench-press": "Barbell-Incline-Bench",
    "barbell-lying-triceps-extension": "Lying-Triceps", "barbell-overhead-press": "Standing-Shoulders-Press", "barbell-preacher-curl": "Preacher",
    "barbell-romanian-deadlift": "Romanian", "barbell-seated-calf-raise": "Seated-Calf", "barbell-standing-calf-raise": "Standing-Calf",
    "dumbbell-bench-press": "02891301", "dumbbell-biceps-curl": "Dumbbell-Biceps-Curl", "dumbbell-hammer-curl": "Hammer",
    "dumbbell-incline-bench-press": "Dumbbell-Incline", "dumbbell-lateral-raise": "Lateral-Raise", "dumbbell-lunge": "Dumbbell-Lunge",
    "dumbbell-one-arm-row": "One-Arm-Row", "dumbbell-seated-shoulder-press": "Seated-Shoulder", "ez-bar-curl": "EZ-Barbell",
}
STARTERS = ["dumbbell-lunge", "barbell-hip-thrust", "dumbbell-bench-press", "dumbbell-one-arm-row", "dumbbell-seated-shoulder-press", "dumbbell-biceps-curl"]

data = {r[0]: dict(zip(["slug", "name", "target", "body", "equip", "cat", "level", "sub"], r)) for r in json.load(open(ex_json))}
for d in data.values():
    e = d["equip"].lower()
    d["kit"] = "EZ Bar" if e.startswith("ez") else ("Dumbbell" if e.startswith("dumbbell") else "Barbell")
    path = [g for g in glob.glob(f"{gif_root}/*/*/*_180.gif") if GIF_KEY[d["slug"]] in g][0]
    d["gif"] = "data:image/gif;base64," + base64.b64encode(open(path, "rb").read()).decode()
total = len(data)


def card(d, group):
    return f"""<li class="ex-card" data-group="{group}" data-kit="{E(d['kit'])}" data-level="{E(d['level'])}" data-type="{E(d['cat'])}" data-name="{E(d['name'].lower())} {E(d['target'].lower())} {E(d['body'].lower())}">
  <a href="{SITE}/exercises/{d['slug']}/">
    <span class="ex-thumb"><img src="{d['gif']}" alt="{E(d['name'])} exercise demonstration" width="180" height="180" loading="lazy" decoding="async"></span>
    <span class="ex-body">
      <span class="ex-name">{E(d['name'])}</span>
      <span class="ex-target">Target: {E(d['target'])}</span>
      <span class="ex-tags"><span>{E(d['kit'])}</span><span>{E(d['cat'])}</span><span class="lvl-{d['level'].lower()}">{E(d['level'])}</span></span>
    </span>
  </a>
</li>"""


faqs = [
    ("How do I choose exercises for a workout?",
     "Pick one or two compound lifts for the main muscle groups you are training, such as a squat, press or row, then add one or two isolation exercises for smaller muscles like the biceps, triceps or calves.",
     ("compound vs isolation exercises", "/compound-vs-isolation/")),
    ("How many exercises should I do per muscle group?",
     "Most people do well with one to three exercises per muscle group in a session. Weekly sets matter more than the number of exercises.",
     ("how many exercises per muscle group", "/how-many-exercises-per-muscle-group-should-you-do/")),
    ("How many sets and reps should I do?",
     "Every exercise guide has a sets and reps table for muscle growth, strength, endurance and beginners. For muscle growth, 3–4 sets of roughly 6–12 reps per exercise is a common starting point.",
     ("reps and sets for muscle growth", "/how-many-reps-and-sets-for-muscle-growth/")),
    ("Do I need a gym for these exercises?",
     "Most exercises in the library use a barbell, dumbbells or an EZ bar, and some need a bench or rack. The equipment for each one is listed on its card and in its guide.",
     None),
]

schema = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "CollectionPage", "@id": f"{SITE}/exercises/#page", "url": f"{SITE}/exercises/",
         "name": "Exercise Library", "description": "Step-by-step exercise guides with GIF demonstrations, muscles worked, sets and reps, and common mistakes.",
         "mainEntity": {"@type": "ItemList", "numberOfItems": total, "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/exercises/{s}/", "name": data[s]["name"]}
             for i, s in enumerate([s for g in GROUPS for s in g[4]])]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Exercises", "item": f"{SITE}/exercises/"}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a, _ in faqs]},
    ],
}

css = """
:root{--red:#dd232f;--red-dark:#b51a24;--red-soft:#fdecee;--ink:#161616;--text:#444;--muted:#6d6d6d;--line:#e6e6e6;--bg:#fff;--soft:#f7f7f7;--black:#0b0b0b}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 Inter,system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
a{color:var(--red)}a:hover{color:var(--red-dark)}
.wrap{max-width:1200px;margin:0 auto;padding:0 16px}
h1,h2,h3{color:var(--ink);font-weight:700;letter-spacing:-.02em;margin:0}
.dev-note{background:#fff8e1;border-bottom:1px solid #f1d98b;color:#6b5600;font-size:13px;padding:8px 16px;text-align:center}
/* hero */
.hero{background:radial-gradient(120% 140% at 85% 30%,#5a0d12 0%,#1a0507 38%,#000 70%);color:#fff;padding:64px 0 48px;text-align:center}
.hero h1{color:#fff;font-size:clamp(34px,5.4vw,56px);line-height:1.08}
.hero h1 span{display:block;color:var(--red)}
.hero p{max-width:780px;margin:18px auto 0;color:#e9e9e9;font-size:16px}
.hero p a{color:#ff6b74}
.search{max-width:620px;margin:28px auto 0;position:relative}
.search input{width:100%;padding:16px 20px 16px 50px;border-radius:999px;border:0;font:inherit;font-size:16px;color:var(--ink);box-shadow:0 8px 30px rgba(0,0,0,.35)}
.search input:focus{outline:3px solid var(--red)}
.search svg{position:absolute;left:18px;top:50%;transform:translateY(-50%);width:20px;height:20px;color:#888}
.stats{display:flex;justify-content:center;gap:56px;flex-wrap:wrap;margin-top:34px}
.stats b{display:block;color:var(--red);font-size:30px;line-height:1.1}
.stats span{font-size:14px;color:#ddd}
.crumbs{font-size:13px;color:var(--muted);padding:18px 0}.crumbs a{color:var(--muted);text-decoration:none}
/* muscle tiles */
.eyebrow{display:inline-block;color:var(--red);font-weight:700;font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px}
.sec{padding:36px 0}
.sec h2{font-size:clamp(26px,3.4vw,38px);line-height:1.15}
.lead{color:var(--muted);margin:8px 0 22px;max-width:760px}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;list-style:none;margin:0;padding:0}
.tile a{display:flex;align-items:center;gap:12px;border:1px solid var(--line);border-radius:14px;padding:14px 16px;color:var(--ink);text-decoration:none;background:#fff;transition:.15s}
.tile a:hover{border-color:var(--red);box-shadow:0 6px 18px rgba(221,35,47,.12)}
.tile i{width:40px;height:40px;border-radius:10px;background:var(--red-soft);color:var(--red);display:flex;align-items:center;justify-content:center;font-style:normal;font-weight:700;flex:none}
.tile b{display:block;font-size:15px}.tile small{color:var(--muted)}
/* steps */
.how{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;counter-reset:s;list-style:none;margin:0;padding:0}
.how li{background:var(--soft);border-radius:14px;padding:18px 18px 18px 64px;position:relative;font-size:15px}
.how li::before{counter-increment:s;content:counter(s);position:absolute;left:18px;top:18px;width:32px;height:32px;border-radius:50%;background:var(--red);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.how b{display:block;color:var(--ink);margin-bottom:2px}
/* filters */
.filters{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 0}
.frow{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.frow label{font-size:13px;font-weight:600;color:var(--ink)}
.frow select{font:inherit;font-size:14px;padding:8px 32px 8px 12px;border:1px solid var(--line);border-radius:999px;background:#fff;color:var(--ink)}
.frow .count{margin-left:auto;font-size:14px;color:var(--muted)}
.frow button{font:inherit;font-size:14px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:8px 14px;cursor:pointer}
.frow button:hover{border-color:var(--red);color:var(--red)}
/* groups + cards */
.group{padding:30px 0 6px;scroll-margin-top:70px}
.group h2{font-size:clamp(22px,2.6vw,28px)}
.group .lead{margin:6px 0 16px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;list-style:none;margin:0;padding:0}
.ex-card a{display:flex;flex-direction:column;height:100%;border:1px solid var(--line);border-radius:14px;overflow:hidden;color:var(--text);text-decoration:none;background:#fff;transition:.15s}
.ex-card a:hover{border-color:var(--red);box-shadow:0 8px 22px rgba(0,0,0,.08);transform:translateY(-2px)}
.ex-thumb{background:#fff;aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line)}
.ex-thumb img{width:100%;height:100%;object-fit:contain}
.ex-body{padding:12px 14px 14px;display:flex;flex-direction:column;gap:4px;flex:1}
.ex-name{color:var(--ink);font-weight:700;font-size:15.5px;line-height:1.3}
.ex-target{font-size:13px;color:var(--muted)}
.ex-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:8px}
.ex-tags span{font-size:11.5px;font-weight:600;padding:3px 9px;border-radius:999px;background:var(--soft);color:#555}
.ex-tags .lvl-beginner{background:#e8f5ee;color:#1a6e3a}.ex-tags .lvl-intermediate{background:#fef3cd;color:#7a5c00}.ex-tags .lvl-advanced{background:#fde8e8;color:#8b0000}
.empty{display:none;text-align:center;padding:40px 0;color:var(--muted)}
/* starter + includes */
.split{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.panel{border:1px solid var(--line);border-radius:16px;padding:24px;background:#fff}
.panel h3{font-size:20px;margin-bottom:6px}
.panel ul{margin:12px 0 0;padding:0;list-style:none}
.panel li{padding:9px 0;border-top:1px solid var(--line);display:flex;gap:10px;align-items:flex-start;font-size:15px}
.panel li:first-child{border-top:0}
.panel li::before{content:"→";color:var(--red);font-weight:700}
.panel.dark{background:var(--black);color:#ddd;border-color:#222}.panel.dark h3{color:#fff}.panel.dark li{border-color:#222}
/* next steps */
.cards3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.ncard{border:1px solid var(--line);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:8px;background:#fff}
.ncard h3{font-size:18px}.ncard p{margin:0;font-size:15px;color:var(--muted)}
.ncard .btn{margin-top:auto;align-self:flex-start}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--red);color:#fff!important;text-decoration:none;font-weight:600;padding:11px 20px;border-radius:8px;transition:.15s}
.btn:hover{background:var(--red-dark)}
.btn.ghost{background:transparent;border:2px solid #fff;color:#fff!important}.btn.ghost:hover{background:#fff;color:var(--ink)!important}
/* faq */
.faq details{border-bottom:1px solid var(--line);padding:16px 0}
.faq summary{cursor:pointer;list-style:none;font-weight:600;color:var(--ink);display:flex;justify-content:space-between;gap:12px;font-size:17px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--red);font-size:22px;line-height:1}
.faq details[open] summary::after{content:"\\2212"}
.faq p{margin:10px 0 0}
/* cta */
.cta{background:radial-gradient(120% 160% at 15% 20%,#5a0d12 0%,#1a0507 40%,#000 75%);color:#ddd;border-radius:20px;padding:44px 28px;text-align:center;margin:20px 0 56px}
.cta h2{color:#fff;font-size:clamp(26px,3.6vw,38px)}.cta h2 span{color:var(--red)}
.cta p{max-width:640px;margin:12px auto 22px}
.cta .row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
@media(max-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}.tiles{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.grid{grid-template-columns:repeat(2,1fr)}.how,.split,.cards3{grid-template-columns:1fr}.stats{gap:28px}
.frow{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}.frow::-webkit-scrollbar{display:none}
.frow label{position:absolute;left:-9999px}.frow select,.frow button{flex:none}.frow .count{display:none}}
@media(max-width:420px){.tiles{grid-template-columns:1fr}.grid{gap:10px}.ex-name{font-size:14px}}
"""

H = []
w = H.append
w(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<!--
  DEVELOPER NOTES (ExerciseMenu /exercises/ hub)
  - This page is the archive of the "exercise" post type (URL /exercises/). Build it as the plugin's archive template
    (archive-exercise.php) or an Elementor Pro Theme Builder "Archive" template for Exercises.
  - Every card, count and group must be generated from the Exercise posts (title, permalink, GIF, Target Muscle,
    Equipment, Category, Skill Level). GIFs are embedded here only for the preview; use the Media Library URLs.
  - Cards stay as normal <a href> links in the HTML so Google can crawl every exercise. Filters only hide/show cards.
  - Rank Math: Title "Exercise Library by Muscle Group: GIFs & Form Guides" · Description (see meta tag below) · Focus keyword "exercise library".
  - Output the JSON-LD below (CollectionPage + ItemList + BreadcrumbList + FAQPage). Do not let Rank Math add a second FAQPage.
-->
<title>Exercise Library by Muscle Group: GIFs &amp; Form Guides</title>
<meta name="description" content="Find exercises for chest, back, legs, shoulders and arms. Filter by equipment and level, then follow GIF form guides with sets, reps and common mistakes.">
<link rel="canonical" href="{SITE}/exercises/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<style>{css}</style></head><body>
<div class="dev-note">Design preview of the /exercises/ hub. Site header and footer come from the theme.</div>

<header class="hero">
  <div class="wrap">
    <h1>Exercise Library <span>Step-by-Step Form Guides</span></h1>
    <p>Browse gym exercises by muscle group, equipment and skill level. Each guide shows a GIF demonstration, step-by-step proper form, the muscles worked, and sets and reps for your goal.</p>
    <form class="search" role="search" onsubmit="return false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <label for="q" class="sr" style="position:absolute;left:-9999px">Search exercises</label>
      <input id="q" type="search" placeholder="Search exercises, e.g. squat or triceps" autocomplete="off">
    </form>
    <div class="stats">
      <div><b>{total}</b><span>Exercise guides</span></div>
      <div><b>{len(GROUPS)}</b><span>Muscle groups</span></div>
      <div><b>4</b><span>Training goals per guide</span></div>
    </div>
  </div>
</header>

<div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{SITE}/">Home</a> › <span>Exercises</span></nav>

  <section class="sec" style="padding-top:8px" aria-labelledby="by-muscle">
    <span class="eyebrow">Browse by muscle</span>
    <h2 id="by-muscle">Exercises by Muscle Group</h2>
    <p class="lead">Jump straight to the body part you are training today.</p>
    <ul class="tiles">""")
for gid, label, h2, intro, slugs in GROUPS:
    w(f'<li class="tile"><a href="#{gid}"><i>{len(slugs)}</i><span><b>{E(label)}</b><small>{len(slugs)} exercise{"s" if len(slugs) > 1 else ""}</small></span></a></li>')
w("""</ul>
  </section>

</div>

<div class="filters" id="library">
  <div class="wrap frow">
    <label for="f-group">Muscle</label>
    <select id="f-group"><option value="">All muscles</option>""")
for gid, label, *_ in GROUPS:
    w(f'<option value="{gid}">{E(label)}</option>')
w("""</select>
    <label for="f-kit">Equipment</label>
    <select id="f-kit"><option value="">All equipment</option><option>Barbell</option><option>Dumbbell</option><option>EZ Bar</option></select>
    <label for="f-level">Level</label>
    <select id="f-level"><option value="">All levels</option><option>Beginner</option><option>Intermediate</option></select>
    <label for="f-type">Type</label>
    <select id="f-type"><option value="">All types</option><option>Compound</option><option>Isolation</option></select>
    <button type="button" id="reset">Reset</button>
    <span class="count" id="count" aria-live="polite"></span>
  </div>
</div>

<div class="wrap">""")
for gid, label, h2, intro, slugs in GROUPS:
    w(f'<section class="group" id="{gid}" aria-labelledby="h-{gid}"><h2 id="h-{gid}">{E(h2)}</h2><p class="lead">{E(intro)}</p><ul class="grid">')
    for s in slugs:
        w(card(data[s], gid))
    w("</ul></section>")
w("""<p class="empty" id="empty">No exercises match these filters. <button type="button" onclick="document.getElementById('reset').click()" style="font:inherit;color:var(--red);background:none;border:0;cursor:pointer;text-decoration:underline">Reset filters</button></p>

  <section class="sec" aria-labelledby="start">
    <div class="split">
      <div class="panel">
        <span class="eyebrow">New to lifting?</span>
        <h3 id="start">Start With These 6 Exercises</h3>
        <p style="margin:0;color:var(--muted);font-size:15px">Six Beginner-level exercises that together train your legs, glutes, chest, back, shoulders and arms.</p>
        <ul>""")
for s in STARTERS:
    w(f'<li><a href="{SITE}/exercises/{s}/">{E(data[s]["name"])}</a></li>')
w(f"""</ul>
      </div>
      <div class="panel dark">
        <span class="eyebrow">Inside every guide</span>
        <h3>What Each Exercise Guide Includes</h3>
        <ul>
          <li>GIF demonstration and a short quick answer</li>
          <li>Numbered steps for proper form</li>
          <li>Primary and secondary muscles worked</li>
          <li>Sets, reps and rest for four training goals</li>
          <li>Common mistakes, tips, and easier or harder variations</li>
          <li>Sources for any study we mention</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="sec" aria-labelledby="next">
    <span class="eyebrow">Next step</span>
    <h2 id="next">Turn Exercises Into a Workout</h2>
    <p class="lead">Knowing the exercises is step one. These guides and tools help you put them into a plan that progresses.</p>
    <div class="cards3">
      <div class="ncard"><h3>Structure Your Workout</h3><p>Exercise order, warm-up sets and how long each session should be.</p><a class="btn" href="{SITE}/how-to-structure-a-workout/">Read the guide →</a></div>
      <div class="ncard"><h3>Pick a Workout Split</h3><p>Answer a few questions to find the split that fits your schedule.</p><a class="btn" href="{SITE}/workout-split-finder/">Find your split →</a></div>
      <div class="ncard"><h3>Keep Making Progress</h3><p>How to add weight, reps or sets so your lifts keep going up.</p><a class="btn" href="{SITE}/what-is-progressive-overload/">Learn progressive overload →</a></div>
    </div>
  </section>

  <section class="sec faq" aria-labelledby="faq">
    <h2 id="faq">Exercise Library FAQs</h2>""")
for q, a, link in faqs:
    extra = f' See our guide on <a href="{SITE}{link[1]}">{E(link[0])}</a>.' if link else ""
    w(f"<details><summary>{E(q)}</summary><p>{E(a)}{extra}</p></details>")
w(f"""</section>

  <section class="cta" aria-labelledby="cta">
    <h2 id="cta">Ready to <span>Train Smarter?</span></h2>
    <p>Follow a ready-made workout plan, or use our guides and free tools to build your own.</p>
    <div class="row">
      <!-- /workout-plans/ redirects to the homepage until the plans hub is live; publish it before this button goes live. -->
      <a class="btn" href="{SITE}/workout-plans/">Browse Workout Plans →</a>
      <a class="btn ghost" href="{SITE}/workout-guides/">Workout Guides</a>
      <a class="btn ghost" href="{SITE}/training-volume-calculator/">Training Volume Calculator</a>
    </div>
  </section>
</div>

<script>
(function(){{
  var q=document.getElementById('q'),g=document.getElementById('f-group'),k=document.getElementById('f-kit'),
      l=document.getElementById('f-level'),t=document.getElementById('f-type'),c=document.getElementById('count'),
      cards=[].slice.call(document.querySelectorAll('.ex-card')),groups=[].slice.call(document.querySelectorAll('.group'));
  function run(){{
    var s=q.value.trim().toLowerCase(),n=0;
    cards.forEach(function(el){{
      var ok=(!s||el.dataset.name.indexOf(s)>-1)&&(!g.value||el.dataset.group===g.value)&&(!k.value||el.dataset.kit===k.value)
            &&(!l.value||el.dataset.level===l.value)&&(!t.value||el.dataset.type===t.value);
      el.hidden=!ok; if(ok) n++;
    }});
    groups.forEach(function(sec){{ sec.hidden=!sec.querySelector('.ex-card:not([hidden])'); }});
    c.textContent='Showing '+n+' of '+cards.length+' exercises';
    document.getElementById('empty').style.display=n?'none':'block';
  }}
  [g,k,l,t].forEach(function(x){{x.addEventListener('change',run);}});
  q.addEventListener('input',function(){{run(); if(q.value.length===1) document.getElementById('library').scrollIntoView({{behavior:'smooth'}});}});
  document.getElementById('reset').addEventListener('click',function(){{q.value='';[g,k,l,t].forEach(function(x){{x.value='';}});run();}});
  [].slice.call(document.querySelectorAll('.tile a')).forEach(function(a){{a.addEventListener('click',function(){{document.getElementById('reset').click();}});}});
  run();
}})();
</script>
</body></html>""")

open(out_path, "w", encoding="utf-8").write("".join(H))
print("saved", out_path, total, "exercises")
