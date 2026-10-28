"""Save the built pages to WordPress as DRAFTS (never publishes).

Auth is injected by the session proxy for exercisemenu.com/wp-json/, so no credentials live here.

  python3 publish.py test     -> users/me + create/verify/delete a test draft with Rank Math meta
  python3 publish.py drafts   -> ensure parent "Workout Plans" draft, then create/update the 11 drafts

Existing pages with the same slug are updated only if they are still drafts; anything
published, pending or scheduled is left untouched and reported.
"""
import json
import os
import pathlib
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://exercisemenu.com/wp-json/wp/v2"
ROOT = pathlib.Path(__file__).parent
CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()


def call(method, path, body=None, params=None):
    url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json", "User-Agent": "em-publisher"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            payload = json.loads(raw)
        except ValueError:
            payload = raw.decode(errors="replace")[:300]
        return e.code, {"error": payload, "proxy": e.headers.get("X-Proxy-Error")}


def meta(title, desc, kw):
    return {"rank_math_title": title, "rank_math_description": desc, "rank_math_focus_keyword": kw}


def find_page(slug):
    code, res = call("GET", "/pages", params={"slug": slug, "status": "draft,pending,publish,future,private", "context": "edit"})
    if code != 200:
        raise SystemExit(f"lookup {slug} failed: {code} {res}")
    return res[0] if res else None


def test():
    code, me = call("GET", "/users/me", params={"context": "edit"})
    print("users/me:", code, me if code != 200 else {k: me.get(k) for k in ("id", "name", "roles")})
    if code != 200:
        raise SystemExit(1)
    caps = me.get("capabilities", {})
    print("unfiltered_html:", caps.get("unfiltered_html"))
    m = meta("EM test title", "EM test description", "em test keyword")
    code, page = call("POST", "/pages", {"title": "EM API test (delete me)", "status": "draft",
                                         "content": '<!-- wp:html -->\n<div class="emp"><input type="radio" id="x"><label for="x">t</label></div>\n<!-- /wp:html -->',
                                         "meta": m})
    print("create:", code, page.get("id") if code == 201 else page)
    if code != 201:
        raise SystemExit(1)
    pid = page["id"]
    code, got = call("GET", f"/pages/{pid}", params={"context": "edit"})
    saved = {k: got.get("meta", {}).get(k) for k in m}
    print("meta round-trip:", "OK" if saved == m else saved)
    print("input/label kept:", "<input" in got["content"]["raw"] and "<label" in got["content"]["raw"])
    code, _ = call("DELETE", f"/pages/{pid}", params={"force": "true"})
    print("delete:", code)


def drafts():
    parent = find_page("workout-plans")
    if parent is None:
        code, parent = call("POST", "/pages", {"title": "Workout Plans", "slug": "workout-plans", "status": "draft", "content": ""})
        print("parent created:", code, parent.get("id"))
    else:
        print("parent exists:", parent["id"], parent["status"])
    pid = parent["id"]
    manifest = json.loads((ROOT / "out" / "manifest.json").read_text())
    for p in manifest:
        body = {
            "title": p["title"], "slug": p["slug"], "status": "draft", "parent": pid,
            "content": (ROOT / "out" / f'{p["slug"]}.html').read_text(),
            "meta": meta(p["meta_title"], p["meta_desc"], p["focus_kw"]),
        }
        existing = find_page(p["slug"])
        if existing and existing["status"] != "draft":
            print(f'#{p["num"]} SKIPPED: /{p["slug"]}/ exists with status {existing["status"]}')
            continue
        if existing:
            code, res = call("POST", f'/pages/{existing["id"]}', body)
        else:
            code, res = call("POST", "/pages", body)
        ok = code in (200, 201)
        if ok:
            _, got = call("GET", f'/pages/{res["id"]}', params={"context": "edit"})
            checks = [got["status"] == "draft", got["slug"] == p["slug"], "emp-tabs" in got["content"]["raw"] and "<input" in got["content"]["raw"],
                      got.get("meta", {}).get("rank_math_title") == p["meta_title"]]
            print(f'#{p["num"]} {"updated" if existing else "created"} id={res["id"]} checks={"OK" if all(checks) else checks} preview={got.get("link")}')
        else:
            print(f'#{p["num"]} FAILED {code} {res}')


if __name__ == "__main__":
    {"test": test, "drafts": drafts}[sys.argv[1] if len(sys.argv) > 1 else "test"]()
