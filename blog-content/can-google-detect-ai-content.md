# Can Google Detect AI Content? What the Data Says (2026)

> **Quick Answer:** Google can spot low-value AI content, but it doesn't rank pages on who or what wrote them. Its spam policies, SpamBrain and core ranking systems judge usefulness. Ahrefs found a 0.011 correlation between AI use and rankings across 600,000 pages. Only Gemini text carries Google's SynthID watermark.

[IMG 01-google-ai-featured.webp | Can Google detect AI content – what the 2026 data says]

Every article on BrightlyFuture starts as a Claude draft. I then edit it by hand, add my own tests and data, and check every source. Our Search Console clicks went from 77 in the first month to 164 in the second and 970 in the third. So when people ask whether Google can detect AI content, I have a stake in the answer.

The short version: it's the wrong question. Google has never said it runs an "is this AI?" check on your pages, and its public guidance says the opposite. What it does run are systems that find pages made to rank rather than to help. Below you'll find what Google has actually said up to September 2026, what the large studies show, and a test I ran that shows why AI detector scores tell you less than you think.

## Can Google detect AI-generated content?

Google has not confirmed that it uses an AI-text classifier for ranking, and it doesn't need one. Its systems look for the patterns that low-effort content leaves behind, such as thin, repetitive or unoriginal pages published at scale, whether a person or a model produced them. The one place Google can identify AI text directly is its own Gemini output, through the SynthID watermark.

Three facts help frame this:

