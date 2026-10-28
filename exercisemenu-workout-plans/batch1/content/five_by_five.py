from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 4,
    "slug": "5x5-workout",
    "title": "5×5 Workout: Strength and Muscle Building Program",
    "meta_title": "5x5 Workout Program: Workouts A & B, Weights and Progression",
    "meta_desc": "The 5x5 workout explained: Workout A and B, starting weights, how much to add each session, what to do when you stall, and when to add accessories.",
    "focus_kw": "5x5 workout",
    "badge": "Barbell Strength",
    "hero_lead": "Five barbell lifts, two alternating workouts, three days a week. You add weight every session, and the program tells you exactly what to do when a lift stalls.",
    "hero_meta": ["📅 3 days/week", "⏱ 40–75 min", "📊 Beginner", "🏋️ Barbell, rack, bench"],
    "stats": [("3", "Training days"), ("2", "Workouts (A/B)"), ("5", "Barbell lifts"), ("+2.5–5 kg", "Per session"), ("3×", "Squats/week")],
    "quick_answer": "The 5x5 workout alternates two sessions three days a week. Workout A is squat, bench press and barbell row; Workout B is squat, overhead press and deadlift. Every lift is 5 sets of 5 except the deadlift (1 set of 5). Add 2.5 kg to upper-body lifts and 5 kg to squats and deadlifts each session.",
    "intro": "<p>Use the tabs to see Workout A and Workout B. Starting weights, the session-by-session progression and the stall rules follow.</p>",
    "sections": [
        ("schedule", "5×5 Schedule", f"""
{WEEK}
<p>Workouts alternate, so one week is A-B-A and the next is B-A-B. Keep a rest day between sessions. You squat every session; bench press, row, overhead press and deadlift each come up three times every two weeks.</p>
"""),
        ("workouts", "Workout A and Workout B", f"""
<p>Choose a workout. All five sets of five use the same weight. Rest about 3 minutes between sets and up to 5 minutes once the weights get heavy; in trained lifters, rests longer than 2 minutes produced more strength gains in a {cite('rest2018', 'systematic review')}.</p>
{TABS}
{box("science", "🔬 Why five sets?", f"<p>In a {cite('radaelli2015', '6-month study')} of untrained men training three times a week, 5 sets per exercise produced bigger strength gains on some lifts and more upper-arm muscle growth than 1 or 3 sets.</p>")}
"""),
        ("start", "Starting Weights", f"""
<ul>
<li><strong>Know your 5-rep max?</strong> Start at about 50% of it. If you can bench 80 kg for 5, start at 40 kg.</li>
<li><strong>New to lifting?</strong> Start every lift with the empty bar (20 kg men's bar, 15 kg women's bar).</li>
<li><strong>Deadlift:</strong> start light, but keep the bar at standard height (about 22 cm off the floor) by using full-size bumper plates or raising the bar on blocks or plates.</li>
</ul>
<p>Starting light is the point: you get weeks of practice on each lift before the weights become hard.</p>
"""),
        ("progression", "Linear Progression: Session by Session", f"""
<p>If you complete all 5 × 5, add weight next time you do that lift: +5 kg on squat and deadlift, +2.5 kg on bench press, overhead press and row. Example of the first two weeks:</p>
{table(["Session", "Workout", "Squat", "Bench / OHP", "Row / Deadlift"], [
    ["1 (Mon)", "A", "60 kg", "Bench 40 kg", "Row 40 kg"],
    ["2 (Wed)", "B", "65 kg", "OHP 30 kg", "Deadlift 70 kg"],
    ["3 (Fri)", "A", "70 kg", "Bench 42.5 kg", "Row 42.5 kg"],
    ["4 (Mon)", "B", "75 kg", "OHP 32.5 kg", "Deadlift 75 kg"],
    ["5 (Wed)", "A", "80 kg", "Bench 45 kg", "Row 45 kg"],
    ["6 (Fri)", "B", "85 kg", "OHP 35 kg", "Deadlift 80 kg"],
])}
<p>The squat climbs fastest because you squat every session. When 2.5 kg jumps get too big on the overhead press or bench press, use fractional plates (0.25–0.5 kg per side) for jumps of 0.5–1 kg. Warm up for every lift with the empty bar × 10, then about 40%, 60% and 80% of your work weight for 5, 3 and 2 reps; the {L('/warm-up-set-calculator/', 'warm-up set calculator')} does the maths.</p>
"""),
        ("stalls", "What to Do When You Stall", f"""
<ol class="emp-steps">
<li><strong>Miss once:</strong> keep the same weight next session.</li>
<li><strong>Miss twice:</strong> same weight again, with 5 minutes of rest between sets.</li>
<li><strong>Miss three times in a row:</strong> drop that lift by 10% and build back up.</li>
<li><strong>Stall again near the same weight:</strong> switch that lift to 3 × 5, then 3 × 3. Once you need 1 × 5, you have outgrown this program.</li>
</ol>
<p>At that point move to a program that progresses weekly rather than every session, such as our {L('/workout-plans/3-day-full-body-workout/', '3-day full body workout for intermediates')} or the {L('/workout-plans/upper-lower-split/', '4-day upper lower split')}.</p>
"""),
        ("accessories", "When to Add Accessories", f"""
<p>For the first 6–8 weeks, the five lifts are enough. After that, if you are sleeping well and still progressing, add these at the end of a session (10–15 minutes total):</p>
{table(["Accessory", "Sets × reps", "When"], [
    ["Barbell curl", "2 × 10–12", "After Workout A"],
    ["Triceps pushdown", "2 × 10–12", "After Workout B"],
    ["Plank", "3 × 30–60 sec", "After either workout"],
])}
"""),
        ("subs", "Exercise Substitutions", f"""
{table(["Programmed lift", "Substitution"], [
    ["Barbell back squat", "Front squat or safety-bar squat"],
    ["Barbell bench press", "Dumbbell bench press"],
    ["Barbell row", "Pendlay row or dumbbell row"],
    ["Overhead press", "Seated dumbbell shoulder press"],
    ["Conventional deadlift", "Trap bar deadlift or sumo deadlift"],
])}
<p>Swap one lift at a time; changing several turns it into a different program.</p>
"""),
        ("compare", "5×5 vs Other Beginner Programs", f"""
{table(["", "5×5 (this plan)", "Starting Strength", "Beginner full body"], [
    ["Main sets", "5 × 5 (deadlift 1 × 5)", "3 × 5 (deadlift 1 × 5)", "Usually 3 × 8–12"],
    ["Lifts", "Squat, bench, row, OHP, deadlift", "Squat, bench, OHP, deadlift, power clean", "Compound lifts plus machines and isolation"],
    ["Progression", "Add weight every session", "Add weight every session", "Reps first, then weight"],
])}
<p>Choose 5×5 if your main goal is barbell strength with a simple, fixed routine. If you also want to learn machines and higher-rep work, our {L('/workout-plans/full-body-workout-plan/', 'full body workout plan for beginners')} is a better fit.</p>
"""),
    ],
    "schedule": [("Mon", "Workout A", "c4"), ("Tue", "Rest", "rest"), ("Wed", "Workout B", "c2"), ("Thu", "Rest", "rest"), ("Fri", "Workout A", "c4"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Workout A", "tab_sub": "Squat · Bench · Row", "title": "Workout A", "tag": "Mon / Fri (week 1)", "color": 4, "time": "50–75 min", "focus": "Full body",
         "exercises": [
             ("Barbell Back Squat", "Primary: quads, glutes · Secondary: back, core", "5 × 5", "3–5 min", "All reps, good form"),
             ("Barbell Bench Press", "Primary: chest · Secondary: front delts, triceps", "5 × 5", "3–5 min", "All reps, good form"),
             ("Barbell Bent-Over Row", "Primary: upper back, lats · Secondary: biceps", "5 × 5", "3–5 min", "All reps, good form"),
         ],
         "notes": "Use a spotter or safety arms on the bench press, and squat inside a rack with the safety bars set just below your lowest position."},
        {"tab": "Workout B", "tab_sub": "Squat · OHP · Deadlift", "title": "Workout B", "tag": "Wed (week 1)", "color": 2, "time": "40–60 min", "focus": "Full body",
         "exercises": [
             ("Barbell Back Squat", "Primary: quads, glutes · Secondary: back, core", "5 × 5", "3–5 min", "All reps, good form"),
             ("Overhead Press (Barbell)", "Primary: shoulders · Secondary: triceps, upper chest", "5 × 5", "3–5 min", "All reps, good form"),
             ("Conventional Deadlift", "Primary: glutes, hamstrings, back · Secondary: grip", "1 × 5", "–", "All reps, good form"),
         ],
         "notes": f"The deadlift is one set because your lower back has already worked through five sets of squats. Read {L('/how-to-deadlift-for-beginners/', 'how to deadlift for beginners')} before your first session."},
    ],
    "faq_title": "5×5 Workout FAQ",
    "faqs": [
        ("Is 5x5 good for building muscle?", "Yes, especially for beginners. Heavy compound lifts done for several sets build muscle as well as strength, and adding arm accessories after 6–8 weeks covers the smaller muscles."),
        ("Can women do the 5x5 workout?", "Yes. The lifts and rules are the same. Women often start with a 15 kg bar and benefit from fractional plates sooner on upper-body lifts."),
        ("Can I do 5x5 with dumbbells only?", "You can follow the same structure with goblet squats, dumbbell presses, dumbbell rows and dumbbell Romanian deadlifts, but progress stalls sooner because dumbbell jumps are larger and maximum weights are lower."),
        ("Can I add cardio on rest days?", "Yes. Walking, cycling or swimming at an easy pace is fine. Avoid hard intervals the day before a session so your squats don't suffer."),
        ("How long can I keep progressing on 5x5?", "It varies with your starting strength, sleep and food. Many lifters progress for a few months before the stall rules move them to an intermediate program."),
    ],
    "related": ["beginner-strength-training-program", "powerlifting-program-for-beginners", "full-body-workout-plan", "3-day-full-body-workout"],
    "refs": refs("rest2018", "radaelli2015"),
    "disclaimer": DISCLAIMER,
}
