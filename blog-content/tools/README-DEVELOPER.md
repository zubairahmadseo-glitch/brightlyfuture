# Pillar tools – developer install notes (28 Sept 2026)

| Tool | Page | File to paste | Action |
|---|---|---|---|
| AI Paraphraser v2 | /ai-paraphrase-rewriter/ | paraphraser/Paraphraser-Code-COPY-THIS.txt | Replace the old tool script in the Elementor HTML widget |
| AI Detector v2 | /ai-blog-detector/ | ai-detector/AI-Detector-Code-COPY-THIS.txt | Replace old script (remove the duplicate copy too) |
| AI Blog Generator (new) | /ai-blog-generator/ | ai-blog-generator/AI-Blog-Generator-Code-COPY-THIS.txt | Delete the old detector HTML+script on this page, paste this in one HTML widget |
| Word Counter v2 | /word-character-counter/ | word-counter/Word-Counter-Code-COPY-THIS.txt | Replace only the old `<script>`; keep existing HTML (same IDs) |
| Readability Checker (new) | /readability-checker/ (create page) | readability-checker/Readability-Checker-Code-COPY-THIS.txt | New page, one HTML widget |
| Headline Analyzer (new) | /headline-analyzer/ (create page) | headline-analyzer/Headline-Analyzer-Code-COPY-THIS.txt | New page, one HTML widget |

Notes
- Each file is self-contained; paste the whole file into one Elementor HTML widget. Widgets use Shadow DOM so theme CSS won't break them.
- Blog Generator uses the free Pollinations API (no key); one request per ~15 s, cooldown built in.
- After install: clear Elementor/cache plugin cache and test each page once.