- **Google's official position is method-neutral.** In its [February 2023 guidance on AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content), Google said it rewards high-quality content however it's produced. Its [generative AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), last updated in December 2025, keeps that line: AI help is fine; generating many pages without adding value may break the scaled content abuse policy.
- **Google does study AI content internally.** Search Engine Journal reported that the LinkedIn profile of Chris Nelson, a Google Search employee who co-authored that guidance, mentions building ranking solutions for the ["detection and treatment of AI-generated content"](https://www.searchenginejournal.com/evidence-that-google-detects-ai-generated-content/537571/). Google has not commented on it officially.
- **SynthID only covers Google's own model.** DeepMind's SynthID-Text, described in a [Nature paper in October 2024](https://www.nature.com/articles/s41586-024-08025-4), watermarks Gemini output by nudging word choices. It can't identify text from other models, and the paper's authors caution that text watermarks can be circumvented by editing or paraphrasing.

So Google may well know when a page reads like unedited AI. The question that decides your rankings is whether the page is worth showing.

## Does Google penalize AI content?

No. Google does not penalize content for being written with AI. It demotes or removes pages that are unhelpful, unoriginal or made mainly to manipulate rankings, and that applies equally to human-written content.

The largest public study backs this up. In July 2025, Ahrefs checked the top 20 results for 100,000 keywords, 600,000 pages in total, with its own AI detector. The [correlation between AI use and ranking position was 0.011](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/), which in practice means none. Most top pages were a mix of human and AI writing.

[IMG 02-google-ai-ahrefs.webp | Ahrefs study: 13.5% purely human, 81.9% mixed, 4.6% purely AI among 600,000 top-ranking pages]

Two details from that study matter more than the headline:

- Only 4.6% of ranking pages were fully AI-generated, while 81.9% mixed human and AI work.
- Pages in position one used slightly less AI on average. Ahrefs calls the trend very weak, but it fits what I see on my own site: the posts that climb are the ones where I added a test, a screenshot or a number no one else had.

Google's July 2026 [guide to generative AI features in Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) makes the same point from another angle. It warns against "commodity content" built on common knowledge and asks for "unique expert or experienced takes that go beyond common knowledge." Raw AI output is commodity content by default, because it's built from what's already been written.

## How does Google actually spot low-quality AI content?

Google uses the same layers it uses for all content: spam policies enforced partly by SpamBrain, core ranking systems that reward helpful pages, and human quality raters whose feedback trains those systems. None of them asks "was this written by AI?" All of them ask "does this page add value?"

[IMG 04-google-ai-how-google-judges.webp | What Google checks instead of who wrote the content]

**Spam policies.** Google's [spam policies](https://developers.google.com/search/docs/essentials/spam-policies), last updated in August 2026, define scaled content abuse as generating many pages to manipulate rankings rather than help users. The policy lists "using generative AI tools or other similar tools" as one method, next to scraping and synonym swapping. Google enforces these policies through regular spam updates. Its [Search Status Dashboard](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history) lists spam updates in August 2025, June 2026, August 2026 and one that began on 24 September 2026.

**Core ranking systems.** In March 2024, Google announced a core update aimed at [reducing low-quality, unoriginal content in search results](https://blog.google/products-and-platforms/products/search/google-search-update-march-2024/). It expected a 40% reduction; after the rollout it reported 45%.

**Quality raters.** Google's [Search Quality Rater Guidelines](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf), current version dated 11 September 2025, tell raters to give the Lowest rating when almost all of a page is copied, paraphrased or AI-generated "with little to no effort, little to no originality, and little to no added value." The guidelines include examples of templated question-and-answer articles "often using generative AI tools" as scaled content abuse. Raters don't change rankings directly, but their ratings help Google test its systems.

[IMG 05-google-ai-timeline.webp | Timeline of Google's stance on AI content from 2023 to 2026]

## Is AI content against Google's guidelines?

No. Using AI to research, outline, draft or edit content is within Google's guidelines. It becomes a problem when AI is used to publish many pages that add nothing, which falls under the scaled content abuse policy.

Google's generative AI guidance adds two specific rules worth knowing. Metadata such as titles, meta descriptions, structured data and alt text must be accurate even when AI writes it. And e-commerce sites must label AI-generated product images with IPTC metadata and specify AI-generated product data separately.

Everything else is judged the same way as human writing. A 3,000-word AI article that repeats the top ten results adds nothing. A 900-word article built on your own data can outrank it, whoever typed the first draft.

## Will AI content get deindexed?

AI content on its own won't get a site deindexed. Sites get deindexed when they break spam policies, most often by publishing large volumes of low-value pages. Many of the sites hit in March 2024 fit that pattern.

When Google's March 2024 update began, it also issued manual actions, and some sites vanished from search entirely. Originality.ai, which sells an AI detector, checked 79,000 sites on three ad networks and [found 1,446 with manual actions](https://originality.ai/blog/google-march-2024-manual-action-ai-update-list). It reported that every deindexed site it sampled showed signs of AI content, many at over 90% AI. Keep in mind who ran the study and which detector it used. The pattern still matches Google's own wording: these were sites publishing at a scale no editor could review.

Pages can also drop out of the index without any penalty. Google crawls far more pages than it keeps, and thin pages that duplicate what's already indexed are the first to go. Search Console shows these under "Crawled – currently not indexed".

## What happened when I tested AI detectors myself?

I tested the free detector we originally built for BrightlyFuture on 37 texts, and it failed: it labelled 20 of 27 human texts "Mixed" and didn't label a single raw AI draft "Likely AI". So I rebuilt it and tested the new version on 176 texts it had never seen. It flagged 87% of ChatGPT answers, but it also flagged 16% of human writing.

**Round 1: the original tool.** I used 27 texts written by people between 1788 and 2012 (Darwin, Austen, Twain, Melville, Conan Doyle, the Federalist Papers and Paul Graham essays), 6 raw AI drafts and 4 AI drafts I had edited by hand, the way I describe in [how to humanize AI content](https://brightlyfuture.co.uk/blog/how-to-humanize-ai-content/).

[IMG 03-google-ai-detector-test.webp | Round 1: 27 human texts, 6 raw AI drafts and 4 edited AI drafts run through our original detector]

| Group | Texts | Average AI score | Labelled "Likely AI" | Labelled "Mixed" | Labelled "Human" |
|---|---|---|---|---|---|
| Human writing (1788–2012) | 27 | 47.6% | 0 | 20 | 7 |
| Raw AI drafts | 6 | 58.5% | 0 | 6 | 0 |
| AI drafts, edited by hand | 4 | 35.0% | 0 | 0 | 4 |

The Federalist Papers scored as "more AI" than the average AI draft. The tool started every sentence at 50% AI and rewarded casual style, so formal human writing looked suspicious and lightly edited AI looked human.

**Round 2: the rebuilt checker.** I rewrote it to measure 14 signals that differ between unedited AI and human text, including stock AI phrases, lists of three, sentence-length variety, specific details, personal voice and informal slips. I fitted the weights on part of [HC3](https://arxiv.org/abs/2301.07597), a public research dataset of human and ChatGPT answers to the same questions, then tested on 176 texts the model had never seen.

[IMG 07-google-ai-old-vs-new.webp | Old detector vs rebuilt checker on 176 unseen texts]

| On 176 unseen texts | Original tool | Rebuilt checker (score 50+) | Rebuilt checker (score 80+) |
|---|---|---|---|
| ChatGPT answers flagged | 14% ("Likely AI") | 87% | 51% |
| Human texts wrongly flagged | 70% ("Mixed" or above) | 16% | 5% |

[IMG 06-google-ai-checker-v2.webp | Screenshot: the rebuilt checker highlighting a raw AI paragraph]

Much better, and still not proof. One in six human texts scored 50 or more, mostly formal or technical writing, and every AI draft I had edited by hand scored as human. That's why the rebuilt tool reports "AI-style signals" and highlights the sentences to fix, instead of claiming to know who wrote the text.

Commercial detectors use larger trained models, but the research shows the same limits:

- **OpenAI withdrew its own detector.** Its AI Text Classifier caught only 26% of AI-written text in OpenAI's tests and was [shut down in July 2023](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) for its low rate of accuracy.
- **Attacks and new models fool detectors.** The RAID benchmark, presented at ACL 2024, tested 12 detectors on over 6 million texts and found them ["easily fooled by adversarial attacks, variations in sampling strategies, repetition penalties, and unseen generative models"](https://arxiv.org/abs/2405.07940).
- **The bias question is still open.** A 2023 study in Patterns found seven detectors flagged [over 61% of TOEFL essays by non-native English writers](https://arxiv.org/abs/2304.02819) as AI. A February 2026 study of Czech texts found [no systematic bias against non-native writers](https://arxiv.org/abs/2602.05769) in modern detectors, which suggests newer tools have improved, at least in that language.

The practical lesson: use a detector as an editing aid, not a verdict. Our [free AI writing checker](https://brightlyfuture.co.uk/ai-blog-detector/) highlights the sentences that read like generic AI so you can rewrite them. It can't prove who wrote a text, and no public tool can.

## How can you use AI without risking your rankings?

Keep AI in the drafting seat and yourself in the editing seat. Every risk in Google's policies comes from publishing AI output that nobody improved, so whether the first draft comes from ChatGPT, Claude or our [AI Blog Generator](https://brightlyfuture.co.uk/ai-blog-generator/), check each page against these five questions before it goes live:

1. **Does it add something the top results don't have?** A test, a screenshot, a client result or your own numbers. In this post, it's the detector test. If the answer is no, the page is commodity content.
2. **Has every fact been checked?** AI drafts invent statistics with confidence. Open each source and cut anything you can't confirm.
3. **Is the metadata accurate?** Google's AI guidance singles out titles, meta descriptions, structured data and alt text.
4. **Would you publish it at this pace without AI?** Scale without review is what the spam policy targets. Ten edited posts beat a hundred unread ones.
5. **Does it read like a person wrote it for a person?** Check the [readability score](https://brightlyfuture.co.uk/readability-checker/) and run it through the [AI writing checker](https://brightlyfuture.co.uk/ai-blog-detector/) to find sentences that need your voice.

For the full drafting workflow, see the [step-by-step guide to writing a blog post with AI](https://brightlyfuture.co.uk/blog/how-to-write-blog-post-using-ai/). For editing techniques, see the humanizing guide linked above, and for where each side is stronger, [AI blog writer vs human writer](https://brightlyfuture.co.uk/blog/ai-blog-writer-vs-human-writer/). If you rework existing text, rewrite rather than spin: synonym swapping is named in Google's spam policies, as I explain in [paraphrasing vs rewriting](https://brightlyfuture.co.uk/blog/ai-paraphrasing-vs-rewriting/).

## Frequently Asked Questions

### Does Google use GPTZero, Originality.ai or Turnitin?

There is no evidence that Google uses any third-party AI detector. Those tools are sold to publishers, schools and SEO teams. Google builds its own ranking and spam systems and has never named an outside detector as part of them.

### Should I tell readers when I use AI to write?

Google's guidance suggests it can help to explain how content was created, especially where readers would reasonably ask, but there is no ranking rule that requires a label on blog posts. A short "how we wrote this" note can build trust with readers. It won't change how Google ranks the page.

### Can Google tell whether I used ChatGPT, Claude or Gemini?

Only Gemini output can carry Google's SynthID watermark, and even that weakens after heavy editing. Google has not said it can tell text from ChatGPT or Claude apart from human writing, and it doesn't need to: the same quality rules apply to all three.

### Do AI humanizer tools protect a site from Google?

No. Humanizers change style, not substance. A page that adds nothing new is still thin after it has been "humanized", and some humanizers produce awkward text that is harder to read. Adding original data or experience does far more than any rewording tool.

### Can AI-written pages appear in AI Overviews and AI Mode?

Yes. Google [says its AI features](https://developers.google.com/search/docs/appearance/ai-features) are rooted in the same core ranking and quality systems as regular results, and that no special optimisation is needed to appear in them. A page is eligible if it is indexed and can show a snippet, so the same quality bar applies whether a person or a model wrote the first draft.

## Final thoughts

Google doesn't need to detect AI to deal with bad AI content. Its systems catch pages that add nothing, and unedited AI drafts usually add nothing. Use AI to write faster, then spend the saved time on the parts only you can supply. That combination is what grew this site, and it's what the 2026 data rewards.

For the bigger picture on tools, SEO and Google's rules, start with our [complete guide to AI content writing](https://brightlyfuture.co.uk/blog/ai-content-writing-guide/). If you'd rather hand the writing over, see our [content marketing service](https://brightlyfuture.co.uk/content-marketing/).
