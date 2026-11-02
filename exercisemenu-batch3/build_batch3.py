"""Build one .docx per exercise for batch 3 (7 machine/cable/bodyweight exercises), same layout as build_batch2.py."""
import glob
import os
import re
import zipfile

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
SITE = "https://exercisemenu.com"
ORDER = ["cable-triceps-pushdown", "seated-leg-curl", "cable-overhead-triceps-extension", "leg-extension", "pull-up", "reverse-pec-deck-fly", "low-to-high-cable-fly"]
LIVE = set()
FOCUS = {"cable-triceps-pushdown": "triceps pushdown", "leg-extension": "leg extension", "seated-leg-curl": "seated leg curl", "cable-overhead-triceps-extension": "overhead triceps extension",
         "pull-up": "pull-up", "reverse-pec-deck-fly": "reverse pec deck", "low-to-high-cable-fly": "low to high cable fly"}
# Exercise pages already published or written in earlier batches.
LIVE_PAGES = {"barbell-romanian-deadlift": "Barbell Romanian Deadlift", "barbell-deadlift": "Barbell Deadlift",
              "barbell-lying-triceps-extension": "Barbell Lying Triceps Extension",
              "barbell-close-grip-bench-press": "Barbell Close-Grip Bench Press",
              "barbell-bent-over-row": "Barbell Bent-Over Row", "dumbbell-one-arm-row": "Dumbbell One-Arm Row",
              "dumbbell-bench-press": "Dumbbell Bench Press", "barbell-incline-bench-press": "Barbell Incline Bench Press",
              "dumbbell-incline-bench-press": "Dumbbell Incline Bench Press",
              "cable-lat-pulldown": "Cable Lat Pulldown", "seated-cable-row": "Seated Cable Row", "cable-face-pull": "Cable Face Pull",
              "leg-press": "Leg Press", "barbell-back-squat": "Barbell Back Squat", "barbell-bulgarian-split-squat": "Barbell Bulgarian Split Squat"}
