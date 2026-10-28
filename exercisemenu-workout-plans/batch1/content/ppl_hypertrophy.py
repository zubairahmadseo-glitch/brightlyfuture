from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 12,
    "slug": "ppl-hypertrophy-program",
    "title": "6-Day PPL Hypertrophy Program for Advanced Lifters",
    "meta_title": "6-Day PPL Hypertrophy Program (Advanced Lifters)",
    "meta_desc": "An advanced 6-day PPL hypertrophy program: 13–18 sets per major muscle, a 6-week mesocycle, drop sets and rest-pause with purpose, and specialization.",
    "focus_kw": "ppl hypertrophy program",
    "badge": "Advanced · 6 Days",
    "hero_lead": "For lifters who have run push pull legs before and still want more size. This PPL hypertrophy program raises weekly volume, uses intensity techniques only where they save time, and runs in 6-week blocks with a built-in specialization option.",
    "hero_meta": ["📅 6 days/week", "⏱ 50–65 min", "📊 Advanced (2+ years)", "🏋️ Full gym"],
    "stats": [("6", "Training days"), ("13–18", "Sets/major muscle/wk"), ("6 wk", "Mesocycle"), ("2×", "Frequency/muscle"), ("34", "Exercises")],
    "quick_answer": "This PPL hypertrophy program runs Push, Pull, Legs twice a week with different exercises on the A and B days. Every session targets muscle growth with mostly 8–15 rep sets taken 0–2 reps from failure. Weeks 1–5 build effort and volume, drop sets and rest-pause appear in weeks 3–5, and week 6 is a deload.",
    "intro": f"<p>Many push pull legs programs mix strength and size work, which suits intermediate lifters. After two or more years of training, though, many lifters want a block that chases growth only: more sets, closer to failure, with tighter control over fatigue.</p><p>This advanced 6-day plan does that. If you are still building your base, our standard {L('/workout-plans/push-pull-legs/', 'push pull legs workout plan')} with heavy and volume days is the better fit.</p>",
    "sections": [
        ("who", "Who This Advanced PPL Program Is For", f"""
<ul>
<li>You have 2+ years of consistent, logged training and have already run a PPL or upper/lower split.</li>
<li>You can recover from six sessions a week: 7+ hours of sleep, enough food, manageable stress.</li>
<li>Your main goal is muscle size, and you accept slower strength progress during this block.</li>
<li>You can judge reps in reserve accurately (within about 1–2 reps). The {L('/rpe-vs-rir/', 'RPE vs RIR guide')} helps you calibrate.</li>
</ul>
{box("warn", "⚠️ Not a fix for stalled progress", "<p>If you have stopped growing on a moderate-volume plan, check sleep, calorie intake and effort before adding volume. Adding sets on top of poor recovery usually makes things worse.</p>")}
"""),
        ("schedule", "Weekly Schedule", f"""
{WEEK}
<p>Sunday is the only full rest day, so keep it free of hard conditioning. If six days in a row is too much, use the rolling option: Push A, Pull A, Legs A, Rest, Push B, Pull B, Legs B, Rest. That spreads the six sessions over eight days.</p>
"""),
        ("mesocycle", "The 6-Week Block", f"""
{table(["Week", "Volume", "Effort", "Intensity techniques"], [
    ["1", "Base sets", "RIR 3", "None"],
    ["2", "Base sets", "RIR 2", "None"],
    ["3", "+1 set on the first exercise of each day", "RIR 1–2", "On marked exercises (last set only)"],
    ["4", "Same as week 3", "RIR 1", "On marked exercises"],
    ["5", "Same as week 3", "RIR 0–1 on isolation", "On marked exercises"],
    ["6", "Half of base sets", "RIR 3–4", "None (deload)"],
])}
<p>This matches how many strength and physique athletes deload. A {cite('delphi2023', 'Delphi consensus')} defined deloading as a planned reduction in training stress to manage fatigue and boost readiness, and a {cite('deload2024', 'survey of physique athletes')} found deloads came about every 5–6 weeks and lasted about a week. See the {L('/what-is-a-deload-week/', 'deload week guide')} for more.</p>
"""),
        ("workouts", "The PPL Hypertrophy Workouts", f"""
<p>Select a day. Base sets are shown; follow the weekly effort target from the block table. "Last set" notes tell you which exercises get a drop set or rest-pause set in weeks 3–5.</p>
{TABS}
"""),
        ("techniques", "Drop Sets and Rest-Pause: How and Why", f"""
<p>Intensity techniques extend a set past the point where you would normally stop. They are useful in an advanced program because they add effective reps without adding more full sets and rest periods.</p>
<ul>
<li><strong>Drop set:</strong> reach the target RIR, cut the weight by 20–30%, and continue to about 1 rep from failure. One drop is enough. Learn the method in {L('/what-is-a-drop-set-and-how-does-it-work/', 'what a drop set is')}.</li>
<li><strong>Rest-pause:</strong> reach the target, rack the weight for 15–20 breaths, then do as many clean reps as you can, repeated twice. Read the full method in {L('/what-are-rest-pause-sets/', 'what rest-pause sets are')}.</li>
</ul>
{box("science", "🔬 What the evidence shows", f"<p>A {cite('dropset2026', '2026 meta-analysis of 12 studies')} found drop sets produced similar long-term muscle growth and strength to traditional sets, while feeling harder in the moment. A {cite('advanced2026', '2026 review of advanced training systems')} found most systems matched traditional training for growth when volume and effort were equal, with a modest edge for rest-pause. In other words, these techniques save time; they do not replace volume and progression.</p>")}
<p>Use them only on machine, cable and dumbbell isolation work, never on squats, deadlifts or barbell presses.</p>
"""),
        ("volume", "Weekly Volume (Base Weeks)", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "14", "–", "14"],
    ["Back (lats & mid-back)", "16", "–", "16"],
    ["Side delts", "10", "Shoulder press 3 → 1.5", "≈ 11.5"],
    ["Rear delts", "6", "Rows 8 → 4", "≈ 10"],
    ["Quads", "13", "–", "13"],
    ["Hamstrings", "9", "Hip thrust, back extension 5 → 2.5", "≈ 11.5"],
    ["Glutes", "3", "Squats, hinges, lunges 13 → 6.5", "≈ 9.5"],
    ["Biceps", "10", "Pulls & rows 16 → 8", "≈ 18"],
    ["Triceps", "8", "Presses & dips 12 → 6", "≈ 14"],
    ["Calves", "8", "–", "8"],
])}
<p>Weeks 3–5 add one set to each day's first exercise. The {cite('pelland2026', 'Pelland 2026 meta-regression')} found growth keeps rising with volume but with diminishing returns, and the {cite('vol2019', 'Schoenfeld 2019 trial')} in trained men found the highest-volume group grew the most. That is why this advanced plan uses higher volumes, and why each extra set should be earned by good recovery. The {L('/training-volume-calculator/', 'training volume calculator')} helps track your totals.</p>
"""),
        ("specialization", "Specialization: Bringing Up a Lagging Muscle", f"""
