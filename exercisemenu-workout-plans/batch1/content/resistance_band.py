from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 35,
    "slug": "resistance-band-workout",
    "title": "Resistance Band Workout: 3-Day Full Body Plan for Home",
    "meta_title": "Resistance Band Workout: Free 3-Day Full Body Plan",
    "meta_desc": "Only have bands? This resistance band workout plan trains your whole body 3 days a week, with sets, reps, a beginner version and how to progress.",
    "focus_kw": "resistance band workout",
    "badge": "Home Workout Plan · Bands",
    "hero_lead": "Three full-body band workouts a week that train your legs, chest, back, shoulders, arms and core with nothing but a few resistance bands and a door anchor. Follow Workout A and B, or start with the 25-minute beginner version, and make the bands harder every week.",
    "hero_meta": ["📅 3 days/week", "⏱ 25–50 min", "📊 Beginner–Intermediate", "🏋️ Bands + door anchor"],
    "stats": [("3", "Days/week"), ("4", "Workout versions"), ("10–20", "Reps per set"), ("1–2", "Reps left in reserve"), ("18", "Exercises")],
    "quick_answer": "",
    "intro": "",
    "sections": [
        ("schedule", "Resistance Band Workout Schedule", f"""
{WEEK}
<p>Alternate Workout A and B on three non-consecutive days: A–B–A one week, B–A–B the next. Both workouts train your whole body, so each major muscle is worked three times a week with a rest day in between. Add the mini-band finisher to the end of any session if your hips and glutes need extra work.</p>
"""),
        ("workouts", "The Resistance Band Workouts", f"""
<p>Choose a band that lets you finish the listed reps with 1–2 clean reps left (RIR 1–2). Rest 60–90 seconds between sets, and warm up with 5 minutes of easy movement plus a light set of the first two exercises. New to training? Start with the beginner tab for 3–4 weeks, then move to Workouts A and B.</p>
{TABS}
"""),
        ("bands", "Which Resistance Bands You Need", f"""
{table(["Band type", "What it looks like", "Use it for"], [
    ["Long loop band (power band)", "A long closed loop, usually about 104 cm (41 in)", "Squats, Romanian deadlifts, presses, rows, push-ups"],
    ["Tube band with handles", "Tube with two handles, clips onto a door anchor", "Chest press, pulldowns, face pulls, curls"],
    ["Mini loop band", "Small loop worn around the thighs or ankles", "Glute bridges, side steps, hip abduction"],
])}
<p>Get at least three resistance levels (light, medium, heavy). Colours mean different resistances from brand to brand, so pick by feel: the right band is the one that makes the last reps of the set hard. Your legs and back will need heavier bands than your shoulders and arms.</p>
{box("science", "🔬 Are bands as good as weights?", f"<p>For strength, the research says yes. A {cite('lopes2019', 'meta-analysis of eight studies')} found elastic bands and tubes built upper- and lower-body strength as well as machines and dumbbells. In a {cite('calatayud2015', '5-week study')}, trained lifters who did band push-ups gained as much bench press strength as those who did the bench press at a similar effort.</p>")}
"""),
        ("progression", "How to Progress With Resistance Bands", f"""
<p>Bands don't come in 2.5 kg steps, so progress in this order. Move to the next step once you reach the top of the rep range on every set:</p>
{table(["Step", "What to change", "Example"], [
    ["1", "Add reps", "Squat: 3 × 12 → 3 × 15"],
    ["2", "Slow the lowering to 3 seconds and pause where the band is tightest", "Row: 1-second squeeze at the top"],
    ["3", "Add tension: step farther from the anchor or shorten the band", "Take one step back on chest presses"],
    ["4", "Move to a heavier band, or use two bands together", "Medium + light band on squats"],
])}
<p>A band gets harder as it stretches, so the top of each rep is the hardest part and the bottom is the easiest. Start every rep with a little tension on the band so the bottom still works. Our guide to {L('/progressive-overload-without-adding-weight/', 'progressive overload without adding weight')} has more options.</p>
"""),
        ("volume", "How Many Sets and Reps With Resistance Bands?", f"""
<p>Use 10–20 reps per set and stop 1–2 reps short of failure. Higher reps are fine with bands: light loads built similar muscle to heavy loads in a {cite('load2021', 'network meta-analysis')} when sets were taken close to failure, while heavier loads built a little more maximal strength. Alternating A and B gives your quads, chest and back about 9 hard sets a week and your glutes more. The {cite('acsm2026', '2026 ACSM position stand')} links 10 or more weekly sets per muscle with more growth, so once you recover well, add one set to the first two exercises of each workout. Our guide to {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group')} shows how to adjust.</p>
"""),
        ("mistakes", "Resistance Band Mistakes and Safety", f"""
<ul>
<li><strong>Using a worn band.</strong> Check every band for nicks, cracks or thin spots before each session, and replace it if you find one. A band that snaps can hit your face.</li>
<li><strong>Anchoring on the wrong side of the door.</strong> Fit the door anchor on the hinge side and stand on the side the door opens away from, so pulling presses the door shut. Lock it if you can.</li>
<li><strong>Letting the band snap back.</strong> Lower every rep under control; the slow return trains your muscles too.</li>
<li><strong>Staying on the same band for months.</strong> If you can do more than 20 easy reps, the band is too light. Use the progression steps above.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Workout A", "c1"), ("Tue", "Rest", "rest"), ("Wed", "Workout B", "c2"), ("Thu", "Rest", "rest"), ("Fri", "Workout A", "c1"), ("Sat", "Rest / walk", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Workout A", "tab_sub": "Squat + push + row", "title": "Resistance Band Workout A", "tag": "Full body", "when": "Mon & Fri in week 1, Wed in week 2", "color": 1, "time": "40–50 min", "focus": "Legs / Chest / Back / Shoulders / Core",
         "exercises": [
             ("Band Squat", "Primary: quads, glutes · Band under feet, over shoulders", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Band Push-Up", "Primary: chest, triceps · Band across upper back", "3 × 8–15", "90 sec", "RIR 1–2"),
             ("Band Bent-Over Row", "Primary: lats, upper back · Secondary: biceps", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Band Romanian Deadlift", "Primary: hamstrings, glutes", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Band Overhead Press", "Primary: shoulders · Secondary: triceps", "2 × 10–15", "60 sec", "RIR 1–2"),
             ("Band Pull-Apart", "Primary: rear delts, upper back", "2 × 15–20", "60 sec", "RIR 1"),
             ("Pallof Press", "Primary: obliques (anti-rotation)", "2 × 10 / side", "45 sec", "RIR 2"),
         ],
         "notes": "On squats and Romanian deadlifts, stand on the band with feet hip-width apart and keep the band over your shoulders or in your hands. On push-ups, hold one end of the band in each hand with the band across your upper back."},
        {"tab": "Workout B", "tab_sub": "Lunge + press + pulldown", "title": "Resistance Band Workout B", "tag": "Full body", "when": "Wed in week 1, Mon & Fri in week 2", "color": 2, "time": "40–50 min", "focus": "Legs / Chest / Back / Arms",
         "exercises": [
             ("Band Split Squat", "Primary: quads, glutes · Band under front foot", "3 × 10–12 / leg", "90 sec", "RIR 1–2"),
             ("Band Chest Press", "Primary: chest · Secondary: triceps · Anchor behind you at chest height", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Band Lat Pulldown", "Primary: lats · Secondary: biceps · Anchor at the top of the door", "3 × 12–15", "90 sec", "RIR 1–2"),
             ("Band Glute Bridge", "Primary: glutes · Band across the hips, held down by your hands", "3 × 12–20", "60 sec", "RIR 1–2"),
             ("Band Face Pull", "Primary: rear delts, upper back · Anchor at face height", "2 × 15–20", "60 sec", "RIR 1"),
             ("Band Biceps Curl", "Primary: biceps", "2 × 12–20", "60 sec", "RIR 1"),
             ("Band Overhead Triceps Extension", "Primary: triceps", "2 × 12–20", "60 sec", "RIR 1"),
         ],
         "notes": "Kneel facing the door for pulldowns and pull your elbows down to your sides. For the chest press, stand far enough from the anchor that the band is already tight at the start."},
        {"tab": "Beginner", "tab_sub": "25 minutes", "title": "Beginner Resistance Band Workout", "tag": "Beginner", "when": "Mon · Wed · Fri", "color": 4, "time": "25–30 min", "focus": "Whole body",
         "exercises": [
             ("Band Squat", "Primary: quads, glutes", "2 × 12–15", "60 sec", "RIR 2"),
             ("Band Seated Row", "Primary: lats, upper back · Band around your feet, legs straight", "2 × 12–15", "60 sec", "RIR 2"),
             ("Band Chest Press", "Primary: chest, triceps", "2 × 12–15", "60 sec", "RIR 2"),
             ("Band Glute Bridge", "Primary: glutes", "2 × 15", "60 sec", "RIR 2"),
             ("Band Overhead Press", "Primary: shoulders", "2 × 10–12", "60 sec", "RIR 2"),
             ("Pallof Press", "Primary: obliques", "2 × 8 / side", "45 sec", "RIR 2"),
         ],
         "notes": "Use a light or medium band and focus on smooth reps. After 3–4 weeks, or once every set feels easy at 15 reps, switch to Workouts A and B."},
        {"tab": "Mini-band", "tab_sub": "10-min glute finisher", "title": "Mini-Band Glute and Hip Finisher", "tag": "Add-on", "when": "After any workout, up to 3 times a week", "color": 6, "time": "10 min", "focus": "Glutes / Outer hips",
         "exercises": [
             ("Mini-Band Glute Bridge", "Primary: glutes · Band just above the knees", "2 × 15–20", "45 sec", "RIR 1–2"),
             ("Lateral Band Walk", "Primary: gluteus medius · Band above the knees or at the ankles", "2 × 12 steps / side", "45 sec", "RIR 1–2"),
             ("Side-Lying Hip Abduction", "Primary: gluteus medius and minimus", "2 × 15 / side", "45 sec", "RIR 1"),
         ],
         "notes": "Keep your knees pushed out against the band on every rep. Moving the band from above the knees to the ankles makes side steps harder."},
    ],
    "swap_overrides": {
        "Band Squat": "Goblet Squat (if you have a dumbbell)", "Band Push-Up": "Push-Up", "Band Bent-Over Row": "Band Seated Row",
        "Band Romanian Deadlift": "Band Good Morning", "Band Overhead Press": "Pike Push-Up", "Band Pull-Apart": "Band Face Pull",
        "Pallof Press": "Side Plank", "Band Split Squat": "Reverse Lunge", "Band Chest Press": "Band Push-Up",
        "Band Lat Pulldown": "Band Bent-Over Row", "Band Glute Bridge": "Single-Leg Glute Bridge", "Band Face Pull": "Band Pull-Apart",
        "Band Biceps Curl": "Band Hammer Curl", "Band Overhead Triceps Extension": "Band Triceps Pushdown", "Band Seated Row": "Band Bent-Over Row",
        "Mini-Band Glute Bridge": "Glute Bridge", "Lateral Band Walk": "Mini-Band Monster Walk", "Side-Lying Hip Abduction": "Mini-Band Clamshell",
    },
    "faq_title": "Resistance Band Workout FAQ",
    "faqs": [
        ("Can you build muscle with resistance bands?", "Yes, as long as your sets are hard. Muscle grows from sets taken close to failure, and bands let you do that at home. Move to heavier bands as you get stronger and eat enough protein; beginners usually see the fastest progress."),
        ("Are resistance bands better than dumbbells?", "Neither is better for building strength; the research shows similar gains. Dumbbells are easier to load in small steps, while bands are cheaper, lighter and easier to store, which makes them a good choice for home and travel."),
        ("Do resistance bands lose resistance over time?", "Yes. Latex bands slowly wear with use, heat and sunlight. Store them out of direct sun, keep them away from sharp edges, and replace any band that has cracks, nicks or no longer snaps back fully."),
        ("Can I combine resistance bands with dumbbells?", "Yes. A simple setup is dumbbells for squats, lunges and Romanian deadlifts, and bands for rows, pulldowns, face pulls and pull-aparts, which are hard to do with dumbbells alone."),
        ("What if I don't have a door anchor?", "Loop the band around a sturdy post or railing, or stand on it. Squats, Romanian deadlifts, rows, presses, curls and push-ups all work with the band under your feet or across your back."),
    ],
    "related": ["full-body-workout-plan", "glute-workout", "core-workout", "strength-training-for-women"],
    "refs": refs("lopes2019", "calatayud2015", "load2021", "acsm2026"),
    "disclaimer": DISCLAIMER,
}
