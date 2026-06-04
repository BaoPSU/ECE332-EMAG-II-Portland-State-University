# Focus: Dipole Antennas — Hertzian, Arbitrary, Half-wave, λ/4

**Cheat sheet location:** Page 2 — `DIPOLE TYPE BY LENGTH`, `HERTZIAN DIPOLE — S(R,θ)`, `ARBITRARY-LENGTH DIPOLE — S(θ)`, `COMMON DIPOLE PARAMETERS`

---

## What the instructor emphasized

_(Drop bullets here)_

- 
- 
- 

## Likely problem types

- [ ] Classify dipole by l/λ ratio → pick the right formula
- [ ] Hertzian S(R,θ) power density at a given (R, θ)
- [ ] Arbitrary-length S(θ) with the (cos(πl/λ cos θ) − cos(πl/λ))/sin θ kernel
- [ ] Half-wave or quarter-wave specialization (S_max = 0.0858 S₀ for λ/4)
- [ ] Find θ_max (broadside = π/2 for symmetric dipoles)
- [ ] Total radiated power P_rad, radiation resistance R_rad
- [ ] R_rad ↔ P_rad ↔ I₀ identities

## Common gotchas

- **Step 0 always:** compute λ = c/f first, then ratio l/λ — this routes you to the right formula
- If l/λ < 1/50, STOP and use Hertzian (do NOT plug small l into the arbitrary formula — wrong shape)
- At θ = 0 or π in the ARB formula, the bracket is 0/0 → L'Hôpital gives S = 0 (axial null)
- Calculator: RAD mode, antenna formulas almost always take θ in radians
- η₀ = 120π ≈ 377 Ω, k = 2π/λ — don't confuse these with each other

## Quick recall

| Type | l | D | D_dB | R_rad (Ω) | θ_max |
|---|---|---|---|---|---|
| Isotropic | N/A | 1 | 0 | — | — |
| Hertzian | < λ/50 | 1.5 | 1.76 | 80π²(l/λ)² | π/2 |
| Half-wave | λ/2 | 1.64 | 2.15 | 73.2 | π/2 |
| λ/4 monopole | λ/4 (gnd) | 1.64 | 2.15 | 36.6 | π/2 |
| Full-wave | λ | 2.41 | 3.82 | 199 | π/2 |

For λ/4 dipole: S_max ≈ 0.0858 S₀ where S₀ = 15I₀²/(πR²)

## Practice — go back to

- HW4 Problems 1 (Hertzian), 3 (λ/4 dipole), 5 (half-wave)
- Lecture _(fill in)_ — dipole pattern derivation
