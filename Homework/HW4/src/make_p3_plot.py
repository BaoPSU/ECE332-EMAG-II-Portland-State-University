"""
Generate the F(theta) plot for HW4 Problem 3(c) — lambda/4 dipole normalized
radiation pattern. Saves both a rectangular plot and a polar plot.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
RECT = OUT_DIR / "HW4_P3c_rect.png"
POLAR = OUT_DIR / "HW4_P3c_polar.png"

# F(theta) = 11.66 * [(cos((pi/4)cos theta) - sqrt(2)/2) / sin theta]^2
def F(theta):
    out = np.zeros_like(theta)
    mask = np.abs(np.sin(theta)) > 1e-6   # avoid div-by-zero at 0, pi
    bracket = (np.cos((np.pi/4)*np.cos(theta[mask])) - np.sqrt(2)/2) / np.sin(theta[mask])
    out[mask] = (1/0.0858) * bracket**2
    return out

theta = np.linspace(0, np.pi, 720)
F_vals = F(theta)

# ---- Rectangular plot ----
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.plot(np.degrees(theta), F_vals, color='#0c447c', linewidth=2)
ax.axhline(0.5, color='#993c1d', linestyle='--', linewidth=0.8, label='-3 dB (half-power)')
ax.axvline(90, color='gray', linestyle=':', linewidth=0.8)
ax.set_xlabel(r'$\theta$ (degrees)')
ax.set_ylabel(r'$F(\theta)$ (normalized)')
ax.set_title(r'$\lambda/4$ dipole normalized radiation pattern $F(\theta)$')
ax.set_xlim(0, 180)
ax.set_ylim(0, 1.1)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=9)
ax.annotate('Peak F=1 at θ=90°\n(broadside)', xy=(90, 1.0), xytext=(120, 0.85),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8), fontsize=9)
ax.annotate('Axis null F=0\nat θ=0°', xy=(0, 0), xytext=(15, 0.18),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8), fontsize=9)
ax.annotate('Axis null F=0\nat θ=180°', xy=(180, 0), xytext=(135, 0.18),
            arrowprops=dict(arrowstyle='->', color='black', lw=0.8), fontsize=9)
plt.tight_layout()
plt.savefig(RECT, dpi=180, bbox_inches='tight')
plt.close(fig)
print(f"Saved {RECT}")

# ---- Polar plot ----
# Mirror to negative theta for full 0->2pi range, antenna along y-axis (theta from z-axis convention)
fig = plt.figure(figsize=(5.5, 5.5))
ax = fig.add_subplot(111, projection='polar')

# Convention: 0 deg at top (z-axis = dipole axis), increasing clockwise
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Full pattern: theta 0->pi (right side) mirrored to -pi->0 (left side, by symmetry)
theta_full = np.concatenate([-theta[::-1], theta])
F_full = np.concatenate([F_vals[::-1], F_vals])

ax.plot(theta_full, F_full, color='#0c447c', linewidth=2)
ax.fill(theta_full, F_full, color='#0c447c', alpha=0.15)

# -3 dB ring
hpbw_circle = np.linspace(0, 2*np.pi, 200)
ax.plot(hpbw_circle, [0.5]*200, color='#993c1d', linestyle='--', linewidth=0.8)

ax.set_rmax(1.05)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'], fontsize=8)
ax.set_xticks(np.deg2rad(np.arange(0, 360, 30)))
ax.set_title(r'$\lambda/4$ dipole $F(\theta)$ — polar view' + '\n(antenna along vertical axis)',
             fontsize=11, pad=14)
plt.tight_layout()
plt.savefig(POLAR, dpi=180, bbox_inches='tight')
plt.close(fig)
print(f"Saved {POLAR}")

# HPBW interpolation
# Find where F drops to 0.5
i_left = np.argmin(np.abs(F_vals[:len(F_vals)//2] - 0.5))
i_right = len(F_vals)//2 + np.argmin(np.abs(F_vals[len(F_vals)//2:] - 0.5))
hpbw = np.degrees(theta[i_right] - theta[i_left])
print(f"HPBW (from plot): {hpbw:.1f} deg")
