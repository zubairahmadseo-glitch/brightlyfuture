"""Outreach Tool: find articles on added sites, extract & verify external links,
collect emails from linked websites, and send templated outreach via Gmail."""
import re
import smtplib
import sqlite3
import threading
import time
from datetime import datetime, date
from email.mime.text import MIMEText
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from dateutil import parser as dparser
from flask import Flask, redirect, render_template_string, request, url_for, flash

DB = "outreach.db"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
BAD_EMAIL_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".css", ".js")
BAD_EMAIL_PARTS = ("example.com", "sentry", "wixpress", "domain.com", "email.com", "yourname")
CONTACT_PATHS = ["", "/contact", "/contact-us", "/about", "/about-us",
                 "/write-for-us", "/advertise", "/contribute"]
DEFAULT_BLOCKS = ["facebook.com", "twitter.com", "x.com", "instagram.com", "youtube.com",
                  "linkedin.com", "pinterest.com", "tiktok.com", "amazon.com", "wikipedia.org",
                  "google.com", "apple.com", "reddit.com", "t.co", "bit.ly", "ncbi.nlm.nih.gov",
                  "pubmed.ncbi.nlm.nih.gov", "doi.org", "whatsapp.com", "flipboard.com"]
DEFAULT_SUBJECT = "Guest Post & Link Insertion Pricing Please"
DEFAULT_BODY = """Hello,

I'm interested in publishing in {site_name}

Could you please share your current pricing for:

  • Guest post publication
  • Link insertion in an existing article

Please also let me know if there are any specific guidelines or requirements.

Looking forward to your reply.

Thanks!
{my_website}"""

app = Flask(__name__)
app.secret_key = "outreach-local"
JOB = {"running": False, "log": []}


# ---------------- DB ----------------
def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    con = db()
    con.executescript("""
    CREATE TABLE IF NOT EXISTS sites(id INTEGER PRIMARY KEY, url TEXT UNIQUE);
    CREATE TABLE IF NOT EXISTS blocks(id INTEGER PRIMARY KEY, domain TEXT UNIQUE);
    CREATE TABLE IF NOT EXISTS articles(id INTEGER PRIMARY KEY, site TEXT, url TEXT UNIQUE,
        title TEXT, published TEXT);
    CREATE TABLE IF NOT EXISTS prospects(id INTEGER PRIMARY KEY, domain TEXT UNIQUE,
        link TEXT, status_code INTEGER, article_url TEXT, article_title TEXT, source_site TEXT,
        emails TEXT DEFAULT '', selected_email TEXT DEFAULT '', subject TEXT DEFAULT '',
        body TEXT DEFAULT '', state TEXT DEFAULT 'new', sent_at TEXT);
    CREATE TABLE IF NOT EXISTS settings(k TEXT PRIMARY KEY, v TEXT);
    """)
    if not con.execute("SELECT 1 FROM blocks").fetchone():
        con.executemany("INSERT OR IGNORE INTO blocks(domain) VALUES(?)", [(d,) for d in DEFAULT_BLOCKS])
    for k, v in {"subject": DEFAULT_SUBJECT, "body": DEFAULT_BODY, "gmail": "", "app_password": "",
                 "my_name": "", "my_website": "https://www.nutriavenue.com/", "delay": "20"}.items():
        con.execute("INSERT OR IGNORE INTO settings VALUES(?,?)", (k, v))
    con.commit()
    con.close()


def setting(k):
    con = db()
    r = con.execute("SELECT v FROM settings WHERE k=?", (k,)).fetchone()
    con.close()
    return r["v"] if r else ""


def log(msg):
    JOB["log"].append(f"[{datetime.now():%H:%M:%S}] {msg}")
    JOB["log"] = JOB["log"][-300:]


# ---------------- helpers ----------------
def domain_of(url):
    d = urlparse(url).netloc.lower().split(":")[0]
    return d[4:] if d.startswith("www.") else d


def is_blocked(dom, blocks):
    return any(dom == b or dom.endswith("." + b) for b in blocks)


def fetch(url, timeout=15):
    try:
        return requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
    except requests.RequestException:
        return None


def norm_site(url):
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def parse_date(s):
    try:
        return dparser.parse(s).date()
    except Exception:
        return None


