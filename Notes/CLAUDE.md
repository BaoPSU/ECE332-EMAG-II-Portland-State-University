# ECE332 Cheat Sheet — Claude Setup Guide

## Overview
This project maintains LaTeX cheat sheets for ECE332 (Electromagnetics II) at Portland State University. The compiled PDFs and source `.tex` files live in the `Notes/` folder of the GitHub repo.

**Repo:** `BaoPSU/ECE332-EMAG-II-Portland-State-University`

**Folder structure:**
```
Notes/Cheatsheets/
├── Exam1/
│   ├── ECE332_Exam1_cheatsheet.pdf
│   ├── ECE332_HW1_cheatsheet.pdf
│   ├── ECE332_HW2_cheatsheet.pdf
│   └── src/
│       ├── ECE332_Exam1_cheatsheet.tex
│       ├── ECE332_HW1_cheatsheet.tex
│       └── ECE332_HW2_cheatsheet.tex
└── Final/
    └── src/          ← drop final cheat sheet .tex files here
```

**Always compile from the `src/` subfolder** — images use `\graphicspath{{../../}}` which resolves to `Notes/`. Compiling from `/tmp` will silently drop figures.

---

## Exam Coverage

### Midterm 1 — May 7, 2026
- **Lectures:** 1–10
- **Homeworks:** HW1, HW2
- **Cheat sheet:** `Exam1/ECE332_Exam1_cheatsheet` (2-sided, 1 page = 2 PDF pages)
- **Topics:** Faraday's & Ampère's laws, charge-current continuity, EM & time-harmonic potentials, plane-wave propagation (lossless & lossy), polarization, current flow in conductors, EM power density
- **Coverage doc:** `Exam1/COVERAGE.md`

### Final — date TBD, NOT cumulative
- **Lectures:** 11 onward (post-midterm only)
- **Homeworks:** HW3, HW4 (and any additional post-midterm assignments)
- **Cheat sheet:** `Final/src/` (to be created)
- **Topics (expected):** rectangular waveguides & resonant modes, plane-wave reflection/transmission at boundaries, optical fibers, dipole antennas, radiation patterns/directivity/beamwidth, Friis transmission, antenna arrays, radar (monostatic, Doppler)
- **Coverage doc:** `Final/COVERAGE.md`
- Per syllabus: "The final exam will not be cumulative."

---

## Workflow

### 1. Download the file from GitHub
Always start by pulling the latest `.tex` from GitHub — `/tmp` is cleared between sessions:
```bash
gh api repos/BaoPSU/ECE332-EMAG-II-Portland-State-University/contents/Notes/ECE332_HW2_cheatsheet.tex \
  --jq '.content' | base64 -d > /tmp/ECE332_HW2_cheatsheet.tex
```

### 2. Edit the file
Use the `Edit` tool on `/tmp/ECE332_HW2_cheatsheet.tex`.

### 3. Compile
```bash
cd /tmp && pdflatex -interaction=nonstopmode ECE332_HW2_cheatsheet.tex
```
Check output for `Output written on ... (1 page, ...)` — it must stay **1 page**.
The two pre-existing `Overfull \hbox` warnings at lines ~223 and ~241 (lossy media section) are harmless and expected.

### 4. Push both files to GitHub
PDF must be base64-encoded and sent via the GitHub API (too large for CLI arg):
```bash
# Push PDF
SHA=$(gh api repos/BaoPSU/ECE332-EMAG-II-Portland-State-University/contents/Notes/ECE332_HW2_cheatsheet.pdf --jq '.sha')
base64 -w 0 /tmp/ECE332_HW2_cheatsheet.pdf > /tmp/pdf_b64.txt
python3 -c "
import json
with open('/tmp/pdf_b64.txt') as f: content = f.read().strip()
json.dump({'message': 'YOUR MESSAGE', 'content': content, 'sha': '$SHA'}, open('/tmp/payload.json','w'))
"
gh api --method PUT repos/BaoPSU/ECE332-EMAG-II-Portland-State-University/contents/Notes/ECE332_HW2_cheatsheet.pdf \
  --input /tmp/payload.json --jq '.commit.sha'

# Push .tex
SHA2=$(gh api repos/BaoPSU/ECE332-EMAG-II-Portland-State-University/contents/Notes/ECE332_HW2_cheatsheet.tex --jq '.sha')
python3 -c "
import json, base64
content = base64.b64encode(open('/tmp/ECE332_HW2_cheatsheet.tex','rb').read()).decode()
json.dump({'message': 'YOUR MESSAGE', 'content': content, 'sha': '$SHA2'}, open('/tmp/payload_tex.json','w'))
"
gh api --method PUT repos/BaoPSU/ECE332-EMAG-II-Portland-State-University/contents/Notes/ECE332_HW2_cheatsheet.tex \
  --input /tmp/payload_tex.json --jq '.commit.sha'
```

---

## Layout
The sheet uses `\documentclass[6pt,letterpaper]{article}` with `0.25in` margins and a **3-column** `multicols` layout for the main body, followed by a 5-box `minipage` row at the bottom as a reference strip.

The three columns break with `\columnbreak` after the direction-of-propagation section (col 1 → col 2) and after the phasor↔time domain section (col 2 → col 3).

