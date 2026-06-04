# Focus: Boundaries — Γ, τ, R, T, Lossy Media

**Cheat sheet location:** Page 1 — `Ẽ PHASOR TEMPLATES`, `TABLE 8-2`, `POWER REFLECTION & TRANSMISSION`, `LOSSY MEDIA — 5 CASES`

---

## What the instructor emphasized (Lecture 19 review)

- Normal incidence in **lossless** AND **lossy** media — both Γ and τ become complex in lossy case (slides 8-23)
- **Standing wave ratio** S = (1+|Γ|)/(1−|Γ|) and the standing-wave maxima/minima positions l_max, l_min in Medium 1 (slides 12-16) — **NOT on the cheat sheet, must memorize**
- For lossless media: θ_Γ = 0 if η₂ > η₁; θ_Γ = π if η₂ < η₁
- T-line analogy (Table 8-1) — plane wave at boundary behaves like a T-line at characteristic-impedance discontinuity (slides 13-14)
- Power flow: S_av,1 = (|E₀|²/2η₁)(1−|Γ|²), S_av,2 = (|τ|²·|E₀|²/2η₂), and power is conserved (slides 19-20)
- Real-world examples he called out: yellow light on glass (windows, lenses), radio waves on metal (mirrors, shielding, filters)

## Likely problem types

- [ ] Compute Γ, τ for normal incidence given η₁, η₂
- [ ] Compute %P_r, %P_t (watch the η₁/η₂ factor on %P_t)
- [ ] Classify a medium into lossless / low-loss / quasi-cond / good cond / magnetic
- [ ] Find α, β, η_c in the right regime
- [ ] Write Ẽⁱ, Ẽʳ, Ẽᵗ phasor templates given direction + polarization

## Common gotchas

- Default μ_r = 1 (nonmagnetic) unless explicitly stated
- η₀/√ε_r is the shortcut, but only valid when μ_r = 1
- For Γ/τ in low-loss case, drop the `j` correction term and use plain η₀/√ε_r
- %P_t is NOT just |τ|² — multiply by (η₁/η₂)
- Magnetic media: keep full √(μ_r/ε_r)·η₀

## Quick recall

- Γ = (η₂−η₁)/(η₂+η₁) at normal incidence
- τ = 1 + Γ always
- %P_r + %P_t = 100 (sanity check)
- η₀ = 120π ≈ 377 Ω
- **Standing wave ratio:** S = (1+|Γ|)/(1−|Γ|) — ranges from 1 (matched) to ∞ (total reflection)
- **l_max position** (E maxima in Medium 1): l_max = −z = (θ_Γ·λ₁)/(4π) + n·λ₁/2 (slide 15)
- **l_min position:** l_min = l_max ± λ₁/4

## Practice — go back to

- HW3 Problem _(fill in)_
- Lecture _(fill in)_ examples
