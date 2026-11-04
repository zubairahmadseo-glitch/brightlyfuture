"""Build one .docx per exercise for batch 4 (Chest Dip, Front Plank, Hanging Knee Raise)."""
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
ORDER = ["chest-dip", "front-plank", "hanging-knee-raise"]
LIVE = set()
FOCUS = {"chest-dip": "chest dip", "front-plank": "front plank", "hanging-knee-raise": "hanging knee raise"}
LIVE_PAGES = {"barbell-bench-press": "Barbell Bench Press", "dumbbell-bench-press": "Dumbbell Bench Press",
              "barbell-close-grip-bench-press": "Barbell Close-Grip Bench Press",
              "cable-kneeling-crunch": "Cable Kneeling Crunch", "pull-up": "Pull-Up",
              "low-to-high-cable-fly": "Low-to-High Cable Fly"}
ALTERNATIVES = {
    "chest-dip": ["barbell-bench-press", "dumbbell-bench-press", "barbell-close-grip-bench-press"],
    "front-plank": ["cable-kneeling-crunch"],
    "hanging-knee-raise": ["cable-kneeling-crunch"],
}
RELATED = {
    "chest-dip": ["/cable-chest-exercises-10-best-moves/", "/shoulder-pain-bench-press/", "/progressive-overload-for-beginners/"],
    "front-plank": ["/medicine-ball-ab-exercises/", "/how-to-structure-a-workout/", "/how-many-sets-per-muscle-group-per-week/"],
    "hanging-knee-raise": ["/medicine-ball-ab-exercises/", "/progressive-overload-for-beginners/", "/how-many-reps-and-sets-for-muscle-growth/"],
}
PLAN_TITLE = {
    "push-pull-legs": "Push Pull Legs Workout Plan", "full-body-workout-plan": "Full Body Workout Plan for Beginners",
    "bro-split": "Bro Split Workout Plan", "ppl-hypertrophy-program": "6-Day PPL Hypertrophy Program",
    "chest-workout": "Chest Workout", "core-workout": "Core Workout", "5x5-workout": "5x5 Workout",
    "beginner-strength-training-program": "Beginner Strength Training Program",
    "powerlifting-program-for-beginners": "Powerlifting Program for Beginners",
    "5-day-workout-split": "5-Day Workout Split",
}
PLANS = {
    "chest-dip": [("push-pull-legs", "Day 1 — Push A (Heavy), weighted"), ("bro-split", "Day 1 — Chest & Abs"),
        ("ppl-hypertrophy-program", "Day 4 — Push B, weighted"), ("chest-workout", "Chest Workout B — Upper Chest Focus")],
    "front-plank": [("full-body-workout-plan", "Day A — Squat Focus"), ("5x5-workout", "Workout B"),
        ("beginner-strength-training-program", "Day 1 — Squat & Bench (Heavy)"), ("core-workout", "Core Workout at Home")],
    "hanging-knee-raise": [("full-body-workout-plan", "Day C — Deadlift Focus"), ("bro-split", "Day 3 — Shoulders & Traps"),
        ("5-day-workout-split", "Day 2 — Lower (Heavy)"), ("powerlifting-program-for-beginners", "Weeks 1–4"),
        ("core-workout", "Core Workout A (Gym)"), ("push-pull-legs", "Day 6 — Legs B (Volume) — listed there as the straight-leg version")],
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
        ["GIF (upload from Media Library)", gif_hint],
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
        fields(doc, [["Alternatives", "Leave empty for now."]])

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
zpath = os.path.join(HERE, "ExerciseMenu-3-Exercise-Pages-Batch-4.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, "ExerciseMenu-3-Exercise-Pages-Batch-4/" + os.path.basename(f))
print("ok", len(files), "->", zpath)

# ---------------------------------------------------------------- developer file (audit + all 5 pages)
AUDIT = [
    ["Check", "Result"],
    ["GIFs played", "All three animations were pulled from your Media Library and stepped through frame by frame: Chest Dip 30 frames, Hanging raise 30 frames, Front Plank 70 frames, all at 100 ms."],
    ["Name corrected from the GIF", "Your file is called Hanging-Leg-Raise-Hips.gif, but the animation keeps the KNEES BENT and lifts the thighs to about hip height. That is a hanging KNEE raise, so the page is named for what it shows. This is also the better fit for your plans: the knee raise appears in 5 of them, the straight-leg version in 1."],
    ["Form and cues from the frames", "Chest Dip: torso leaning clearly forward, knees bent back, lowering until the upper arms reach about shoulder level. Front Plank: the animation starts with the hips raised and settles into a straight line from head to heels - the flat line is the position the page tells you to hold. Knee Raise: dead hang, overhand grip, thighs to about hip height, controlled return."],
    ["High-authority sources", "ACE Front Plank (exercise library) for the plank cues, hip-height warning and the low-back advice. ACE's triceps article for the dip's shoulder-stability and shoulder-blade cues. ACE's 6 Exercises for a Stronger Core for the hanging-raise caution and the captain's chair progression. Every line quoted was read on the page it came from."],
    ["Claims NOT made", "No EMG numbers for the dip. The forward-lean-versus-upright figures that circulate come from fitness blogs citing studies secondhand, with conflicting values, and the primary papers could not be verified - so the page explains the lean anatomically and leaves the numbers out."],
    ["Honest about the hip flexors", "The knee raise page names the iliopsoas and rectus femoris as PRIMARY movers, because they are. Most pages call this an ab exercise and leave that out. The page then explains how to bring the abs in with a pelvic tilt at the top."],
    ["Plank is a hold, not reps", "The Sets & Reps table gives hold times rather than rep counts, and the page tells readers to end the set when the shape breaks rather than when a timer stops."],
    ["AI voice / patterns", "Banned-word check runs in the build and passes on all three. No sentence of body text is shared between any two pages."],
    ["Related articles", "3 per page, 9 links, all checked live (200) and matched to the topic."],
    ["Workout plan usage", "From your 20 plans: Chest Dip 4 plans, Front Plank 4 plans, Hanging Knee Raise 6 entries across 6 plans. Day labels copied from the plan tables."],
    ["Calories", "2024 Compendium of Physical Activities, 70 kg person, 30-60 s set: 3-6 kcal for the dip, 2-4 for the knee raise, 2-3 for the plank hold."],
    ["Media Library", "All three GIFs are already uploaded, so the developer picks them in the GIF field without uploading anything."],
]
dev = new_doc()
dev.add_heading("ExerciseMenu — Developer File: 3 Exercise Pages (Batch 4)", level=0)
dev.add_paragraph("Headings below are the exact box names on the Edit Exercise screen (plugin v1.2.0). Copy each value into the field with the same name.")
dev.add_heading("Audit", level=1)
grid(dev, AUDIT[0], AUDIT[1:], (120, 380))
dev.add_heading("Order of work", level=1)
for line in ["Create all 3 pages as Drafts first so they appear in each other's 'Alternative Exercises' dropdowns.",
             "Upload each 720 GIF to the Media Library and pick it in 'GIF / Media'.",
             "Fill every box below, then publish and purge LiteSpeed Cache.",
             "Add 'Workout Plans Using This Exercise' entries only after each plan page is live under /workout-plans/."]:
    dev.add_paragraph(line, style="List Number")
for s in ORDER:
    dev.add_page_break()
    build(s, data[s], names, dev)
dpath = os.path.join(HERE, "ExerciseMenu-Developer-File-3-Exercises-Batch-4.docx")
dev.save(dpath)
print("dev ->", dpath)
