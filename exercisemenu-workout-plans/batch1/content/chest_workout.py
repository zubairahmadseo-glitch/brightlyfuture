from .common import L, box, table, cite, refs, WEEK, TABS, DISCLAIMER

PAGE = {
    "num": 97,
    "slug": "chest-workout",
    "title": "Chest Workout: Best Chest Exercises and a 4-Week Plan",
    "meta_title": "Chest Workout: Best Exercises + Free 4-Week Chest Plan",
    "meta_desc": "A chest workout plan you can follow today: the best chest exercises for upper, middle and lower chest, plus gym, dumbbell and no-equipment versions.",
    "focus_kw": "chest workout",
    "badge": "Body Part Plan · Chest",
    "hero_lead": "Two chest workouts a week, built around presses at two bench angles, a fly and dips or push-ups. Pick the gym, dumbbell or no-equipment version and follow the 4-week progression.",
    "hero_meta": ["📅 2 chest days/week", "⏱ 30–50 min", "📊 Beginner–Intermediate", "🏋️ Gym, dumbbells or home"],
    "stats": [("2", "Chest days/week"), ("4", "Workout versions"), ("20–24", "Chest sets/week"), ("4 wk", "Progression block"), ("12", "Exercises")],
    "quick_answer": "A good chest workout starts with a heavy press, adds an incline press for the upper chest, then finishes with a fly and dips or push-ups. Train chest twice a week for about 20 hard sets (fewer in your first weeks), with 6–15 reps per set, and add weight or reps every week.",
    "intro": "<p>Choose a workout in the tabs. Below the workouts you'll find which exercise hits which part of your chest, the 4-week progression and how to fit these sessions into your split.</p>",
    "sections": [
        ("schedule", "Chest Workout Schedule", f"""
{WEEK}
<p>Put the two chest workouts 2–3 days apart, such as Monday and Thursday, and train your other muscles on the remaining days. Workout A leads with the flat bench press; Workout B leads with an incline press, so across the week you train every part of the chest with heavy and moderate loads.</p>
"""),
        ("workouts", "The Chest Workouts", f"""
<p>Pick your version. Effort is shown as RIR (reps in reserve): RIR 1–2 means you stop with one or two clean reps left. New to lifting? Use 2 sets per exercise for the first two weeks.</p>
{TABS}
"""),
        ("exercises", "Best Chest Exercises by Area", f"""
<p>Your pectoralis major has an upper (clavicular) part and a larger middle-to-lower (sternal) part, and the bench angle changes which part works hardest.</p>
{table(["Exercise", "Main area", "Why it's in the plan"], [
    ["Flat barbell or dumbbell bench press", "Middle and lower chest", "Heaviest chest lift; the best one to progress for strength"],
    ["Incline press (about 30°)", "Upper chest", "30° gave the highest upper-chest activity in an EMG study"],
    ["Dips (leaning forward)", "Lower chest, triceps", "Loads the chest through a deep stretch"],
    ["Cable or dumbbell fly", "Whole chest", "Trains the chest without the triceps limiting the set"],
    ["Push-up", "Whole chest, triceps", "Builds muscle like a light bench press when the load is similar"],
])}
{box("science", "🔬 Flat vs incline", f"<p>In a {cite('ridao2020', 'study of five bench angles')}, upper-chest activity peaked at 30°, while angles above 45° shifted the work to the front delts. In an {cite('chaves2020', '8-week training study')}, the incline group grew more upper-chest muscle than the flat-bench group, with similar strength gains. That's why Workout B uses a 30° incline instead of a steep one.</p>")}
<p>There is no separate "inner chest" muscle to isolate; the fibres run across the whole chest, so a full range of motion on presses and flyes trains the inner area too. For more cable options, see our {L('/cable-chest-exercises-10-best-moves/', 'cable chest exercises')}.</p>
"""),
        ("progression", "4-Week Progression", f"""
{table(["Week", "Sets", "Effort", "What to do"], [
    ["1", "As listed", "RIR 3", "Learn loads and settings"],
    ["2", "As listed", "RIR 2", "Beat week 1 by a rep or a little weight"],
    ["3", "+1 set on the first exercise", "RIR 1–2", "Push the main press"],
    ["4", "Same as week 3", "RIR 1", "Hardest week; then repeat with heavier starting loads"],
])}
<p>Within each week, use double progression: once every set reaches the top of its rep range, add the smallest jump available (2.5 kg on a barbell, 1–2 kg per dumbbell) and build the reps back up. That is the core of {L('/what-is-progressive-overload/', 'progressive overload')}. After two 4-week blocks, take a lighter week with half the sets.</p>
"""),
        ("volume", "How Many Chest Sets per Week?", f"""
<p>The two gym workouts give you about 20 hard chest sets a week, and the dumbbell and home versions about 24, because you do the same workout twice. The {cite('acsm2026', '2026 ACSM position stand')} links more muscle growth with 10 or more sets per muscle per week, and a {cite('vol2017', 'dose-response meta-analysis')} found growth kept rising as sets increased. If you are new to lifting or your shoulders feel beaten up, start nearer 10 sets (2 per exercise) and add sets as you recover well. Our guide to {L('/how-many-sets-per-muscle-group-per-week/', 'sets per muscle group per week')} explains how to adjust.</p>
"""),
        ("split", "How to Fit These Chest Workouts Into Your Split", f"""
<ul>
<li><strong>Push pull legs:</strong> use Workout A on your first push day and Workout B on the second. See our {L('/workout-plans/push-pull-legs/', 'push pull legs workout plan')}.</li>
<li><strong>Upper/lower:</strong> do the first two exercises of each workout on your upper days.</li>
<li><strong>Bro split:</strong> run Workout A on chest day and add 4–6 sets from Workout B on shoulder or arm day so the chest gets a second weekly session.</li>
</ul>
<p>Whatever split you run, keep 2–3 days between the two chest sessions.</p>
"""),
        ("mistakes", "Chest Workout Mistakes", f"""
<ul>
<li><strong>Bouncing the bar.</strong> Touch the chest under control; the bounce takes work away from the muscle you are training. Our {L('/how-to-bench-press/', 'bench press guide')} covers the setup.</li>
<li><strong>Inclines that are too steep.</strong> Above 45° the front delts take over. Keep the bench at about 30°.</li>
<li><strong>Half reps on flyes and presses.</strong> Lower until you feel a stretch across the chest, then press.</li>
<li><strong>Grinding every set to failure.</strong> Training to failure built no more muscle than stopping short in a {cite('failure2023', '2023 meta-analysis')}, and it adds fatigue, so save failure for the last set of flyes or push-ups.</li>
</ul>
"""),
    ],
    "schedule": [("Mon", "Chest A", "c1"), ("Tue", "Other muscles", "rest"), ("Wed", "Other muscles", "rest"), ("Thu", "Chest B", "c2"), ("Fri", "Other muscles", "rest"), ("Sat", "Other / rest", "rest"), ("Sun", "Rest", "rest")],
    "days": [
        {"tab": "Gym A", "tab_sub": "Flat press focus", "title": "Chest Workout A: Flat Press Focus", "tag": "Gym", "color": 1, "time": "40–50 min", "focus": "Chest / Triceps / Front delts",
         "exercises": [
             ("Barbell Bench Press", "Primary: middle and lower chest · Secondary: front delts, triceps", "4 × 6–8", "2–3 min", "RIR 1–2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest · Secondary: front delts", "3 × 8–10", "2 min", "RIR 1–2"),
             ("Cable Fly", "Primary: whole chest", "3 × 12–15", "60–90 sec", "RIR 1"),
         ],
         "notes": "Do 2–3 warm-up sets on the bench press before your working sets. Pause each cable fly for a second at the stretch."},
        {"tab": "Gym B", "tab_sub": "Upper chest focus", "title": "Chest Workout B: Upper Chest Focus", "tag": "Gym", "color": 2, "time": "40–50 min", "focus": "Upper chest / Triceps",
         "exercises": [
             ("Incline Barbell Bench Press", "Primary: upper chest · Secondary: front delts, triceps", "3 × 6–10", "2–3 min", "RIR 1–2"),
             ("Dumbbell Bench Press", "Primary: middle chest · Secondary: triceps", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Low-to-High Cable Fly", "Primary: upper chest", "2 × 12–15", "60–90 sec", "RIR 1"),
             ("Dip (or Assisted Dip)", "Primary: lower chest · Secondary: triceps", "2 × 8–12", "2 min", "RIR 1–2"),
         ],
         "notes": "Set the incline bench to about 30°. Lean forward on dips to bias the chest; skip them if they bother your shoulders and do a machine chest press instead."},
        {"tab": "Dumbbells", "tab_sub": "Bench + dumbbells", "title": "Chest Workout: Dumbbells Only", "tag": "Home gym", "color": 4, "time": "35–45 min", "focus": "Chest / Triceps",
         "exercises": [
             ("Dumbbell Bench Press", "Primary: middle chest · Secondary: triceps, front delts", "4 × 8–12", "2 min", "RIR 1–2"),
             ("Incline Dumbbell Press (30°)", "Primary: upper chest", "3 × 8–12", "2 min", "RIR 1–2"),
             ("Dumbbell Fly", "Primary: whole chest", "3 × 10–15", "90 sec", "RIR 1"),
             ("Push-Up", "Primary: chest · Secondary: triceps", "2 × as many as possible", "90 sec", "RIR 1"),
         ],
         "notes": "Do this workout twice a week. With no bench, use the floor press for presses and a floor fly with a short range."},
        {"tab": "No equipment", "tab_sub": "Push-ups only", "title": "Chest Workout: No Equipment", "tag": "Home", "color": 6, "time": "30–40 min", "focus": "Chest / Triceps",
         "exercises": [
             ("Push-Up", "Primary: chest · Secondary: triceps, front delts", "4 × 8–20", "90 sec", "RIR 1–2"),
             ("Feet-Elevated Push-Up", "Primary: upper chest · Secondary: front delts", "3 × 6–15", "90 sec", "RIR 1–2"),
             ("Slow-Lowering Push-Up (3 sec down)", "Primary: chest", "3 × 6–10", "90 sec", "RIR 1"),
             ("Incline Push-Up (hands on a bench)", "Primary: lower chest · Secondary: triceps", "2 × 12–20", "60 sec", "RIR 1"),
         ],
         "notes": f"Too easy? Wear a backpack with books. Too hard? Do every set with hands on a bench. Push-ups built similar chest muscle to a bench press of the same load in a {cite('kikuchi2017', '2017 training study')}."},
    ],
    "faq_title": "Chest Workout FAQ",
    "faqs": [
        ("Do I need the bench press to build my chest?", "No. Dumbbell presses, machine presses and loaded push-ups all build the chest. The barbell bench press is simply the easiest to load heavy and track over time."),
        ("How long until I see chest growth?", "Training studies measure chest growth after about 8 weeks. Strength usually rises sooner, and visible change depends on your starting point and diet."),
        ("Should I train chest and triceps together?", "Yes, it works well. Your triceps already help on every press, so finishing a chest workout with 2–3 sets of triceps work is time-efficient."),
        ("Can women follow this chest workout?", "Yes. The exercises and sets are the same; many women start with dumbbells or the no-equipment version and progress from there."),
        ("Why do my shoulders take over on presses?", "Usually the bench is too steep or the shoulder blades aren't pulled back. Keep inclines around 30°, set your shoulder blades back and down, and lower the bar to mid-chest."),
    ],
    "related": ["arm-workout", "push-pull-legs", "bro-split", "upper-lower-split"],
    "refs": refs("ridao2020", "chaves2020", "acsm2026", "vol2017", "kikuchi2017", "failure2023"),
    "disclaimer": DISCLAIMER,
}
