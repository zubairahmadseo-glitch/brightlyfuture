from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 3,
    "slug": "upper-lower-split",
    "title": "4-Day Upper Lower Split Workout Plan (With Progression)",
    "meta_title": "Upper Lower Split: Free 4-Day Workout Plan (Sets & Reps)",
    "meta_desc": "A 4-day upper lower split that trains every muscle twice a week: all 4 workouts with sets, reps and rest, a progression table and easy exercise swaps.",
    "focus_kw": "upper lower split",
    "badge": "4 Days · 2× Frequency",
    "hero_lead": "Upper body twice and lower body twice a week, with three rest days. Compound lifts come first, isolation work after, and a simple progression rule tells you when to add weight.",
    "hero_meta": ["📅 4 days/week", "⏱ 40–60 min", "📊 Beginner–Intermediate", "🏋️ Gym"],
    "stats": [("4", "Training days"), ("2×", "Frequency/muscle"), ("16", "Exercises"), ("3", "Rest days"), ("4 wk", "Progression cycle")],
    "quick_answer": "This upper lower split trains Upper A, Lower A, Upper B and Lower B each week, for example Monday, Tuesday, Thursday and Friday. Upper A leads with the bench press, Upper B with the barbell row; Lower A is squat-focused and Lower B is hip-hinge-focused. Add weight once every set reaches the top of its rep range.",
    "intro": "<p>Choose your schedule, then use the day tabs to see each workout. Progression, swaps and FAQs follow the workouts.</p>",
    "sections": [
        ("schedule", "Upper Lower Split Schedule", f"""
{WEEK}
{table(["Option", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], [
    ["A", "Upper A", "Lower A", "Rest", "Upper B", "Lower B", "Rest", "Rest"],
    ["B", "Upper A", "Rest", "Lower A", "Upper B", "Rest", "Lower B", "Rest"],
    ["C", "Rest", "Upper A", "Lower A", "Rest", "Upper B", "Lower B", "Rest"],
])}
<p>The one rule: keep at least one rest day between the two upper sessions and between the two lower sessions. Option A is the most common; option B spreads sessions out if you recover slowly. Training each muscle twice a week grew more muscle than once a week in a {cite('freq2016', '2016 meta-analysis')}.</p>
"""),
        ("workouts", "The Upper Lower Workouts", f"""
<p>Pick a day. Compound lifts use RPE 7–8 (finish with 2–3 reps left); isolation lifts use RPE 8–9 (1–2 reps left). Read the {L('/rpe-vs-rir/', 'RPE vs RIR guide')} if the scale is new to you.</p>
{TABS}
"""),
        ("progression", "How to Progress Each Week", f"""
<p>Use double progression: add reps each week within the range, then add weight once all sets reach the top. Example for a lift programmed at 4 × 6–8:</p>
{table(["Week", "Weight", "Sets × reps", "What happens"], [
    ["1", "80 kg", "4 × 6", "Start at the bottom of the range"],
    ["2", "80 kg", "4 × 7", "Add 1 rep per set"],
    ["3", "80 kg", "4 × 8", "Top of the range: increase next week"],
    ["4", "82.5 kg", "4 × 6", "Add 2.5 kg, back to the bottom"],
])}
<p>Isolation exercises follow the same system with 1–2 kg jumps. Going to failure on compound lifts adds fatigue with little extra growth; a {cite('failure2023', '2023 meta-analysis')} found only a trivial difference between training to failure and stopping short. Save near-failure sets for the last set of isolation work. More on the method: {L('/what-is-progressive-overload/', 'what is progressive overload')}.</p>
"""),
        ("volume", "Weekly Sets per Muscle", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "7", "–", "7"],
    ["Back", "10", "–", "10"],
    ["Side delts", "6", "Overhead press 3 → 1.5", "≈ 7.5"],
    ["Rear delts", "6", "Rows 4 → 2", "≈ 8"],
    ["Biceps", "4", "Pulldowns & rows 10 → 5", "≈ 9"],
    ["Triceps", "4", "Presses 10 → 5", "≈ 9"],
    ["Quads", "16", "–", "16"],
    ["Hamstrings", "10", "–", "10"],
    ["Glutes", "–", "Squats, presses, RDL, split squats 17 → 8.5", "≈ 8.5"],
    ["Calves", "8", "–", "8"],
])}
<p>Legs and back get the most work. If chest is a priority, add 2 sets of cable flyes to Upper A. See {L('/how-many-sets-per-muscle-group-per-week/', 'how many sets per muscle group per week')} before adding more.</p>
"""),
        ("deload", "Deloads and Rest Days", f"""
<p>When your main lifts stall for two sessions in a row at the same weight and reps, take a deload week: same exercises and weights, about half the sets (4 sets → 2). Then resume the progression.</p>
<p>On rest days, a 20–30 minute walk or a short mobility session is enough. Take an extra day off if joint soreness doesn't fade during your warm-up or your sleep has been poor for several nights. The {L('/rest-day-vs-active-recovery/', 'rest day vs active recovery guide')} explains the options.</p>
"""),
        ("mistakes", "Common Mistakes", f"""
