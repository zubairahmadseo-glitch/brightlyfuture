# Homepage Fixes: What to Edit and Why

Checked on 30 September 2026 against the live site (brightlyfuture.co.uk), your screenshots, the About page and the Editorial Policy. Fixes are in priority order: do Part 1 first.

## Part 1: Critical (trust and legal) – fix before anything else

### 1. Testimonials: confirm they are real, or remove them

The "What clients say" section shows James Whitfield (CTO, Proventus Logistics), Sarah Okonkwo (Head of Content, Meridian Media) and Marcus Reid (Founder, EduPortal UK). These look like the placeholder reviews that come with website templates.

- If they are **not** real clients: delete the whole section now. Since April 2025, fake reviews are banned outright in the UK under the Digital Markets, Competition and Consumers Act 2024, and fake testimonials also destroy trust with Google's quality raters.
- If they **are** real: add a photo, a link to the company or LinkedIn profile, and get written permission to publish.
- Better replacement: use your real Project A, B and C Search Console results from the About page as proof (see Part 4).

### 2. Footer company details

The footer says "© 2025 BrightlyFuture Ltd. All rights reserved. Registered in England & Wales."

- If BrightlyFuture Ltd **is** registered at Companies House: the law requires the company number and registered office address on the website. Add: "BrightlyFuture Ltd, company number [number], registered office [address]."
- If it is **not** a registered company: remove "Ltd" and "Registered in England & Wales". Calling a business "Ltd" when it isn't registered is not allowed.
- Change "© 2025" to "© 2026" (or set it to update automatically).

### 3. Privacy Policy and Terms of Service links are broken

Both footer links go to pages that don't exist (404). You need a Privacy Policy because the contact form collects names and emails, and some tools send text to an outside AI service. Create both pages before sending traffic to the site.

### 4. Numbers that can't be backed up

| Where | Claim | Problem | Fix |
|---|---|---|---|
| Hero + About section | 120+ projects delivered | No evidence anywhere on the site | Keep only if you can list or count them; otherwise remove |
| Hero + About section | 98% client satisfaction | A percentage needs a survey or review source | Remove, or replace with a real, linkable review rating (e.g. Google reviews) |
| Hero + About section | 15+ free tools | Only 14 tool pages are live (checked) | Change to "14 free tools", or build one more |
| Hero badge | Est. 2020 | About page says 6 years of SEO experience (since 2020 is 6 years; fine) but "5yr in business" in the About section contradicts "Est. 2020" | Use one number everywhere: "Est. 2020" and "6 years" |
| About section | "grew into a small, focused team" | About page describes a one-person blog written by you | Only say "team" if others work with you; otherwise say "I" |
| Hero dashboard | 4,200 req/min, 99.97% uptime, 12ms latency | Looks like real client data but is decoration | Replace with a real Search Console screenshot, or label it "Example dashboard" |

## Part 2: Broken links on the homepage

Checked every link. These go to 404 pages:

| Link | Where it appears | Fix |
|---|---|---|
| /ai-solutions/ | Services card "Learn More", footer | Create the page, or remove the card |
| /php-development/ | Services card "Learn More", footer | Create the page, or remove the card |
| /custom-api/ | Services card "Learn More", footer | Create the page, or remove the card |
| /blog-analyzer/ and /tools/blog-analyzer.html | Tools section card, footer | Tool doesn't exist: replace with Readability Checker (/readability-checker/) |
| /json-validator/ and /tools/json-validator.html | Tools section card, footer | Tool doesn't exist: replace with Headline Analyzer (/headline-analyzer/) |
| /password-generator/ and /tools/password-generator.html | Tools section card, footer | Tool doesn't exist: replace with AI Content Detector (/ai-blog-detector/) |
| /spam-score-checker/, /ssl-checker/ | Menu | Remove from menu until built |
| /tools/ai-blog-generator.html | Footer | Change to /ai-blog-generator/ |
| /blog/ | "Blog" in menu and footer | Create a blog page (Settings → Reading → Posts page), or hide until the first post is live |
| /services | Footer "Services" | Create a services page, or point it to /content-marketing/ |
| Privacy Policy, Terms of Service | Footer | See Part 1 |

Pages that **do** work: /web-design/, /content-marketing/, /social-media-marketing/, /resources/, /tools/, /about/, /contact/ and these 14 tools: AI Blog Generator, AI Content Detector, AI Paraphraser, Readability Checker, Headline Analyzer, Word Counter, Domain Checker, AI Caption Generator, AI Email Writer, Email Signature Generator, Hashtag Generator, Instagram Bio Generator, Twitter/X Character Count, YouTube Title & Tag Generator.

## Part 3: One clear identity (the biggest content problem)

The homepage presents a UK software agency ("we", "team", AI, PHP, APIs). The About page, Editorial Policy and all the blog content present an SEO specialist's blog ("I", Zubair Ahmad, SEO and content). The services menu is split the same way: the working service pages are Web Design, Content Marketing and Social Media Marketing, while the AI, PHP and API pages don't exist.

Google's quality guidelines put a lot of weight on "who is behind this site". Mixed messages lower trust. Pick one, then make every page match:

