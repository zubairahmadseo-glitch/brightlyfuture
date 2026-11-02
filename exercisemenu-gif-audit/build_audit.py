"""Build the GIF-vs-content audit: every media-library GIF played frame by frame, section-wise fixes."""
import os
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
B = "https://exercisemenu.com/wp-content/uploads/2026/10/"

def shade(cell, hexc):
    pr = cell._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexc); pr.append(sh)

def new_doc():
    d = Document(); s = d.styles["Normal"]; s.font.name = "Calibri"; s.font.size = Pt(10.5)
    for sec in d.sections:
        sec.left_margin = sec.right_margin = Pt(50); sec.top_margin = sec.bottom_margin = Pt(46)
    return d

def grid(doc, header, rows, widths, head_fill="D9E2F3"):
    t = doc.add_table(rows=0, cols=len(header)); t.style = "Table Grid"; t.autofit = False
    for i, row in enumerate([header] + rows):
        cells = t.add_row().cells
        for j, val in enumerate(row):
            cells[j].text = str(val); cells[j].width = Pt(widths[j])
            if i == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], head_fill)
            elif j == 0:
                for r in cells[j].paragraphs[0].runs: r.bold = True
                shade(cells[j], "F3F2F0")
    doc.add_paragraph()

def small(doc, text, italic=True):
    p = doc.add_paragraph(); r = p.add_run(text); r.italic = italic
    r.font.color.rgb = RGBColor(0x5f, 0x5c, 0x55); r.font.size = Pt(9.5)

# ---------------------------------------------------------------- data
FIXES = [
 dict(name="Barbell Lying Triceps Extension", gif="Barbell-Lying-Triceps-Extension.gif",
   page="/exercises/barbell-lying-triceps-extension/   — LIVE",
   saw="The upper arms stay vertical the whole time, which the page already says. But at the bottom the bar "
       "travels past the forehead and finishes just over the top of the head, rather than stopping above the forehead.",
   verdict="Wording fix in 5 places so the steps describe the arc the GIF actually shows. FAQ 4 already says "
           "both versions of this lift exist, so leave that one alone.",
   rows=[["How-To Steps, Step 4 Title", "Lower toward your forehead", "Lower past your forehead"],
         ["How-To Steps, Step 4 Description",
          "Bend your elbows to lower the bar slowly in an arc toward your forehead, stopping just above it.",
          "Bend your elbows to lower the bar slowly in an arc past your forehead until it is just above the top "
          "of your head, as the demonstration shows. Keep your upper arms vertical the whole way."],
         ["Common Mistakes, Mistake 4",
          "Dropping the Bar Fast: Letting the bar fall toward your head is unsafe. Control every rep and stop just above the forehead.",
          "Dropping the Bar Fast: Letting the bar fall toward your head is unsafe. Control every rep and never let the bar touch your head."],
         ["GIF / Media, GIF Alt Text",
          "Barbell lying triceps extension exercise demonstration lowering the bar toward the forehead",
          "Barbell lying triceps extension exercise demonstration lowering the bar past the forehead"],
         ["Quick Answer (AEO)",
          "and bend only at the elbows to lower it toward your forehead. Press back up.",
          "and bend only at the elbows to lower it past your forehead to just above your head. Press back up."]]),

 dict(name="Cable Kneeling Crunch", gif="Cable-Kneeling-Crunch.gif",
   page="/exercises/cable-kneeling-crunch/   — LIVE",
   saw="Kneeling with the back to the machine and the hands beside the head, both correct. But at the bottom the "
       "hips clearly travel back toward the heels as the body folds into a ball. They do not stay over the knees. "
       "Checked against vertical reference lines drawn over the frames, not by eye alone.",
   verdict="The page calls that a mistake, so the GIF and the text contradict each other in 5 places. The real "
           "fault is folding at the hips with a FLAT back; some hip travel while the spine rounds is normal.",
   rows=[["Quick Answer (AEO)",
          "Hold a rope beside your head, keep your hips still, and curl your ribs toward your hips by rounding your spine.",
          "Hold a rope beside your head and curl your ribs toward your hips by rounding your spine, not by folding at the hips."],
         ["Rank Math SEO, Description",
          "How to do the cable kneeling crunch with your hips still and your spine doing the work. Muscles worked, sets and reps, common mistakes, and FAQs.",
          "How to do the cable kneeling crunch so your spine does the work, not your hips. Muscles worked, sets and reps, common mistakes, and FAQs."],
         ["How-To Steps, Step 4 Description",
          "Breathe out and round your spine, pulling your ribs toward your hips and your elbows toward your thighs. Your hips stay where they are.",
          "Breathe out and round your spine, pulling your ribs toward your hips and your elbows toward your thighs. "
          "Your hips will settle back a little as you fold, which is fine - what matters is that your spine rounds."],
         ["Common Mistakes, Mistake 1",
          "Moving the Hips: Sitting back toward your heels or pushing the hips back turns the crunch into a hip hinge and takes work away from the abs. Keep your hips over your knees.",
          "Folding at the Hips With a Flat Back: If your back stays straight and you just bend forward at the hips, "
          "the abs do little. Round your spine on every rep instead."],
         ["FAQs, Answer 3",
          "Most often the hips are moving. Keep your hips still over your knees and lighten the weight until the movement comes from your spine.",
          "Most often the back is staying flat and the movement is coming from the hips. Lighten the weight and curl "
          "your ribs toward your hips so the spine rounds."]]),

 dict(name="Leg Press (45-degree sled)", gif="Sled-45%C2%B0-Leg-Press-Hips.gif",
   page="/exercises/leg-press/   — LIVE",
   saw="Feet in the middle of the platform at about hip width, which the page gets right. The depth is deeper than "
       "the page says: the knees bend well past 90 degrees and the thighs come close to the torso, while the hips "
       "and lower back stay flat on the pad.",
   verdict="Lead with the real limit (hips and back on the pad) instead of the 90-degree number. FAQ 1 already "
           "says '90 degrees or a little more', so that one is fine as it stands.",
   rows=[["Quick Answer (AEO)",
          "lower the sled until your knees bend to about 90 degrees without your hips lifting, then press back up without locking your knees.",
          "lower the sled as far as you can while your hips and lower back stay flat on the pad, then press back up without locking your knees."],
         ["How-To Steps, Step 4 Description",
          "Bend your knees to lower the sled toward your chest until your knees reach about 90 degrees, or as deep as you can while your hips and lower back stay on the pad.",
          "Bend your knees to lower the sled toward your chest as far as you can while your hips and lower back stay "
          "flat on the pad. The demonstration goes past 90 degrees of knee bend; stop sooner if your hips start to curl up."]]),
]