---

## Color Scheme
Each topic section uses a consistent color pair `(bg, text)`:

| Color   | Used for                          |
|---------|-----------------------------------|
| purple  | Lossless plane wave parameters    |
| teal    | Polarization, direction tables    |
| coral   | Lossy media                       |
| amber   | Circular waves (bottom strip)     |
| green   | Poynting / power density          |
| blue    | Lossy media workflow, useful nums |
| gray    | Read-a-wave quick steps           |
| pink    | Phasor ↔ time domain              |

Define colors with `\definecolor` and section headers with:
```latex
\shead{<bg>bg}{<color>}{SECTION TITLE}
```

---

## Table Pattern (IMPORTANT)

All tables with `\rowcolor` rows **must** use this exact wrapper to prevent the grey from bleeding to the full column width:

```latex
{\centering\makebox[0.98\linewidth][c]{{\setlength{\tabcolsep}{2pt}\begin{tabular}{@{}...@{}}
\toprule
...
\bottomrule
\end{tabular}}}\par}
```

Key rules:
- `{\centering ... \par}` — centers the makebox within the ebox
- `\makebox[0.98\linewidth][c]{...}` — constrains rowcolor fill to table width; 98% leaves a small visual margin
- `{\setlength{\tabcolsep}{2pt}...}` — reduces inter-column padding so `p{}` columns fit inside the 0.98\linewidth box
- `@{}` at both ends of column spec — removes leading/trailing column padding
- `p{}` column widths must sum to ≈ 0.95\linewidth or less (accounts for inter-column spacing at tabcolsep=2pt)

For **auto-sized** columns (`c`, `l`, `r`) the `\setlength{\tabcolsep}{2pt}` wrapper is optional since width is content-driven:
```latex
{\centering\makebox[0.98\linewidth][c]{\begin{tabular}{@{}ccll@{}}
...
\end{tabular}}\par}
```

Tables that still use `{\centering\begin{tabular}...\end{tabular}\par}` (without `\makebox`) will have rowcolor bleeding — convert them if it becomes visible.

---

## ebox Environment
All content blocks sit inside `\begin{ebox}...\end{ebox}` (defined via `mdframed`):
```latex
\newmdenv[linewidth=0.4pt, innerleftmargin=3pt, innerrightmargin=3pt,
  innertopmargin=0.5pt, innerbottommargin=0.5pt,
  skipabove=0.5pt, skipbelow=0.5pt]{ebox}
```
The inner `\linewidth` inside an ebox is approximately **182.7 pt** (column width 188.7 pt minus 6 pt of inner margins).

---

## Spacing Controls (Tight vs. Readable)

These are the key knobs for how dense the sheet looks:

### Box padding (`innertopmargin` / `innerbottommargin` / `skipabove` / `skipbelow`)
| Style | Settings | When to use |
|-------|----------|-------------|
| **Ultra-tight** | `innertopmargin=0.5pt, innerbottommargin=0.5pt, skipabove=0.5pt, skipbelow=0.5pt` | Max content, very compact look |
| **Readable** | `innertopmargin=2pt, innerbottommargin=2pt, skipabove=1pt, skipbelow=1pt` | Slightly more breathing room |

### Line spacing (`\fontsize{size}{baselineskip}`)
- `\fontsize{6}{7}\selectfont` — tighter line spacing (letters closer together)
- `\fontsize{6}{7.5}\selectfont` — slightly looser, easier to read

### Math equation spacing
```latex
\setlength{\abovedisplayskip}{0pt}\setlength{\belowdisplayskip}{0.5pt}   % ultra-tight
\setlength{\abovedisplayskip}{1pt}\setlength{\belowdisplayskip}{1.5pt}   % readable
\setlength{\abovedisplayshortskip}{0pt}\setlength{\belowdisplayshortskip}{0pt}
```

### Changing spacing mid-document (multi-page sheets)
You can reset any of the above with `\setlength` after `\newpage` to apply different density per page:
```latex
\newpage
\fontsize{6}{7}\selectfont
\setlength{\abovedisplayskip}{0pt}\setlength{\belowdisplayskip}{0.5pt}
```

---

## microtype Fix for Sub-6pt Fonts

If you get `pdfTeX error (font expansion): auto expansion is only possible with scalable fonts`, use:
```latex
\usepackage[expansion=false]{microtype}
```
This happens when `\eq{}{}` renders labels at 5.5–5.8pt and the CM bitmap font is hit. Disabling expansion fixes it with no visible quality loss.

---

## Images in Subdirectories

If the `.tex` is in `src/` but images live two levels up (e.g., `Notes/pol_ellipse.jpg`), add to the preamble:
```latex
\usepackage{graphicx}
\graphicspath{{../../}}
```
Then reference the image by filename only: `\includegraphics[width=\linewidth]{pol_ellipse.jpg}`

---

## Page Length Control
The sheet must fit on **1 page**. If it overflows, try (in order of impact):
1. Remove or shorten a section
2. Reduce `\vspace{}` between sections (currently `0.3pt`)
3. Tighten ebox margins (`innertopmargin`/`innerbottommargin`)
4. Condense multi-line items to one line
