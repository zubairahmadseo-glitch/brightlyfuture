from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 6,
    "slug": "4-day-workout-split",
    "title": "4-Day Workout Split: The Torso/Limbs Plan for Muscle and Strength",
    "meta_title": "4-Day Workout Split: Torso/Limbs Plan With Sets & Reps",
    "meta_desc": "This 4 day workout split trains every muscle twice a week. Full torso/limbs workouts, sets and reps, progression rules and how each 4-day split compares.",
    "focus_kw": "4 day workout split",
    "badge": "2× Frequency in 4 Days",
    "hero_lead": "Four sessions a week is enough to train every muscle twice, as long as the days are split the right way. This plan uses a torso/limbs split with a heavier A rotation and a higher-rep B rotation.",
    "hero_meta": ["📅 4 days/week", "⏱ 60–75 min", "📊 Intermediate", "🏋️ Full gym"],
    "stats": [("4", "Training days"), ("2×", "Frequency/muscle"), ("10–14", "Sets/major muscle/wk"), ("8 wk", "Block length"), ("A/B", "Heavy + volume")],
    "quick_answer": "The best 4-day workout split for most intermediate lifters trains each muscle twice a week. This plan alternates torso days (chest, back, shoulders) with limbs days (legs, biceps, triceps) on Monday, Tuesday, Thursday and Friday, using one heavier and one higher-rep version of each day.",
    "takeaways": [
        "Torso/limbs separates upper-body pressing and pulling from arm isolation, so arms get fresh, focused work twice a week.",
        "A days use 5–8 reps on the main lifts for strength; B days use 8–15 reps for extra hypertrophy volume.",
        "Wednesday, Saturday and Sunday stay off, giving each muscle 72 hours between direct sessions.",
        "Upper/lower, torso/limbs, PPL + upper and a 4-day bro split all work; choose by recovery and schedule (comparison table below).",
        "Run the plan for 7 weeks, deload in week 8, then repeat with heavier starting loads.",
    ],
    "intro": "<p>A 4-day workout split hits the sweet spot for many lifters: enough sessions to train each muscle twice a week, and enough rest days to recover and keep a life outside the gym. The catch is that \"4-day split\" covers several layouts, and some of them train certain muscles only once.</p><p>This page gives you a complete torso/limbs program with every set and rep, then compares it with the other common 4-day splits so you can choose with confidence.</p>",
    "sections": [
        ("options", "Which 4-Day Split Should You Choose?", f"""
<p>All of the common 4-day layouts can build muscle. The differences are how often each muscle is trained, how long sessions run, and how much one missed day hurts the week.</p>
{table(["4-day split", "Layout", "Frequency/muscle", "Best for"], [
    ["Torso/Limbs (this plan)", "Torso A · Limbs A · Torso B · Limbs B", "2×", "Lifters who want arm and leg focus twice a week"],
    ["Upper/Lower", "Upper · Lower · Upper · Lower", "2×", "Strength-focused lifters; simplest to run"],
    ["PPL + Upper", "Push · Pull · Legs · Upper", "1–2×", "Lifters moving from PPL with only 4 days"],
    ["4-day bro split", "Chest/Tri · Back/Bi · Legs · Shoulders/Arms", "1× direct", "Bodybuilding-style lifters who recover slowly"],
    ["Full body ×4", "Full · Full · Full · Full", "4×", "Experienced lifters spreading volume thin"],
])}
{box("science", "🔬 Does frequency matter?", f"<p>A {cite('freq2016', '2016 meta-analysis')} found training a muscle twice a week grew it more than once a week. A larger {cite('pelland2026', '2026 meta-regression')} found frequency mattered little for growth once weekly sets were equal, but more frequent training did improve strength. Splitting sets over two sessions also keeps each workout shorter and fresher, which is the practical reason this plan uses 2× frequency.</p>")}
<p>If you prefer a classic upper/lower layout, our {L('/workout-plans/upper-lower-split/', '4-day upper lower split')} covers it in full. If you want torso/limbs, keep reading.</p>
"""),
        ("who", "Who This 4-Day Split Is For", f"""
<p>This plan suits lifters with 6+ months of consistent training who can bench, squat, row and hinge with good form. It fits people who:</p>
<ul>
<li>Can train four days, ideally Monday, Tuesday, Thursday and Friday.</li>
<li>Want visible arm and leg development, since limbs days give both fresh effort.</li>
<li>Want strength and size together, through heavy A days and volume B days.</li>
<li>Have 60–75 minutes per session.</li>
</ul>
{box("tip", "💡 Coach's note", f"<p>New to lifting? Start with a full-body plan for 3–6 months first. Full-body training lets you practice each lift three times a week, which speeds up technique learning. Compare the two approaches in our {L('/upper-lower-split-vs-full-body/', 'upper/lower vs full body guide')}.</p>")}
"""),
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
<p>Each rotation progresses differently, a simple application of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
<h3>A days (heavy)</h3>
<ol class="emp-steps">
<li>Start week 1 at a load you could lift for about 2 more reps than the top of the range.</li>
<li>When every set reaches the top of the range (e.g., 4 × 7 on bench) at RIR 2 or more, add 2.5 kg to upper-body lifts or 5 kg to squats.</li>
<li>If you miss the bottom of the range on two straight sessions, drop the load 5–10% and build back up.</li>
</ol>
<h3>B days (volume)</h3>
<p>Use double progression: add reps until every set hits the top of the range at the listed RIR, then add the smallest available load. The {cite('acsm2009', 'ACSM progression model')} recommends 2–10% load jumps once you exceed the target reps by one or two.</p>
<p>Track every session; a training log is the only reliable way to know the plan is working. The {L('/how-to-track-your-workouts/', 'workout tracking guide')} shows a simple format.</p>
"""),
        ("deload", "Deload and Long-Term Plan", f"""
<p>Train weeks 1–7 as written, then deload in week 8. Keep the same four days and exercises, cut sets by about half, and stop every set at RIR 3–4. A {cite('delphi2023', 'Delphi consensus of coaches and researchers')} defines a deload as a planned period of reduced training stress to manage fatigue and prepare for the next block, which is exactly its job here.</p>
<p>After the deload, start block two with loads about 2.5–5% heavier than block one's week 1. Swap 1–2 accessory exercises per day if they feel stale, but keep the main lifts so progress stays measurable. Our {L('/what-is-a-deload-week/', 'deload week guide')} covers signs you need one earlier.</p>
"""),
        ("nutrition", "Nutrition and Recovery", f"""
<div class="emp-macros">
<div class="emp-macro"><b>1.6–2.2 g/kg</b><span>Daily protein</span></div>
<div class="emp-macro"><b>0.25–0.5%</b><span>Body weight gained per week if bulking</span></div>
<div class="emp-macro"><b>7–9 h</b><span>Sleep per night</span></div>
</div>
<p>Protein intakes around 1.6 g/kg/day maximised gains in a {cite('protein2018', 'meta-analysis of 49 trials')}, and a {cite('offseason2019', 'review of off-season bodybuilding nutrition')} recommends a slow gain of 0.25–0.5% of body weight per week to limit fat gain. If you want to lose fat while running this plan, keep protein high and keep the training loads; the program itself does not need to change. Work out your number with the {L('/protein-calculator/', 'protein calculator')}.</p>
"""),
        ("mistakes", "Mistakes That Stall a 4-Day Split", f"""
<ul>
<li><strong>Stacking Torso A and Torso B on consecutive days.</strong> Pressing and rowing two days in a row leaves the second session under-recovered.</li>
<li><strong>Rushing rests on heavy lifts.</strong> Trained lifters gained more strength with {cite('rest2018', 'rests longer than 2 minutes')}. Keep 2–3 minutes on A-day compounds.</li>
<li><strong>Treating arm work as an afterthought.</strong> On limbs days, arms come after legs, so keep arm sets controlled and close to the listed RIR rather than rushing them.</li>
<li><strong>Changing exercises every week.</strong> Constant novelty makes it impossible to see progress. Keep the main lifts for the full 8-week block.</li>
</ul>
<p>Get those right and the four-day structure will carry you for many training blocks. When progress slows across a whole block, revisit total weekly sets before changing the split.</p>
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
        ("Is a 4-day split enough to build muscle?", "Yes. Four sessions let you train every muscle twice a week with 10 or more weekly sets for the major groups, which matches current hypertrophy guidelines for intermediate lifters."),
        ("Can I do cardio on the off days?", "Yes. Easy cardio such as walking or cycling for 20–40 minutes on Wednesday or the weekend supports recovery and heart health. Keep hard intervals away from the day before Limbs A so your squats do not suffer."),
        ("Can beginners use a 4-day workout split?", "Beginners can, but most progress faster on three full-body sessions a week while learning the lifts. After 3–6 months of steady progress, a 4-day split adds the extra volume you will start to need."),
        ("Is torso/limbs better than upper/lower?", "Neither is better for growth when weekly sets are equal. Torso/limbs gives arms a dedicated slot twice a week, while upper/lower makes it easier to run heavy squats and deadlifts on separate days."),
        ("How long should each workout take?", "Plan on 60–75 minutes including a 10-minute warm-up. Supersets on arm and calf work keep limbs days within that window."),
        ("Can I train four days in a row?", "You can, but performance on day four usually drops. If your schedule forces it, run Torso A, Limbs A, Torso B, Limbs B and accept slightly lower loads on the last day."),
    ],
    "related": ["upper-lower-split", "hypertrophy-program", "5-day-workout-split", "bro-split"],
    "refs": refs("freq2016", "pelland2026", "load2021", "currier2023", "acsm2026", "acsm2009", "delphi2023", "protein2018", "offseason2019", "rest2018"),
    "disclaimer": DISCLAIMER,
}
