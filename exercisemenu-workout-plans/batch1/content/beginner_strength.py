from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 13,
    "slug": "beginner-strength-training-program",
    "title": "Beginner Workout Plan: 12-Week Strength Training Program (3 Days)",
    "meta_title": "Beginner Workout Plan: 12-Week Strength Program (3 Days)",
    "meta_desc": "A 12-week beginner workout plan for getting stronger: three gym days, sets of 5 on the main barbell lifts, simple weekly progression and safe warm-ups.",
    "focus_kw": "beginner workout plan",
    "badge": "Beginner · Strength",
    "hero_lead": "New to the barbell and want to get strong? This beginner workout plan teaches the squat, bench press, deadlift and overhead press, then adds weight to them every week for 12 weeks, with sessions under an hour.",
    "hero_meta": ["📅 3 days/week", "⏱ 45–60 min", "📊 Beginner (0–6 months)", "🏋️ Barbell + basic gym"],
    "stats": [("12 wk", "Program length"), ("3", "Training days"), ("3 × 5", "Main lift sets"), ("+2.5–5 kg", "Weekly jumps"), ("4", "Barbell lifts learned")],
    "quick_answer": "This beginner workout plan runs three full-body days a week for 12 weeks. Days 1 and 2 build strength with 3 sets of 5 on the squat, bench press, deadlift and overhead press. Day 3 uses lighter sets of 8. You add a small amount of weight to each main lift every week while form stays solid.",
    "intro": "<p>A good beginner workout plan is simple enough to follow without thinking and specific enough to make you stronger every week. This 12-week program does both. You train three days a week, master four barbell lifts, and follow one progression rule.</p><p>Beginners usually gain strength quickly, and much of that early progress comes from learning the movements. That's why this plan trains each main pattern at least twice a week and keeps the rep counts low enough to focus on form.</p>",
    "sections": [
        ("why", "Why a Strength-First Plan for Beginners?", f"""
<p>Getting stronger first lets you use heavier loads later in muscle-building training. The {cite('acsm2026', '2026 ACSM position stand')} found resistance training also improves physical function, and that strength improved most with heavier loads (80% of your one-rep max or more), 2–3 sets per exercise, lifts placed at the start of the session, and two or more sessions a week. This plan follows each of those points.</p>
{box("science", "🔬 Beginners also build muscle", f"<p>Training for strength builds muscle too. In a {cite('load2021', 'network meta-analysis')}, untrained participants showed greater muscle growth than trained ones, and growth was similar across load ranges. Heavy sets of 5 on the main lifts plus 8–12 rep accessories cover both goals.</p>")}
<p>If your main goal is muscle size rather than strength, our {L('/workout-plans/full-body-workout-plan/', 'full body workout plan for beginners')} is the better starting point.</p>
"""),
        ("who", "Who This Beginner Program Is For", f"""
<ul>
<li>You have lifted for less than six months, or not at all.</li>
<li>You have access to a barbell, squat rack, bench and a few dumbbells and machines.</li>
<li>You can train three non-consecutive days a week for 45–60 minutes.</li>
<li>You are healthy and free of injuries that limit squatting, hinging or pressing.</li>
</ul>
<p>Not sure about sets and reps yet? The {L('/how-many-reps-and-sets-should-a-beginner-do/', 'beginner sets and reps guide')} explains the basics behind this plan.</p>
"""),
        ("schedule", "Weekly Schedule", f"""
{WEEK}
<p>Day 1 and Day 3 both train squat and bench, so keep at least one rest day between all sessions. Tuesday/Thursday/Saturday works equally well.</p>
"""),
        ("workouts", "The Beginner Workouts", f"""
<p>Pick a day. Effort is shown as reps in reserve (RIR). Beginners should finish main-lift sets with 2–3 clean reps left; the bar should move at a steady speed on the last rep. The {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains how to judge this.</p>
{TABS}
<p>Form guides for the main lifts: {L('/how-to-bench-press/', 'how to bench press')}, {L('/how-to-deadlift-for-beginners/', 'how to deadlift for beginners')} and {L('/types-of-squats/', 'squat variations explained')}.</p>
"""),
        ("phases", "The 12 Weeks at a Glance", f"""
{table(["Weeks", "Phase", "Main-lift loads", "Goal"], [
    ["1–2", "Learn", "Empty bar to light; RIR 3–4", "Groove technique, find starting weights"],
    ["3–8", "Build", "Add 2.5 kg (upper) / 5 kg (lower) each week", "Steady weekly strength gains"],
    ["9–11", "Grind smart", "Smaller jumps: 1–1.25 kg (upper) / 2.5 kg (lower)", "Keep progressing as jumps get harder"],
    ["12", "Recover & review", "Day 1 and 2 loads from week 10; half the accessory sets", "Recover, compare logs, choose next plan"],
])}
<p>Day 3 squat uses about 85–90% of that week's Day 1 squat load for 3 sets of 8. It adds practice and volume without another heavy day.</p>
"""),
        ("progression", "How to Progress Every Week", f"""
<p>Use one rule: if you completed all 3 sets of 5 with good form and at least 1–2 reps in reserve, add weight next week. This is linear progression, the most direct form of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
{table(["Week", "Squat (Day 1)", "Bench (Day 1)", "Result"], [
    ["3", "60 kg × 5, 5, 5", "40 kg × 5, 5, 5", "All reps, solid form"],
    ["4", "65 kg × 5, 5, 5", "42.5 kg × 5, 5, 5", "All reps"],
    ["5", "70 kg × 5, 5, 4", "45 kg × 5, 5, 5", "Squat missed one rep: repeat 70 kg"],
    ["6", "70 kg × 5, 5, 5", "47.5 kg × 5, 5, 5", "Back on track"],
])}
<p><strong>If you miss reps two weeks in a row</strong> at the same load, drop that lift by 10% and build back up with half-size jumps. The {cite('acsm2009', 'ACSM progression guidelines')} use 2–10% load increases, which matches 2.5–5 kg on most beginner lifts. Accessories use double progression: reach the top of the rep range on all sets, then add the next dumbbell or plate. More examples are in {L('/progressive-overload-for-beginners/', 'progressive overload for beginners')}.</p>
"""),
        ("rest", "Rest Periods and Warm-Ups", f"""
<p>Rest about 2 minutes between main-lift sets and 60–90 seconds between accessory sets. A {cite('rest2018', 'systematic review on rest intervals')} found that for untrained lifters, 60–120 second rests were enough to maximise strength gains; longer rests mattered more for trained lifters. If a set of 5 feels heavy, take up to 3 minutes.</p>
<h3>Warm-up (8–10 minutes)</h3>
<ol class="emp-steps">
<li>5 minutes of easy cardio (bike, rower or brisk walk).</li>
<li>Bodyweight squats × 10, hip hinges × 10, arm circles × 10 each way.</li>
<li>Ramp-up sets: empty bar × 8–10, then 2–3 sets of 3–5 reps working up to your work weight.</li>
</ol>
<p>The {L('/warm-up-set-calculator/', 'warm-up set calculator')} works out the ramp-up loads for you. A standard men's Olympic barbell weighs 20 kg and a women's Olympic bar 15 kg; see {L('/how-much-does-a-barbell-weigh/', 'how much a barbell weighs')} for other bars.</p>
"""),
        ("mistakes", "Beginner Mistakes to Avoid", f"""
<ul>
<li><strong>Starting too heavy.</strong> Beginning light gives you many weeks of steady progress instead of stalling early.</li>
<li><strong>Chasing failure.</strong> Grinding reps makes good form harder to keep. A {cite('failure2023', 'meta-analysis')} found training to failure added little for muscle growth compared with stopping short.</li>
<li><strong>Skipping the log.</strong> Write down every set. Our {L('/how-to-track-your-workouts/', 'workout tracking guide')} shows how.</li>
<li><strong>Adding extra days or exercises.</strong> More is not better in the first months. Recovery is when you adapt.</li>
<li><strong>Ignoring pain.</strong> Normal muscle soreness fades in a few days. Sharp or joint pain means stop the lift and get it checked.</li>
</ul>
"""),
        ("nutrition", "Eating for Strength Gains", f"""
<p>Eat about 1.6 g of protein per kg of body weight daily; muscle gains plateaued near 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}. Get enough total food to support training: if you want to gain weight, eat a little above maintenance; if you want to lose fat, a modest deficit usually still allows strength gains as a beginner. Use the {L('/protein-calculator/', 'protein calculator')} to set your target.</p>
"""),
        ("next", "What to Do After 12 Weeks", f"""
<p>Once weekly jumps stall even with smaller increments, you have outgrown simple linear progression. The next step is a program that mixes heavy, light and medium days and progresses more slowly, such as our {L('/workout-plans/3-day-full-body-workout/', '3-day full body workout for intermediates')} if you still train three days, or our {L('/workout-plans/upper-lower-split/', '4-day upper lower split')} if you can add a day.</p>
"""),
    ],
    "schedule": [("Mon", "Day 1", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Day 2", "c2"), ("Thu", "Rest", "rest"), ("Fri", "Day 3", "c1"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Squat + Bench", "title": "Day 1 — Squat & Bench (Heavy)", "tag": "3 × 5", "color": 4, "time": "45–60 min", "focus": "Full body",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors, core", "3 × 5", "2–3 min", "RIR 2–3"),
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 5", "2–3 min", "RIR 2–3"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 8–10", "90 sec", "RIR 2"),
             ("Dumbbell Romanian Deadlift", "Primary: hamstrings, glutes", "2 × 10–12", "90 sec", "RIR 2"),
             ("Plank", "Primary: abs, deep core", "3 × 20–40 sec", "60 sec", "Stop before form breaks"),
         ],
         "notes": "Use a spotter or set the rack safety bars for bench press. Squat to at least parallel (hip crease level with the top of the knee) if your mobility allows."},
        {"tab": "Day 2", "tab_sub": "Deadlift + Press", "title": "Day 2 — Deadlift & Overhead Press (Heavy)", "tag": "3 × 5", "color": 2, "time": "45–55 min", "focus": "Full body",
         "exercises": [
             ("Trap Bar Deadlift", "Primary: glutes, quads, hamstrings · Secondary: upper back, grip", "3 × 5", "2–3 min", "RIR 2–3"),
             ("Standing Overhead Press", "Primary: shoulders · Secondary: triceps, upper chest", "3 × 5", "2 min", "RIR 2–3"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, lats", "3 × 8–10", "90 sec", "RIR 2"),
             ("Goblet Squat", "Primary: quads, glutes", "2 × 8–10", "90 sec", "RIR 2–3"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "2 × 10–12", "60 sec", "RIR 2"),
         ],
         "notes": "No trap bar? Use a conventional barbell deadlift for 1–2 sets of 5 after a careful warm-up. Reset your position before every rep."},
        {"tab": "Day 3", "tab_sub": "Volume", "title": "Day 3 — Squat & Press (Volume)", "tag": "3 × 8", "color": 1, "time": "45–55 min", "focus": "Full body",
         "exercises": [
             ("Back Squat", "85–90% of this week's Day 1 load", "3 × 8", "2 min", "RIR 2–3"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: triceps", "3 × 8–10", "90 sec", "RIR 2"),
             ("Barbell Row", "Primary: mid-back · Secondary: rear delts, biceps", "3 × 8", "90 sec", "RIR 2"),
             ("Seated Leg Curl", "Primary: hamstrings", "2 × 10–12", "60–90 sec", "RIR 2"),
             ("Triceps Pushdown", "Primary: triceps", "2 × 10–12", "60 sec", "RIR 2"),
             ("Dead Bug", "Primary: abs, deep core", "2 × 8 / side", "60 sec", "Slow and controlled"),
         ],
         "notes": "Day 3 should feel moderate. If squats move slowly, lower the load; this session builds practice, not maximum strength."},
    ],
    "faq_title": "Beginner Workout Plan FAQ",
    "faqs": [
        ("How much weight should a beginner start with?", "Start with a load you can lift for 5 reps with 3–4 reps left, often just the empty bar for presses and squats. Starting light gives more weeks of steady progress."),
        ("Is 3 days a week enough for a beginner?", "Yes. Three full-body sessions train every pattern two or three times a week, which is plenty for strength and muscle in the first months of lifting."),
        ("Should beginners do cardio too?", "Yes. Two or three sessions of 20–30 minutes of moderate cardio per week support heart health. Do them on rest days or after lifting, not before heavy squats."),
        ("Can women follow this beginner workout plan?", "Yes. Women gain strength at similar or faster relative rates than men in the early months of training, and the same lifts and progression work."),
        ("What if I can't squat or deadlift with a barbell yet?", "Use a goblet squat and dumbbell Romanian deadlift for the first 2–4 weeks, then move to the barbell once the movement feels natural."),
        ("When will I see results?", "Strength usually rises within the first two weeks as your technique improves. Visible muscle changes often take 8–12 weeks of consistent training and eating."),
    ],
    "related": ["full-body-workout-plan", "5x5-workout", "3-day-full-body-workout", "powerlifting-program-for-beginners"],
    "refs": refs("acsm2026", "load2021", "acsm2009", "rest2018", "failure2023", "protein2018", "sex2020"),
    "disclaimer": DISCLAIMER,
}
