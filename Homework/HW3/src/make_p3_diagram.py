"""
Generate the 3-layer dielectric diagram for HW3 Problem 3.

Shows a parallel-polarized plane wave at theta_i = 30 deg entering a
stack of two dielectric slabs (eps_r = 6.25 then eps_r = 2.25) and
exiting back into air, with the lateral displacement d marked.

Layer thicknesses: 5 cm each. Computed angles:
  theta_2 = sin^-1(0.2)    = 11.54 deg  (in eps_r = 6.25)
  theta_3 = sin^-1(1/3)    = 19.47 deg  (in eps_r = 2.25)
  theta_4 = 30 deg                       (back in air)
Lateral displacement d = 5 cm tan(theta_2) + 5 cm tan(theta_3) = 2.79 cm.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent

# Angles (degrees) computed from Snell's law.
theta_i = 30.0
theta_2 = np.degrees(np.arcsin(0.2))      # 11.54
theta_3 = np.degrees(np.arcsin(1/3))      # 19.47
theta_4 = 30.0                            # back to air

# Layer thicknesses (cm).
t_slab1 = 5.0
t_slab2 = 5.0

fig, ax = plt.subplots(figsize=(7, 7))

# Vertical positions (top to bottom): air, slab1 (eps=6.25), slab2 (eps=2.25), air
y_top_air     = 12.0
y_top_slab1   = 8.0   # interface 1
y_top_slab2   = y_top_slab1 - t_slab1
y_bottom_air  = y_top_slab2 - t_slab2

# Layer regions (full width)
WIDTH = 12.0
ax.add_patch(Rectangle((-WIDTH/2, y_top_slab1), WIDTH, y_top_air - y_top_slab1,
                       facecolor='#E6F1FB', edgecolor='black', linewidth=0.8))
ax.add_patch(Rectangle((-WIDTH/2, y_top_slab2), WIDTH, t_slab1,
                       facecolor='#EAF3DE', edgecolor='black', linewidth=0.8))
ax.add_patch(Rectangle((-WIDTH/2, y_bottom_air), WIDTH, t_slab2,
                       facecolor='#FAEEDA', edgecolor='black', linewidth=0.8))
ax.add_patch(Rectangle((-WIDTH/2, y_bottom_air - 4), WIDTH, 4,
                       facecolor='#E6F1FB', edgecolor='black', linewidth=0.8))

# Layer labels
ax.text(WIDTH/2 - 0.4, y_top_air - 1.0, "Air\n$\\mu_r=1,\\ \\varepsilon_r=1$",
        ha='right', va='center', fontsize=11)
ax.text(WIDTH/2 - 0.4, y_top_slab1 - t_slab1/2,
        "$\\mu_r=1,\\ \\varepsilon_r=6.25$",
        ha='right', va='center', fontsize=11)
ax.text(WIDTH/2 - 0.4, y_top_slab2 - t_slab2/2,
        "$\\mu_r=1,\\ \\varepsilon_r=2.25$",
        ha='right', va='center', fontsize=11)
ax.text(WIDTH/2 - 0.4, y_bottom_air - 2,
        "Air", ha='right', va='center', fontsize=11)

# Thickness arrows
def thickness_arrow(x, y0, y1, label):
    ax.annotate('', xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(x - 0.5, (y0 + y1)/2, label, fontsize=10, ha='right')

thickness_arrow(-WIDTH/2 + 0.6, y_top_slab1, y_top_slab2, '5 cm')
thickness_arrow(-WIDTH/2 + 0.6, y_top_slab2, y_bottom_air, '5 cm')

# Beam path. Start at top entering at theta_i. Beam strikes first interface at x = 0.
# Walk back up at theta_i to find the start point above the air layer.
seg_len_air_top = (y_top_air - y_top_slab1) / np.cos(np.radians(theta_i))
x_start = -seg_len_air_top * np.sin(np.radians(theta_i))

# At interface 1 (y = y_top_slab1), beam refracts to theta_2 going down.
dx_slab1 = t_slab1 * np.tan(np.radians(theta_2))
x_at_iface2 = 0 + dx_slab1   # x at top of slab 2

# At interface 2 (y = y_top_slab2), beam refracts to theta_3 going down.
dx_slab2 = t_slab2 * np.tan(np.radians(theta_3))
x_at_iface3 = x_at_iface2 + dx_slab2  # x at bottom of slab 2 = top of air below

# At interface 3 (y = y_bottom_air), beam refracts back to theta_4 = theta_i = 30 deg.
seg_len_air_bot = 4.0 / np.cos(np.radians(theta_4))
x_end = x_at_iface3 + seg_len_air_bot * np.sin(np.radians(theta_4))

beam_x = [x_start, 0, x_at_iface2, x_at_iface3, x_end]
beam_y = [y_top_air, y_top_slab1, y_top_slab2, y_bottom_air, y_bottom_air - 4]

ax.plot(beam_x, beam_y, color='royalblue', linewidth=2.5)
# Arrow on the final segment
ax.annotate('', xy=(x_end, y_bottom_air - 4),
            xytext=(x_at_iface3 + 0.5 * (x_end - x_at_iface3),
                    y_bottom_air - 2),
            arrowprops=dict(arrowstyle='-|>', color='royalblue',
                            lw=2, mutation_scale=18))

# Normal lines (dashed verticals) at each interface entry
def normal_line(x, y0, length=2.0):
    ax.plot([x, x], [y0 - length/2, y0 + length/2], 'k--', linewidth=0.8)

normal_line(0, y_top_slab1, 2.2)
normal_line(x_at_iface2, y_top_slab2, 2.2)
normal_line(x_at_iface3, y_bottom_air, 2.2)

# Angle labels at each interface
def angle_label(x, y, angle_deg, name, offset_angle, color='darkred'):
    ax.text(x + 0.35 * np.cos(np.radians(offset_angle)),
            y + 0.35 * np.sin(np.radians(offset_angle)),
            fr"$\theta_{{{name}}}={angle_deg:.2f}^\circ$",
            fontsize=10, color=color, ha='left', va='center')

angle_label(0, y_top_slab1, theta_i, 'i', 45)
angle_label(x_at_iface2, y_top_slab2, theta_2, '2', 45)
angle_label(x_at_iface3, y_bottom_air, theta_3, '3', 45)
ax.text(x_end + 0.3, y_bottom_air - 3.6,
        fr"$\theta_4 = {theta_4:.0f}^\circ$",
        fontsize=10, color='darkred')

# Lateral displacement d (between the no-refraction continuation of incident
# ray at the lower air layer, and the actual exit point on the bottom interface)
no_refract_x = 0 + (y_top_slab1 - y_bottom_air) * np.tan(np.radians(theta_i))
ax.annotate('', xy=(x_at_iface3, y_bottom_air - 0.5),
            xytext=(no_refract_x, y_bottom_air - 0.5),
            arrowprops=dict(arrowstyle='<->', color='darkgreen', lw=1.6))
ax.plot([no_refract_x, no_refract_x], [y_top_slab1, y_bottom_air - 0.7],
        color='darkgreen', linestyle=':', linewidth=1.0)
ax.text((no_refract_x + x_at_iface3)/2, y_bottom_air - 1.0,
        fr"$d = 2.79$ cm", fontsize=11, color='darkgreen',
        ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                  edgecolor='darkgreen'))

# Cosmetic
ax.set_xlim(-WIDTH/2, WIDTH/2)
ax.set_ylim(y_bottom_air - 4.5, y_top_air + 0.5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("HW3 P3: parallel-polarized wave through dielectric layers",
             fontsize=11)

plt.tight_layout()
out = OUT_DIR / "HW3_P3_layers.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"wrote {out.name}")
