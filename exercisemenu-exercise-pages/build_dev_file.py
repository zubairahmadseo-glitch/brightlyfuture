"""Build the developer .docx from the exercise markdown files.

Usage: python3 build_dev_file.py  ->  writes ExerciseMenu-Developer-File.docx
"""
import glob
import os
import re

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://exercisemenu.com"
PPL = "**Push Pull Legs Workout Plan** (/workout-plans/push-pull-legs/ — link when live)"

RELATED = {
    "01": ["/how-to-deadlift-for-beginners/", "/sumo-vs-conventional-deadlift/", "/is-your-deadlift-good-average-weights-by-level-age/"],
    "02": ["/cable-back-exercises/", "/push-pull-legs-split/", "/how-many-sets-per-muscle-group-per-week/"],
    "03": ["/how-to-bench-press/", "/bench-press-grip-width/", "/shoulder-pain-bench-press/"],
    "04": ["/types-of-squats/", "/high-bar-vs-low-bar-squat/", "/why-your-knees-hurt-when-squatting/"],
    "05": ["/cable-shoulder-exercises/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/push-pull-legs-split/"],
    "06": ["/ez-curl-bar-weight/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "07": ["/cable-back-exercises/", "/push-pull-legs-split/", "/how-many-exercises-per-muscle-group-should-you-do/"],
    "08": ["/cable-shoulder-exercises/", "/how-much-does-a-barbell-weigh/", "/push-pull-legs-split/"],
    "09": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/reps-and-sets-for-woman/"],
    "10": ["/cable-shoulder-exercises/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/how-many-sets-per-muscle-group-per-week/"],
    "11": ["/cable-chest-exercises-10-best-moves/", "/shoulder-pain-bench-press/", "/push-pull-legs-split/"],
    "12": ["/what-is-progressive-overload/", "/how-many-reps-and-sets-for-muscle-growth/", "/how-to-structure-a-workout/"],
    "13": ["/ez-curl-bar-weight/", "/how-to-train-deltoids-and-biceps-with-dumbbells/", "/eccentric-vs-concentric/"],
    "14": ["/types-of-squats/", "/why-your-knees-hurt-when-squatting/", "/how-many-reps-and-sets-for-muscle-growth/"],
    "15": ["/dumbbell-romanian-deadlift/", "/how-to-deadlift-for-beginners/", "/sumo-vs-conventional-deadlift/"],
    "16": ["/how-many-reps-and-sets-for-muscle-growth/", "/what-is-progressive-overload/", "/time-under-tension/"],
}

# Where each exercise appears in the written PPL plan (the only plan with full content so far).
PLANS = {
    "01": "Pull A", "02": "Pull A", "03": "Push A", "04": "Legs A", "05": "Push B",
    "07": "Pull B", "08": "Push A", "09": "Legs B", "10": "Push A + Push B",
    "11": "Push A + Push B", "12": "Legs B (plan says 'Walking Lunges' — see GIF note)",
    "14": "Legs A", "15": "Legs A", "16": "Legs B",
}

# ---------------------------------------------------------------- docx helpers
doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10)
for sec in doc.sections:
    sec.left_margin = sec.right_margin = Pt(50)
    sec.top_margin = sec.bottom_margin = Pt(50)


def shade(cell, hex_color):
    tc = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), hex_color)
    tc.append(sh)


def rich(par, text):
    """Add text to a paragraph, rendering **bold** spans."""
    for i, part in enumerate(re.split(r"\*\*", text)):
        if part:
            par.add_run(part).bold = bool(i % 2)


def table(rows, header=True, widths=None):
    t = doc.add_table(rows=0, cols=len(rows[0]))
    t.style = "Table Grid"
    for r_i, row in enumerate(rows):
        cells = t.add_row().cells
        for c_i, val in enumerate(row):
            cells[c_i].text = ""
            rich(cells[c_i].paragraphs[0], str(val))
            if header and r_i == 0:
                for run in cells[c_i].paragraphs[0].runs:
                    run.bold = True
                shade(cells[c_i], "D9E2F3")
    if widths:
        t.autofit = False
        scale = 500 / sum(widths)
        for i, w in enumerate(widths):
            t.columns[i].width = Pt(w * scale)
            for c in t.columns[i].cells:
                c.width = Pt(w * scale)
    doc.add_paragraph()
    return t


def h(text, level):
    doc.add_heading(text, level=level)


def p(text, bold=False, italic=False):
    par = doc.add_paragraph()
    rich(par, text)
    for r in par.runs:
        r.italic = italic or r.italic
        if bold:
            r.bold = True
    return par


