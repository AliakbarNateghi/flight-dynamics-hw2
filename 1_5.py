# question 1_5
import numpy as np
import matplotlib.pyplot as plt

# Airfoil coordinates
x_upper = np.array([0, 0.012934, 0.025588, 0.0508, 0.07595, 0.101062, 0.151221, 0.201299, 0.251314, 0.301279,
                    0.401119, 0.500887, 0.600603, 0.700385, 0.800216, 0.900097, 1])
y_upper = np.array([0, 0.033131, 0.044865, 0.061035, 0.072505, 0.081076, 0.093219, 0.099163, 0.100308, 0.097653,
                    0.085445, 0.067738, 0.046032, 0.029425, 0.016517, 0.007409, 0])
x_lower = np.array([0, 0.012274, 0.024717, 0.049677, 0.074602, 0.099569, 0.149516, 0.199489, 0.24948, 0.299472,
                    0.399455, 0.499437, 0.599473, 0.699552, 0.799669, 0.899821, 1])
y_lower = np.array([0, -0.017261, -0.021624, -0.024651, -0.030377, -0.032904, -0.036959, -0.039013, -0.039668, -0.040323,
                    -0.041633, -0.042943, -0.040253, -0.034164, -0.025276, -0.013688, 0])

# Wing geometry
span = 12  # meters
half_span = span / 2
c_r = 3.0  # root chord (m)
c_t = 1.2  # tip chord (m)
sweep_deg = 35
sweep_rad = np.radians(sweep_deg)

# Sweep offset
x_le_tip = half_span * np.tan(sweep_rad)

# Airfoil outlines
x_root = np.concatenate([x_upper, x_lower[::-1]]) * c_r
z_root = np.concatenate([y_upper, y_lower[::-1]]) * c_r
y_root = np.zeros_like(x_root)

x_tip = np.concatenate([x_upper, x_lower[::-1]]) * c_t + x_le_tip
z_tip = np.concatenate([y_upper, y_lower[::-1]]) * c_t
y_tip = np.full_like(x_tip, half_span)

# Mean Geometric Chord (MGC)
mgc = (2 / 3) * (c_r**2 + c_r * c_t + c_t**2) / (c_r + c_t)
y_mgc = (span / 6) * (c_r + 2 * c_t) / (c_r + c_t)

# Leading edge of MGC (swept)
x_mgc_le = y_mgc * np.tan(sweep_rad)

# Trailing edge of MGC
x_mgc_te = x_mgc_le + mgc

# Plotting
plt.figure(figsize=(12, 4))
plt.plot(x_root, y_root, label="Root Airfoil", color='blue')
plt.plot(x_tip, y_tip, label="Tip Airfoil", color='red')
plt.plot([0, x_le_tip], [0, half_span], '--k', label="Leading Edge")
plt.plot([c_r, x_le_tip + c_t], [0, half_span], '--k', label="Trailing Edge")

# MGC line
plt.plot([x_mgc_le, x_mgc_te], [y_mgc, y_mgc], label=f"Mean Geometric Chord = {mgc:.2f} m", color='green', linewidth=2)

# Annotate
plt.scatter([x_mgc_le], [y_mgc], color='green')
plt.text(x_mgc_le + 0.2, y_mgc + 0.2, "MGC", color='green')

plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.title("Wing Planform with Mean Geometric Chord (MGC)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
