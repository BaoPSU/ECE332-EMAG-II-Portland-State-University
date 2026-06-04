# Focus: Friis Transmission, Link Budget, Noise / SNR

**Cheat sheet location:** Page 2 — `FRIIS TRANSMISSION FORMULA`, `dB ↔ LINEAR`, `NOISE & SNR`

---

## What the instructor emphasized

_(Drop bullets here)_

- 
- 
- 

## Likely problem types

- [ ] Friis link budget: find P_r given G_t, G_r, R, P_t, f
- [ ] Power density at RX: S_r = G_t P_t / (4π R²)
- [ ] Max range: solve Friis for R given minimum P_r threshold
- [ ] Off-axis Friis: include F_t(θ,ϕ) F_r(θ,ϕ) when patterns not peak-aligned
- [ ] Noise power P_N = k_B T_sys B
- [ ] SNR = P_r / P_N (linear) or 10 log₁₀(P_r / P_N) (dB)
- [ ] dB ↔ linear conversion for any quantity (G, D, P_r/P_t, SNR)

## Common gotchas

- **Convert dB to linear FIRST** before plugging into Friis (G_lin = 10^(G_dB/10))
- For half-wave dipole TX/RX, G = 1.64 (lossless ξ = 1, so G = D)
- 3 dB = ×2, 10 dB = ×10, 20 dB = ×100, 30 dB = ×1000 — memorize
- λ = c/f BEFORE using Friis (everyone forgets this when given f in GHz)
- For E-field amplitude (not power): use 20 log not 10 log
- k_B = 1.38 × 10⁻²³ J/K — units of P_N work out to W when T in K, B in Hz
- Watch the prefix on the answer: nW, μW, mW — easy to miss a factor of 1000

## Quick recall

- S_r = G_t P_t / (4π R²) (W/m²)
- P_r = G_t G_r (λ/(4π R))² P_t (W)
- R = (λ/(4π)) √(G_t G_r P_t / P_r) — solve for range
- P_N = k_B T_sys B (W)
- SNR_dB = 10 log₁₀(P_r / P_N)
- Free-space path loss: L_fs = (4π R/λ)²

## Practice — go back to

- HW4 Problem 5 (half-wave TV broadcast, 3 dB RX)
- HW4 Problem 6 (full link budget with noise: S_r, P_r, SNR)
- Lecture _(fill in)_ — Friis derivation
