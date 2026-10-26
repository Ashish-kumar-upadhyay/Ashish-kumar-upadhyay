#!/usr/bin/env python3
"""Neofetch-style info card (Now / Prev / Stack / Highlights) with line reveal."""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "info-card.svg")

HOST = os.environ.get("PROFILE_HOST", "ashish@github")
NAME = os.environ.get("PROFILE_NAME", "Ashish Kumar Upadhyay")
# match profile-ascii.svg canvas height when COLS=100 (~880)
H = int(os.environ.get("CARD_H", "880"))
W = 490
TITLEBAR_H = 30
PAD = 22
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
TEXT = "#e6edf3"

ROWS = [
    ("Now", "Full Stack Developer · Freelancer", "#22d3ee"),
    ("Prev", "BCA · International client projects", "#39d353"),
    ("Stack", "React · Next.js · Node · TypeScript", "#a371f7"),
    ("Stack", "MongoDB · Firebase · Supabase · Vercel", "#f778ba"),
    ("Highlights", "Dubai perfume e-commerce (live)", "#ffa657"),
    ("Highlights", "LMS platform · Kitchen recipe app", "#79c0ff"),
    ("Highlights", "State-level volleyball · DSA", "#ffd700"),
]

STATIC = bool(os.environ.get("STATIC"))
LINE_DUR = 0.45
STAGGER = 0.14

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

y0 = TITLEBAR_H + 40
parts.append(
    f'<text x="{PAD}" y="{y0}" fill="{TEXT}" font-size="20" font-weight="700">'
    f"{html.escape(NAME)}</text>"
)
parts.append(
    f'<text x="{PAD}" y="{y0 + 26}" fill="{MUTED}" font-size="12">'
    f"ashishupadhyay.me · Indore, India</text>"
)

for i, (key, val, color) in enumerate(ROWS):
    y = y0 + 56 + i * 36
    delay = i * STAGGER
    cls = "" if STATIC else ' class="l"'
    style = "" if STATIC else f' style="animation-delay:{delay:.2f}s"'
    parts.append(
        f'<g{cls}{style}>'
        f'<text x="{PAD}" y="{y}" fill="{color}" font-size="13" font-weight="700">'
        f"{html.escape(key)}</text>"
        f'<text x="{PAD + 98}" y="{y}" fill="{TEXT}" font-size="13">'
        f"{html.escape(val)}</text>"
        f"</g>"
    )

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes)")