<p>Many advanced lifters do not need more volume everywhere, only for one or two lagging muscles. Each block, pick one priority muscle:</p>
<ol class="emp-steps">
<li><strong>Add 2–4 weekly sets</strong> for the priority muscle, split across its two sessions, and move its exercise earlier in the session.</li>
<li><strong>Remove 2–4 weekly sets</strong> from a muscle that is already ahead, so total fatigue stays similar.</li>
<li><strong>Keep it for the full 6-week block,</strong> then reassess with photos and measurements.</li>
</ol>
<p>Example: for side delts, add 2 sets of lateral raises on Pull A and Pull B, and cut 2 sets of chest work from Push B.</p>
"""),
        ("progression", "Progression and Recovery Checks", f"""
<p>Use double progression on every exercise: add reps at the same load until all sets reach the top of the range at the week's RIR, then add the smallest load jump. This is the same principle behind any {L('/what-is-progressive-overload/', 'progressive overload')} plan, applied with tighter effort targets.</p>
{table(["Check", "Green light", "Red flag → action"], [
    ["Logbook", "Reps or load up week to week", "Down two sessions in a row → deload now"],
    ["Joints", "Normal soreness", "Pain that lasts into the next session → swap the exercise"],
    ["Sleep", "7+ hours, falling asleep easily", "Restless for a week → drop week-3 extra sets"],
])}
<p>Eat enough to support the volume: about 1.6–2.2 g/kg of protein per day, which covers the point where gains plateaued in a {cite('protein2018', 'meta-analysis of 49 trials')}, and calories at or slightly above maintenance. Running this plan in a deep calorie deficit is a poor match for its volume.</p>
"""),
    ],
    "schedule": [("Mon", "Push A", "c1"), ("Tue", "Pull A", "c2"), ("Wed", "Legs A", "c3"), ("Thu", "Push B", "c4"), ("Fri", "Pull B", "c5"), ("Sat", "Legs B", "c6"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Push A", "title": "Day 1 — Push A", "tag": "Chest · Delts · Triceps", "color": 1, "time": "50–60 min", "focus": "Chest / Shoulders / Triceps",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 6–10", "2–3 min", "RIR 1–2"),
             ("Seated Dumbbell Shoulder Press", "Primary: front delts · Secondary: triceps", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Low-to-High Cable Fly", "Primary: upper chest", "3 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Cable Lateral Raise", "Primary: side delts", "5 × 12–20", "45–60 sec", "RIR 0–1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–15", "60–90 sec", "RIR 0–1"),
         ],
         "notes": "Weeks 3–5: drop set on the last cable fly set; rest-pause on the last lateral raise set."},
        {"tab": "Day 2", "tab_sub": "Pull A", "title": "Day 2 — Pull A", "tag": "Back · Rear delts · Biceps", "color": 2, "time": "50–60 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Weighted Pull-Up (or Lat Pulldown)", "Primary: lats · Secondary: biceps", "3 × 6–10", "2–3 min", "RIR 1–2"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, rear delts", "3 × 8–12", "2 min", "RIR 1"),
             ("Straight-Arm Cable Pulldown", "Primary: lats", "2 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Reverse Pec Deck", "Primary: rear delts", "3 × 12–20", "60 sec", "RIR 0–1"),
             ("Incline Dumbbell Curl", "Primary: biceps (long head)", "3 × 10–15", "60–90 sec", "RIR 0–1"),
             ("Hammer Curl", "Primary: brachialis", "2 × 10–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Weeks 3–5: rest-pause on the last reverse pec deck set; drop set on the last incline curl set."},
        {"tab": "Day 3", "tab_sub": "Legs A", "title": "Day 3 — Legs A", "tag": "Quad focus", "color": 3, "time": "55–65 min", "focus": "Quads / Hamstrings / Calves",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors", "3 × 6–10", "3 min", "RIR 1–2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 8–10", "2–3 min", "RIR 2"),
             ("Leg Extension", "Primary: quads", "3 × 10–15", "90 sec", "RIR 0–1"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–15", "90 sec", "RIR 0–1"),
             ("Standing Calf Raise", "Primary: calves", "4 × 10–15", "60 sec", "RIR 0–1"),
             ("Cable Crunch", "Primary: abs", "2 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Weeks 3–5: drop set on the last leg extension set; rest-pause on the last calf raise set. Keep squats and RDLs at RIR 1–2 throughout."},
        {"tab": "Day 4", "tab_sub": "Push B", "title": "Day 4 — Push B", "tag": "Chest · Delts · Triceps", "color": 4, "time": "50–60 min", "focus": "Chest / Shoulders / Triceps",
         "exercises": [
             ("Incline Barbell Bench Press", "Primary: upper chest · Secondary: front delts, triceps", "3 × 8–12", "2–3 min", "RIR 1–2"),
             ("Weighted Dip", "Primary: lower chest, triceps", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Pec Deck", "Primary: chest", "2 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "5 × 12–20", "45–60 sec", "RIR 0–1"),
             ("EZ-Bar Skull Crusher", "Primary: triceps", "3 × 10–12", "90 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 12–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Weeks 3–5: drop set on the last pec deck set and the last pushdown set. Skip dips if they cause shoulder pain; use a machine chest press instead."},
        {"tab": "Day 5", "tab_sub": "Pull B", "title": "Day 5 — Pull B", "tag": "Back · Rear delts · Biceps", "color": 5, "time": "50–60 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Barbell Row", "Primary: mid-back, lats · Secondary: rear delts", "3 × 8–10", "2–3 min", "RIR 1–2"),
             ("Lat Pulldown (neutral grip)", "Primary: lats", "3 × 10–12", "2 min", "RIR 1"),
             ("Single-Arm Cable Row", "Primary: lats, mid-back", "2 × 10–15", "90 sec", "RIR 0–1"),
             ("Face Pull", "Primary: rear delts", "3 × 12–15", "60 sec", "RIR 1"),
             ("Barbell Curl", "Primary: biceps", "3 × 8–12", "90 sec", "RIR 1"),
             ("Cable Curl", "Primary: biceps", "2 × 12–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Weeks 3–5: drop set on the last cable curl set."},
        {"tab": "Day 6", "tab_sub": "Legs B", "title": "Day 6 — Legs B", "tag": "Glute & hamstring focus", "color": 6, "time": "55–65 min", "focus": "Glutes / Hamstrings / Quads / Calves",
         "exercises": [
             ("Hack Squat", "Primary: quads", "3 × 8–12", "2–3 min", "RIR 1–2"),
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "2 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–15", "90 sec", "RIR 0–1"),
             ("45° Back Extension", "Primary: glutes, hamstrings, erectors", "2 × 10–15", "90 sec", "RIR 1"),
             ("Leg Extension", "Primary: quads", "2 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "4 × 12–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Weeks 3–5: rest-pause on the last seated calf raise set. Superset leg extensions with calf raises to save time."},
    ],
    "faq_title": "PPL Hypertrophy Program FAQ",
    "faqs": [
        ("Can I swap exercises between the A and B days?", "Yes, as long as each day keeps the same muscles and movement types, for example two chest presses and a fly on push days. Keep your swaps for the whole 6-week block so progress stays measurable."),
        ("Can intermediate lifters use this PPL hypertrophy program?", "Lifters with about a year of training can run it with the week 3–5 extra sets and intensity techniques removed. Add those back once you recover well from the base volume."),
        ("Is training 6 days a week safe for natural lifters?", "Yes, for healthy lifters who sleep and eat well. Each muscle group's two direct sessions are 72 hours apart. If joints ache or lifts drop, use the rolling 8-day schedule instead."),
        ("How many blocks should I run?", "Two or three 6-week blocks back to back is a common approach. After that, a lower-volume strength block of 4–6 weeks lets you recover from the high volume while still training hard."),
        ("Should I bulk while running this program?", "A small surplus helps, about 0.25–0.5% of body weight gained per week. Advanced lifters should stay near the lower end to limit fat gain."),
        ("What if I can only train five days?", "Run the rolling schedule: the six sessions spread over eight days, with a rest day after each Legs day."),
    ],
    "related": ["push-pull-legs", "hypertrophy-program", "5-day-workout-split", "lean-bulk-workout-plan"],
    "refs": refs("delphi2023", "deload2024", "dropset2026", "advanced2026", "pelland2026", "vol2019", "protein2018"),
    "disclaimer": DISCLAIMER,
}
