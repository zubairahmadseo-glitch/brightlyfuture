"""Helpers shared by page content files."""
from .refs import R, refs, cite  # noqa: F401

SITE = "https://exercisemenu.com"
WEEK = "{{WEEK}}"
TABS = "{{TABS}}"


def L(path, text):
    """Internal link (path must be verified live on the sitemap)."""
    return f'<a href="{SITE}{path}">{text}</a>'


def box(kind, label, html):
    return f'<div class="emp-{kind}"><span class="emp-label">{label}</span>{html}</div>'


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="emp-tw emp-data"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


DISCLAIMER = ("This plan is general education for healthy adults, not medical advice. If you have an injury, "
              "a heart, joint or blood-pressure condition, or you are pregnant or postpartum, check with your "
              "doctor or a physiotherapist before starting a new training program.")