def bullet(text):
    rich(doc.add_paragraph(style="List Bullet"), text)


# ---------------------------------------------------------------- md parsing
def section(t, name):
    m = re.search(r"^## " + re.escape(name) + r"\s*\n(.*?)(?=^## |^---\s*$|\Z)", t, re.S | re.M)
    return m.group(1).strip() if m else ""


def md_table(block):
    rows = [r for r in block.splitlines() if r.startswith("|")]
    out = []
    for r in rows:
        cells = [c.strip() for c in r.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        out.append(cells)
    return out


def code_lines(block):
    m = re.search(r"```\n(.*?)```", block, re.S)
    return m.group(1).strip() if m else ""


def parse(path):
    t = open(path, encoding="utf-8").read()
    d = {"name": re.search(r"^# (.+)", t, re.M).group(1).strip()}
    d["head"] = [l[2:] for l in t.split("---")[0].splitlines() if l.startswith("- ")]
    seo = section(t, "SEO & Meta")
    d["title"] = re.search(r"\*\*Meta Title \(≤60\):\*\*\s*\n(.+)", seo).group(1).strip()
    d["desc"] = re.search(r"\*\*Meta Description \(≤160\):\*\*\s*\n(.+)", seo).group(1).strip()
    d["basics"] = dict((r[0], r[1]) for r in md_table(section(t, "Exercise Basics"))[1:])
    d["alt"] = re.search(r"GIF Alt Text:\*\*\s*(.+)", t).group(1).strip()
    d["qa"] = section(t, "Quick Answer (AEO)")
    mw = section(t, "Muscles Worked")
    parts = mw.split("**Secondary Muscles")
    d["primary"], d["secondary"] = code_lines(parts[0]), code_lines(parts[1])
    d["steps"] = md_table(section(t, "How-To Steps"))[1:]
    d["sets"] = md_table(section(t, "Sets & Reps Table"))
    d["mistakes"] = re.findall(r"^\d+\. \*\*(.+?)\*\* (.+)$", section(t, "Common Mistakes"), re.M)
    d["tips"] = re.findall(r"^\d+\. \*\*(.+?)\*\* (.+)$", section(t, "Tips"), re.M)
    d["mods"] = md_table(section(t, "Modifications (Easier/Harder)"))[1:]
    faq = section(t, "FAQs")
    d["faqs"] = re.findall(r"\*\*Q: (.+?)\*\*\s*\n\s*A: (.+)", faq)
    d["cites"] = re.findall(r"\*\*Citation[^*]*\*\*\s*(.+)", t)
    return d


# ---------------------------------------------------------------- content: audit + fixes
LIVE_FIXES = [
    ("Barbell Lying Triceps Extension", "/exercises/barbell-lying-triceps-extension/", [
        ("Quick Answer (AEO)", "Quick Answer Text", "Says 'lower it behind your head'. The GIF lowers the bar to the forehead.",
         "The barbell lying triceps extension is an isolation lift that targets all three heads of the triceps. Lie flat on a bench, hold a barbell over your shoulders with arms straight, and bend only at the elbows to lower it toward your forehead. Press back up. Use 3 sets of 8 to 12 reps."),
        ("How-To Steps", "Step 2 Title", "'positioned over your eyes' does not match the GIF", "Press the bar up so your arms are straight and vertical over your shoulders"),
        ("How-To Steps", "Step 4 Title", "'behind your head until forearms touch biceps' does not match the GIF", "Lower the bar slowly toward your forehead, keeping your upper arms still"),
        ("Tips", "Tip 2", "Says this 'extends the shoulder'. Wrong: arms angled back = shoulder FLEXION.",
         "Let the Upper Arms Tilt Back Slightly: Allowing the upper arms to angle slightly toward your head increases shoulder flexion, which puts the long head of the triceps under more stretch. Keep the movement at the elbows."),
        ("Tips", "Tip 4", "'Set the bar over your eyes' contradicts the GIF; 'reduces results' is unsupported",
         "Start with the Bar Over Your Shoulders: Begin each set with your arms vertical over your shoulders so the triceps hold the weight in a stable position."),
        ("Modifications (Easier/Harder)", "Harder #1", "Decline bench gives LESS long-head stretch, not more",
         "Type: Harder | Title: Incline Lying Triceps Extension | Description: Doing the lift on a low incline bench angles the arms further overhead relative to the torso, which puts the long head of the triceps under a greater stretch."),
        ("FAQs", "Answer 1", "Contradicts itself", "Yes. Skull crusher is the common gym name for this exercise. Some lifters lower the bar to the forehead and others just behind the head; both are the same lift."),
        ("FAQs", "Answer 2", "'Straight bar for maximum long-head stretch' is unsupported", "Both work. Many lifters find the angled EZ bar grip easier on the wrists and elbows, so it is a common choice."),
    ]),
    ("Barbell Incline Bench Press", "/exercises/barbell-incline-bench-press/", [
        ("How-To Steps", "Step 5", "'press slightly over your face' — GIF finishes over the shoulders", "Press the bar back up until your arms lock out with the bar over your shoulders."),
        ("Common Mistakes", "Mistake 5", "Tells readers to finish 'above your eyes'",
         "Letting the Bar Drift Toward Your Stomach: On an incline the bar should finish over your shoulders. Pressing it forward toward your stomach puts the weight in a weaker, harder-to-control position."),
        ("Tips", "Tip 1", "Says 30–45° while the rest of the page says 30°", "Confirm the Bench Angle First: Not every bench marks its angle. Aim for about 30 degrees and use the same setting every week so you can track progress."),
        ("FAQs", "Answer 1", "'Research-backed' with no source",
         "About 30 degrees. A 2020 study by Rodríguez-Ridao and colleagues found upper-chest activity peaked at 30 degrees, while angles above 45 degrees shifted more work to the front delts. (Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC7579505/)"),
        ("FAQs", "Answer 5", "'20 to 30 percent less weight' has no source", "Yes for most lifters. The front delts take a bigger share of the work on an incline, so expect to use less weight than on a flat bench."),
    ]),
    ("Barbell Bench Press", "/exercises/barbell-bench-press/", [
        ("How-To Steps", "Steps 1–6", "SECTION IS EMPTY ON THE LIVE PAGE",
         "1 Set up under the bar — Lie on the bench with your eyes under the bar and feet flat on the floor. | 2 Set your grip — Grip the bar slightly wider than shoulder-width, wrists stacked over your forearms. | 3 Pin your shoulder blades — Pull them back and down into the bench, keeping a small natural arch. | 4 Unrack — Lift the bar out and hold it with straight arms over your shoulders. | 5 Lower to mid-chest — Lower under control to your mid or lower chest, elbows about 45–70° from your torso. | 6 Press up — Press up and slightly back until your arms lock out over your shoulders."),
        ("Modifications (Easier/Harder)", "Harder — Close-Grip Bench Press", "'shifts load to the inner chest' — inner-chest targeting is a myth",
         "Narrow your grip to about shoulder-width. This shifts more of the work to the triceps and builds lockout strength."),
        ("FAQs", "Answer 1", "'women start with a 15–25 lb bar' — not a standard bar; no source",
         "Start with a weight you can lift for 8–10 controlled reps. For many beginners that is the empty 20 kg (45 lb) bar or a lighter fixed barbell. Add 1–2.5 kg (2.5–5 lb) when every set feels solid."),
        ("FAQs", "Answer 4", "Correct, but no source", "Add: (Rodríguez-Ridao et al., 2020 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7579505/)"),
    ]),
    ("Barbell Standing Calf Raise", "/exercises/992896/", [
        ("URL / Slug", "Slug", "Slug is a number", "barbell-standing-calf-raise  + 301 redirect from /exercises/992896/"),
        ("Quick Answer (AEO)", "Quick Answer Text", "Calls the soleus a 'stabiliser' (it is a prime mover); unclear wording",
         "The barbell standing calf raise is a calf exercise done standing with a barbell across your upper back. Straight knees make the gastrocnemius the main mover, with the soleus assisting. Raise your heels as high as you can, then lower for a full stretch. Use 3–4 sets of 10–15 reps."),
        ("Tips", "Tip 2", "Wrong journal (it is Experimental Brain Research) and an invented '20–35°' threshold",
         "Knee Position Decides Which Calf Muscle Works Most: Cresswell and colleagues (1995, Experimental Brain Research) found gastrocnemius activity fell as the knee bent while soleus activity stayed the same. Straight knees bias the gastrocnemius; bent-knee seated raises bias the soleus. (https://pubmed.ncbi.nlm.nih.gov/7498381/)"),
        ("Tips", "Tip 1", "Study is real and correctly described — only the link is missing", "Add link: https://www.mdpi.com/1660-4601/17/24/9487"),
        ("Tips", "Tip 3", "'Gastrocnemius recovers faster… responds better to frequency' — no source",
         "Train Calves 2–3 Times per Week: Splitting your weekly calf sets across two or three sessions keeps each session short and the quality of each rep high."),
        ("Tips", "Tip 4", "'Lifters… are almost always missing this range' — overclaim",
         "Use a Raised Platform: Standing on a step lets the heels drop below the toes. Kassiano et al. (2023) found calf raises trained in the stretched range grew the gastrocnemius more than raises trained in the shortened range."),
        ("Common Mistakes", "Mistake 3", "'small muscle that fatigues faster' — unsupported", "Delete that sentence; keep the rest of the mistake."),
        ("Modifications (Easier/Harder)", "Harder #2", "Seated calf raise labelled 'Harder' — the page itself says it is not a progression",
         "Type: Harder | Title: Paused Standing Calf Raise | Description: Hold the bottom stretch for 2 seconds and the top for 1 second on every rep. This removes the bounce and makes the calves do all the work."),
    ]),
    ("Dumbbell Bench Press", "/exercises/dumbbell-bench-press/", [
        ("Tips", "Tip 3", "MISQUOTED STUDY. Solstad 2020 compared barbell bench vs dumbbell FLYES, not dumbbell presses",
         "Dumbbells vs Barbell: Saeterbakken and colleagues (2011, Journal of Sports Sciences) found similar chest and front-delt activity in barbell, Smith machine and dumbbell bench presses, but 1-RM was about 17% lower with dumbbells. (https://pubmed.ncbi.nlm.nih.gov/21225489/)"),
        ("Common Mistakes", "Mistake 1", "'load transfers away from the pecs' — unsupported", "Flaring Elbows to 90 Degrees: Fully flared elbows put the front of the shoulder in a more stressful position. Keep them about 45–75 degrees from your torso."),
        ("Common Mistakes", "Mistake 5", "'most common injury mechanism' — no source", "Dropping the Dumbbells to the Side: Letting heavy dumbbells fall out wide with your arms stretched can strain the shoulders. Bring them to your thighs and sit up."),
        ("Tips", "Tip 4", "'reduces long-term impingement risk' — no evidence", "Program It Early: Do the dumbbell bench press near the start of a push session while you are fresh, and balance your weekly pressing with rows."),
        ("Tips", "Tip 1", "NASM citation without a link", "Remove '(NASM Exercise Library: nasm.org)'."),
        ("Modifications (Easier/Harder)", "Harder #2 (Tempo)", "'Research consistently supports eccentric loading as a primary driver' — overclaim; Schoenfeld 2015 found similar growth from 0.5–8 s reps",
         "Lower each rep over 3–4 seconds. The slower lowering makes the same weight harder and builds control."),
        ("FAQs", "Answer 4", "'women 6–10 kg, men 10–16 kg' — no source", "Start with a weight you can press for 10–12 controlled reps with a full range of motion. The right starting weight varies widely from person to person."),
    ]),
    ("Barbell Curl", "/exercises/barbell-curl/", [
        ("How-To Steps", "Step 5 Description", "'eccentric is a primary driver of hypertrophy' — overclaim", "Lower the bar slowly over 2–3 seconds until your arms are almost straight."),
        ("Common Mistakes", "Mistake 4", "'eccentric is a primary driver of muscle protein synthesis' — overclaim", "Rushing the Lowering Phase: Dropping the bar fast loses control and tension. Lower over 2–3 seconds."),
        ("Tips", "Tip 2 + FAQ Answer 2", "Leaves out the study's main finding", "Marcolin and colleagues (2018, PeerJ) found only small differences between the straight bar and the EZ bar, and higher activation with the EZ bar than with dumbbells. Pick the bar that feels better on your wrists. (https://peerj.com/articles/5165/)"),
        ("Modifications (Easier/Harder)", "Harder — Barbell Drag Curl", "'stretches the long head… removes delts entirely' — incorrect",
         "Drag the bar up along your body while pulling the elbows back. This stops the front delts from helping and keeps the biceps working hard at the top."),
    ]),
    ("Dumbbell Hammer Curl", "/exercises/dumbbell-hammer-curl/", [
        ("Exercise Basics", "Subtitle", "'An alternating curl' — both arms together is also standard", "A dumbbell curl with a neutral (thumbs-up) grip that works the brachialis and brachioradialis more than a standard curl."),
        ("Common Mistakes", "Mistake 2", "WRONG: curling both arms together is not a mistake", "Letting the Dumbbells Swing Forward: Swinging the weights out in front uses momentum. Keep them moving straight up and down at your sides."),
        ("Tips", "Tip 1", "Copy-paste of Mistake 5", "Keep the Thumbs Up the Whole Time: Hold the neutral grip from bottom to top so the brachialis and brachioradialis stay loaded."),
        ("Tips", "Tip 2", "Wrist straps make no sense for a forearm-building curl", "Try Cross-Body Hammer Curls: Curling toward the opposite shoulder is a common variation that some lifters find more comfortable."),
        ("Modifications (Easier/Harder)", "Harder — Cross-Body Hammer Curl", "'greater range and brachialis stretch' — unsupported", "Curl the dumbbell across your body toward the opposite shoulder. Many lifters find this angle comfortable on the wrist and elbow."),
        ("FAQs", "Answer 2", "Says bilateral hammer curls are less common — incorrect", "Both are fine. Alternating gives each arm a short rest and makes strict form easier; curling both arms together saves time."),
        ("FAQs", "Answer 3", "FALSE: says the brachioradialis is larger than the biceps", "With a neutral grip the brachioradialis is in a strong position, and the brachialis and biceps still help, so most people can lift a little more than with a palms-up curl."),
        ("Related Training Articles", "—", "Empty", f"{SITE}/how-to-train-deltoids-and-biceps-with-dumbbells/ · {SITE}/how-many-reps-and-sets-for-muscle-growth/ · {SITE}/what-is-progressive-overload/"),
    ]),
    ("Dumbbell Biceps Curl", "/exercises/dumbbell-biceps-curl/", [
        ("How-To Steps", "Step 5 Description", "'significant portion of muscle stimulus' — overclaim + banned word", "Return the dumbbells slowly over 2–3 seconds to full extension. Do not bounce or cut the range short."),
        ("Common Mistakes", "Mistake 4", "'NSCA research confirms…' — no such source given", "Rushing the Lowering Phase: Dropping the weight fast loses control and tension. Lower over 2–3 seconds on every rep."),
        ("Tips", "Tip 2", "'external rotation of the wrist… short head' — wrong anatomy (it is forearm supination)", "Keep Turning the Palms Up: The biceps bend the elbow and also turn the palm up. Keeping the palms fully turned up, little finger slightly higher, keeps the biceps working through the rep."),
        ("FAQs", "Question 2 + Answer 4", "Stray ':' at the start", "Delete the leading colon."),
        ("FAQs", "Answer 4", "'48–72 hours' — no source", "Training biceps hard every day leaves little time to recover. Two or three sessions a week with a rest day between works well for most lifters."),
        ("FAQs", "Answer 5", "'women 5–8 kg, men 8–12 kg' — no source", "Start with a weight you can curl for 10–12 controlled reps without swinging. If the last two reps break form, go lighter."),
        ("Related Training Articles", "—", "Empty", f"{SITE}/how-to-train-deltoids-and-biceps-with-dumbbells/ · {SITE}/how-many-reps-and-sets-for-muscle-growth/ · {SITE}/eccentric-vs-concentric/"),
    ]),
]

PPL_FIXES = [
    ("What Is a PPL Split — research box", "Says 2×/week beat 1×/week 'even when total weekly volume was equated'. The 2019 update (Schoenfeld, Grgic & Krieger) found NO frequency effect when volume is equated.",
     "Training each muscle twice a week makes it easier to spread your weekly sets across sessions. A 2019 meta-analysis by Schoenfeld, Grgic and Krieger found that when weekly volume is equal, frequency itself makes little difference — so choose the split that lets you hit your weekly sets with good quality."),
    ("Schedule intro", "'force production and metabolic stress — the two primary drivers of muscle growth' — inaccurate", "Delete the phrase after the dash."),
    ("Workout B intro", "Lists 'time under tension, metabolic stress, accumulated volume' as Schoenfeld's 3 mechanisms — wrong. Schoenfeld (2010) named mechanical tension, metabolic stress and muscle damage.",
     "…the emphasis shifts to more volume, shorter rests and more isolation work."),
    ("Weekly Volume Summary", "Glutes A-day = squat 4 + RDL 4 + BSS 3 = 11, not 7. Weekly total = 18, not 14.", "Glutes: A = 11 · B = 7 · Total = 18"),
    ("Weekly Volume Summary intro + Mistake 3", "Attributes '10–20 sets is the most efficient range' and a '~20-set ceiling' to Pelland 2025. The paper reports diminishing returns, not a fixed ceiling.",
     "Most lifters grow well on about 10–20 hard sets per muscle per week. Pelland et al. (Sports Medicine, 2025) found more volume keeps adding muscle but with diminishing returns, so add sets only if you recover well."),
    ("Stats bar", "'33 Unique Exercises' — the plan lists 34 (35 if woodchop and hanging leg raise count separately)", "Change to 34."),
    ("Mistake 2 'Skipping Leg Day'", "'produce the most growth hormone… limits whole-body growth' — myth", "Leg training builds the largest muscles in your body and the strength you use in almost every other lift. Skipping it leaves your physique and strength unbalanced."),
    ("Mistake 4", "'creates internal rotation and shoulder problems' — overclaim", "This plan balances pressing with rowing and face pulls on both pull days. Do not skip them."),
    ("Legs B notes", "'one of the most effective glute exercises based on EMG' — EMG did not predict growth (Plotkin 2023)", "Hip thrusts load the glutes hard at full hip extension, which complements the deep-knee-bend work from squats and lunges."),
    ("Push B notes", "'pushdowns hit the lateral head, overhead extensions hit the long head' — oversimplified", "Overhead extensions train the long head in a stretched position; Maeo et al. (2022) found more triceps growth with overhead than with neutral-arm extensions."),
    ("Pull B notes", "'stretch the long head, which regular curls miss' — overclaim", "Incline curls start with the arms behind the body, which puts the biceps long head in a longer position than standing curls."),
    ("Author box", "'Reviewed by FISAF-certified coaches · verified by registered dietitian' — your brief says NO byline; only keep if true and named", "Remove the box."),
    ("CTA 'Download PDF / spreadsheet'", "Those files do not exist", "Remove, or replace with a link to the workout plans hub when it is live."),
    ("Related Workout Plans", "'Body Recomposition Workout Plan' is not one of your 15 plans", "Replace with 5×5 Workout or Hypertrophy Program (4-Day)."),
    ("Exercise names", "No links to exercise pages", "Link each exercise name to its /exercises/ page once it is live (map below)."),
    ("Legs B — 'Walking Lunges (Dumbbells)'", "Your purchased GIF is a forward lunge, not a walking lunge", "Rename to 'Dumbbell Lunge' or buy a walking-lunge GIF."),
]

# ---------------------------------------------------------------- build
title = doc.add_heading("ExerciseMenu — Developer File: Exercise Pages", 0)
p("Field names below match the Exercise plugin exactly. Copy each value into the field with the same name. Prepared 29 Oct 2026.", italic=True)

h("1. Audit Result (short)", 1)
table([
    ["Check", "Result"],
    ["Content accurate?", f"New 16 pages: yes, after re-check. Live 8 pages: NO — {sum(len(x[2]) for x in LIVE_FIXES)} fixes listed in Part 3 (1 false fact, 1 misquoted study, 1 wrong journal, 2 pages that don't match their GIF, 1 empty section)."],
    ["Authentic / verified data?", "Only 9 studies are cited, every one opened and checked (links included). Unsourced numbers (beginner weights, '48–72 h', '20–30% less') were removed."],
    ["Exercise performance (form) accurate?", "Every step was matched frame-by-frame to the purchased GIF. Two live pages describe a different movement than their GIF (Lying Triceps Extension, Incline Bench finish position)."],
    ["AI voice / AI pattern?", "Banned words removed (very, significant, essentially, etc.). Repeated FAQ openers ('Both work.') varied. Live pages still have stock lines like 'Almost always…' and 'This is the most common…' — fixed where they were also factual errors."],
    ["Related articles relevant?", "Each new page gets 3 live, topic-matched articles (all checked on the sitemap). Hammer Curl + Biceps Curl live pages had none — added."],
    ["Anything irrelevant?", "Removed: wrist straps on hammer curls, 'growth hormone' claim, fake PDF download CTA, non-existent 'Body Recomposition' plan card, unverified author box."],
    ["Calories per set", "Recalculated with the 2024 Compendium of Physical Activities (code 02054 = 3.5 MET; squat/deadlift = 5.0 MET), 70 kg person, 30–60 s set → 2–4 kcal (most lifts), 3–6 kcal (squat, deadlift, RDL, split squat)."],
], widths=[130, 360])

h("2. Plugin / Site Changes for the Developer", 1)
h("2a. Change These Existing Sections", 2)
table([
    ["Plugin Section", "Change", "Why"],
    ["SEO & Meta", "Make sure the plugin's Meta Title / Meta Description feed Rank Math (or Rank Math's own fields) — the page must output only ONE <title> and ONE meta description. Set the description counter to 155.", "Duplicate meta tags confuse Google; Google usually cuts descriptions around 155 characters."],
    ["Exercise Basics", "Turn Target Muscle, Body Part, Equipment and Skill Level into taxonomies (dropdown / checkbox), not free text.", "The archive says 'filtered by muscle group, equipment, and skill level' — filters need taxonomies, and each term gets its own archive page (e.g. /equipment/dumbbells/)."],
    ["Exercise Basics", "Rename 'Approx. Calories per set' → 'Estimated Calories per set' and show a fixed note on the page: 'Estimate for a 70 kg person, 30–60 s set.'", "It is an estimate; the note keeps it honest."],
    ["GIF / Media", "Replace the URL text box with a Media Library picker; output width/height and loading=\"lazy\". Remove the 'Replace YOUR_CDN_URL' helper text.", "Fewer broken links and faster pages."],
    ["How-To Steps", "Make Step Description required; limit Step Title to ~60 characters.", "Lying Triceps page has full sentences in the titles and every description empty."],
    ["Common Mistakes", "Split each item into 'Mistake Title' + 'Mistake Description'.", "Today it is one textarea; Lying Triceps Mistake 5 has no title, so formatting is inconsistent."],
    ["Tips", "Split each item into 'Tip Title' + 'Tip Description'.", "Same reason as Common Mistakes."],
    ["Modifications (Easier/Harder)", "Add optional 'Link to exercise page' to each item.", "When the variation has its own page (e.g. Dumbbell Bench Press), it becomes an internal link."],
    ["FAQs", "Trim leading/trailing spaces and punctuation on save.", "Dumbbell Biceps Curl FAQs show a stray ':' at the start."],
    ["Sets & Reps Table", "Remove the line 'Rest periods follow ACSM guidelines' or link it to the ACSM position stand.", "An unlinked authority claim."],
], widths=[90, 230, 170])

h("2b. Add These New Sections", 2)
table([
    ["New Section", "Fields", "Why"],
    ["Related Training Articles", "3 post pickers (shown as cards).", "It shows on the front end but there is no field — two live pages show it empty."],
    ["Workout Plans Using This Exercise", "Repeater: Plan (post picker) + Day label (e.g. 'Push A'). Best: fill automatically from plans that link to this exercise.", "LoadMuscle has 'Workout plans with Push up'. This is the exercise → plan internal link you want."],
    ["Alternative Exercises", "2–4 exercise post pickers, shown as cards with the GIF thumbnail.", "LoadMuscle has 'Alternatives'. Links exercise → exercise."],
    ["Sources", "Repeater: Citation text + URL.", "Studies appear in one list at the bottom instead of inside Tips."],
    ["Last Updated", "Automatic date from the post's modified date.", "Shows the page is maintained (no author byline needed)."],
    ["Muscle Map Image (optional)", "Image picker.", "LoadMuscle shows a front/back muscle diagram."],
], widths=[110, 200, 180])

h("2c. Technical (no new field)", 2)
for b in [
    "**Sitemap:** the 'exercises' post type is missing from sitemap_index.xml. Rank Math → Sitemap Settings → enable Exercises.",
    "**Slug:** change /exercises/992896/ → /exercises/barbell-standing-calf-raise/ and add a 301 redirect.",
    "**Schema:** output FAQPage (from FAQs) + ImageObject (GIF) + Article/WebPage JSON-LD. Note: Google stopped showing HowTo rich results in 2023 and limits FAQ rich results, so schema helps understanding, not star-style snippets.",
    "**REST API:** register the exercise post type and its meta with show_in_rest = true. Then pages can be filled automatically through the API instead of copy-paste.",
]:
    bullet(b)

h("3. Fixes for the 8 Live Pages", 1)
for name, url, fixes in LIVE_FIXES:
    h(f"{name}  ({url})", 2)
    table([["Plugin Section", "Field", "Problem", "Replace With"]] + [list(f) for f in fixes], widths=[80, 70, 130, 210])

h("4. Workout Plan Check — Push Pull Legs (Plan #1)", 1)
p("The 15 plans are not live yet (/workout-plans/ redirects to the homepage). The full PPL draft (sample-ppl-page.html) was checked; sets per session and the other weekly-volume totals add up correctly. Fixes:")
table([["Section", "Problem", "Replace With"]] + [list(f) for f in PPL_FIXES], widths=[100, 190, 200])
p("**Plans #2–#15:** only titles and meta exist in the repo (no exercise lists), so they could not be checked. Send them and they will get the same check.")

h("Exercise → Plan link map (PPL)", 2)
table([
    ["Exercise in PPL", "Link to"],
    ["Barbell Bench Press (Push A)", "/exercises/barbell-bench-press/ (live)"],
    ["Flat Dumbbell Press (Push B)", "/exercises/dumbbell-bench-press/ (live)"],
    ["Barbell Curl (Pull A)", "/exercises/barbell-curl/ (live)"],
    ["Dumbbell Curl (Pull B)", "/exercises/dumbbell-biceps-curl/ (live)"],
    ["Standing Calf Raise (Legs A)", "/exercises/barbell-standing-calf-raise/ (after slug fix)"],
    ["Overhead Press, Incline DB Press, Lateral Raise, Close-Grip Bench, Deadlift, Bent-Over Row, Back Squat, RDL, Bulgarian Split Squat, Seated DB Shoulder Press, One-Arm Row, Hip Thrust, Lunge, Seated Calf Raise", "New pages in Part 5 — link once published"],
    ["Weighted Dips, Pull-Ups, Cable Row, Face Pull, Leg Curl, Leg Extension, Cable Fly, Pushdown, Overhead Cable Ext., Lat Pulldown, Reverse Pec Deck, Incline Hammer Curl, Leg Press, Woodchop / Hanging Leg Raise", "No GIF purchased yet — leave unlinked"],
], widths=[260, 230])

h("5. New Exercise Pages (16)", 1)
p("GIF: upload the _720.gif from the zip to the Media Library and paste its URL into 'GIF CDN URL'. Rename files as shown (no brackets or spaces).")

for f in sorted(g for g in glob.glob(os.path.join(HERE, "[01][0-9]-*.md")) if not os.path.basename(g).startswith("00")):
    n = os.path.basename(f)[:2]
    d = parse(f)
    doc.add_page_break()
    h(f"5.{int(n)}  {d['name']}", 2)
    for line in d["head"]:
        p(line.replace("`", ""))

    h("SEO & Meta", 3)
    table([["Field", "Value"], [f"Meta Title {len(d['title'])}/60", d["title"]], [f"Meta Description {len(d['desc'])}/160", d["desc"]]], widths=[130, 360])

    h("Exercise Basics", 3)
    b = d["basics"]
    table([["Field", "Value"],
           ["Subtitle (one line description)", b["Subtitle"]],
           ["Tags (comma-separated)", b["Tags"]],
           ["Target Muscle (sidebar display)", b["Target Muscle (sidebar)"]],
           ["Body Part", b["Body Part"]],
           ["Equipment", b["Equipment"]],
           ["Category (Isolation / Compound)", b["Category"]],
           ["Skill Level", b["Skill Level"]],
           ["Movement Pattern", b["Movement Pattern"]],
           ["Also Known As", b["Also Known As"]],
           ["Approx. Calories per set", b["Approx. Calories per set"]]], widths=[160, 330])

    h("GIF / Media", 3)
    gif = re.search(r"rename to (\S+)", " ".join(d["head"]))
    table([["Field", "Value"], ["GIF CDN URL", f"{SITE}/wp-content/uploads/YYYY/MM/{gif.group(1).strip('`') if gif else ''}"], ["GIF Alt Text", d["alt"]]], widths=[130, 360])

    h("Quick Answer (AEO)", 3)
    table([["Field", "Value"], [f"Quick Answer Text {len(d['qa'])}/320 · {len(d['qa'].split())} words", d["qa"]]], widths=[130, 360])

    h("Muscles Worked", 3)
    table([["Field", "Value (one per line)"], ["Primary Muscles", d["primary"]], ["Secondary Muscles", d["secondary"]]], widths=[110, 380])

    h("How-To Steps", 3)
    table([["Step", "Step Title", "Step Description"]] + [[s[0], s[1], s[2]] for s in d["steps"]], widths=[30, 120, 340])

    h("Sets & Reps Table", 3)
    table(d["sets"], widths=[120, 90, 120, 120])

    h("Common Mistakes", 3)
    table([["Field", "Value"]] + [[f"Mistake {i}", f"{a} {b_}"] for i, (a, b_) in enumerate(d["mistakes"], 1)], widths=[70, 420])

    h("Tips", 3)
    table([["Field", "Value"]] + [[f"Tip {i}", f"{a} {b_}"] for i, (a, b_) in enumerate(d["tips"], 1)], widths=[70, 420])

    h("Modifications (Easier/Harder)", 3)
    table([["Type", "Title", "Description"]] + [[m[0].replace("🔽 ", "").replace("🔼 ", ""), m[1], m[2]] for m in d["mods"]], widths=[55, 130, 305])

    h("FAQs", 3)
    rows = [["#", "Question", "Answer"]] + [[str(i), q, a] for i, (q, a) in enumerate(d["faqs"], 1)]
    table(rows, widths=[20, 160, 310])

    h("Related Training Articles", 3)
    for u in RELATED[n]:
        bullet(SITE + u)

    h("Workout Plans Using This Exercise (new section — Part 2)", 3)
    bullet(f"{PPL} — {PLANS[n]}" if n in PLANS else "Not used in the PPL plan. Add plans #2–#15 here when they are written.")

    if d["cites"]:
        h("Sources", 3)
        for c in d["cites"]:
            bullet(c)

out = os.path.join(HERE, "ExerciseMenu-Developer-File.docx")
doc.save(out)
print("saved", out)