ALTERNATIVES = {
    "cable-triceps-pushdown": ["cable-overhead-triceps-extension", "barbell-lying-triceps-extension", "barbell-close-grip-bench-press"],
    "leg-extension": ["leg-press", "barbell-back-squat", "barbell-bulgarian-split-squat"],
    "seated-leg-curl": ["barbell-romanian-deadlift", "barbell-deadlift"],
    "cable-overhead-triceps-extension": ["barbell-lying-triceps-extension", "barbell-close-grip-bench-press"],
    "pull-up": ["cable-lat-pulldown", "seated-cable-row", "barbell-bent-over-row"],
    "reverse-pec-deck-fly": ["cable-face-pull", "seated-cable-row"],
    "low-to-high-cable-fly": ["dumbbell-bench-press", "barbell-incline-bench-press", "dumbbell-incline-bench-press"],
}
RELATED = {
    "cable-triceps-pushdown": ["/how-to-use-a-cable-machine/", "/compound-vs-isolation/", "/how-many-exercises-per-muscle-group-should-you-do/"],
    "leg-extension": ["/compound-vs-isolation/", "/why-your-knees-hurt-when-squatting/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "seated-leg-curl": ["/dumbbell-romanian-deadlift/", "/compound-vs-isolation/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "cable-overhead-triceps-extension": ["/how-to-use-a-cable-machine/", "/how-many-exercises-per-muscle-group-should-you-do/", "/compound-vs-isolation/"],
    "pull-up": ["/progressive-overload-for-beginners/", "/push-pull-legs-split/", "/how-many-sets-per-muscle-group-per-week/"],
    "reverse-pec-deck-fly": ["/cable-shoulder-exercises/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-sets-per-muscle-group-per-week/"],
    "low-to-high-cable-fly": ["/cable-chest-exercises-10-best-moves/", "/how-to-use-a-cable-machine/", "/compound-vs-isolation/"],
}
PLAN_TITLE = {
    "push-pull-legs": "Push Pull Legs Workout Plan", "full-body-workout-plan": "Full Body Workout Plan for Beginners",
    "upper-lower-split": "4-Day Upper Lower Split", "bro-split": "Bro Split Workout Plan", "4-day-workout-split": "4-Day Workout Split",
    "3-day-full-body-workout": "3-Day Full Body Workout", "lean-bulk-workout-plan": "Lean Bulk Workout Plan",
    "hypertrophy-program": "4-Day Hypertrophy Program", "workout-plan-for-skinny-guys": "Workout Plan for Skinny Guys",
    "5-day-workout-split": "5-Day Workout Split", "ppl-hypertrophy-program": "6-Day PPL Hypertrophy Program",
    "beginner-strength-training-program": "Beginner Strength Training Program", "strength-training-for-women": "Strength Training for Women",
    "powerlifting-program-for-beginners": "Powerlifting Program for Beginners", "leg-day-workout": "Leg Day Workout",
    "core-workout": "Core Workout", "arm-workout": "Arm Workout", "chest-workout": "Chest Workout",
}
# (plan slug, day label) — read out of the workout tables of the 20 written plans
PLANS = {
    "cable-triceps-pushdown": [("push-pull-legs", "Day 4 — Push B (Volume)"), ("full-body-workout-plan", "Day B — Bench Press Focus"),
        ("upper-lower-split", "Day 1 — Upper A + Day 3 — Upper B"), ("bro-split", "Day 5 — Arms & Calves"),
        ("4-day-workout-split", "Day 4 — Limbs B (Volume)"), ("3-day-full-body-workout", "Day 2 — Light"),
        ("hypertrophy-program", "Day 4 — Posterior B"), ("workout-plan-for-skinny-guys", "Day 1 — Upper Body"),
        ("5-day-workout-split", "Day 3 — Push (Volume)"), ("ppl-hypertrophy-program", "Day 4 — Push B"),
        ("beginner-strength-training-program", "Day 3 — Squat & Press (Volume)"), ("strength-training-for-women", "Day 3 — Full Body Strength"),
        ("powerlifting-program-for-beginners", "Day 2 — Deadlift & Paused Bench"), ("arm-workout", "Arm Workout B — Isolation Day")],
    "leg-extension": [("push-pull-legs", "Day 3 — Legs A (Heavy) + Day 6 — Legs B (Volume)"), ("upper-lower-split", "Day 2 — Lower A (Squat Focus)"),
        ("bro-split", "Day 4 — Legs"), ("4-day-workout-split", "Day 4 — Limbs B (Volume)"), ("hypertrophy-program", "Day 1 — Anterior A"),
        ("5-day-workout-split", "Day 5 — Legs (Volume)"), ("ppl-hypertrophy-program", "Day 3 — Legs A"), ("leg-day-workout", "Leg Day A — Quad Focus")],
    "seated-leg-curl": [("push-pull-legs", "Day 3 — Legs A (Heavy) + Day 6 — Legs B (Volume)"), ("full-body-workout-plan", "Day A — Squat Focus"),
        ("upper-lower-split", "Day 2 — Lower A + Day 4 — Lower B"), ("bro-split", "Day 4 — Legs"),
        ("4-day-workout-split", "Day 2 — Limbs A (Heavy) + Day 4 — Limbs B (Volume)"), ("3-day-full-body-workout", "Day 2 — Light"),
        ("lean-bulk-workout-plan", "Day 3 — Legs"), ("hypertrophy-program", "Day 2 — Posterior A + Day 4 — Posterior B"),
        ("workout-plan-for-skinny-guys", "Day 2 — Lower Body"), ("5-day-workout-split", "Day 2 — Lower (Heavy) + Day 5 — Legs (Volume)"),
        ("ppl-hypertrophy-program", "Day 3 — Legs A + Day 6 — Legs B"), ("beginner-strength-training-program", "Day 3 — Squat & Press (Volume)"),
        ("strength-training-for-women", "Day 1 — Squat, Glutes & Push"), ("leg-day-workout", "Beginner Leg Day + Leg Day B")],
    "cable-overhead-triceps-extension": [("push-pull-legs", "Day 4 — Push B (Volume)"), ("bro-split", "Day 5 — Arms & Calves"),
        ("4-day-workout-split", "Day 2 — Limbs A (Heavy)"), ("3-day-full-body-workout", "Day 3 — Medium"), ("lean-bulk-workout-plan", "Day 1 — Push"),
        ("hypertrophy-program", "Day 2 — Posterior A"), ("5-day-workout-split", "Day 3 — Push (Volume)"), ("ppl-hypertrophy-program", "Day 1 — Push A"),
        ("arm-workout", "Arm Workout A — Heavy Day")],
    "pull-up": [("push-pull-legs", "Day 2 — Pull A (Heavy), weighted"), ("bro-split", "Day 2 — Back & Rear Delts"),
        ("4-day-workout-split", "Day 3 — Torso B (Volume)"), ("3-day-full-body-workout", "Day 1 — Heavy, weighted"),
        ("hypertrophy-program", "Day 2 — Posterior A"), ("workout-plan-for-skinny-guys", "Day 3 — Full Body"),
        ("5-day-workout-split", "Day 1 — Upper (Heavy), weighted"), ("ppl-hypertrophy-program", "Day 2 — Pull A, weighted")],
    "reverse-pec-deck-fly": [("push-pull-legs", "Day 5 — Pull B (Volume)"), ("bro-split", "Day 3 — Shoulders & Traps"),
        ("hypertrophy-program", "Day 4 — Posterior B"), ("5-day-workout-split", "Day 4 — Pull (Volume)"),
        ("ppl-hypertrophy-program", "Day 2 — Pull A")],
    "low-to-high-cable-fly": [("push-pull-legs", "Day 4 — Push B (Volume)"), ("ppl-hypertrophy-program", "Day 1 — Push A"),
        ("chest-workout", "Chest Workout B — Upper Chest Focus")],
}
BANNED = r"\b(very|really|actually|basically|essentially|incredibly|significantly|straightforward|absolutely|certainly|game changer|dive into)\b"

# ---------------------------------------------------------------- md parsing
def section(t, name):
    m = re.search(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=^## |^---\s*$|^### |\Z)", t, re.S | re.M)
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


def code_lines(block):
    m = re.search(r"```\n(.*?)```", block, re.S)
    return m.group(1).strip() if m else ""


def parse(path):
    t = open(path, encoding="utf-8").read()
    d = {"text": t, "name": re.search(r"^# (.+)", t, re.M).group(1).split(" (")[0].strip()}
    d["head"] = [l[2:] for l in t.split("---")[0].splitlines() if l.startswith("- ")]
    seo = section(t, "SEO & Meta")
    d["title"] = re.search(r"Meta Title \(≤60\):\*\*\s*\n(.+)", seo).group(1).strip()
    d["desc"] = re.search(r"Meta Description \(≤160\):\*\*\s*\n(.+)", seo).group(1).strip()
    d["basics"] = dict((r[0], r[1]) for r in md_table(section(t, "Exercise Basics"))[1:])
    d["alt"] = re.search(r"GIF Alt Text:\*\*\s*(.+)", t).group(1).strip()
    d["qa"] = section(t, "Quick Answer (AEO)")
    mw = section(t, "Muscles Worked").split("**Secondary Muscles")
    d["primary"], d["secondary"] = code_lines(mw[0]), code_lines(mw[1])
    d["steps"] = md_table(section(t, "How-To Steps"))[1:]
    d["sets"] = md_table(section(t, "Sets & Reps Table"))[1:]
    d["mistakes"] = re.findall(r"^\d+\. \*\*(.+?)\*\* (.+)$", section(t, "Common Mistakes"), re.M)
    d["tips"] = re.findall(r"^\d+\. \*\*(.+?)\*\* (.+)$", section(t, "Tips"), re.M)
    d["mods"] = md_table(section(t, "Modifications (Easier/Harder)"))[1:]
    d["faqs"] = re.findall(r"\*\*Q: (.+?)\*\*\s*\n\s*A: (.+)", section(t, "FAQs"))
    d["cites"] = []
    for c in re.findall(r"\*\*Citation[^*]*\*\*\s*(.+)", t):
        url = re.search(r"https?://\S+", c).group(0)
        d["cites"].append((c.replace(url, "").replace("*", "").strip(), url))
    return d


def check(slug, d):
    problems = []
    if len(d["title"]) > 60: problems.append(f"meta title {len(d['title'])}")
    if len(d["desc"]) > 160: problems.append(f"meta description {len(d['desc'])}")
    if len(d["qa"]) >= 320 or len(d["qa"].split()) >= 60: problems.append("quick answer too long")
    if len(d["steps"]) < 4 or any(not s[2] for s in d["steps"]): problems.append("steps incomplete")
    if len(d["mistakes"]) < 4 or len(d["tips"]) < 4 or len(d["mods"]) < 4 or len(d["faqs"]) < 5: problems.append("section count")
    if len(d["sets"]) != 4: problems.append("sets table")
    body = d["text"].split("### Internal")[0]
    if re.search(BANNED, body, re.I): problems.append("banned word: " + re.search(BANNED, body, re.I).group(0))
    for a in ALTERNATIVES[slug]:
        if a not in ORDER and a not in LIVE_PAGES: problems.append("unknown alternative " + a)
    assert not problems, (slug, problems)


# ---------------------------------------------------------------- docx
def shade(cell, hex_color):
    pr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hex_color)
    pr.append(sh)


def new_doc():
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
    for sec in doc.sections:
        sec.left_margin = sec.right_margin = Pt(54); sec.top_margin = sec.bottom_margin = Pt(50)
    return doc


def box(doc, title, note=None):
    doc.add_heading(title, level=2)
    if note:
        p = doc.add_paragraph(); r = p.add_run(note); r.italic = True; r.font.color.rgb = RGBColor(0x6b, 0x68, 0x60)


def fields(doc, rows, widths=(150, 350)):
    t = doc.add_table(rows=0, cols=len(rows[0])); t.style = "Table Grid"; t.autofit = False
    for i, row in enumerate(rows):
        cells = t.add_row().cells
        for j, val in enumerate(row):
            cells[j].text = str(val)
            cells[j].width = Pt(widths[j])
            if j == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], "F0EFED")
    doc.add_paragraph()


