"""Competitor + keyword research for one workout plan.

python3 research.py <slug> "<seed keyword>" url1 url2 ... url7
Writes research/<slug>.json (raw) — report.py turns it into markdown + xlsx.
Page HTML is treated as untrusted data: parsed for text only.
"""
import json, re, sys, time, html, subprocess, urllib.parse, collections, pathlib

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
STOP = set("""a an the and or of to for in on at by with from your you is are be this that these those it its as into how what why when which who best top
can do does will my our we i vs than more most get make one two three four five six seven eight nine ten use using about over up out all any not
""".split())

def fetch(url):
    r = subprocess.run(["curl", "-sSL", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", url], capture_output=True)
    return r.stdout.decode("utf-8", "replace")

def clean(t): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()

def parse(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header|form|aside)[^>]*>.*?</\1>", " ", raw)
    title = clean((re.search(r"(?is)<title[^>]*>(.*?)</title>", raw) or [None, ""])[1])
    heads = [(int(m.group(1)), clean(m.group(2))) for m in re.finditer(r"(?is)<h([1-4])[^>]*>(.*?)</h\1>", raw)]
    heads = [(l, h) for l, h in heads if 2 < len(h) < 160]
    main = re.search(r"(?is)<(article|main)[^>]*>(.*)</\1>", raw)
    body = clean(main.group(2) if main else raw)
    return title, heads, body

def ngrams(words, n):
    for i in range(len(words) - n + 1):
        g = words[i:i + n]
        if g[0] in STOP or g[-1] in STOP: continue
        if any(len(w) < 2 for w in g): continue
        yield " ".join(g)

def tokens(t): return re.findall(r"[a-z0-9][a-z0-9'\-]*", t.lower())

def suggest(q):
    out = []
    for url in (f"https://suggestqueries.google.com/complete/search?client=firefox&q={urllib.parse.quote(q)}",
                f"https://api.bing.com/osjson.aspx?query={urllib.parse.quote(q)}"):
        try:
            d = json.loads(fetch(url)); out += d[1]
        except Exception: pass
        time.sleep(0.3)
    return out

def main():
    slug, seed, urls = sys.argv[1], sys.argv[2], sys.argv[3:]
    comps = []
    for u in urls:
        raw = fetch(u)
        title, heads, body = parse(raw)
        words = len(body.split())
        faqs = [h for _, h in heads if h.endswith("?")]
        comps.append({"url": u, "title": title, "headings": heads, "words": words, "faqs": faqs, "body": body[:60000]})
        print(f"{u[:70]:<72} words={words:<6} headings={len(heads)}", file=sys.stderr)
        time.sleep(1)
    # keyword phrases appearing in >=2 competitors (title+headings weighted, body included)
    per = []
    for c in comps:
        txt = c["title"] + " . " + " . ".join(h for _, h in c["headings"]) + " . " + c["body"]
        tk = tokens(txt); s = set()
        for n in range(1, 7): s |= set(ngrams(tk, n))
        per.append(s)
    cnt = collections.Counter(p for s in per for p in s)
    seedw = set(tokens(seed))
    rel = [p for p, k in cnt.items() if k >= 2 and (set(p.split()) & seedw or len(p.split()) >= 3)]
    # heading phrases (exact) across competitors
    headphr = collections.Counter()
    for c in comps:
        for _, h in c["headings"]:
            headphr[h.lower()] += 1
    # autocomplete expansion
    mods = ["", " for beginners", " at home", " for men", " for women", " with dumbbells", " plan", " routine", " exercises", " how", " best", " vs", " gym", " mass", " upper", " lower", " without", " days", " sets and reps"]
    ac = collections.OrderedDict()
    for m in mods:
        for s in suggest(seed + m): ac[s.lower()] = 1
    for ch in "abcdefghijklmnopqrstuvwxyz":
        for s in suggest(f"{seed} {ch}"): ac[s.lower()] = 1
    json.dump({"slug": slug, "seed": seed, "competitors": comps, "phrases": {p: cnt[p] for p in rel},
               "autocomplete": list(ac)}, open(f"research/{slug}.json", "w"))
    print("phrases", len(rel), "autocomplete", len(ac), file=sys.stderr)

if __name__ == "__main__":
    main()
