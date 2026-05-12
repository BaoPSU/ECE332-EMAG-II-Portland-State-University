"""
Generate the four polarization locus plots for HW2 Problem 3 (a)-(d).

Plots E(0, t) = a_x cos(wt) x_hat + a_y cos(wt + delta) y_hat for one cycle.
Adds direction-of-motion arrows (small triangles along the curve) so the
sense of rotation is visible. Linear cases show double-headed oscillation
arrows along the line. Saves HW2_P3a.png ... HW2_P3d.png in the script dir.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
N = 1000


def plot_case(name, ax_amp, ay_amp, delta, delta_str, title, kind):
    t = np.linspace(0, 2 * np.pi, N)
    Ex = ax_amp * np.cos(t)
    Ey = ay_amp * np.cos(t + delta)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(Ex, Ey, color='royalblue', linewidth=2.2,
            label=fr"$a_x={ax_amp}$, $a_y={ay_amp}$, $\delta={delta_str}$")

    if kind == 'linear':
        # Mark the two endpoints of the oscillation and a double-headed arrow.
        p1 = (ax_amp, ay_amp * np.cos(delta))
        p2 = (-ax_amp, -ay_amp * np.cos(delta))
        ax.plot(*p1, 'ro', markersize=7)
        ax.plot(*p2, 'ro', markersize=7)
        arrow = FancyArrowPatch(p2, p1,
                                arrowstyle='<->', mutation_scale=20,
                                color='darkred', linewidth=1.6)
        ax.add_patch(arrow)
        ax.text(p1[0] + 0.2, p1[1] + 0.2, f"({p1[0]:g}, {p1[1]:g})",
                fontsize=8, color='darkred')
        ax.text(p2[0] - 1.0, p2[1] - 0.4, f"({p2[0]:g}, {p2[1]:g})",
                fontsize=8, color='darkred')
        ax.text(0.0, max(ax_amp, ay_amp) + 0.6,
                "oscillates along line (no rotation)",
                fontsize=8, color='darkred', ha='center')

    elif kind == 'rotating':
        # Place 3 arrow heads along the curve to show direction of motion.
        for frac in (0.05, 0.30, 0.55, 0.80):
            i = int(frac * N)
            dx = Ex[i + 5] - Ex[i]
            dy = Ey[i + 5] - Ey[i]
            ax.annotate('', xy=(Ex[i + 5], Ey[i + 5]),
                        xytext=(Ex[i], Ey[i]),
                        arrowprops=dict(arrowstyle='-|>', color='darkred',
                                        lw=1.8, mutation_scale=18))
        # Determine sense by checking first crossover.
        # Going from t=0 to small t>0: dE/dt direction tells the sense.
        sense = 'CW' if (Ex[5] - Ex[0]) * Ey[0] - (Ey[5] - Ey[0]) * Ex[0] < 0 else 'CCW'
        ax.text(0.0, max(ax_amp, ay_amp) + 0.6,
                f"rotation in plot: {sense}",
                fontsize=8, color='darkred', ha='center')

    # axes
    ax.axhline(0, color='k', linewidth=0.8)
    ax.axvline(0, color='k', linewidth=0.8)
    lim = max(ax_amp, ay_amp) + 1.5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel(r'$E_x$ (V/m)', fontsize=11)
    ax.set_ylabel(r'$E_y$ (V/m)', fontsize=11)
    ax.set_title(title, fontsize=10)
    ax.legend(loc='lower right', fontsize=8)

    plt.tight_layout()
    out = OUT_DIR / f"HW2_P3{name}.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  wrote {out.name}")


# (a) linear, delta = 0
plot_case('a', 3, 4, 0.0, "0",
          r"P3(a): Linear  |  $\chi=0$  |  $\gamma=\psi=53.13^\circ$",
          kind='linear')

# (b) linear, delta = pi
plot_case('b', 3, 4, np.pi, r"\pi",
          r"P3(b): Linear  |  $\chi=0$  |  $\gamma=\psi=-53.13^\circ$",
          kind='linear')

# (c) elliptical, ax = ay = 3, delta = pi/4
plot_case('c', 3, 3, np.pi / 4, r"\pi/4",
          r"P3(c): Elliptical  |  $\gamma=45^\circ$  |  $\chi=22.5^\circ$  (RHEP)",
          kind='rotating')

# (d) elliptical, ax = 3, ay = 4, delta = -3pi/4
plot_case('d', 3, 4, -3 * np.pi / 4, r"-3\pi/4",
          r"P3(d): Elliptical  |  $\gamma=-21.4^\circ$  |  $\chi=-36.9^\circ$  (LHEP)",
          kind='rotating')

print("done")
