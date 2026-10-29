"""Build one .docx per exercise, laid out box-by-box like the Exercise plugin (v1.2.0) admin screen.

Usage: python3 build_final.py  ->  out/NN-<slug>.docx + out/00-READ-ME-FIRST.docx, zipped.
"""
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

# Order: live pages first (fixes), then new pages.
ORDER = [
    "barbell-bench-press", "barbell-incline-bench-press", "dumbbell-bench-press", "barbell-lying-triceps-extension",
    "barbell-curl", "dumbbell-biceps-curl", "dumbbell-hammer-curl", "barbell-standing-calf-raise",
    "barbell-deadlift", "barbell-back-squat", "barbell-romanian-deadlift", "barbell-bent-over-row",
    "barbell-overhead-press", "barbell-hip-thrust", "barbell-bulgarian-split-squat", "barbell-close-grip-bench-press",
    "dumbbell-incline-bench-press", "dumbbell-seated-shoulder-press", "dumbbell-lateral-raise", "dumbbell-one-arm-row",
    "dumbbell-lunge", "ez-bar-curl", "barbell-preacher-curl", "barbell-seated-calf-raise",
]
LIVE = set(ORDER[:8])

FOCUS = {s: s.replace("-", " ") for s in ORDER}
FOCUS.update({"ez-bar-curl": "ez bar curl", "dumbbell-one-arm-row": "one arm dumbbell row",
              "dumbbell-incline-bench-press": "incline dumbbell press", "dumbbell-seated-shoulder-press": "seated dumbbell shoulder press",
              "barbell-close-grip-bench-press": "close grip bench press", "barbell-romanian-deadlift": "romanian deadlift",
              "barbell-overhead-press": "barbell overhead press", "barbell-lying-triceps-extension": "barbell lying triceps extension"})

ALTERNATIVES = {
    "barbell-bench-press": ["dumbbell-bench-press", "barbell-incline-bench-press", "barbell-close-grip-bench-press"],
    "barbell-incline-bench-press": ["dumbbell-incline-bench-press", "barbell-bench-press"],
    "dumbbell-bench-press": ["barbell-bench-press", "dumbbell-incline-bench-press"],
    "barbell-lying-triceps-extension": ["barbell-close-grip-bench-press"],
    "barbell-curl": ["ez-bar-curl", "dumbbell-biceps-curl", "barbell-preacher-curl"],
    "dumbbell-biceps-curl": ["barbell-curl", "ez-bar-curl", "dumbbell-hammer-curl"],
    "dumbbell-hammer-curl": ["dumbbell-biceps-curl", "ez-bar-curl"],
    "barbell-standing-calf-raise": ["barbell-seated-calf-raise"],
    "barbell-deadlift": ["barbell-romanian-deadlift", "barbell-hip-thrust", "barbell-back-squat"],
    "barbell-back-squat": ["barbell-bulgarian-split-squat", "dumbbell-lunge"],
    "barbell-romanian-deadlift": ["barbell-deadlift", "barbell-hip-thrust"],
    "barbell-bent-over-row": ["dumbbell-one-arm-row"],
    "barbell-overhead-press": ["dumbbell-seated-shoulder-press"],
    "barbell-hip-thrust": ["barbell-romanian-deadlift", "barbell-back-squat", "barbell-bulgarian-split-squat"],
    "barbell-bulgarian-split-squat": ["dumbbell-lunge", "barbell-back-squat"],
    "barbell-close-grip-bench-press": ["barbell-bench-press", "barbell-lying-triceps-extension"],
    "dumbbell-incline-bench-press": ["barbell-incline-bench-press", "dumbbell-bench-press"],
    "dumbbell-seated-shoulder-press": ["barbell-overhead-press"],
    "dumbbell-lateral-raise": ["dumbbell-seated-shoulder-press", "barbell-overhead-press"],
    "dumbbell-one-arm-row": ["barbell-bent-over-row"],
    "dumbbell-lunge": ["barbell-bulgarian-split-squat", "barbell-back-squat"],
    "ez-bar-curl": ["barbell-curl", "dumbbell-biceps-curl", "barbell-preacher-curl"],
    "barbell-preacher-curl": ["ez-bar-curl", "barbell-curl", "dumbbell-biceps-curl"],
    "barbell-seated-calf-raise": ["barbell-standing-calf-raise"],
}

