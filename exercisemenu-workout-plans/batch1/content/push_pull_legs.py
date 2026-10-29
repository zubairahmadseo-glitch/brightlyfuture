from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 1,
    "slug": "push-pull-legs",
    "title": "Push Pull Legs Workout Plan: The 6-Day PPL Split",
    "meta_title": "Push Pull Legs Workout Plan: Free 6-Day PPL Routine",
    "meta_desc": "Free 6-day push pull legs workout plan: heavy A days, higher-rep B days, every exercise with sets, reps and rest, plus how to add weight each week.",
    "focus_kw": "push pull legs workout plan",
    "badge": "Most Popular Plan",
    "hero_lead": "Push, pull and legs, twice a week. The A days are heavy (4–8 reps) to build strength; the B days use 8–20 reps to add muscle. Every exercise, set and rest time is below.",
    "hero_meta": ["📅 6 days/week", "⏱ 55–75 min", "📊 Intermediate–Advanced", "🏋️ Full gym"],
    "stats": [("6", "Training days"), ("2×", "Frequency/muscle"), ("14–21", "Sets/major muscle/wk"), ("8 wk", "Program length"), ("A/B", "Heavy + volume")],
    "quick_answer": "This push pull legs workout plan trains Push, Pull and Legs twice a week from Monday to Saturday, with Sunday off. Monday to Wednesday are heavy A days (4–8 reps, longer rests); Thursday to Saturday are B days (8–20 reps, shorter rests) for extra muscle-building volume.",
    "intro": "<p>Use the day tabs to see each workout. The sections after the workouts cover weekly sets, how to add weight, deloads and the most common questions.</p>",
    "sections": [
        ("schedule", "Push Pull Legs Schedule", f"""
{WEEK}
<p>Each movement pattern comes up twice a week: once heavy, once with more volume. Push days train chest, shoulders and triceps; pull days train back, rear delts and biceps; leg days train quads, hamstrings, glutes and calves. If six days in a row is too much, run Push A, Pull A, Legs A, rest, then Push B, Pull B, Legs B, rest.</p>
"""),
        ("workouts", "The Push Pull Legs Workouts", f"""
<p>Pick a day. Effort is shown as RPE: RPE 8 means you stop with about 2 good reps left, RPE 9 with 1 left. Do 2–3 warm-up sets before the first exercise of each day.</p>
{TABS}
{box("science", "🔬 Why A days rest longer", f"<p>Trained men who rested 3 minutes between sets gained more strength and quad size than those who rested 1 minute in a {cite('rest2016', '2016 study')}. That is why heavy A-day lifts use 2.5–4 minutes and B-day isolation work uses 60–90 seconds.</p>")}
"""),
        ("volume", "Weekly Sets per Muscle", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "20", "Close-grip bench 2 → 1", "≈ 21"],
    ["Back (lats & mid-back)", "20", "Deadlift 3 → 1.5", "≈ 21.5"],
    ["Side delts", "7", "Overhead & DB press 7 → 3.5", "≈ 10.5"],
    ["Rear delts", "9", "Rows 13 → 6.5", "≈ 15.5"],
    ["Biceps", "10", "Pulls & rows 20 → 10", "≈ 20"],
    ["Triceps", "8", "Presses & dips 24 → 12", "≈ 20"],
    ["Quads", "20", "–", "20"],
    ["Hamstrings", "11", "Deadlift, hip thrust 7 → 3.5", "≈ 14.5"],
    ["Glutes", "4", "Squats, hinges, lunges, leg press 21 → 10.5", "≈ 14.5"],
    ["Calves", "6", "–", "6"],
])}
<p>Direct sets count fully and indirect sets count as half, the method that best fit the data in a {cite('pelland2026', '2026 dose-response meta-regression')}. That analysis found more sets keep adding growth, but with diminishing returns, and the {cite('acsm2026', '2026 ACSM position stand')} links hypertrophy with 10 or more sets per muscle per week. Most muscles here sit well above that. If you are not recovering, remove one set from each B-day exercise first.</p>
"""),
        ("progression", "How to Add Weight: Double Progression", f"""