- **Recommended:** SEO, content and web, led by Zubair Ahmad, with free tools and guides. This matches your real results, your About page, your working service pages and all 11 articles.
- AI/PHP/API development can stay as extra services, but only once their pages exist.

## Part 4: Section-by-section edits (with new text)

### Hero

- **Badge:** "UK SEO & Digital Marketing · Since 2020"
- **H1 (keep it short):** "SEO, content and web design that grow your traffic"
- **Subheading:** "I'm Zubair Ahmad. I help businesses rank on Google with topical SEO, content that answers real questions and fast, clean websites, and I share what works in free guides and tools."
- **Buttons:** "Get a Free Quote" (→ /contact/) and "Explore Free Tools" (→ /tools/). Use one quote wording site-wide: the header says "Get A Quote", the hero says "Start A Project"; pick one.
- **Stats row:** replace with real, checkable numbers, e.g. "1.1M+ impressions in 6 months (Project A)", "6 years in SEO", "14 free tools".
- **Right-hand dashboard:** replace with a real (anonymised) Search Console growth screenshot from Project A or B. That is proof; the current graphic is decoration.

### "What We Build" section

- The subheading repeats the hero text word for word. Replace it with: "Services built around one goal: more of the right visitors, turning into customers."
- Cards: show the services whose pages work: **SEO** (create page), **Content Marketing** (/content-marketing/), **Web Design** (/web-design/), **Social Media Marketing** (/social-media-marketing/). Add AI Solutions back when its page is live.
- The H2 "Digital solutions that actually ship" is used twice on the page (here and in the About section). Keep it in one place only.

### Free Tools section

- Heading is good. Change "15+" to "14" and "built and maintained by the BrightlyFuture team" to "built and tested by Zubair at BrightlyFuture" (or keep "team" if others help).
- **Featured tool card (AI Blog Generator):** the chips don't match the tool.
  - "6 tone options" → the tool has 4 tones (Friendly, Professional, Expert, Casual).
  - "Meta description" → it doesn't write one. Remove.
  - Keep: Keyword targeting, FAQ generation, Markdown export, No sign-up. Add: "UK or US English", "No made-up facts".
  - Text: "Get a structured first draft with question-style headings and an FAQ. It won't invent facts; it marks where yours should go."
- **Side cards:** replace Blog Analyzer, JSON Validator and Password Generator (all 404) with Readability Checker, Headline Analyzer and AI Content Detector.

### About section

- Replace "Founded in 2020 … grew into a small, focused team … We don't produce slide decks" with: "BrightlyFuture started in 2020. I apply every SEO strategy on real websites before I recommend it, and I publish the results, including what didn't work." (Adjust if you do have a team.)
- Stats: same rule as the hero. Use real numbers or remove.
- "Our Story" button → /about/.

### "Every service, end to end" section

- All three cards are labelled "SERVICE 1". Change to 1, 2 and 3, or remove the labels.
- The same H2 appears twice on the page (checked in the HTML). Remove the duplicate.
- If you keep AI & Machine Learning, PHP & Laravel and API Development here, their pages must exist. Otherwise swap them for SEO, Content Marketing and Web Design.

### Testimonials section

See Part 1. Replace with real results: three cards for Project A, B and C, each with the headline number, a one-line lesson and a link to the About page.

## Part 5: New sections to add

1. **Latest guides:** once articles are published, show the 3 newest posts. Start with the pillar "AI Content Writing: The Complete Guide for 2026". This gives the homepage fresh links to your content.
2. **Meet the founder:** photo, name, "SEO Specialist, 6 years", two lines and a link to /about/ and /author/zubair-ahmad/. This is the strongest E-E-A-T signal on a small site.
3. **Trust links in the footer:** About, Editorial Policy, Contact, Privacy Policy, Terms.
4. **Contact details in the footer:** admin@brightlyfuture.co.uk and +44 7458 931560, as on the Contact page.

## Part 6: SEO settings for the homepage

- **Title tag** (currently "Home - BrightlyFuture", which wastes the most important title on the site): "BrightlyFuture: SEO, Content & Web Design + Free Tools"
- **Meta description** (currently copies the agency tagline): "SEO, content marketing and web design from Zubair Ahmad, plus free tools and tested guides. See real Search Console results and get a free quote." (145 characters)
- **H1:** keep one H1 only (the hero). It currently is one; keep it that way after editing.
- **Schema:** add Organization (or Person) schema with name, logo, email, phone and social profiles. If you keep "Ltd", include the legal name.
- **Images:** give the logo and hero image descriptive alt text, e.g. "BrightlyFuture logo" and "Search Console growth chart for Project A".

## Quick checklist

- [ ] Real or removed testimonials
- [ ] Footer: Ltd details corrected, © 2026
- [ ] Privacy Policy and Terms pages created
- [ ] 120+ / 98% / 15+ / 5yr fixed or removed
- [ ] All 404 links fixed (services, tools, blog, footer)
- [ ] One identity: "I" and SEO/content focus, matching About
- [ ] Featured tool chips corrected
- [ ] Duplicate H2s and "SERVICE 1" labels fixed
- [ ] Founder and latest-guides sections added
- [ ] Homepage title and meta description updated
