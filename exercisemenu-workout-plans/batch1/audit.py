"""Audit helpers: session-time estimate, exercise counts, FAQ/body overlap, AI-style phrase scan."""
import importlib, re, sys, pathlib
sys.path.insert(0, ".")
from build import PAGES

def rest_sec(r):
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", r)]
    if not nums: return 60
    m = sum(nums) / len(nums)
    return m * 60 if "min" in r else m

def sets_of(s):
    m = re.match(r"\s*(\d+)", s); return int(m.group(1)) if m else 0

def day_minutes(d):
    t = 10 * 60  # general warm-up
    for i, (name, _, sets, rest, _) in enumerate(d["exercises"]):
        n = sets_of(sets)
        work = 45 * (2 if "/ leg" in sets or "/ side" in sets else 1)
        t += n * work + (n - 1) * rest_sec(rest) + 90  # 90 s setup/transition per exercise
        if i == 0: t += 4 * 60  # ramp-up sets on first lift
    return t / 60

AI = [r"\bthe catch\b", r"sweet spot", r"here's", r"the takeaway", r"honest", r"that's (a good thing|expected)", r"exactly its job",
      r"not only", r"get those right", r"one goal", r"serves that", r"no magic|not magic|isn't magic", r"—", r"the answer for",
      r"in practice", r"the key word", r"simple:", r"is simple", r"it's not about", r"rather than", r"whether"]

def words(t): return set(re.findall(r"[a-z]{4,}", t.lower()))

for m in PAGES:
    p = importlib.import_module("content." + m).PAGE
    print(f"\n===== #{p['num']} {p['slug']}")
    names = [e[0] for d in p["days"] for e in d["exercises"]]
    print(f"exercise entries={len(names)} unique={len(set(names))} stats={[s for s in p['stats'] if 'xercise' in s[1]]}")
    for d in p["days"]:
        print(f"  {d['title']:<40} stated {d['time']:<10} est {day_minutes(d):.0f} min")
    body = " ".join(s[2] for s in p["sections"]) + p["intro"]
    body = re.sub(r"<[^>]+>", " ", body)
    for q, a in p["faqs"]:
        a_txt = re.sub(r"<[^>]+>", " ", a)
        # longest shared 6-word sequence
        aw = a_txt.lower().split(); bw = " ".join(body.lower().split())
        hits = [" ".join(aw[i:i+5]) for i in range(len(aw)-4) if " ".join(aw[i:i+5]) in bw]
        print(f"  FAQ: {q[:60]:<62} shared5grams={len(hits)}")
    text = body + " ".join(a for _, a in p["faqs"])
    for pat in AI:
        c = len(re.findall(pat, text, re.I))
        if c: print(f"  AI-ish '{pat}': {c}")
