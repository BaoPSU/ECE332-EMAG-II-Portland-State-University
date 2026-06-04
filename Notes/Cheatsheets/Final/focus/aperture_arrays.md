# Focus: Aperture Antennas + Linear Antenna Arrays

**Cheat sheet location:** Page 2 — `APERTURE ANTENNAS (horn, dish)` (shape + scaling tables), `LINEAR ANTENNA ARRAY`

---

## What the instructor emphasized

_(Drop bullets here)_

- 
- 
- 

## Likely problem types

**Aperture (horn / dish):**
- [ ] Directivity from physical area: D ≈ 4π A_p/λ²
- [ ] Directivity from beamwidths: D ≈ 4π/(β_xz β_yz) or circular: D ≈ 4π/β²
- [ ] HPBW by shape:
  - Rectangular: β ≈ 0.88λ/ℓ
  - Square: β ≈ 0.88λ/ℓ
  - Circular: β ≈ 1.02λ/d
- [ ] Scaling: double area → 2D, β/√2 ; double freq → 4D, β/2

**Linear array:**
- [ ] Write array factor F_a(θ) for N elements, spacing d
- [ ] Uniform amplitude + equal phase: closed form sin²(Nγ/2)/sin²(γ/2), γ = kd cos θ
- [ ] Normalize: F_a^norm = F_a / N²
- [ ] HPBW (broadside, uniform): β ≈ 0.88 λ/(Nd)
- [ ] Identify broadside vs steered beam from phase scheme
- [ ] Watch for grating lobes when d > λ

## Common gotchas

- β formulas use rad — convert from degrees first if needed
- For aperture D ≈ 4πA_p/λ², A_e ≈ A_p (almost equal, unlike thin-wire dipoles)
- Array HPBW: use **N·d**, NOT (N−1)·d — the formula bakes in the right convention
- Peak of unnormalized F_a is N² at γ = 0 (broadside, θ = π/2). Always normalize by N².
- Progressive phase ψ_i = iα steers beam to cos θ_max = −α/(kd)
- Grating lobes: if d > λ for broadside, you get extra main lobes at unwanted angles — usually avoid

## Quick recall

- D ≈ 4π A_p/λ² (aperture)
- D ≈ 4π/β² (circular aperture or single-lobe symmetric)
- β ≈ 1.02λ/d (circular dish, d = diameter)
- F_a^uniform = sin²(Nγ/2)/sin²(γ/2), γ = kd cos θ
- F_a^max = N² at θ = π/2 (broadside)
- β_array ≈ 0.88 λ/(Nd) (broadside, uniform)

## Practice — go back to

- HW4 Problem 7 (circular aperture, scaling area / frequency)
- HW4 Problem 8 (5-element uniform array, d = 3λ/4)
- Lecture _(fill in)_ — aperture antennas and array factor
