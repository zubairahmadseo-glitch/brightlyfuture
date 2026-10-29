from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 54,
    "slug": "leg-day-workout",
    "title": "Leg Day Workout: Complete Plans for Quads, Hamstrings and Calves",
    "meta_title": "Leg Day Workout: 4 Free Leg Day Plans (Gym & Dumbbells)",
    "meta_desc": "Not sure how to structure leg day? Pick a beginner, quad-focus, hamstring-focus or dumbbell leg day workout, with sets, reps, rest and progression.",
    "focus_kw": "leg day workout",
    "badge": "Body Part Plan · Legs",
    "hero_lead": "Four complete leg day workouts: a beginner session, a quad-focused day, a hamstring and glute day, and a dumbbell-only version. Each one trains your quads, hamstrings, glutes and calves, in the order that gets the most from every exercise.",
    "hero_meta": ["📅 1–2 leg days/week", "⏱ 50–65 min", "📊 Beginner–Intermediate", "🏋️ Gym or dumbbells"],
    "stats": [("1–2", "Leg days/week"), ("4", "Leg day plans"), ("2–3 min", "Rest on big lifts"), ("5–15", "Rep range"), ("15", "Exercises")],
    "quick_answer": "A complete leg day workout starts with a heavy squat or leg press, then adds a hip hinge such as the Romanian deadlift, a single-leg exercise, a leg curl or leg extension, and calf raises. Do 3–4 sets of each and train legs twice a week if you can.",
    "intro": "<p>Pick a leg day in the tabs. If you train legs twice a week, alternate the quad-focus and hamstring-focus days. Below the workouts you'll see how to order your exercises and how many sets your legs need.</p>",
    "sections": [
        ("schedule", "Leg Day Schedule", f"""
{WEEK}
<p>Two leg days a week, three or four days apart, let you train each leg muscle twice. Training a muscle twice a week builds more muscle than once a week in a {cite('freq2016', 'meta-analysis')}. If you only have time for one leg day, use the beginner workout or alternate the quad and hamstring days from week to week.</p>
"""),
        ("workouts", "The Leg Day Workouts", f"""
<p>"/ leg" means do the reps on each leg. RIR (reps in reserve) 2 means you stop with two clean reps left. Warm up with 2–4 lighter sets on the first exercise.</p>
{TABS}
"""),
        ("structure", "How to Structure a Leg Day Workout", f"""
{table(["Order", "Exercise type", "Why", "Examples"], [
    ["1", "Heavy squat or press", "Hardest lift, done while you're fresh", "Back squat, goblet squat, leg press"],
    ["2", "Hip hinge", "Hamstrings and glutes under a heavy stretch", "Romanian deadlift"],
    ["3", "Single-leg exercise", "Evens out left-right differences", "Bulgarian split squat, walking lunge"],
    ["4", "Isolation", "Trains what the big lifts miss", "Leg extension, seated leg curl"],
    ["5", "Calves", "Small muscle, needs its own work", "Standing or seated calf raise"],
])}
{box("science", "🔬 Why squats aren't enough", f"<p>In a {cite('kubo2019', '10-week squat study')}, full squats grew the quads, glutes and inner thighs, but not the hamstrings or the rectus femoris (the quad that crosses the hip). That's why each plan here adds a hinge, a leg curl and, on the quad day, a leg extension. For the leg curl, choose the seated machine: it grew the hamstrings more than the lying leg curl in a {cite('maeo2021', '2021 study')}.</p>")}
<p>For calves, spend most of each rep in the bottom half. Partial reps in the stretched position grew the inner calf more than full reps in a {cite('kassiano2023', 'calf training study')}, so pause at the bottom and don't rush the top.</p>
"""),
        ("volume", "How Many Sets and Reps on Leg Day?", f"""
<p>Each workout has 15–16 hard sets. Use 5–8 reps on heavy squats, 8–12 on most other exercises and 10–15 on isolation and calf work. Rest 2–3 minutes between sets of squats and deadlifts: longer rest built more leg muscle than one-minute rest in a {cite('rest2016', 'study on rest periods')}. Running the quad day and hamstring day each week gives your quads about 14 direct sets, your glutes about 18, your hamstrings 7 and your calves 6. The {cite('acsm2026', '2026 ACSM position stand')} links 10 or more weekly sets per muscle with more growth, so if your hamstrings lag, add 2–3 sets of seated leg curls to the end of the quad day.</p>
<p>New to leg training? Start with two sets per exercise and add a set every two weeks. Our guide to {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group')} explains how to adjust.</p>
"""),
        ("progression", "How to Progress Your Leg Day", f"""
<p>Add weight when you complete the top of the rep range on every set: 2.5–5 kg on squats, Romanian deadlifts and the leg press, and the smallest step available on machines. Track your numbers each session; if your squat stalls for three sessions in a row, take a lighter week. See {L('/what-is-progressive-overload/', 'progressive overload')} for more options, and our guide to {L('/types-of-squats/', 'types of squats')} if you need a different squat variation.</p>
"""),
        ("mistakes", "Leg Day Mistakes", f"""
<ul>
<li><strong>Cutting squat depth.</strong> Half squats build less muscle. Go as deep as you can with a neutral back. If your knees ache, read {L('/why-your-knees-hurt-when-squatting/', 'why your knees hurt when squatting')}.</li>
<li><strong>Skipping hamstrings.</strong> Squats and leg presses barely train them. Every leg day needs a hinge or a leg curl.</li>
<li><strong>Bouncing calf raises.</strong> Pause for a second at the bottom of each rep.</li>
<li><strong>Doing cardio-style circuits on leg day.</strong> Short rests and light weights tire you out without building much muscle.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Leg day: Quads", "c1"), ("Tue", "Upper body", "rest"), ("Wed", "Rest", "rest"), ("Thu", "Leg day: Hamstrings", "c2"), ("Fri", "Upper body", "rest"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Beginner", "tab_sub": "First leg day", "title": "Beginner Leg Day Workout", "tag": "Gym", "color": 1, "time": "50–60 min", "focus": "Quads / Hamstrings / Glutes / Calves",
         "exercises": [
             ("Goblet Squat", "Primary: quads, glutes · Secondary: adductors", "3 × 8–12", "2 min", "RIR 2"),
             ("Leg Press", "Primary: quads, glutes", "3 × 10–12", "2 min", "RIR 2"),
             ("Dumbbell Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 10–12", "2 min", "RIR 2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–15", "90 sec", "RIR 1–2"),
             ("Standing Calf Raise", "Primary: calves", "3 × 12–15", "60 sec", "RIR 1–2"),
         ],
         "notes": "Hold one dumbbell at your chest for goblet squats and sit down between your heels. Use this workout twice a week for your first 8–12 weeks."},
        {"tab": "Quad focus", "tab_sub": "Squat day", "title": "Leg Day A: Quad Focus", "tag": "Gym", "color": 2, "time": "55–65 min", "focus": "Quads / Glutes / Calves",
         "exercises": [
             ("Back Squat", "Primary: quads, glutes · Secondary: adductors", "4 × 5–8", "3 min", "RIR 2"),
             ("Leg Press", "Primary: quads, glutes", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "2 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("Leg Extension", "Primary: quads (incl. rectus femoris)", "3 × 10–15", "90 sec", "RIR 1"),
             ("Barbell Standing Calf Raise", "Primary: gastrocnemius", "3 × 10–15", "90 sec", "RIR 1–2"),
         ],
         "notes": "Keep your torso more upright on Bulgarian split squats to bias the quads. Pause one second in the stretch at the bottom of every calf raise."},
        {"tab": "Hamstring focus", "tab_sub": "Hinge day", "title": "Leg Day B: Hamstring and Glute Focus", "tag": "Gym", "color": 3, "time": "55–65 min", "focus": "Hamstrings / Glutes / Calves",
         "exercises": [
             ("Romanian Deadlift", "Primary: hamstrings, glutes", "4 × 6–10", "2–3 min", "RIR 2"),
             ("Barbell Hip Thrust", "Primary: glutes", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Seated Leg Curl", "Primary: hamstrings", "3 × 10–12", "90 sec", "RIR 1"),
             ("Walking Lunge", "Primary: glutes, quads", "2 × 10–12 / leg", "90 sec", "RIR 1–2"),
             ("Seated Calf Raise", "Primary: soleus", "3 × 12–15", "60 sec", "RIR 1"),
         ],
         "notes": "Lower the Romanian deadlift until you feel a strong hamstring stretch, usually just below the knee, keeping your back flat. The seated calf raise trains the soleus, which the standing version works less."},
        {"tab": "Dumbbells", "tab_sub": "Home or gym", "title": "Dumbbell Leg Day Workout", "tag": "Home gym", "color": 4, "time": "50–60 min", "focus": "Quads / Hamstrings / Glutes / Calves",
         "exercises": [
             ("Goblet Squat", "Primary: quads, glutes", "4 × 8–15", "2 min", "RIR 1–2"),
             ("Dumbbell Romanian Deadlift", "Primary: hamstrings, glutes", "4 × 8–12", "2 min", "RIR 1–2"),
             ("Bulgarian Split Squat", "Primary: quads, glutes", "3 × 8–12 / leg", "90 sec", "RIR 1–2"),
             ("Dumbbell Step-Up", "Primary: glutes, quads", "2 × 10–12 / leg", "90 sec", "RIR 1–2"),
             ("Single-Leg Calf Raise", "Primary: calves", "3 × 10–20 / leg", "60 sec", "RIR 1"),
         ],
         "notes": "Do this workout twice a week. Without a leg curl, the Romanian deadlift does all the hamstring work, so keep it heavy and slow. Do calf raises on a step with the heel dropping below it."},
    ],
    "faq_title": "Leg Day Workout FAQ",
    "faqs": [
        ("Can I build legs without squats?", "Yes. The leg press, Bulgarian split squat and hack squat all train the quads and glutes well. Squats are one good option, not a requirement."),
        ("Should I do cardio after leg day?", "Light walking or easy cycling is fine and can help you feel less stiff. Leave hard intervals or long runs for another day so they don't hurt your next leg session."),
        ("How long should leg day take?", "About 50–65 minutes including warm-up. Leg exercises need longer rests than upper-body work, so a leg day with 15–16 sets rarely fits into 30 minutes."),
        ("How many exercises should I do on leg day?", "Four to six is enough. Cover a squat or press, a hinge, a single-leg move and calves; adding more exercises past that usually means lower-quality sets on the ones that matter."),
        ("What should I train the day after leg day?", "Upper body. Your legs need 48–72 hours before another hard session, but your chest, back and arms are fresh."),
    ],
    "related": ["glute-workout", "upper-lower-split", "push-pull-legs", "5-day-workout-split"],
    "refs": refs("freq2016", "kubo2019", "maeo2021", "kassiano2023", "rest2016", "acsm2026"),
    "disclaimer": DISCLAIMER,
}
