# ExerciseMenu Workout Plans — Handoff Brief (read this first)

New session: read `HANDOFF.md` (full session summary) and this whole file before doing anything. Do NOT ask the user to re-explain.
Also load the `exercisemenu-content` skill. Reply to the user in Roman Urdu.

**MANDATORY: read `SOURCES.md` before writing any workout plan or exercise page.** Every recommendation (sets/reps, rest, progression, muscles, form/cues, mistakes, nutrition, supplements) must be verified against the sources listed there, then written in our own coach voice. Experience shapes how we explain, never what is true; never invent stories, results or studies.

## Current status (updated 28 Oct 2026)
- **Plans #1–#15 are finished** and live in `batch1/` (content, builder, zip packaging). The user pastes pages into WordPress manually from the zip (`batch1/make_zip.py`); the REST connection failed (proxy rejected the network secret).
- **Next plans come from `ExerciseMenu_Workout_Plans_YMYL_Safe_Roadmap.xlsx`** (tab "Remaining Plans", Status = "To write"). 14 YMYL-risk plans were removed (tab "Removed (YMYL Risk)") — never write those. Respect the "YMYL Notes" column for each plan.
- Avoid keyword cannibalisation with written pages (e.g. #85 "beginner gym workout" and #77 "full body workout" vs #2 "gym workout plan") — give each a clearly different angle and tell the user.

## MANDATORY workflow for every new plan and exercise page (user instruction, 28 Oct 2026)

> **Two rules, both mandatory, for EVERY workout plan AND exercise page (user instruction, 30 Oct 2026):**
> 1. **Competitor + keyword research first** (steps 1–4 below): fetch the pages Google ranks in the top 7 for the target keyword, then extract short-tail, mid-tail and long-tail keywords, entities, People Also Ask / related queries and autocomplete queries, plus each competitor's outline, structure, FAQs and gaps. Use it to match user intent and cover what users search for, better than the competitors. Show the research data to the user (xlsx + summary) before or with the page.
> 2. **Verified sources** (`SOURCES.md`): every recommendation is checked against those sources, then written in our own coach voice.
> Research decides *what* to cover; sources decide *what is true*.
Do these steps in order for each plan, and show the research to the user before writing:

1. **Competitor research — top 7 ranking pages** for the plan's target keyword (WebSearch; fetch each page with WebFetch or curl). For each competitor record: URL, H1→H2→H3 outline, workout structure (days, exercises, sets/reps/rest), FAQs, data/sources used, word count, depth, and what they do badly.
2. **From all 7 competitors, extract:**
   - **Short-tail keywords** (1–2 words), **mid-tail** (3–4 words) and **long-tail** keywords (5+ words / question phrases) actually used in their titles, headings and body.
   - **Entities** (exercises, muscles, equipment, training concepts, organisations, studies, people) — tag each as used by 3+ competitors (must include) or 2 (differentiator).
3. **Own keyword research** beyond competitors:
   - Autocomplete (all work from the container): Google `https://suggestqueries.google.com/complete/search?client=firefox&q=<kw>`, Bing `https://api.bing.com/osjson.aspx?query=<kw>`, DuckDuckGo `https://duckduckgo.com/ac/?q=<kw>&type=list`. Expand with modifiers (for beginners, for men, for women, at home, pdf, 3 days, 4 days, how to, best, vs, a–z).
   - People Also Ask / related searches via WebSearch.
   - **No search-volume tool is available** — keywords are content-derived, not volume-verified. Say so; the user cross-checks volumes in their keyword tool.
4. **Gap analysis + structure** (what all cover, what 1–2 cover, what none cover), then build the page outline.
5. **Then write the plan** in the batch 1 system (below), verify every claim, build, lint, audit, link-check, and deliver a paste-ready zip.

## Page standards (learned in batch 1 — keep them)
- **Workout first:** Quick Answer → schedule → day tabs → everything else. Users come for the plan; don't make them dig. Keep pages short; no padding, no repeated info, FAQs must add new info.
- **No Key Takeaways box and no Quick Answer box** (plan pages, not articles). Order: hero → stats → jump chips → workout tabs → schedule → other sections.
- Each tab card shows its training days (📅, from `schedule` colours or a `"when"` override), a "Swap:" line per exercise (`batch1/swaps.py`, page `swap_overrides`, or `"swaps": False`), and a "How to progress ↓" link.
- **Day tabs are pure CSS** (radio inputs) so WordPress keeps them; "All days" tab included.
- **Hero line on every page:** "✓ Training reviewed by FISAF-certified coaches · Nutrition reviewed by [Rimsha Shahid](https://exercisemenu.com/rimsha-shahid/), certified dietitian" (her profile title is "Certified Dietitian | Clinical Nutritionist" — never write "registered dietitian").
- **Author box after the FAQ:** Sadia Baloch, FISAF-certified fitness trainer (text in `batch1/build.py` `AUTHOR_BOX`). No other bylines.
- YMYL accuracy: every sets/reps/rest/nutrition claim must match a PubMed/ACSM/NSCA source read in full abstract; cite with working links (`batch1/content/refs.py`). Never invent downloads, tools, reviewers or credentials.
- Link exercise names only to live `/exercises/` pages; internal links only to URLs in the live sitemap (re-check `post-sitemap.xml` and `page-sitemap.xml` each session).
- Rank Math: meta title ≤60, description ≤155, focus keyword in title/description.
- Related plan cards: 4 relevant plans from `PLANS` in `batch1/build.py` (add each new plan there).

## How to build
- Add `batch1/content/<plan>.py` (copy an existing one), add it to `PAGES` and `PLANS` in `batch1/build.py`.
- `python3 build.py` → `python3 lint.py <live_paths.txt>` → `python3 audit.py` (session times, FAQ overlap, AI-phrases) → check all links → `python3 make_zip.py <dir>`.

## WordPress connection (currently not working)
- Auth via Claude **Network secret**: host `exercisemenu.com`, path `/wp-json/`, header `Authorization: Basic <base64>` injected automatically. On 28 Oct 2026 the proxy returned `X-Proxy-Error: upstream auth failed` — the user must fix the secret in the environment settings. `batch1/publish.py test` checks it; `publish.py drafts` saves drafts only.