# ---------------- article discovery ----------------
def sitemap_articles(site, d_from, d_to, limit=200):
    """Walk sitemap(s) and return [(url, lastmod)] in date range."""
    candidates = []
    r = fetch(site + "/robots.txt")
    if r is not None and r.ok:
        candidates += re.findall(r"(?im)^sitemap:\s*(\S+)", r.text)
    candidates += [site + "/sitemap_index.xml", site + "/sitemap.xml", site + "/post-sitemap.xml"]
    seen, out, queue = set(), [], list(dict.fromkeys(candidates))
    while queue and len(seen) < 60 and len(out) < limit:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        r = fetch(sm)
        if r is None or not r.ok or "<" not in r.text[:500]:
            continue
        try:
            root = ET.fromstring(r.content)
        except ET.ParseError:
            continue
        tag = root.tag.split("}")[-1]
        for node in root:
            loc = lastmod = None
            for c in node:
                n = c.tag.split("}")[-1]
                if n == "loc":
                    loc = (c.text or "").strip()
                elif n == "lastmod":
                    lastmod = (c.text or "").strip()
            if not loc:
                continue
            if tag == "sitemapindex":
                lm = parse_date(lastmod) if lastmod else None
                name = loc.lower()
                if any(x in name for x in ("page-sitemap", "category", "tag-sitemap", "author", "image", "video")):
                    continue
                if lm is None or lm >= d_from:  # child sitemap may contain range
                    queue.append(loc)
            else:
                lm = parse_date(lastmod) if lastmod else None
                if lm and d_from <= lm <= d_to:
                    out.append((loc, lm.isoformat()))
    return out[:limit]


def rss_articles(site, d_from, d_to):
    out = []
    for feed in (site + "/feed", site + "/rss", site + "/feed.xml", site + "/rss.xml"):
        r = fetch(feed)
        if r is None or not r.ok:
            continue
        soup = BeautifulSoup(r.content, "xml")
        for it in soup.find_all(["item", "entry"]):
            link = it.find("link")
            href = (link.get("href") or link.text).strip() if link else ""
            pd = it.find(["pubDate", "published", "updated"])
            d = parse_date(pd.text) if pd else None
            if href and d and d_from <= d <= d_to:
                out.append((href, d.isoformat()))
        if out:
            break
    return out


def extract_external_links(article_url, site_dom):
    r = fetch(article_url)
    if r is None or not r.ok:
        return "", []
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.text.strip() if soup.title else article_url
    body = soup.find("article") or soup.find(class_=re.compile(r"entry-content|article-body|post-content|content")) or soup
    for bad in body.find_all(["nav", "header", "footer", "aside"]):
        bad.decompose()
    links = []
    for a in body.find_all("a", href=True):
        href = urljoin(article_url, a["href"].strip())
        if not href.startswith("http"):
            continue
        dom = domain_of(href)
        if dom and dom != site_dom and not dom.endswith("." + site_dom):
            links.append(href)
    return title, list(dict.fromkeys(links))


def verify_link(url):
    try:
        r = requests.head(url, headers=UA, timeout=10, allow_redirects=True)
        if r.status_code in (403, 405) or r.status_code >= 400:
            r = requests.get(url, headers=UA, timeout=12, allow_redirects=True, stream=True)
        return r.status_code
    except requests.RequestException:
        return 0


def find_emails(dom):
    found = []
    base = f"https://{dom}"
    for path in CONTACT_PATHS:
        r = fetch(base + path, timeout=12)
        if r is None or not r.ok:
            continue
        text = r.text
        soup = BeautifulSoup(text, "html.parser")
        for a in soup.select('a[href^="mailto:"]'):
            found.append(a["href"][7:].split("?")[0])
        found += EMAIL_RE.findall(text.replace("[at]", "@").replace("(at)", "@"))
        if len(set(found)) >= 3:
            break
    clean = []
    for e in found:
        e = e.strip().strip(".").lower()
        if e.endswith(BAD_EMAIL_EXT) or any(b in e for b in BAD_EMAIL_PARTS) or len(e) > 60:
            continue
        clean.append(e)
    clean = list(dict.fromkeys(clean))
    own = [e for e in clean if e.split("@")[-1].endswith(dom.split(".")[-2] + "." + dom.split(".")[-1])] if "." in dom else []
    return own + [e for e in clean if e not in own]


