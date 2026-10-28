"""Package out/ into a paste-ready zip: python3 make_zip.py <dest_dir>"""
import json, pathlib, shutil, sys, zipfile

ROOT = pathlib.Path(__file__).parent
dest = pathlib.Path(sys.argv[1])
name = "ExerciseMenu-Workout-Plans-All-15"
base = dest / name
shutil.rmtree(base, ignore_errors=True)
base.mkdir(parents=True)
man = json.loads((ROOT / "out/manifest.json").read_text())
for p in man:
    d = base / f'{p["num"]:02d}-{p["slug"]}'
    d.mkdir()
    shutil.copy(ROOT / f'out/{p["slug"]}.html', d / "1-PASTE-IN-WORDPRESS.txt")
    (d / "2-SEO-SETTINGS.txt").write_text(f"""PAGE TITLE (WordPress title / H1):
{p["title"]}

SLUG (Permalink):
{p["slug"]}

PARENT PAGE:
Workout Plans  (final URL: https://exercisemenu.com/workout-plans/{p["slug"]}/)

RANK MATH - SEO TITLE ({len(p["meta_title"])} characters):
{p["meta_title"]}

RANK MATH - META DESCRIPTION ({len(p["meta_desc"])} characters):
{p["meta_desc"]}

RANK MATH - FOCUS KEYWORD:
{p["focus_kw"]}
""")
    shutil.copy(ROOT / f'preview/{p["slug"]}.html', d / "3-PREVIEW-open-in-browser.html")
rows = "\n".join(f'  {p["num"]:>2}. {p["title"]}\n      -> /workout-plans/{p["slug"]}/' for p in man)
(base / "00-PROCESS-GUIDE.txt").write_text((ROOT / "PROCESS-GUIDE.txt").read_text().replace("{PAGES}", rows))
zpath = dest / f"{name}.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(base.rglob("*")):
        z.write(f, f.relative_to(dest))
print(zpath)