WITHDRAWN = [
 ["Barbell Incline Bench Press", "Barbell-Incline-Bench-Press.gif",
  "I first wrote that the bench looked much steeper than the 30 degrees the page recommends, close to 45.",
  "Withdrawn. Putting this GIF beside your own Dumbbell-Incline-Bench-Press-Chest.gif at the same scale, the two "
  "benches look about the same, and a 3-D render in perspective cannot be measured reliably from pixels. "
  "CHANGE NOTHING on this page."],
 ["Barbell Hip Thrust", "Barbell-Hip-Thrust-Hips.gif",
  "I first wrote that the demonstration uses a bare bar with no barbell pad, so step 1 should stop saying 'padded'.",
  "Withdrawn, and this one was simply wrong. Enlarging the hip area shows a thick black barbell pad on the bar in "
  "every frame. Step 1 is correct as written. CHANGE NOTHING on this page."],
 ["Seated Cable Row", "Cable-seated-row-Back.gif",
  "I first wrote that the torso finishes 10 to 15 degrees past vertical, which made the page's 'stop when upright' "
  "cue a contradiction.",
  "Downgraded to a note. With vertical reference lines over the frames, the torso finishes upright or only just past "
  "it. That is close enough to what the page already says. The optional clarification is in Part B."],
]

