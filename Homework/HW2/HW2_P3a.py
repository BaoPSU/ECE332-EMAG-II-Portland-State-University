import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ax_amp = 3  # V/m
ay_amp = 4  # V/m
delta  = 0  # rad

t  = np.linspace(0, 2*np.pi, 1000)
Ex = ax_amp * np.cos(t)
Ey = ay_amp * np.cos(t + delta)

fig, ax = plt.subplots(figsize=(5, 5))

# locus
ax.plot(Ex, Ey, color='royalblue', linewidth=2.5, label='Locus of E(0,t)')

# arrow showing direction of travel along line
ax.annotate('', xy=(2.5, 10/3), xytext=(1.5, 2),
            arrowprops=dict(arrowstyle='->', color='royalblue', lw=2))

# peak amplitude marker
peak = np.sqrt(ax_amp**2 + ay_amp**2)
ax.plot([0, ax_amp], [0, ay_amp], 'r--', linewidth=1.2, label=f'Peak = {peak} V/m')
ax.plot(ax_amp, ay_amp, 'ro', markersize=7)

# gamma angle arc
theta_arc = np.linspace(0, np.radians(53.13), 100)
r_arc = 1.4
ax.plot(r_arc*np.cos(theta_arc), r_arc*np.sin(theta_arc), 'k-', linewidth=1.2)
ax.text(1.1, 0.45, r'$\gamma = 53.1°$', fontsize=10)

# axes & grid
ax.axhline(0, color='k', linewidth=0.8)
ax.axvline(0, color='k', linewidth=0.8)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.25, linestyle='--')
ax.set_xlabel('$E_x$ (V/m)', fontsize=12)
ax.set_ylabel('$E_y$ (V/m)', fontsize=12)
ax.set_title('Problem 3(a): $a_x=3$, $a_y=4$, $\\delta=0$\nLinear Polarization  |  $\\chi=0°$  |  $\\gamma=53.1°$', fontsize=11)

ax.legend(loc='lower right', fontsize=9)

# labels at tips
ax.text( ax_amp+0.1,  ay_amp+0.1, f'({ax_amp}, {ay_amp})', fontsize=9, color='red')
ax.text(-ax_amp-0.5, -ay_amp-0.4, f'({-ax_amp}, {-ay_amp})', fontsize=9, color='red')

plt.tight_layout()
plt.savefig('/tmp/HW2_P3a.png', dpi=150, bbox_inches='tight')
print("saved")
