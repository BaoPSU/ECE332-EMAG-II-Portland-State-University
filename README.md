# ECE 332 — Engineering Electromagnetics II
**Portland State University — Spring 2026**

## Course Info
- **Repo owner / student:** Bao Nguyen (`baon@pdx.edu`)
- **Lab partner:** Nick Stites
- **Instructor:** Mark Martin (`marmart2@pdx.edu`), FAB 20-10
- **Office hours:** T/Th 12:30–1:20
- **Syllabus:** [`syllabus.pdf`](syllabus.pdf) at repo root

## Grading
| Component | Weight |
|---|---|
| Labs       | 20% |
| Homework   | 30% |
| Midterm 1  | 25% |
| Final exam | 25% |

## Exams
- **Midterm 1** (May 7, 2026) — covers lectures 1–10, HW1, HW2.
- **Final exam** (date TBD) — covers lecture 11 onward. **NOT cumulative.**

## Repository Structure
```
Exams/          Midterm 1 answer keys (PDF + LaTeX src/)
Homework/       HW1 … HW5 — Original, Blank, Submission, solutions, Generate walkthrough
Labs/           Lab 1 … Lab 4 — PSU-formatted LaTeX reports
Notes/
  ├── lecture01.pdf … lecture13.pdf
  ├── Cheatsheets/
  │   ├── Exam1/   ECE332_Exam1_cheatsheet (active for lectures 1–10)
  │   └── Final/      ECE332_Final_cheatsheet (active for lectures 11+)
  ├── Textbook/
  │   ├── EM1-book-7th-ed.pdf
  │   └── tables/     Reference snapshots (Table 8-2, 8-3, …)
  └── METHODOLOGY.md  How the cheat sheets are built
syllabus.pdf
README.md
CLAUDE.md       Project-wide Claude Code guide (writing persona, workflows)
```

## Lab Status
| # | Topic | Status |
|---|---|---|
| 1 | Signal Integrity            | submitted |
| 2 | Wireless Power              | submitted |
| 3 | Waveguides                  | submitted |
| 4 | Patch Antenna (WiFi 2.4 GHz)| in progress |

## Homework Naming Convention
Each `Homework/HWN/` uses:

| File | Meaning |
|---|---|
| `HWN_Original.pdf`   | Instructor's original prompt |
| `HWN_Blank.pdf`      | Xournal worksheet with extra space |
| `HWN_Submission.pdf` | Completed and turned in |
| `hwN_solutions.pdf`  | Official solutions (lowercase) |
| `HWN_Generate.pdf`   | Walkthrough showing which cheat sheet snippets solve each problem |
| `src/`               | LaTeX source + Python scripts + cs_crops/ image cuts |

## Topics Covered
**First half (Midterm 1):**
- Faraday's law, induced EMF, transformers, mutual inductance
- Displacement current, Maxwell's equations
- Plane wave propagation (lossless and lossy media)
- Polarization (linear, circular, elliptical)
- Current flow in conductors, EM power density (Poynting)

**Second half (Final):**
- Normal incidence: Γ, τ, power reflection/transmission
- Oblique incidence: Snell's law, lateral displacement
- Fresnel coefficients (perpendicular, parallel polarization)
- Critical angle, Brewster angle, total internal reflection
- Fiber optics
- Rectangular waveguides: TE/TM modes, cutoff, dispersion
- Wave impedance, phase and group velocity, ω-β diagrams
- Dipole antennas, beam parameters (HPBW, $\Omega_p$, $D$)
- Friis transmission, effective area
