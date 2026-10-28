from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 9,
    "slug": "hypertrophy-program",
    "title": "4-Day Hypertrophy Program: A 6-Week Muscle-Building Mesocycle",
    "meta_title": "4-Day Hypertrophy Program: 6-Week Muscle Building Plan",
    "meta_desc": "A 4-day hypertrophy program run as a 6-week mesocycle: anterior/posterior split, weekly set ramps, RIR targets and a planned deload for steady growth.",
    "focus_kw": "hypertrophy program",
    "badge": "Muscle Growth Focus",
    "hero_lead": "This hypertrophy program has one goal: more muscle. It uses a 4-day anterior/posterior split, a 6-week block that ramps effort and sets week by week, and exercise choices that load each muscle through a full stretch.",
    "hero_meta": ["📅 4 days/week", "⏱ 55–70 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("6 wk", "Mesocycle"), ("2×", "Frequency/muscle"), ("10–14", "Peak sets/major muscle"), ("RIR 3→0", "Effort ramp"), ("26", "Exercises")],
    "quick_answer": "This 4-day hypertrophy program alternates anterior days (quads, chest, front delts, biceps) with posterior days (back, hamstrings, glutes, triceps, calves). It runs as a 6-week mesocycle: effort rises from 3 reps in reserve to near failure, sets increase in week 3, and week 6 is a deload.",
    "takeaways": [
        "Most sets use 8–15 reps; load matters less for growth than effort and weekly volume.",
        "Effort climbs each week (RIR 3 → 2 → 2 → 1 → 0–1) so fatigue peaks just before the deload.",
        "Weekly sets for the major muscles rise from about 10–12 to 11–14 during weeks 3–5.",
        "Exercises are chosen to load muscles at long lengths, such as seated leg curls and incline curls.",
        "Repeat the 6-week block 2–3 times, adding small amounts of load or a set where you recovered well.",
    ],
    "intro": "<p>Strength programs chase heavier weights. A hypertrophy program chases productive sets: enough of them, taken close enough to failure, on exercises that load the muscle well, for long enough to see change. Everything in this plan serves that one aim.</p><p>You get a complete 4-day split, a week-by-week effort and volume plan, and the reasoning from current research behind each choice, so you can adjust it without guessing.</p>",
    "sections": [
        ("principles", "What Makes a Program Good for Hypertrophy?", f"""
<p>Four variables do most of the work. The {cite('acsm2026', '2026 ACSM position stand')}, which pooled 137 systematic reviews, found muscle growth was enhanced by higher weekly volume (10 or more sets per muscle) and eccentric overload, while many other details had inconsistent effects.</p>
{table(["Variable", "This program", "Evidence"], [
    ["Weekly sets per muscle", "10–14 for major muscles", f"{cite('vol2017', 'More sets → more growth')} (dose-response)"],
    ["Load / reps", "Mostly 8–15 reps, compounds 6–10", f"{cite('load2021', 'Growth similar across load ranges')}"],
    ["Proximity to failure", "RIR 3 → 0–1 over 5 weeks", f"{cite('failure2023', 'Failure not required for growth')}"],
    ["Frequency", "2× per muscle per week", f"{cite('freq2016', '2× beat 1× per week')}"],
])}
<p>Two smaller levers round it out: rest long enough to keep rep quality high, and train through a full range of motion with emphasis on the stretched position.</p>
{box("science", "🔬 Long muscle lengths", f"<p>In a {cite('maeo2021', 'within-person trial')}, seated leg curls (hamstrings stretched at the hip) built about 14% more hamstring volume versus 9% for lying curls. A {cite('wolf2025', '2025 study in trained lifters')} found that partial reps in the stretched position produced similar growth to full reps. This plan uses full range of motion and picks exercises that stretch the target muscle under load.</p>")}
"""),
        ("split", "Why an Anterior/Posterior Split?", f"""
<p>An anterior/posterior split divides the body front and back instead of upper and lower. Anterior days train quads, chest, front and side delts, and biceps. Posterior days train back, hamstrings, glutes, rear delts, triceps and calves.</p>
<ul>
<li><strong>Balanced session length.</strong> Each day mixes one big lower-body lift with upper-body work, so no day is a 75-minute leg session.</li>
<li><strong>Less overlap.</strong> Biceps are trained on chest days and triceps on back days, so arms are fresh for their direct work.</li>
<li><strong>Two exposures per muscle.</strong> Each anterior and posterior session runs twice a week.</li>
</ul>
<p>If you prefer splitting by upper and lower body, our {L('/workout-plans/4-day-workout-split/', '4-day workout split')} compares the main options.</p>
"""),
        ("schedule", "Weekly Schedule", f"""
{WEEK}
<p>Two days on, one off, two on, two off. Each anterior and posterior session is 72 hours apart from its repeat.</p>
"""),
        ("mesocycle", "The 6-Week Mesocycle", f"""
<p>A mesocycle is a training block that builds fatigue on purpose and then clears it. Here, you start each block comfortably and finish it working hard, then deload.</p>
{table(["Week", "Sets", "Target effort", "Goal"], [
    ["1", "Base (as listed)", "RIR 3", "Learn loads, low soreness"],
    ["2", "Base", "RIR 2", "Add reps or load from week 1"],
    ["3", "+1 set on the first two exercises each day", "RIR 2", "Volume step"],
    ["4", "Same as week 3", "RIR 1", "Push reps"],
    ["5", "Same as week 3", "RIR 1 (compounds), 0–1 (isolation)", "Peak week"],
    ["6", "Half the base sets", "RIR 3–4", "Deload and recover"],
])}
<p>Week 6 follows the consensus definition from a {cite('delphi2023', 'Delphi study of coaches and researchers')}: a period of reduced training stress to reduce fatigue and prepare for the next block. In practice, athletes in a {cite('deload2024', 'cross-sectional survey')} deloaded about every 5–6 weeks by cutting sets and reps, close to the rhythm used here. More on timing is in our {L('/what-is-a-deload-week/', 'deload week guide')}.</p>
"""),
        ("workouts", "The Hypertrophy Workouts", f"""
<p>Choose a day. Sets shown are the week 1–2 base. Effort uses reps in reserve; read the {L('/rpe-vs-rir/', 'RPE vs RIR guide')} if you need a refresher, and follow the week's target from the table above.</p>
{TABS}
"""),
        ("volume", "Weekly Volume: Base vs Peak", f"""
{table(["Muscle", "Weeks 1–2", "Weeks 3–5"], [
    ["Quads", "11", "13"],
    ["Chest", "12", "14"],
    ["Back (lats & mid-back)", "12", "13"],
    ["Hamstrings", "≈ 10.5", "≈ 13"],
    ["Glutes", "≈ 8.5", "≈ 11"],
    ["Biceps", "≈ 12", "≈ 12.5"],
    ["Triceps", "≈ 10.5", "≈ 11.5"],
    ["Side delts", "8", "8"],
    ["Rear delts", "≈ 6", "≈ 6"],
    ["Calves", "6", "6"],
])}
<p>Direct sets count as 1, indirect sets as 0.5, following the fractional method that best predicted outcomes in the {cite('pelland2026', 'Pelland 2026 meta-regression')}. That analysis also found diminishing returns as volume climbs, so the plan adds sets in small steps instead of doubling them. If one muscle lags after two blocks, add 2 sets for that muscle to the peak weeks. The {L('/training-volume-calculator/', 'training volume calculator')} helps you total your own numbers.</p>
"""),
        ("progression", "How to Progress Inside and Between Blocks", f"""
<p><strong>Inside a block:</strong> keep the same exercises for all six weeks. Each week, aim to beat last week's reps or load at the new RIR target. Because the target RIR gets lower, reps often rise even at the same weight.</p>
<p><strong>Between blocks:</strong> start block two with week 1 loads about 2.5–5% above block one's week 1. Keep 70–80% of exercises; swap only ones that caused joint pain or felt like they did not train the target muscle. This keeps {L('/what-is-progressive-overload/', 'progressive overload')} measurable.</p>
{box("warn", "⚠️ Signs you need to deload early", "<p>Loads dropping on two sessions in a row, joint pain that lasts into the next session, or sleep and motivation falling off for a week. Take the deload, then restart the block at week 2.</p>")}
"""),
        ("technique", "Technique Rules for Every Set", f"""
<ul>
<li><strong>Control the lowering.</strong> Take about 2–3 seconds on the eccentric to keep tension on the muscle and every rep consistent.</li>
<li><strong>Full range, with a pause in the stretch.</strong> One second at the bottom of presses, curls and leg curls removes bounce.</li>
<li><strong>Rest for performance.</strong> 2–3 minutes on compounds, 60–90 seconds on isolation work. Trained men grew more with {cite('rest2016', '3-minute than 1-minute rests')} on compound lifts.</li>
<li><strong>Count only hard sets.</strong> Warm-up sets do not count toward weekly volume. See {L('/warm-up-sets-vs-working-sets/', 'warm-up sets vs working sets')}.</li>
</ul>
<p>Apply these on every working set and the program does the rest.</p>
"""),
        ("nutrition", "Nutrition for Hypertrophy", f"""
<p>Eat about 1.6–2.2 g of protein per kg of body weight daily; gains from protein plateaued around 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}. A small calorie surplus speeds growth, though the {cite('surplus2019', 'ideal size of that surplus is not known')}; a weight gain of about 0.25–0.5% of body weight per week is a sensible target. Calculate your protein with the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
    ],
    "schedule": [("Mon", "Anterior A", "c1"), ("Tue", "Posterior A", "c2"), ("Wed", "Rest", "rest"), ("Thu", "Anterior B", "c6"), ("Fri", "Posterior B", "c5"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Anterior A", "title": "Day 1 — Anterior A", "tag": "Quads · Chest · Biceps", "color": 1, "time": "60–70 min", "focus": "Quads / Chest / Delts / Biceps",
         "exercises": [
             ("Back Squat (or Hack Squat)", "Primary: quads · Secondary: glutes, adductors", "3 × 6–10", "2–3 min", "Week target"),
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 6–10", "2–3 min", "Week target"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest", "3 × 8–12", "2 min", "Week target"),
             ("Leg Extension", "Primary: quads (rectus femoris)", "3 × 10–15", "90 sec", "Week target"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "4 × 12–20", "60 sec", "Week target"),
             ("Incline Dumbbell Curl", "Primary: biceps (long head)", "3 × 10–15", "60–90 sec", "Week target"),
         ],
         "notes": "Lower the bench press to the chest with a brief pause. Set the leg extension seat back slightly so the quads stretch at the bottom."},
        {"tab": "Day 2", "tab_sub": "Posterior A", "title": "Day 2 — Posterior A", "tag": "Back · Hamstrings · Triceps", "color": 2, "time": "60–70 min", "focus": "Back / Hamstrings / Triceps / Calves",
         "exercises": [
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 6–10", "2–3 min", "Week target"),
             ("Pull-Up (or Lat Pulldown)", "Primary: lats · Secondary: biceps", "3 × 6–10", "2–3 min", "Week target"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, rear delts", "3 × 8–12", "2 min", "Week target"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–15", "90 sec", "Week target"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–15", "60–90 sec", "Week target"),
             ("Standing Calf Raise", "Primary: calves", "3 × 10–15", "60 sec", "Week target"),
         ],
         "notes": "On RDLs, push the hips back until you feel a strong hamstring stretch, usually just below the knee. Pause 1–2 seconds at the bottom of every calf raise."},
        {"tab": "Day 3", "tab_sub": "Anterior B", "title": "Day 3 — Anterior B", "tag": "Quads · Chest · Biceps", "color": 6, "time": "55–65 min", "focus": "Quads / Chest / Delts / Biceps",
         "exercises": [
             ("Leg Press", "Primary: quads · Secondary: glutes", "3 × 10–15", "2 min", "Week target"),
             ("Machine Chest Press", "Primary: chest · Secondary: triceps", "3 × 8–12", "2 min", "Week target"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "2 × 8–12 / leg", "2 min", "Week target"),
             ("Cable Fly", "Primary: chest", "3 × 12–15", "60–90 sec", "Week target"),
             ("Cable Lateral Raise", "Primary: side delts", "4 × 12–20", "60 sec", "Week target"),
             ("Barbell Curl", "Primary: biceps", "3 × 8–12", "90 sec", "Week target"),
             ("Cable Crunch", "Primary: abs", "2 × 10–15", "60 sec", "Week target"),
         ],
         "notes": "Run cable lateral raises behind the body so the side delt is loaded at the bottom of the rep."},
        {"tab": "Day 4", "tab_sub": "Posterior B", "title": "Day 4 — Posterior B", "tag": "Back · Glutes · Triceps", "color": 5, "time": "60–70 min", "focus": "Back / Glutes / Hamstrings / Triceps",
         "exercises": [
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "3 × 8–12", "2 min", "Week target"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–15", "90 sec", "Week target"),
             ("Lat Pulldown (close grip)", "Primary: lats", "3 × 10–12", "2 min", "Week target"),
             ("One-Arm Dumbbell Row", "Primary: lats, mid-back", "3 × 8–12", "90 sec", "Week target"),
             ("Reverse Pec Deck", "Primary: rear delts", "3 × 12–20", "60 sec", "Week target"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 10–15", "60 sec", "Week target"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "3 × 12–15", "60 sec", "Week target"),
         ],
         "notes": "Superset reverse pec deck with triceps pushdowns. On the one-arm row, let the shoulder blade stretch forward at the bottom of each rep."},
    ],
    "faq_title": "Hypertrophy Program FAQ",
    "faqs": [
        ("What rep range is best for hypertrophy?", "Muscle grows across a wide range, roughly 5 to 30 reps, when sets end close to failure. Most sets here sit at 8–15 because that range is time-efficient and easy on the joints."),
        ("Do I need to train to failure to build muscle?", "No. Stopping one or two reps short builds similar muscle with less fatigue. This plan only takes isolation sets to 0–1 RIR in the peak week."),
        ("Can I run this hypertrophy program while cutting?", "Yes, but keep sets at the week 1–2 base level for the whole block, because recovery is lower in a calorie deficit. Keep loads as heavy as possible to hold muscle."),
        ("How many blocks should I run before changing programs?", "Two to three 6-week blocks is typical. Change the program when progress stalls across a full block despite good sleep and nutrition, not because of boredom."),
        ("Is this hypertrophy program suitable for women?", "Yes. Women and men grow at similar relative rates on the same program. Many women add one extra set of hip thrusts and split squats in place of a chest set."),
        ("How long are the sessions?", "About 55–70 minutes, including a short warm-up. Supersetting the last two exercises saves 10 minutes if needed."),
    ],
    "related": ["ppl-hypertrophy-program", "4-day-workout-split", "upper-lower-split", "lean-bulk-workout-plan"],
    "refs": refs("acsm2026", "vol2017", "load2021", "failure2023", "freq2016", "maeo2021", "wolf2025", "delphi2023", "deload2024", "pelland2026", "rest2016", "protein2018", "surplus2019", "sex2020"),
    "disclaimer": DISCLAIMER,
}
