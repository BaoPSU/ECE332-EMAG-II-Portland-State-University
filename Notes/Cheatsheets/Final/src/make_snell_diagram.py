"""
Generate the small Snell's law inline diagram for the cheat sheet.
Single boundary, incident ray bending into denser medium.
Output: ../img/snell_diagram.png
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "img" / "snell_diagram.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

theta_i_deg = 35.0
theta_t_deg = 18.0
theta_i = np.deg2rad(theta_i_deg)
theta_t = np.deg2rad(theta_t_deg)

# Geometry: boundary at y=0 (horizontal); medium 1 above (y>0), medium 2 below (y<0).
# Rays meet at origin.

fig, ax = plt.subplots(figsize=(2.0, 1.7), dpi=300)

# Background fills for the two media
ax.axhspan(0, 1.2, facecolor="#e6f1fb", zorder=0)   # light blue - Med 1
ax.axhspan(-1.2, 0, facecolor="#faece7", zorder=0)  # light coral - Med 2

# Boundary
ax.axhline(0, color="black", linewidth=1.0, zorder=2)

# Normal (dashed vertical)
ax.plot([0, 0], [-1.1, 1.1], color="black", linestyle=(0, (3, 2)), linewidth=0.7, zorder=2)

# Incident ray (top-left to origin)
L = 1.0
x_i, y_i = -L*np.sin(theta_i), L*np.cos(theta_i)
ax.annotate("", xy=(0, 0), xytext=(x_i, y_i),
            arrowprops=dict(arrowstyle="->", color="#0c447c", lw=1.4), zorder=3)

# Refracted ray (origin to bottom-right, smaller angle)
x_t, y_t = L*np.sin(theta_t), -L*np.cos(theta_t)
ax.annotate("", xy=(x_t, y_t), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="#0c447c", lw=1.4), zorder=3)

# Arc for theta_i (between normal and incident ray, in medium 1)
arc_r = 0.32
ax.add_patch(Arc((0, 0), 2*arc_r, 2*arc_r, angle=0,
                 theta1=90, theta2=90+theta_i_deg, color="#993c1d", linewidth=0.9, zorder=3))

# Arc for theta_t (between normal and refracted ray, in medium 2)
ax.add_patch(Arc((0, 0), 2*arc_r, 2*arc_r, angle=0,
                 theta1=270-theta_t_deg, theta2=270, color="#993c1d", linewidth=0.9, zorder=3))

# Angle labels
ax.text(-0.18, 0.42, r"$\theta_i$", fontsize=9, color="#993c1d", ha="center", va="center")
ax.text(0.13, -0.38, r"$\theta_t$", fontsize=9, color="#993c1d", ha="center", va="center")

# Medium labels
ax.text(0.95, 0.85, r"Med 1", fontsize=7, ha="right", va="center", color="#0c447c")
ax.text(0.95, 0.70, r"$\varepsilon_{r1}$", fontsize=7.5, ha="right", va="center", color="#0c447c")
ax.text(0.95, -0.78, r"Med 2", fontsize=7, ha="right", va="center", color="#993c1d")
ax.text(0.95, -0.93, r"$\varepsilon_{r2}>\varepsilon_{r1}$", fontsize=7, ha="right", va="center", color="#993c1d")

# Normal label
ax.text(0.06, 1.04, "normal", fontsize=6, color="gray", ha="left", va="top", style="italic")

ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.15, 1.15)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout(pad=0.05)
plt.savefig(OUT, bbox_inches="tight", pad_inches=0.02, dpi=300)
print(f"saved {OUT}, {OUT.stat().st_size//1024} KB")
