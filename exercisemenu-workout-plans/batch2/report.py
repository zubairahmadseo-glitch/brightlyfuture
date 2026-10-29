"""Turn research/<slug>.json into research/<slug>.md and research/<slug>.xlsx.

python3 report.py <slug> "<topic words comma separated>" [extra_competitor_json]
Keywords are content-derived (competitor pages + Google/Bing autocomplete) — NOT volume-verified.
"""
import json, re, sys, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

ENTITIES = {
 "Exercises": ["bench press","incline bench press","decline bench press","dumbbell bench press","incline dumbbell press","dumbbell fly","cable fly","cable crossover","pec deck","machine chest press","push-up","dips","dumbbell pullover","svend press","landmine press","floor press","close-grip bench press",
   "barbell curl","dumbbell curl","hammer curl","preacher curl","incline dumbbell curl","concentration curl","cable curl","chin-up","skull crusher","triceps pushdown","overhead triceps extension","diamond push-up","bench dip","reverse curl","spider curl","bayesian curl","kickback",
   "plank","side plank","dead bug","bird dog","pallof press","hanging leg raise","ab wheel","cable crunch","russian twist","mountain climber","farmer's carry","suitcase carry","hollow hold","crunch","bicycle crunch","glute bridge",
   "hip thrust","glute bridge","romanian deadlift","bulgarian split squat","squat","sumo squat","step-up","cable kickback","hip abduction","lunge","reverse lunge","walking lunge","good morning","back extension","kettlebell swing","frog pump","deadlift",
   "back squat","front squat","leg press","hack squat","leg extension","leg curl","seated leg curl","lying leg curl","nordic curl","calf raise","seated calf raise","goblet squat","split squat"],
 "Muscles": ["pectoralis major","pectoralis minor","upper chest","lower chest","clavicular","sternal","serratus anterior","anterior deltoid","front delts","triceps","biceps","brachialis","brachioradialis","forearms","long head","short head","lateral head","medial head",
   "rectus abdominis","obliques","transverse abdominis","erector spinae","lower back","glutes","gluteus maximus","gluteus medius","gluteus minimus","hamstrings","quadriceps","quads","adductors","calves","hip flexors"],
 "Equipment": ["barbell","dumbbell","cable","machine","resistance band","kettlebell","bench","smith machine","ez bar","pull-up bar","medicine ball","stability ball","weight plate","dip station","squat rack","leg press machine"],
 "Training concepts": ["progressive overload","hypertrophy","sets and reps","rep range","rest periods","volume","frequency","range of motion","time under tension","mind-muscle connection","warm-up","failure","rpe","reps in reserve","deload","supersets","drop sets","compound","isolation","form","tempo","stretch","recovery","protein","muscle activation","emg"],
}

def load(slug): return json.load(open(f"research/{slug}.json"))

def classify(p):
    n = len(p.split())
    return "short" if n <= 2 else ("mid" if n <= 4 else "long")

