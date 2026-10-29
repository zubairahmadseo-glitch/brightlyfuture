from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 53,
    "slug": "glute-workout",
    "title": "Glute Workout: 2-Day Plan to Build Your Glutes",
    "meta_title": "Glute Workout: Free 2-Day Plan to Build Bigger Glutes",
    "meta_desc": "Which exercises actually grow your glutes? This glute workout uses hip thrusts, squats, hinges and lunges twice a week, with a gym and home version.",
    "focus_kw": "glute workout",
    "badge": "Body Part Plan · Glutes",
    "hero_lead": "Two glute workouts a week built on the exercises that grew glute muscle in training studies: hip thrusts, deep squats, Romanian deadlifts and lunges, plus abduction work for the sides of your hips. Follow the gym or home version and add load every week.",
    "hero_meta": ["📅 2 glute days/week", "⏱ 45–60 min", "📊 Beginner–Intermediate", "🏋️ Gym or home"],
    "stats": [("2", "Glute days/week"), ("3", "Workout versions"), ("12–13", "Glute sets/session"), ("6–20", "Rep range"), ("11", "Exercises")],
    "quick_answer": "The best glute workout combines a hip thrust, a deep squat or lunge, a hip hinge such as the Romanian deadlift, and a hip abduction exercise. Train glutes twice a week with about 12 hard sets per session, and add weight or reps every week.",
    "intro": "<p>Pick a workout in the tabs. Below them you'll find why each exercise is there, how to progress and what to expect from glute training.</p>",
    "sections": [
        ("schedule", "Glute Workout Schedule", f"""
{WEEK}
<p>Leave at least two days between glute workouts. Upper-body training fits on the days in between. If you follow a full leg program as well, replace one of your leg days with Glute Day A instead of adding it on top.</p>
"""),
        ("workouts", "The Glute Workouts", f"""
<p>"/ leg" means do the reps on each leg. Effort is shown as RIR (reps in reserve): RIR 1–2 means stop with one or two clean reps left. In your first two weeks, do one set fewer on every exercise while you learn the movements.</p>
{TABS}
"""),
        ("exercises", "Why These Glute Exercises", f"""
{table(["Exercise", "What it adds", "Muscles"], [
    ["Hip thrust", "Heaviest load on the glutes with the hips fully extended", "Gluteus maximus"],
    ["Deep squat", "Glutes trained at a long, stretched length", "Gluteus maximus, quads, adductors"],
    ["Romanian deadlift", "Hip hinge under a heavy stretch", "Gluteus maximus, hamstrings"],
    ["Bulgarian split squat and lunges", "One leg at a time, deep hip bend", "Gluteus maximus, quads"],
    ["Hip abduction", "Works the sides of your hips", "Gluteus medius and minimus"],
])}
{box("science", "🔬 Hip thrust or squat?", f"<p>Both. In a {cite('plotkin2023', '9-week MRI study')}, hip thrusts and back squats grew the glutes by a similar amount, while squats also grew the quads and inner thighs more. Hip thrusts showed more glute activity on EMG, but that didn't predict who grew more. Depth matters for squats: full squats grew the glutes about three times more than half squats in a {cite('kubo2019', '10-week study')}.</p>")}
<p>In the hip thrust study, the gluteus medius and minimus barely grew from either exercise, which is why each workout ends with an abduction exercise.</p>
"""),
        ("progression", "How to Progress Your Glute Workout", f"""
<p>Use double progression: keep the same weight until every set reaches the top of its rep range, then add 2.5–5 kg on the hip thrust and squat or move up one dumbbell size on lunges. On abduction machines, add one plate. Write your numbers down; small weekly increases are what keep your glutes growing. Our guide to {L('/what-is-progressive-overload/', 'progressive overload')} explains the method in detail.</p>
<p>After 6–8 weeks, take a lighter week with half the sets, then start again a little heavier.</p>
"""),
        ("home", "Can You Build Glutes Without Weights?", f"""
<p>Yes, up to a point. Light loads built similar muscle to heavy loads in a {cite('load2021', 'meta-analysis')} when sets were taken close to failure. At home, that means slowing your reps, pausing at the bottom and doing single-leg versions. Once bodyweight sets pass 25–30 reps, a pair of dumbbells or a loop band will make each set count again.</p>
"""),
        ("mistakes", "Glute Workout Mistakes", f"""
<ul>
<li><strong>Arching your back on hip thrusts.</strong> Tuck your chin and ribs and finish the rep with your glutes, so your hips stop where your body forms a straight line.</li>
<li><strong>Half squats.</strong> Squat as deep as you can with a neutral back; shallow reps grow the glutes far less.</li>
<li><strong>Too many light activation moves.</strong> A few band exercises warm you up, but they don't replace hard sets of heavy exercises.</li>
<li><strong>Changing the plan every week.</strong> Repeat the same exercises long enough to add weight to them.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Glute Day A", "c1"), ("Tue", "Upper body", "rest"), ("Wed", "Rest", "rest"), ("Thu", "Glute Day B", "c2"), ("Fri", "Upper body", "rest"), ("Sat", "Rest / walk", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Day A", "tab_sub": "Hip thrust focus", "title": "Glute Workout A: Hip Thrust Focus", "tag": "Gym", "color": 1, "time": "50–60 min", "focus": "Glutes / Hamstrings",
         "exercises": [
             ("Barbell Hip Thrust", "Primary: gluteus maximus", "4 × 8–12", "2 min", "RIR 1–2"),
             ("Romanian Deadlift", "Primary: gluteus maximus, hamstrings", "3 × 8–10", "2 min", "RIR 2"),
             ("Bulgarian Split Squat", "Primary: gluteus maximus, quads", "3 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("Cable Hip Abduction", "Primary: gluteus medius and minimus", "2 × 12–15 / leg", "60 sec", "RIR 1"),
         ],
         "notes": "Pause for one second at the top of every hip thrust. On Bulgarian split squats, lean your torso slightly forward to bias the glutes."},
        {"tab": "Day B", "tab_sub": "Squat focus", "title": "Glute Workout B: Squat Focus", "tag": "Gym", "color": 2, "time": "50–60 min", "focus": "Glutes / Quads",
         "exercises": [
             ("Back Squat (full depth)", "Primary: gluteus maximus, quads, adductors", "4 × 6–10", "2–3 min", "RIR 2"),
             ("Reverse Lunge", "Primary: gluteus maximus, quads", "3 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("45° Back Extension (glute bias)", "Primary: gluteus maximus · Secondary: hamstrings", "3 × 12–15", "60–90 sec", "RIR 1"),
             ("Machine Hip Abduction", "Primary: gluteus medius and minimus", "3 × 15–20", "60 sec", "RIR 1"),
         ],
         "notes": "Squat to at least thighs parallel, deeper if your back stays neutral. For glute-biased back extensions, round your upper back slightly and point your toes out."},
        {"tab": "At home", "tab_sub": "Dumbbells + band", "title": "Glute Workout at Home", "tag": "Home", "color": 4, "time": "45–55 min", "focus": "Glutes / Hamstrings / Quads",
         "exercises": [
             ("Dumbbell Hip Thrust", "Primary: gluteus maximus", "4 × 10–20", "90 sec", "RIR 1"),
             ("Dumbbell Romanian Deadlift", "Primary: gluteus maximus, hamstrings", "3 × 10–12", "90 sec", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: gluteus maximus, quads", "3 × 8–15 / leg", "90 sec", "RIR 1"),
             ("Banded Side-Lying Hip Abduction", "Primary: gluteus medius and minimus", "2 × 15–20 / leg", "45 sec", "RIR 1"),
         ],
         "notes": "Do this workout twice a week. Rest your upper back on a sofa for hip thrusts and hold the dumbbell on your hips. No dumbbells? Do single-leg hip thrusts and slow (3-second) split squats."},
    ],
    "faq_title": "Glute Workout FAQ",
    "faqs": [
        ("How long until I see results from glute workouts?", "Studies such as the hip thrust and squat trials above measured glute growth after 9–10 weeks. Strength rises sooner, often within the first month, and visible change depends on your starting point."),
        ("Is it OK to train glutes every day?", "Not with hard sessions. Glutes need time to recover like other muscles, and they also work in squats, deadlifts and lunges on your leg days. Two hard sessions a week, with 2–3 days between them, is enough."),
        ("Can I target my lower glutes or upper glutes?", "Not in isolation. Hip thrusts, squats and Romanian deadlifts train the whole gluteus maximus, and abduction exercises add work for the upper side of the hips through the gluteus medius."),
        ("Do I need to eat more to grow my glutes?", f"You need enough protein: about 1.6 g per kg of body weight a day suits most lifters in a {cite('protein2018', 'large meta-analysis')}, and our {L('/protein-calculator/', 'protein calculator')} works out your number. A large calorie deficit makes building muscle harder, so eat at maintenance or slightly above it while glute growth is your goal."),
        ("Are glute kickbacks worth doing?", "They're fine as an extra, but they are hard to load heavily. Spend most of your sets on hip thrusts, squats, lunges and hinges, then add kickbacks if you have time."),
    ],
    "related": ["leg-day-workout", "strength-training-for-women", "core-workout", "hypertrophy-program"],
    "refs": refs("plotkin2023", "kubo2019", "load2021", "protein2018"),
    "disclaimer": DISCLAIMER,
}
