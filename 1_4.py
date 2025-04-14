# question 1_4
import numpy as np
import matplotlib.pyplot as plt

# Airfoil shape (normalized to chord length = 1)
x_upper = np.array([0, 0.012934, 0.025588, 0.0508, 0.07595, 0.101062, 0.151221, 0.201299, 0.251314, 0.301279,
                    0.401119, 0.500887, 0.600603, 0.700385, 0.800216, 0.900097, 1])
y_upper = np.array([0, 0.033131, 0.044865, 0.061035, 0.072505, 0.081076, 0.093219, 0.099163, 0.100308, 0.097653,
                    0.085445, 0.067738, 0.046032, 0.029425, 0.016517, 0.007409, 0])

x_lower = np.array([0, 0.012274, 0.024717, 0.049677, 0.074602, 0.099569, 0.149516, 0.199489, 0.24948, 0.299472,
                    0.399455, 0.499437, 0.599473, 0.699552, 0.799669, 0.899821, 1])
y_lower = np.array([0, -0.017261, -0.021624, -0.024651, -0.030377, -0.032904, -0.036959, -0.039013, -0.039668, -0.040323,
                    -0.041633, -0.042943, -0.040253, -0.034164, -0.025276, -0.013688, 0])

# Geometry inputs
span = 12  # meters
half_span = span / 2
root_chord = 3.0  # meters
tip_chord = 1.2  # meters
sweep_deg = 35
sweep_rad = np.radians(sweep_deg)

# Tip leading edge X offset due to sweep
x_le_tip = half_span * np.tan(sweep_rad)

# Root airfoil coordinates (scaled)
x_root = np.concatenate([x_upper, x_lower[::-1]]) * root_chord
z_root = np.concatenate([y_upper, y_lower[::-1]]) * root_chord
y_root = np.zeros_like(x_root)

# Tip airfoil coordinates (scaled and swept)
x_tip = np.concatenate([x_upper, x_lower[::-1]]) * tip_chord + x_le_tip
z_tip = np.concatenate([y_upper, y_lower[::-1]]) * tip_chord
y_tip = np.full_like(x_tip, half_span)

# Plotting the planform view
plt.figure(figsize=(12, 4))
# Plot root and tip airfoil outlines
plt.plot(x_root, y_root, label="Root Airfoil", color='blue')
plt.plot(x_tip, y_tip, label="Tip Airfoil", color='red')

# Plot leading and trailing edges
plt.plot([0, x_le_tip], [0, half_span], '--k', label="Leading Edge")
plt.plot([root_chord, x_le_tip + tip_chord], [0, half_span], '--k', label="Trailing Edge")

plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.title("Wing Planform with Airfoil Shape (Top View)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