<p>Stay at one weight until every set reaches the top of the rep range with good form, then add the smallest jump available (usually 2.5 kg upper body, 5 kg lower body) and work back up. This is the simplest form of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
{table(["Week", "Bench press 4 × 4–6", "Next step"], [
    ["1", "80 kg × 6, 5, 5, 4", "Stay at 80 kg"],
    ["2", "80 kg × 6, 6, 5, 5", "Stay"],
    ["3", "80 kg × 6, 6, 6, 6", "Add 2.5 kg"],
    ["4", "82.5 kg × 5, 4, 4, 4", "Build back to 6s"],
])}
<p>When an isolation exercise can't go up in weight, add a rep per set first. Log every set so you know what to beat next session; the {L('/how-to-track-your-workouts/', 'workout tracking guide')} shows a simple format.</p>
"""),
        ("deload", "Deload Weeks", f"""
<p>Train hard for 3 weeks, then deload in week 4 and again in week 8. Keep the same days and exercises, cut sets roughly in half, use lighter loads and stop each set with 3–4 reps left. Strength and physique athletes in a {cite('deload2024', '2024 survey')} deloaded about every 5–6 weeks for roughly a week, so if you still feel fresh in week 4 you can train one more week first. Deload early if your lifts drop two sessions in a row. More detail is in the {L('/what-is-a-deload-week/', 'deload week guide')}.</p>
"""),
        ("who", "Who This PPL Plan Is For", f"""
<ul>
<li>At least 6–12 months of consistent lifting, with solid form on the bench press, squat, deadlift, overhead press and row.</li>
<li>Six training days a week and 55–75 minutes per session.</li>
<li>Access to a full gym: barbell, dumbbells, cables and machines.</li>
</ul>
<p>Newer lifters do better with three full-body sessions a week; start with our {L('/workout-plans/full-body-workout-plan/', 'full body workout plan for beginners')}. If you can train only four days, the {L('/workout-plans/upper-lower-split/', '4-day upper lower split')} still trains everything twice.</p>
"""),
        ("warmup", "Warm-Up", f"""
<p>Spend 3 minutes on easy cardio, 3–4 minutes on dynamic moves (arm circles, leg swings, band pull-aparts, bodyweight squats), then do ramp-up sets of your first lift: empty bar × 10, about 50% × 5, about 75% × 3. Our {L('/how-to-warm-up-before-a-workout/', 'warm-up guide')} covers each step.</p>
"""),
        ("nutrition", "What to Eat on a PPL Split", f"""
