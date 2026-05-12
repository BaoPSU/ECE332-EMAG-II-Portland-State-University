"""
Generate the four polarization locus plots for HW2 Problem 3 (a)-(d).

Each case plots E(0, t) = a_x cos(wt) x_hat + a_y cos(wt + delta) y_hat
for one revolution.  Saves HW2_P3a.png ... HW2_P3d.png in the script dir.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent

def plot_case(name, ax_amp, ay_amp, delta, title_extra, fig_title):
    t = np.linspace(0, 2 * np.pi, 1000)
    Ex = ax_amp * np.cos(t)
    Ey = ay_amp * np.cos(t + delta)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(Ex, Ey, color='royalblue', linewidth=2.2,
            label=fr"$a_x={ax_amp}$, $a_y={ay_amp}$, $\delta={title_extra}$")

    # axes through origin
    ax.axhline(0, color='k', linewidth=0.8)
    ax.axvline(0, color='k', linewidth=0.8)

    lim = max(ax_amp, ay_amp) + 1.3
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel(r'$E_x$ (V/m)', fontsize=11)
    ax.set_ylabel(r'$E_y$ (V/m)', fontsize=11)
    ax.set_title(fig_title, fontsize=10)
    ax.legend(loc='lower right', fontsize=8)

    plt.tight_layout()
    out = OUT_DIR / f"HW2_P3{name}.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  wrote {out.name}")

# (a) linear, delta = 0 -> line from (-3,-4) to (3,4), inclination 53.13 deg
plot_case('a', 3, 4, 0.0, "0",
          r"P3(a): Linear  |  $\chi=0$  |  $\gamma=\psi=53.13^\circ$")

# (b) linear, delta = pi -> line from (-3, 4) to (3, -4), inclination -53.13 deg
plot_case('b', 3, 4, np.pi, r"\pi",
          r"P3(b): Linear  |  $\chi=0$  |  $\gamma=\psi=-53.13^\circ$")

# (c) elliptical, ax = ay = 3, delta = pi/4 -> gamma=pi/4, chi=pi/8, RH
plot_case('c', 3, 3, np.pi / 4, r"\pi/4",
          r"P3(c): Elliptical  |  $\gamma=45^\circ$  |  $\chi=22.5^\circ$  (RHEP)")

# (d) elliptical, ax = 3, ay = 4, delta = -3pi/4 -> gamma ~ -21.4 deg, chi ~ -36.9 deg, LH
plot_case('d', 3, 4, -3 * np.pi / 4, r"-3\pi/4",
          r"P3(d): Elliptical  |  $\gamma=-21.4^\circ$  |  $\chi=-36.9^\circ$  (LHEP)")

print("done")