def render_tpl(text, p):
    vals = {"domain": p["domain"], "site_name": p["domain"].split(".")[0].capitalize() + "." + ".".join(p["domain"].split(".")[1:]),
            "article_url": p["article_url"] or "", "article_title": p["article_title"] or "",
            "source_site": p["source_site"] or "", "my_website": setting("my_website"), "my_name": setting("my_name")}
    for k, v in vals.items():
        text = text.replace("{" + k + "}", v)
    return text


# ---------------- background job ----------------
def run_scan(site_ids, d_from, d_to, max_articles, verify, collect):
    JOB["running"] = True
    try:
        con = db()
        blocks = [r["domain"] for r in con.execute("SELECT domain FROM blocks")]
        q = "SELECT * FROM sites" + (f" WHERE id IN ({','.join('?' * len(site_ids))})" if site_ids else "")
        sites = con.execute(q, site_ids).fetchall()
        for s in sites:
            site = s["url"]
            sdom = domain_of(site)
            log(f"Scanning {site} ({d_from} → {d_to})")
            arts = sitemap_articles(site, d_from, d_to) or rss_articles(site, d_from, d_to)
            arts = sorted(arts, key=lambda x: x[1], reverse=True)[:max_articles]
            log(f"  {len(arts)} articles found")
            for url, pub in arts:
                title, links = extract_external_links(url, sdom)
                con.execute("INSERT OR IGNORE INTO articles(site,url,title,published) VALUES(?,?,?,?)",
                            (site, url, title, pub))
                for link in links:
                    dom = domain_of(link)
                    if is_blocked(dom, blocks):
                        continue
                    if con.execute("SELECT 1 FROM prospects WHERE domain=?", (dom,)).fetchone():
                        continue
                    code = verify_link(link) if verify else None
                    if verify and not (200 <= (code or 0) < 400):
                        log(f"  ✗ {link} broken ({code})")
                        continue
                    emails = find_emails(dom) if collect else []
                    state = "ready" if emails else "no_email"
                    con.execute("""INSERT OR IGNORE INTO prospects(domain,link,status_code,article_url,
                        article_title,source_site,emails,selected_email,state) VALUES(?,?,?,?,?,?,?,?,?)""",
                                (dom, link, code, url, title, site, ",".join(emails),
                                 emails[0] if emails else "", state))
                    con.commit()
                    log(f"  ✓ {dom} → {', '.join(emails) or 'no email'}")
        con.close()
        log("Scan finished.")
    except Exception as e:
        log(f"ERROR: {e}")
    finally:
        JOB["running"] = False