<ul>
<li><strong>Skipping Lower B.</strong> It carries most of the week's hamstring work. If you must miss it, move it to the next free day.</li>
<li><strong>Adding lots of extra exercises.</strong> If you want more volume, add one set to an existing exercise instead.</li>
<li><strong>Not logging workouts.</strong> Double progression only works when you know last session's exact weights and reps.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Upper A", "c1"), ("Tue", "Lower A", "c3"), ("Wed", "Rest", "rest"), ("Thu", "Upper B", "c2"), ("Fri", "Lower B", "c6"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Upper A", "title": "Day 1: Upper A (Push Emphasis)", "tag": "Upper", "color": 1, "time": "50–60 min", "focus": "Chest / Shoulders / Back / Arms",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "4 × 6–8", "2–3 min", "RPE 7–8"),
             ("Overhead Press (Barbell)", "Primary: front & side delts · Secondary: triceps", "3 × 8–10", "2 min", "RPE 7–8"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 10–12", "90 sec", "RPE 7–8"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RPE 8–9"),
             ("Face Pull", "Primary: rear delts, rotator cuff", "3 × 15–20", "60 sec", "RPE 8–9"),
             ("Barbell Curl", "Primary: biceps", "2 × 10–12", "60 sec", "RPE 8–9"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 10–12", "60 sec", "RPE 8–9"),
         ],
         "notes": "Bench and overhead press go first while you are fresh. The pulldown keeps pulling work in balance with the pressing."},
        {"tab": "Day 2", "tab_sub": "Lower A", "title": "Day 2: Lower A (Squat Focus)", "tag": "Lower", "color": 3, "time": "45–55 min", "focus": "Quads / Hamstrings / Calves",
         "exercises": [
             ("Barbell Back Squat", "Primary: quads, glutes", "4 × 6–8", "2–3 min", "RPE 7–8"),
             ("Leg Press", "Primary: quads, glutes", "3 × 10–12", "2 min", "RPE 7–8"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–12", "90 sec", "RPE 8–9"),
             ("Leg Extension", "Primary: quads", "3 × 12–15", "60 sec", "RPE 8–9"),
             ("Standing Calf Raise", "Primary: calves", "4 × 12–15", "60 sec", "RPE 8–9"),
         ],
         "notes": f"The leg press adds quad work without loading your spine a second time. Seated leg curls built more hamstring muscle than lying curls in a {cite('maeo2021', 'controlled trial')}."},
        {"tab": "Day 3", "tab_sub": "Upper B", "title": "Day 3: Upper B (Pull Emphasis)", "tag": "Upper", "color": 2, "time": "50–60 min", "focus": "Back / Chest / Shoulders / Arms",
         "exercises": [
             ("Barbell Bent-Over Row", "Primary: lats, mid-back · Secondary: rear delts, biceps", "4 × 6–8", "2–3 min", "RPE 7–8"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 8–10", "2 min", "RPE 7–8"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts, triceps", "3 × 8–12", "2 min", "RPE 7–8"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RPE 8–9"),
             ("Face Pull", "Primary: rear delts", "3 × 15–20", "60 sec", "RPE 8–9"),
             ("Barbell Curl", "Primary: biceps", "2 × 10–12", "60 sec", "RPE 8–9"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 10–12", "60 sec", "RPE 8–9"),
         ],
         "notes": "The row leads today because grip and lower-back fatigue would hold it back later in the session. The incline press gives your chest its second session of the week."},
        {"tab": "Day 4", "tab_sub": "Lower B", "title": "Day 4: Lower B (Hip-Hinge Focus)", "tag": "Lower", "color": 6, "time": "45–55 min", "focus": "Hamstrings / Glutes / Quads / Calves",
         "exercises": [
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "4 × 8–10", "2–3 min", "RPE 7–8"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "3 × 8–10 / leg", "90 sec", "RPE 7–8"),
             ("Leg Press", "Primary: quads", "3 × 12–15", "90 sec", "RPE 8"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–12", "60 sec", "RPE 8–9"),
             ("Standing Calf Raise", "Primary: calves", "4 × 12–15", "60 sec", "RPE 8–9"),
         ],
         "notes": "The RDL trains the hamstrings and glutes through a long stretch. Split squats train each leg on its own, so a weaker side can't hide."},
    ],
    "faq_title": "Upper Lower Split FAQ",
    "faqs": [
        ("Can beginners follow this upper lower split?", "Yes, after about 2–3 months of regular training and once you can squat, bench and row with confidence. Complete beginners usually do better with a 3-day full-body plan first."),
        ("What if I can only train three days this week?", "Run Upper A, Lower A and Upper B, then start next week with Lower B. Every workout still gets done over two weeks. If three days is your normal schedule, a full-body plan suits you better."),
        ("Can I do cardio with this plan?", "Yes. Easy cardio on rest days or after upper sessions works well. Keep hard intervals away from the day before a lower session."),
        ("When should I switch to a different program?", "Run it for at least 12 weeks. Switch when progress stalls for 3+ weeks despite a deload, when your goals change, or when you can train 5–6 days a week."),
    ],
    "related": ["full-body-workout-plan", "4-day-workout-split", "push-pull-legs", "hypertrophy-program"],
    "refs": refs("freq2016", "failure2023", "maeo2021"),
    "disclaimer": DISCLAIMER,
}
