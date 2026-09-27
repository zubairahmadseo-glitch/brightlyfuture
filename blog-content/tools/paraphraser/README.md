# BrightlyFuture Paraphraser v2 – install notes

## What was wrong with v1 (the live tool on /ai-paraphrase-rewriter/)
- It was a fixed synonym list (~350 words), not AI. On a normal 64-word paragraph, Standard mode changed 2 words (3%) and Simple mode changed 0.
- It only matched base word forms, so "works", "answers", "ranks" were never changed.
- Several swaps made text worse or wrong: "use" → "utilise" (harder to read), noun "state" → "declare", "help" → "assist".
- Creative and Academic modes pasted "Moreover," / "Furthermore," / "Additionally," onto every third sentence.
- The progress bar faked 1.8 seconds of "Analysing text structure…" work.

## What v2 does
- ~55 phrase rules applied first (e.g. "in order to" → "to", "due to the fact that" → "because", "need to" → "have to").
- ~110 word rules with inflection (works/worked/working), a/an agreement, and a verb/noun guard, so ambiguous words such as "post", "check" or "question" are only changed in the right grammatical position.
- Sentence changes: moves leading clauses ("Before writing, check X" → "Check X before drafting"), fronts trailing "because / if / when" clauses, and splits sentences of 26+ words.
- Mode direction: Simple never picks a longer word and adds contractions; Formal and Academic expand contractions; Casual contracts; Creative restructures the most.
- Protects proper nouns, numbers, URLs, emails and anything in "quotes".
- New "Phrases kept" stat: the share of 5-word phrases that still match the original, plus a note that tells users to cite sources and check names, numbers and "not".
- Each click gives a new variation.

Measured on the test paragraph over 50 runs: Standard kept 22.7% of 5-word phrases on average, Creative 7.9%, Formal 23.8%. v1 kept 83%.

## How to install (Elementor)
1. Edit the /ai-paraphrase-rewriter/ page in Elementor.
2. Open the HTML widget that contains `<script>eval(atob("..."))</script>`.
3. Delete that whole `<script>…</script>` block.
4. Paste the contents of `paste-into-elementor-html-widget.html` in its place.
5. Update, clear any cache plugin, and test all six modes.

No HTML changes are needed: v2 uses the same element IDs and button functions (`setMode`, `paraphraseText`, `copyOutput`, `downloadOutput`, `clearAll`, `toggleFaq`).

## Page copy to fix (currently inaccurate)
| Current claim | Why it's a problem | Suggested wording |
|---|---|---|
| "AI Paraphraser" / "AI-powered" in title and H1 | The tool is rule-based; no AI model runs | "Free Paraphrasing Tool" (or keep "AI" only if you add an AI mode) |
| Standard mode "changes vocabulary and sentence structure" | v1 did not change structure | True for v2 – keep |
| "6 Free Rewriting Modes – More Than QuillBot Offers" | Compares a rule-based tool with an AI model on mode count only | "6 free modes, no sign-up, no word limit" |
| Comparison table figures for QuillBot / Wordtune / Paraphraser.io | Competitor limits change; re-check before publishing | Add "checked on [date]" under the table |
| FAQ "Will the paraphrased text pass plagiarism checkers?" | Tool can't guarantee this; encouraging it conflicts with Google's spam policy | Answer: "Check the Phrases kept score, rewrite anything still close to the original, and always cite your source." |

## Optional next step: a real AI mode
A server-side AI mode (e.g. via the Claude API through a small WordPress plugin) would give true rewriting. It needs an API key, a monthly budget and rate limiting because the tool is free and public, and the page's "processed in your browser" privacy claim would change for that mode.