def grid(doc, header, rows, widths):
    t = doc.add_table(rows=0, cols=len(header)); t.style = "Table Grid"; t.autofit = False
    for i, row in enumerate([header] + rows):
        cells = t.add_row().cells
        for j, val in enumerate(row):
            cells[j].text = str(val); cells[j].width = Pt(widths[j])
            if i == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], "D9E2F3")
    doc.add_paragraph()


def norm(s):
    return re.sub(r"[^a-z]", "", s.lower())


def build(slug, d, names, doc=None):
    doc = doc or new_doc()
    doc.add_heading(d["name"], level=0)
    status = "LIVE PAGE — replace every field with the content below." if slug in LIVE else "NEW PAGE — add as a new Exercise (save as Draft, check, then Publish)."
    p = doc.add_paragraph(); r = p.add_run(status); r.bold = True
    for line in d["head"]:
        if line.startswith("**Status"): continue
        doc.add_paragraph(re.sub(r"[`*]", "", line), style="List Bullet")
    doc.add_paragraph("Each heading below is the name of a box on the Edit Exercise screen. Copy each value into the field with the same name.")

    box(doc, "Title (top of the edit screen)")
    fields(doc, [["Title", d["name"]], ["Permalink / Slug", slug]])

    box(doc, "Rank Math SEO", "Fill these in the Rank Math box (not the 'SEO & Meta (Legacy)' box, which no longer shows on the page).")
    fields(doc, [[f"Title ({len(d['title'])}/60)", d["title"]], [f"Description ({len(d['desc'])}/155)", d["desc"]], ["Focus Keyword", FOCUS[slug]]])

    b = d["basics"]
    box(doc, "Exercise Basics")
    fields(doc, [
        ["Subtitle (one line description)", b["Subtitle"]],
        ["Tags (comma-separated: Beginner, Isolation, Dumbbells…)", b["Tags"]],
        ["Target Muscle (sidebar display)", b["Target Muscle (sidebar)"]],
        ["Body Part", b["Body Part"]],
        ["Equipment", b["Equipment"]],
        ["Category (Isolation / Compound)", b["Category"]],
        ["Skill Level", b["Skill Level"]],
        ["Movement Pattern (e.g. Elbow Flexion)", b["Movement Pattern"]],
        ["Also Known As", b["Also Known As"]],
        ["Estimated Calories per set (e.g. 3–5 kcal)", b["Approx. Calories per set"]],
    ], widths=(190, 310))

    box(doc, "GIF / Media")
    gif_line = next((h for h in d["head"] if "GIF" in h and "Alt" not in h), "")
    gif_hint = re.sub(r"[`*]", "", gif_line.split(":", 1)[1]).strip() if ":" in gif_line else ""
    fields(doc, [
        ["GIF (upload from Media Library)", gif_hint if slug not in LIVE else "Optional: pick the same GIF from the Media Library (keeps width/height for page speed)"],
        ["Legacy GIF URL (fallback if no Media Library file is selected)", "Leave as it is" if slug in LIVE else "Leave empty"],
        ["GIF Alt Text", d["alt"]],
    ], widths=(190, 310))

    box(doc, "Quick Answer (AEO)")
    fields(doc, [[f"Quick Answer Text ({len(d['qa'])}/320 · {len(d['qa'].split())} words)", d["qa"]]], widths=(150, 350))

    box(doc, "Muscles Worked")
    fields(doc, [["Primary Muscles (one per line)", d["primary"]], ["Secondary Muscles (one per line)", d["secondary"]]])

    box(doc, "Muscle Map Image (optional)")
    fields(doc, [["Muscle Map Image", "Leave empty (no muscle map image purchased)."]])

    box(doc, "How-To Steps")
    rows = []
    for n, ti, de in d["steps"]:
        rows += [[f"Step {n} Title", ti], [f"Step {n} Description", de]]
    fields(doc, rows)
    if slug in LIVE:
        doc.add_paragraph("Remove any extra old steps so only these remain.")

    box(doc, "Sets & Reps Table")
    grid(doc, ["Goal", "Sets", "Reps", "Rest"], d["sets"], (140, 110, 120, 130))

    box(doc, "Common Mistakes", "Type the title, a colon, then the description — the page shows the part before the colon as a heading.")
    fields(doc, [[f"Mistake {i}", f"{a} {b_}"] for i, (a, b_) in enumerate(d["mistakes"], 1)], widths=(80, 420))

    box(doc, "Tips", "Same format as Common Mistakes.")
    fields(doc, [[f"Tip {i}", f"{a} {b_}"] for i, (a, b_) in enumerate(d["tips"], 1)], widths=(80, 420))

    box(doc, "Modifications (Easier/Harder)")
    rows = []
    for ty, ti, de in d["mods"]:
        link = names.get(norm(ti), "")
        rows.append(["Easier" if "Easier" in ty else "Harder", ti, de, f"{link} (select once published)" if link else "— None —"])
    grid(doc, ["Type", "Title (e.g. Cable Bicep Curl)", "Description", "Link to exercise page (optional)"], rows, (55, 120, 220, 105))

    box(doc, "Alternative Exercises", "Pick these in the dropdowns. A page only appears in the dropdown after it has been created (draft is fine); it shows on the site once published.")
    if ALTERNATIVES[slug]:
        fields(doc, [[f"Alternative {i}", names_by_slug[a] + ("" if a in LIVE_PAGES else " (this batch — create it first)")] for i, a in enumerate(ALTERNATIVES[slug], 1)])
    else:
        fields(doc, [["Alternatives", "Leave empty for now — no matching page is published yet."]])

    box(doc, "Sources (Citations)")
    if d["cites"]:
        rows = []
        for i, (txt, url) in enumerate(d["cites"], 1):
            rows += [[f"Source {i} — Citation Text", txt], [f"Source {i} — URL", url]]
        fields(doc, rows)
    else:
        fields(doc, [["Sources", "Leave empty — this page does not cite a study."]])

    box(doc, "FAQs")
    rows = []
    for i, (q, a) in enumerate(d["faqs"], 1):
        rows += [[f"Question {i}", q], [f"Answer {i}", a]]
    fields(doc, rows)
    if slug in LIVE:
        doc.add_paragraph("Remove any extra old FAQs so only these remain.")

    box(doc, "Workout Plans Using This Exercise", "Add each plan only after its page is published under /workout-plans/.")
    rows = []
    for i, (p, day) in enumerate(PLANS[slug], 1):
        rows += [[f"Plan {i} (search posts/pages)", f"{PLAN_TITLE[p]}  — /workout-plans/{p}/"], [f"Plan {i} Day Label", day]]
    fields(doc, rows)

    box(doc, "Related Articles (right-hand sidebar box)", "Search and pick each article. Leave the manual Title/URL boxes empty.")
    fields(doc, [[f"Article {i}", SITE + u] for i, u in enumerate(RELATED[slug], 1)])

    return doc


