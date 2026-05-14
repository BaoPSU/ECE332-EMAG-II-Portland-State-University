# Final Exam Coverage

**Exam date:** TBD (end of Spring 2026 term)
**Weight:** 25% of course grade
**Cumulative?** No. The final covers only the second half of the course.

> "The midterm will cover the first half of the course and the final exam will cover the second half of the course. The final exam will not be cumulative."
> — ECE332 Spring 2026 syllabus, Method of Evaluation

## Lectures
Lecture **11 onward** (post-midterm material): lectures 11, 12, 13, …

## Homework
HW3 (boundary problems + waveguides) and HW4 (antennas + Friis).

## Topics
- Normal incidence: Γ, τ, power reflection/transmission
- Lossy media: 5-case classification (lossless / low-loss / quasi-conductor / good conductor / magnetic)
- Snell's law, lateral displacement through layered slabs
- Fresnel coefficients for perpendicular and parallel polarization
- Critical angle (TIR), Brewster angle, polarizing angle
- Fiber optics (acceptance angle, numerical aperture)
- Rectangular waveguides: TE/TM modes, cutoff frequency, dispersion
- Wave impedance, phase velocity, group velocity, ω-β diagrams
- Dipole antennas: Hertzian, arbitrary length, half-wave
- Beam parameters: HPBW, pattern solid angle Ω_p, directivity D
- Effective area A_e, Friis transmission, radar equation

## Related labs
- Lab 3 (Waveguides) — connects to waveguide modes, cutoff, group velocity
- Lab 4 (Patch Antenna) — connects to antenna radiation patterns, polarization, far-field

## Cheat sheet
**Built and active:** `src/ECE332_Final_cheatsheet.tex` → `ECE332_Final_cheatsheet.pdf` (2 pages).

Page 1 sections (in order):
- NORMAL INCIDENCE — Γ and τ
- Ẽ PHASOR TEMPLATES (direction table, polarization unit vectors)
- POWER REFLECTION & TRANSMISSION
- LOSSY MEDIA — 5 CASES (decision table with η_c, α, β formulas)
- SNELL'S LAW — OBLIQUE INCIDENCE
- LATERAL DISPLACEMENT (with common arctan values)
- FRESNEL OBLIQUE — Γ, τ, R, T (critical angle, Brewster)
- TABLE 8-2 — Γ, τ, R, T SUMMARY (normal / perp / parallel side-by-side)
- FIBER OPTICS
- RECTANGULAR WAVEGUIDE — MODES
- TABLE 8-3 — FULL FIELD COMPONENTS (TE/TM full set + TEM reference)
- CUTOFF FREQUENCY (common cutoffs table)
- ε_r FROM DISPERSION
- WAVE IMPEDANCE & H_y
- GROUP VELOCITY & TRAVEL TIME
- Bottom strip glossary: BOUNDARY / SNELL / WAVEGUIDE / VELOCITIES / POWER

Page 2 sections (antennas):
- DIPOLE TYPE BY LENGTH (Hertzian / short / half-wave / arbitrary)
- HERTZIAN DIPOLE — S(R,θ)
- ARBITRARY-LENGTH DIPOLE — S(θ)
- BEAM PARAMETERS — HPBW, Ω_p, D
- COMMON DIPOLE PARAMETERS (D, R_rad, A_e for standard lengths)
- EFFECTIVE AREA A_e
- POWER FLOW IDENTITIES
- FRIIS TRANSMISSION FORMULA
- dB ↔ LINEAR conversion
- RADAR EQUATION (bonus)
- ANTENNA INTEGRATION TIPS
- Bottom strip glossary: DIPOLE / RADIATION / ANTENNA / FRIIS / RADAR

## Source references
Original textbook tables saved at `Notes/Textbook/tables/`:
- `Table_8-2_reflection_transmission.png`
- `Table_8-3_waveguide_fields.png`
