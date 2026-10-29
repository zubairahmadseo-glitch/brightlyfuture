# v1.1.0 Test Checklist — Run Before and After Upgrade

## PRE-UPGRADE (backup)
- [ ] WordPress database full backup
- [ ] Backup current plugin folder (`wp-content/plugins/exercisemenu-exercises/`)
- [ ] List current live exercise URLs (should be 8):
  - [ ] barbell-bench-press
  - [ ] barbell-incline-bench-press
  - [ ] dumbbell-bench-press
  - [ ] barbell-curl
  - [ ] dumbbell-biceps-curl
  - [ ] dumbbell-hammer-curl
  - [ ] barbell-standing-calf-raise
  - [ ] barbell-lying-triceps-extension

## UPGRADE STEPS
1. Deactivate the current plugin (do NOT delete)
2. Upload the new `exercisemenu-exercises-v1.1.0.zip` via WP Admin → Plugins → Add New → Upload (replace existing)
3. Activate the plugin
4. Visit **Settings → Permalinks** and click Save (flushes rewrite rules)

## POST-UPGRADE VERIFICATION — Open each of the 8 live pages

For EACH of the 8 pages, confirm:
- [ ] Page loads with no PHP errors (check `debug.log` and `wp-admin → Site Health`)
- [ ] H1 title shows correctly
- [ ] Subtitle shows (if set)
- [ ] "Last updated: [date]" line is visible under subtitle
- [ ] Tags render as pills
- [ ] GIF loads (legacy URL fallback for old pages)
- [ ] Quick Answer box renders
- [ ] How-To Steps list renders (same count as before)
- [ ] Muscles Worked grid renders (primary + secondary)
- [ ] Sets & Reps table renders (no "ACSM" hint now)
- [ ] Common Mistakes list renders (no change)
- [ ] Tips list renders (no change)
- [ ] Modifications render (no change if no `link_id` set)
- [ ] FAQs render (should be visually identical)
- [ ] Related Training Articles section renders (legacy text URLs still work)
- [ ] Sidebar Exercise Profile card renders with ALL fields
- [ ] Sidebar shows "Est. X per set" instead of "Approx. X per set"
- [ ] Below the pill, the "Estimate for a 70 kg person, 30–60 second set." note appears
- [ ] Sidebar Workout Plans card renders (if set)
- [ ] Browse All Exercises CTA button is present

## NEW FUNCTIONALITY TEST (on a new or test exercise)
- [ ] Create a new exercise draft
- [ ] GIF: upload via Media Library picker → preview appears → save → view page: `<img>` has `width`, `height`, `loading="lazy"`
- [ ] How-To Steps: try saving a step with empty description → browser blocks submission (required)
- [ ] How-To Steps: type over 60 chars in title → counter turns red
- [ ] Modifications: pick a "Link to exercise page" → view page: title is clickable, goes to that exercise
- [ ] Related Training Articles: use search picker → pick a post → view page: shows as link card
- [ ] Alternative Exercises: pick 2 exercises → view page: cards with GIF thumbnails appear at bottom
- [ ] Sources: add 2 citations with URLs → view page: numbered list appears before FAQs, links open in new tab
- [ ] Muscle Map Image: upload image → view page: image appears next to Muscles Worked
- [ ] Workout Plans Using This Exercise: pick a post, add day label → view page: card appears after Modifications
- [ ] FAQ sanitize: enter a question with trailing spaces + colon like "Is this safe? :  " → save → re-open: trimmed cleanly

## SEO & SCHEMA VERIFICATION
- [ ] View page source: there should be ONLY ONE `<title>` tag (Rank Math's)
- [ ] View page source: there should be ONLY ONE `<meta name="description">` tag (Rank Math's)
- [ ] If Rank Math is NOT active, the admin "SEO & Meta" box shows a red warning
- [ ] Test Rank Math migration: open an exercise, tick "Copy to Rank Math" box, save → check Rank Math meta title/description fields now populated
- [ ] Google Rich Results Test (https://search.google.com/test/rich-results) on one live page:
  - [ ] Article schema present
  - [ ] FAQPage schema present (only ONE)
  - [ ] BreadcrumbList schema present
  - [ ] ImageObject present (if GIF has Media Library ID)
  - [ ] NO HowTo schema (removed in v1.1)
  - [ ] No duplicate FAQPage from Rank Math

## REST API VERIFICATION
- [ ] GET `/wp-json/wp/v2/exercises` returns list of exercises
- [ ] GET `/wp-json/wp/v2/exercises/[ID]?_fields=meta` returns all `_em_*` meta keys
- [ ] POST with auth creates/updates an exercise (test with Postman using application password)

## SITEMAP VERIFICATION
- [ ] After upgrade, go to **Rank Math SEO → Titles & Meta → Exercises**
- [ ] Toggle "Include in Sitemap" ON (should be visible now)
- [ ] Visit `/sitemap_index.xml`
- [ ] Confirm `exercises-sitemap.xml` is listed
- [ ] Open `exercises-sitemap.xml` — all 8 exercises should appear

## ROLLBACK (if anything breaks)
1. Deactivate v1.1.0
2. Delete v1.1.0 plugin folder
3. Restore the pre-upgrade backup folder
4. Activate the restored plugin
5. All 8 pages should look exactly as before — if not, restore DB backup
