# Cheat Sheet Methodology — Reverse-Engineered from Midterm 1

This document explains how `Midterm1/ECE332_Exam1_cheatsheet.pdf` was built and how to replicate that quality for the Final using `Homework/HW3/hw3_solutions.pdf` and `Homework/HW4/hw4_solutions.pdf` as the primary source.

Goal: a one-page (two-sided) reference dense enough to walk through every HW problem and exam question without flipping back to lectures or the textbook.

---

## 1. Source hierarchy (most important first)

1. **HW answer keys** are the primary source. Every section of the midterm cheat sheet maps to a step that appears in the HW1 or HW2 solutions. If a method shows up in two solutions, it earns a section. If it shows up once, it earns a lookup table.
2. **Lecture slides** are the secondary source. They define notation and order of operations but the cheat sheet should not just transcribe lecture math. Use lectures to confirm sign conventions and units.
3. **Textbook** (`Notes/Textbook/EM1-book-7th-ed.pdf`, Ulaby & Ravaioli 7e) is the fallback for derivations and edge cases. Pull tables and figures (e.g. polarization ellipse, waveguide mode pictures) from here, not from lectures, since they reproduce more cleanly.

Workflow: read the answer keys first. Highlight every distinct technique. Each technique becomes one ebox.

---

## 2. Page budget

- 1 physical page, 2-sided = 2 PDF pages.
- 6 pt body, 7.5 pt baseline on page 1; 6 pt / 7 pt on page 2 (tighter when more content is needed).
- 0.25 in side margins, 0.3 in top, 0.25 in bottom.
- 3-column `multicols` body + 5-minipage bottom strip = 8 layout slots per page.
- Roughly 10 to 13 eboxes per page. Beyond that, density wins and content gets cut.

The bottom strip is the **definitions and unit reference** — variable names, units, constants. Never put a formula there. Definitions only.

---

## 3. The 3-column flow

Each column is its own theme:
- **Column 1**: setup formulas (what the wave/circuit is). Lossless plane-wave parameters, source quantities, EMF basics.
- **Column 2**: cases and lookup tables. Sign conventions, polarization handedness table, $\hat{k}\times\hat{E}$ direction tables, quadrant rules.
- **Column 3**: hard / lossy / advanced. Lossy media exact and approximations, Poynting, dB, skin depth, surface resistance.

Insert `\columnbreak` at the boundary so LaTeX doesn't reflow your theme order. The midterm sheet breaks after the rotating-loop generator (col 1 → 2) and after the phasor-to-time table (col 2 → 3).

---

## 4. Color taxonomy

Each topic class gets one (background, foreground) pair and **the same pair is reused** across the sheet so the reader's eye learns the code:

| Pair | Used for |
|---|---|
| purple | Maxwell / Faraday / EMF / plane-wave base parameters |
| teal | Sources (B fields, polarization, $\hat{k}\times\hat{E}$ tables) |
| coral | Lossy / conductor / displacement vs conduction / boundaries (anything with $\sigma$ or $\varepsilon''$) |
| amber | Geometry / specific cases (rotating loop, circular polarization, retarded potentials) |
| green | Power density / Poynting / dB |
| blue | Comparison tables, useful numbers |
| gray | Quick-steps / unit circle / trig identities |
| pink | Phasor ↔ time domain / $j$ identities / transformers |

Defined once in the preamble with `\definecolor`. Headers come from `\shead{bgcolor}{textcolor}{TITLE}` (already defined in the existing tex file).

---

## 5. The LaTeX patterns that make it work

### 5.1 `\shead{bg}{fg}{TITLE}` — section header
A colored bar with the title in bold small-caps-like 6pt. One per ebox. Always all-caps for scannability.

### 5.2 `\eq{label}{when-to-use}` — formula label with conditional
This is the highest-leverage pattern. Every formula gets a tiny italic teal annotation describing **when** to apply it. Example:

```
\eq{Transformer EMF}{stationary loop, $B$ changes}
\[V_\text{emf} = -\int_S \partial\mathbf{B}/\partial t \cdot d\mathbf{s}\]
```

This converts the cheat sheet from a formula list into a decision tree. The reader scans labels to find the right tool instead of pattern-matching on equation shapes.

