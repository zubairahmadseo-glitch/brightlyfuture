# Cluster 1 (Content Marketing & AI Writing): pillar, skips, linking and publishing plan
Updated 28 September 2026 after reading BrightlyFutureContentRoadmap.xlsx (sheet "Pillar 1 - Content", "Internal Linking", "12-Month Calendar").

## 1. Status of the 20 planned pages
| # | Sheet title | Status | Decision |
|---|---|---|---|
| 1 | Complete Guide to AI Content Writing in 2026 (PILLAR) | **Written** (ai-content-writing-guide.md, ~3,100 words) | Publish Day 1 |
| 2 | How to Write a Blog Post Using AI | Drafted | Keep; trim hub-style sections (see 3) |
| 3 | AI Blog Writer vs Human Writer | Drafted | Keep; add links |
| 4 | How to Humanize AI Content | Drafted | Keep; trim Google section; add links |
| 5 | 10 Best Free AI Writing Tools for Bloggers | Drafted as "10 Best AI Blog Writing Tools in 2026 (Free & Paid, Tested)" | Done – counts as #5 |
| 6 | Blog Post Word Count | Drafted (your folder) | Keep |
| 7 | How to Improve Blog Readability Score | Drafted | Keep |
| 8 | How to Write Blog Headlines That Get Clicks | Drafted | Keep |
| 9 | AI Paraphrasing vs Rewriting | Drafted | Keep |
| 10 | Can Google Detect AI Content? | Drafted | Keep |
| 11 | AI Content Writing for Small Business | Drafted | Keep |
| 12 | AI Blog Writing Prompts: 40 Templates | Not written | **Optional – write later** |
| 13 | How to Write SEO Content That Ranks in 2026 | Not written | **Skip for now** |
| 14 | How to Use AI for Content Marketing: 2026 Workflow | Not written | **Skip (merge into pillar)** |
| 15 | Character Count Guide | Not written | **Skip for now (move to Social cluster)** |
| 16 | BrightlyFuture AI Blog Generator Tutorial | Not written | **Skip until the tool exists** |
| 17 | Free Headline Analyzer Tool tutorial | Not written | **Skip – put on the tool page** |
| 18 | Free Readability Checker tutorial | Not written | **Skip – put on the tool page** |
| 19 | Online Word & Character Counter tutorial | Not written | **Skip – put on the tool page** |
| 20 | Free AI Paraphraser tutorial | Not written | **Skip – put on the tool page** |

### Why each skip
- **#12 Prompts:** a real, separate intent ("ai blog writing prompts"), but #2 already has a prompts section and the pillar doesn't need it. Worth writing later as a resource; if you do, cut #2's prompts section to a summary + link.
- **#13 SEO content that ranks:** broad SEO. It would overlap #6 word count, #7 readability, #8 headlines and the Web Design pillar's on-page SEO posts. Better as the hub of a future SEO cluster.
- **#14 AI content marketing workflow:** the same searcher as the pillar ("how to use AI for content") plus #11 small business. Put a short "AI content workflow" section in the pillar instead.
- **#15 Character count guide:** about platform limits (Instagram, X, LinkedIn, meta tags), not AI writing. The sheet itself calls it a cross-pillar bridge. It also needs the Word Counter, which doesn't exist yet.
- **#16–#20 tool tutorials:** the tool pages should rank for "free readability checker", "free ai paraphraser", "word counter", "headline analyzer". A separate blog post with the same keyword would compete with the tool page. The live tool pages already have how-it-works and FAQ sections; improve those instead. #16 needs a working AI Blog Generator first (the page currently runs the old detector code).

**Cluster size for launch: pillar + 10 supporting articles = 11 pages.**

## 2. The pillar (brief from the sheet)
- Title: Complete Guide to AI Content Writing in 2026
- Primary keyword: ai content writing complete guide · Short-tail: ai writing
- Intent: informational · Length: 4,000–5,000 words · Priority: HIGH
- PAA to answer: What is AI content writing? · Is AI writing good for SEO? · Can Google detect AI content? · How to make AI content rank? · Is AI content against Google policies?
- Entities: ChatGPT, Jasper, Copy.ai, Grammarly, Google, Hemingway, WordPress
- Must link: all 10 supporting posts, all 5 content tools, Content Marketing service page
- Suggested URL: /blog/ai-content-writing-guide/ (already used in the 5 drafts I updated; change it everywhere if you choose another)

**How to avoid overlap with #2:** the pillar answers "what is AI content writing and how does it all fit together" (overview, SEO, Google rules, tools, workflow, formats beyond blogs) and hands each topic to its spoke in 1–2 paragraphs. #2 stays the step-by-step tutorial for one blog post.

