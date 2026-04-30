#!/usr/bin/env python3
"""Vygeneruje HTML stránky pro jednotlivé dny tábora z `dny/den_*.md`.

Použití: python3 build_day_pages.py
Výstup: dny/den_01.html ... dny/den_12.html
"""
from __future__ import annotations
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
DNY_DIR = ROOT / "dny"

DAYS = [
    (1,  "den_01_prijezd_zlocin.md",  "den_01.html",  "Příjezd, zahájení a noční zločin",       "11. 7. (sobota)"),
    (2,  "den_02_objev.md",           "den_02.html",  "Objev a místo činu",                      "12. 7. (neděle)"),
    (3,  "den_03_vyslechy.md",        "den_03.html",  "Výslechy personálu",                      "13. 7. (pondělí)"),
    (4,  "den_04_mapa_forenzika.md",  "den_04.html",  "Mapa tábora a forenziku",                 "14. 7. (úterý)"),
    (5,  "den_05_navstevy.md",        "den_05.html",  "Příjezd hostů",                           "15. 7. (středa)"),
    (6,  "den_06_klid_udrzba.md",     "den_06.html",  "Den klidu, údržby a Aniččina výpověď",    "16. 7. (čtvrtek)"),
    (7,  "den_07_zlom.md",            "den_07.html",  "Zlom — Markův vzkaz z FN Brno",           "17. 7. (pátek)"),
    (8,  "den_08_vyjezd.md",          "den_08.html",  "Výjezd do Blanska",                       "18. 7. (sobota)"),
    (9,  "den_09_konfrontace.md",     "den_09.html",  "Konfrontace, přiznání, útěk",             "19. 7. (neděle)"),
    (10, "den_10_honicka.md",         "den_10.html",  "Hon na pachatele a nález závěti",         "20. 7. (pondělí)"),
    (11, "den_11_finale.md",          "den_11.html",  "FINÁLE — čtení závěti a dědictví",        "21. 7. (úterý)"),
    (12, "den_12_odjezd.md",          "den_12.html",  "Odjezd",                                  "22. 7. (středa)"),
]

CSS = r"""
:root {
  --color-primary: #1e3a5f;
  --color-primary-light: #2c5282;
  --color-accent: #d63031;
  --color-accent-bg: #fadbd8;
  --color-helper: #e67e22;
  --color-success: #27ae60;
  --color-success-bg: #d5f5e3;
  --color-bg: #f8fafc;
  --color-card: #ffffff;
  --color-text: #1e293b;
  --color-muted: #64748b;
  --color-border: #e2e8f0;
  --shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 12px rgba(0,0,0,0.04);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", Roboto, sans-serif;
  line-height: 1.7; color: var(--color-text); background: var(--color-bg);
  margin: 0; padding: 0;
}
.container { max-width: 880px; margin: 0 auto; padding: 0 24px; }

header.day-hero {
  background: linear-gradient(135deg, #1e3a5f 0%, #2c5282 100%);
  color: white; padding: 56px 0 40px;
}
.day-hero .pill {
  display: inline-block; padding: 4px 12px; background: rgba(255,255,255,0.18);
  border-radius: 16px; font-size: 13px; margin-bottom: 12px; letter-spacing: 0.3px;
}
.day-hero h1 { font-size: 36px; margin: 0 0 8px; font-weight: 700; line-height: 1.2; }
.day-hero .subtitle { font-size: 17px; opacity: 0.92; margin: 0; }

nav.day-nav {
  position: sticky; top: 0; z-index: 50;
  background: #1e3a5f; color: #f1f5f9;
  border-bottom: 1px solid #2c5282; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
nav.day-nav .container {
  display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
  padding: 10px 24px;
}
nav.day-nav a {
  color: #f1f5f9; text-decoration: none; padding: 8px 14px;
  font-size: 14px; font-weight: 500; border-radius: 6px;
  transition: background 0.15s;
}
nav.day-nav a:hover { background: rgba(255,255,255,0.10); }
nav.day-nav a.home { background: #fbbf24; color: #1e3a5f; font-weight: 600; }
nav.day-nav a.home:hover { background: #fcd34d; }
nav.day-nav .spacer { flex: 1; }
nav.day-nav .disabled { opacity: 0.4; pointer-events: none; }

main.day-content { padding: 40px 0 64px; }
main.day-content .container {
  background: var(--color-card); padding: 40px 56px;
  border-radius: 12px; box-shadow: var(--shadow); margin-top: -24px;
}

main.day-content h1 { display: none; }
main.day-content h2 {
  color: var(--color-primary); font-size: 24px; font-weight: 700;
  margin: 36px 0 16px; padding-bottom: 8px;
  border-bottom: 2px solid var(--color-border);
}
main.day-content h2:first-child { margin-top: 0; }
main.day-content h3 {
  color: var(--color-primary-light); font-size: 19px; font-weight: 600;
  margin: 28px 0 12px;
}
main.day-content h4 {
  color: var(--color-text); font-size: 16px; font-weight: 600;
  margin: 20px 0 8px;
  text-transform: uppercase; letter-spacing: 0.4px;
}
main.day-content p { margin: 12px 0; }
main.day-content ul, main.day-content ol { padding-left: 24px; margin: 12px 0; }
main.day-content li { margin-bottom: 6px; }
main.day-content strong { color: var(--color-primary); font-weight: 600; }
main.day-content em { color: var(--color-muted); }
main.day-content hr {
  border: 0; border-top: 1px solid var(--color-border); margin: 32px 0;
}

main.day-content blockquote {
  margin: 16px 0; padding: 12px 20px;
  background: #f8fafc; border-left: 4px solid var(--color-primary-light);
  border-radius: 0 8px 8px 0; color: var(--color-text);
}
main.day-content blockquote p { margin: 6px 0; }
main.day-content blockquote strong { color: var(--color-primary); }

main.day-content table {
  width: 100%; border-collapse: collapse; margin: 16px 0;
  font-size: 14px; box-shadow: var(--shadow); border-radius: 6px; overflow: hidden;
  table-layout: auto;
}
main.day-content table th {
  background: var(--color-primary); color: white; text-align: left;
  padding: 10px 12px; font-weight: 600;
  vertical-align: top; word-break: break-word;
}
main.day-content table td {
  padding: 8px 12px; border-top: 1px solid var(--color-border);
  vertical-align: top; word-break: break-word; overflow-wrap: anywhere;
}
main.day-content table tr:nth-child(even) td { background: #f8fafc; }
main.day-content table td:first-child {
  color: var(--color-primary);
  font-family: "JetBrains Mono", "Courier New", monospace;
  font-size: 13px;
}
/* Časy ve formátu HH:MM lze ponechat bez lámání — krátké stringy */
main.day-content table td:first-child:is(.time, [data-time]) {
  white-space: nowrap;
}

main.day-content code {
  font-family: "JetBrains Mono", "Courier New", monospace;
  background: var(--color-bg); border: 1px solid var(--color-border);
  padding: 1px 6px; border-radius: 4px; font-size: 0.92em;
}

footer.day-footer {
  background: #1e3a5f; color: #cbd5e1;
  padding: 28px 0; text-align: center; font-size: 14px;
}
footer.day-footer a { color: #fbbf24; text-decoration: none; font-weight: 600; }
footer.day-footer a:hover { text-decoration: underline; }
footer.day-footer .footer-nav { margin-top: 12px; }
footer.day-footer .footer-nav a { margin: 0 12px; }

@media (max-width: 768px) {
  .day-hero h1 { font-size: 26px; }
  .day-hero .subtitle { font-size: 15px; }
  main.day-content .container { padding: 24px; margin-top: -16px; }
  main.day-content h2 { font-size: 20px; }
  main.day-content h3 { font-size: 17px; }
  main.day-content table { font-size: 13px; }
  main.day-content table td, main.day-content table th { padding: 6px 8px; }
  nav.day-nav .container { padding: 8px 12px; }
  nav.day-nav a { padding: 6px 10px; font-size: 13px; }
}
@media print {
  nav.day-nav, footer.day-footer { display: none; }
  main.day-content .container { box-shadow: none; padding: 0; }
}
"""

