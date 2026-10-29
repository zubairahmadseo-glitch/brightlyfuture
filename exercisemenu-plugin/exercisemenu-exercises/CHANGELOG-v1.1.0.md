# ExerciseMenu Exercises Plugin — v1.1.0 Changelog

## Changed files
1. `exercisemenu-exercises.php` — plugin main file
2. `templates/single-exercise.php` — front-end template

## PART 1 — Modified sections

### SEO & Meta
- Plugin's own `<title>` and `<meta name="description">` output is now DISABLED by default.
- Rank Math fully controls these tags.
- Legacy fields (`_em_meta_title`, `_em_meta_desc`) are preserved in the DB and still editable in the admin, now labeled "Legacy".
- A "Copy to Rank Math" checkbox lets you transfer legacy values to `rank_math_title` / `rank_math_description` on save.
- Meta Description counter changed from 160 → 155.
- To re-enable the old output (if Rank Math is removed), add this to `wp-config.php`:
  ```php
  define('EM_OUTPUT_LEGACY_META', true);
  ```
- Plugin now also disables Rank Math's FAQPage schema on exercise pages (plugin outputs its own) to prevent duplicates.

### Exercise Basics
- "Approx. Calories per set" renamed to "Estimated Calories per set".
- Front end now shows: "Estimate for a 70 kg person, 30–60 second set."
- NOTE: Taxonomy conversion for Target Muscle / Body Part / Equipment / Skill Level is deferred to v2.0 (breaking change with migration — needs dedicated release).

### GIF / Media
- Added WordPress Media Library picker.
- Legacy "GIF CDN URL" field preserved as fallback.
- Removed "Replace YOUR_CDN_URL with actual CDN domain." helper text.
- Front end `<img>` now outputs `width`, `height`, and `loading="lazy"` when a Media Library item is selected.

### How-To Steps
- Step Title is limited to 60 characters with a live counter.
- Step Description is marked required (HTML5 `required` attribute + visual asterisk).

### Common Mistakes and Tips
- NOT split in v1.1 — deferred to v2.0 (breaking change, needs migration).
- Current behavior preserved.

### Modifications
- Added "Link to exercise page" dropdown (lists all exercise CPTs).
- If filled, the modification title becomes a clickable link to that exercise.

### FAQs
- On save, leading/trailing whitespace and stray colons (`:`) are trimmed from both the question and the answer.

### Sets & Reps Table
- Removed the "Rest periods follow ACSM guidelines" hint.

## PART 2 — New sections

### Related Training Articles (upgraded)
- Replaced manual title+URL fields with a post/page picker (searchable).
- Legacy text URL fields still work as fallback.
- Supports 3 articles.

### Workout Plans Using This Exercise (new)
- Manual repeater with post/page picker + Day label (e.g. "Push A").
- Rendered as cards after Modifications on the front end.
- Note: auto-detect option deferred (needs clarity on your workout-plan post structure).

### Alternative Exercises (new)
- 4 dropdowns to pick exercise CPT posts.
- Rendered as cards with GIF thumbnail at the bottom of the page.

### Sources (new)
- Repeater: citation text + URL.
- Rendered as numbered list before FAQs.
- All links use `target="_blank" rel="noopener"`.

### Last Updated (new)
- "Last updated: [date]" line shown directly under the subtitle.
- Uses `get_the_modified_date('F j, Y', $post_id)`.
- No field needed.

### Muscle Map Image (new)
- Image picker (Media Library).
- Shown next to the Muscles Worked grid if set.

## PART 3 — Technical

### CPT public + Rank Math sitemap
- CPT `exercise` was already registered with `'public' => true`.
- NEW: `show_in_rest => true` is now forced on the CPT so Rank Math exposes it in the sitemap.
- To enable in Rank Math UI:
  - Go to **Rank Math SEO → Titles & Meta → Exercises** (the CPT appears once `show_in_rest` is active)
  - Set **"Include in Sitemap"** to **ON**
  - Save. Then visit `/sitemap_index.xml` and confirm `exercises-sitemap.xml` appears.

### Schema
- REMOVED: HowTo schema (Google deprecated rich results for HowTo in 2023).
- ADDED: Article schema (with author = Sadia Baloch, publisher = Exercise Menu).
- ADDED: ImageObject schema for the GIF (including width/height when known).
- KEPT: FAQPage, BreadcrumbList.
- Plugin automatically suppresses Rank Math's duplicate FAQPage schema on exercise pages.

### REST API
- CPT exposed at: `/wp-json/wp/v2/exercises`
- All plugin fields registered with `show_in_rest => true` and `auth_callback` requiring `edit_posts`.
- Full meta key list below.

## REST API — Meta Keys & Formats

| Meta Key | Type | Notes |
|---|---|---|
| `_em_meta_title` | string | Legacy, superseded by `rank_math_title` |
| `_em_meta_desc` | string | Legacy, superseded by `rank_math_description` |
| `_em_subtitle` | string | |
| `_em_tags` | string | Comma-separated |
| `_em_target_muscle` | string | |
| `_em_body_part` | string | |
| `_em_equipment` | string | |
| `_em_category` | string | |
| `_em_skill_level` | string | Beginner / Intermediate / Advanced |
| `_em_movement` | string | |
| `_em_also_known_as` | string | |
| `_em_calories` | string | |
| `_em_gif_url` | string | Legacy URL fallback |
| `_em_gif_media_id` | integer | WP attachment ID (preferred) |
| `_em_gif_alt` | string | |
| `_em_muscle_map_id` | integer | WP attachment ID |
| `_em_quick_answer` | string | |
| `_em_primary_muscles` | array of strings | |
| `_em_secondary_muscles` | array of strings | |
| `_em_mistakes` | array of strings | |
| `_em_tips` | array of strings | |
| `_em_alt_exercises` | array of integers | Exercise post IDs |
| `_em_steps` | string (JSON) | `[{"title":"","desc":""},...]` |
| `_em_sets_reps` | string (JSON) | `[{"goal":"","sets":"","reps":"","rest":""},...]` |
| `_em_mods` | string (JSON) | `[{"type":"easier","title":"","desc":"","link_id":0},...]` |
| `_em_faqs` | string (JSON) | `[{"q":"","a":""},...]` |
| `_em_related` | string (JSON) | `[{"title":"","url":"","post_id":0},...]` |
| `_em_sources` | string (JSON) | `[{"text":"","url":""},...]` |
| `_em_workout_plans_list` | string (JSON) | `[{"post_id":0,"day_label":""},...]` |
| `_em_sidebar_plans` | string (JSON) | `[{"title":"","url":"","meta":"","coming_soon":""},...]` |

### REST write example
```bash
curl -X POST https://exercisemenu.com/wp-json/wp/v2/exercises \
  -u "username:application_password" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dumbbell Fly",
    "status": "draft",
    "meta": {
      "_em_subtitle": "Isolation chest exercise...",
      "_em_quick_answer": "The dumbbell fly isolates...",
      "_em_gif_media_id": 1234,
      "_em_steps": "[{\"title\":\"Lie flat\",\"desc\":\"On a bench...\"}]",
      "_em_faqs": "[{\"q\":\"How many reps?\",\"a\":\"8-12 for growth.\"}]"
    }
  }'
```

## Deferred to v1.2.0 (next release)
- Full Rank Math SEO sync (bi-directional, if needed)

## Deferred to v2.0.0 (breaking release, needs migration)
- Converting Target Muscle / Body Part / Equipment / Skill Level into custom taxonomies with archive pages
- Splitting Mistakes/Tips into Title + Description fields
- Workout Plans auto-detect (if you want this instead of manual picker)
