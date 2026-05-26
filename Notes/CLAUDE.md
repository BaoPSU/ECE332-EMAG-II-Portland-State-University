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

---

## "Retard-Proof" Methodology (HW3 / HW4 / Exam1 style)

**Hard rule learned the hard way: a cheat sheet is a GENERIC FORMULA REFERENCE for a topic area, not a dump of the HW problems with answers boxed inline.**

The cheat sheet must be reusable on:
- This HW
- Future HWs covering the same topic
- The exam (where the questions will use different numbers / different setups)

So the sheet shows you HOW to recognize and solve problems of a given type. It must NOT:
- Tag formulas with HW problem numbers (`(P1)`, `(P2)`, etc.) — that ties the sheet to one specific assignment
- Box the actual HW answer next to the formula — that gives away the work and looks like a problem dump
- Use the exact HW numerical values as worked examples (e.g. `HW4 P1: l=1m, f=1MHz, R=5km → S = 1.51×10⁻⁹ W/m²`)

What the sheet should have instead:
- Formula templates with units
- `\eq{label}{when-to-use}` clarifiers
- Decision lookups (dipole-type-by-length, lossy-media-5-cases, etc.) that route any problem to the right formula
- Numbered recipes (Step 1 normalize, Step 2 HPBW, etc.)
- Tiny illustrative examples that show the SHAPE of the formula without solving any specific HW problem (e.g. `Gaussian shortcut: F = e^(-aθ²) = 0.5 ⇒ θ = √(ln 2/a)`)
- Coral warnings for traps that apply generally (e.g. "If l/λ < 1/50 STOP and use Hertzian, do NOT plug small l into the arbitrary formula")

Where the worked HW answers DO belong: `HWN_Generate.pdf` — the walkthrough document, which embeds cheat sheet snippets AND walks through the actual problem. That's the right place for `Problem 1: l = 1m, f = 1MHz → ... → S = 1.51×10⁻⁹ W/m²` work.

Anchor the cheat sheet to the topic, not the assignment.

### Top of sheet: PROBLEM LOOKUP table
First box on the sheet is a 2-column lookup mapping question types → section name. Sized so the eye lands on it first.
```latex
\shead{graybg}{gray}{HW4 PROBLEM LOOKUP --- READ FIRST}
\begin{ebox}
{\centering\makebox[0.98\linewidth][c]{...\begin{tabular}{@{}p{0.10\linewidth}p{0.86\linewidth}@{}}
\toprule
\# & Question $\to$ section\\
\midrule
\rowcolor{rowB}P1 & Power density of a dipole $\to$ HERTZIAN\\
P2 & HPBW, solid angle, directivity $\to$ BEAM PARAMETERS\\
...
```
- Tag each row with the HW problem number (`P1`, `P2`, ...) so you know which formula solves which problem.
- Footer with `\textit{\color{coral}Step 0 always: ...}` for universal prerequisites (e.g. compute λ first).

### `\eq{label}{when-to-use}` pattern
Every formula gets a label AND a when-to-use clarifier. The clarifier is in italic teal:
```latex
\eq{Power density}{$l/\lambda<1/50$; far field}
\[S(R,\theta) = ...\]
```
The condition tells you when this formula applies vs the alternate (e.g. arbitrary-length dipole).

### Worked numerical example inline
After each formula, drop one italic blue line with HW problem numbers plugged in and boxed answer:
```latex
\textit{\color{blue}HW4 P1: $l=1$m, $f=1$MHz, ... $S=...=\mathbf{1.51\times10^{-9}}$ W/m$^2$.}
```
- Use **bold** for the final number.
- Box the answer with `\boxed{...}` for the key step.
- Lets you find the right formula by recognizing the worked numbers, not by re-deriving from labels.

### Coral warnings for gotchas
Use `\textit{\color{coral}...}` for traps:
```latex
\textit{\color{coral}If $l/\lambda<1/50$ STOP and use Hertzian. Do NOT plug small $l$ into the arbitrary formula --- you'll get the wrong shape.}
```

### Recipe blocks
For multi-step procedures (Friis, effective area, beam parameters), number the steps with `\eq{Step N --- ...}{condition}` so each formula stands alone but the order is forced.

### Units everywhere
Every formula output gets a unit annotation `(Ω)`, `(rad/m)`, `(V/m)`, `(unitless)`, etc. — including bottom-strip symbol boxes. Single-line note acceptable for tables where every entry shares a unit:
```latex
\textit{$\tilde{E}$ in V/m, $\tilde{H}$ in A/m.}  % applies to whole box
```

### Bottom-strip symbol reference
Always end with 4–5 `\minipage` boxes summarizing the symbols. Each line: `$symbol$ --- description (unit)`. One symbol per line. Don't pack multiple symbols on one line — give each its own description and unit.

---

## Lessons Learned (What Breaks Page Count)

- **Adding ~2 lines to bottom-strip boxes** is enough to push from 1 page to 2. Trim something else first.
- **Bold + extra punctuation in italic notes** consumes more space than expected — keep notes lean.
- **Column widths in tables**: changing `p{0.18}` → `p{0.23}` (5%) is a meaningful visual change but rarely affects pages. Changing the total sum past `0.98\linewidth` causes overflow warnings.
- **Shrinking font below 5.5pt** to fit content usually means you should restructure, not shrink. 4.6pt is the practical floor for readability.
- **Vertical line separators** (`|p{...}|`) are cheap visually — no page-count impact, helps eye-scan tables.