RELATED = {
    "barbell-bench-press": ["/how-to-bench-press/", "/bench-press-grip-width/", "/average-bench-press-by-age-weight-and-sex/"],
    "barbell-incline-bench-press": ["/how-to-bench-press/", "/bench-press-grip-width/", "/shoulder-pain-bench-press/"],
    "dumbbell-bench-press": ["/cable-chest-exercises-10-best-moves/", "/how-to-bench-press/", "/push-pull-legs-split/"],
    "barbell-lying-triceps-extension": ["/how-many-reps-and-sets-for-muscle-growth/", "/push-pull-legs-split/", "/what-is-progressive-overload/"],
    "barbell-curl": ["/ez-curl-bar-weight/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "dumbbell-biceps-curl": ["/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-reps-and-sets-for-muscle-growth/", "/eccentric-vs-concentric/"],
    "dumbbell-hammer-curl": ["/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/"],
    "barbell-standing-calf-raise": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/progressive-overload-for-beginners/"],
    "barbell-deadlift": ["/how-to-deadlift-for-beginners/", "/sumo-vs-conventional-deadlift/", "/is-your-deadlift-good-average-weights-by-level-age/"],
    "barbell-back-squat": ["/types-of-squats/", "/high-bar-vs-low-bar-squat/", "/why-your-knees-hurt-when-squatting/"],
    "barbell-romanian-deadlift": ["/dumbbell-romanian-deadlift/", "/how-to-deadlift-for-beginners/", "/sumo-vs-conventional-deadlift/"],
    "barbell-bent-over-row": ["/cable-back-exercises/", "/push-pull-legs-split/", "/how-many-sets-per-muscle-group-per-week/"],
    "barbell-overhead-press": ["/cable-shoulder-exercises/", "/how-much-does-a-barbell-weigh/", "/push-pull-legs-split/"],
    "barbell-hip-thrust": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/reps-and-sets-for-woman/"],
    "barbell-bulgarian-split-squat": ["/types-of-squats/", "/why-your-knees-hurt-when-squatting/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "barbell-close-grip-bench-press": ["/how-to-bench-press/", "/bench-press-grip-width/", "/shoulder-pain-bench-press/"],
    "dumbbell-incline-bench-press": ["/cable-chest-exercises-10-best-moves/", "/shoulder-pain-bench-press/", "/push-pull-legs-split/"],
    "dumbbell-seated-shoulder-press": ["/cable-shoulder-exercises/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/push-pull-legs-split/"],
    "dumbbell-lateral-raise": ["/cable-shoulder-exercises/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-sets-per-muscle-group-per-week/"],
    "dumbbell-one-arm-row": ["/cable-back-exercises/", "/push-pull-legs-split/", "/how-many-exercises-per-muscle-group-should-you-do/"],
    "dumbbell-lunge": ["/what-is-progressive-overload/", "/how-many-reps-and-sets-for-muscle-growth/", "/how-to-structure-a-workout/"],
    "ez-bar-curl": ["/ez-curl-bar-weight/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "barbell-preacher-curl": ["/ez-curl-bar-weight/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/eccentric-vs-concentric/"],
    "barbell-seated-calf-raise": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/time-under-tension/"],
}

# Where each exercise is used in the written Push Pull Legs plan (the only plan with full content so far).
PPL_DAY = {
    "barbell-bench-press": "Push A", "barbell-overhead-press": "Push A", "barbell-close-grip-bench-press": "Push A",
    "dumbbell-incline-bench-press": "Push A + Push B", "dumbbell-lateral-raise": "Push A + Push B",
    "dumbbell-bench-press": "Push B", "dumbbell-seated-shoulder-press": "Push B",
    "barbell-deadlift": "Pull A", "barbell-bent-over-row": "Pull A", "barbell-curl": "Pull A",
    "dumbbell-one-arm-row": "Pull B", "dumbbell-biceps-curl": "Pull B",
    "barbell-back-squat": "Legs A", "barbell-romanian-deadlift": "Legs A", "barbell-bulgarian-split-squat": "Legs A",
    "barbell-standing-calf-raise": "Legs A", "barbell-hip-thrust": "Legs B", "barbell-seated-calf-raise": "Legs B",
    "dumbbell-lunge": "Legs B (the plan says 'Walking Lunges' — rename it to 'Dumbbell Lunge' in the plan, or buy a walking-lunge GIF)",
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
        if a not in ORDER: problems.append("unknown alternative " + a)
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


def build(slug, d, names):
    doc = new_doc()
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
    fields(doc, [[f"Alternative {i}", names_by_slug[a]] for i, a in enumerate(ALTERNATIVES[slug], 1)])

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

    box(doc, "Workout Plans Using This Exercise", "Add only plan pages that are published. The Push Pull Legs plan is not live yet.")
    if slug in PPL_DAY:
        fields(doc, [["Workout Plan (search posts/pages)", "Push Pull Legs Workout Plan — add when the plan page is published"], ["Day Label", PPL_DAY[slug]]])
    else:
        fields(doc, [["Workout Plan", "Leave empty for now — not used in the Push Pull Legs plan. Add other plans when they are published."]])
    if slug == "barbell-lying-triceps-extension":
        doc.add_paragraph("Remove '/push-pull-legs-split/' from this box — it is an article, not a workout plan.")

    box(doc, "Related Articles (right-hand sidebar box)", "Search and pick each article. Leave the manual Title/URL boxes empty.")
    fields(doc, [[f"Article {i}", SITE + u] for i, u in enumerate(RELATED[slug], 1)])

    return doc


# ---------------------------------------------------------------- main
os.makedirs(OUT, exist_ok=True)
data = {s: parse(os.path.join(HERE, s + ".md")) for s in ORDER}
names_by_slug = {s: data[s]["name"] for s in ORDER}
names = {norm(v): v for v in names_by_slug.values()}
names[norm("Close-Grip Bench Press")] = names_by_slug["barbell-close-grip-bench-press"]
names[norm("Dumbbell Incline Bench Press")] = names_by_slug["dumbbell-incline-bench-press"]
names[norm("EZ Bar Curl")] = names_by_slug["ez-bar-curl"]

files = []
for i, s in enumerate(ORDER, 1):
    check(s, data[s])
    path = os.path.join(OUT, f"{i:02d}-{s}.docx")
    build(s, data[s], names).save(path)
    files.append(path)

# Read-me
doc = new_doc()
doc.add_heading("ExerciseMenu — 24 Exercise Pages (Plugin v1.2.0)", level=0)
doc.add_paragraph("One file per exercise. Every heading inside a file is the exact name of a box on the Edit Exercise screen.")
grid(doc, ["#", "Exercise", "Status", "What to do"], [
    [f"{i:02d}", names_by_slug[s], "LIVE" if s in LIVE else "NEW",
     "Replace all fields (corrected content)" if s in LIVE else "Create new Exercise, fill fields, publish"]
    for i, s in enumerate(ORDER, 1)], (30, 200, 50, 220))
doc.add_heading("Order of work", level=2)
for line in [
    "Create all 16 NEW pages as Drafts first, so they appear in the 'Alternative Exercises' and 'Link to exercise page' dropdowns.",
    "Then fill the dropdowns on every page and publish.",
    "Barbell Standing Calf Raise: change the slug from 992896 to barbell-standing-calf-raise and add a 301 redirect in Rank Math → Redirections.",
    "Upload the _720.gif version of each new GIF to the Media Library and rename it as shown in the file (no brackets or spaces).",
    "After publishing, purge LiteSpeed Cache.",
    "Calories per set are estimates (2024 Compendium of Physical Activities MET values, 70 kg person, 30–60 s set).",
]:
    doc.add_paragraph(line, style="List Number")
readme = os.path.join(OUT, "00-READ-ME-FIRST.docx")
doc.save(readme)

zpath = os.path.join(HERE, "ExerciseMenu-24-Exercise-Pages.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in [readme] + files:
        z.write(f, "ExerciseMenu-24-Exercise-Pages/" + os.path.basename(f))
print("ok", len(files), "pages ->", zpath)