## 3. Fixes needed in the older 4 drafts (branch claude/new-session-8z4t0x)
| Article | Problem | Fix |
|---|---|---|
| #2 How to Write a Blog Post Using AI | Has full H2s on "Does Google penalize AI content?", "Optimize for AI search", "Which free AI tools" – these belong to #10, pillar and #5 | Cut each to 2–3 lines + link |
| #2 | FAQ "How long should an AI blog post be?" | 1 line + link to #6 |
| #2, #3, #4 | FAQ "Should you disclose AI use?" repeated (also in #10) | Keep only in #10; replace the others |
| #3 AI vs Human | FAQs "Can Google detect AI?" and "AI Overviews" duplicate #10 | Replace |
| #4 Humanize | H2 "What does Google actually say about AI content in 2026?" duplicates #10 | Cut to 2 lines + link |
| #3, #4 | **0 internal links** | Add pillar, tools and lateral links (table 4) |
| #2, #5 | Link to /tools/ai-blog-generator/ (wrong URL; live page is /ai-blog-generator/) | Fix URL |

## 4. Internal linking matrix (sheet rule: every supporting post → pillar ALWAYS + ≥1 tool + service page + 2–3 lateral)
| Article | Pillar | Tools | Service | Lateral links | Status |
|---|---|---|---|---|---|
| #2 Blog post with AI | add | AI Blog Generator*, Readability Checker | add | #4 Humanize, #5 Tools, #12 Prompts (if written) | needs fixes |
| #3 AI vs Human | add | AI Blog Generator*, AI Paraphraser | add | #2, #4, #10 | needs fixes |
| #4 Humanize | add | AI Paraphraser, Readability Checker, AI Detector | add | #3, #10, #9 | needs fixes |
| #5 Best AI Tools | add | AI Blog Generator*, AI Paraphraser, Headline Analyzer | add | #2, #3 | needs fixes |
| #6 Word Count | add | Word Counter*, Readability Checker | add | #2, #7 | check your file |
| #7 Readability | ✓ | Readability Checker ✓ | ✓ | #4 ✓, #6 ✓, #2 ✓ | done |
| #8 Headlines | ✓ | Headline Analyzer ✓, AI Blog Generator* ✓ | ✓ | #7 ✓, #2 ✓, #5 ✓ | done |
| #9 Paraphrasing | ✓ | AI Paraphraser ✓, Readability Checker ✓ | ✓ | #4 ✓, #5 ✓, #10 ✓, #2 ✓ | done |
| #10 Google Detect | ✓ | AI Detector ✓, Readability ✓, AI Blog Generator* ✓ | ✓ | #4 ✓, #3 ✓, #9 ✓, #2 ✓ | done |
| #11 Small Business | ✓ | – (sheet tools not live) | ✓ | #5 ✓, #4 ✓, #10 ✓, #8 ✓, #2 ✓ | add tools when live |
\* tool page not working yet (see section 6).

## 5. Publishing order (one per day)
The sheet's calendar says publish the pillar **after** the supporting posts. With daily publishing, **pillar first** is simpler: each new spoke links to a live pillar on its first day, and you only update one page (the pillar) each day instead of editing ten posts at the end. Either works; don't publish links to pages that aren't live yet.

| Day | Publish |
|---|---|
| 1 | Pillar – Complete Guide to AI Content Writing |
| 2 | #2 How to Write a Blog Post Using AI |
| 3 | #5 Best AI Blog Writing Tools |
| 4 | #3 AI Blog Writer vs Human Writer |
| 5 | #4 How to Humanize AI Content |
| 6 | #10 Can Google Detect AI Content? |
| 7 | #9 AI Paraphrasing vs Rewriting |
| 8 | #6 Blog Post Word Count |
| 9 | #7 Readability Score |
| 10 | #8 Blog Headlines |
| 11 | #11 AI Content Writing for Small Business |
Each day: add the new post to the pillar's hub list and to any earlier post that mentions its topic.

## 6. Before Day 1
- Tools the pillar must link: AI Blog Generator (page runs old detector code – build the real generator or drop the link), AI Paraphraser (paste v2 code), Readability Checker (upload to /readability-checker/), Word Counter (doesn't exist – build or drop), Headline Analyzer (upload to /headline-analyzer/).
- Tool URLs follow the site pattern (root level, e.g. /ai-paraphrase-rewriter/). The 5 updated drafts now use /readability-checker/ and /headline-analyzer/.
- Confirm #6's slug (drafts use /blog/blog-post-word-count/).
- Update the skill's site-info.md with all URLs.

## 7. Indexing
Google discovers pages through your sitemap and internal links whether or not you request indexing; the only way to hold it back is a noindex tag, which isn't worth it. Request indexing in Search Console for each post on the day it goes live, and start the next cluster in parallel.

## 8. Pillar design notes (written 28 Sept 2026)
- Each section answers its question in 2–4 short paragraphs, then links to the spoke that owns the topic. It does not repeat spoke data (tests, studies, checklists).
- Pillar-only content (no spoke covers it): what AI content writing is and how LLMs work, content-type table and format tips (email, social, product descriptions, ads), the 7-stage workflow overview (replaces roadmap #14), a measurement scorecard, a glossary, and the tools hub.
- Length: ~3,100 words instead of the sheet's 4,000–5,000. Going longer would mean re-explaining spokes, which creates the overlap you asked to avoid.
- Links: all 10 spokes, 6 tools, Content Marketing service page.
