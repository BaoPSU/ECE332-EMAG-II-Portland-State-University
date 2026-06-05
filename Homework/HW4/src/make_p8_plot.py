"""
Generate the F_a^norm(theta) plot for HW4 Problem 8 — 5-element uniform broadside
linear array, spacing d = 3*lambda/4. Style matches answer-key conventions:
  - Rectangular plot, theta in 0..pi (rad)
  - F_a^norm on y-axis (0..1)
  - Thin black/blue line
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
OUT = OUT_DIR / "HW4_P8_array_pattern.png"

# Array params
N = 5
d_lambda = 3 / 4   # d = (3/4) lambda, expressed as multiple of lambda
# kd = 2pi/lambda * d = 2pi * (3/4) = 3pi/2
kd = 2 * np.pi * d_lambda

def Fa_norm(theta):
    gamma = kd * np.cos(theta)
    # closed form: sin^2(N*gamma/2) / sin^2(gamma/2), normalized by N^2
    # handle gamma -> 0 (and multiples of 2*pi where denominator -> 0): limit = N^2
    out = np.zeros_like(theta)
    half = gamma / 2.0
    sin_half = np.sin(half)
    mask = np.abs(sin_half) > 1e-9
    out[mask] = (np.sin(N * half[mask]) ** 2) / (sin_half[mask] ** 2)
    out[~mask] = N ** 2
    return out / (N ** 2)

theta = np.linspace(0, np.pi, 2000)
Fa = Fa_norm(theta)

fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(theta, Fa, color='blue', linewidth=1.2)

ax.set_xlabel(r'$\theta$ (rad)')
ax.set_ylabel(r'$F_a^{\,\mathrm{norm}}(\theta)$')
ax.set_title(r'5-element uniform broadside array, $d = 3\lambda/4$')

ax.set_xlim(0, np.pi)
ax.set_ylim(0, 1.05)

# x ticks at 0, pi/4, pi/2, 3pi/4, pi
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
ax.set_xticklabels(['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$'])
ax.set_yticks(np.arange(0, 1.01, 0.1))

# Mark broadside peak
ax.axvline(np.pi/2, color='gray', linestyle=':', linewidth=0.7)
ax.annotate('Main lobe\n(broadside)', xy=(np.pi/2, 1.0), xytext=(np.pi/2 + 0.3, 0.85),
            fontsize=9, arrowprops=dict(arrowstyle='->', color='black', lw=0.6))

# Mark HPBW with horizontal line at 0.5
ax.axhline(0.5, color='red', linestyle='--', linewidth=0.7, alpha=0.7)
ax.text(0.05, 0.52, '0.5 (-3 dB)', fontsize=8, color='red')

ax.tick_params(direction='out', length=4, width=0.6)
for spine in ax.spines.values():
    spine.set_linewidth(0.6)

plt.tight_layout()
plt.savefig(OUT, dpi=200, bbox_inches='tight')
plt.close(fig)
print(f"Saved {OUT}")

# HPBW from plot
half_idx = len(Fa) // 2
i_left = np.argmin(np.abs(Fa[:half_idx] - 0.5))
i_right = half_idx + np.argmin(np.abs(Fa[half_idx:] - 0.5))
hpbw_rad = theta[i_right] - theta[i_left]
print(f"HPBW (from plot): {hpbw_rad:.4f} rad = {np.degrees(hpbw_rad):.2f} deg")
