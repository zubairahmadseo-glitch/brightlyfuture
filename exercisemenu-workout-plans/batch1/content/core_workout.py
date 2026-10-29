from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 62,
    "slug": "core-workout",
    "title": "Core Workout: Short Ab and Core Plan for Gym or Home",
    "meta_title": "Core Workout: 20-Minute Ab & Core Plan (Gym or Home)",
    "meta_desc": "Short on time? This core workout trains your abs, obliques and lower back in about 20 minutes, 3 days a week, with gym, home and 10-minute versions.",
    "focus_kw": "core workout",
    "badge": "Body Part Plan · Core",
    "hero_lead": "Three short core sessions a week that train every job your core does: bending, resisting bending, resisting twisting and carrying. Do them after your main workout or on their own, at the gym or at home.",
    "hero_meta": ["📅 3 core days/week", "⏱ 10–25 min", "📊 Beginner–Intermediate", "🏋️ Gym or home"],
    "stats": [("3", "Core days/week"), ("4", "Workout versions"), ("20–25", "Minutes per session"), ("5", "Core functions trained"), ("14", "Exercises")],
    "quick_answer": "A complete core workout includes one exercise for each core job: a crunch or leg raise, a plank or ab wheel, an anti-rotation press, a side plank or carry, and a back extension. Do 2–3 sets of each, three times a week, and make them harder once they feel easy.",
    "intro": "<p>Choose a version in the tabs. Under the workouts you'll find what each exercise trains, how to make core exercises harder and why core training alone won't show your abs.</p>",
    "sections": [
        ("schedule", "Core Workout Schedule", f"""
{WEEK}
<p>Put core work at the end of your gym sessions on three non-consecutive days. Doing it first can tire the muscles that keep your trunk stable during squats and deadlifts. Alternate Core A and Core B; on busy days, do the 10-minute version.</p>
"""),
        ("workouts", "The Core Workouts", f"""
<p>Holds are written in seconds; "/ side" means do the time or reps on each side. Rest 45–60 seconds between sets.</p>
{TABS}
"""),
        ("functions", "What Each Core Exercise Trains", f"""
<p>Your core is more than your six-pack muscle. It includes the rectus abdominis, the obliques on your sides, the deep transverse abdominis and the muscles along your spine. Core A and Core B each train all of them by covering these five jobs:</p>
{table(["Core job", "Main muscles", "Exercises in this plan"], [
    ["Bending forward (flexion)", "Rectus abdominis", "Cable crunch, reverse crunch, hanging knee raise"],
    ["Resisting arching (anti-extension)", "Rectus abdominis, transverse abdominis", "Plank, ab wheel rollout, dead bug"],
    ["Resisting twisting (anti-rotation)", "Obliques", "Pallof press, bird dog"],
    ["Resisting side bending", "Obliques, quadratus lumborum", "Side plank, suitcase carry"],
    ["Extending the spine", "Erector spinae, glutes", "Back extension"],
])}
<p>Rotation exercises such as the cable wood chop and the {L('/medicine-ball-ab-exercises/', 'medicine ball Russian twist')} add a sixth job, turning the trunk, and are optional extras.</p>
"""),
        ("progression", "How to Make Core Exercises Harder", f"""
<p>Your abs adapt like any other muscle, so the same plank every week soon stops challenging them. Progress in this order:</p>
{table(["Exercise type", "When to progress", "How"], [
    ["Holds (plank, side plank)", "You can hold 45–60 sec with good form", "Move to a harder version (feet elevated, long-lever plank) instead of holding longer"],
    ["Reps (crunch, leg raise)", "You hit the top of the rep range on every set", "Add weight on the cable stack or straighten your legs"],
    ["Carries", "You walk 30 m without leaning", "Use a heavier weight"],
])}
<p>For more hold-based moves, see our list of {L('/isometric-exercises/', 'isometric exercises')}.</p>
"""),
        ("abs", "Will a Core Workout Give You Visible Abs?", f"""
<p>Not on its own. Everyone has abdominal muscles; you can see them only when little enough fat covers them. In a {cite('vispute2011', 'controlled study')}, people who did ab exercises five days a week for six weeks improved their ab endurance but lost no more belly fat than people who didn't train. A core workout makes your abs stronger; overall fat loss through your diet decides when they show.</p>
"""),
        ("mistakes", "Core Workout Mistakes", f"""
<ul>
<li><strong>Arching your lower back.</strong> If your back sags in a plank or lifts off the floor in a dead bug, shorten the lever or the range until you can keep it flat.</li>
<li><strong>Pulling on your neck.</strong> In crunches, curl your ribs toward your hips; your hands only support your head.</li>
<li><strong>Doing only crunches.</strong> Crunches train one of the five jobs. A balanced core workout covers all of them.</li>
<li><strong>Holding planks for minutes.</strong> Once you can hold 60 seconds, a harder 30–45 second variation does more than a longer hold.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Core A", "c1"), ("Tue", "Rest from core", "rest"), ("Wed", "Core B", "c2"), ("Thu", "Rest from core", "rest"), ("Fri", "Core A", "c1"), ("Sat", "Rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Core A", "tab_sub": "Gym", "title": "Core Workout A (Gym)", "tag": "Gym", "color": 1, "time": "20–25 min", "focus": "Abs / Obliques / Lower back",
         "exercises": [
             ("Cable Crunch", "Primary: rectus abdominis", "3 × 10–15", "60 sec", "RIR 1–2"),
             ("Pallof Press", "Primary: obliques (anti-rotation)", "2 × 10 / side", "45 sec", "RIR 2"),
             ("Dead Bug", "Primary: transverse abdominis, rectus abdominis", "2 × 8 / side", "45 sec", "Slow and controlled"),
             ("Side Plank", "Primary: obliques, quadratus lumborum", "2 × 20–45 sec / side", "45 sec", "Hold with good form"),
             ("Back Extension", "Primary: erector spinae · Secondary: glutes, hamstrings", "2 × 10–15", "60 sec", "RIR 2"),
         ],
         "notes": "Kneel facing the cable for crunches and round your spine down toward your knees; keep your hips still. On dead bugs, press your lower back into the floor the whole time."},
        {"tab": "Core B", "tab_sub": "Gym", "title": "Core Workout B (Gym)", "tag": "Gym", "color": 2, "time": "20–25 min", "focus": "Abs / Obliques / Lower back",
         "exercises": [
             ("Ab Wheel Rollout", "Primary: rectus abdominis (anti-extension)", "3 × 6–12", "60 sec", "RIR 2"),
             ("Cable Wood Chop", "Primary: obliques (rotation)", "2 × 10 / side", "45 sec", "RIR 2"),
             ("Hanging Knee Raise", "Primary: rectus abdominis, hip flexors", "2 × 8–15", "60 sec", "RIR 1–2"),
             ("Suitcase Carry", "Primary: obliques, quadratus lumborum · Secondary: grip", "2 × 20–30 m / side", "60 sec", "Heavy, no leaning"),
             ("Bird Dog", "Primary: erector spinae, obliques · Secondary: glutes", "2 × 8 / side", "45 sec", "Pause 2 sec each rep"),
         ],
         "notes": "Start ab wheel rollouts from your knees and roll only as far as you can without your lower back sagging. Carry a dumbbell or kettlebell in one hand and walk tall. Raise your knees to hip height or higher on knee raises without swinging."},
        {"tab": "At home", "tab_sub": "No equipment", "title": "Core Workout at Home", "tag": "Home", "color": 4, "time": "20–25 min", "focus": "Abs / Obliques / Lower back",
         "exercises": [
             ("Reverse Crunch", "Primary: rectus abdominis", "3 × 10–15", "45 sec", "RIR 1–2"),
             ("Plank", "Primary: rectus abdominis, transverse abdominis", "3 × 20–45 sec", "45 sec", "Hold with good form"),
             ("Side Plank", "Primary: obliques, quadratus lumborum", "2 × 20–45 sec / side", "45 sec", "Hold with good form"),
             ("Dead Bug", "Primary: transverse abdominis, rectus abdominis", "2 × 8 / side", "45 sec", "Slow and controlled"),
             ("Superman Hold", "Primary: erector spinae · Secondary: glutes", "2 × 20–30 sec", "45 sec", "Hold with good form"),
         ],
         "notes": "Lift your hips off the floor on reverse crunches by curling your pelvis, not by swinging your legs. For the superman, lift your chest and legs a few centimetres and keep your neck in line."},
        {"tab": "10-minute", "tab_sub": "Busy days", "title": "10-Minute Core Workout", "tag": "Home or gym", "color": 6, "time": "10 min", "focus": "Whole core",
         "exercises": [
             ("Dead Bug", "Primary: transverse abdominis", "2 rounds × 40 sec", "20 sec", "Steady pace"),
             ("Bicycle Crunch", "Primary: rectus abdominis, obliques", "2 rounds × 40 sec", "20 sec", "Slow, controlled reps"),
             ("Side Plank", "Primary: obliques", "2 rounds × 20 sec / side", "20 sec", "Hold with good form"),
             ("Bird Dog", "Primary: erector spinae, obliques", "2 rounds × 40 sec", "20 sec", "Pause each rep"),
         ],
         "notes": "Do the four exercises back to back as a circuit, rest 60 seconds, then repeat once. Use this version on days you're short on time; Core A, Core B or the home workout build more strength."},
    ],
    "faq_title": "Core Workout FAQ",
    "faqs": [
        ("Can I train my core every day?", "Light core work every day is fine for most people, but daily hard sessions don't leave time to recover. Three focused sessions a week is enough to get stronger."),
        ("Do squats and deadlifts train my core?", "They do, mainly the muscles that keep your trunk stiff and your spine still. They don't train bending forward or resisting side bending much, which is why direct core exercises are still worth doing."),
        ("Is a core workout upper or lower body?", "Neither. Your core connects the two, so you can add it to the end of either session."),
        ("How many reps and sets should I do for abs?", "Most people do well with 2–3 sets of 10–15 reps, or 20–45 second holds, per exercise. Once you can do more than 15–20 clean reps, add weight or switch to a harder variation."),
        ("Should I feel my lower back during core exercises?", "No. Feeling it in your lower back usually means your back is arching. Shorten the lever (bend your knees, plank on your knees) and only progress once your back stays flat. See a physiotherapist if your back hurts."),
    ],
    "related": ["glute-workout", "leg-day-workout", "full-body-workout-plan", "strength-training-for-women"],
    "refs": refs("vispute2011"),
    "disclaimer": DISCLAIMER,
}
