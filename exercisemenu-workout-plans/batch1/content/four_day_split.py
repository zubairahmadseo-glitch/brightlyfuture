from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 6,
    "slug": "4-day-workout-split",
    "title": "4-Day Workout Split: The Torso/Limbs Plan for Muscle and Strength",
    "meta_title": "4 Day Workout Split: Train Every Muscle Twice (Free Plan)",
    "meta_desc": "Free 4 day workout split that hits every muscle twice a week: torso and limbs days with sets, reps and rest, plus how it compares to upper/lower.",
    "focus_kw": "4 day workout split",
    "badge": "2× Frequency in 4 Days",
    "hero_lead": "Four sessions a week is enough to train every muscle twice, as long as the days are split the right way. This plan uses a torso/limbs split with a heavier A rotation and a higher-rep B rotation.",
    "hero_meta": ["📅 4 days/week", "⏱ 60–75 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("4", "Training days"), ("2×", "Frequency/muscle"), ("10–14", "Sets/major muscle/wk"), ("8 wk", "Block length"), ("A/B", "Heavy + volume")],
    "quick_answer": "A good 4-day workout split trains each muscle twice a week, which keeps sessions shorter and helps strength. This plan alternates torso days (chest, back, shoulders) with limbs days (legs, biceps, triceps) on Monday, Tuesday, Thursday and Friday, using one heavier and one higher-rep version of each day.",
    "intro": "<p>Use the day tabs to see each workout. After the workouts you'll find weekly sets, progression rules and how the other 4-day splits compare.</p>",
    "sections": [
        ("schedule", "4-Day Workout Split Schedule", f"""
<p>The week runs on two on, one off, two on, two off. Each muscle gets one heavy and one volume session with at least 72 hours between them.</p>
{WEEK}
<p>Shift-workers can use any four days as long as Torso A and Torso B are not back to back. A Monday/Wednesday/Friday/Saturday pattern also works if Wednesday is Limbs A.</p>
"""),
        ("workouts", "The Workouts: Torso and Limbs, A and B", f"""
<p>Choose a day below. <strong>A days</strong> open with heavier compound lifts at 5–8 reps and longer rests. <strong>B days</strong> use 8–15 reps, more machines and cables, and shorter rests on isolation work. Effort is shown as reps in reserve (RIR); if you are new to it, the {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains how to judge it.</p>
{TABS}
{box("science", "🔬 Why mix heavy and moderate loads?", f"<p>A {cite('load2021', 'network meta-analysis of 28 studies')} found muscle growth was similar across light, moderate and heavy loads, but strength gains were greater with heavier loads. A {cite('currier2023', '2023 Bayesian network meta-analysis')} ranked higher-load, multi-set training two to three times a week as the top prescriptions for strength and size. A/B rotation gives you both: heavy work for strength, moderate-rep volume for size.</p>")}
"""),
        ("volume", "Weekly Sets per Muscle", f"""
<p>Direct sets count fully; indirect sets (for example, biceps during rows) count as half, following the method that best predicted results in the {cite('pelland2026', 'Pelland 2026 analysis')}.</p>
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "13", "–", "13"],
    ["Back (lats, mid-back)", "14", "–", "14"],
    ["Side delts", "8", "Shoulder press 3 → 1.5", "≈ 9.5"],
    ["Rear delts", "3", "Rows 7 → 3.5", "≈ 6.5"],
    ["Quads", "11", "–", "11"],
    ["Hamstrings", "9", "–", "9"],
    ["Glutes", "3", "Squat, leg press, RDL 11 → 5.5", "≈ 8.5"],
    ["Biceps", "6", "Pulls & rows 14 → 7", "≈ 13"],
    ["Triceps", "6", "Presses 11 → 5.5", "≈ 11.5"],
    ["Calves", "6", "–", "6"],
])}
<p>The {cite('acsm2026', '2026 ACSM position stand')} ties greater hypertrophy to 10 or more weekly sets per muscle. Chest, back, quads, biceps and triceps clear that mark. If rear delts or calves are a priority, add 2 sets of face pulls to Torso A and 2 sets of calf raises to Limbs A. See {L('/how-many-sets-per-muscle-group-per-week/', 'how many sets per muscle group per week')} to fine-tune.</p>
"""),
        ("progression", "Progression Rules", f"""
<p><strong>A days (heavy):</strong> when every set reaches the top of the range at RIR 2 (e.g., 4 × 7 on bench), add 2.5 kg to upper-body lifts or 5 kg to squats. If you miss the bottom of the range two sessions in a row, drop the load 5–10% and build back up.</p>
<p><strong>B days (volume):</strong> add reps until every set reaches the top of the range, then add the smallest available load. The {cite('acsm2009', 'ACSM progression model')} recommends 2–10% load jumps once you exceed the target reps by one or two. Log every session; the {L('/how-to-track-your-workouts/', 'workout tracking guide')} shows a simple format, and {L('/what-is-progressive-overload/', 'progressive overload')} explains the principle.</p>
"""),
        ("deload", "Deload and Long-Term Plan", f"""
<p>Train weeks 1–7 as written, then deload in week 8. Keep the same four days and exercises, cut sets by about half, and stop every set at RIR 3–4. A {cite('delphi2023', 'Delphi consensus of coaches and researchers')} defines a deload as a planned period of reduced training stress to manage fatigue and prepare for the next block.</p>
<p>After the deload, start block two with loads about 2.5–5% heavier than block one's week 1. Swap 1–2 accessory exercises per day if they feel stale, but keep the main lifts so progress stays measurable. Our {L('/what-is-a-deload-week/', 'deload week guide')} covers signs you need one earlier.</p>
"""),
        ("options", "Which 4-Day Split Should You Choose?", f"""
{table(["4-day split", "Layout", "Frequency/muscle", "Best for"], [
    ["Torso/Limbs (this plan)", "Torso A · Limbs A · Torso B · Limbs B", "2×", "Arms and legs trained twice a week"],
    ["Upper/Lower", "Upper · Lower · Upper · Lower", "2×", "Strength focus; simplest to run"],
    ["PPL + Upper", "Push · Pull · Legs · Upper", "1–2×", "Lifters moving from PPL with 4 days"],
    ["4-day bro split", "Chest/Tri · Back/Bi · Legs · Shoulders/Arms", "1× direct", "One muscle group per session"],
])}
<p>All of these can build muscle. A {cite('freq2016', '2016 meta-analysis')} found twice-weekly training grew muscle more than once a week, while a {cite('pelland2026', '2026 meta-regression')} found frequency mattered little for growth once weekly sets were equal but did help strength. For the classic layout, see our {L('/workout-plans/upper-lower-split/', '4-day upper lower split')}.</p>
"""),
        ("who", "Who This 4-Day Split Is For", f"""
<ul>
<li>6+ months of consistent training with good form on the bench press, squat, row and hinge.</li>
<li>Four training days (ideally Monday, Tuesday, Thursday, Friday) and 60–75 minutes per session.</li>
<li>You want strength and size together, with arms trained directly twice a week.</li>
</ul>
<p>New to lifting? Start with a full-body plan for 3–6 months; our {L('/upper-lower-split-vs-full-body/', 'upper/lower vs full body guide')} compares the two.</p>
"""),
        ("nutrition", "What to Eat on This Plan", f"""
<p>Muscle gains from protein plateaued at intakes around 1.6 g/kg/day in a {cite('protein2018', 'meta-analysis of 49 trials')}, and a {cite('offseason2019', 'review of off-season bodybuilding nutrition')} recommends a slow gain of 0.25–0.5% of body weight per week to limit fat gain. If you want to lose fat while running this plan, keep protein high and keep the training loads; the program itself does not need to change. Work out your number with the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
        ("mistakes", "Mistakes That Stall a 4-Day Split", f"""
<ul>
<li><strong>Torso A and Torso B on back-to-back days.</strong> The second session is usually weaker.</li>
<li><strong>Short rests on heavy lifts.</strong> Trained lifters gained more strength with {cite('rest2018', 'rests longer than 2 minutes')}; keep 2–3 minutes on A-day compounds.</li>
<li><strong>Changing exercises every week.</strong> Keep the main lifts for the full 8-week block so you can see progress.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Torso A", "c1"), ("Tue", "Limbs A", "c3"), ("Wed", "Rest", "rest"), ("Thu", "Torso B", "c2"), ("Fri", "Limbs B", "c6"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Torso A", "title": "Day 1 — Torso A (Heavy)", "tag": "Strength", "color": 1, "time": "60–70 min", "focus": "Chest / Back / Shoulders",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "4 × 5–7", "3 min", "RIR 2"),
             ("Barbell Row", "Primary: mid-back, lats · Secondary: rear delts, biceps", "4 × 6–8", "2–3 min", "RIR 2"),
             ("Seated Dumbbell Shoulder Press", "Primary: front delts · Secondary: triceps", "3 × 6–8", "2 min", "RIR 2"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Cable Fly", "Primary: chest", "2 × 12–15", "60–90 sec", "RIR 1"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "4 × 12–15", "60 sec", "RIR 0–1"),
         ],
         "notes": "Do 2–3 ramp-up sets before bench press. Pair the cable fly and lateral raise as a superset to save time."},
        {"tab": "Day 2", "tab_sub": "Limbs A", "title": "Day 2 — Limbs A (Heavy)", "tag": "Strength", "color": 3, "time": "60–70 min", "focus": "Legs / Biceps / Triceps",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors", "4 × 5–7", "3 min", "RIR 2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 6–8", "2–3 min", "RIR 2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–12", "90 sec", "RIR 1"),
             ("Barbell Curl", "Primary: biceps", "3 × 8–10", "90 sec", "RIR 1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–12", "90 sec", "RIR 1"),
             ("Standing Calf Raise", "Primary: calves", "3 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Squat to at least parallel. If back squats irritate your lower back, use a safety-bar squat or hack squat and keep it for the whole block."},
        {"tab": "Day 3", "tab_sub": "Torso B", "title": "Day 3 — Torso B (Volume)", "tag": "Hypertrophy", "color": 2, "time": "60–70 min", "focus": "Chest / Back / Shoulders",
         "exercises": [
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "4 × 8–10", "2 min", "RIR 1–2"),
             ("Pull-Up (or Assisted Pull-Up)", "Primary: lats · Secondary: biceps", "4 × 8–10", "2 min", "RIR 1–2"),
             ("Seated Cable Row", "Primary: mid-back · Secondary: rear delts", "3 × 10–12", "90 sec", "RIR 1"),
             ("Pec Deck", "Primary: chest", "3 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Cable Lateral Raise", "Primary: side delts", "4 × 12–15", "60 sec", "RIR 0–1"),
             ("Face Pull", "Primary: rear delts · Secondary: rotator cuff", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Control the lowering phase (2–3 seconds) on presses and rows. Stop each pull-up set when your chin no longer clears the bar cleanly."},
        {"tab": "Day 4", "tab_sub": "Limbs B", "title": "Day 4 — Limbs B (Volume)", "tag": "Hypertrophy", "color": 6, "time": "65–75 min", "focus": "Legs / Biceps / Triceps",
         "exercises": [
             ("Leg Press", "Primary: quads · Secondary: glutes", "4 × 10–12", "2 min", "RIR 1–2"),
             ("Barbell Hip Thrust", "Primary: glutes · Secondary: hamstrings", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 12–15", "90 sec", "RIR 1"),
             ("Leg Extension", "Primary: quads", "3 × 12–15", "60–90 sec", "RIR 0–1"),
             ("Incline Dumbbell Curl", "Primary: biceps (long head)", "3 × 10–12", "60–90 sec", "RIR 1"),
             ("Triceps Pushdown", "Primary: triceps", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Superset the curl with the pushdown, and run calf raises between leg-curl sets, to keep this day near 65 minutes."},
    ],
    "faq_title": "4-Day Workout Split FAQ",
    "faqs": [
        ("Can I add a fifth day for arms or weak points?", "Yes, if you recover well. Keep it short (30–40 minutes) and light, for example lateral raises, curls and triceps work for 2–3 sets each, and place it on Saturday so it does not crowd Torso A."),
        ("Can I do cardio on the off days?", "Yes. Easy cardio such as walking or cycling for 20–40 minutes on Wednesday or the weekend supports heart health without hurting your lifting. Keep hard intervals away from the day before Limbs A so your squats do not suffer."),
        ("Can beginners use a 4-day workout split?", "Beginners can, but most progress faster on three full-body sessions a week while learning the lifts. After 3–6 months of steady progress, a 4-day split adds the extra volume you will start to need."),
        ("Is torso/limbs better than upper/lower?", "Neither is better for growth when weekly sets are equal. Torso/limbs gives arms a dedicated slot twice a week, while upper/lower is simpler to set up and keeps all leg work on dedicated lower-body days."),
        ("Can I do this 4-day split with only dumbbells?", "Mostly. Swap barbell lifts for dumbbell versions, pulldowns for pull-ups or band-assisted pull-ups, and cable moves for dumbbell flyes and raises. Leg training is the hardest part to load at home, so use split squats and single-leg work."),
        ("Can I train four days in a row?", "You can, but performance on day four may drop. If your schedule forces it, run Torso A, Limbs A, Torso B, Limbs B and accept slightly lower loads on the last day."),
    ],
    "related": ["upper-lower-split", "hypertrophy-program", "5-day-workout-split", "bro-split"],
    "refs": refs("freq2016", "pelland2026", "load2021", "currier2023", "acsm2026", "acsm2009", "delphi2023", "protein2018", "offseason2019", "rest2018"),
    "disclaimer": DISCLAIMER,
}
