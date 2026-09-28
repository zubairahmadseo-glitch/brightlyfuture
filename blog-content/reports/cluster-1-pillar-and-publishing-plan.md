# Cluster 1 (AI Blog Writing): pillar decision and publishing plan
Prepared 28 September 2026

## 1. What is drafted (10 articles)
| # | Article | Words | Where the draft is |
|---|---|---|---|
| 1 | How to Write a Blog Post Using AI | ~5,430 | branch claude/new-session-8z4t0x |
| 2 | 10 Best AI Blog Writing Tools (Free & Paid) | ~5,210 | branch claude/new-session-8z4t0x |
| 3 | AI Blog Writer vs Human Writer | ~2,880 | branch claude/new-session-8z4t0x |
| 4 | How to Humanize AI Content | ~3,280 | branch claude/new-session-8z4t0x |
| 5 | Blog Post Word Count | ? | your folder (not in repo) |
| 6 | How to Improve Blog Readability Score | ~2,300 | this branch |
| 7 | How to Write Blog Headlines That Get Clicks | ~2,300 | this branch |
| 8 | AI Paraphrasing vs Rewriting | ~1,480 | this branch |
| 9 | Can Google Detect AI Content? | ~2,100 | this branch |
| 10 | AI Content Writing for Small Business | ~2,000 | this branch |

## 2. Pillar decision
Article 1 already works like a pillar: 9 steps covering topics, research, outlines, prompts, humanizing, Google and AI content, SEO, AI search, tools and publishing. A separate new pillar on "AI blog writing" would chase the same searcher and compete with it.

**Recommendation: upgrade Article 1 into the pillar instead of writing a new page.**
1. Keep its URL and primary keyword.
2. Add a "Complete guide" hub block near the top that links every spoke.
3. Shorten each section that a spoke now covers in depth to 2–4 lines, then link:
   - "How do you make AI content sound human?" → Humanize
   - "Does Google penalize AI-generated content?" → Can Google Detect AI Content
   - "Which free AI tools work best?" → Best AI Blog Writing Tools
   - Prompts/headlines/length/readability mentions → Headlines, Word Count, Readability
4. Keep what only the pillar does: the end-to-end 9-step process.

If the roadmap sheet names a *different* pillar keyword (e.g. "AI content writing: complete guide"), check it against Article 1 first. If the intent is the same, don't publish both.

## 3. Roadmap topics that are NOT needed for this cluster
| Roadmap topic | Decision | Why |
|---|---|---|
| 10 Best Free AI Writing Tools for Bloggers | Skip (merge) | Article 2 already has a "Which free AI writing tools are best for bloggers?" section; a second page would cannibalise it |
| How to Use AI for Content Marketing: 2026 Workflow | Skip (merge) | Covered by the pillar (process) + Small Business article (strategy) |
| How to Write SEO Content That Ranks in 2026 | Move to next cluster (SEO) | Broader SEO intent; becomes that cluster's hub |
| Character Count Guide (social, blogs, meta) | Move to tools cluster | Pairs with the Twitter/X character count and meta tag tools |
| AI Blog Writing Prompts: 40 Templates | Optional, later | Distinct intent ("ai blog writing prompts"), but the pillar already has a prompts section. Only write it if you trim that section to a link |

The cluster is complete for launch with the 10 drafted articles.

## 4. Duplication to fix before publishing
| Issue | Where | Fix |
|---|---|---|
| "Should you disclose AI use?" FAQ appears 4 times | Pillar, AI vs Human, Humanize, Google Detect | Keep it in Google Detect only; replace the other three FAQs |
| "Can Google detect AI content?" FAQ | AI vs Human | Replace; link to Google Detect in body |
| H2 "What does Google actually say about AI content in 2026?" | Humanize | Cut to 2 lines + link to Google Detect |
| "How long should an AI blog post be?" FAQ | Pillar | Keep a 1-line answer + link to Word Count |
| "Can AI content appear in AI Overviews?" FAQ | AI vs Human, Google Detect | Keep in Google Detect only |
| Tool links to pages that don't work yet | Several | See section 6 |

## 5. Publishing order (one per day)
| Day | Publish | Links it can carry on the day |
|---|---|---|
| 1 | Pillar (upgraded Article 1) | Hub block lists all spokes as plain text for now; link only live pages |
| 2 | Best AI Blog Writing Tools | Pillar |
| 3 | AI Blog Writer vs Human Writer | Pillar, Tools |
| 4 | How to Humanize AI Content | Pillar, Tools, AI vs Human |
| 5 | Can Google Detect AI Content? | Pillar, Humanize, AI vs Human |
| 6 | AI Paraphrasing vs Rewriting | Pillar, Humanize, Google Detect |
| 7 | Blog Post Word Count | Pillar |
| 8 | How to Improve Blog Readability Score | Pillar, Humanize, Word Count |
| 9 | How to Write Blog Headlines | Pillar, Readability, Tools |
| 10 | AI Content Writing for Small Business | Pillar, Tools, Humanize, Google Detect, Headlines, Paraphrasing |

After each publish: add the new link to the pillar hub block and to any earlier post that mentions the topic.

## 6. Before Day 1
- Upload tools: Readability Checker, Headline Analyzer; paste the fixed Detector and Paraphraser code.
- /ai-blog-generator/ currently shows the old detector. Either build the real generator or remove links to it.
- Confirm the Word Count article's final slug.
- Update the brightlyfuture-content skill's site-info.md with all 10 URLs.

## 7. Indexing
Google finds new pages through your sitemap and internal links whether or not you request indexing, so you can't hold indexing back without a noindex tag (not recommended). Publish daily as planned and request indexing in Search Console for each page on the day it goes live, then the updated pillar.
