# Focus: Beam Parameters (β, Ω_p, D) and Effective Area A_e

**Cheat sheet location:** Page 2 — `BEAM PARAMETERS — β, Ω_p, D` (5-step recipe), `EFFECTIVE AREA A_e`

---

## What the instructor emphasized

_(Drop bullets here)_

- 
- 
- 

## Likely problem types

- [ ] Compute HPBW β from F(θ) — set F = 0.5, solve for θ_{1/2}, β = 2θ_{1/2}
- [ ] Pattern solid angle Ω_p via 2π ∫ F(θ) sin θ dθ (calculator or Gaussian shortcut)
- [ ] Directivity D = 4π/Ω_p (and D_dB = 10 log₁₀ D)
- [ ] Gain G = ξD when efficiency ξ given (lossless: G = D)
- [ ] Effective area A_e = λ²D/(4π) (and inverse: D from A_e)
- [ ] Compare A_e to physical area A_p (thin-wire dipole: A_e ≫ A_p)
- [ ] Alt directivity from two orthogonal HPBWs: D ≈ 4π/(β_xz β_yz)

## Common gotchas

- F(θ) MUST be normalized first (S/S_max) — Step 1 of the recipe
- β is the FULL width at half power, = 2θ_{1/2}, not just θ_{1/2}
- TI-36X Pro for the Ω_p integral: `[2nd][d/dx]` for ∫, RAD mode, multiply by 2π at the end
- For Gaussian F = e^(−aθ²): θ_{1/2} = √(ln 2 / a) — pre-derived shortcut
- D is unitless. D_dB requires 10 log (power-like quantity), not 20 log
- A_e uses λ², not λ — common slip
- A_p for half-wave wire = (λ/2) · d_wire (length × diameter)

## Quick recall

- F(θ) = S(θ)/S_max → β = 2θ_{1/2} where F = 0.5
- Ω_p = 2π ∫₀^π F(θ) sin θ dθ (no ϕ dependence)
- D = 4π/Ω_p ; D_dB = 10 log₁₀ D
- A_e = λ²D/(4π) ; A_e^Hertz = 3λ²/(8π) ≈ 0.119λ²

## Practice — go back to

- HW4 Problem 2 (Gaussian F → β, Ω_p, D)
- HW4 Problem 4 (A_e vs A_p for half-wave at 100 MHz)
- Lecture _(fill in)_ — beam parameters derivation