def send_mail(to, subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"], msg["From"], msg["To"] = subject, setting("gmail"), to
    if setting("my_name"):
        msg["From"] = f'{setting("my_name")} <{setting("gmail")}>'
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as s:
        s.login(setting("gmail"), setting("app_password").replace(" ", ""))
        s.sendmail(setting("gmail"), [to], msg.as_string())


def run_send(ids):
    JOB["running"] = True
    try:
        delay = int(setting("delay") or 20)
        con = db()
        for i, pid in enumerate(ids):
            p = con.execute("SELECT * FROM prospects WHERE id=?", (pid,)).fetchone()
            if not p or not p["selected_email"] or p["state"] == "sent":
                continue
            subject = p["subject"] or render_tpl(setting("subject"), p)
            body = p["body"] or render_tpl(setting("body"), p)
            try:
                send_mail(p["selected_email"], subject, body)
                con.execute("UPDATE prospects SET state='sent', sent_at=? WHERE id=?",
                            (datetime.now().isoformat(timespec="seconds"), pid))
                con.commit()
                log(f"Sent → {p['selected_email']}")
            except Exception as e:
                con.execute("UPDATE prospects SET state='failed' WHERE id=?", (pid,))
                con.commit()
                log(f"FAILED → {p['selected_email']}: {e}")
            if i < len(ids) - 1:
                time.sleep(delay)
        con.close()
        log("Sending finished.")
    finally:
        JOB["running"] = False


# ---------------- UI ----------------
BASE = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Outreach Tool</title><style>
body{font-family:system-ui,Arial;margin:0;background:#f4f6fb;color:#222}
nav{background:#1e3a8a;padding:12px 20px}nav a{color:#fff;margin-right:18px;text-decoration:none;font-weight:600}
main{max-width:1200px;margin:20px auto;padding:0 16px}.card{background:#fff;border-radius:10px;padding:18px;margin-bottom:18px;box-shadow:0 1px 3px #0002}
input,textarea,select{padding:8px;border:1px solid #ccc;border-radius:6px;font:inherit}textarea{width:100%;box-sizing:border-box}
button{background:#2563eb;color:#fff;border:0;padding:8px 14px;border-radius:6px;cursor:pointer}button.red{background:#dc2626}button.gray{background:#64748b}
table{width:100%;border-collapse:collapse;font-size:14px}td,th{padding:7px;border-bottom:1px solid #eee;text-align:left;vertical-align:top}
.tag{padding:2px 8px;border-radius:10px;font-size:12px;color:#fff}.ready{background:#16a34a}.sent{background:#2563eb}.no_email{background:#9ca3af}.failed{background:#dc2626}.new{background:#f59e0b}
pre{background:#0f172a;color:#cbd5e1;padding:10px;border-radius:8px;max-height:300px;overflow:auto;font-size:12px}
.flash{background:#dcfce7;padding:10px;border-radius:6px;margin-bottom:12px}.wrap{word-break:break-all}
</style></head><body><nav><a href="/">Websites & Scan</a><a href="/prospects">Prospects / Drafts</a>
<a href="/template">Email Template</a><a href="/blocks">Blocked Domains</a><a href="/settings">Settings</a></nav><main>
{% for m in get_flashed_messages() %}<div class=flash>{{m}}</div>{% endfor %}{{ content|safe }}</main></body></html>"""


def page(tpl, **kw):
    return render_template_string(BASE, content=render_template_string(tpl, **kw))


@app.route("/", methods=["GET", "POST"])
def home():
    con = db()
    if request.method == "POST":
        for line in request.form["urls"].splitlines():
            if line.strip():
                con.execute("INSERT OR IGNORE INTO sites(url) VALUES(?)", (norm_site(line),))
        con.commit()
        return redirect("/")
    sites = con.execute("SELECT s.*, (SELECT COUNT(*) FROM articles a WHERE a.site=s.url) n FROM sites s").fetchall()
    con.close()
    today = date.today().isoformat()
    return page("""
<div class=card><h3>Add websites</h3><form method=post><textarea name=urls rows=3 placeholder="muscleandfitness.com&#10;menshealth.com (one per line)"></textarea><br><br><button>Add</button></form></div>
<div class=card><h3>Scan articles (date wise)</h3><form method=post action="/scan">
<table><tr><th></th><th>Website</th><th>Articles scanned</th><th></th></tr>
{% for s in sites %}<tr><td><input type=checkbox name=site value="{{s.id}}" checked></td><td>{{s.url}}</td><td>{{s.n}}</td>
<td><a href="/site/delete/{{s.id}}" onclick="return confirm('Delete?')">delete</a></td></tr>{% endfor %}</table><br>
From <input type=date name=d_from value="{{today}}"> To <input type=date name=d_to value="{{today}}">
Max articles/site <input type=number name=max value=20 style="width:70px">
<label><input type=checkbox name=verify checked> Verify links</label>
<label><input type=checkbox name=collect checked> Collect emails</label>
<button {{'disabled' if running}}>Start scan</button></form></div>
<div class=card><h3>Activity log {{'(running…)' if running}}</h3><pre id=log>{{log}}</pre></div>
{% if running %}<script>setTimeout(()=>location.reload(),4000)</script>{% endif %}""",
                sites=sites, today=today, running=JOB["running"], log="\n".join(JOB["log"][-80:]))


@app.route("/site/delete/<int:i>")
def site_delete(i):
    con = db(); con.execute("DELETE FROM sites WHERE id=?", (i,)); con.commit(); con.close()
    return redirect("/")


@app.route("/scan", methods=["POST"])
def scan():
    if JOB["running"]:
        flash("A job is already running."); return redirect("/")
    ids = [int(x) for x in request.form.getlist("site")]
    d_from = date.fromisoformat(request.form["d_from"]); d_to = date.fromisoformat(request.form["d_to"])
    threading.Thread(target=run_scan, daemon=True, args=(ids, d_from, d_to, int(request.form.get("max", 20)),
                     "verify" in request.form, "collect" in request.form)).start()
    flash("Scan started — log neeche update hota rahega.")
    return redirect("/")


@app.route("/prospects")
def prospects():
    st = request.args.get("state", "")
    con = db()
    rows = con.execute("SELECT * FROM prospects" + (" WHERE state=?" if st else "") + " ORDER BY id DESC",
                       (st,) if st else ()).fetchall()
    con.close()
    return page("""
<div class=card><h3>Prospects ({{rows|length}})</h3>
Filter: <a href="?">all</a> · <a href="?state=ready">ready</a> · <a href="?state=no_email">no email</a> · <a href="?state=sent">sent</a> · <a href="?state=failed">failed</a>
<form method=post action="/send"><table><tr><th><input type=checkbox onclick="document.querySelectorAll('.ck').forEach(c=>c.checked=this.checked)"></th>
<th>Domain</th><th>Email</th><th>Found in article</th><th>Status</th><th></th></tr>
{% for p in rows %}<tr><td>{% if p.selected_email and p.state!='sent' %}<input class=ck type=checkbox name=id value="{{p.id}}">{% endif %}</td>
<td><a href="https://{{p.domain}}" target=_blank>{{p.domain}}</a><br><small class=wrap>{{p.link}} ({{p.status_code}})</small></td>
<td>{{p.selected_email or '-'}}<br><small>{{p.emails}}</small></td>
<td><small><a href="{{p.article_url}}" target=_blank>{{p.article_title[:70]}}</a></small></td>
<td><span class="tag {{p.state}}">{{p.state}}</span></td>
<td><a href="/draft/{{p.id}}">draft / edit</a> · <a href="/prospect/delete/{{p.id}}">del</a></td></tr>{% endfor %}</table><br>
<button onclick="return confirm('Send to selected?')">Send selected</button> <small>Running: {{running}}</small></form></div>
<div class=card><pre>{{log}}</pre></div>""", rows=rows, running=JOB["running"], log="\n".join(JOB["log"][-30:]))


@app.route("/prospect/delete/<int:i>")
def prospect_delete(i):
    con = db(); con.execute("DELETE FROM prospects WHERE id=?", (i,)); con.commit(); con.close()
    return redirect(request.referrer or "/prospects")


@app.route("/draft/<int:i>", methods=["GET", "POST"])
def draft(i):
    con = db()
    if request.method == "POST":
        f = request.form
        con.execute("UPDATE prospects SET selected_email=?, subject=?, body=?, state=CASE WHEN state='sent' THEN state WHEN ?<>'' THEN 'ready' ELSE 'no_email' END WHERE id=?",
                    (f["email"].strip(), f["subject"], f["body"], f["email"].strip(), i))
        con.commit()
        if f.get("action") == "send":
            con.close()
            threading.Thread(target=run_send, args=([i],), daemon=True).start()
            flash("Sending…"); return redirect("/prospects")
        flash("Draft saved.")
    p = con.execute("SELECT * FROM prospects WHERE id=?", (i,)).fetchone()
    con.close()
    subject = p["subject"] or render_tpl(setting("subject"), p)
    body = p["body"] or render_tpl(setting("body"), p)
    return page("""<div class=card><h3>Draft for {{p.domain}}</h3><form method=post>
To: <input name=email value="{{p.selected_email}}" style="width:300px" list=em><datalist id=em>{% for e in p.emails.split(',') %}<option>{{e}}{% endfor %}</datalist><br><br>
Subject:<br><input name=subject value="{{subject}}" style="width:100%"><br><br>
Body:<br><textarea name=body rows=16>{{body}}</textarea><br><br>
<button name=action value=save class=gray>Save draft</button> <button name=action value=send>Send now</button></form></div>""",
                p=p, subject=subject, body=body)


@app.route("/send", methods=["POST"])
def send():
    ids = [int(x) for x in request.form.getlist("id")]
    if not setting("gmail") or not setting("app_password"):
        flash("Pehle Settings me Gmail + App Password daalein."); return redirect("/settings")
    if JOB["running"]:
        flash("A job is already running."); return redirect("/prospects")
    threading.Thread(target=run_send, args=(ids,), daemon=True).start()
    flash(f"Sending {len(ids)} emails in background…")
    return redirect("/prospects")


@app.route("/template", methods=["GET", "POST"])
def template():
    con = db()
    if request.method == "POST":
        con.execute("UPDATE settings SET v=? WHERE k='subject'", (request.form["subject"],))
        con.execute("UPDATE settings SET v=? WHERE k='body'", (request.form["body"],))
        if "reset" in request.form:
            con.execute("UPDATE prospects SET subject='', body='' WHERE state!='sent'")
        con.commit(); flash("Template saved.")
    con.close()
    return page("""<div class=card><h3>Email template</h3>
<p>Placeholders: <code>{domain} {site_name} {article_url} {article_title} {source_site} {my_website} {my_name}</code></p>
<form method=post>Subject:<br><input name=subject value="{{s}}" style="width:100%"><br><br>
Body:<br><textarea name=body rows=18>{{b}}</textarea><br>
<label><input type=checkbox name=reset checked> Apply to all unsent drafts (custom edits reset)</label><br><br><button>Save template</button></form></div>""",
                s=setting("subject"), b=setting("body"))


@app.route("/blocks", methods=["GET", "POST"])
def blocks():
    con = db()
    if request.method == "POST":
        for line in request.form["domains"].splitlines():
            if line.strip():
                con.execute("INSERT OR IGNORE INTO blocks(domain) VALUES(?)", (domain_of(norm_site(line)),))
        con.commit()
    rows = con.execute("SELECT * FROM blocks ORDER BY domain").fetchall(); con.close()
    return page("""<div class=card><h3>Blocked domains</h3><p>In domains (aur unke subdomains) ki emails find nahi hongi.</p>
<form method=post><textarea name=domains rows=3 placeholder="amazon.com&#10;healthline.com"></textarea><br><br><button>Add</button></form><br>
{% for b in rows %}<span style="display:inline-block;background:#e2e8f0;padding:4px 10px;border-radius:12px;margin:3px">{{b.domain}} <a href="/blocks/delete/{{b.id}}">✕</a></span>{% endfor %}</div>""", rows=rows)


@app.route("/blocks/delete/<int:i>")
def block_delete(i):
    con = db(); con.execute("DELETE FROM blocks WHERE id=?", (i,)); con.commit(); con.close()
    return redirect("/blocks")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    keys = ["gmail", "app_password", "my_name", "my_website", "delay"]
    if request.method == "POST":
        con = db()
        for k in keys:
            con.execute("UPDATE settings SET v=? WHERE k=?", (request.form.get(k, ""), k))
        con.commit(); con.close()
        if "test" in request.form:
            try:
                send_mail(setting("gmail"), "Outreach tool test", "Test email works ✅")
                flash("Test email sent to yourself.")
            except Exception as e:
                flash(f"Test failed: {e}")
        else:
            flash("Settings saved.")
    vals = {k: setting(k) for k in keys}
    return page("""<div class=card><h3>Settings</h3><form method=post>
Gmail address<br><input name=gmail value="{{v.gmail}}" style="width:320px"><br><br>
Gmail App Password (<a href="https://myaccount.google.com/apppasswords" target=_blank>generate</a>)<br><input type=password name=app_password value="{{v.app_password}}" style="width:320px"><br><br>
Your name<br><input name=my_name value="{{v.my_name}}" style="width:320px"><br><br>
Your website<br><input name=my_website value="{{v.my_website}}" style="width:320px"><br><br>
Delay between emails (seconds)<br><input type=number name=delay value="{{v.delay}}"><br><br>
<button>Save</button> <button name=test value=1 class=gray>Save & send test email to myself</button></form></div>""", v=vals)


if __name__ == "__main__":
    init_db()
    app.run(debug=False, port=5000)
