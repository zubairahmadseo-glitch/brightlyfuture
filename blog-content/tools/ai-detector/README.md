# BrightlyFuture AI Writing Pattern Checker v2 (/ai-blog-detector/)

## Problems found in the live v1 tool
1. **Results never showed.** The page CSS has `.result-section { display: none; }` and v1 set `style.display = ''`, which falls back to that CSS rule. Users clicked "Analyse" and saw nothing after the progress bar.
2. **Scores were not meaningful.** Every sentence started at 50% "AI". On 176 unseen texts, v1's "Likely AI" label caught 14% of ChatGPT answers, while its "Mixed" label caught 70% of human texts.
3. **"Perplexity" was mislabelled.** It was the share of words outside a 100-word common list, not perplexity.
4. **Fake progress bar** of 2.2 seconds.

## What v2 does
- 14 signals: stock AI phrases (weighted list of ~100), lists of three, stock transition openers, generic advice phrasing, stock framing ("there are several…", "it is also…"), hedging words, specific details (numbers, names, quotes), first-person voice and contractions, informal slips, parentheses, long-word share, vocabulary richness, sentence-length variety, average sentence length.
- Logistic model fitted on 252 labelled texts (HC3 ChatGPT vs human answers + pre-AI human writing). Weights in `model-weights.json`.
- Honest output: "Strong / Some / Few AI-style signals", a plain-English explanation, and a note stating accuracy limits.
- Sentence highlighting with a tooltip showing *why* each sentence was flagged (e.g. "leverage", list of three, stock opener).
- Relabels the four breakdown boxes to what they actually measure: Stock AI phrases, Sentence variety, Specific details, Generic framing.
- Minimum 40 words; warns under 120 words.
- Downloadable report lists every sentence with its reasons.

## Measured accuracy (176 texts not used for fitting: 79 ChatGPT, 97 human)
| Threshold | ChatGPT answers flagged | Human texts wrongly flagged |
|---|---|---|
| Score 50+ ("Some" or "Strong") | 87% | 16% |
| Score 80+ ("Strong") | 51% | 5% |
Hand-edited AI drafts (6) all scored below 50: the tool measures style, and edited AI changes style.

## Install (Elementor)
1. Edit /ai-blog-detector/ in Elementor.
2. In the HTML widget, delete the whole `<script>eval(atob("..."))</script>` block.
3. Paste the contents of `paste-into-elementor-html-widget.html` in its place.
4. Update, clear cache, click "Load Sample Text" then "Analyse". Results should now appear.
No HTML edits are needed; the script relabels the boxes itself.

## Page copy to update (currently inaccurate)
| Current | Suggested |
|---|---|
| H1 "Free AI Content Detector" / "detect whether any text was written by AI" | "Free AI Writing Checker – find the sentences that sound like AI" |
| "AI Probability / Human Probability" | Handled by the script ("AI-style signals / Human-style signals") |
| "Perplexity Score" explanation section | Replace with the four signals the tool now shows |
| Comparison table vs GPTZero / Originality.ai claiming parity | Remove accuracy comparisons; keep "free, no sign-up, no limit" |
| Any FAQ promising the tool can tell if a teacher/Google will flag text | "No detector can prove authorship. Use the highlights to edit." |

## Files
- `detector-core.js` – scoring engine (Node + browser)
- `detector-engine.js` – engine + page wiring
- `paste-into-elementor-html-widget.html` – ready to paste
- `model-weights.json` – fitted weights, means, standard deviations
- `test-results-2026-09.json` – round 1 scores of the old tool
