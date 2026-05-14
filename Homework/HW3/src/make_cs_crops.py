"""
Generate cs_crops/*.png for HW3_Generate.tex.

Parses the Final cheat sheet TeX source, extracts each `\\shead{}{}{TITLE}`
+ `\\begin{ebox}...\\end{ebox}` block, then compiles each one in a
standalone mini-doc and renders to PNG.
"""

import re
import subprocess
import tempfile
import shutil
from pathlib import Path
from PIL import Image
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
CHEATSHEET_TEX = REPO_ROOT / "Notes" / "Cheatsheets" / "Final" / "src" / "ECE332_Final_cheatsheet.tex"
OUT_DIR = SCRIPT_DIR / "cs_crops"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Keyword -> output slug. HW3 covers boundary normal incidence (P1, P2),
# Snell's law / multilayer (P3), waveguide modes (P4), multi-mode group
# velocity (P5).
WANT = {
    "NORMAL INCIDENCE":             "cs_normal",
    "PHASOR TEMPLATES":             "cs_phasor_templates",
    "POWER REFLECTION":             "cs_power",
    "LOSSY MEDIA --- 5 CASES":      "cs_lowloss",
    "SNELL'S LAW":                  "cs_snell",
    "LATERAL DISPLACEMENT":         "cs_lateral",
    "RECTANGULAR WAVEGUIDE":        "cs_wgmodes",
    "CUTOFF FREQUENCY":             "cs_cutoff",
    "$\\VAREPSILON_R$ FROM DISPERSION": "cs_epsilon_disp",
    "WAVE IMPEDANCE":               "cs_wgimpedance",
    "GROUP VELOCITY":               "cs_groupvel",
}


def find_brace_end(text, open_pos):
    depth = 0
    i = open_pos
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        elif c == "\\":
            i += 2
            continue
        i += 1
    raise ValueError(f"unbalanced braces starting at {open_pos}")


def parse_sections(tex_source):
    # Skip the preamble; the `\shead` macro definition is in there and
    # would otherwise look like a section to the parser.
    body_idx = tex_source.find(r"\begin{document}")
    i = body_idx if body_idx != -1 else 0
    while True:
        idx = tex_source.find(r"\shead", i)
        if idx == -1:
            return
        p = idx + len(r"\shead")
        try:
            a1 = find_brace_end(tex_source, tex_source.index("{", p))
            a2 = find_brace_end(tex_source, tex_source.index("{", a1))
            a3 = find_brace_end(tex_source, tex_source.index("{", a2))
        except ValueError:
            i = idx + 1
            continue
        title = tex_source[tex_source.index("{", a2) + 1 : a3 - 1].strip()
        body_start = tex_source.find(r"\begin{ebox}", a3)
        if body_start == -1:
            i = a3
            continue
        body_end = tex_source.find(r"\end{ebox}", body_start)
        if body_end == -1:
            i = a3
            continue
        body_end += len(r"\end{ebox}")
        yield title, tex_source[idx:body_end]
        i = body_end


def matches_keyword(title, keyword):
    norm_t = re.sub(r"\s+", " ", title).upper()
    norm_k = re.sub(r"\s+", " ", keyword).upper()
    return norm_k in norm_t


tex_source = CHEATSHEET_TEX.read_text()

section_by_keyword = {}
all_sections = list(parse_sections(tex_source))
for kw, slug in WANT.items():
    found = None
    for title, body in all_sections:
        if matches_keyword(title, kw):
            found = (title, body)
            break
    if found is None:
        print(f"  MISS  '{kw}' -> {slug}")
        continue
    section_by_keyword[slug] = found


MINI_PREAMBLE = r"""
\documentclass[6pt,letterpaper]{article}
\usepackage[paperwidth=2.67in,paperheight=14in,margin=4pt]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{mdframed}
\usepackage[expansion=false]{microtype}
\usepackage{booktabs}
\usepackage{colortbl}
\usepackage{array}
\usepackage{graphicx}

\definecolor{purple}{HTML}{534AB7}\definecolor{purplebg}{HTML}{EEEDFE}
\definecolor{teal}{HTML}{0F6E56}\definecolor{tealbg}{HTML}{E1F5EE}
\definecolor{coral}{HTML}{993C1D}\definecolor{coralbg}{HTML}{FAECE7}
\definecolor{amber}{HTML}{854F0B}\definecolor{amberbg}{HTML}{FAEEDA}
\definecolor{green}{HTML}{3B6D11}\definecolor{greenbg}{HTML}{EAF3DE}
\definecolor{blue}{HTML}{0C447C}\definecolor{bluebg}{HTML}{E6F1FB}
\definecolor{gray}{HTML}{444441}\definecolor{graybg}{HTML}{F1EFE8}
\definecolor{pink}{HTML}{72243E}\definecolor{pinkbg}{HTML}{FBEAF0}
\definecolor{rowB}{HTML}{F2F2EF}

\newmdenv[linewidth=0.4pt,innerleftmargin=3pt,innerrightmargin=3pt,
  innertopmargin=2pt,innerbottommargin=2pt,skipabove=1pt,skipbelow=1pt]{ebox}

\newcommand{\shead}[3]{%
  \noindent\colorbox{#1}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}%
  {\color{#2}\bfseries\fontsize{6}{7}\selectfont #3}}\vspace{0.5pt}}

\newcommand{\eq}[2]{\noindent{\color{gray}\bfseries\fontsize{5.8}{6}\selectfont#1}\enspace{\color{teal}\fontsize{5.5}{6}\selectfont\textit{#2}}}

\pagestyle{empty}
\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}
"""


def render_section(slug, body):
    tmpdir = Path(tempfile.mkdtemp(prefix="cs_section_"))
    tex_path = tmpdir / "section.tex"
    full_doc = (
        MINI_PREAMBLE
        + r"""
\begin{document}
\fontsize{6}{7.5}\selectfont
\setlength{\abovedisplayskip}{1pt}\setlength{\belowdisplayskip}{1.5pt}
\setlength{\abovedisplayshortskip}{0pt}\setlength{\belowdisplayshortskip}{0pt}
""" + body + r"""
\end{document}
"""
    )
    tex_path.write_text(full_doc)
    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", str(tex_path)],
        capture_output=True, cwd=str(tmpdir),
    )
    pdf_path = tmpdir / "section.pdf"
    if not pdf_path.exists():
        print(f"  COMPILE FAIL  {slug}:  see {tmpdir}")
        return None
    subprocess.run(["pdftoppm", "-r", "300", "-png", str(pdf_path), str(tmpdir / "rendered")], check=True)
    png = tmpdir / "rendered-1.png"
    img = Image.open(png).convert("RGB")
    arr = np.array(img)
    mask = (arr.sum(axis=2) < 255 * 3 - 30)
    ys, xs = np.where(mask)
    if ys.size == 0:
        cropped = img
    else:
        pad = 6
        y0, y1 = ys.min() - pad, ys.max() + pad
        x0, x1 = xs.min() - pad, xs.max() + pad
        y0, x0 = max(0, y0), max(0, x0)
        y1, x1 = min(img.height, y1 + 1), min(img.width, x1 + 1)
        cropped = img.crop((x0, y0, x1, y1))
    out_path = OUT_DIR / f"{slug}.png"
    cropped.save(out_path, "PNG", optimize=True)
    shutil.rmtree(tmpdir, ignore_errors=True)
    return cropped.size


for slug, (title, body) in section_by_keyword.items():
    size = render_section(slug, body)
    if size:
        print(f"  {slug:24s}  {size[0]}x{size[1]}  '{title[:50]}'")

print("done")
