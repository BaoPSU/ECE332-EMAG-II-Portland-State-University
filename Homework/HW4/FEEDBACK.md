# HW4 — TA Feedback

**Grade:** 88 / 88 (100%)
**Submitted:** June 5, 2026 at 11:46 AM
**Returned:** June 10, 2026

## Comments

All 8 problems marked full points:

| Problem | Score | Topic |
|---|---|---|
| P1 | 8/8 | Hertzian dipole, $S(R,\theta)$ at 5 km, 45° |
| P2 | 15/15 | Beam parameters from $F(\theta)=e^{-20\theta^2}$ (HPBW, $\Omega_p$, $D$) |
| P3 | 15/15 | $\lambda/4$ dipole pattern: $\theta_\text{max}$, $S_\text{max}$, plot $F(\theta)$ |
| P4 | 5/5 | Effective area vs physical area, half-wave dipole at 100 MHz |
| P5 | 5/5 | Friis link, half-wave TV broadcast |
| P6 | 15/15 | Comm link with SNR, $G_t=20$ dB, $G_r=23$ dB |
| P7 | 15/15 | Circular aperture scaling ($D$, $\beta$ under area / freq doubling) |
| P8 | 10/10 | 5-element linear broadside array, $d=3\lambda/4$ |

### TA correction note (P1)

The TA crossed out the original unit `pW/m²` and wrote `nW/m²` to flag the correct unit.
The numerical value $1.51 \times 10^{-9}$ W/m² is correct; the prefix should be **nano** (n), not **pico** (p).

$$1\;\text{nW} = 10^{-9}\;\text{W},\quad 1\;\text{pW} = 10^{-12}\;\text{W}$$

So $1.51 \times 10^{-9}$ W/m² = $1.51$ nW/m², not pW/m². Full credit awarded despite the unit slip.

## Takeaways

- **Always check SI prefix carefully against the exponent.** $10^{-9} \to$ nano (n), $10^{-12} \to$ pico (p), $10^{-6} \to$ micro (μ), $10^{-3} \to$ milli (m). One letter off gives a 1000× error.
- The Hertzian routing through DIPOLE TYPE BY LENGTH worked cleanly: $l/\lambda < 1/50$ classified the dipole, $S(R,\theta) = \eta_0 k^2 I_0^2 l^2 / (32\pi^2 R^2) \sin^2\theta$ plugged in directly.
- HW4 cheat sheet's coverage was complete enough that no problem required deriving anything off-sheet. The Generate doc cross-references held up.
- For aperture scaling (P7) and array HPBW (P8): the proportionality method beats re-computing absolute numbers. Read `D ∝ A_p/λ²`, `β ∝ λ/√A_p`, multiply ratios, done.