# ---------------------------------------------------------------- main
os.makedirs(OUT, exist_ok=True)
data = {s: parse(os.path.join(HERE, s + ".md")) for s in ORDER}
names_by_slug = dict(LIVE_PAGES, **{s: data[s]["name"] for s in ORDER})
names = {norm(v): v for v in names_by_slug.values()}
files = []
for i, s in enumerate(ORDER, 1):
    check(s, data[s])
    path = os.path.join(OUT, f"{i:02d}-{s}.docx")
    build(s, data[s], names).save(path)
    files.append(path)
zpath = os.path.join(HERE, "ExerciseMenu-7-Exercise-Pages-Batch-3.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, "ExerciseMenu-7-Exercise-Pages-Batch-3/" + os.path.basename(f))
print("ok", len(files), "->", zpath)

# ---------------------------------------------------------------- developer file (audit + all 5 pages)
AUDIT = [
    ["Check", "Result"],
    ["Exercise names", "Every GIF was zoomed in on before anything was written and the name taken from what the image shows: Cable Triceps Pushdown (rope), Seated Leg Curl, Cable Overhead Triceps Extension (rope), Leg Extension, Pull-Up, Reverse Pec Deck Fly, Low-to-High Cable Fly."],
    ["Form, cues and positioning vs GIF", "Steps written from the frames. Pushdown: high pulley, rope, elbows pinned at the sides, hands starting at upper-stomach height. Leg curl: roller just above the heels, thigh pad above the knees. Overhead extension: LOW pulley with the back to the stack, elbows pointing forward. Leg extension: roller across the front of the lower legs just above the feet, knees bent about 90 degrees at the start, hands on the side handles. Pull-Up: overhand grip a little wider than the shoulders, ankles crossed. Reverse pec deck: palms-down grip on the horizontal handles, chest on the pad. Cable fly: two LOW pulleys, staggered stance, trunk upright."],
    ["Verified research", "7 sources, each abstract opened and read: Maeo 2021 (seated vs lying leg curl, 14% vs 9%), Maeo 2023 (overhead vs neutral triceps, 28.5% vs 19.6% long head at 34-39% less load), Youdas 2010 (pull-up vs chin-up EMG), Schoenfeld 2013 (neutral vs pronated grip on the reverse fly machine), Pedrosa 2022 (knee extension ROM, 100-65 degrees grew more than full range in several muscle regions), Smith 2009 (20-study review: VMO cannot be preferentially activated), Rendos 2016 (handle type does not change triceps EMG in the pushdown). ACE's Standing Incline Cable Flyes page was fetched for the cable fly cues."],
    ["Claims NOT made", "No 'rope beats bar' claim on the pushdown: the only head-to-head data found no triceps difference, and the page says so. No upper-chest EMG claim for the low-to-high fly: no study has measured that exercise. No 'turning your toes shapes the inner quad' claim on the leg extension - the page states the opposite, with the review behind it. No 'leg extensions wreck your knees' claim either way."],
    ["Honest caveats on the page", "Low-to-High Cable Fly, Tip 3 and FAQ 1 both say the upper-chest rationale is anatomical, not measured. Reverse Pec Deck notes the neutral-grip finding came from a machine with vertical handles, while the GIF shows palms-down handles. Leg Extension FAQ 1 tells anyone with knee pain to see a clinician rather than giving medical advice."],
    ["AI voice / patterns", "Banned-word check runs in the build (very, really, basically, significantly, game changer, dive into and others) and passes on all 7 pages. FAQ openers varied; no repeated sentence shapes across pages."],
    ["Related articles", "3 per page, all live on exercisemenu.com (checked, all return 200) and all topically matched - cable chest article for the cable fly, Romanian deadlift for the leg curl, knee-pain article for the leg extension, cable machine guide for both triceps pages."],
    ["Anything irrelevant?", "Teres major was dropped from the Reverse Pec Deck muscle list: it is not a horizontal abductor. No rower or lateral raise is listed as a rear-delt alternative."],
    ["Workout plan usage", "Read out of the tables of your 20 written plans: Seated Leg Curl 14 plans, Cable Triceps Pushdown 14, Cable Overhead Triceps Extension 9, Pull-Up 8, Leg Extension 8, Reverse Pec Deck 5, Low-to-High Cable Fly 3."],
    ["Calories", "Estimates from the 2024 Compendium of Physical Activities, 70 kg person, 30-60 s set. 3-6 kcal for the pull-up (bodyweight compound), 2-4 kcal for the rest."],
    ["Not checked", "Only still frames were reviewed, since the files supplied are single-frame images rather than animations. Play each purchased GIF once before publishing to confirm the movement matches the steps."],
]
dev = new_doc()
dev.add_heading("ExerciseMenu — Developer File: 7 Exercise Pages (Batch 3)", level=0)
dev.add_paragraph("Headings below are the exact box names on the Edit Exercise screen (plugin v1.2.0). Copy each value into the field with the same name.")
dev.add_heading("Audit", level=1)
grid(dev, AUDIT[0], AUDIT[1:], (120, 380))
dev.add_heading("Order of work", level=1)
for line in ["Create all 5 pages as Drafts first so they appear in each other's 'Alternative Exercises' dropdowns.",
             "Upload each 720 GIF to the Media Library and pick it in 'GIF / Media'.",
             "Fill every box below, then publish and purge LiteSpeed Cache.",
             "Add 'Workout Plans Using This Exercise' entries only after each plan page is live under /workout-plans/."]:
    dev.add_paragraph(line, style="List Number")
for s in ORDER:
    dev.add_page_break()
    build(s, data[s], names, dev)
dpath = os.path.join(HERE, "ExerciseMenu-Developer-File-7-Exercises-Batch-3.docx")
dev.save(dpath)
print("dev ->", dpath)
