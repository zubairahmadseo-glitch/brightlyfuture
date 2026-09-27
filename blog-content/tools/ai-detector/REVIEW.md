# Review: /ai-blog-detector/ (September 2026)

## Is it the right tool for the "Can Google detect AI content?" article?
Yes, on topic. But it must be described honestly: it is a pattern/style checker, not a detector that can prove authorship.

## How it works (decoded from the page script)
- Every sentence starts at 50% "AI" and gains or loses points for length, a short list of AI phrases, passive voice, contractions, "I/me", and casual words.
- "Perplexity" on the page is actually the share of words not in a 100-word common-word list. That is not perplexity (which needs a language model).
- "Burstiness", "uniformity" and "vocabulary richness" are real, simple statistics.

## Test (37 texts)
| Group | Texts | Avg AI score | Likely AI | Mixed | Human |
|---|---|---|---|---|---|
| Human writing 1788–2012 (Gutenberg + Paul Graham) | 27 | 47.6% | 0 | 20 | 7 |
| Raw AI drafts | 6 | 58.5% | 0 | 6 | 0 |
| AI drafts edited by hand | 4 | 35.0% | 0 | 0 | 4 |
Full per-text scores: test-results-2026-09.json

## Recommended fixes
1. Rename metrics: "Perplexity" → "Common-word ratio" (or compute nothing called perplexity).
2. Replace "AI Probability %" with an "AI-style signals" score and say plainly on the page that no free tool can prove who wrote a text.
3. Remove the 50% starting point per sentence; it pushes formal human writing into "Mixed".
4. Expand the AI-phrase list (and include the kill-list phrases used in our writing rules) so the tool is useful as an editing aid.
5. Page copy: remove comparisons that imply accuracy parity with GPTZero / Originality.ai unless tested.

I can rebuild it the same way as the paraphraser (drop-in script, same element IDs) if you want.
