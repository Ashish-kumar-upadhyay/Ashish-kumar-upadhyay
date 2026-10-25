#!/usr/bin/env python3
"""Neofetch-style profile info card SVG with staggered line reveal."""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "info-card.svg")

HOST = os.environ.get("PROFILE_HOST", "ashish@github")
NAME = os.environ.get("PROFILE_NAME", "Ashish Kumar Upadhyay")

W, H = 490, 520
TITLEBAR_H = 30
PAD = 22
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
TEXT = "#e6edf3"

ROWS = [
    ("OS", "Full Stack Developer", "#22d3ee"),
    ("Host", "Freelancer · India", "#39d353"),
    ("Kernel", "React · Next.js · Node.js", "#a371f7"),
    ("Shell", "JavaScript · TypeScript · MongoDB", "#f778ba"),
    ("Uptime", "BCA · International clients", "#ffa657"),
    ("Packages", "Firebase · Supabase · Vercel", "#79c0ff"),
    ("Highlight", "Dubai e-commerce · LMS · Recipe app", "#ffd700"),
    ("Fun", "State-level volleyball · DSA", "#8b949e"),
]

STATIC = bool(os.environ.get("STATIC"))
LINE_DUR = 0.45
STAGGER = 0.12

css = f"""
@keyframes lineIn {{
  0% {{ opacity: 0; transform: translateX(-8px); }}
  100% {{ opacity: 1; transform: translateX(0); }}
}}
.l {{ opacity: 0; animation: lineIn {LINE_DUR}s ease-out both; }}
""".strip()

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    f"<style>{css}</style>",
    "<defs>"
    f'<linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
    f"</linearGradient></defs>",
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" '
    f'fill="none" stroke="{FRAME}" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
parts.append(
    f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
    f'text-anchor="middle">{html.escape(HOST)}: ~$ neofetch</text>'
)

y0 = TITLEBAR_H + 36
parts.append(
    f'<text x="{PAD}" y="{y0}" fill="{TEXT}" font-size="22" font-weight="700">'
    f"{html.escape(NAME)}</text>"
)
parts.append(
    f'<text x="{PAD}" y="{y0 + 28}" fill="{MUTED}" font-size="12">'
    f"Building real-world apps · Portfolio on Vercel</text>"
)

for i, (key, val, color) in enumerate(ROWS):
    y = y0 + 58 + i * 34
    delay = i * STAGGER
    cls = "" if STATIC else ' class="l"'
    style = "" if STATIC else f' style="animation-delay:{delay:.2f}s"'
    parts.append(
        f'<g{cls}{style}>'
        f'<text x="{PAD}" y="{y}" fill="{color}" font-size="13" font-weight="700">'
        f"{html.escape(key)}</text>"
        f'<text x="{PAD + 108}" y="{y}" fill="{TEXT}" font-size="13">'
        f"{html.escape(val)}</text>"
        f"</g>"
    )

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes)")