NOTES = [
 dict(name="Seated Cable Row", gif="Cable-seated-row-Back.gif", page="/exercises/seated-cable-row/   — LIVE",
   saw="The start matches the page: torso leaning forward from the hips with the arms reaching. At the finish the "
       "torso comes up to upright or only just past it - checked against vertical reference lines over the frames.",
   action="No contradiction worth a rewrite. Optional, if you want the page to match the demonstration exactly - "
          "Tips, Tip 1: change the opening from 'Avoid a Backward Lean' to 'Keep the Lean Small', and in the body "
          "change 'avoiding any backward lean' to 'avoiding a backward lean'. Everything else stays."),
 dict(name="Barbell Back Squat", gif="Barbell-Full-Squat-Thighs.gif", page="/exercises/barbell-back-squat/   — LIVE",
   saw="High-bar squat on the upper traps, stance about shoulder width, toes slightly out. The demonstration squats "
       "clearly BELOW parallel — hips below the knees.",
   action="No contradiction: step 4 says 'as low as you can while your back stays neutral', and nothing on the page "
          "tells people to stop at parallel. Optional: add to Step 4 Description — 'The demonstration goes below "
          "parallel; go as deep as your own hips and back allow.'"),
 dict(name="Barbell Seated Calf Raise", gif="Barbell-Seated-Calf-Raise-Calves.gif", page="/exercises/barbell-seated-calf-raise/   — LIVE",
   saw="Seated on the end of a flat bench, knees at about 90 degrees, bar across the lower thighs. The feet are FLAT "
       "ON THE FLOOR — there is no step or plate under the forefeet.",
   action="No contradiction: Step 3 already offers both. Optional, so readers are not confused: start Step 3 with "
          "'Place your feet flat on the floor, as the demonstration shows, or...' (it already reads in that order)."),
 dict(name="Barbell Preacher Curl", gif="Barbell-Preacher-Curl-Upper-Arms.gif", page="/exercises/barbell-preacher-curl/   — LIVE",
   saw="The lifter is STANDING at the preacher station, chest against the pad, using a STRAIGHT barbell (not an EZ bar).",
   action="No contradiction: the steps never say 'sit', and Equipment already reads 'Barbell (or EZ Bar), Preacher Bench'. "
          "Optional: Step 1 Description could begin 'Standing or seated at the preacher bench, adjust it so...'."),
 dict(name="Dumbbell Lateral Raise", gif="Dumbbell-Lateral-Raise-shoulder-AFIX.gif", page="/exercises/dumbbell-lateral-raise/   — LIVE",
   saw="The dumbbells start in front of the thighs, close together, and are raised out to about shoulder height with "
       "the palms turning down. Everything else matches.",
   action="Optional precision fix. Step 1 Description: change 'holding a dumbbell in each hand at your sides' to "
          "'holding a dumbbell in each hand in front of your thighs'."),
 dict(name="Barbell Close-Grip Bench Press", gif="Barbell-Close-Grip-Bench-Press-Upper-Arms.gif", page="/exercises/barbell-close-grip-bench-press/   — LIVE",
   saw="The grip looks slightly narrower than shoulder width and the elbows stay tucked. The bar lowers to the lower chest.",
   action="No change needed. 'About shoulder-width apart' is the standard cue and is close to what the GIF shows."),
]

