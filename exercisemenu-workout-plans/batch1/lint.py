"""Checks: meta lengths, quick answer limits, banned phrases, links (internal vs sitemap, external 200)."""
import importlib, json, pathlib, re, subprocess, sys
sys.path.insert(0, ".")
from build import PAGES
BANNED = ["in this article we will", "without further ado", "we hope you found", "there are many types", "great question",
          "absolutely", "certainly", "as an ai", "straightforward", "dive in", "dive into", "game changer", "game-changer", "it's worth noting",
          "significantly", "transform", "in today's world", "it's important to note", "whether you're a beginner or advanced",
          "let's dive", "in conclusion", "very", "really", "actually", "basically", "essentially", "incredibly", "many people struggle", "it depends"]
live = set(pathlib.Path(sys.argv[1]).read_text().split()) if len(sys.argv) > 1 else None
allowed_extra = {"/workout-plans/" + s + "/" for s in __import__("build").PLANS} | {"/exercises/barbell-bench-press/", "/exercises/barbell-curl/", "/exercises/barbell-incline-bench-press/", "/exercises/dumbbell-bench-press/", "/exercises/dumbbell-biceps-curl/", "/exercises/dumbbell-hammer-curl/"}
ext_all = set()
for m in [m for m in PAGES if pathlib.Path("content", m + ".py").exists()]:
    p = importlib.import_module("content." + m).PAGE
    html = pathlib.Path("out", p["slug"] + ".html").read_text()
    text = re.sub(r"<style.*?</style>|<script.*?</script>", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    words = len(re.findall(r"[A-Za-z0-9’'–-]+", text))
    qa = re.sub(r"<[^>]+>", "", p["quick_answer"])
    probs = []
    if len(p["meta_title"]) > 60: probs.append(f"meta_title {len(p['meta_title'])}")
    if len(p["meta_desc"]) > 155: probs.append(f"meta_desc {len(p['meta_desc'])}")
    if len(qa.split()) >= 60 or len(qa) >= 320: probs.append(f"quick answer {len(qa.split())}w/{len(qa)}c")
    if p["focus_kw"].lower() not in (p["meta_desc"] + p["title"]).lower(): probs.append("focus kw missing in title/desc")
    uniq = len({e[0] for d in p["days"] for e in d["exercises"]})
    for v, lab in p["stats"]:
        if "xercise" in lab and v != str(uniq): probs.append(f"exercise stat {v} != {uniq}")
    if re.search(r"\{(L|cite|box|table)\(|\{\{(WEEK|TABS)\}\}", html): probs.append("UNRENDERED TEMPLATE CODE")
    low = " " + text.lower() + " "
    for b in BANNED:
        if re.search(r"\b" + re.escape(b) + r"\b", low): probs.append("banned:" + b)
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith("#"): continue
        if href.startswith("https://exercisemenu.com"):
            path = href[len("https://exercisemenu.com"):]
            if path not in allowed_extra and (live is not None and path not in live): probs.append("NOT LIVE " + path)
        else: ext_all.add(href)
    print(f'#{p["num"]:>2} {p["slug"]:<38} words≈{words:<5} mt={len(p["meta_title"])} md={len(p["meta_desc"])} qa={len(qa.split())}w ' + ("OK" if not probs else "PROBLEMS: " + "; ".join(probs)))
pathlib.Path("ext_links.txt").write_text("\n".join(sorted(ext_all)) + "\n")
