"""The three GIF-vs-content fixes, applied, with the source behind each one."""
import os
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
B = "https://exercisemenu.com/wp-content/uploads/2026/10/"

def shade(c, h):
    pr = c._tc.get_or_add_tcPr(); s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), h); pr.append(s)

def new_doc():
    d = Document(); st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
    for s in d.sections:
        s.left_margin = s.right_margin = Pt(50); s.top_margin = s.bottom_margin = Pt(46)
    return d

def grid(doc, header, rows, widths, fill="D9E2F3"):
    t = doc.add_table(rows=0, cols=len(header)); t.style = "Table Grid"; t.autofit = False
    for i, row in enumerate([header] + rows):
        cells = t.add_row().cells
        for j, v in enumerate(row):
            cells[j].text = str(v); cells[j].width = Pt(widths[j])
            if i == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], fill)
            elif j == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], "F3F2F0")
    doc.add_paragraph()

def small(doc, text):
    p = doc.add_paragraph(); r = p.add_run(text); r.italic = True
    r.font.color.rgb = RGBColor(0x5f, 0x5c, 0x55); r.font.size = Pt(9.5)

PAGES = [
 dict(n="Barbell Lying Triceps Extension", gif="Barbell-Lying-Triceps-Extension.gif",
   url="https://exercisemenu.com/exercises/barbell-lying-triceps-extension/",
   gifsaw="Across all 30 frames the upper arms stay vertical and only the forearms move. At the bottom the bar "
          "passes the forehead and finishes just over the top of the head.",
   wrong="The page said the bar stops just above the forehead, which is not what the GIF does.",
   src="ACE (American Council on Exercise), Lying Barbell Triceps Extensions, Exercise Library:\n"
       "\"Lower the bar toward your forehead. It can go slightly behind your head, but stop once it reaches just "
       "above your forehead or once your upper arms start drifting backward.\" It also says to keep the upper arms "
       "vertical to the floor and move only the forearms.\n"
       "https://www.acefitness.org/resources/everyone/exercise-library/36/lying-barbell-triceps-extensions/",
   why="The GIF is doing exactly what ACE allows: upper arms vertical, bar travelling slightly past the forehead. "
       "So the page now describes that path AND carries ACE's stopping rule, which it did not have before.",
   rows=[["How-To Steps, Step 4 Title", "Lower to your forehead or just past it"],
         ["How-To Steps, Step 4 Description",
          "Bend your elbows to lower the bar slowly in an arc to just above your forehead. It can travel a little "
          "further, to just over the top of your head, as the demonstration shows. Stop if your upper arms start to drift backward."],
         ["Common Mistakes, Mistake 4",
          "Dropping the Bar Fast: Letting the bar fall toward your head is unsafe. Control every rep and never let the bar touch your head."],
         ["GIF / Media, GIF Alt Text",
          "Barbell lying triceps extension exercise demonstration lowering the bar past the forehead"],
         ["Quick Answer (AEO)  (290 of 320 characters, 58 of 60 words)",
          "The barbell lying triceps extension is an isolation lift for all three heads of the triceps. Lie flat on a "
          "bench, hold a barbell over your shoulders with straight arms, then bend only at the elbows to lower it to "
          "your forehead or a little past it. Press back up. Use 3 sets of 8 to 12 reps."]]),

 dict(n="Cable Kneeling Crunch", gif="Cable-Kneeling-Crunch.gif",
   url="https://exercisemenu.com/exercises/cable-kneeling-crunch/",
   gifsaw="At the top the hips sit over the knees. By the bottom the body has folded into a ball and the hips have "
          "clearly travelled back toward the heels. Checked against vertical reference lines drawn over the frames.",
   wrong="The page called any hip travel a mistake and told readers to keep the hips over the knees, so it "
         "contradicted its own GIF in five places.",
   src="ACE (American Council on Exercise), Crunch, Exercise Library:\n"
       "\"The movement should focus on pulling your rib cage towards your pelvis.\" The same page warns that moving "
       "too fast recruits the hip flexors to assist, which tilts the pelvis and should be avoided.\n"
       "https://www.acefitness.org/resources/everyone/exercise-library/52/crunch/",
   why="ACE defines the fault precisely: the problem is the hip flexors doing the work, not the hips moving at all. "
       "The page now says the same thing, and the new Mistake 1 cites ACE directly. A new Sources entry was added.",
   rows=[["Quick Answer (AEO)",
          "The cable kneeling crunch is an ab exercise done on your knees below a high pulley. Hold a rope beside your "
          "head and curl your ribs toward your hips by rounding your spine, not by folding at the hips. Uncurl slowly "
          "to return. Use 2 to 3 sets of 10 to 15 reps."],
         ["Rank Math SEO, Description  (143 of 155)",
          "How to do the cable kneeling crunch so your spine does the work, not your hips. Muscles worked, sets and "
          "reps, common mistakes, and FAQs."],
         ["How-To Steps, Step 4 Description",
          "Breathe out and round your spine, pulling your ribs toward your hips and your elbows toward your thighs. "
          "Your hips settle back a little as you fold, as they do in the demonstration; what matters is that the "
          "movement comes from your spine rounding."],
         ["Common Mistakes, Mistake 1",
          "Folding at the Hips With a Flat Back: If your back stays straight and you simply bend forward at the hips, "
          "the abs do little. ACE's crunch instructions describe the movement as pulling your rib cage toward your "
          "pelvis, so round your spine on every rep."],
         ["FAQs, Answer 3",
          "Most often the back is staying flat and the movement is coming from the hips. Lighten the weight and curl "
          "your ribs toward your hips so your spine rounds."],
         ["Sources (Citations) — ADD as Source 1, push the existing one to Source 2",
          "Citation text: American Council on Exercise (ACE). Crunch - Exercise Library.\n"
          "URL: https://www.acefitness.org/resources/everyone/exercise-library/52/crunch/"]]),

 dict(n="Leg Press (45-degree sled)", gif="Sled-45%C2%B0-Leg-Press-Hips.gif",
   url="https://exercisemenu.com/exercises/leg-press/",
   gifsaw="Feet in the middle of the platform at about hip width, which the page already had right. The knees bend "
          "well past 90 degrees and the thighs come close to the torso, while the hips and lower back stay flat on the pad.",
   wrong="The page led with 'about 90 degrees', which is shallower than the demonstration.",
   src="Martin-Fuentes I, Oliva-Lozano JM, Muyor JM. Evaluation of the Lower Limb Muscles' Electromyographic "
       "Activity during the Leg Press Exercise and Its Variants: A Systematic Review. Int J Environ Res Public "
       "Health. 2020;17(13):4626. The review states: \"The range of motion performed during the leg press exercises "
       "ranged from 120 degrees to 0 degrees knee flexion.\"\n"
       "https://pmc.ncbi.nlm.nih.gov/articles/PMC7369968/\n"
       "This review is already cited on your page for foot position, so no new source is needed.",
   why="Going past 90 degrees is inside the range the research itself uses, so the demonstration is not doing "
       "anything unusual. The page now leads with the practical limit instead of a number.",
   rows=[["Quick Answer (AEO)  (277 of 320 characters, 57 of 60 words)",
          "The leg press is a machine exercise for the quads and glutes. Sit with your back flat on the pad and feet "
          "hip-width on the platform, lower the sled as far as you can with your hips and back still flat, then press "
          "back up without locking your knees. Use 3 sets of 10 to 15 reps."],
         ["How-To Steps, Step 4 Description",
          "Bend your knees to lower the sled toward your chest as far as you can while your hips and lower back stay "
          "flat on the pad. The demonstration goes past 90 degrees of knee bend. Stop sooner if your hips start to "
          "curl up off the pad."],
         ["Common Mistakes, Mistake 1",
          "Hips Lifting off the Pad: Lowering past your own hip mobility makes your hips curl up and your lower back "
          "round. Your own limit is the depth where your hips and back still stay flat on the pad, whatever the knee angle."],
         ["Tips, Tip 2",
          "Depth Comes Before Weight: Use a load you can lower to your full, safe depth. The review by Martin-Fuentes "
          "and colleagues (2020) describes leg press ranges of motion running to 120 degrees of knee flexion, so a "
          "demonstration that goes past 90 degrees is normal."]]),
]

