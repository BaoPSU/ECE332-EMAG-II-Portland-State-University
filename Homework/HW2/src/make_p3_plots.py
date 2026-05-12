"""
Generate the four polarization locus plots for HW2 Problem 3 (a)-(d).

Plots E(0, t) = a_x cos(wt) x_hat + a_y cos(wt + delta) y_hat for one cycle.

Linear cases (a, b): show the line locus, bounding box at +/- a_x, +/- a_y,
the inclination angle psi (= gamma), and labeled endpoints. No direction
arrows since the field oscillates along the line with no rotation.

Elliptical cases (c, d): annotate like the cheat sheet polarization figure
with the bounding box (+/- a_x, +/- a_y), the auxiliary diagonal showing
psi_0 = arctan(a_y/a_x), the major-axis line at rotation angle gamma, and
labeled angles. Includes direction-of-rotation indicator.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc, Rectangle
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
N = 1000


def draw_bounding_box(ax, ax_amp, ay_amp):
    rect = Rectangle((-ax_amp, -ay_amp), 2 * ax_amp, 2 * ay_amp,
                     fill=False, edgecolor='gray', linewidth=1.0,
                     linestyle='--', alpha=0.8)
    ax.add_patch(rect)
    ax.text(ax_amp + 0.15, 0.1, fr"$a_x={ax_amp}$",
            fontsize=8, color='gray')
    ax.text(0.1, ay_amp + 0.2, fr"$a_y={ay_amp}$",
            fontsize=8, color='gray')


def draw_angle_arc(ax, theta_deg, radius, label, color='darkgreen', ang_offset=0):
    arc = Arc((0, 0), 2 * radius, 2 * radius, angle=0,
              theta1=min(0, theta_deg), theta2=max(0, theta_deg),
              color=color, linewidth=1.4)
    ax.add_patch(arc)
    label_theta = np.radians(theta_deg / 2 + ang_offset)
    ax.text((radius + 0.25) * np.cos(label_theta),
            (radius + 0.25) * np.sin(label_theta),
            label, fontsize=9, color=color, ha='center', va='center')


def plot_linear(name, ax_amp, ay_amp, delta, delta_str, title):
    """Linear polarization: line locus, bounding box, psi inclination angle."""
    t = np.linspace(0, 2 * np.pi, N)
    Ex = ax_amp * np.cos(t)
    Ey = ay_amp * np.cos(t + delta)

    fig, ax = plt.subplots(figsize=(5.4, 5.4))

    # Locus (line)
    ax.plot(Ex, Ey, color='royalblue', linewidth=2.2,
            label=fr"$\delta={delta_str}$")

    # Bounding box
    draw_bounding_box(ax, ax_amp, ay_amp)

    # Endpoints of oscillation
    p1 = (ax_amp, ay_amp * np.cos(delta))
    p2 = (-ax_amp, -ay_amp * np.cos(delta))
    ax.plot(*p1, 'ro', markersize=7)
    ax.plot(*p2, 'ro', markersize=7)
    ax.text(p1[0] + 0.2, p1[1] + 0.2, f"({p1[0]:g}, {p1[1]:g})",
            fontsize=9, color='darkred')
    ax.text(p2[0] - 1.4, p2[1] - 0.4, f"({p2[0]:g}, {p2[1]:g})",
            fontsize=9, color='darkred')

    # Inclination angle psi (= gamma for linear). Arc from +x axis to the line.
    psi_deg = np.degrees(np.arctan2(p1[1], p1[0]))
    draw_angle_arc(ax, psi_deg, 1.2, fr"$\psi=\gamma={psi_deg:.2f}^\circ$")

    # Axes
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


def plot_ellipse(name, ax_amp, ay_amp, delta, delta_str, title,
                  gamma_deg, chi_deg, handedness):
    """Elliptical polarization with cheat-sheet-style annotations."""
    t = np.linspace(0, 2 * np.pi, N)
    Ex = ax_amp * np.cos(t)
    Ey = ay_amp * np.cos(t + delta)

    fig, ax = plt.subplots(figsize=(5.8, 5.8))

    # Bounding box
    draw_bounding_box(ax, ax_amp, ay_amp)

    # Locus
    ax.plot(Ex, Ey, color='royalblue', linewidth=2.2,
            label=fr"$\delta={delta_str}$")

    # Auxiliary diagonal showing psi_0 = arctan(a_y/a_x): from origin to (a_x, a_y).
    ax.plot([0, ax_amp], [0, ay_amp], color='purple', linestyle=':', linewidth=1.4)
    ax.plot(ax_amp, ay_amp, 'o', color='purple', markersize=6)
    psi0_deg = np.degrees(np.arctan2(ay_amp, ax_amp))
    draw_angle_arc(ax, psi0_deg, 0.8,
                   fr"$\psi_0={psi0_deg:.1f}^\circ$",
                   color='purple')

    # Major axis line at angle gamma. Length = R (axial ratio).
    if abs(chi_deg) > 1e-3:
        R = 1.0 / abs(np.tan(np.radians(chi_deg)))
    else:
        R = float('inf')
    # Use a fixed length proportional to the bounding box for drawing.
    L = max(ax_amp, ay_amp) * 1.2
    gx = L * np.cos(np.radians(gamma_deg))
    gy = L * np.sin(np.radians(gamma_deg))
    ax.plot([-gx, gx], [-gy, gy], color='darkgreen',
            linestyle='--', linewidth=1.5, alpha=0.8,
            label=fr"major axis $\gamma$")

    # Gamma arc from +x to major axis.
    draw_angle_arc(ax, gamma_deg, 1.6,
                   fr"$\gamma={gamma_deg:.1f}^\circ$",
                   color='darkgreen')

    # Annotation block top-right.
    info_lines = [
        fr"$\chi = {chi_deg:.1f}^\circ$",
        fr"$R = 1/|\tan\chi| = {R:.2f}$" if R != float('inf') else r"$R=\infty$",
        f"Handedness: {handedness}",
    ]
    info_text = "\n".join(info_lines)
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
            fontsize=9, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.4',
                      facecolor='white', edgecolor='gray', alpha=0.9))

    # Direction-of-rotation tick: place 3 small arrowheads along the curve.
    for frac in (0.07, 0.32, 0.57, 0.82):
        i = int(frac * N)
        ax.annotate('', xy=(Ex[i + 6], Ey[i + 6]),
                    xytext=(Ex[i], Ey[i]),
                    arrowprops=dict(arrowstyle='-|>', color='darkred',
                                    lw=1.6, mutation_scale=15))
    sense = 'CW' if (Ex[5] - Ex[0]) * Ey[0] - (Ey[5] - Ey[0]) * Ex[0] < 0 else 'CCW'
    ax.text(0.98, 0.02, f"rotation in plot: {sense}",
            transform=ax.transAxes, fontsize=9, ha='right', va='bottom',
            color='darkred')

    # Axes
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


# Cases (a) and (b): linear
plot_linear('a', 3, 4, 0.0, "0",
            r"P3(a): Linear  |  $\chi=0$  |  $\gamma=\psi=53.13^\circ$")
plot_linear('b', 3, 4, np.pi, r"\pi",
            r"P3(b): Linear  |  $\chi=0$  |  $\gamma=\psi=-53.13^\circ$")

# Cases (c) and (d): elliptical with cheat-sheet-style annotations
plot_ellipse('c', 3, 3, np.pi / 4, r"\pi/4",
             r"P3(c): Elliptical  |  RHEP",
             gamma_deg=45.0, chi_deg=22.5, handedness="RH (CCW)")
plot_ellipse('d', 3, 4, -3 * np.pi / 4, r"-3\pi/4",
             r"P3(d): Elliptical  |  LHEP",
             gamma_deg=-21.4, chi_deg=-36.9, handedness="LH (CW)")

print("done")
