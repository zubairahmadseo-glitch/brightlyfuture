"""Build Issue 03 HTML: inserts the SVG illustrations into the template."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import figures

here = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(here, "medicine-ball-workout-collection.template.html")).read()
html = tpl.replace("{{HERO}}", figures.hero_figure())
html = html.replace("{{PICKUP}}", figures.compare_svg(figures.PICKUP_WRONG, figures.PICKUP_RIGHT))
html = re.sub(r"\{\{FIG:(\w+)\}\}", lambda m: figures.card(m.group(1)), html)
assert "{{" not in html
out = os.path.join(here, "..", "medicine-ball-workout-collection.html")
open(out, "w").write(html)
print("wrote", os.path.normpath(out), len(html))