doc = new_doc()
doc.add_heading("ExerciseMenu — 3 GIF Fixes, Applied and Sourced", level=0)
doc.add_paragraph("These are the three fixes that survived the re-check. Each one is already written out in final "
                  "form below: open the page, go to the box named in the left column, and replace what is there with "
                  "the text on the right. Nothing else on these pages changes. All three pages are LIVE.")
p = doc.add_paragraph()
r = p.add_run("Every change below is backed by a named source that was opened and read, and the exact supporting "
              "line from that source is printed with it so you can check it yourself.")
r.bold = True
small(doc, "How each GIF was checked: the real animation was downloaded from your Media Library (30 frames at 100 ms), "
           "every frame was stepped through, and the start, middle and end positions were enlarged. Position claims "
           "were checked against vertical reference lines drawn over the frames rather than by eye. "
           "Character and word counts were measured after the edit, and the build check that enforces the 320-character "
           "and 60-word Quick Answer limits passes on all three pages.")

for i, pg in enumerate(PAGES, 1):
    doc.add_page_break() if i > 1 else None
    doc.add_heading(f"{i}. {pg['n']}", level=1)
    grid(doc, ["", ""], [
        ["Page (live)", pg["url"]],
        ["GIF file", B + pg["gif"]],
        ["What the GIF does", pg["gifsaw"]],
        ["What was wrong", pg["wrong"]],
        ["Source", pg["src"]],
        ["Why this wording", pg["why"]],
    ], (108, 392), "EDEDEA")
    doc.add_heading("Paste this in", level=2)
    grid(doc, ["Plugin section / box", "New text"], pg["rows"], (150, 350))

doc.add_page_break()
doc.add_heading("One thing stated plainly", level=1)
doc.add_paragraph("The leg press rule 'stop where your hips and lower back stay flat on the pad' is standard coaching "
                  "practice, not a research finding. I searched for a peer-reviewed or ACE source for it and found "
                  "only coaching blogs, so the page states it as a practical limit and does not dress it up as evidence. "
                  "The 120-degree range of motion figure in Tip 2 IS from the peer-reviewed review above.")
doc.add_heading("Withdrawn earlier — do not act on these", level=1)
grid(doc, ["Exercise", "What I had claimed", "Why it was dropped"], [
 ["Barbell Incline Bench Press", "The bench looked steeper than 30 degrees, close to 45.",
  "Side by side at the same scale with your dumbbell incline GIF, the two benches look about the same, and a 3-D "
  "render in perspective cannot be measured from pixels. Nothing to change."],
 ["Barbell Hip Thrust", "The demonstration used a bare bar with no pad.",
  "Wrong. Enlarging the hip area shows a thick black barbell pad in every frame. Step 1 is correct as written."],
 ["Seated Cable Row", "The torso finished 10 to 15 degrees past vertical.",
  "Overstated. Against vertical reference lines the torso finishes upright or only just past it, which is close "
  "enough to what the page already says."],
], (110, 170, 220), "F6D9D9")

out = os.path.join(HERE, "ExerciseMenu-3-GIF-Fixes-Applied.docx")
doc.save(out); print("saved", out)
