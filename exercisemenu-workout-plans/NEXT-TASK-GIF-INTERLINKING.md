# Next Task: Fix all workout plan pages + interlink exercise GIF pages

Paste this whole file as the first message of a new Claude Code session (repo `zubairahmadseo-glitch/brightlyfuture`, branch `claude/quirky-hawking-mxnkp4`).

---

Read `exercisemenu-workout-plans/HANDOFF.md`, `BRIEF.md` and `SOURCES.md` first, and load the `exercisemenu-content` skill. Reply to me in Roman Urdu. Do NOT start any new workout plan until this task is finished.

## Goal
All 21 workout plan pages built in `exercisemenu-workout-plans/batch1/` (the 20 live under `https://exercisemenu.com/workout-plans/` + #35 resistance-band-workout) must:
1. Use exercise names that match the exercise GIFs/pages exactly (same exercise, same equipment, same setup).
2. Link every exercise that has a live `/exercises/<slug>/` page.
3. Have the matching entry on each exercise page's plugin section **"Workout Plans With the [Exercise]"** (`<section id="em-plans">`, entries `<a class="em-plan" href="..."><span class="em-day">TAB NAME</span><b>PLAN PAGE TITLE</b></a>`).

## Context
- I am buying 15 new GIFs from Gym Visual (list: `batch2/GymVisual-15-GIFs-to-buy.xlsx`): Seated Cable Row, Lat Pulldown, Triceps Rope Pushdown, Face Pull, Seated Leg Curl, Leg Press, Weighted Dip, Pull-Up, Leg Extension, Low-to-High Cable Fly, Overhead Cable Triceps Extension, Reverse Pec Deck, Hanging Leg Raise, Plank, Cable Crunch. Also already in hand: Barbell Seated Calf Raise and Dumbbell Lateral Raise.
- My developer creates the exercise pages (post type `exercise`) with the GIFs. I will tell you which pages are live.
- Near-identical exercises may share one GIF/page (user approved), e.g. Close-Grip Seated Cable Row → Seated Cable Row page; Wide-Grip Lat Pulldown → Lat Pulldown page; Hanging Knee Raise → Hanging Leg Raise page (with a note to bend the knees).

## Steps
1. **Inventory (verify, don't assume):**
   - GIFs in the media library: `curl -s "https://exercisemenu.com/wp-json/wp/v2/media?mime_type=image/gif&per_page=100&_fields=id,source_url"`.
   - Live exercise pages: fetch `https://exercisemenu.com/exercise-sitemap.xml` (or open `/exercises/<slug>/` and check for HTTP 200). Also refresh `post-sitemap.xml` and `page-sitemap.xml` into a live-paths file for `lint.py`.
   - All exercises used in the 21 plans: from `batch1/content/*.py` (`days` → `exercises`).
2. **Mapping sheet:** For every plan exercise, record: plan, tab, exercise name, matching GIF (exact / near-same / none), live exercise page URL (if any). Look at each GIF frame if the match is unclear. Give me this sheet (xlsx) and a short list of exercises that still have no GIF.
3. **Rename where the GIF differs** (keep the training intent; update notes if needed). Already agreed:
   | Plan | Now | Change to |
   |---|---|---|
   | PPL | Incline Dumbbell Hammer Curl | Hammer Curl |
   | PPL | Triceps Pushdown | Triceps Rope Pushdown |
   | PPL | Seated Calf Raise | Seated Calf Raise (machine or barbell) + note: put a plate or step under the balls of your feet |
   | PPL | Bulgarian Split Squat | Bulgarian Split Squat (barbell or dumbbells) |
   | PPL + Full Body | Dumbbell Walking Lunge | Dumbbell Lunge (walking or in place) |
   | Full Body | Hanging Knee Raise | keep name; note: bend your knees (GIF shows the straight-leg version) |
   | Full Body | Dumbbell Romanian Deadlift | keep (already links to the /dumbbell-romanian-deadlift/ guide) |
   **Also fix the swaps that would clash after renaming (PPL):** Day 4 "Triceps Pushdown" → "Triceps Rope Pushdown", so its swap must change from "Triceps Rope Pushdown" to "Triceps Pushdown (straight bar)". Day 5 "Incline Dumbbell Hammer Curl" → "Hammer Curl", so its swap must change from "Hammer Curl" to "Rope Cable Hammer Curl". After every rename, check that no exercise has itself as its swap.
   GIF names on Gym Visual differ from site names (e.g. "Lever Seated Reverse Fly" = Reverse Pec Deck, "Sled 45 Leg Press" = Leg Press, "Cable Low Fly" = Low-to-High Cable Fly, "Cable Kneeling Crunch" = Cable Crunch, "Cable Wide Grip Lat Pulldown (female)" = Lat Pulldown + Wide-Grip Lat Pulldown). Match by exercise, not by name.
   Dumbbell Lateral Raise and Barbell Seated Calf Raise GIFs are with the user and will be uploaded too.
   Check the other 19 plans the same way and propose renames before applying them. Every rename must keep the plan accurate (sets/reps, muscles, swaps, volume counts, exercise-count stat). Re-check `batch1/swaps.py` and page `swap_overrides` after renames.
4. **Links:** add each live exercise page to `EXERCISE_LINKS` in `batch1/build.py` (name match is exact name or `name + " ("` prefix) and to `allowed_extra` in `lint.py`. Never link to a page that is not live.
5. **Build + check:** `python3 build.py`, `python3 lint.py <live_paths.txt>`, `python3 audit.py`; check every internal link returns 200; screenshot one tab per changed page.
6. **Developer file:** update `batch2/DEVELOPER-EXERCISE-PLUGIN-UPDATES.md` with every "Workout Plans With the …" entry for all live exercise pages across all 21 plans (em-day = tab name, `<b>` = plan page title, link `/workout-plans/<slug>/`). Keep existing entries.
7. **Deliver:** zip of only the changed plan pages (`python3 make_zip.py <dir> <zip_name> slug1,slug2,...`), the mapping xlsx and the developer file. Commit and push. Update `HANDOFF.md`.

## Rules (never break)
- Plan pages stay plan-first; do not change the page structure or add article sections.
- No false information: if a rename changes how the exercise is done, update the cue/notes and check it against `SOURCES.md`.
- Never store passwords or secrets in the repo.
