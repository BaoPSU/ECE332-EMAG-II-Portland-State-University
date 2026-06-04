# Focus: Snell's Law, Lateral Displacement, Fiber Optics

**Cheat sheet location:** Page 1 — `SNELL'S LAW — OBLIQUE INCIDENCE`, `LATERAL DISPLACEMENT` (with layered-slab diagram)

---

## What the instructor emphasized (Lecture 19 review)

- **Snell's law of reflection:** θ_r = θ_i (always)
- **Snell's law of refraction:** sin θ_t / sin θ_i = n₁/n₂ = √(μ_r1·ε_r1)/√(μ_r2·ε_r2) (slides 25-26)
- **Index of refraction:** n = c/u_p = √(μ_r·ε_r). For nonmagnetic: n = √ε_r
- **Critical angle (TIR):** sin θ_c = n₂/n₁ — only when going dense → less dense (slides 27-28)
- **Brewster angle (polarizing angle)** θ_B∥ where parallel-pol reflection coefficient Γ∥ = 0 — the reflected wave is pure perp-polarized at this angle (slides 48-49). **NOT on cheat sheet.**
- **Fiber optics** got 8+ slides — he wants you to know:
  - Acceptance angle sin θ_a = (1/n₀)·√(n_f² − n_c²)
  - Modal dispersion τ = (l·n_f/c)·(n_f − n_c)/n_c
  - Max data rate f_p = 1/(2τ) = c·n_c/(2·l·n_f·(n_f − n_c)) (slides 29-35)
  - These are **NOT on the cheat sheet** — add to your 2-sided summary or memorize

## Likely problem types

- [ ] Snell single-boundary: find θ₂ given θ₁ and ε_r ratio
- [ ] Multilayer slab chain: track θ inside each slab using ε_r,i / ε_r,i+1
- [ ] Lateral displacement d = Σ t_i tan θ_i (angle in each slab)
- [ ] Air–slab–air shortcut: exit angle = incident angle
- [ ] Fiber optics: acceptance angle, numerical aperture (NA), TIR / critical angle

## Common gotchas

- Snell uses angles **from the normal** (not from the surface)
- For lateral displacement, the angle in each term is the angle **inside that slab**, not the incidence angle from outside
- Snell only sets angles — for reflection/transmission magnitudes you still need Fresnel (perp vs parallel)
- TIR: only happens going dense → less-dense (n₁ > n₂)
- Critical angle: sin θ_c = n₂/n₁

## Quick recall

- sin θ_t = sin θ_i · √(ε_r,1/ε_r,2) = sin θ_i · n₁/n₂
- sin θ_c = n₂/n₁ (TIR critical angle, dense → less dense)
- d = Σᵢ tᵢ tan θᵢ
- **Brewster:** θ_B∥ = tan⁻¹√(ε₂/ε₁) for nonmagnetic — at this angle, only perp-pol reflects
- **Fiber acceptance angle:** sin θ_a = (1/n₀)·√(n_f² − n_c²)
- **Fiber modal dispersion delay:** τ = (l·n_f/c)·(n_f − n_c)/n_c
- **Fiber max data rate:** f_p = 1/(2τ)

## Practice — go back to

- HW3 Problem _(fill in — lateral displacement)_
- Lecture _(fill in)_ — fiber optics block
