# ExerciseMenu Workout Plans — Handoff Brief (read this first)

New session: read this file, `roadmap.html`, and `sample-ppl-page.html` in this folder. Do NOT ask the user to re-explain.
Also load the `exercisemenu-content` skill. Reply to the user in Roman Urdu.

## Task
Write Batch 1 workout plan pages #5–#15 (11 pages) for exercisemenu.com and save each as a **WordPress DRAFT** (never publish).
Plans #1–#4 are already written by the user (not live yet): PPL 6-Day, Full Body Beginners 3-Day, 4-Day Upper Lower, 5×5.

| # | Plan | Slug (under /workout-plans/) | Target keyword |
|---|---|---|---|
| 1 | Push Pull Legs (6-Day PPL) — DONE by user | push-pull-legs | push pull legs workout plan |
| 2 | Full Body for Beginners (3-Day) — DONE | full-body-workout-plan | gym workout plan |
| 3 | 4-Day Upper Lower Split — DONE | upper-lower-split | upper lower split |
| 4 | 5×5 Strength & Muscle — DONE | 5x5-workout | 5x5 workout |
| 5 | Bro Split 5-Day | bro-split | bro split workout plan |
| 6 | 4-Day Workout Split | 4-day-workout-split | 4 day workout split |
| 7 | 3-Day Full Body (Intermediate) | 3-day-full-body-workout | 3 day full body workout |
| 8 | Lean Bulk (12-Week) | lean-bulk-workout-plan | lean bulk workout plan |
| 9 | Hypertrophy Program (4-Day) | hypertrophy-program | hypertrophy program |
| 10 | Skinny Guys / Hardgainers | workout-plan-for-skinny-guys | workout plan for skinny guys |
| 11 | 5-Day Workout Split (Gym) | 5-day-workout-split | 5 day workout split |
| 12 | 6-Day PPL Hypertrophy (Advanced) | ppl-hypertrophy-program | ppl hypertrophy program |
| 13 | Beginner Strength Program (3-Day) | beginner-strength-training-program | beginner workout plan |
| 14 | Strength Training for Women | strength-training-for-women | strength training for women |
| 15 | Powerlifting for Beginners | powerlifting-program-for-beginners | powerlifting program for beginners |

Avoid overlap between #2/#7/#13, #1/#12, #6/#9, #5/#11 — each must have a distinct angle.

## User requirements
- YMYL: content must be 100% accurate. Verify every sets/reps/rest/nutrition claim against NSCA/ACSM/PubMed; cite with working links. Recheck every page after writing.
- Follow the structure + design of `sample-ppl-page.html` (improve where better for users).
- Add a **Day 1 / Day 2 / Day 3 tab filter** for the workouts (inspired by loadmuscle.com/workout-routines/weight-loss/beginner-weight-loss-workout-plan) — must work inside a WordPress Custom HTML block.
- Bottom: related workout plan **cards** with internal links (slugs above; #1–#4 included).
- Link exercise names to exercise pages ONLY if live (format: https://exercisemenu.com/exercises/dumbbell-biceps-curl/). Check sitemap first; never link non-live URLs.
- Internal links to live guides (reps & sets, progressive overload, how-to-structure, etc. — verify via sitemap).
- **NO author byline** (user said no "FISAF-certified coach Sadia Baloch" byline).
- Easy to edit later in WordPress: one shared CSS block, clean sections.
- Rank Math: meta title ≤60 chars, meta description ≤155 chars, focus keyword.
- Parent page `/workout-plans/` (hub) will be built later by the user; create an empty DRAFT parent "Workout Plans" (slug workout-plans) if it does not exist.
- User may paste Q&A from another Claude chat for cross-checking — use it to recheck.

## WordPress connection
- Auth via Claude **Network secret**: host `exercisemenu.com`, path `/wp-json/`, header `Authorization: Basic <base64>` injected automatically. Just call `https://exercisemenu.com/wp-json/wp/v2/...` with no auth header.
- Wordfence: application passwords enabled. WPCode snippet "Rank Math REST meta" registers `rank_math_title`, `rank_math_description`, `rank_math_focus_keyword` for pages with show_in_rest.
- First step: test (GET /wp-json/wp/v2/users/me?context=edit, then create + verify a test draft with Rank Math meta, then delete it).

## Approved Rank Math meta (use exactly; page content MUST deliver every promise in the description)

| # | Meta title | Meta description |
|---|---|---|
| 1 | Push Pull Legs Workout Plan: 6-Day PPL Split (Free) | Free 6-day push pull legs workout plan with strength and hypertrophy days, sets, reps, rest times and a simple progression system to build muscle. |
| 2 | Full Body Workout Plan for Beginners: 3 Days a Week | A simple 3-day full body gym plan for beginners. Exact exercises, sets, reps and rest, plus how to add weight safely each week. Free to follow. |
| 3 | Upper Lower Split: 4-Day Workout Plan for Muscle | Train each muscle twice a week with this 4-day upper lower split. Full workouts with sets, reps and rest, progression rules and exercise swaps. |
| 4 | 5x5 Workout: Simple Strength and Muscle Program | Get stronger with a proven 5x5 workout. Two alternating sessions, 3 days a week, starting weights, how to add weight and what to do when you stall. |
| 5 | Bro Split Workout Plan: 5-Day Body Part Routine | One muscle group per day, five days a week. Full bro split routine with sets, reps and rest, plus how to make it work for natural lifters. |
| 6 | 4 Day Workout Split: Best Options for Muscle Growth | Compare the best 4 day workout splits and follow a complete plan with sets, reps and rest. Pick the right split for your schedule and goals. |
| 7 | 3 Day Full Body Workout for Intermediate Lifters | Past the beginner stage? This 3 day full body workout uses heavy, medium and light days to keep you progressing. Full sets, reps and rest. |
| 8 | Lean Bulk Workout Plan: 12-Week Program to Gain Muscle | Build muscle with minimal fat gain. 12-week lean bulk workout plan with training splits, calorie surplus guidance and weekly progress checks. |
| 9 | Hypertrophy Program: 4-Day Plan to Build Muscle | Evidence-based 4-day hypertrophy program with weekly set targets, rep ranges, rest times and progression to grow muscle steadily. |
| 10 | Workout Plan for Skinny Guys: Gain Muscle and Size | Struggle to gain weight? This workout plan for skinny guys pairs heavy compound lifts with simple eating targets to add muscle week by week. |
| 11 | 5 Day Workout Split: Complete Gym Plan for Muscle | Train five days a week with a balanced 5 day workout split. Daily workouts with sets, reps and rest, plus how to recover between sessions. |
| 12 | PPL Hypertrophy Program: Advanced 6-Day Split | Advanced 6-day PPL hypertrophy program with higher volume, intensity techniques and a planned deload. For lifters with 1+ year of training. |
| 13 | Beginner Workout Plan: 3-Day Strength Program | New to lifting? This 3-day beginner workout plan teaches the main lifts, sets your starting weights and shows you how to get stronger each week. |
| 14 | Strength Training for Women: 3-Day Beginner Plan | A practical strength training plan for women. 3 days a week, clear exercise instructions, sets and reps, and how to progress with confidence. |
| 15 | Powerlifting Program for Beginners: 12-Week Plan | Build your squat, bench and deadlift with a 12-week powerlifting program for beginners. Percentages, weekly progression and meet-day tips. |
