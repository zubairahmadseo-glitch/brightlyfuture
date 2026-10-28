from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 14,
    "slug": "strength-training-for-women",
    "title": "Strength Training for Women: A 3-Day Gym Workout Plan",
    "meta_title": "Strength Training for Women: 3-Day Gym Workout Plan",
    "meta_desc": "A strength training for women plan: 3 full-body gym days with glute and leg emphasis, clear progression, and evidence on toning, cycles and bone health.",
    "focus_kw": "strength training for women",
    "badge": "Women's Strength Plan",
    "hero_lead": "Strength training for women does not need a pink-dumbbell version of the real thing. This 3-day plan uses the same proven lifts as any good program, with extra emphasis on glutes and legs, a 2-day option for busy weeks, and straight answers to the questions women ask most.",
    "hero_meta": ["📅 3 days/week (2-day option)", "⏱ 45–60 min", "📊 Beginner–Intermediate", "🏋️ Gym"],
    "stats": [("3", "Training days"), ("19", "Exercises"), ("≈ 13", "Glute sets/week"), ("8 wk", "Block length"), ("1.6 g/kg", "Protein/day")],
    "quick_answer": "Strength training for women works best with 2–3 full-body sessions a week built on squats, hip thrusts, deadlift variations, presses and rows, using 6–15 reps and adding weight over time. This plan follows that pattern with extra glute and leg volume and a progression rule you can use for months.",
    "takeaways": [
        "Women and men gain muscle at similar relative rates on the same program, so women do not need lighter, high-rep-only training.",
        "Muscle grows gradually; \"bulky\" results from a few months of lifting are not realistic for most women.",
        "Current evidence does not show that you need to plan training around your menstrual cycle; adjust by how you feel.",
        "Heavy, supervised resistance training improved bone density in postmenopausal women with low bone mass in the LIFTMOR trial.",
        "Two sessions a week still bring results; three gives more room for progress.",
    ],
    "intro": "<p>Many women start strength training with light weights and high reps because they were told heavier lifting makes you bulky. The research says otherwise, and so do the results of women who lift. Muscle builds shape; strength makes daily life easier; heavy loading supports bones as you age.</p><p>This page gives you a full 3-day plan with every set and rep, a simple way to progress, and the evidence behind the most common concerns.</p>",
    "sections": [
        ("myths", "Will Strength Training Make Women Bulky?", f"""
<p>No, not by accident. A {cite('sex2020', 'meta-analysis comparing men and women')} on the same programs found similar relative muscle growth between sexes and greater relative upper-body strength gains in women. Relative is the key word. In a {cite('hubal2005', 'study of 585 adults')} following the same 12-week arm program, women gained more relative strength than men, while men gained slightly more muscle size.</p>
<p>What women see after a few months of lifting is usually firmer, more defined arms, legs and glutes, especially if body fat drops. Building visibly large muscle takes years of deliberate training and eating in a surplus.</p>
{box("tip", "💡 \"Toning\" is building muscle", "<p>\"Toned\" describes visible muscle with moderate body fat. The way to get it is the same for everyone: build muscle with progressive strength training, and manage body fat with nutrition.</p>")}
"""),
        ("who", "Who This Plan Is For", f"""
<ul>
<li>Women with 0–2 years of lifting experience who want a structured gym plan.</li>
<li>Goals of strength, shape (especially glutes and legs), fat loss support or long-term health.</li>
<li>Access to a gym with barbells, dumbbells, cables and basic machines.</li>
<li>Time for three 45–60 minute sessions a week, or two when life is busy.</li>
</ul>
<p>For a deeper look at rep ranges, read our guide to {L('/reps-and-sets-for-woman/', 'reps and sets for women')}. If fat loss is your main goal and you are just starting out, the {L('/3-week-beginner-fat-loss-workout-plan-for-women/', '3-week beginner fat loss plan for women')} is a gentler on-ramp.</p>
"""),
        ("schedule", "Weekly Schedule (and the 2-Day Option)", f"""
{WEEK}
<p><strong>2-day option:</strong> train Day 1 and Day 2 on non-consecutive days (for example Tuesday and Friday), and add one set to the hip thrust and lat pulldown. This keeps every major muscle trained twice a week.</p>
"""),
        ("workouts", "The Strength Workouts", f"""
<p>Select a day. Effort is in reps in reserve (RIR): RIR 2 means you could do two more good reps. Start new lifts at RIR 3 for the first two weeks. The {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains how to judge it.</p>
{TABS}
"""),
        ("volume", "Weekly Volume: Where the Work Goes", f"""
{table(["Muscle", "Weekly sets (approx.)", "Main exercises"], [
    ["Glutes", "≈ 13", "Hip thrust, split squat, kickback, squat, deadlift variations"],
    ["Quads", "≈ 9.5", "Squat, leg press, split squat"],
    ["Hamstrings", "≈ 8", "Romanian deadlift, leg curl"],
    ["Back", "9", "Lat pulldown, cable row, dumbbell row"],
    ["Chest", "6", "Dumbbell bench, incline press"],
    ["Arms & shoulders", "≈ 4–7 each", "Presses, curls, pushdowns, lateral raises"],
])}
<p>Direct sets count fully and indirect sets count as half. Glutes and legs get the most volume because most women name them as a priority; the upper body gets enough to grow stronger and keep posture balanced. The {cite('acsm2026', '2026 ACSM position stand')} links more growth with 10+ weekly sets per muscle, so add 2 sets of upper-body work per session if that is your priority.</p>
"""),
        ("progression", "How to Progress", f"""
<p>Use double progression on every exercise. Work within the rep range, and when you hit the top on all sets at the listed RIR, increase the load: 2.5 kg on barbell lifts, the next dumbbell up, or one plate on machines. This is the core of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
{table(["Week", "Hip thrust 3 × 8–12", "Next step"], [
    ["1", "40 kg × 12, 10, 9", "Stay at 40 kg"],
    ["2", "40 kg × 12, 11, 10", "Stay"],
    ["3", "40 kg × 12, 12, 12", "Add 5 kg"],
    ["4", "45 kg × 10, 9, 8", "Build reps again"],
])}
<p>Small dumbbell jumps can feel large on upper-body lifts. When the next dumbbell is too heavy, add one rep per set per week instead, or use fractional plates on a barbell. Run weeks 1–7 as written and take a lighter week 8 with half the sets, then start a new block. The {L('/what-is-a-deload-week/', 'deload week guide')} explains why.</p>
"""),
        ("cycle", "Should You Train Around Your Menstrual Cycle?", f"""
<p>Current research does not support rigid cycle-based programming. A {cite('cycle2023', '2023 umbrella review')} concluded it is premature to say short-term hormone changes across the cycle meaningfully affect strength performance or long-term gains from resistance training.</p>
<p>Symptoms are real, though. If cramps, fatigue or poor sleep hit during certain days, it is fine to lower the load, cut a set, or swap to RIR 3 for that session. Keep training consistently across the month and let your logbook, not the calendar, guide you.</p>
"""),
        ("bones", "Strength Training and Bone Health", f"""
<p>Bone responds to high loads. In the {cite('liftmor2018', 'LIFTMOR randomized trial')}, postmenopausal women with low bone mass did 8 months of twice-weekly, supervised high-intensity resistance and impact training (5 sets of 5 at more than 85% of their one-rep max). They improved spine and hip bone density and physical function, with only one minor adverse event.</p>
{box("warn", "⚠️ Important context", "<p>LIFTMOR participants were screened and closely supervised. If you have osteopenia or osteoporosis, get medical clearance and coaching before lifting heavy. The deadlift and squat variations in this plan should be learned with lighter loads first.</p>")}
<p>For older women, our article on why {L('/aging-women-need-high-intensity-exercise/', 'aging women need high-intensity exercise')} covers more of the health case.</p>
"""),
        ("nutrition", "Nutrition for Women Who Lift", f"""
<p>Protein needs are the same per kilogram for women as for men. Gains from protein plateaued near 1.6 g/kg/day in a {cite('protein2018', 'meta-analysis of 49 trials')}, and the {cite('issnprotein', 'ISSN position stand')} suggests spreading it across meals of about 0.25 g/kg each. For a 65 kg woman, that is about 105 g a day, roughly 25–30 g over four meals. Use the {L('/protein-calculator/', 'protein calculator')} for your own number.</p>
<p>Eating too little is a common reason women stop progressing. If your lifts stall for several weeks and you feel tired, review your total intake before changing the program.</p>
"""),
    ],
    "schedule": [("Mon", "Day 1", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Day 2", "c2"), ("Thu", "Rest", "rest"), ("Fri", "Day 3", "c6"), ("Sat", "Walk / rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Squat + Push", "title": "Day 1 — Squat, Glutes & Push", "tag": "Lower + upper push", "color": 4, "time": "50–60 min", "focus": "Quads / Glutes / Chest / Shoulders",
         "exercises": [
             ("Back Squat (or Goblet Squat)", "Primary: quads, glutes · Secondary: adductors, core", "3 × 6–10", "2–3 min", "RIR 2"),
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 8–12", "90 sec", "RIR 2"),
             ("Seated Dumbbell Shoulder Press", "Primary: shoulders · Secondary: triceps", "2 × 8–12", "90 sec", "RIR 2"),
             ("Seated Leg Curl", "Primary: hamstrings", "2 × 10–15", "60–90 sec", "RIR 1–2"),
             ("Pallof Press", "Primary: obliques, deep core", "2 × 10 / side", "60 sec", "Controlled"),
         ],
         "notes": "Use a pad on the bar for hip thrusts. Beginners should goblet squat for the first 2–4 weeks before moving to the barbell."},
        {"tab": "Day 2", "tab_sub": "Hinge + Pull", "title": "Day 2 — Hinge, Glutes & Pull", "tag": "Lower + upper pull", "color": 2, "time": "50–60 min", "focus": "Hamstrings / Glutes / Back / Arms",
         "exercises": [
             ("Romanian Deadlift", "Primary: hamstrings, glutes · Secondary: back", "3 × 6–10", "2–3 min", "RIR 2"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 8–12", "90 sec", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: glutes, quads", "2 × 8–12 / leg", "90 sec", "RIR 2"),
             ("Seated Cable Row", "Primary: mid-back · Secondary: rear delts", "3 × 10–12", "90 sec", "RIR 1–2"),
             ("Cable Glute Kickback", "Primary: glutes", "2 × 12–15 / leg", "60 sec", "RIR 1"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "2 × 10–15", "60 sec", "RIR 1–2"),
         ],
         "notes": "For more glute work on split squats, lean your torso slightly forward and use a longer stance."},
        {"tab": "Day 3", "tab_sub": "Full Body", "title": "Day 3 — Full Body Strength", "tag": "Strength + carry", "color": 6, "time": "50–60 min", "focus": "Full body",
         "exercises": [
             ("Trap Bar Deadlift", "Primary: glutes, quads, hamstrings · Secondary: upper back, grip", "3 × 5–8", "2–3 min", "RIR 2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 8–12", "90 sec", "RIR 2"),
             ("Leg Press", "Primary: quads, glutes", "3 × 10–15", "2 min", "RIR 1–2"),
             ("One-Arm Dumbbell Row", "Primary: lats, mid-back", "3 × 8–12", "90 sec", "RIR 1–2"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "2 × 12–15", "60 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 10–15", "60 sec", "RIR 1–2"),
             ("Farmer's Carry", "Primary: grip, traps, core", "2 × 30–40 m", "90 sec", "Heavy but upright"),
         ],
         "notes": "Place feet higher on the leg press platform for more glute and hamstring involvement. Superset lateral raises with pushdowns."},
    ],
    "faq_title": "Strength Training for Women FAQ",
    "faqs": [
        ("How heavy should women lift?", "Heavy enough that the last 1–3 reps of each set are hard while form stays clean. For most exercises in this plan, that means loads you can lift 6–15 times."),
        ("Can I do this plan to lose fat?", "Yes. Strength training preserves muscle while you eat in a calorie deficit, so more of the weight you lose comes from fat. Keep protein high and the loads as heavy as you can manage."),
        ("Is strength training safe during pregnancy?", "Many women continue strength training during pregnancy, but needs change by trimester and individual health. Get guidance from your doctor or midwife before continuing or starting any program."),
        ("How long until I see results?", "Strength usually improves within 2–4 weeks. Visible changes in shape typically take 8–12 weeks of consistent training and eating."),
        ("Do I need different exercises than men?", "No. The same movements build muscle and strength for everyone. This plan simply places more weekly volume on glutes and legs."),
        ("Can I add cardio?", "Yes. Two or three sessions of walking, cycling or swimming per week support heart health and recovery. Avoid hard leg intervals the day before Day 1 or Day 3."),
    ],
    "related": ["beginner-strength-training-program", "full-body-workout-plan", "upper-lower-split", "hypertrophy-program"],
    "refs": refs("sex2020", "hubal2005", "acsm2026", "cycle2023", "liftmor2018", "protein2018", "issnprotein"),
    "disclaimer": DISCLAIMER,
}
