from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 11,
    "slug": "5-day-workout-split",
    "title": "5-Day Workout Split: Upper, Lower, Push, Pull, Legs Gym Plan",
    "meta_title": "5-Day Workout Split: Upper/Lower + PPL Gym Program",
    "meta_desc": "A 5 day workout split that trains every muscle twice a week: upper, lower, push, pull and legs days with full sets, reps, rest, progression and deloads.",
    "focus_kw": "5 day workout split",
    "badge": "Hybrid Split · 5 Days",
    "hero_lead": "Most 5-day splits train each muscle once a week. This 5 day workout split combines an upper/lower pair with a push/pull/legs rotation, so every muscle gets one heavy and one higher-rep session each week.",
    "hero_meta": ["📅 5 days/week", "⏱ 55–70 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("5", "Training days"), ("2×", "Frequency/muscle"), ("11–14", "Sets/major muscle/wk"), ("8 wk", "Block length"), ("30", "Exercises")],
    "quick_answer": "This 5 day workout split runs Upper and Lower on Monday and Tuesday with heavier 5–8 rep work, rests Wednesday, then runs Push, Pull and Legs Thursday to Saturday with 8–15 rep hypertrophy work. Each muscle is trained twice a week with about 11–14 weekly sets for most major groups.",
    "takeaways": [
        "The hybrid layout gives 2× weekly frequency in five days, which a classic bro split does not.",
        "Monday and Tuesday build strength on the main lifts; Thursday to Saturday add volume for size.",
        "A rest day on Wednesday splits the week so the heavy and volume halves don't collide.",
        "Every muscle gets at least 72 hours between direct sessions.",
        "Deload in week 8, then start the next block 2.5–5% heavier on the main lifts.",
    ],
    "intro": "<p>Search \"5 day workout split\" and most results show a body-part split: chest Monday, back Tuesday and so on. That works, but it trains each muscle once a week. If you can train five days, you can do better by training each muscle twice.</p><p>This plan uses a hybrid known as ULPPL: Upper, Lower, Push, Pull, Legs. Below are the full workouts, the weekly volume per muscle, and the rules for progressing and deloading.</p>",
    "sections": [
        ("why", "Why Choose a Hybrid 5-Day Split?", f"""
<p>A {cite('freq2016', 'meta-analysis on training frequency')} found muscles trained twice a week grew more than muscles trained once. More recent work in the {cite('pelland2026', 'Pelland 2026 meta-regression')} suggests weekly volume explains most of that effect, while extra frequency still helps strength. Either way, splitting your weekly sets across two sessions keeps each session shorter and each set fresher.</p>
{table(["", "Classic 5-day bro split", "5-day hybrid (this plan)"], [
    ["Layout", "Chest · Back · Shoulders · Legs · Arms", "Upper · Lower · Push · Pull · Legs"],
    ["Direct hits per muscle", "1×", "2×"],
    ["Rep focus", "Mostly 8–12", "Heavy (5–8) + volume (8–15)"],
    ["Leg sessions per week", "1", "2"],
    ["Best for", "Bodybuilding-style lifters who like single-muscle days", "Lifters who want strength and size together"],
])}
<p>If you prefer one muscle group per day, our {L('/workout-plans/bro-split/', 'bro split workout plan')} covers that approach with the same attention to weekly volume.</p>
"""),
        ("who", "Who This 5-Day Split Is For", f"""
<ul>
<li>You have trained consistently for at least a year and know the main barbell lifts.</li>
<li>You can commit to five sessions of 55–70 minutes.</li>
<li>You want strength numbers to rise while adding size.</li>
<li>You have outgrown a 3- or 4-day program and need more weekly volume.</li>
</ul>
{box("tip", "💡 Coach's note", f"<p>Five days is a big commitment. If you regularly miss one session a week, a 4-day plan you finish beats a 5-day plan you half-finish. See {L('/how-to-create-a-weekly-workout-schedule/', 'how to create a weekly workout schedule')} for help choosing.</p>")}
"""),
        ("schedule", "The 5-Day Workout Split Schedule", f"""
{WEEK}
{table(["Day", "Focus", "Rep range", "Rest (compounds)"], [
    ["Mon – Upper", "Strength: bench, row, overhead press", "5–8", "2–3 min"],
    ["Tue – Lower", "Strength: squat, Romanian deadlift", "5–8", "3 min"],
    ["Thu – Push", "Hypertrophy: chest, delts, triceps", "8–15", "2 min"],
    ["Fri – Pull", "Hypertrophy: back, rear delts, biceps", "8–15", "2 min"],
    ["Sat – Legs", "Hypertrophy: quads, glutes, hamstrings", "8–15", "2 min"],
])}
<p>Need weekends free? You can run all five sessions Monday to Friday. Keep the order and expect slightly lower performance in Friday's legs session.</p>
"""),
        ("workouts", "The Workouts", f"""
<p>Choose a day below. Effort uses reps in reserve (RIR): stop each set with the listed number of good reps left. New to RIR? Read the {L('/rpe-vs-rir/', 'RPE vs RIR guide')}.</p>
{TABS}
{box("science", "🔬 Heavy days and volume days", f"<p>A {cite('load2021', 'network meta-analysis')} found strength rose more with heavy loads, while growth was similar across load ranges. A {cite('currier2023', 'Bayesian network meta-analysis')} ranked higher-load, multi-set training 2–3 times a week highest for both strength and size. This plan puts the heavy work early in the week, when you are freshest, and uses moderate loads for the extra volume.</p>")}
"""),
        ("volume", "Weekly Volume per Muscle", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "11", "–", "11"],
    ["Back", "14", "–", "14"],
    ["Side delts", "7", "Overhead press 3 → 1.5", "≈ 8.5"],
    ["Rear delts", "5", "Rows 8 → 4", "≈ 9"],
    ["Quads", "12", "–", "12"],
    ["Hamstrings", "9", "Hip thrust 3 → 1.5", "≈ 10.5"],
    ["Glutes", "3", "Squats, hinges, leg presses 13 → 6.5", "≈ 9.5"],
    ["Biceps", "5", "Pulls & rows 14 → 7", "≈ 12"],
    ["Triceps", "5", "Presses 12 → 6", "≈ 11"],
    ["Calves", "6", "–", "6"],
])}
<p>The {cite('acsm2026', '2026 ACSM position stand')} links greater growth with 10 or more sets per muscle per week, and a {cite('vol2017', 'dose-response meta-analysis')} showed growth rising with each added set. Most major muscles here sit at 10–14. To bring up a lagging muscle, add 2 sets on its volume day. Our {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group guide')} explains how far to push it.</p>
"""),
        ("progression", "Progression Rules", f"""
<p>Heavy days and volume days progress differently, both forms of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
{table(["Days", "Rule", "Example"], [
    ["Upper & Lower (heavy)", "When all sets hit 8 reps at RIR 2, add 2.5 kg (upper) or 5 kg (lower)", "Squat 3 × 8 at 100 kg → 105 kg × 3 × 5–6"],
    ["Push, Pull, Legs (volume)", "Double progression: add reps to the top of the range, then add the smallest load", "Incline DB press 3 × 12 at 26 kg → 28 kg"],
])}
<p>Log every set. If a heavy lift stalls for two weeks in a row, drop it 5–10% and rebuild over three weeks.</p>
"""),
        ("deload", "Deload Protocol", f"""
<p>Run weeks 1–7 as written, then deload in week 8: same five days, same exercises, about half the sets, RIR 3–4 on everything. Athletes in a {cite('deload2024', 'survey on deloading')} deloaded roughly every 5–6 weeks for about a week, mostly by reducing sets and reps. If you feel run down sooner, deload sooner. Full guidance is in the {L('/what-is-a-deload-week/', 'deload week guide')}.</p>
"""),
        ("nutrition", "Nutrition and Recovery", f"""
<p>Five sessions a week need fuel. Eat about 1.6–2.2 g of protein per kg of body weight daily; gains plateaued around 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}. To build muscle, aim for a modest surplus and a weight gain of 0.25–0.5% of body weight per week, as recommended in a {cite('offseason2019', 'review of off-season nutrition')}. Sleep 7–9 hours: five training days leave little margin for short nights. Get your number from the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
        ("mistakes", "Common 5-Day Split Mistakes", f"""
<ul>
<li><strong>Making Push, Pull and Legs heavy too.</strong> The volume days are for controlled 8–15 rep work. Grinding heavy triples there wrecks Monday and Tuesday.</li>
<li><strong>Short rests on heavy lifts.</strong> Trained lifters gained more strength with {cite('rest2018', 'rests over 2 minutes')}. Keep 2–3 minutes on Monday and Tuesday compounds.</li>
<li><strong>Skipping Saturday legs.</strong> It's the only quad and glute volume day. Move it to Sunday rather than dropping it.</li>
<li><strong>Adding a sixth day.</strong> More days rarely help when the five you have are not fully recovered.</li>
</ul>
<p>Run the plan for at least two 8-week blocks before judging it.</p>
"""),
    ],
    "schedule": [("Mon", "Upper", "c1"), ("Tue", "Lower", "c3"), ("Wed", "Rest", "rest"), ("Thu", "Push", "c4"), ("Fri", "Pull", "c2"), ("Sat", "Legs", "c6"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Upper", "title": "Day 1 — Upper (Heavy)", "tag": "Strength", "color": 1, "time": "60–70 min", "focus": "Chest / Back / Shoulders",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 5–8", "3 min", "RIR 2"),
             ("Barbell Row", "Primary: mid-back, lats · Secondary: rear delts, biceps", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Standing Overhead Press", "Primary: front delts · Secondary: triceps", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Weighted Pull-Up (or Lat Pulldown)", "Primary: lats · Secondary: biceps", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 1"),
             ("Face Pull", "Primary: rear delts · Secondary: rotator cuff", "2 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Pair lateral raises with face pulls as a superset. Ramp up on bench with 2–3 warm-up sets."},
        {"tab": "Day 2", "tab_sub": "Lower", "title": "Day 2 — Lower (Heavy)", "tag": "Strength", "color": 3, "time": "55–65 min", "focus": "Quads / Hamstrings / Glutes / Calves",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors", "3 × 5–8", "3 min", "RIR 2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Leg Press", "Primary: quads", "2 × 10–12", "2 min", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–12", "90 sec", "RIR 1"),
             ("Standing Calf Raise", "Primary: calves", "3 × 10–15", "60 sec", "RIR 1"),
             ("Hanging Knee Raise", "Primary: abs", "2 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Squat and RDL are the priority; cut the knee raises before cutting either of them."},
        {"tab": "Day 3", "tab_sub": "Push", "title": "Day 3 — Push (Volume)", "tag": "Hypertrophy", "color": 4, "time": "55–65 min", "focus": "Chest / Delts / Triceps",
         "exercises": [
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: triceps", "3 × 10–12", "2 min", "RIR 1–2"),
             ("Cable Fly", "Primary: chest", "2 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Cable Lateral Raise", "Primary: side delts", "4 × 12–20", "60 sec", "RIR 0–1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–15", "60–90 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 12–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Take 2–3 seconds to lower each press. Alternate cable lateral raise sets with triceps sets to save time."},
        {"tab": "Day 4", "tab_sub": "Pull", "title": "Day 4 — Pull (Volume)", "tag": "Hypertrophy", "color": 2, "time": "55–65 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 10–12", "2 min", "RIR 1–2"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, rear delts", "3 × 10–12", "90 sec", "RIR 1"),
             ("Single-Arm Cable Row", "Primary: lats", "2 × 10–15", "90 sec", "RIR 1"),
             ("Reverse Pec Deck", "Primary: rear delts", "3 × 12–20", "60 sec", "RIR 0–1"),
             ("Incline Dumbbell Curl", "Primary: biceps (long head)", "3 × 10–15", "60–90 sec", "RIR 1"),
             ("Hammer Curl", "Primary: brachialis", "2 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "On rows, let the shoulder blades move forward at the stretch and squeeze back at the top."},
        {"tab": "Day 5", "tab_sub": "Legs", "title": "Day 5 — Legs (Volume)", "tag": "Hypertrophy", "color": 6, "time": "60–70 min", "focus": "Quads / Glutes / Hamstrings / Calves",
         "exercises": [
             ("Hack Squat (or Leg Press)", "Primary: quads", "3 × 10–15", "2 min", "RIR 1–2"),
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "2 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 12–15", "90 sec", "RIR 0–1"),
             ("Leg Extension", "Primary: quads", "2 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Pause 1 second at the top of every hip thrust. Superset leg extensions with calf raises."},
    ],
    "faq_title": "5-Day Workout Split FAQ",
    "faqs": [
        ("Is a 5-day split good for beginners?", "Usually not. Beginners progress fastest with three full-body sessions while they learn the lifts. Move to five days after a year or more of steady training."),
        ("Which 5-day split is best for building muscle?", "Any split that gives each muscle 10 or more hard sets a week can build muscle. Hybrids like Upper/Lower/Push/Pull/Legs make that easier because each muscle is trained twice."),
        ("Can I do cardio on a 5-day split?", "Yes. Easy cardio on rest days or after upper-body sessions is fine. Keep hard intervals away from the day before a leg session."),
        ("How long should I run this 5-day split?", "Run it in 8-week blocks, including a deload week, for as long as your main lifts and body measurements keep improving."),
        ("Can I swap Upper and Lower days?", "Yes. Doing Lower on Monday and Upper on Tuesday works as long as Saturday legs stays at least 72 hours from your next leg day."),
    ],
    "related": ["bro-split", "push-pull-legs", "upper-lower-split", "ppl-hypertrophy-program"],
    "refs": refs("freq2016", "pelland2026", "load2021", "currier2023", "acsm2026", "vol2017", "deload2024", "protein2018", "offseason2019", "rest2018"),
    "disclaimer": DISCLAIMER,
}
