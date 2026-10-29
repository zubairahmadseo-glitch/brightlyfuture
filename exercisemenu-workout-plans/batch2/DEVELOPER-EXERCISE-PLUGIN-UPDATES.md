# Developer Task: Exercise Plugin Updates for 5 New Workout Plans

**When:** only after these 5 pages are published under `/workout-plans/`. Before that, the links below return 404.

**Where:** on each exercise page (post type `exercise`), find the section
**"Workout Plans With the [Exercise Name]"** (`<section id="em-plans" class="em-card em-sec">`).
Keep the entry that is already there (Push Pull Legs Split) and add the new entries below it.

Each entry uses the plugin's existing markup:

```html
<a class="em-plan" href="https://exercisemenu.com/workout-plans/chest-workout/">
  <span class="em-day">Gym A</span>
  <b>Chest Workout: Best Chest Exercises and a 4-Week Plan</b>
</a>
```

`em-day` = the name of the day tab on the plan page. `<b>` = the plan's page title.

---

## 1. Entries to add (8 live exercise pages)

| Exercise page | `em-day` | `<b>` plan title | Link |
|---|---|---|---|
| [Barbell Bench Press](https://exercisemenu.com/exercises/barbell-bench-press/) | Gym A | Chest Workout: Best Chest Exercises and a 4-Week Plan | /workout-plans/chest-workout/ |
| [Barbell Incline Bench Press](https://exercisemenu.com/exercises/barbell-incline-bench-press/) | Gym B | Chest Workout: Best Chest Exercises and a 4-Week Plan | /workout-plans/chest-workout/ |
| [Dumbbell Bench Press](https://exercisemenu.com/exercises/dumbbell-bench-press/) | Gym B · Dumbbells | Chest Workout: Best Chest Exercises and a 4-Week Plan | /workout-plans/chest-workout/ |
| [Barbell Curl](https://exercisemenu.com/exercises/barbell-curl/) | Gym A | Arm Workout: Biceps and Triceps Plan for Gym or Home | /workout-plans/arm-workout/ |
| [Dumbbell Biceps Curl](https://exercisemenu.com/exercises/dumbbell-biceps-curl/) | Gym B · Dumbbells | Arm Workout: Biceps and Triceps Plan for Gym or Home | /workout-plans/arm-workout/ |
| [Dumbbell Hammer Curl](https://exercisemenu.com/exercises/dumbbell-hammer-curl/) | Gym A · Dumbbells | Arm Workout: Biceps and Triceps Plan for Gym or Home | /workout-plans/arm-workout/ |
| [Barbell Lying Triceps Extension](https://exercisemenu.com/exercises/barbell-lying-triceps-extension/) | Gym B | Arm Workout: Biceps and Triceps Plan for Gym or Home | /workout-plans/arm-workout/ |
| [Barbell Standing Calf Raise](https://exercisemenu.com/exercises/barbell-standing-calf-raise/) | Quad focus | Leg Day Workout: Complete Plans for Quads, Hamstrings and Calves | /workout-plans/leg-day-workout/ |

(Full link = `https://exercisemenu.com` + the path in the Link column.)

## 2. For exercise pages that don't exist yet (GIF is already in the media library)

Add these entries when the exercise page is created:

| Future exercise page | `em-day` | `<b>` plan title | Link |
|---|---|---|---|
| Back Squat | Day B | Glute Workout: 2-Day Plan to Build Your Glutes | /workout-plans/glute-workout/ |
| Back Squat | Quad focus | Leg Day Workout: Complete Plans for Quads, Hamstrings and Calves | /workout-plans/leg-day-workout/ |

Once the Back Squat page is live, tell the content team so the exercise names on the Glute and Leg Day pages can link to it.

## 3. No change needed
- The plan pages already link the 8 exercise names above to their exercise pages.
- Medicine Ball Russian Twist: the Core page links to the article `/medicine-ball-ab-exercises/`, which already shows this exercise. No plugin entry is needed.
- No other exercise in these 5 plans has an exercise page yet.