### 5.3 `ebox` environment — bordered content block
Thin frame with 3 pt inner margins. Houses one topic. Stack vertically with `\vspace{0.3pt}` to `\vspace{2pt}` between them (tighter on page 2).

### 5.4 Striped tables (`\rowcolor{rowB}`)
Alternating row tint. Wrap every rowcolor table in:

```
{\centering\makebox[0.98\linewidth][c]{{\setlength{\tabcolsep}{2pt}
\begin{tabular}{@{}...@{}} ... \end{tabular}}}\par}
```

The `\makebox[0.98\linewidth][c]` constrains the rowcolor fill so it does not bleed past the ebox. The `\setlength{\tabcolsep}{2pt}` tightens columns so they fit. The `@{}` at both ends strips end-padding. Required because the default rowcolor extends to the full column width of the parent multicol, which leaks color into the next ebox.

### 5.5 Image inclusion via `\graphicspath{{../img/}}`
Figures live in `Midterm1/img/`. Compile from `Midterm1/src/` and the path resolves. Use `\includegraphics[width=0.9\linewidth,keepaspectratio]{name.png}` inside a `{\centering ... \par}` wrapper so it does not break ebox spacing.

### 5.6 Manual spacing
Math display skip is `0pt` above and `0.5pt` to `1.5pt` below. `\parskip` is zero. The page is dense by deliberate suppression of LaTeX's default spacing, not by font shrinking past 6 pt (which would trip `microtype` errors — see `Notes/CLAUDE.md` for the `expansion=false` fix).

---

## 6. Content design principles

These are the rules the existing cheat sheet follows. Use them when picking what to include.

### 6.1 Lookup-first
For every recurring decision in the HW solutions, build a table not a sentence. Examples from the existing sheet:
- $\hat{k}\times\hat{E}$ direction table (18 rows, all $\hat{k}$ × $\hat{E}$ pairs)
- $\partial B/\partial t$ derivative table (4 common $B(t)$ forms)
- Sign-of-$V_{\text{emf}}$ to current-direction table
- Lossy classification by loss tangent ranges
- Quadrant rule for $\tan(2\gamma)$ with 4 sign cases

If the HW solution does any computation that takes more than two lines of algebra, table the result.

### 6.2 Order of operations
Each topic ebox should follow the order the HW solution uses. For plane-wave problems, that order is $\omega \to u_p \to k \to \lambda \to \eta$. Print that order in the ebox. The reader follows it left-to-right.

### 6.3 "When to use" labels are not optional
Every formula's `\eq{}{}` second argument is the condition that selects it: "always works", "loop moves, B static", "good conductor", "low-loss dielectric". This is what makes the sheet usable under exam time pressure.

### 6.4 Approximations earn their own ebox
Lossy media split into three eboxes: exact, low-loss, good conductor. Each carries its $\alpha$, $\beta$, $\eta_c$, $u_p$ in its own block. The reader picks the regime once (via loss tangent table) then stays in one ebox.

### 6.5 Highlight the trap with `\textit{\color{coral}...}`
Anywhere a student is likely to mess up sign, units, or convention, drop a coral italic warning. Examples in the existing sheet:
- "$N$ in $\mathbf{B}$ only if the source is a multi-turn coil. Single wire $\Rightarrow N=1$"
- "If sign$(\gamma)\!\neq\!$sign$(\delta)$: $\gamma\leftarrow\gamma\pm\pi/2$"
- "$\cos^{-1}$ gives $[0,\pi]$; take $\phi_0$ in that range"

These came directly from worked-out HW mistakes.

### 6.6 The bottom strip is units, not formulas
Five minipages. Each is a vocabulary list with variable, what it means, units. No formulas. No tables. This is where the reader confirms what $\eta_c$ versus $\eta$ means, not how to compute it.

---

## 7. Mapping HW1+HW2 solutions to the Midterm 1 cheat sheet

So you can see the recipe: each cheat sheet ebox traces directly to a solution step.

