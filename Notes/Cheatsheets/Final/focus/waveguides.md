# Focus: Rectangular Waveguides + Cavity Resonators, Modes, Cutoff, Group Velocity

**Cheat sheet location:** Page 1 — `RECTANGULAR WAVEGUIDE — MODES`, `TABLE 8-3 — FULL FIELD COMPONENTS`, `CUTOFF FREQUENCY`, `ε_r FROM DISPERSION`, `GROUP VELOCITY & TRAVEL TIME`

---

## What the instructor emphasized (Lecture 19 review)

- Dominant modes: **TE₁₀** for TE, **TM₁₁** for TM (slide 61)
- Table 8-3 covers all field components for TE_mn, TM_mn, and TEM reference — **he provides this on the exam**
- Cutoff wavenumber identity: k_c² = k² − β² = ω²με − β² (slide 59)
- Phase velocity u_p > u_p0, group velocity u_g < u_p0, and u_p·u_g = u_p0² (slide 64)
- ω-β diagrams: mode mn starts at ω = 2πf_mn at β = 0; TEM line is straight; modes approach TEM as f → ∞ (slide 65)
- **Cavity resonators** (slides 67-68) — NEW topic, NOT on the cheat sheet:
  - Cavity = waveguide with metal end-caps; supports only resonant modes
  - f_mnp = (u_p0/2)·√((m/a)² + (n/b)² + (p/d)²)
  - TM modes: m,n start at 1, p starts at 0
  - TE modes: m,n start at 0, p starts at 1
  - Quality factor Q ≈ f_mnp/Δf (Δf = bandwidth at f_mnp/√2 amplitude)

## Likely problem types

- [ ] Identify TE_mn vs TM_mn from a given field expression
- [ ] Compute cutoff f_mn for a given mode
- [ ] Determine the dominant mode (TE_10) and which modes propagate at a given f
- [ ] Use Table 8-3 to write all 6 field components from H̃_z (TE) or Ẽ_z (TM)
- [ ] Wave impedance Z_TE / Z_TM at a given frequency
- [ ] Phase velocity u_p, group velocity u_g, travel time t = L/u_g
- [ ] Find ε_r from a measured β at known frequency / mode

## Common gotchas

- TE allows m=0 OR n=0 (one zero ok); TM forbids both — so TE_10 exists, TM_10 does NOT
- a > b convention (a is wide dimension along x̂)
- Propagation requires f > f_mn; otherwise wave is evanescent
- In Z_TE/TM and u_g formulas, f_c is the cutoff of the SPECIFIC mode you're using
- u_p · u_g = u_p0² (always)
- Higher modes have lower u_g → arrive later → multi-mode dispersion

## Quick recall

- f_mn = (u_p0/2) √((m/a)² + (n/b)²)
- u_p0 = c/√ε_r (hollow waveguide: u_p0 = c)
- TE_10 cutoff: f_10 = u_p0/(2a) — dominant mode (waveguide)
- TM_11 dominant for TM
- β = k √(1 − (f_c/f)²)
- Z_TE = η/√(1−(f_c/f)²) > η ; Z_TM = η·√(1−(f_c/f)²) < η
- **Cavity resonance:** f_mnp = (u_p0/2)·√((m/a)² + (n/b)² + (p/d)²)
- **Quality factor:** Q ≈ f_mnp/Δf

## Practice — go back to

- HW3 Problem _(fill in — waveguide travel time, dispersion)_
- Lab 3 (Waveguides) — connects directly
- Lecture _(fill in)_ — TE/TM derivation
