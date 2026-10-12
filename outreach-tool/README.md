# Outreach Tool (Link Prospecting + Email Outreach)

## Kya karta hai
1. **Websites add karein** (e.g. muscleandfitness.com)
2. **Date range select karein** → tool sitemap/RSS se us date ke articles nikalta hai
3. Har article ke **external links** nikal kar **verify** karta hai (HTTP status check)
4. **Blocked domains** (facebook, amazon, wikipedia, ya jo aap add karein) skip hote hain
5. External websites ke homepage + contact/about/write-for-us pages se **emails collect** karta hai
6. **Email template** edit/save karein (placeholders ke saath)
7. Har prospect ke liye **draft** banta hai → preview/edit → **Send** (Gmail SMTP)

## Setup
```bash
cd outreach-tool
pip install -r requirements.txt
python app.py
```
Browser me kholein: http://127.0.0.1:5000

## Gmail setup
Gmail normal password se SMTP allow nahi karta. **App Password** banayein:
1. Google Account → Security → 2-Step Verification ON karein
2. https://myaccount.google.com/apppasswords → app password generate karein (16 characters)
3. Tool me **Settings** page par apni Gmail aur App Password daalein

## Template placeholders
`{domain}` `{site_name}` `{article_url}` `{article_title}` `{source_site}` `{my_website}` `{my_name}`

## Tips
- Gmail ki daily sending limit (~500/din normal account) ka khayal rakhein; Settings me delay set karein.
- Pehle "Test email" apne aap ko bhejein.
