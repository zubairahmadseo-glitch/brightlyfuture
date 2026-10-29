# ExerciseMenu — Full Session Handoff (read this first, then BRIEF.md)

New session: read this file completely before doing anything. It summarises everything agreed with the user so far. Do NOT ask the user to re-explain anything below. Reply to the user in **Roman Urdu**. Also load the `exercisemenu-content` skill.

Repo: `zubairahmadseo-glitch/brightlyfuture`, branch **`claude/quirky-hawking-mxnkp4`** (all work is here; folder `exercisemenu-workout-plans/`).
Site: **exercisemenu.com** (WordPress, SmartMag theme, Rank Math, Wordfence, Hostinger/LiteSpeed). Owner/author: **Sadia Baloch**.

---

## 1. What has been done

### Workout plans #1–#15 — finished
All 15 pages are built in `batch1/` and packaged as a paste-ready zip. The user pastes them into WordPress manually (WordPress REST connection never worked — see section 6).

| # | Plan | Slug (under /workout-plans/) | Focus keyword |
|---|---|---|---|
| 1 | Push Pull Legs (6-Day) | push-pull-legs | push pull legs workout plan |
| 2 | Full Body for Beginners (3-Day) | full-body-workout-plan | gym workout plan |
| 3 | 4-Day Upper Lower Split | upper-lower-split | upper lower split |
| 4 | 5×5 Strength & Muscle | 5x5-workout | 5x5 workout |
| 5 | Bro Split 5-Day | bro-split | bro split workout plan |
| 6 | 4-Day Workout Split (Torso/Limbs) | 4-day-workout-split | 4 day workout split |
| 7 | 3-Day Full Body (Intermediate, Heavy/Light/Medium) | 3-day-full-body-workout | 3 day full body workout |
| 8 | Lean Bulk (12-Week) | lean-bulk-workout-plan | lean bulk workout plan |
| 9 | Hypertrophy Program (4-Day, anterior/posterior, 6-week block) | hypertrophy-program | hypertrophy program |
| 10 | Skinny Guys / Hardgainers | workout-plan-for-skinny-guys | workout plan for skinny guys |
| 11 | 5-Day Split (Upper/Lower + PPL) | 5-day-workout-split | 5 day workout split |
| 12 | 6-Day PPL Hypertrophy (Advanced) | ppl-hypertrophy-program | ppl hypertrophy program |
| 13 | Beginner Strength Program (12-week linear progression) | beginner-strength-training-program | beginner workout plan |
| 14 | Strength Training for Women | strength-training-for-women | strength training for women |
| 15 | Powerlifting for Beginners (12 weeks + test day) | powerlifting-program-for-beginners | powerlifting program for beginners |

Plans #1–#4 were originally written by the user (two HTML files + two .docx). They were rebuilt in the same template and fixed: false "reviewed by dietitian/coaches" box (later the user confirmed reviewers are real — see section 3), fake "download PDF/tracker" offers removed, misquoted studies fixed (Pelland, Ralston, ACSM, Seynnes, Reg Park), 5×5 progression maths corrected (session-by-session table), deadlift bar-height claim fixed, Upper/Lower chest only trained once → incline press added to Upper B, Full Body hamstrings got a leg curl + dumbbell RDL, lying leg curl → seated (Maeo 2021).

### Meta titles/descriptions (latest, CTR-optimised, in each `batch1/content/*.py`)
Rewritten for all 15 on 29 Oct 2026: focus keyword first, numbers (days/weeks), "Free" (plans are free), question hook in description, every promise matches page content. Titles 48–57 chars, descriptions 140–152 chars. "4 Day / 3 Day / 5 Day" written without hyphen so Rank Math matches the focus keyword exactly.

### YMYL-safe roadmap sheet
`ExerciseMenu_Workout_Plans_YMYL_Safe_Roadmap.xlsx` (from the original 100-plan `roadmap.html`):
- **86 plans kept** (15 written, 71 "To write"; P1 15, P2 29, P3 27) — tab "Remaining Plans" with keyword, volume, KD, priority, suggested slug, internal links, status, YMYL notes.
- **14 removed** (tab "Removed (YMYL Risk)") — never write these: #19 Over 40, #23 12-Week Fat Loss, #24 Gym Plan for Weight Loss, #25 Fat Burning at Home, #26 Strength for Fat Loss, #28 Walking for Weight Loss, #29 Body Recomposition, #30 Low Impact Weight Loss, #32 30-Day Weight Loss Challenge, #58 Knee-Friendly Legs, #61 Six Pack in 6 Weeks, #66 Lower Back Friendly Core, #90 Seniors/Over 50, #91 Teenagers.
- Kept but needs care: #27 Metabolic Conditioning and #31 Cardio+Strength (fitness angle only, no weight-loss promises); HIIT/sprint plans need a medical-clearance line; follow the "YMYL Notes" column.
- Cannibalisation warning: #85 "beginner gym workout" and #77 "full body workout" overlap with #2 — give them clearly different angles.

---

## 2. User preferences (very important)
- **Zero mistakes / YMYL accuracy.** Every sets/reps/rest/nutrition claim must be backed by a source you actually read (PubMed abstract, ACSM, NSCA). Cite with working links. Never invent studies, numbers, downloads, tools, reviewers or credentials. Recheck every page after writing.
- **Pages must not be long or boring.** Users come for the plan: Quick Answer → schedule → workouts (day tabs) → everything else. No padding, no repeated info, every H2 answers one question directly, FAQs must add NEW info (not repeat the body).
- **No Key Takeaways box** (removed — it repeated the body).
- **No AI voice**: avoid "the catch", "sweet spot", "the takeaway", "not only…", triplets, "It's worth noting", and the banned list in the `exercisemenu-content` skill.
- Nutrition: full section only where the intent needs it (lean bulk, skinny guys); elsewhere 2–3 lines (protein 1.6 g/kg + protein calculator link).
- Internal links only to URLs live in the sitemap; exercise names link only to live `/exercises/` pages (6 live on 28 Oct 2026: barbell-bench-press, barbell-incline-bench-press, dumbbell-bench-press, barbell-curl, dumbbell-biceps-curl, dumbbell-hammer-curl).
- Related workout plan cards (4 per page) must be relevant and accurate.
- Deliver work as a **zip** (paste-ready). The user prefers concise, clear answers.

