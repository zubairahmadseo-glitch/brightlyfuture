from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 15,
    "slug": "powerlifting-program-for-beginners",
    "title": "Powerlifting Program for Beginners: 12 Weeks to Your First Test Day",
    "meta_title": "Powerlifting Program for Beginners: 12-Week Plan",
    "meta_desc": "A 12-week powerlifting program for beginners: squat, bench and deadlift 3 days a week with RPE targets, three training phases and a test day to finish.",
    "focus_kw": "powerlifting program for beginners",
    "badge": "Squat · Bench · Deadlift",
    "hero_lead": "Powerlifting is three lifts: squat, bench press and deadlift, each tested for one heavy rep. This powerlifting program for beginners trains them three days a week through three phases and finishes with a test day where you set your first real totals.",
    "hero_meta": ["📅 3 days/week", "⏱ 60–80 min", "📊 Beginner–Intermediate", "🏋️ Barbell, rack, bench"],
    "stats": [("12 wk", "Program length"), ("3", "Phases"), ("2–3×", "Weekly practice per lift"), ("RPE 6→9", "Effort ramp"), ("1", "Test day")],
    "quick_answer": "A good powerlifting program for beginners practices the squat, bench press and deadlift two to three times a week, uses moderate loads to build technique first, then gets heavier in planned phases. This 12-week plan runs three days a week with RPE targets and ends with a test day for all three lifts.",
    "takeaways": [
        "Bench is trained three times a week, squat twice and deadlift once heavy plus one lighter variation.",
        "Weeks 1–4 build volume at RPE 6–7, weeks 5–8 build strength at RPE 7–8, and weeks 9–11 practise heavy singles to doubles.",
        "Week 12 cuts volume so you arrive at test day fresh.",
        "Competition-style technique matters from day one: squat depth, a paused bench and a full deadlift lockout.",
        "Rest 3–5 minutes between heavy sets of the main lifts.",
    ],
    "intro": "<p>Plenty of beginners are already strong enough to try powerlifting. What they lack is a plan that practises the three lifts the way they are judged, builds strength in a sensible order, and teaches them to handle heavy singles safely.</p><p>This program gives you that structure. You need about six months of general lifting experience and the ability to squat, bench and deadlift with consistent form. If you are newer than that, run our {L('/workout-plans/beginner-strength-training-program/', 'beginner strength training program')} first.</p>",
    "sections": [
        ("rules", "What Makes Powerlifting Different?", f"""
<p>In a powerlifting meet, each lift must meet a standard. Training to those standards from week 1 means your gym numbers will count on the platform.</p>
{table(["Lift", "What judges look for", "How this plan trains it"], [
    ["Squat", "Hip crease below the top of the knee, then stand to full lockout", "Competition-depth squats, plus paused squats on Day 3"],
    ["Bench press", "Bar held motionless on the chest before pressing; shoulders and glutes stay on the bench and feet stay on the floor", "Paused bench on Day 2, touch-and-go only for volume"],
    ["Deadlift", "Stand fully upright with hips and knees locked, no hitching", "Full lockout every rep; no bouncing between reps"],
])}
<p>Federations differ slightly in their rules, so read the rulebook of any meet you enter. For technique details, see {L('/high-bar-vs-low-bar-squat/', 'high-bar vs low-bar squat')}, {L('/bench-press-grip-width/', 'bench press grip width')} and {L('/sumo-vs-conventional-deadlift/', 'sumo vs conventional deadlift')}.</p>
"""),
        ("rpe", "How RPE Works in This Program", f"""
<p>Loads are set by RPE (rating of perceived exertion), not fixed percentages. That lets the program adjust on days you feel strong or tired. This plan uses the {cite('rpe2016', 'reps-in-reserve RPE scale validated by Zourdos et al.')}:</p>
{table(["RPE", "Meaning", "Reps in reserve"], [
    ["10", "Maximal effort, no reps left", "0"],
    ["9", "One more rep possible", "1"],
    ["8", "Two more reps possible", "2"],
    ["7", "Three more reps possible; bar moves quickly", "3"],
    ["6", "Four or more reps left; warm-up feel", "4+"],
])}
<p>New lifters tend to underrate how many reps they have left, so be honest and conservative. The {L('/rpe-calculator/', 'RPE calculator')} converts RPE and reps into an estimated one-rep max, and our {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains the scale in more depth.</p>
"""),
        ("schedule", "Weekly Schedule", f"""
{WEEK}
{table(["Day", "Squat", "Bench", "Deadlift"], [
    ["Day 1", "Main squat (heavy)", "Touch-and-go bench (volume)", "–"],
    ["Day 2", "–", "Paused bench (heavy)", "Main deadlift"],
    ["Day 3", "Paused squat (technique)", "Close-grip bench", "Romanian deadlift"],
])}
{box("science", "🔬 Why this frequency?", f"<p>A {cite('freqstr2018', 'meta-analysis on training frequency')} found strength gains rose with more weekly sessions, mostly because frequency allowed more total practice and volume. A {cite('currier2023', 'network meta-analysis of 178 studies')} ranked higher-load, multi-set training three times a week as the most effective prescription for strength.</p>")}
"""),
        ("phases", "The Three Phases", f"""
<p>The weekly structure stays the same for 12 weeks. What changes is sets, reps and RPE on the main lifts.</p>
{table(["Main lift", "Weeks 1–4: Base", "Weeks 5–8: Strength", "Weeks 9–11: Peak"], [
    ["Squat (Day 1)", "4 × 6 @ RPE 7", "5 × 4 @ RPE 7–8", "Top set @ RPE 8 (wk 9: 3 reps, wk 10: 2, wk 11: 1), then 3 × 3 at −10%"],
    ["Bench (Day 1)", "3 × 8 @ RPE 7", "4 × 6 @ RPE 7", "3 × 5 @ RPE 7"],
    ["Paused bench (Day 2)", "4 × 5 @ RPE 7", "5 × 3 @ RPE 8", "Top set @ RPE 8 (3, 2, 1 reps), then 3 × 3 at −10%"],
    ["Deadlift (Day 2)", "3 × 5 @ RPE 7", "4 × 3 @ RPE 7–8", "Top set @ RPE 8 (3, 2, 1 reps), then 2 × 3 at −10%"],
    ["Paused squat (Day 3)", "3 × 5 @ RPE 6–7", "3 × 4 @ RPE 7", "2 × 3 @ RPE 7"],
])}
<p>Heavier work arrives late on purpose. A {cite('load2021', 'network meta-analysis')} found high loads produced the largest strength gains, and the {cite('acsm2026', '2026 ACSM position stand')} found heavier loads (80%+ of max) improved strength most. The base phase builds the muscle and technique that make those heavy weeks productive.</p>
"""),
        ("workouts", "The Powerlifting Workouts", f"""
<p>Pick a day. The main-lift sets shown are for <strong>weeks 1–4</strong>; use the phase table above for weeks 5–11. Accessories stay the same all program.</p>
{TABS}
"""),
        ("rest", "Rest Periods and Warm-Ups", f"""
<p>Rest 3–5 minutes between heavy sets of the main lifts and 90 seconds to 2 minutes on accessories. A {cite('rest2018', 'systematic review')} found rests over 2 minutes were needed to maximise strength gains in trained lifters.</p>
<p>Warm up with 5 minutes of light cardio, then ramp up gradually: empty bar × 8–10, then sets of 5, 3, 2 and 1 at roughly 40%, 60%, 75% and 85–90% of the day's top set. Use the {L('/warm-up-set-calculator/', 'warm-up set calculator')} to plan the jumps.</p>
"""),
        ("taper", "Week 12: Taper and Test Day", f"""
<p>Evidence on peaking for powerlifting is limited; a {cite('taper2020', 'review on tapering for powerlifters')} found few studies with enough detail to give a fixed protocol. This plan takes a conservative approach common in coaching: reduce volume, keep some heavy work, and arrive rested.</p>
{table(["Week 12 day", "Session"], [
    ["Monday", "Squat 2 × 2 @ RPE 7, bench 2 × 2 @ RPE 7"],
    ["Wednesday", "Bench 3 × 3 @ RPE 6, light accessories only"],
    ["Saturday", "Test day: squat, bench, deadlift (3 attempts each)"],
])}
<h3>Choosing your attempts</h3>
<ul>
<li><strong>Opener:</strong> a weight you could triple on a bad day, roughly 90% of your estimated max.</li>
<li><strong>Second:</strong> about 95%, a confident lift.</li>
<li><strong>Third:</strong> 100–102% if the second moved well; repeat the second plus 2.5 kg if it was slow.</li>
</ul>
<p>Estimate your max from week 11's top single with the {L('/how-to-calculate-your-1rm/', '1RM calculator guide')}. Use spotters on squat and bench, or safety bars set just below the bottom position.</p>
"""),
        ("nutrition", "Nutrition, Recovery and Body Weight", f"""
<p>Eat about 1.6–2.2 g of protein per kg of body weight daily; a {cite('protein2018', 'meta-analysis of 49 trials')} found muscle gains plateaued near 1.6 g/kg. Beginners do not need to cut weight for a weight class; eat at maintenance or slightly above and let strength rise. Creatine monohydrate at 3–5 g per day is the {cite('creatine', 'best-supported supplement')} for strength training and is optional.</p>
"""),
        ("next", "After the Test Day", f"""
<p>Take an easy week, then rerun the program with your new numbers. A second 12-week cycle is usually just as productive for a beginner. Once progress across a full cycle slows, it is time for more volume and longer phases. Typical strength levels by age and body weight are in our guides to the {L('/average-squat-weight/', 'average squat')}, {L('/average-bench-press-by-age-weight-and-sex/', 'average bench press')} and {L('/is-your-deadlift-good-average-weights-by-level-age/', 'average deadlift')}.</p>
"""),
    ],
    "schedule": [("Mon", "Day 1", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Day 2", "c2"), ("Thu", "Rest", "rest"), ("Fri", "Day 3", "c1"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Squat + Bench", "title": "Day 1 — Squat & Bench Volume", "tag": "Weeks 1–4", "color": 4, "time": "65–80 min", "focus": "Squat / Bench / Upper back",
         "exercises": [
             ("Back Squat (competition depth)", "Primary: quads, glutes · Secondary: adductors, back", "4 × 6", "3–4 min", "RPE 7"),
             ("Barbell Bench Press (touch-and-go)", "Primary: chest · Secondary: front delts, triceps", "3 × 8", "3 min", "RPE 7"),
             ("Barbell Row", "Primary: upper back, lats", "3 × 8–10", "2 min", "RPE 7–8"),
             ("Leg Press", "Primary: quads", "2 × 10–12", "2 min", "RPE 7–8"),
             ("Hanging Knee Raise", "Primary: abs", "3 × 10–15", "60 sec", "RPE 8"),
         ],
         "notes": "Film a side view of your top squat set each week to check depth. Use the same stance and bar position every session."},
        {"tab": "Day 2", "tab_sub": "Deadlift + Bench", "title": "Day 2 — Deadlift & Paused Bench", "tag": "Weeks 1–4", "color": 2, "time": "65–80 min", "focus": "Deadlift / Bench / Back",
         "exercises": [
             ("Deadlift (conventional or sumo)", "Primary: glutes, hamstrings, back · Secondary: quads, grip", "3 × 5", "3–5 min", "RPE 7"),
             ("Paused Bench Press (1-second pause)", "Primary: chest · Secondary: triceps, front delts", "4 × 5", "3–4 min", "RPE 7"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 8–12", "90 sec", "RPE 8"),
             ("45° Back Extension", "Primary: spinal erectors, glutes", "3 × 10–12", "90 sec", "RPE 7–8"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 10–12", "60 sec", "RPE 8"),
         ],
         "notes": "Pick sumo or conventional in week 1 and keep it for the full 12 weeks. Pause until the bar is still on the chest, then press."},
        {"tab": "Day 3", "tab_sub": "Technique", "title": "Day 3 — Paused Squat & Variations", "tag": "Weeks 1–4", "color": 1, "time": "60–75 min", "focus": "Squat / Bench / Hinge",
         "exercises": [
             ("Paused Back Squat (2-second pause)", "Primary: quads, glutes · Builds position in the hole", "3 × 5", "3 min", "RPE 6–7"),
             ("Close-Grip Bench Press", "Primary: triceps, chest", "3 × 6–8", "2–3 min", "RPE 7"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 6–8", "2–3 min", "RPE 7"),
             ("Chest-Supported Dumbbell Row", "Primary: upper back, rear delts", "3 × 10–12", "90 sec", "RPE 8"),
             ("Face Pull", "Primary: rear delts, rotator cuff", "2 × 15", "60 sec", "RPE 8"),
         ],
         "notes": "Paused squats use about 80–85% of the load you would use for regular squats at the same reps. Keep the torso tight through the pause."},
    ],
    "faq_title": "Powerlifting Program for Beginners FAQ",
    "faqs": [
        ("How long should you lift before starting powerlifting?", "About six months of consistent training is enough for most people, as long as you can squat, bench and deadlift with repeatable technique."),
        ("Do I need powerlifting gear as a beginner?", "Flat-soled shoes and chalk help. A lifting belt is useful once loads get heavy but is optional. Knee sleeves and wrist wraps are personal preference."),
        ("Can I do cardio while powerlifting?", "Yes. Two or three easy 20–30 minute sessions a week support health and work capacity. Avoid hard leg conditioning before Day 1 or Day 2."),
        ("Should beginners max out often?", "No. Heavy singles are a skill to practise in a controlled way, which is why they appear only in weeks 9–11 at RPE 8 before a single test day."),
        ("Can women use this powerlifting program?", "Yes. The lifts and progression are the same. Many women find bench progress slower in absolute kilograms, so use smaller jumps of 1–1.25 kg when available."),
        ("Do I have to compete?", "No. Running the test day in your gym gives you the same benchmark. Entering a local novice meet is a good next step if you enjoy it."),
    ],
    "related": ["5x5-workout", "beginner-strength-training-program", "upper-lower-split", "3-day-full-body-workout"],
    "refs": refs("rpe2016", "freqstr2018", "currier2023", "load2021", "acsm2026", "rest2018", "taper2020", "protein2018", "creatine"),
    "disclaimer": DISCLAIMER,
}