def md_to_html(md_text: str) -> str:
    md = markdown.Markdown(extensions=["tables", "extra", "sane_lists"])
    return md.convert(md_text)


def build_day(num: int, src_md: str, out_html: str, title: str, date_label: str) -> None:
    src_path = DNY_DIR / src_md
    out_path = DNY_DIR / out_html

    md_text = src_path.read_text(encoding="utf-8")
    body_html = md_to_html(md_text)

    prev_link = ""
    next_link = ""
    if num > 1:
        prev_link = f'<a href="{DAYS[num-2][2]}">← Den {num-1}</a>'
    else:
        prev_link = '<a class="disabled">← Den</a>'
    if num < 12:
        next_link = f'<a href="{DAYS[num][2]}">Den {num+1} →</a>'
    else:
        next_link = '<a class="disabled">Den →</a>'

    html = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Den {num} — {title} · Tábor Světlo 2026</title>
<style>{CSS}</style>
</head>
<body>

<header class="day-hero">
  <div class="container">
    <span class="pill">Den {num} · {date_label}</span>
    <h1>{title}</h1>
    <p class="subtitle">Detailní program a příběh dne</p>
  </div>
</header>

<nav class="day-nav">
  <div class="container">
    <a class="home" href="../pruvodce.html#dny">← Průvodce hrou</a>
    <span class="spacer"></span>
    {prev_link}
    {next_link}
  </div>
</nav>

<main class="day-content">
  <div class="container">
    {body_html}
  </div>
</main>

<footer class="day-footer">
  <div class="container">
    <div>Tábor Světlo 2026 — Případ ztracené závěti · Den {num}</div>
    <div class="footer-nav">
      <a href="../pruvodce.html#dny">Průvodce hrou</a>
      <a href="../pribeh.html">Příběh jako kniha</a>
      <a href="../{src_md}">Zdrojový MD</a>
    </div>
  </div>
</footer>

</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")
    print(f"  ✓ {out_html}")


def main() -> None:
    print(f"Generuji HTML pro {len(DAYS)} dní → {DNY_DIR}/")
    for num, src, out, title, date in DAYS:
        build_day(num, src, out, title, date)
    print("Hotovo.")


if __name__ == "__main__":
    main()