<p>Eat about 1.6 g of protein per kg of body weight daily; muscle gains plateaued near 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}. To add size, eat a little above maintenance and aim to gain about 0.25–0.5% of body weight per week, as a {cite('offseason2019', 'review of off-season nutrition')} recommends. Find your number with the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
        ("mistakes", "Common PPL Mistakes", f"""
<ul>
<li><strong>Ego lifting.</strong> If you have to swing or bounce the weight, it's too heavy for that rep range.</li>
<li><strong>Skipping face pulls.</strong> Six pressing exercises a week need rear-delt and upper-back work to balance them.</li>
<li><strong>Long cardio before lifting.</strong> Do hard cardio after lifting or on another day; see {L('/should-you-do-cardio-before-or-after-weights/', 'cardio before or after weights')}.</li>
<li><strong>Changing the plan every week.</strong> Run all 8 weeks before judging it.</li>
</ul>
"""),
        ("comparison", "PPL vs Other Splits", f"""
{table(["Split", "Days", "Frequency", "Best for"], [
    ["Push pull legs (this plan)", "6", "2×", "Intermediate lifters with 6 days"],
    ["Upper/lower", "4", "2×", "Lifters with 4 days"],
    ["Full body", "3", "3×", "Beginners and busy lifters"],
    ["Bro split", "5", "1× direct", "Lifters who like one muscle per day"],
])}
<p>Split and full-body routines produced similar strength and size gains when weekly sets were equal in a {cite('split2024', '2024 meta-analysis')}, so choose the split that fits the days you can train.</p>
"""),
    ],
    "schedule": [("Mon", "Push A", "c1"), ("Tue", "Pull A", "c2"), ("Wed", "Legs A", "c3"), ("Thu", "Push B", "c4"), ("Fri", "Pull B", "c5"), ("Sat", "Legs B", "c6"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Push A", "title": "Day 1 — Push A (Heavy)", "tag": "Strength", "color": 1, "time": "60–70 min", "focus": "Chest / Shoulders / Triceps",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "4 × 4–6", "3–4 min", "RPE 8–9"),
             ("Overhead Press (Barbell)", "Primary: front & side delts · Secondary: triceps", "4 × 5–7", "3 min", "RPE 8"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 6–8", "2.5 min", "RPE 8"),
             ("Weighted Dip", "Primary: lower chest, triceps", "3 × 6–8", "2.5 min", "RPE 8"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 10–12", "90 sec", "RPE 8"),
             ("Close-Grip Bench Press", "Primary: triceps · Secondary: chest", "2 × 6–8", "2 min", "RPE 8"),
         ],
         "notes": "Use a dip belt once bodyweight dips feel easy for 8+ reps. No dips? Use the flat dumbbell press."},
        {"tab": "Day 2", "tab_sub": "Pull A", "title": "Day 2 — Pull A (Heavy)", "tag": "Strength", "color": 2, "time": "60–70 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Conventional Deadlift", "Primary: glutes, hamstrings, back · Secondary: traps, grip", "3 × 4–6", "4 min", "RPE 8–9"),
             ("Barbell Bent-Over Row", "Primary: lats, mid-back · Secondary: rear delts, biceps", "4 × 5–7", "3 min", "RPE 8"),
             ("Weighted Pull-Up", "Primary: lats · Secondary: biceps", "3 × 5–8", "2.5 min", "RPE 8"),
             ("Seated Cable Row", "Primary: mid-back · Secondary: biceps", "3 × 8–10", "2 min", "RPE 8"),
             ("Face Pull", "Primary: rear delts, rotator cuff", "3 × 15–20", "90 sec", "RPE 7"),
             ("Barbell Curl", "Primary: biceps", "3 × 6–8", "90 sec", "RPE 8"),
         ],
         "notes": "Deadlifts come first while you are fresh; keep them at 3 sets. Use lifting straps if grip fails before your back. Can't do pull-ups? Use lat pulldowns."},
        {"tab": "Day 3", "tab_sub": "Legs A", "title": "Day 3 — Legs A (Heavy)", "tag": "Strength", "color": 3, "time": "65–75 min", "focus": "Quads / Hamstrings / Glutes / Calves",
         "exercises": [
             ("Barbell Back Squat", "Primary: quads, glutes · Secondary: adductors, core", "4 × 4–6", "3–4 min", "RPE 8–9"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "4 × 6–8", "3 min", "RPE 8"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "3 × 8–10 / leg", "2 min", "RPE 8"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 8–10", "2 min", "RPE 8"),
             ("Leg Extension", "Primary: quads", "3 × 10–12", "90 sec", "RPE 8"),
             ("Standing Calf Raise", "Primary: calves", "3 × 10–12", "90 sec", "RPE 9"),
         ],
         "notes": f"Squat to at least parallel. Seated leg curls built more hamstring muscle than lying curls in a {cite('maeo2021', 'controlled trial')}; use the lying version if that's what your gym has. Pause 1 second at the bottom of each calf raise."},
        {"tab": "Day 4", "tab_sub": "Push B", "title": "Day 4 — Push B (Volume)", "tag": "Hypertrophy", "color": 4, "time": "55–65 min", "focus": "Chest / Shoulders / Triceps",
         "exercises": [
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "4 × 8–12", "2 min", "RPE 8"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: triceps", "3 × 10–12", "2 min", "RPE 8"),
             ("Seated Dumbbell Shoulder Press", "Primary: front & side delts · Secondary: triceps", "3 × 10–12", "2 min", "RPE 8"),
             ("Low-to-High Cable Fly", "Primary: upper chest", "3 × 12–15", "90 sec", "RPE 7–8"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "4 × 15–20", "60 sec", "RPE 8"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 12–15", "60 sec", "RPE 8"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 12–15", "60 sec", "RPE 8"),
         ],
         "notes": "Raise lateral raises with control (about 2 seconds up, 2 seconds down). Superset the two triceps exercises to save time."},
        {"tab": "Day 5", "tab_sub": "Pull B", "title": "Day 5 — Pull B (Volume)", "tag": "Hypertrophy", "color": 5, "time": "55–65 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Wide-Grip Lat Pulldown", "Primary: lats · Secondary: biceps", "4 × 10–12", "2 min", "RPE 8"),
             ("One-Arm Dumbbell Row", "Primary: lats, mid-back", "3 × 10–12 / arm", "90 sec", "RPE 8"),
             ("Close-Grip Seated Cable Row", "Primary: mid-back · Secondary: biceps", "3 × 12–15", "90 sec", "RPE 8"),
             ("Face Pull", "Primary: rear delts", "3 × 20–25", "60 sec", "RPE 7"),
             ("Reverse Pec Deck", "Primary: rear delts", "3 × 15–20", "60 sec", "RPE 8"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "3 × 10–12", "90 sec", "RPE 8"),
             ("Incline Dumbbell Hammer Curl", "Primary: brachialis, biceps", "4 × 12–15", "60 sec", "RPE 8"),
         ],
         "notes": "No deadlifts today, which gives your lower back a break before Legs B. Squeeze the rear-delt work instead of swinging."},
        {"tab": "Day 6", "tab_sub": "Legs B", "title": "Day 6 — Legs B (Volume)", "tag": "Hypertrophy", "color": 6, "time": "60–70 min", "focus": "Quads / Glutes / Hamstrings / Core",
         "exercises": [
             ("Leg Press", "Primary: quads, glutes", "4 × 12–15", "2 min", "RPE 8"),
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "4 × 10–12", "2 min", "RPE 8"),
             ("Dumbbell Walking Lunge", "Primary: quads, glutes", "3 × 12–14 / leg", "90 sec", "RPE 8"),
             ("Seated Leg Curl", "Primary: hamstrings", "4 × 12–15", "90 sec", "RPE 8"),
             ("Leg Extension", "Primary: quads", "3 × 15–20", "60 sec", "RPE 8"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "3 × 15–20", "60 sec", "RPE 9"),
             ("Hanging Leg Raise (or Cable Woodchop)", "Primary: abs, obliques", "3 × 12–15", "60 sec", "RPE 7"),
         ],
         "notes": "The leg press trains the quads hard without loading the spine like a heavy squat."},
    ],
    "faq_title": "Push Pull Legs Workout Plan FAQ",
    "faqs": [
        ("What if I miss a day?", "Do the missed workout the next day and shift the rest of the week by one day. Don't combine two workouts into one session."),
        ("Do I have to deadlift on pull day?", "No. If deadlifts leave your rows weak, move them to the end of Legs A or swap them for rack pulls, which train the back with less leg fatigue."),
        ("Can I do push pull legs only 3 days a week?", "Yes, as Push, Pull, Legs once a week, alternating A and B workouts each week. Each muscle is then trained once a week, so progress is slower than on the 6-day plan."),
        ("Can I add more ab work?", "Yes. Add 2–3 sets of planks or ab wheel rollouts at the end of any session. Squats, deadlifts and overhead presses already train your trunk hard."),
        ("Can I follow this PPL plan while cutting?", "Yes. Keep the weights heavy, keep protein at the upper end of 1.6–2.2 g/kg, and drop one set per exercise on B days if recovery suffers."),
        ("When will I see results?", "Strength usually rises within the first few weeks. Visible muscle changes often take 6–8 weeks; compare photos and your training log every 4 weeks."),
    ],
    "related": ["ppl-hypertrophy-program", "upper-lower-split", "5-day-workout-split", "full-body-workout-plan"],
    "refs": refs("rest2016", "pelland2026", "acsm2026", "deload2024", "maeo2021", "protein2018", "offseason2019", "split2024"),
    "disclaimer": DISCLAIMER,
}
