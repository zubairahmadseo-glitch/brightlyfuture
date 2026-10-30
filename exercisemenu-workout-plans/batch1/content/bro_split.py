from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 5,
    "slug": "bro-split",
    "title": "Bro Split Workout Plan: The 5-Day Bodybuilding Routine",
    "meta_title": "Bro Split Workout Plan: Free 5-Day Routine (Sets & Reps)",
    "meta_desc": "A 5-day bro split workout plan: chest, back, shoulders, legs and arms days with every set, rep and rest time, plus weekly volume and progression rules.",
    "focus_kw": "bro split workout plan",
    "badge": "Classic Bodybuilding Split",
    "hero_lead": "One muscle group per day, five days a week. This bro split workout plan keeps the focused, high-pump sessions bodybuilders love and fixes the classic weak spot: too little weekly volume for some muscles.",
    "hero_meta": ["📅 5 days/week", "⏱ 55–75 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("5", "Training days"), ("30", "Exercises"), ("9–16", "Sets/major muscle/wk"), ("8 wk", "Block length"), ("1×", "Direct hits/muscle")],
    "quick_answer": "A bro split trains one main muscle group per session: chest Monday, back Tuesday, shoulders Wednesday, legs Thursday and arms Friday. Each muscle gets one hard, high-volume session plus indirect work from the other days. It suits intermediate lifters who can train five days a week.",
    "intro": "<p>Use the day tabs to see each workout. Weekly sets, progression, deloads and FAQs follow the workouts.</p>",
    "sections": [
        ("schedule", "Bro Split Schedule: The Weekly Layout", f"""
<p>The plan runs Monday to Friday with the weekend off. The order is built around overlap: muscles that assist on one day (triceps on chest day, biceps on back day) get at least 48 hours before their own session.</p>
{WEEK}
{table(["Day", "Main target", "Also trained indirectly"], [
    ["Mon – Chest", "Pecs", "Front delts, triceps"],
    ["Tue – Back", "Lats, mid-back, rear delts", "Biceps, forearms"],
    ["Wed – Shoulders", "Side, rear and front delts, upper traps", "Triceps"],
    ["Thu – Legs", "Quads, hamstrings, glutes, calves", "Lower back, core"],
    ["Fri – Arms", "Biceps, triceps", "Forearms, calves (second session)"],
])}
<p>If you need a different start day, keep the sequence and keep two rest days in the week. You can also place one rest day after legs (Mon, Tue, Wed, Thu, Sat) if Thursday legs leaves you too sore for Friday arms. The {L('/how-to-create-a-weekly-workout-schedule/', 'weekly workout schedule guide')} shows how to fit training around work shifts.</p>
"""),
        ("workouts", "The 5-Day Bro Split Workouts", f"""
<p>Pick a day below to see the full session. Each workout opens with a heavy compound lift in the 6–10 rep range, then moves to machine, cable and dumbbell work in the 10–15 range where you can train close to failure with less joint stress.</p>
<p><strong>How to read "Effort":</strong> RIR means reps in reserve. RIR 1–2 means you stop each set with one or two good reps left. If the scale is new to you, read the {L('/rpe-vs-rir/', 'RPE vs RIR guide')} first.</p>
{TABS}
{box("science", "🔬 Why the rest periods differ", f"<p>In a study of trained men, {cite('rest2016', '3-minute rests produced more strength and quad growth than 1-minute rests')} on the same program. A {cite('restsys2017', 'systematic review')} concluded both short and long rests can build muscle, with a possible edge for longer rests in trained lifters. That is why the heavy compound lifts here use 2–3 minutes and the isolation work uses 60–90 seconds.</p>")}
"""),
        ("volume", "Weekly Sets per Muscle", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "13", "Close-grip bench 3 → 1.5", "≈ 14.5"],
    ["Lats & mid-back", "14", "–", "14"],
    ["Side delts", "7", "Shoulder press 4 → 2", "≈ 9"],
    ["Rear delts", "6", "Rows 7 → 3.5", "≈ 9.5"],
    ["Front delts", "4", "Chest pressing 10 → 5", "≈ 9"],
    ["Biceps", "9", "Pulls & rows 11 → 5.5", "≈ 14.5"],
    ["Triceps", "9", "Chest & shoulder presses 14 → 7", "≈ 16"],
    ["Quads", "10", "–", "10"],
    ["Hamstrings", "8", "Back extension 3 → 1.5", "≈ 9.5"],
    ["Calves", "7 (2 sessions)", "–", "7"],
])}
<p>Indirect sets count as half, the method that best fit the data in the {cite('pelland2026', 'Pelland 2026 meta-regression')}. The {cite('acsm2026', '2026 ACSM position stand')} links hypertrophy with 10 or more sets per muscle per week, and {cite('vol2017', 'growth kept rising with more sets')} in an earlier meta-analysis. To bring up delts, hamstrings or calves, add two sets to their session rather than a sixth day; piling 20+ sets for one muscle into a single session mostly adds tired, low-quality sets. See {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group')} for more.</p>
"""),
        ("progression", "How to Progress: Double Progression", f"""
<p>Stay at one weight until every set reaches the top of the rep range at the listed RIR, then add the smallest jump available (2.5 kg on barbells, 1–2 kg per dumbbell) and work back up. Example, bench press 4 × 6–8 at 80 kg: week 2 = 8, 7, 7, 6; week 3 = 8, 8, 7, 7; week 4 = 8, 8, 8, 8 → add 2.5 kg. The {cite('acsm2009', 'ACSM progression guidelines')} suggest a 2–10% load increase once you can do one or two reps beyond the target. Start week 1 with about 3 reps in reserve, and log every set. Isolation moves progress more slowly; adding reps at the same dumbbell still counts. More in {L('/what-is-progressive-overload/', 'what is progressive overload')}.</p>
"""),
        ("deload", "Deload Protocol", f"""
<p>Plan a lighter week after week 7, then start a new 8-week block with slightly heavier starting weights. Deload earlier if your main lifts drop two sessions in a row, joints ache, or sleep and motivation slide.</p>
<p>In a {cite('deload2024', 'survey of strength and physique athletes')}, deloads lasted about a week and were taken every 5–6 weeks on average, mostly by cutting sets and reps while keeping the same training days. This plan follows that pattern:</p>
<ul>
<li>Keep the same five days and exercises.</li>
<li>Cut working sets roughly in half (4 sets → 2, 3 sets → 1–2).</li>
<li>Keep loads about the same or slightly lighter, and stop every set at RIR 3–4.</li>
</ul>
<p>More detail on timing is in the {L('/what-is-a-deload-week/', 'deload week guide')}.</p>
"""),
        ("warmup", "Warm-Up", f"""
<p>Do 5 minutes of easy cardio, then 2–3 ramp-up sets of the first exercise: an empty bar or light load for 8–10 reps, about 60% of your working weight for 5 reps, then about 80% for 2–3 reps. Later exercises need only one lighter feeder set.</p>
"""),
        ("nutrition", "What to Eat on a Bro Split", f"""
<p>Two numbers matter most. Eat about 1.6 g of protein per kg of body weight daily: muscle gains from protein plateaued near 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}. If you want to add size, eat slightly above maintenance; a {cite('offseason2019', 'bodybuilding nutrition review')} suggests a 10–20% surplus with a gain of about 0.25–0.5% of body weight per week. Get your protein target from the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
        ("mistakes", "Common Bro Split Mistakes", f"""
<ul>
<li><strong>Treating legs as optional.</strong> Thursday is the only direct quad and hamstring session.</li>
<li><strong>Training everything to failure.</strong> A {cite('failure2023', '2023 meta-analysis')} found little extra growth from failure versus stopping just short. Save it for the last set of isolation moves.</li>
<li><strong>Too many exercises.</strong> Seven or eight per muscle adds {L('/what-is-junk-volume/', 'junk volume')} and pushes sessions past 90 minutes.</li>
<li><strong>No log.</strong> Without written numbers there is no progression, only pump sessions.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Chest", "c1"), ("Tue", "Back", "c2"), ("Wed", "Shoulders", "c5"), ("Thu", "Legs", "c3"), ("Fri", "Arms", "c4"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Chest", "title": "Day 1: Chest & Abs", "tag": "Push focus", "color": 1, "time": "55–65 min", "focus": "Chest / Abs",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "4 × 6–8", "2–3 min", "RIR 1–2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Weighted Dip (or Assisted Dip)", "Primary: lower chest · Secondary: triceps", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Cable Fly (high to low)", "Primary: chest (stretch focus)", "3 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Cable Crunch", "Primary: abs", "3 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Lean forward slightly on dips to bias the chest. If dips bother your shoulders, use the decline dumbbell press. On cable flyes, pause for a second in the stretched position."},
        {"tab": "Day 2", "tab_sub": "Back", "title": "Day 2: Back & Rear Delts", "tag": "Pull focus", "color": 2, "time": "60–70 min", "focus": "Lats / Mid-back / Rear delts",
         "exercises": [
             ("Pull-Up (weighted or assisted)", "Primary: lats · Secondary: biceps", "4 × 6–10", "2–3 min", "RIR 1–2"),
             ("Barbell Row", "Primary: mid-back, lats · Secondary: rear delts, biceps", "4 × 6–8", "2–3 min", "RIR 2"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, rear delts", "3 × 10–12", "90 sec", "RIR 1"),
             ("Straight-Arm Cable Pulldown", "Primary: lats", "3 × 12–15", "60–90 sec", "RIR 1"),
             ("Face Pull", "Primary: rear delts · Secondary: rotator cuff", "3 × 12–15", "60 sec", "RIR 1"),
             ("45° Back Extension", "Primary: spinal erectors · Secondary: glutes, hamstrings", "3 × 10–12", "90 sec", "RIR 2"),
         ],
         "notes": "Swap pull-ups for lat pulldowns if you cannot complete 6 strict reps. Keep the barbell row torso at about 45° and avoid jerking the weight up."},
        {"tab": "Day 3", "tab_sub": "Shoulders", "title": "Day 3: Shoulders & Traps", "tag": "Delt focus", "color": 5, "time": "50–60 min", "focus": "Delts / Traps / Abs",
         "exercises": [
             ("Seated Dumbbell Shoulder Press", "Primary: front delts · Secondary: side delts, triceps", "4 × 6–10", "2–3 min", "RIR 1–2"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "4 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Cable Lateral Raise (single arm)", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Reverse Pec Deck", "Primary: rear delts", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Dumbbell Shrug", "Primary: upper traps", "3 × 10–12", "60–90 sec", "RIR 1"),
             ("Hanging Knee Raise", "Primary: abs, hip flexors", "3 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Keep lateral raises strict and controlled. If you have to swing the dumbbells up, the weight is too heavy."},
        {"tab": "Day 4", "tab_sub": "Legs", "title": "Day 4: Legs", "tag": "Priority day", "color": 3, "time": "65–75 min", "focus": "Quads / Hamstrings / Glutes / Calves",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors", "4 × 6–8", "3 min", "RIR 2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "4 × 8–10", "2–3 min", "RIR 2"),
             ("Leg Press", "Primary: quads · Secondary: glutes", "3 × 10–12", "2 min", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "4 × 10–12", "90 sec", "RIR 1"),
             ("Leg Extension", "Primary: quads", "3 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Standing Calf Raise", "Primary: calves (gastrocnemius)", "4 × 10–15", "60–90 sec", "RIR 1"),
         ],
         "notes": f"The seated leg curl is chosen over the lying version because training the hamstrings at longer lengths produced more growth in a {cite('maeo2021', 'controlled trial')}. Pause 1–2 seconds at the bottom of each calf raise."},
        {"tab": "Day 5", "tab_sub": "Arms", "title": "Day 5: Arms & Calves", "tag": "Arm focus", "color": 4, "time": "55–65 min", "focus": "Biceps / Triceps / Calves",
         "exercises": [
             ("Close-Grip Bench Press", "Primary: triceps · Secondary: chest", "3 × 6–10", "2–3 min", "RIR 2"),
             ("Barbell Curl", "Primary: biceps", "3 × 8–10", "90 sec", "RIR 1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–12", "90 sec", "RIR 1"),
             ("Incline Dumbbell Curl", "Primary: biceps (long head)", "3 × 10–12", "60–90 sec", "RIR 1"),
             ("Hammer Curl", "Primary: brachialis, brachioradialis", "3 × 10–12", "60 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Pair biceps and triceps moves as supersets (e.g., curl then pushdown) to save time."},
    ],
    "swap_overrides": {"Barbell Bench Press": "Dumbbell Bench Press or Machine Chest Press", "Weighted Dip": "Flat or Decline Dumbbell Press",
                       "Romanian Deadlift": "Dumbbell Romanian Deadlift or 45° Back Extension", "Back Squat": "Hack Squat or Leg Press", "Barbell Back Squat": "Hack Squat or Leg Press"},
    "faq_title": "Bro Split Workout Plan FAQ",
    "faqs": [
        ("Can I do cardio on a bro split?", "Yes. Easy cardio such as walking or cycling for 20–30 minutes fits after upper-body days or on weekends. Avoid hard intervals the day before leg day so squats and Romanian deadlifts do not suffer."),
        ("Can I do a bro split at home?", "Only with enough equipment. You need adjustable dumbbells, a bench and ideally a pull-up bar and bands to replace the cable and machine moves. Without them, a full-body or upper/lower plan is easier to load properly."),
        ("Can I do a bro split in 4 days?", "You can combine shoulders and arms into one day, but that session runs long and side delts tend to get shortchanged. A 4-day schedule usually works better with a torso/limbs or upper/lower layout."),
        ("Should I train abs every day on a bro split?", "No. Abs recover like other muscles. Two or three focused sessions a week, such as the cable crunch and hanging knee raise in this plan, are enough alongside the bracing done on squats and rows."),
        ("Can women follow a bro split?", "Yes. Men and women gain muscle at similar relative rates on the same program. Women who want more glute work can add hip thrusts at the start of arm day."),
        ("What if I miss a day?", "Do the missed session the next day and push the rest of the week back by one day. Avoid skipping legs; if you must drop a session, drop arms, since biceps and triceps already get indirect work."),
    ],
    "related": ["push-pull-legs", "5-day-workout-split", "upper-lower-split", "ppl-hypertrophy-program"],
    "refs": refs("pelland2026", "acsm2026", "vol2017", "rest2016", "restsys2017", "acsm2009", "deload2024", "failure2023", "maeo2021", "protein2018", "offseason2019"),
    "disclaimer": DISCLAIMER,
}