| Cheat sheet ebox | HW step that motivated it |
|---|---|
| Transformer EMF / Motional EMF / Flux form | HW1 problems about loop EMF in changing B |
| $\partial B/\partial t$ table | HW1 had multiple loops with $B_0\sin(\omega t)$ |
| Long wire + rect loop integral | HW1 specific geometry that recurred |
| Sign-to-current-direction table | HW1 always asked for current direction after EMF sign |
| Displacement vs conduction current | HW1 had parallel-plate cap with both $\sigma$ and $\varepsilon$ |
| Charge relaxation $\tau_r$ | HW1 had a decay-time problem |
| Plane-wave parameter order ($\omega\to u_p\to k\to\lambda\to\eta$) | HW2 P1 walked through all five |
| Polarization auxiliary / rotation / ellipticity | HW2 P3 polarization analysis |
| Quadrant rule for $\tan(2\gamma)$ | HW2 P3 required quadrant correction |
| Lossy media: exact / low-loss / good conductor | HW2 had one problem in each regime |
| Skin depth $\delta_s$ formulas | HW2 surface resistance question |
| Poynting average | HW2 power density question |
| dB / attenuation | HW2 attenuation-over-distance question |

So the recipe is: read each HW solution problem. Every distinct technique that appears becomes one ebox. Every recurring lookup becomes one table.

---

## 8. Plan for the Final cheat sheet (built from HW3 + HW4)

`Homework/HW3/hw3_solutions.pdf` and `Homework/HW4/hw4_solutions.pdf` are the source. Here is the section list derived from them, ready to build.

### HW3 content (boundaries + waveguides)

