"""
Generate the F(theta) plot for HW4 Problem 3(c) - lambda/4 dipole normalized
radiation pattern. Styled to match the answer key's P2 plot:
  - dashed half-power marker at F = 0.5
  - vertical dashed lines at theta_1/2 points
  - beta double-headed arrow
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
RECT = OUT_DIR / "HW4_P3c_rect.png"

# F(theta) = (1/0.0858) * [(cos((pi/4)cos theta) - sqrt(2)/2) / sin theta]^2
def F(theta):
    out = np.zeros_like(theta)
    mask = np.abs(np.sin(theta)) > 1e-6
    bracket = (np.cos((np.pi/4)*np.cos(theta[mask])) - np.sqrt(2)/2) / np.sin(theta[mask])
    out[mask] = (1/0.0858) * bracket**2
    return out

theta = np.linspace(0, np.pi, 1440)
F_vals = F(theta)

# Find the half-power angles theta1/2 (where F = 0.5) on each side of peak (pi/2)
half_idx = len(F_vals) // 2
i_left = np.argmin(np.abs(F_vals[:half_idx] - 0.5))
i_right = half_idx + np.argmin(np.abs(F_vals[half_idx:] - 0.5))
theta_left = theta[i_left]
theta_right = theta[i_right]
beta = theta_right - theta_left
print(f"theta1/2 left  = {np.degrees(theta_left):.2f} deg")
print(f"theta1/2 right = {np.degrees(theta_right):.2f} deg")
print(f"HPBW beta      = {beta:.4f} rad = {np.degrees(beta):.2f} deg")

# ---- Plot ----
fig, ax = plt.subplots(figsize=(7, 4.8))
ax.plot(theta, F_vals, color='blue', linewidth=1.2)

# Dashed half-power marker at F = 0.5
ax.plot([theta_left, theta_right], [0.5, 0.5],
        color='gray', linestyle='--', linewidth=0.8)
# Vertical dashed lines from F-axis (0) up to the curve at theta_1/2 points
ax.plot([theta_left, theta_left], [0, 0.5],
        color='gray', linestyle='--', linewidth=0.8)
ax.plot([theta_right, theta_right], [0, 0.5],
        color='gray', linestyle='--', linewidth=0.8)

# "0.5" label on the half-power level
ax.text(np.pi/2 + 0.04, 0.52, '0.5', fontsize=10, ha='left', va='bottom')

# beta double-headed arrow between the two theta_1/2 points (slightly below 0.5)
arrow_y = 0.36
ax.annotate('', xy=(theta_right, arrow_y), xytext=(theta_left, arrow_y),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.0))
ax.text((theta_left + theta_right)/2, arrow_y + 0.02, r'$\beta = 1.52$ rad',
        fontsize=13, ha='center', va='bottom')

# theta1/2 tick labels under the x-axis
ax.text(theta_left, -0.03, r'$\theta_{1/2}$', fontsize=10, ha='center', va='top')
ax.text(theta_right, -0.03, r'$\theta_{1/2}$', fontsize=10, ha='center', va='top')

ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$F(\theta)$')
ax.set_xlim(0, np.pi)
ax.set_ylim(0, 1.05)

# X ticks in radians (drop pi/4 and 3pi/4 so theta_1/2 labels don't collide)
ax.set_xticks([0, np.pi/2, np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$'])
ax.set_yticks(np.arange(0, 1.01, 0.1))

ax.tick_params(direction='out', length=4, width=0.6)
for spine in ax.spines.values():
    spine.set_linewidth(0.6)

plt.tight_layout()
plt.savefig(RECT, dpi=200, bbox_inches='tight')
plt.close(fig)
print(f"Saved {RECT}")
