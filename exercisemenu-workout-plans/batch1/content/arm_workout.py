from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 100,
    "slug": "arm-workout",
    "title": "Arm Workout: Biceps and Triceps Plan for Gym or Home",
    "meta_title": "Arm Workout: Free Biceps & Triceps Plan (Gym or Home)",
    "meta_desc": "Want bigger arms? This arm workout trains biceps and triceps twice a week, with gym, dumbbell and resistance band versions plus weekly progression.",
    "focus_kw": "arm workout",
    "badge": "Body Part Plan · Arms",
    "hero_lead": "Two arm workouts a week that train every part of your biceps and triceps: a heavy curl, an overhead triceps move, a press and a hammer curl for the forearms. Choose the gym, dumbbell or band version and add a rep or a little weight each week.",
    "hero_meta": ["📅 2 arm days/week", "⏱ 30–45 min", "📊 Beginner–Intermediate", "🏋️ Gym, dumbbells or bands"],
    "stats": [("2", "Arm days/week"), ("4", "Workout versions"), ("12–16", "Sets per muscle/week"), ("8–15", "Reps per set"), ("15", "Exercises")],
    "quick_answer": "A good arm workout pairs 2–3 biceps curls with 2–3 triceps exercises, including one overhead extension. Train arms twice a week for about 12–16 sets per muscle, use 8–15 reps, stop 1–2 reps short of failure and add reps or weight every week.",
    "intro": "<p>Pick a version in the tabs. Below the workouts you'll see which exercise trains which part of your arm, how many sets you need when you also do presses and rows, and how to keep progressing.</p>",
    "sections": [
        ("schedule", "Arm Workout Schedule", f"""
{WEEK}
<p>Keep the two arm sessions 2–3 days apart. You can run them as stand-alone arm days or add them to the end of an upper-body, push or pull day. If you already press and row heavy the day before, start with the dumbbell version so your elbows aren't overloaded.</p>
"""),
        ("workouts", "The Arm Workouts", f"""
<p>Rest 60–90 seconds between sets, or pair one biceps and one triceps exercise as a superset to save time. RIR (reps in reserve) 1 means you finish the set with one clean rep left.</p>
{TABS}
"""),
        ("exercises", "Best Arm Exercises by Muscle", f"""
<p>Your triceps make up more of your upper arm than your biceps, so they get as much work here as the curls do.</p>
{table(["Muscle", "What it does", "Best exercises in this plan"], [
    ["Biceps (long and short head)", "Bends the elbow, turns the palm up", "Barbell curl, incline dumbbell curl, preacher curl"],
    ["Brachialis and brachioradialis", "Bends the elbow with a neutral grip", "Hammer curl"],
    ["Triceps long head", "Straightens the elbow, pulls the arm down", "Overhead extension, lying triceps extension"],
    ["Triceps lateral and medial heads", "Straighten the elbow", "Close-grip bench press, pushdown"],
])}
{box("science", "🔬 What the research shows", f"<p>Overhead work matters for the triceps: in a {cite('maeo2023', '12-week study')}, cable extensions done with the arm overhead grew the whole triceps about 1.4 times more than the same exercise with the arm at the side. For the biceps, a {cite('mannarino2021', '2021 study')} found that biceps curls built about twice as much elbow-flexor muscle as dumbbell rows in beginners, so rows alone won't max out your biceps.</p>")}
<p>The incline curl and the overhead extension both load the muscle while it is stretched, which is why each workout includes one of them.</p>
"""),
        ("volume", "How Many Sets for Arms per Week?", f"""
<p>This plan gives each muscle about 12–16 direct sets a week. Rows and pull-downs also train your biceps, and presses train your triceps, so count each pulling or pressing set as about half a set for your arms, as the {cite('pelland2026', '2026 dose-response meta-analysis')} did. That means if you already do 10 sets of rows a week, your biceps get roughly 5 extra sets from them.</p>
<p>Training a muscle twice a week builds more muscle than once a week in a {cite('freq2016', 'meta-analysis of training frequency')}, and the {cite('acsm2026', '2026 ACSM position stand')} links 10 or more weekly sets per muscle with more growth. If your elbows get sore, drop one exercise per workout before you drop a session. Our guide to {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group')} shows how to adjust volume.</p>
"""),
        ("progression", "How to Progress Your Arm Workout", f"""
<p>Arm exercises use small weights, so progress with reps first. Stay at one weight until you hit the top of the rep range on every set, then move up by the smallest step available: 1–2 kg per dumbbell or one pin on a cable stack. A 2 kg jump on a 10 kg curl is a 20% increase, so expect reps to drop and build back up. That is {L('/what-is-progressive-overload/', 'progressive overload')} for small muscles.</p>
<p>Every 6–8 weeks, swap one exercise per muscle (for example, preacher curl to cable curl) and take a lighter week with half the sets.</p>
"""),
        ("mistakes", "Arm Workout Mistakes", f"""
<ul>
<li><strong>Swinging the weight.</strong> If your hips or shoulders move, the load is too heavy. Keep your upper arms still and lower each rep in about two seconds.</li>
<li><strong>Short reps.</strong> Straighten your arm fully at the bottom of curls and bend fully on extensions. Cutting the bottom of the rep skips the stretched position this plan is built around.</li>
<li><strong>Only doing biceps.</strong> Skipping triceps leaves the bigger part of your arm untrained.</li>
<li><strong>Training arms on the day before a heavy press or pull day.</strong> Tired arms limit your bench press and rows. Put arm work after those sessions, not before them.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Other muscles", "rest"), ("Tue", "Arms A", "c1"), ("Wed", "Other muscles", "rest"), ("Thu", "Other muscles", "rest"), ("Fri", "Arms B", "c2"), ("Sat", "Other / rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Gym A", "tab_sub": "Heavy curl + press", "title": "Arm Workout A: Heavy Day", "tag": "Gym", "color": 1, "time": "35–45 min", "focus": "Biceps / Triceps",
         "exercises": [
             ("Barbell Curl", "Primary: biceps · Secondary: forearms", "3 × 8–10", "90 sec", "RIR 1–2"),
             ("Close-Grip Bench Press", "Primary: triceps · Secondary: chest", "3 × 6–10", "2 min", "RIR 1–2"),
             ("Incline Dumbbell Curl", "Primary: biceps (stretched)", "3 × 10–12", "60–90 sec", "RIR 1"),
             ("Overhead Cable Triceps Extension", "Primary: triceps long head", "3 × 10–12", "60–90 sec", "RIR 1"),
             ("Hammer Curl", "Primary: brachialis, brachioradialis", "2 × 10–12", "60 sec", "RIR 1"),
         ],
         "notes": "Use a shoulder-width grip on the close-grip bench press; a narrow grip strains the wrists. Set the incline bench to about 45° for curls."},
        {"tab": "Gym B", "tab_sub": "Isolation day", "title": "Arm Workout B: Isolation Day", "tag": "Gym", "color": 2, "time": "30–40 min", "focus": "Biceps / Triceps",
         "exercises": [
             ("Barbell Lying Triceps Extension", "Primary: triceps long head", "3 × 8–12", "90 sec", "RIR 1–2"),
             ("EZ-Bar Preacher Curl", "Primary: biceps", "3 × 8–12", "90 sec", "RIR 1–2"),
             ("Triceps Pushdown", "Primary: triceps lateral and medial heads", "3 × 10–15", "60 sec", "RIR 1"),
             ("Dumbbell Biceps Curl", "Primary: biceps", "3 × 10–12", "60 sec", "RIR 1"),
         ],
         "notes": "Lower the bar on lying extensions to just behind your head, not your nose, so the long head works through a full stretch. Superset the last two exercises if you're short on time."},
        {"tab": "Dumbbells", "tab_sub": "Home or gym", "title": "Arm Workout: Dumbbells Only", "tag": "Home gym", "color": 4, "time": "35–45 min", "focus": "Biceps / Triceps",
         "exercises": [
             ("Dumbbell Biceps Curl", "Primary: biceps", "3 × 8–12", "60–90 sec", "RIR 1–2"),
             ("Close-Grip Dumbbell Press", "Primary: triceps · Secondary: chest", "3 × 8–12", "90 sec", "RIR 1–2"),
             ("Incline Dumbbell Curl", "Primary: biceps (stretched)", "3 × 10–12", "60 sec", "RIR 1"),
             ("Overhead Dumbbell Triceps Extension", "Primary: triceps long head", "3 × 10–12", "60 sec", "RIR 1"),
             ("Hammer Curl", "Primary: brachialis, brachioradialis", "2 × 10–12", "60 sec", "RIR 1"),
         ],
         "notes": "Do this workout twice a week. Press the dumbbells with palms facing each other and elbows close to your sides. Hold one dumbbell with both hands for the overhead extension."},
        {"tab": "Bands", "tab_sub": "No weights", "title": "Arm Workout: Resistance Bands and Bodyweight", "tag": "Home", "color": 6, "time": "30–40 min", "focus": "Biceps / Triceps",
         "exercises": [
             ("Diamond Push-Up", "Primary: triceps · Secondary: chest", "3 × as many as possible", "90 sec", "RIR 1"),
             ("Band Curl", "Primary: biceps", "3 × 12–20", "60 sec", "RIR 1"),
             ("Band Overhead Triceps Extension", "Primary: triceps long head", "3 × 12–20", "60 sec", "RIR 1"),
             ("Band Hammer Curl", "Primary: brachialis, brachioradialis", "3 × 12–20", "60 sec", "RIR 1"),
         ],
         "notes": f"Higher reps work as long as you finish each set close to failure: light and heavy loads built similar muscle in a {cite('load2021', 'meta-analysis')} when sets were hard. When 20 reps feel easy, use a thicker band or stand farther from the anchor."},
    ],
    "faq_title": "Arm Workout FAQ",
    "faqs": [
        ("Can I do an arm workout every day?", "It's not a good idea. Your biceps and triceps also work during every pull and press, so daily arm sessions leave them with no time to recover. Two or three arm sessions a week is enough to grow."),
        ("Will arm exercises get rid of flabby arms?", f"No exercise burns fat from one spot. In a {cite('vispute2011', '6-week study on ab training')}, targeted exercise didn't reduce fat in the trained area. Arm training builds the muscle underneath, and overall fat loss comes from your diet and total activity."),
        ("Are pull-ups and push-ups enough for arms?", "They train your arms, but less than direct work does. If arm size is a goal, add at least 2–3 sets of curls and triceps extensions twice a week."),
        ("How long until my arms get bigger?", "Training studies usually measure arm growth after 8–12 weeks of twice-weekly training. Arm size changes slowly, so track your curl and extension weights to see progress sooner."),
        ("Should I train biceps or triceps first?", "Start with whichever is weaker. Pairing a biceps and a triceps exercise as a superset also works and shortens the session."),
    ],
    "related": ["chest-workout", "bro-split", "push-pull-legs", "hypertrophy-program"],
    "refs": refs("maeo2023", "mannarino2021", "pelland2026", "freq2016", "acsm2026", "load2021", "vispute2011"),
    "disclaimer": DISCLAIMER,
}
