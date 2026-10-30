from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 7,
    "slug": "3-day-full-body-workout",
    "title": "3-Day Full Body Workout for Intermediate Lifters (Heavy, Light, Medium)",
    "meta_title": "3 Day Full Body Workout for Intermediates (Free Plan)",
    "meta_desc": "Only 3 days to train? This 3 day full body workout uses heavy, light and medium days with full sets and reps, so you keep progressing past beginner.",
    "focus_kw": "3 day full body workout",
    "badge": "Intermediate · 3 Days",
    "hero_lead": "Past the beginner stage but still limited to three gym days? This 3 day full body workout rotates a heavy, a light and a medium session so you can train every muscle three times a week without grinding yourself down.",
    "hero_meta": ["📅 3 days/week", "⏱ 60–75 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("3", "Training days"), ("3×", "Frequency/muscle"), ("9–12", "Sets/major muscle/wk"), ("8 wk", "Block length"), ("H/L/M", "Daily load rotation")],
    "quick_answer": "This 3 day full body workout trains every major muscle on Monday, Wednesday and Friday. Monday is heavy (4–6 reps on the main lifts), Wednesday is light (10–15 reps with shorter rests) and Friday is medium (5–10 reps), with different exercises each day.",
    "intro": "<p>Use the day tabs to see the heavy, light and medium sessions. Progression, deloads and FAQs follow the workouts.</p>",
    "sections": [
        ("schedule", "Weekly Schedule", f"""
<p>Keep at least one rest day between sessions. Monday's heavy session follows two rest days, and Friday's medium session is followed by two.</p>
{WEEK}
{table(["Day", "Rep focus", "Rest periods", "Main lifts"], [
    ["Day 1 – Heavy", "4–6 reps (main lifts)", "2–3 min", "Back squat, bench press, weighted pull-up"],
    ["Day 2 – Light", "10–15 reps", "60–90 sec", "Leg press, dumbbell bench, cable row"],
    ["Day 3 – Medium", "5–10 reps", "90 sec–2.5 min", "Trap bar deadlift, overhead press, split squat"],
])}
<p>Walking, cycling or mobility work on rest days is fine. Avoid hard leg conditioning on Thursday because it carries into Friday's deadlifts and split squats.</p>
"""),
        ("workouts", "The 3-Day Full Body Workouts", f"""
<p>Tap a day to see the session. Effort is written as reps in reserve (RIR): RIR 2 means you finish with two clean reps left. The {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains how to judge it.</p>
{TABS}
"""),
        ("volume", "Weekly Volume Check", f"""
<p>Three full-body sessions give each muscle several smaller doses instead of one large one. Direct sets count fully; indirect sets count as half.</p>
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Quads", "10", "Trap bar deadlift 3 → 1.5", "≈ 11.5"],
    ["Hamstrings", "6", "Trap bar deadlift 3 → 1.5", "≈ 7.5"],
    ["Glutes", "–", "Squats, hinges, split squats 16 → 8", "≈ 8"],
    ["Chest", "10", "–", "10"],
    ["Back", "9", "–", "9"],
    ["Side delts", "6", "Overhead press 3 → 1.5", "≈ 7.5"],
    ["Biceps", "5", "Pulls & rows 9 → 4.5", "≈ 9.5"],
    ["Triceps", "5", "Presses 13 → 6.5", "≈ 11.5"],
    ["Calves", "3", "–", "3"],
])}
<p>The {cite('acsm2026', 'ACSM position stand')} associates more growth with 10+ weekly sets per muscle, and {cite('vol2019', 'Schoenfeld et al. (2019)')} found strength gains were similar across low and high volumes while size kept rising with more sets. This plan sits near the 10-set mark for most muscles to keep sessions under 75 minutes. If hamstrings, side delts or calves are a priority, add 2–3 sets to the light day; see {L('/how-many-sets-per-muscle-group-per-week/', 'how many sets per muscle group per week')} for guidance on adding volume.</p>
"""),
        ("progression", "Progression by Day", f"""
<p>Each day progresses differently, which is the main skill an intermediate lifter needs. Read the {L('/what-is-progressive-overload/', 'progressive overload guide')} for the wider principles.</p>
{table(["Day", "Rule", "Example"], [
    ["Heavy", "When all sets hit the top of the range at RIR 2, add 2.5 kg (upper) or 5 kg (lower)", "Squat 4 × 6 at 100 kg → next week 4 sets at 105 kg"],
    ["Light", "Add reps until all sets reach 15, then add the smallest load", "Leg press 12, 13, 14 reps → 15, 15, 15 → add 10 kg"],
    ["Medium", "Double progression within each rep range", "OHP 3 × 8 → 3 × 10 → add 2.5 kg"],
])}
<p>Progress on the light day will look slow on paper. Its job is to add volume with low joint stress, not to set records. If the heavy day stalls for two weeks, check sleep and calories before changing the program.</p>
"""),
        ("deload", "Deload Every 8th Week", f"""
<p>Run weeks 1–7 as written and deload in week 8. Keep all three days, cut sets roughly in half, and stop each set at RIR 3–4. In a {cite('deload2024', 'survey of strength and physique athletes')}, deloads lasted about a week, came every 5–6 weeks on average, and mostly reduced sets and reps while keeping training frequency. If you feel worn down by week 5 or 6, deload then. The {L('/what-is-a-deload-week/', 'deload week guide')} lists the warning signs.</p>
"""),
        ("warmup", "Warm-Up", f"""
<p>Warm up for 5–8 minutes with light cardio and a few bodyweight squats, hip hinges and band pull-aparts. Then ramp up on the first lift: bar or light load × 8, about 60% × 5, about 80% × 2–3. The {L('/how-to-warm-up-before-a-workout/', 'warm-up guide')} covers this in more detail.</p>
"""),
        ("why", "Why Full Body Still Works for Intermediates", f"""
<p>Split and full-body routines produced similar strength and muscle gains when weekly volume was matched in a {cite('split2024', '2024 meta-analysis of 14 studies')}. Training a lift more often also helps strength: gains rose with weekly frequency in a {cite('freqstr2018', '2018 meta-analysis')}, and the {cite('pelland2026', '2026 Pelland meta-regression')} found the same with diminishing returns. The heavy/light/medium rotation is a fatigue tool; the {cite('acsm2026', '2026 ACSM position stand')} found periodization models did not consistently change outcomes, so its value is practical: you grind heavy loads only once a week.</p>
"""),
        ("nutrition", "What to Eat on This Plan", f"""
<p>Aim for about 1.6 g of protein per kg of body weight daily, the point where gains plateaued in a {cite('protein2018', 'meta-analysis of 49 trials')}. Spread it evenly over 3–5 meals; the {cite('issnprotein', 'ISSN protein position stand')} suggests 20–40 g per meal every 3–4 hours. A meal with carbs and protein 1–3 hours before training helps you start the session fuelled. For meal ideas, see the {L('/best-pre-workout-meal-for-muscle-gain/', 'best pre-workout meals for muscle gain')}.</p>
"""),
    ],
    "schedule": [("Mon", "Heavy", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Light", "c1"), ("Thu", "Rest", "rest"), ("Fri", "Medium", "c2"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Heavy", "title": "Day 1: Heavy", "tag": "4–6 reps", "color": 4, "time": "65–75 min", "focus": "Full body",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors, core", "4 × 4–6", "3 min", "RIR 2"),
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "4 × 4–6", "3 min", "RIR 2"),
             ("Weighted Pull-Up", "Primary: lats · Secondary: biceps", "3 × 5–7", "2–3 min", "RIR 2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 1"),
             ("Standing Calf Raise", "Primary: calves", "3 × 8–12", "60–90 sec", "RIR 1"),
         ],
         "notes": "Squat and bench are the priority. If time is short, cut lateral raises and calf raises, not the main lifts."},
        {"tab": "Day 2", "tab_sub": "Light", "title": "Day 2: Light", "tag": "10–15 reps", "color": 1, "time": "55–65 min", "focus": "Full body",
         "exercises": [
             ("Leg Press", "Primary: quads · Secondary: glutes", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: triceps", "3 × 10–12", "90 sec", "RIR 1–2"),
             ("Seated Cable Row", "Primary: mid-back · Secondary: rear delts, biceps", "3 × 10–12", "90 sec", "RIR 1"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 12–15", "60–90 sec", "RIR 1"),
             ("Cable Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "3 × 10–15", "60 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Run the curl and pushdown as a superset. The aim today is clean reps and a strong pump, not heavy loads."},
        {"tab": "Day 3", "tab_sub": "Medium", "title": "Day 3: Medium", "tag": "5–10 reps", "color": 2, "time": "60–70 min", "focus": "Full body",
         "exercises": [
             ("Trap Bar Deadlift", "Primary: glutes, quads, hamstrings · Secondary: upper back", "3 × 5–7", "3 min", "RIR 2"),
             ("Standing Overhead Press", "Primary: front delts · Secondary: triceps, upper chest", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "3 × 8–10 / leg", "2 min", "RIR 2"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, lats", "3 × 8–10", "90 sec", "RIR 1–2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Hammer Curl", "Primary: brachialis, biceps", "2 × 10–12", "60 sec", "RIR 1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "2 × 10–12", "60 sec", "RIR 1"),
         ],
         "notes": "Rest a full 2 minutes between split-squat legs if you need it. Superset the hammer curl and overhead extension."},
    ],
    "swap_overrides": {"Back Squat": "Safety-Bar Squat or Hack Squat", "Barbell Back Squat": "Safety-Bar Squat or Hack Squat",
                       "Weighted Pull-Up": "Lat Pulldown (if you can't do 6 strict pull-ups)", "Bulgarian Split Squat": "Reverse Lunge or Leg Press"},
    "faq_title": "3-Day Full Body Workout FAQ",
    "faqs": [
        ("Can I do this 3 day full body workout on consecutive days?", "It's not recommended. Each session trains every muscle, so back-to-back days leave you under-recovered. Keep at least 48 hours between sessions."),
        ("Is 3 days a week enough to build muscle as an intermediate?", "Yes. With about 9–12 hard sets per major muscle each week and steady progression, three sessions can keep you progressing for a long time, though progress is slower than on a higher-volume 4–5 day plan."),
        ("Can I add a fourth day?", "Add an optional short arms-and-delts session on Saturday (lateral raises, curls, triceps extensions, 2–3 sets each) if you have time. Keep it light enough that Monday's heavy day is not affected."),
        ("What if I miss the heavy day?", "Do the heavy session at your next workout and skip the light day that week. The heavy day drives strength, so it should not be the session you drop."),
        ("Should I train abs separately?", "Squats, deadlifts, split squats and overhead presses all train your trunk. If you want direct ab work, add 2–3 sets of cable crunches or hanging knee raises to the light day."),
    ],
    "related": ["full-body-workout-plan", "beginner-strength-training-program", "5x5-workout", "4-day-workout-split"],
    "refs": refs("split2024", "freqstr2018", "pelland2026", "acsm2026", "vol2019", "deload2024", "protein2018", "issnprotein"),
    "disclaimer": DISCLAIMER,
}
