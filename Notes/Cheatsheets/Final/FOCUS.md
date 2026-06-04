# Final Exam — Focus Guide

> **Source:** Lecture 19 (`Notes/lecture19.pdf`) is the official final review. Everything below is pulled from it. Lecture 18 is supporting prep material.

---

## Logistics (confirmed in Lecture 19, slides 1-5)

- **Date:** Tuesday, June 9, 2026, 1:30–3:20 pm
- **Location:** FAB 48, in person, on paper
- **Coverage:** Chapters 8 & 9 (everything post-midterm)
- **Cheat sheet allowed:** **Two-sided, 1-page** summary of your own facts/formulas — exactly what `ECE332_Final_cheatsheet.pdf` is (2 PDF pages = 2 sides). He will NOT collect cheat sheets.
- **Calculator:** FE-exam approved (trig, exp, log only). [List of approved calculators on Canvas.]
- **Calculus must be done by hand.** No CAS allowed.
- **Tables provided:** Mark said *"I will provide any needed tables."* → Tables 8-2 (Γ/τ/R/T) and 8-3 (waveguide field components) will be on the exam.
- **Textbook + other electronic devices:** NOT allowed.
- **Show all work** — partial credit needs visible work.
- He'll display a clock and announce time points.

---

## Topics from the review (Lecture 19 outline)

Chapters 8 & 9. From slides 2-3:

### Chapter 8 — Reflection / Transmission / Waveguides
1. **Reflection and transmission at a boundary**
   - Normal incidence (lossless + lossy)
   - Geometric optics — Snell's laws, critical angle, TIR, fiber optics
   - General oblique incidence — perp & parallel polarization, Brewster angle, R, T
2. **Waveguides and Cavities** ← cavities is the only sub-topic not already on the cheat sheet

### Chapter 9 — Radiation and Antennas
3. **Quantities that characterize antennas** (pattern, polarization, impedance)
4. **Effective area of a receiving antenna**
5. **Current-source antennas** — dipole antennas (Hertzian / half-wave / quarter-wave / arbitrary)
6. **Aperture-field antennas** — large aperture antennas (horn, dish)
7. **Antenna arrays** — linear arrays, **electronic steering / scanning** ← steering & frequency scanning are new

---

## What's on the cheat sheet vs what's NEW (gaps to know cold without the sheet)

The current Final cheat sheet covers most of the above. These items showed up in Lecture 19 but are **not** explicitly on the sheet — memorize or add to your two-sided cheat sheet.

| Topic | Status on cheat sheet | What lecture 19 wants you to know |
|---|---|---|
| Standing wave ratio S = (1+\|Γ\|)/(1−\|Γ\|) | ❌ missing | l_max position formula; θ_Γ = 0 if η₂>η₁, π if η₂<η₁ (slides 12-16) |
| Brewster (polarizing) angle θ_B∥ = tan⁻¹√(ε₂/ε₁) | ❌ missing | At θ_B∥, parallel-pol fully transmitted → reflected wave is perp-pol only (slides 48-49) |
| Fiber optics: acceptance angle sin θ_a = (1/n₀)√(n_f²−n_c²) | ❌ missing | Modal dispersion τ = (l·n_f/c)(n_f−n_c)/n_c, max data rate f_p = 1/(2τ) (slides 29-35) |
| Cavity resonators: f_mnp = (u_p0/2)√((m/a)²+(n/b)²+(p/d)²) | ❌ missing | Q ≈ f_mnp/Δf; TM: m,n≥1, p≥0; TE: m,n≥0, p≥1 (slides 67-68) |
| Electronic steering: ψ_i = −iδ, δ = (2πd/λ)cos θ₀ | ❌ missing | Broadside θ₀=π/2 (δ=0); end-fire θ₀=0 (δ=kd) (slides 110-112) |
| Frequency scanning: cos θ₀ ≈ (n₀λ₀/d)(Δf/f₀) | ❌ missing | Steers beam by changing freq, not phase (slides 113-115) |

Everything else (Γ/τ, lossy media, Snell, waveguide modes, Hertzian/half-wave/λ/4 dipoles, beam params, Friis, dB↔lin, noise/SNR, aperture, linear array uniform broadside) is on the sheet.

---

## Topic guides

Drill-down notes per topic. Each has the same skeleton.

1. [focus/boundaries.md](focus/boundaries.md) — Reflection / transmission (Γ, τ, R, T, lossy media, **standing wave ratio**)
2. [focus/snell_optics.md](focus/snell_optics.md) — Snell, lateral displacement, **fiber optics formulas**, **Brewster**
3. [focus/waveguides.md](focus/waveguides.md) — Rectangular waveguides + **cavity resonators**, modes, cutoff, group velocity
4. [focus/antennas.md](focus/antennas.md) — Dipoles (Hertzian / λ/4 / λ/2 / arbitrary)
5. [focus/beam_and_area.md](focus/beam_and_area.md) — HPBW, Ω_p, D, A_e, receiving antenna circuit
6. [focus/friis_noise.md](focus/friis_noise.md) — Friis, link budget, SNR
7. [focus/aperture_arrays.md](focus/aperture_arrays.md) — Aperture antennas + linear arrays + **electronic steering** + **frequency scanning**

---

## Exam-day plan

- **Time budget:** ~1h 50min total. If 8 problems → ~13 min each. Spend the last 10 min sanity-checking units and final boxed answers.
- **Cheat sheet quick-routing:**
  - Boundary problem? → page 1, hit `DIPOLE TYPE BY LENGTH` (page 2) or `TABLE 8-2` (page 1) lookup first
  - Antenna problem? → page 2, start with `DIPOLE TYPE BY LENGTH`, then `BEAM PARAMETERS` recipe
  - Friis problem? → page 2 column 3, follow the 4-step recipe
  - dB anywhere? → page 2 `dB ↔ LINEAR` lookup table (3 dB = ×2 etc.)
- **Step 0 always:** compute λ = c/f first. Boxed at top of `DIPOLE TYPE BY LENGTH` on page 2.
- **RAD mode on calculator** for antennas (β, sin θ, cos θ in formulas).
- **Convert dB → linear before plugging** into Friis or noise/SNR.

---

## Lecture references

| Lecture | Topic | Status |
|---|---|---|
| 11 | _(fill in)_ | uploaded |
| 12 | _(fill in)_ | uploaded |
| 13 | _(fill in)_ | uploaded |
| 14 | _(fill in)_ | uploaded |
| 15 | _(fill in)_ | uploaded |
| 16 | _(fill in)_ | uploaded |
| 17 | _(fill in)_ | uploaded |
| **18** | _(fill in)_ | uploaded |
| **19** | **Final review (Exam 2)** — full coverage rundown of Chapters 8 + 9 | uploaded |

---

## Related files

- `COVERAGE.md` — official coverage summary (lectures, topics, cheat sheet section index)
- `src/ECE332_Final_cheatsheet.tex` — combined cheat sheet source (2 sides, exam-allowed)
- `../../Homework/HW3/`, `../../Homework/HW4/` — graded problem walkthroughs