OK = [
 ("Barbell Bench Press", "Barbell-Bench-Press.gif", "Flat bench, feet down, grip a little wider than the shoulders, bar to mid-chest, press to lockout."),
 ("Barbell Bent-Over Row", "Barbell-Bent-Over-Row_Back-FIX.gif", "Torso bent well forward, overhand grip, bar pulled to the lower ribs, knees softly bent."),
 ("Barbell Curl", "Barbell-Curl.gif", "Shoulder-width underhand grip, elbows at the sides, bar curled to chest height."),
 ("Barbell Deadlift", "Barbell-Deadlift_Hips-FIX.gif", "Bar from the floor, hip-width stance, double overhand grip, bar close to the legs, tall lockout."),
 ("Barbell Romanian Deadlift", "Barbell-Romanian-Deadlift-Hips-FIX.gif", "Knees softly bent and fixed, hips pushed back, bar down to mid-shin, back flat."),
 ("Barbell Overhead Press", "Barbell-Standing-Shoulders-Press-Shoulder.gif", "Standing, bar from the front shoulders, pressed to lockout overhead."),
 ("Barbell Standing Calf Raise", "Barbell-Standing-CalfRaise.gif", "Bar on the upper back, balls of the feet on a plate, heels dropped then raised high."),
 ("Barbell Bulgarian Split Squat", "Barbell-Single-Leg-Split-Squat-Hips-FIX.gif", "Top of the rear foot resting on the bench, front knee bent deeply, bar on the upper traps."),
 ("Dumbbell Bench Press", "Dumbbell-Bench-Press.gif", "Flat bench, palms forward, dumbbells to the sides of the chest, pressed up in a slight arc."),
 ("Dumbbell Incline Bench Press", "Dumbbell-Incline-Bench-Press-Chest.gif", "Incline bench, dumbbells from chest level to arms extended."),
 ("Dumbbell Biceps Curl", "Dumbbell-Biceps-Curl.gif", "Both arms together, palms forward at the start, elbows at the sides."),
 ("Dumbbell Hammer Curl", "Dumbbell-Hammer-Curl.gif", "Neutral grip, one arm at a time — matches the page, which curls one then the other."),
 ("Dumbbell One-Arm Row", "Dumbbell-One-Arm-Row.gif", "Free hand braced on a rack, staggered stance with both feet down, dumbbell rowed to the hip."),
 ("Dumbbell Seated Shoulder Press", "Dumbbell-Seated-Shoulder-Press-Shoulders.gif", "Upright back pad, dumbbells from about ear height to lockout."),
 ("Dumbbell Lunge", "Dumbbell-Lunge-Hips-FIX.gif", "Steps forward into the lunge, back knee near the floor, returns to standing, then alternates."),
 ("EZ-Bar Curl", "EZ-Barbell-Curl-Upper-Arms.gif", "Angled grip on the cambered sections, elbows at the sides, curled to chest height."),
 ("Cable Lat Pulldown", "Cable-Wide-Grip-Lat-Pulldown.gif", "Thighs under the pad, wide overhand grip, bar pulled to the upper chest in front, slight lean back."),
 ("Cable Face Pull", "Cable-Standing-Face-Pull-Shoulders.gif", "Pulley at about shoulder height, elbows high, rope ends finishing beside the head."),
 ("Leg Extension", "Lever-Leg-Extension-Thighs.gif", "Knees from about 90 degrees to straight, roller above the feet, hands on the side handles."),
 ("Seated Leg Curl", "Lever-Seated-Leg-Curl-Thighs-FIX.gif", "Legs from almost straight to fully curled, roller above the heels, hands on the thigh-pad handles."),
 ("Cable Overhead Triceps Extension", "Cable-Overhead-Triceps-Extension-rope-at.gif", "Low pulley behind, hands to ear height behind the head, elbows up and forward."),
 ("Pull-Up", "Pull-up-Back.gif", "Dead hang with straight arms, overhand grip a little wider than the shoulders, chin clear of the bar."),
 ("Reverse Pec Deck Fly", "Lever-Seated-Reverse-Fly-Shoulders.gif", "Palms-down handles, arms from in front out to the shoulder line. No chest pad on this machine."),
 ("Cable Triceps Pushdown", "Cable-Pushdown-with-rope-attachment-Upp.gif", "Hands from mid-chest to the waistband, elbows pinned, hands stay together at the bottom."),
 ("Low-to-High Cable Fly", "Cable-Low-Fly-Chest.gif", "Two low pulleys, staggered stance, hands meeting in front of the chest."),
]

HOUSE = [
 ["Duplicate: Barbell Seated Calf Raise",
  "Barbell-Seated-Calf-Raise-Calves.gif and Barbell-Seated-Calf-Raise.gif are both in the library.",
  "Keep one, point the page at it, and delete the other so the Media Library stays clean."],
 ["Duplicate: Dumbbell Lateral Raise",
  "Dumbbell-Lateral-Raise-shoulder-AFIX.gif and Dumbbell-Lateral-Raise-shoulder.gif are both in the library.",
  "The live page should use the AFIX one. Delete the other if nothing links to it."],
 ["GIFs with no exercise page yet",
  "Chest-Dip-Chest.gif, Front-Plank-waist-FIX.gif, Hanging-Leg-Raise-Hips.gif",
  "These three are bought and uploaded but have no page. Say the word and I will write them next."],
 ["Not exercise GIFs",
  "back-squat.gif, front-squat.gif, high_bar_back_squat_side_view.gif, low_bar_back_squat_side_view.gif, "
  "Medicine-Ball-Overhead-Press.gif, Medicine-ball-Russian-twist-exercise.gif, Cinematic_frontangle_shot_welllit_indoor_g.gif",
  "These belong to articles, not to exercise pages, so they were not checked against exercise content."],
]

# ---------------------------------------------------------------- build
doc = new_doc()
doc.add_heading("ExerciseMenu — GIF vs Content Audit (v2, corrected)", level=0)
doc.add_paragraph("Every exercise GIF in your Media Library was downloaded and played frame by frame, then compared "
                  "with the content written for its page. Section names below are the exact box names on the Edit "
                  "Exercise screen, so you can go straight to the box and change the text.")