**Page 1, Col 1 — Boundary at normal incidence (purple / coral)**
- Setup: $\eta_1, \eta_2$, derive $\Gamma$ and $\tau$ formulas.
- `\eq` block: "lossless to lossless" → $\eta_i = \eta_0/\sqrt{\varepsilon_{r,i}}$.
- `\eq` block: "lossless to poor conductor" → use low-loss $\eta_2 \approx \sqrt{\mu/\varepsilon'}(1+j\sigma/(2\omega\varepsilon))$ from HW3 P2.
- $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$, $\tau = 1 + \Gamma$.
- Reflected/transmitted phasor templates with $e^{\pm jk_1 z}$ and $e^{-\alpha_2 z}e^{-j\beta_2 z}$.
- % power table: $|\Gamma|^2$ reflected, $|\tau|^2 \eta_1/\eta_2$ transmitted.

**Page 1, Col 2 — Snell + multilayer (teal / blue)**
- Snell's law: $\sin\theta_2 = \sin\theta_1\sqrt{\varepsilon_{r1}/\varepsilon_{r2}}$.
- Chained Snell for stacks (HW3 P3 has 3 layers).
- Lateral displacement geometry: $d = \sum_i t_i \tan\theta_i$.
- `\eq{Equal-impedance shortcut}{air-to-X-to-air slab}`: angle returns to $\theta_i$.

**Page 1, Col 3 — Rectangular waveguide identification (coral)**
- Mode form: $E_x = E_0 \cos(m\pi x/a)\sin(n\pi y/b)\sin(\omega t - \beta z)$.
- Read $m, n$ from the arguments: $m\pi/a$ coefficient on $x$, $n\pi/b$ on $y$. Table the mapping.
- Dispersion: $\varepsilon_r = (c/\omega)^2[\beta^2 + (m\pi/a)^2 + (n\pi/b)^2]$.
- Cutoff: $f_{mn} = (u_{p0}/2)\sqrt{(m/a)^2 + (n/b)^2}$ where $u_{p0} = c/\sqrt{\varepsilon_r}$.
- Wave impedance: $Z_{\text{TE}} = \eta/\sqrt{1-(f_c/f)^2}$, $Z_{\text{TM}} = \eta\sqrt{1-(f_c/f)^2}$.
- $H_y = E_x / Z_{\text{TE}}$ for TE modes.

**Page 2, Col 1 — Multi-mode propagation (coral / amber)**
- Mode list: TE$_{10}$, TE$_{01}$, TE$_{11}$, TM$_{11}$, TE$_{20}$, ... with cutoff formulas.
- `\eq{Hollow guide}{$\varepsilon_r = 1$, use $c$ directly}`.
- Propagation condition: $f > f_{mn}$.
- Group velocity: $u_g = c\sqrt{1-(f_{mn}/f)^2}$ (hollow), or $u_{p0}\sqrt{1-(f_{mn}/f)^2}$ (filled).
- Travel time: $t = L/u_g$.
- Table the four lowest-mode cutoffs for $a > b$ rectangles.

### HW4 content (antennas)

**Page 2, Col 2 — Hertzian dipole + arbitrary dipole (purple)**
- Hertzian criterion: $l/\lambda < 1/50$.
- $S(R,\theta) = (\eta_0 k^2 I_0^2 l^2)/(32\pi^2 R^2)\sin^2\theta$ for Hertzian.
- Arbitrary length: $S(\theta) = (15 I_0^2/(\pi R^2))[(\cos(\pi l/\lambda \cos\theta) - \cos(\pi l/\lambda))/\sin\theta]^2$.
- Half-wave dipole shortcut: $l = \lambda/2$, $D = 1.64$.

**Page 2, Col 3 — Beam parameters + Friis (green / pink)**
- Half-power beamwidth: solve $F(\theta) = 0.5$.
- Pattern solid angle: $\Omega_p = \iint_{4\pi} F(\theta)\sin\theta\, d\theta\, d\phi$.
- Directivity: $D = 4\pi/\Omega_p$.
- Effective area: $A_e = \lambda^2 D/(4\pi)$.
- Physical area for half-wave: $A_p = l d = (\lambda/2) d$ where $d$ is wire diameter.
- Friis: $P_{\text{rec}} = G_t G_r (\lambda/(4\pi R))^2 P_t$.
- dB → linear: $G_{\text{lin}} = 10^{G_{\text{dB}}/10}$. (3 dB = 2, 10 dB = 10, 20 dB = 100.)

### Bottom strip both pages — units / definitions
- Page 1 (boundaries/waveguide): $\Gamma$, $\tau$, $\theta_i$, $a$, $b$, $f_{mn}$, $u_g$, $Z_{\text{TE/TM}}$.
- Page 2 (antennas): $I_0$, $l$, $\eta_0$, $S$, $F(\theta)$, $\Omega_p$, $D$, $G$, $A_e$, $R$.

---

## 9. Build workflow for the Final sheet

1. **Copy the existing tex** as a starting template. The preamble (colors, `\shead`, `\eq`, `ebox`, header/footer) is already correct.
2. **Replace the body** with the section list from §8.
3. **Reuse images** from `Midterm1/img/` if relevant (unit circle, conductor diagram). Add new figures to a `Final/img/` folder: waveguide cross-section, dipole pattern, layer-stack with $\theta$ angles.
4. **Compile from `Final/src/`** twice with `pdflatex -interaction=nonstopmode`. Verify output is exactly 1 physical page (2 PDF pages).
5. **Spot-check against the answer keys**: pick HW3 P4 (waveguide TE$_{23}$ identification). Try to do it using only the cheat sheet. If you have to flip to the solutions, the missing piece becomes a new ebox.
6. **Push** both `.tex` and `.pdf` to `Notes/Cheatsheets/Final/` and `Notes/Cheatsheets/Final/src/`.

---

## 10. What separates "complete" from "powerful"

A complete cheat sheet has every formula. A powerful one tells you which formula to use. Three habits make the difference:

1. **`\eq{}{}` on every formula** — the second argument is the condition that selects it.
2. **Lookup tables over inline math** — sign, direction, quadrant, regime.
3. **Coral warnings on the traps** — the things you mess up once in HW and never again.

Apply those three rules to every ebox and the final sheet will carry the same weight as the midterm one.

---

## References

- `Notes/Cheatsheets/Midterm1/src/ECE332_Exam1_cheatsheet.tex` — reference implementation.
- `Notes/Cheatsheets/Midterm1/COVERAGE.md` — topic list for the midterm.
- `Notes/Cheatsheets/Final/COVERAGE.md` — topic list for the final.
- `Notes/Textbook/EM1-book-7th-ed.pdf` — Ulaby & Ravaioli for derivations and figures.
- `Homework/HW1/hw1solns.pdf`, `Homework/HW2/HW2_solutions.pdf` — midterm source material.
- `Homework/HW3/hw3_solutions.pdf`, `Homework/HW4/hw4_solutions.pdf` — final source material.
- `Notes/CLAUDE.md` — compile/push workflow.