## Lessons Learned (Source Authoring)

- **HW solutions are the primary source.** Build the sheet by reverse-engineering what the official `hwN_solutions.pdf` actually computes. Every section should map back to a specific HW problem.
- **Don't include sections from prior HW.** HW4 sheet should not have Snell, Brewster, or T-line analogies. Keep the sheet scoped to the assignment.
- **Default to no shorthand.** Full `\cos\theta_i` reads cleaner than `c_i` even if it takes more space. Use shorthand only if the table genuinely doesn't fit — and document the shorthand in the caption.
- **Vertical/horizontal lines in tables.** Vertical column separators (`|p{...}|`) help readability for wide formula tables. Horizontal `\midrule` between every row is visual clutter — use only between conceptually distinct row groups.

---

## Coverage Analysis: Does the Cheat Sheet Cover the HW?

After every cheat sheet rewrite, do a quick map of HW problem → cheat sheet section it solves. If any HW problem can't be solved using only the cheat sheet (plus standard mental math), the sheet is incomplete. If multiple sections are needed, the sheet should make the routing obvious.

### Example: HW4 ↔ HW4 cheat sheet (post-rewrite)

| HW4 problem | What it asks | Cheat sheet sections that solve it |
|---|---|---|
| P1 (8 pts) | Hertzian dipole power density at distance | DIPOLE TYPE BY LENGTH (classify) → HERTZIAN DIPOLE — $S(R,\theta)$ |
| P2 (15 pts) | HPBW, $\Omega_p$, $D$ from $F(\theta)$ | BEAM PARAMETERS step 2 (Gaussian shortcut), step 3, step 4 |
| P3 (15 pts) | $\lambda/4$ dipole pattern, $\theta_\text{max}$, $S_\text{max}$, plot $F(\theta)$ | ARBITRARY-LENGTH DIPOLE (quarter-wave specialization gives $S_\text{max} = 0.0858 S_0$ directly) |
| P4 (5 pts)  | Effective area vs physical area for half-wave dipole | EFFECTIVE AREA $A_e$ + COMMON DIPOLE PARAMETERS ($D = 1.64$) |
| P5 (5 pts)  | Friis link budget, TV broadcast | FRIIS TRANSMISSION + dB ↔ LINEAR (3 dB = ×2) + COMMON DIPOLE PARAMETERS ($G_t = 1.64$ for half-wave) |

**Coverage: 5/5 HW4 problems** solvable using only the cheat sheet. No external lookups needed except for one numerical integral in P2 ($\Omega_p$ for $e^{-20\theta^2}\sin\theta$), which the sheet flags as requiring Wolfram / numerical evaluation.

### "OP-ness" rating: how much does the sheet shortcut the work?

- **Mode classification step**: ⭐⭐⭐⭐⭐ The DIPOLE TYPE BY LENGTH lookup eliminates ambiguity (Hertzian vs arbitrary) on sight. Saves a step of derivation each problem.
- **Direct formulas with units inline**: ⭐⭐⭐⭐⭐ Every formula has units annotated, so plug-and-chug is direct — no unit-tracking errors.
- **Quarter-wave / half-wave specializations pre-derived**: ⭐⭐⭐⭐⭐ $S_\text{max} = 0.0858 S_0$ for $\lambda/4$ and $D = 1.64$ for half-wave are baked in. No re-deriving cos(π/4) terms on the exam.
- **Numbered recipe for beam parameters**: ⭐⭐⭐⭐⭐ Steps 1–4 (normalize → HPBW → $\Omega_p$ → $D$) make multi-part directivity problems mechanical.
- **Gaussian HPBW shortcut**: ⭐⭐⭐⭐⭐ $F = e^{-a\theta^2} \Rightarrow \theta_{1/2} = \sqrt{\ln 2/a}$ pre-derived. Skips the algebra step.
- **3 dB ↔ ×2 dB-linear table**: ⭐⭐⭐⭐ Friis problems with mixed dB/linear gains get done without calculator log conversions.
- **Friis recipe**: ⭐⭐⭐⭐ Numbered 1–4 (compute λ, convert dB→lin, pick $G_t$, plug in) so the problem reads like a checklist.

**Overall OP rating: 9/10.** The only soft spot is Problem 2(b) requiring numerical integration — the sheet flags it but can't shortcut it without a CAS. Everything else is plug-and-chug from the formulas printed on the sheet.

### Gaps to fix if any HW problem can't be solved from the sheet:
1. Identify which formula / table is missing
2. Add a new section OR extend an existing one
3. Do NOT add HW-specific values — keep the new section generic
4. Re-run `make_cs_crops.py` so the walkthrough doc picks up the new snippet

### Sign that the sheet has drifted into "HW dump" territory:
- You see `(P1)`, `(P2)`, etc. tags next to section headers
- Boxed numerical answers like `\mathbf{1.51 \times 10^{-9}}$ W/m²` appear inline with formulas
- Worked example uses the exact problem statement of an HW problem ("HW4 P1: l = 1m, f = 1MHz, R = 5km...")
- The sheet wouldn't be useful next term when the HW numbers change

If any of these appear: rewrite generic.