p = doc.add_paragraph()
r = p.add_run("This is version 2. You asked me to check my own work, so I re-opened every finding. Three of the "
              "nine I first reported did not survive that check — two were wrong and one was overstated. They are "
              "listed in Part 0 so you do not act on them. Three real fixes remain.")
r.bold = True
small(doc, "Method: 36 exercise GIFs — 29 pulled from the Media Library for this pass, plus the 7 batch-3 files played "
           "in the previous round. Each is 30 frames at 100 ms (the dumbbell lunge is 50). Frames were extracted with "
           "Python/Pillow into contact sheets; start, middle and end positions were enlarged and examined one at a "
           "time, and position claims were checked against vertical reference lines drawn over the frames. Every "
           "'Current text' line below was matched word for word against the page source before it went in this file, "
           "and every GIF link and page URL was requested live.")

doc.add_heading("What came out of it", level=1)
grid(doc, ["", "Count", "Meaning"], [
  ["Withdrawn", str(len(WITHDRAWN)), "Findings from version 1 that did not hold up. Do nothing with these. Part 0."],
  ["Fixes needed", str(len(FIXES)), "The GIF and the written content say different things. Section-wise changes in Part A."],
  ["Notes only", str(len(NOTES)), "No contradiction, but something in the GIF is worth a line on the page. Part B."],
  ["Verified, no change", str(len(OK)), "The movement, cues and positions in the GIF match the page as written. Part C."],
  ["Housekeeping", str(len(HOUSE)), "Duplicate files and GIFs with no page yet. Part D."],
], (120, 55, 345))
doc.add_paragraph("Page status: 29 of your exercise pages are already live. Only the 7 batch-3 pages (triceps "
                  "pushdown, seated leg curl, overhead triceps extension, leg extension, pull-up, reverse pec deck, "
                  "low-to-high cable fly) are not published yet. All three fixes below are on LIVE pages.")

doc.add_page_break()
doc.add_heading("Part 0 — Withdrawn from version 1", level=1)
doc.add_paragraph("If you already started on any of these, stop. Nothing on these three pages needs changing.")
grid(doc, ["Exercise", "GIF file", "What I said in v1", "What the re-check found"],
     [[n, g, a, b] for n, g, a, b in WITHDRAWN], (88, 118, 148, 148), "F6D9D9")

doc.add_page_break()
doc.add_heading("Part A — GIFs that do not match their content", level=1)
doc.add_paragraph("Each block: what the GIF shows, what to do, then the exact box to change. All three pages are live.")
for i, f in enumerate(FIXES, 1):
    doc.add_heading(f"A{i}. {f['name']}", level=2)
    grid(doc, ["", ""], [["GIF file", B + f["gif"]], ["Page", f["page"]],
                         ["What the GIF shows", f["saw"]], ["What to do", f["verdict"]]], (110, 390), "EDEDEA")
    grid(doc, ["Plugin section / box", "Current text", "Change it to"], f["rows"], (112, 194, 194))

doc.add_page_break()
doc.add_heading("Part B — Notes, no contradiction", level=1)
doc.add_paragraph("Nothing here is wrong on the page. Each one is a detail in the GIF that a reader might otherwise "
                  "wonder about, with an optional line you can add.")
for i, n in enumerate(NOTES, 1):
    doc.add_heading(f"B{i}. {n['name']}", level=2)
    grid(doc, ["", ""], [["GIF file", B + n["gif"]], ["Page", n["page"]],
                         ["What the GIF shows", n["saw"]], ["Optional change", n["action"]]], (110, 390), "EDEDEA")

doc.add_page_break()
doc.add_heading("Part C — Verified, nothing to change", level=1)
doc.add_paragraph("These were played the same way and the page text already describes what happens in the GIF. "
                  "The last seven were played in the previous round, when batch 3 was corrected.")
grid(doc, ["Exercise", "GIF file", "What the frames show"],
     [[n, g, s] for n, g, s in OK], (108, 160, 232))

doc.add_heading("Part D — Media Library housekeeping", level=1)
grid(doc, ["Item", "What is there", "What to do"], HOUSE, (112, 194, 194))

doc.add_heading("One thing outside the GIFs", level=1)
doc.add_paragraph("A missing /exercises/ URL on exercisemenu.com returns the home page with a 200 status instead of a "
                  "404. That lets Google index pages that do not exist. Worth giving your developer separately.")

out = os.path.join(HERE, "ExerciseMenu-GIF-vs-Content-Fixes.docx")
doc.save(out)
print("saved", out)
