"""Build one .docx per exercise for batch 2 (5 cable/machine exercises), same layout as build_final.py."""
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
ORDER = ["cable-kneeling-crunch", "cable-face-pull", "cable-lat-pulldown", "seated-cable-row", "leg-press"]
LIVE = set()
FOCUS = {"cable-kneeling-crunch": "cable crunch", "cable-face-pull": "face pull", "cable-lat-pulldown": "lat pulldown",
         "seated-cable-row": "seated cable row", "leg-press": "leg press"}
# Live exercise pages (published) and the other pages in this batch.
LIVE_PAGES = {"barbell-bent-over-row": "Barbell Bent-Over Row", "dumbbell-one-arm-row": "Dumbbell One-Arm Row",
              "barbell-back-squat": "Barbell Back Squat", "barbell-bulgarian-split-squat": "Barbell Bulgarian Split Squat",
              "dumbbell-lunge": "Dumbbell Lunge", "dumbbell-lateral-raise": "Dumbbell Lateral Raise"}
ALTERNATIVES = {
    "cable-kneeling-crunch": [],
    "cable-face-pull": [],
    "cable-lat-pulldown": ["seated-cable-row", "dumbbell-one-arm-row", "barbell-bent-over-row"],
    "seated-cable-row": ["barbell-bent-over-row", "dumbbell-one-arm-row", "cable-lat-pulldown"],
    "leg-press": ["barbell-back-squat", "barbell-bulgarian-split-squat", "dumbbell-lunge"],
}
RELATED = {
    "cable-kneeling-crunch": ["/medicine-ball-ab-exercises/", "/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/"],
    "cable-face-pull": ["/cable-shoulder-exercises/", "/cable-back-exercises/", "/push-pull-legs-split/"],
    "cable-lat-pulldown": ["/cable-back-exercises/", "/how-to-use-a-cable-machine/", "/push-pull-legs-split/"],
    "seated-cable-row": ["/cable-back-exercises/", "/how-to-use-a-cable-machine/", "/how-many-sets-per-muscle-group-per-week/"],
    "leg-press": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/how-to-structure-a-workout/"],
}
PLAN_TITLE = {
    "push-pull-legs": "Push Pull Legs Workout Plan", "full-body-workout-plan": "Full Body Workout Plan for Beginners",
    "upper-lower-split": "4-Day Upper Lower Split", "bro-split": "Bro Split Workout Plan", "4-day-workout-split": "4-Day Workout Split",
    "3-day-full-body-workout": "3-Day Full Body Workout", "lean-bulk-workout-plan": "Lean Bulk Workout Plan",
    "hypertrophy-program": "4-Day Hypertrophy Program", "workout-plan-for-skinny-guys": "Workout Plan for Skinny Guys",
    "5-day-workout-split": "5-Day Workout Split", "ppl-hypertrophy-program": "6-Day PPL Hypertrophy Program",
    "beginner-strength-training-program": "Beginner Strength Training Program", "strength-training-for-women": "Strength Training for Women",
    "powerlifting-program-for-beginners": "Powerlifting Program for Beginners", "leg-day-workout": "Leg Day Workout", "core-workout": "Core Workout",
}
# (plan slug, day label) — taken from the workout tables of the 20 written plans
PLANS = {
    "cable-kneeling-crunch": [("full-body-workout-plan", "Day B"), ("bro-split", "Day 1 — Chest & Abs"), ("lean-bulk-workout-plan", "Day 3 — Legs"),
        ("hypertrophy-program", "Day 3 — Anterior B"), ("workout-plan-for-skinny-guys", "Day 2 — Lower Body"), ("ppl-hypertrophy-program", "Day 3 — Legs A"),
        ("core-workout", "Core Workout A (Gym)")],
    "cable-face-pull": [("push-pull-legs", "Pull A + Pull B"), ("full-body-workout-plan", "Day C"), ("upper-lower-split", "Upper A + Upper B"),
        ("bro-split", "Day 2 — Back & Rear Delts"), ("4-day-workout-split", "Day 3 — Torso B"), ("lean-bulk-workout-plan", "Day 2 — Pull"),
        ("5-day-workout-split", "Day 1 — Upper"), ("ppl-hypertrophy-program", "Day 5 — Pull B"), ("powerlifting-program-for-beginners", "Day 3")],
    "cable-lat-pulldown": [("push-pull-legs", "Pull B (wide grip)"), ("full-body-workout-plan", "Day A"), ("upper-lower-split", "Upper A + Upper B"),
        ("4-day-workout-split", "Day 1 — Torso A"), ("lean-bulk-workout-plan", "Day 2 — Pull"), ("workout-plan-for-skinny-guys", "Day 1 — Upper Body"),
        ("5-day-workout-split", "Day 4 — Pull"), ("beginner-strength-training-program", "Day 1"), ("strength-training-for-women", "Day 2"),
        ("powerlifting-program-for-beginners", "Day 2")],
    "seated-cable-row": [("push-pull-legs", "Pull A + Pull B"), ("full-body-workout-plan", "Day C"), ("4-day-workout-split", "Day 3 — Torso B"),
        ("3-day-full-body-workout", "Day 2 — Light"), ("lean-bulk-workout-plan", "Day 2 — Pull"), ("workout-plan-for-skinny-guys", "Day 1 — Upper Body"),
        ("strength-training-for-women", "Day 2")],
    "leg-press": [("push-pull-legs", "Legs B"), ("full-body-workout-plan", "Day B"), ("upper-lower-split", "Lower A + Lower B"), ("bro-split", "Day 4 — Legs"),
        ("4-day-workout-split", "Day 4 — Limbs B"), ("3-day-full-body-workout", "Day 2 — Light"), ("lean-bulk-workout-plan", "Day 3 — Legs"),
        ("hypertrophy-program", "Day 3 — Anterior B"), ("workout-plan-for-skinny-guys", "Day 2 — Lower Body"), ("5-day-workout-split", "Day 2 + Day 5"),
        ("strength-training-for-women", "Day 3"), ("powerlifting-program-for-beginners", "Day 1"), ("leg-day-workout", "Beginner + Leg Day A")],
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
        later = {"cable-kneeling-crunch": "Hanging Knee Raise or Reverse Crunch", "cable-face-pull": "Reverse Pec Deck (rear delt fly machine)"}[slug]
        fields(doc, [["Alternatives", f"Leave empty for now — no matching page is published yet. Add {later} when that page goes live."]])

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
zpath = os.path.join(HERE, "ExerciseMenu-5-Cable-Machine-Exercise-Pages.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, "ExerciseMenu-5-Exercise-Pages/" + os.path.basename(f))
print("ok", len(files), "->", zpath)

# ---------------------------------------------------------------- developer file (audit + all 5 pages)
AUDIT = [
    ["Check", "Result"],
    ["Exercise names", "Matched to each GIF and to the names used in your 20 plans: Cable Kneeling Crunch, Cable Face Pull, Cable Lat Pulldown, Seated Cable Row (V-bar), Leg Press (45-degree sled)."],
    ["Form and cues vs GIF", "Each image was zoomed and the steps written to match it: crunch kneeling with the back to the machine; face pull at shoulder height with the rope ends separating; wide-grip pulldown to the upper chest; V-bar row starting with a forward reach; 45-degree sled with safety handles."],
    ["Verified research", "4 sources, each opened and checked: Andersen 2014 (lat pulldown grip width), Martín-Fuentes 2020 review (leg press foot position), Vispute 2011 (ab exercise and belly fat), ACE seated row instructions."],
    ["Claims removed or corrected", "V-bar 'allows more weight' (study used overhand grips, not a V-bar); 'wide bar works upper back more' (not proven); 'pushing through toes stresses knees' (not proven); 'face pull works more upper back than reverse fly' (changed to outward rotation only); ACE source now named as the machine row it is; unverified page numbers removed from a citation."],
    ["Honest caveats on the page", "Leg press foot position: research is mixed, so the page recommends a self-selected stance. Seated row start: the GIF reaches forward; the page says staying upright is also used."],
    ["AI voice / patterns", "Banned words checked automatically; repeated FAQ openers ('Usually because…') varied; plain, direct sentences."],
    ["Related articles", "All 9 links return 200 and were opened: cable shoulder/back and cable machine articles mention these exercises. 'Types of Squats' was removed from Leg Press because it does not mention the leg press."],
    ["Anything irrelevant?", "Dumbbell Lateral Raise removed as a Face Pull alternative (it trains the side delts, not the rear delts)."],
    ["Calories", "Estimates from the 2024 Compendium of Physical Activities (3.5 MET), 70 kg person, 30–60 s set."],
    ["Not checked", "Only still frames of the GIFs were reviewed. Play each GIF once before publishing to confirm the movement matches the steps."],
]
dev = new_doc()
dev.add_heading("ExerciseMenu — Developer File: 5 Exercise Pages", level=0)
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
dpath = os.path.join(HERE, "ExerciseMenu-Developer-File-5-Exercises.docx")
dev.save(dpath)
print("dev ->", dpath)