def main():
    slug, topics = sys.argv[1], [t.strip() for t in sys.argv[2].split(",")]
    d = load(slug)
    comps = [c for c in d["competitors"] if c["words"] >= 100]
    extra = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else []
    texts = [(c["title"] + " " + " ".join(h for _, h in c["headings"]) + " " + c["body"]).lower() for c in comps] + [e["text"].lower() for e in extra]
    ncomp = len(texts)
    def has(t, p): return re.search(r"(?<![a-z])" + re.escape(p) + r"s?(?![a-z])", t) is not None
    topical = lambda p: any(t in p for t in topics)
    # competitor phrases
    comp_kw = {}
    for p, k in d["phrases"].items():
        if topical(p) and not re.search(r"\d{3,}|http|www|cookie|subscribe|newsletter|privacy|©|neuromuscular|effects of|\b(your|their|you|until|above|below|toward|towards|through|across|lie|keep|squeez\w*|set|off|back on|every|few|chest chest|especially|because|should|primarily|works|targets?|great|effective|ultimate|common|complete|their|right|increase|maximise|maximize|made|are|is|like|helps|many|perform|reps|per|serious|curl the|first|stationary|fully|once|if|starting|developing|side of|arms arm)\b", p):
            comp_kw[p] = sum(has(t, p) for t in texts)
    # autocomplete
    JUNK = r"\b(near me|tiktok|meme|reddit|png|gif|svg|youtube|song|game|quotes?|instagram|zumba|christmas|athlean|jeff|nippard|cavaliere|joe wicks|juice|toya|vicky|justiz|zuhause|zurich|vijayawada|upper east side|xhit|zfit|massage|planet fitness|peloton|calculator|chair|seniors|over 50|over 60|pain|injur\w*|pregnan\w*|postpartum|png|meaning|in hindi|in urdu|spanish|español|clip ?art|cartoon|anime|drawing|shirt|meme|app|pdf free|chart for men pdf)\b"
    ac = [s for s in d["autocomplete"] if topical(s) and not re.search(JUNK, s)]
    rows = collections.defaultdict(dict)
    for p, k in comp_kw.items():
        if k >= 2: rows[classify(p)][p] = {"competitors": k, "autocomplete": "Yes" if p in ac else "", "source": "Competitors"}
    for s in ac:
        c = classify(s); r = rows[c].get(s)
        k = sum(has(t, s) for t in texts)
        if r: r["autocomplete"] = "Yes"; r["source"] = "Competitors + autocomplete"
        else: rows[c][s] = {"competitors": k, "autocomplete": "Yes", "source": "Autocomplete"}
    questions = [s for s in ac if re.match(r"(how|what|why|is|are|can|should|does|do|which|when)\b", s)]
    ents = {}
    for cat, lst in ENTITIES.items():
        for e in dict.fromkeys(lst):
            k = sum(has(t, e) for t in texts)
            if k: ents[(cat, e)] = k
    # --- write xlsx
    wb = Workbook(); F = "Arial"; hf = Font(name=F, bold=True, color="FFFFFF"); fill = PatternFill("solid", start_color="1A1A2E")
    def sheet(name, header, data, widths):
        ws = wb.create_sheet(name); ws.append(header)
        for r in data: ws.append(r)
        for c in ws[1]: c.font = hf; c.fill = fill
        for row in ws.iter_rows(min_row=2):
            for c in row: c.font = Font(name=F, size=10); c.alignment = Alignment(wrap_text=True, vertical="top")
        for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
        ws.freeze_panes = "A2"
    wb.remove(wb.active)
    sheet("Competitors", ["#", "URL", "Title", "Word count (page text)", "H2/H3 headings", "FAQ-style headings"],
          [[i + 1, c["url"], c["title"], c["words"], " | ".join(h for l, h in c["headings"] if l in (2, 3))[:3000], " | ".join(c["faqs"])] for i, c in enumerate(comps)] +
          [[len(comps) + i + 1, e["url"], e["title"], e["words"], e["headings"], ""] for i, e in enumerate(extra)], [4, 45, 40, 12, 90, 40])
    for cls, name in (("short", "Short-tail (1-2 words)"), ("mid", "Mid-tail (3-4 words)"), ("long", "Long-tail (5+ words)")):
        data = sorted(rows[cls].items(), key=lambda kv: (-kv[1]["competitors"], kv[0]))
        sheet(name, ["Keyword", f"Used by competitors (of {ncomp})", "In Google/Bing autocomplete", "Source"],
              [[k, v["competitors"], v["autocomplete"], v["source"]] for k, v in data], [55, 18, 18, 26])
    sheet("Questions (PAA-style)", ["Question from autocomplete"], [[q] for q in questions], [80])
    sheet("Entities", ["Category", "Entity", f"Competitors using it (of {ncomp})", "Tag"],
          [[c, e, k, "MUST INCLUDE" if k >= 3 else ("DIFFERENTIATOR" if k == 2 else "")] for (c, e), k in sorted(ents.items(), key=lambda kv: (kv[0][0], -kv[1]))], [20, 34, 22, 18])
    ws = wb.create_sheet("Notes"); ws.append(["Keywords are content-derived from the competitor pages and Google/Bing autocomplete. Search volumes are NOT verified — check them in your keyword tool."])
    wb.save(f"research/{slug}.xlsx")
    json.dump({"rows": {k: v for k, v in rows.items()}, "questions": questions, "entities": {f"{c}|{e}": k for (c, e), k in ents.items()}, "ncomp": ncomp}, open(f"research/{slug}.summary.json", "w"))
    print({k: len(v) for k, v in rows.items()}, "questions", len(questions), "entities", len(ents), "competitors", ncomp)

if __name__ == "__main__":
    main()