---

## 3. Fixed page elements (keep on every plan page)
- **Hero credit line** (between hero description and the days/minutes meta):
  `✓ Training reviewed by FISAF-certified coaches · Nutrition reviewed by [Rimsha Shahid](https://exercisemenu.com/rimsha-shahid/), certified dietitian`
  Rimsha's profile: "Certified Dietitian | Clinical Nutritionist", MS Human Nutrition & Dietetics, DDNS, Certified Diabetes Specialist (USA). **Never write "registered dietitian".**
- **"See the workouts ↓" button** in the hero + **"Jump to:" chip menu** under the intro.
- **Author box after the FAQ** (Sadia Baloch, FISAF-certified fitness trainer): "Sadia Baloch is a FISAF-certified fitness trainer who has personally coached hundreds of clients over the past 7 years. She specializes in strength training, fat loss, and workout programming for beginners through intermediate lifters. Every article on ExerciseMenu.com is based on the same methods she uses with her in-person clients daily." (No "BookWorkouts" AdSense anchors.)
- **Day tabs are pure CSS** (radio inputs, "All days" tab) so WordPress keeps them; no JavaScript.
- One shared CSS block (scoped to `.emp`), each section its own Custom HTML block, FAQPage JSON-LD at the end. Theme prints the H1, so content starts at H2.
- Rank Math: meta title ≤60, description ≤155, focus keyword in both.

---

## 4. Mandatory workflow for every NEW plan (user instruction)
1. **Top 7 competitors** for the target keyword (WebSearch + fetch each page): outline, workout structure, FAQs, sources, word count, weaknesses.
2. From all 7: **short-tail, mid-tail and long-tail keywords** and **entities** (tag 3+ competitors = must include, 2 = differentiator).
3. **Own keyword research**: Google/Bing/DuckDuckGo autocomplete (work from the container — URLs in BRIEF.md) with modifiers, plus People Also Ask. No search-volume tool exists — say volumes are not verified; the user checks them.
4. Gap analysis → outline → show research to the user.
5. Then write in the batch 1 system, verify, build, lint, audit, link-check, zip.

---

## 5. How the build system works (`exercisemenu-workout-plans/batch1/`)
- `content/<plan>.py` — page data (hero, stats, quick answer, sections, days/exercises, FAQs, related plans, refs). `content/refs.py` — verified PubMed sources (36+). `content/common.py` — helpers.
- `build.py` — renders WordPress block HTML (`out/`) + browser previews (`preview/`); holds `PAGES`, `PLANS` (related cards), `CHIPS`, `AUTHOR_BOX`, hero credit line. `shared.css` — styles.
- `lint.py <live_paths>` — meta lengths, quick-answer limits, banned phrases, exercise-count stats, unrendered template code, uncited refs, `#workouts` present, internal links vs sitemap.
- `audit.py` — session-time estimates vs stated times, FAQ/body overlap, AI-phrase scan.
- `make_zip.py <dir>` + `PROCESS-GUIDE.txt` — builds `ExerciseMenu-Workout-Plans-All-15.zip` (per page: `1-PASTE-IN-WORDPRESS.txt`, `2-SEO-SETTINGS.txt`, `3-PREVIEW-open-in-browser.html`, plus `00-PROCESS-GUIDE.txt` in Roman Urdu).
- `publish.py test|drafts` — WordPress REST: test connection; save all pages as DRAFTS (never publish), parent page "Workout Plans", Rank Math meta.
- Live sitemap paths: rebuild from `https://exercisemenu.com/post-sitemap.xml` and `page-sitemap.xml` each session.

Manual paste process (also in the zip guide): Pages → Add New → title → ⋮ → Code editor → paste `1-PASTE-IN-WORDPRESS.txt` → Exit code editor → slug + Parent "Workout Plans" → Rank Math fields → Save draft → Preview. Needs an Administrator/Editor with unfiltered HTML; use Gutenberg, not Elementor.

---

## 6. WordPress connection status (not working yet)
- REST API via the environment **Network secret** (host exercisemenu.com, path /wp-json/) still returns `401 rest_not_logged_in`.
- Done so far: user created a new Application Password and updated the secret; `.htaccess` fix added at the top of `public_html/.htaccess`:
  `SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1` and `RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]`. Application passwords are enabled on the site (REST index shows them).
- Still to check: the secret value must be exactly `Basic ` + base64(`username:application password`); secrets often load only in a NEW session — so **first thing in a new session: run `python3 batch1/publish.py test`**.
- Fallback the user can choose: create a WordPress user **`claude-editor` with Editor role** and share its username/password; `/wp-login.php` is reachable from the cloud container, so cookie login + REST nonce works. Ask the user to delete that user afterwards. Never store any password in the repo.

---

## 7. Next steps
1. Test the WordPress connection (section 6). If it works, save all 15 pages as drafts with Rank Math meta and parent "Workout Plans" (create the parent as a draft if missing). Never publish.
2. When the user names the next plan(s), pick from the YMYL-safe sheet (Status "To write") and follow the workflow in section 4.
