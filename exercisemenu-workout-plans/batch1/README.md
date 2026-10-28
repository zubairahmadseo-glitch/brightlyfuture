# Batch 1 — Workout plan pages #5–#15

Status (2026-10-28): all 11 pages built, checked and ready. **Not yet saved to WordPress** — the proxy rejects the
`exercisemenu.com/wp-json/` network secret (`X-Proxy-Error: upstream auth failed`). Once the secret is fixed, run:

```
python3 publish.py test      # users/me, test draft + Rank Math meta round-trip, delete
python3 publish.py drafts    # parent "Workout Plans" draft + 11 DRAFT pages (never publishes)
```

## Files
- `content/*.py` — page text and workouts (edit here, then `python3 build.py`)
- `content/refs.py` — verified PubMed sources (each PMID checked against its abstract)
- `shared.css` — the one shared style block (scoped to `.emp`, no theme bleed)
- `out/<slug>.html` — WordPress block content (Custom HTML blocks: CSS, intro, one block per section, FAQ, related + refs, FAQ schema)
- `preview/<slug>.html` — open in a browser to preview
- `lint.py` — meta lengths, quick-answer limits, banned phrases, internal links vs sitemap

## Notes
- Day tabs are pure CSS (radio inputs), no JavaScript, so WordPress cannot strip them; an "All days" tab shows every workout and print shows all.
- No author byline. Theme (SmartMag) prints the H1, so content starts at H2.
- Exercise links only to the 6 live `/exercises/` pages (bench press, incline bench, dumbbell bench, barbell curl, dumbbell curl, hammer curl) plus the live dumbbell RDL and trap bar deadlift guides.
- `/how-sleep-affects-muscle-growth-and-recovery/` is listed in the skill but is NOT in the sitemap, so it is not linked.
- All 32 external (PubMed) and all non-plan internal links returned HTTP 200 on 2026-10-28.

| # | Slug | Meta title (chars) | Desc chars | Focus keyword | Day tabs | Internal links | Sources | FAQs |
|---|---|---|---|---|---|---|---|---|
| 5 | `bro-split` | Bro Split Workout Plan: 5-Day Routine With Sets & Reps (54) | 153 | bro split workout plan | 5 | 11 | 14 | 6 |
| 6 | `4-day-workout-split` | 4-Day Workout Split: Torso/Limbs Plan With Sets & Reps (54) | 153 | 4 day workout split | 4 | 9 | 10 | 6 |
| 7 | `3-day-full-body-workout` | 3-Day Full Body Workout: Intermediate Heavy/Light/Medium (56) | 151 | 3 day full body workout | 3 | 11 | 8 | 5 |
| 8 | `lean-bulk-workout-plan` | Lean Bulk Workout Plan: 12-Week Training & Calorie Guide (56) | 150 | lean bulk workout plan | 4 | 11 | 10 | 6 |
| 9 | `hypertrophy-program` | 4-Day Hypertrophy Program: 6-Week Muscle Building Plan (54) | 150 | hypertrophy program | 4 | 8 | 14 | 6 |
| 10 | `workout-plan-for-skinny-guys` | Workout Plan for Skinny Guys: 3-Day Hardgainer Program (54) | 152 | workout plan for skinny guys | 3 | 11 | 7 | 6 |
| 11 | `5-day-workout-split` | 5-Day Workout Split: Upper/Lower + PPL Gym Program (50) | 152 | 5 day workout split | 5 | 9 | 10 | 5 |
| 12 | `ppl-hypertrophy-program` | 6-Day PPL Hypertrophy Program (Advanced Lifters) (48) | 150 | ppl hypertrophy program | 6 | 10 | 7 | 6 |
| 13 | `beginner-strength-training-program` | Beginner Workout Plan: 12-Week Strength Program (3 Days) (56) | 151 | beginner workout plan | 3 | 15 | 7 | 6 |
| 14 | `strength-training-for-women` | Strength Training for Women: 3-Day Gym Workout Plan (51) | 152 | strength training for women | 3 | 10 | 7 | 6 |
| 15 | `powerlifting-program-for-beginners` | Powerlifting Program for Beginners: 12-Week Plan (48) | 151 | powerlifting program for beginners | 3 | 11 | 9 | 6 |
