from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 2,
    "slug": "full-body-workout-plan",
    "title": "Full Body Workout Plan for Beginners: 3-Day Gym Program",
    "meta_title": "Gym Workout Plan for Beginners: 3-Day Full Body Program",
    "meta_desc": "A beginner gym workout plan: three full-body days led by the squat, bench press and deadlift, with every set and rep and an easy 8-week progression.",
    "focus_kw": "gym workout plan",
    "badge": "Beginner Program",
    "hero_lead": "Your first gym workout plan: three full-body sessions a week, each led by one big lift (squat, bench press or deadlift), with simple rules for when to add weight over 8 weeks.",
    "hero_meta": ["📅 3 days/week", "⏱ 45–55 min", "📊 Beginner (0–6 months)", "🏋️ Gym"],
    "stats": [("3", "Training days"), ("20", "Exercises"), ("45–55", "Minutes/session"), ("8 wk", "Program length"), ("3×", "Frequency/muscle")],
    "quick_answer": "This beginner gym workout plan has three full-body workouts: Day A (squat focus), Day B (bench press focus) and Day C (deadlift focus), done on non-consecutive days such as Monday, Wednesday and Friday. Each takes 45–55 minutes, and you add weight once you reach the top of each rep range.",
    "intro": "<p>Pick a day in the tabs to see each workout. Below the workouts you will find the 8-week progression, form cues for the three main lifts and answers to common beginner questions.</p>",
    "sections": [
        ("schedule", "3-Day Full Body Workout Schedule", f"""
{WEEK}
<p>Any three days work as long as there is a rest day between sessions: Monday/Wednesday/Friday or Tuesday/Thursday/Saturday are the most common. Each day starts with a different main lift, so you practise the squat, bench press and deadlift every week while every muscle is trained three times. The {cite('acsm2009', 'ACSM progression guidelines')} recommend 2–3 sessions a week and sets of 8–12 reps for people new to lifting, which matches this plan.</p>
"""),
        ("workouts", "The Beginner Workouts", f"""
<p>Choose a day. Effort is shown as RIR (reps in reserve): RIR 2–3 means you stop each set with 2–3 good reps left. Weeks 1–2 should feel easier than that while you learn the movements.</p>
{TABS}
{box("warn", "⚠️ New to deadlifts?", f"<p>For the first two weeks, use a {L('/how-to-trap-bar-deadlift/', 'trap bar deadlift')} or a {L('/dumbbell-romanian-deadlift/', 'dumbbell Romanian deadlift')} to learn the hip hinge, then move to the barbell. Read {L('/how-to-deadlift-for-beginners/', 'how to deadlift for beginners')} before your first heavy session.</p>")}
"""),
        ("progression", "8-Week Progression", f"""
{table(["Weeks", "Phase", "What to do"], [
    ["1–2", "Learn", "Light weights, bottom of each rep range, focus on technique. Film your squat, bench press and deadlift."],
    ["3–4", "Load", "Add weight until the last 2–3 reps of each set feel hard (RIR 2–3)."],
    ["5–7", "Build", "Double progression: when all sets reach the top of the range, add weight and drop back to the bottom. Stop sets at RIR 1–2."],
    ["8", "Test", "Work up to a hard set of 5 on squat, bench press and deadlift. Compare with week 1, take 2–3 days off, then restart with your new weights."],
])}
<p>Add the smallest jump your gym allows: 1–2.5 kg on upper-body lifts and 2.5–5 kg on lower-body lifts. Example: squats call for 3 × 8–10; once you hit 10, 10, 10, add 2.5–5 kg and start again at 8. More examples are in {L('/progressive-overload-for-beginners/', 'progressive overload for beginners')}.</p>
{box("science", "🔬 How fast beginners change", f"<p>Strength rises quickly at first, partly because your nervous system gets better at each lift. Muscle grows early too: in a {cite('seynnes2007', 'training study')}, increases in thigh muscle size were measurable after about 3 weeks of training three times a week.</p>")}
"""),
        ("volume", "Weekly Sets per Muscle", f"""
{table(["Muscle", "Direct sets", "Indirect (×0.5)", "Weekly total"], [
    ["Chest", "9", "–", "9"],
    ["Back", "9", "Deadlift 3 → 1.5", "≈ 10.5"],
    ["Quads", "8", "–", "8"],
    ["Hamstrings", "7", "–", "7"],
    ["Shoulders (side & rear)", "4", "Shoulder press, rows 11 → 5.5", "≈ 9.5"],
    ["Biceps", "2", "Pulldown & rows 9 → 4.5", "≈ 6.5"],
    ["Triceps", "2", "Presses 11 → 5.5", "≈ 7.5"],
    ["Core", "6", "–", "6"],
])}
<p>These are moderate numbers on purpose. Beginners grow well on lower volumes, and the {cite('acsm2009', 'ACSM guidelines')} suggest 1–3 sets per exercise for novices. After 8 weeks you can add a set to the exercises you most want to improve.</p>
"""),
        ("form", "Form Cues for the Three Main Lifts", f"""
<h3>Back squat</h3>
<ul><li>Bar on your upper back, feet about shoulder-width, toes slightly out.</li><li>Brace your core, then bend hips and knees together.</li><li>Go down until your hip crease reaches knee level or lower; drive up through the whole foot.</li></ul>
<h3>Bench press</h3>
<ul><li>Pull your shoulder blades back and down before unracking.</li><li>Lower the bar to mid-chest with forearms roughly vertical.</li><li>Keep feet flat and press the bar up and slightly back over the shoulders. Full guide: {L('/how-to-bench-press/', 'how to bench press')}.</li></ul>
<h3>Deadlift</h3>
<ul><li>Bar over mid-foot, hands just outside the legs.</li><li>Chest up, take the slack out of the bar before pulling.</li><li>Push the floor away, keep the bar close, and finish by standing tall without leaning back.</li></ul>
<p>If your form breaks down on any rep, the weight is too heavy; drop it 10–20% and build back up.</p>
"""),
        ("warmup", "Warm-Up (5 Minutes + Ramp-Up Sets)", f"""
<p>Do 3 minutes of easy cardio, then arm circles, leg swings and 10–15 bodyweight squats. Before your first barbell lift, do an empty-bar set of 10 and a set of 5 at about 50–60% of your working weight. The {L('/warm-up-set-calculator/', 'warm-up set calculator')} works out the numbers.</p>
"""),
        ("nutrition", "What to Eat as a Beginner", f"""
<p>Aim for about 1.6 g of protein per kg of body weight a day; gains in muscle plateaued around that intake in a {cite('protein2018', 'meta-analysis of 49 trials')}. For a 75 kg person that is about 120 g, spread over 3–4 meals. If your goal is muscle, eat at maintenance or slightly above; if you want to lose fat, a moderate deficit still lets most beginners get stronger. Use the {L('/protein-calculator/', 'protein calculator')} to set your target.</p>
"""),
        ("mistakes", "Beginner Mistakes to Avoid", f"""
<ul>
<li><strong>Adding weight too fast.</strong> Increase only when every set reaches the top of the rep range with clean form.</li>
<li><strong>Going to failure every set.</strong> Keep 1–3 reps in reserve during these 8 weeks.</li>
<li><strong>Not tracking.</strong> Write down every set; see the {L('/how-to-track-your-workouts/', 'workout tracking guide')}.</li>
<li><strong>Program hopping.</strong> Finish all 8 weeks before changing anything.</li>
</ul>
"""),
        ("compare", "Full Body vs Split for Beginners", f"""
{table(["", "Full body (this plan)", "Upper/lower", "Push pull legs"], [
    ["Days per week", "3", "4", "6"],
    ["Frequency per muscle", "3×", "2×", "2×"],
    ["Practice on main lifts", "High", "Good", "Moderate"],
    ["If you miss a session", "Every muscle still trained twice", "Some muscles once", "Some muscles once"],
])}
<p>Split and full-body routines built similar muscle and strength when weekly sets were equal in a {cite('split2024', '2024 meta-analysis')}. Full body is the easier starting point because it gives you more practice on each lift with only three gym days.</p>
"""),
    ],
    "schedule": [("Mon", "Day A", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Day B", "c1"), ("Thu", "Rest", "rest"), ("Fri", "Day C", "c2"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day A", "tab_sub": "Squat focus", "title": "Day A — Squat Focus", "tag": "Full body", "color": 4, "time": "45–55 min", "focus": "Full body",
         "exercises": [
             ("Barbell Back Squat", "Primary: quads, glutes · Secondary: core", "3 × 8–10", "2–3 min", "RIR 2–3"),
             ("Dumbbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 10–12", "90 sec", "RIR 2–3"),
             ("Lat Pulldown", "Primary: lats · Secondary: biceps, rear delts", "3 × 10–12", "90 sec", "RIR 2–3"),
             ("Seated Leg Curl", "Primary: hamstrings", "2 × 10–12", "60–90 sec", "RIR 2"),
             ("Seated Dumbbell Shoulder Press", "Primary: shoulders · Secondary: triceps", "2 × 10–12", "90 sec", "RIR 2–3"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "2 × 12–15", "60 sec", "RIR 2"),
             ("Plank", "Primary: core", "2 × 30–45 sec", "60 sec", "Stop before form breaks"),
         ],
         "notes": "Squat until your hip crease is at or just below knee level. If you can't reach that depth yet, use goblet squats while your mobility improves."},
        {"tab": "Day B", "tab_sub": "Bench focus", "title": "Day B — Bench Press Focus", "tag": "Full body", "color": 1, "time": "45–55 min", "focus": "Full body",
         "exercises": [
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "3 × 8–10", "2–3 min", "RIR 2–3"),
             ("Barbell Bent-Over Row", "Primary: back · Secondary: biceps, rear delts", "3 × 8–10", "2 min", "RIR 2–3"),
             ("Leg Press", "Primary: quads, glutes", "3 × 10–12", "90 sec", "RIR 2–3"),
             ("Dumbbell Romanian Deadlift", "Primary: hamstrings, glutes", "2 × 10–12", "90 sec", "RIR 2–3"),
             ("Dumbbell Lateral Raise", "Primary: side delts", "2 × 12–15", "60 sec", "RIR 2"),
             ("Triceps Rope Pushdown", "Primary: triceps", "2 × 12–15", "60 sec", "RIR 2"),
             ("Cable Crunch", "Primary: abs", "2 × 15–20", "60 sec", "RIR 2"),
         ],
         "notes": "Always bench with a spotter or with the rack's safety arms set just below chest height."},
        {"tab": "Day C", "tab_sub": "Deadlift focus", "title": "Day C — Deadlift Focus", "tag": "Full body", "color": 2, "time": "45–55 min", "focus": "Full body",
         "exercises": [
             ("Conventional Deadlift", "Primary: hamstrings, glutes, back · Secondary: core, grip", "3 × 6–8", "2–3 min", "RIR 2–3"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: shoulders, triceps", "3 × 10–12", "90 sec", "RIR 2–3"),
             ("Seated Cable Row", "Primary: mid-back, lats · Secondary: biceps", "3 × 10–12", "90 sec", "RIR 2–3"),
             ("Dumbbell Walking Lunge", "Primary: quads, glutes", "2 × 10 / leg", "90 sec", "RIR 2–3"),
             ("Face Pull", "Primary: rear delts, rotator cuff", "2 × 15–20", "60 sec", "RIR 2"),
             ("Hanging Knee Raise", "Primary: abs, hip flexors", "2 × 10–15", "60 sec", "RIR 2"),
         ],
         "notes": "Reset your position before every deadlift rep instead of bouncing the bar off the floor."},
    ],
    "faq_title": "Beginner Gym Workout Plan FAQ",
    "faqs": [
        ("What weight should I start with?", "Start with the empty barbell (20 kg men's bar, 15 kg women's bar) and light dumbbells. If the bar is too heavy for the bench press, use dumbbells until it isn't."),
        ("Can I do cardio on rest days?", "Yes. Two or three 20–30 minute sessions of walking, easy cycling or swimming are a good start. Keep hard sprints or long runs away from the day before Day A."),
        ("What if my gym has no barbell or squat rack?", "Use goblet squats for back squats, the dumbbell bench press for the barbell bench press and the dumbbell Romanian deadlift for the deadlift. The progression rules stay the same."),
        ("Can I follow this plan while losing weight?", "Yes. Eat in a moderate deficit, keep protein at 1.6–2.0 g/kg and follow the plan as written. Large calorie deficits make it harder to keep muscle and train well."),
        ("When will I see results?", "Strength often improves within 2–3 weeks. Visible muscle changes usually take 6–8 weeks or more, and bigger changes take several months of steady training."),
        ("What should I do after 8 weeks?", "Repeat the 8 weeks with heavier starting weights, or move to a 4-day upper/lower split if you can add a day. Many beginners stay on full body for 3–6 months."),
    ],
    "related": ["beginner-strength-training-program", "upper-lower-split", "5x5-workout", "push-pull-legs"],
    "refs": refs("acsm2009", "seynnes2007", "protein2018", "split2024"),
    "disclaimer": DISCLAIMER,
}
