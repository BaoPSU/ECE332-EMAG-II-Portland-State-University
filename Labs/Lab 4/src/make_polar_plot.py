"""
Polar (azimuth) plot for the Lab 4 patch-antenna radiation pattern.

Uses the measured S21 drop-from-baseline data and mirrors across 0 deg for the
full +/-90 view (problem says "you may assume the radiation pattern is
symmetrical"). Saves to src/photos/azimuth_polar.png.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent / "photos" / "azimuth_polar.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

# Measured data: drop from 0-deg baseline (normalized pattern), in dB.
# Baseline (face-to-face) was -26.8 dB; angle 0 = 0 dB drop.
angles_deg = [0, 15, 30, 45, 60, 75, 90]
drop_dB    = [0.0, -1.0, -2.8, -4.1, -4.8, -7.6, -23.2]

# Build symmetric pattern: mirror onto negative angles.
angles = np.array(angles_deg + [-a for a in angles_deg[1:]])
drops  = np.array(drop_dB  + drop_dB[1:])
order  = np.argsort(angles)
angles = angles[order]
drops  = drops[order]
theta  = np.deg2rad(angles)

fig = plt.figure(figsize=(6.5, 6.5))
ax = fig.add_subplot(111, projection="polar")

# Convention: 0 deg at TOP, increasing clockwise (broadside antenna pattern).
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# Plot the line + filled markers.
ax.plot(theta, drops, "-o", color="#0c447c", linewidth=2.0, markersize=6,
        markerfacecolor="#0c447c", markeredgecolor="white", label="Measured")

# Radial axis: from -25 (outer) to 0 (peak). Use rmin/rmax via set_ylim.
ax.set_rmin(-25)
ax.set_rmax(2)
ax.set_yticks([-3, -10, -20])
ax.set_yticklabels(["$-3$ dB", "$-10$ dB", "$-20$ dB"], fontsize=9)

# Angle ticks every 15 deg
ax.set_xticks(np.deg2rad(np.arange(-90, 91, 15)))
ax.set_thetamin(-90)
ax.set_thetamax(90)

# Mark the -3 dB level with a dashed circle for HPBW reference.
hpbw_angles = np.linspace(-np.pi/2, np.pi/2, 200)
ax.plot(hpbw_angles, [-3]*200, color="#993c1d", linestyle="--", linewidth=1.0, alpha=0.7)
ax.text(np.deg2rad(70), -3, " $-3$ dB", color="#993c1d", fontsize=9, ha="left", va="center")

# Estimate HPBW from data (interpolate where drop crosses -3 dB).
# Going from 30 deg (-2.8) to 45 deg (-4.1):
frac = (-3 - (-2.8)) / ((-4.1) - (-2.8))
hpbw_half = 30 + frac * 15
hpbw_full = 2 * hpbw_half

# Title and HPBW annotation
ax.set_title(f"Patch antenna azimuth pattern (HPBW $\\approx$ {hpbw_full:.1f}$^\\circ$)",
             fontsize=11, pad=18)

# Bottom annotation
fig.text(0.5, 0.04,
         "Measured $S_{21}/S_{12}$ drop from 0-degree (face-to-face) baseline.\n"
         "Baseline $-26.8$ dB; antennas spaced 50 cm at 2.443 GHz. "
         "Pattern assumed symmetric about $0^\\circ$.",
         ha="center", fontsize=9, color="#333")

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(OUT, dpi=200, bbox_inches="tight")
plt.close(fig)

print(f"Saved {OUT}")
print(f"HPBW estimate (interpolated -3 dB crossing): {hpbw_full:.1f} deg")
