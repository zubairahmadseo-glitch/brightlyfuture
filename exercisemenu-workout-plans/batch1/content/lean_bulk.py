from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 8,
    "slug": "lean-bulk-workout-plan",
    "title": "12-Week Lean Bulk Workout Plan: Training and Calorie Guide",
    "meta_title": "Lean Bulk Workout Plan: 12 Weeks + Calorie Targets",
    "meta_desc": "A 12-week lean bulk workout plan with a 4-day split, plus how many calories to add and how fast to gain so you build muscle without much fat.",
    "focus_kw": "lean bulk workout plan",
    "badge": "12-Week Program",
    "hero_lead": "A lean bulk is a training plan and an eating plan working together. This 12-week lean bulk workout plan gives you both: a 4-day split that ramps volume, then intensity, and calorie targets designed to add muscle while keeping fat gain small.",
    "hero_meta": ["📅 4 days/week", "⏱ 55–70 min", "📊 Intermediate", "🏋️ Full gym", "🍽 Nutrition included"],
    "stats": [("12 wk", "Program length"), ("3", "Training phases"), ("+10–20%", "Calorie surplus"), ("0.25–0.5%", "BW gain/week"), ("1.6–2.2", "Protein g/kg")],
    "quick_answer": "A lean bulk pairs progressive strength training with a small calorie surplus of about 10–20% above maintenance, aiming to gain 0.25–0.5% of body weight per week. This 12-week plan trains four days a week (Push, Pull, Legs, Full Body) and moves through volume, deload and intensity phases.",
    "intro": "<p>The 12-week training plan comes first. After the workouts you'll find how to set your calorie surplus, track your weight and adjust.</p>",
    "sections": [
        ("program", "Program Overview: Three Phases", f"""
<p>The training runs four days a week for 12 weeks. The exercises stay the same throughout so you can see progress; sets and rep ranges change by phase.</p>
{WEEK}
{table(["Weeks", "Phase", "What changes", "Effort"], [
    ["1–4", "Foundation", "Program as written", "RIR 2–3 in week 1, RIR 1–2 by week 4"],
    ["5–8", "Volume", "+1 set on the first two exercises of each day", "RIR 1–2"],
    ["9", "Deload", "Half the sets, same loads", "RIR 3–4"],
    ["10–12", "Intensity", "First two exercises each day: 4 sets of 5–8 with 2.5–3 min rests", "RIR 1–2"],
])}
{box("tip", "💡 Why this order?", f"<p>Volume drives muscle growth: {cite('vol2017', 'more weekly sets produced more growth')} in a dose-response meta-analysis. Heavier loads drive strength: {cite('load2021', 'high-load training produced greater strength gains')} than lighter loads, while growth was similar. The plan builds size with volume first, deloads, then converts it into strength you can use in your next bulk or cut.</p>")}
"""),
        ("workouts", "The Lean Bulk Workouts", f"""
<p>Select a day. Rep ranges shown are for Phase 1 and 2. Effort is in reps in reserve (RIR); the {L('/rpe-vs-rir/', 'RPE vs RIR guide')} explains how to rate it.</p>
{TABS}
"""),
        ("volume", "Weekly Volume by Phase", f"""
{table(["Muscle", "Phase 1 (sets/week)", "Phase 2 (sets/week)"], [
    ["Chest", "≈ 11", "≈ 13"],
    ["Back", "≈ 12", "≈ 15"],
    ["Side delts", "≈ 7.5", "≈ 8"],
    ["Quads", "≈ 9", "≈ 10"],
    ["Hamstrings", "≈ 7", "≈ 8"],
    ["Biceps", "≈ 13", "≈ 14.5"],
    ["Triceps", "≈ 11", "≈ 12.5"],
])}
<p>Totals count direct sets fully and indirect sets (such as biceps during rows) as half, the method best supported by the {cite('pelland2026', 'Pelland 2026 dose-response analysis')}. Phase 2 puts most major muscles in the 10–15 set range linked with growth in the {cite('acsm2026', '2026 ACSM position stand')}. For more on set targets, read {L('/how-many-sets-per-muscle-group-per-week/', 'how many sets per muscle group per week')}.</p>
"""),
        ("progression", "Progression During the Bulk", f"""
<p>A surplus makes progression easier, so expect your logbook to move. Use double progression on every exercise: when all sets hit the top of the rep range at the target RIR, add the smallest available load. That is the core of {L('/what-is-progressive-overload/', 'progressive overload')}.</p>
<p>On a well-run lean bulk, your main lifts should trend up every 1–3 weeks. If your weight is rising on target but lifts have not moved in three weeks, check training effort and sleep before adding more food. If neither weight nor lifts move, add calories first.</p>
"""),
        ("rate", "How Fast Should You Gain on a Lean Bulk?", f"""
<p>The target rate is the core of a lean bulk. A {cite('offseason2019', 'review of off-season bodybuilding nutrition')} recommends a 10–20% calorie surplus with weight gain of about 0.25–0.5% of body weight per week for novice and intermediate lifters, and a more conservative approach for advanced lifters.</p>
{table(["Body weight", "0.25% per week", "0.5% per week", "Per 12 weeks"], [
    ["60 kg", "0.15 kg", "0.30 kg", "1.8–3.6 kg"],
    ["75 kg", "0.19 kg", "0.38 kg", "2.3–4.5 kg"],
    ["90 kg", "0.23 kg", "0.45 kg", "2.7–5.4 kg"],
])}
{box("science", "🔬 Why faster is not better", f"<p>In a {cite('garthe2013', 'trial on elite athletes')}, a group eating a planned surplus gained more body weight than a group eating freely (3.9% vs 1.5%), but lean mass gains were the same. The difference was mostly fat: fat mass rose about 15% in the bigger-surplus group versus 3% in the other. A {cite('surplus2019', '2019 review')} adds that the ideal surplus for muscle gain has never been pinned down, so a moderate, monitored surplus is the safest bet.</p>")}
<p>Use the lower end (0.25%) if you have trained for 2+ years or gain fat easily, and the upper end (0.5%) if you are newer to lifting or lean to start.</p>
"""),
        ("nutrition", "Lean Bulk Calories and Macros", f"""
<ol class="emp-steps">
<li><strong>Find maintenance.</strong> Track food and morning body weight for 14 days without trying to change either. If weight is stable, your average intake is maintenance.</li>
<li><strong>Add 10–20%.</strong> Example: 2,500 kcal maintenance × 1.10–1.20 = 2,750–3,000 kcal. Start at the low end.</li>
<li><strong>Set protein.</strong> 1.6–2.2 g per kg of body weight per day. Gains in muscle mass plateaued around 1.62 g/kg in a {cite('protein2018', 'meta-analysis of 49 trials')}.</li>
<li><strong>Set fat.</strong> 0.5–1.5 g per kg per day, per the {cite('offseason2019', 'off-season nutrition review')}.</li>
<li><strong>Fill the rest with carbs.</strong> That review suggests at least 3–5 g/kg/day to fuel training.</li>
</ol>
<div class="emp-macros">
<div class="emp-macro"><b>1.6–2.2 g/kg</b><span>Protein</span></div>
<div class="emp-macro"><b>0.5–1.5 g/kg</b><span>Fat</span></div>
<div class="emp-macro"><b>≥3–5 g/kg</b><span>Carbohydrate</span></div>
<div class="emp-macro"><b>3–5 g</b><span>Creatine/day (optional)</span></div>
</div>
<p>Split protein across 3–5 meals. Creatine monohydrate at 3–5 g per day is the {cite('creatine', 'most researched supplement')} for strength and lean mass, and it is optional. Use the {L('/protein-calculator/', 'protein calculator')} for your exact daily target.</p>
"""),
        ("tracking", "How to Track and Adjust the Bulk", f"""
<p>Weigh yourself each morning after the bathroom and before eating, then compare weekly averages. Daily weight swings of 0.5–1 kg from water and food are common and tell you nothing on their own.</p>
{table(["2-week trend", "What it means", "Action"], [
    ["Gaining less than 0.25% BW/week", "Surplus too small", "Add 150–200 kcal/day (mostly carbs)"],
    ["Gaining 0.25–0.5% BW/week", "On target", "No change"],
    ["Gaining more than 0.5% BW/week", "Surplus too large", "Remove 150–200 kcal/day"],
    ["Waist growing quickly while lifts stall", "Likely mostly fat gain", "Reduce calories; check training effort"],
])}
<p>Re-check every two weeks. Weight often jumps more than the target in the first week because of extra food and water in your body, so judge the bulk from week 2 onward.</p>
"""),
        ("after", "What to Do After 12 Weeks", f"""
<p>At the end of week 12, compare your weekly-average weight, waist measurement, photos and main lifts with week 1. Then choose:</p>
<ul>
<li><strong>Continue:</strong> waist grew only slightly and lifts rose. Take a deload week, then run another 12-week block.</li>
<li><strong>Maintenance phase:</strong> you gained more fat than you wanted. Eat at maintenance for 4–8 weeks while training normally.</li>
<li><strong>Cut:</strong> you are ready to lose fat. Keep training heavy and keep protein high.</li>
</ul>
<p>For recovery between blocks, the {L('/what-is-a-deload-week/', 'deload week guide')} explains how to reduce training without losing progress.</p>
"""),
        ("mistakes", "Lean Bulk Mistakes to Avoid", f"""
<ul>
<li><strong>"See food" bulking.</strong> A large surplus adds fat faster than muscle, as the {cite('garthe2013', 'Garthe trial')} showed.</li>
<li><strong>Ignoring the scale.</strong> Without a tracked trend, a lean bulk can quickly turn into a regular bulk.</li>
<li><strong>Program-hopping.</strong> Changing exercises every few weeks hides whether the extra food is building strength.</li>
<li><strong>Junk-food surplus.</strong> Calories count, but most of the surplus should come from carb-rich whole foods that fuel training. See {L('/post-workout-snacks-for-muscle-gain/', 'post-workout snacks for muscle gain')} for practical options.</li>
</ul>
<p>Avoid these and the next 12 weeks should end with more muscle, stronger lifts and a waistline you are happy with.</p>
"""),
    ],
    "schedule": [("Mon", "Push", "c1"), ("Tue", "Pull", "c2"), ("Wed", "Rest", "rest"), ("Thu", "Legs", "c3"), ("Fri", "Rest", "rest"), ("Sat", "Full Body", "c4"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day 1", "tab_sub": "Push", "title": "Day 1 — Push", "tag": "Chest · Shoulders · Triceps", "color": 1, "time": "55–65 min", "focus": "Chest / Shoulders / Triceps",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 6–10", "2–3 min", "RIR 1–2"),
             ("Seated Dumbbell Shoulder Press", "Primary: front delts · Secondary: triceps", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Pec Deck", "Primary: chest", "2 × 12–15", "60–90 sec", "RIR 1"),
             ("Cable Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps (long head)", "3 × 10–12", "60–90 sec", "RIR 1"),
         ],
         "notes": "Phase 2: bench press and shoulder press go to 4 sets. Phase 3: bench and shoulder press become 4 × 5–8 with 2.5–3 min rests."},
        {"tab": "Day 2", "tab_sub": "Pull", "title": "Day 2 — Pull", "tag": "Back · Rear delts · Biceps", "color": 2, "time": "55–65 min", "focus": "Back / Rear delts / Biceps",
         "exercises": [
             ("Lat Pulldown (or Pull-Up)", "Primary: lats · Secondary: biceps", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Barbell Row", "Primary: mid-back, lats · Secondary: rear delts", "3 × 6–10", "2–3 min", "RIR 2"),
             ("Seated Cable Row", "Primary: mid-back", "3 × 10–12", "90 sec", "RIR 1"),
             ("Face Pull", "Primary: rear delts", "3 × 12–15", "60 sec", "RIR 1"),
             ("Barbell Curl", "Primary: biceps", "3 × 8–10", "90 sec", "RIR 1"),
             ("Hammer Curl", "Primary: brachialis", "2 × 10–12", "60 sec", "RIR 1"),
         ],
         "notes": "Phase 2: pulldown and barbell row go to 4 sets. Keep the row strict; if your torso rises above 45°, the load is too heavy."},
        {"tab": "Day 3", "tab_sub": "Legs", "title": "Day 3 — Legs", "tag": "Quads · Hamstrings · Calves", "color": 3, "time": "60–70 min", "focus": "Legs / Core",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes", "3 × 6–10", "3 min", "RIR 2"),
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 8–10", "2–3 min", "RIR 2"),
             ("Leg Press", "Primary: quads · Secondary: glutes", "3 × 10–12", "2 min", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "4 × 10–12", "90 sec", "RIR 1"),
             ("Standing Calf Raise", "Primary: calves", "3 × 10–15", "60 sec", "RIR 1"),
             ("Cable Crunch", "Primary: abs", "2 × 10–15", "60 sec", "RIR 1"),
         ],
         "notes": "Phase 2: squat and RDL go to 4 sets. Phase 3: squat becomes 4 × 5–8."},
        {"tab": "Day 4", "tab_sub": "Full Body", "title": "Day 4 — Full Body", "tag": "Second weekly hit", "color": 4, "time": "55–65 min", "focus": "Full body",
         "exercises": [
             ("Incline Barbell Bench Press", "Primary: upper chest · Secondary: front delts, triceps", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Chest-Supported Dumbbell Row", "Primary: mid-back, lats", "3 × 8–12", "90 sec", "RIR 1"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "3 × 8–10 / leg", "2 min", "RIR 2"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "3 × 12–15", "60 sec", "RIR 0–1"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "2 × 10–12", "60 sec", "RIR 1"),
             ("EZ-Bar Skull Crusher", "Primary: triceps", "2 × 10–12", "60–90 sec", "RIR 1"),
             ("Seated Calf Raise", "Primary: calves (soleus)", "2 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Phase 2: incline press and row go to 4 sets. Superset curls with skull crushers."},
    ],
    "faq_title": "Lean Bulk Workout Plan FAQ",
    "faqs": [
        ("How much muscle can I gain in 12 weeks?", f"It varies widely with training age, genetics, sleep and food. {cite('hubal2005', 'In one large study')}, arm muscle size changes after the same 12-week program ranged from almost none to nearly 60%, so track your own progress instead of chasing a fixed number."),
        ("Should I do cardio on a lean bulk?", "Yes, in moderation. Two or three 20–30 minute easy sessions a week support heart health. Add about 100–200 kcal on cardio days if your weight trend drops below target."),
        ("Should I bulk or cut first?", "If you are lean and want more size, bulk first. If you carry more fat than you are comfortable with, a few months of cutting or eating at maintenance first usually makes the later bulk more enjoyable."),
        ("What should I eat before training?", "A meal with 20–40 g of protein and a solid carb portion 1–3 hours before training, such as rice and chicken or oats with Greek yogurt, is easy to digest for most people."),
        ("Can I lean bulk without counting calories?", "Yes, if you weigh yourself daily. Eat similar meals each day, add one extra snack of about 200–300 kcal, and adjust portions based on your weekly average weight."),
        ("How long should a lean bulk last?", "There is no fixed length. Keep going while you gain at the target rate, your lifts keep rising and you are comfortable with your waist measurement, and reassess every 12 weeks."),
    ],
    "related": ["workout-plan-for-skinny-guys", "hypertrophy-program", "push-pull-legs", "upper-lower-split"],
    "refs": refs("offseason2019", "garthe2013", "surplus2019", "hubal2005", "protein2018", "creatine", "vol2017", "load2021", "pelland2026", "acsm2026"),
    "disclaimer": DISCLAIMER,
}
