import numpy as np

# Airfoil data (same as before)
x_upper = np.array([0, 0.012934, 0.025588, 0.0508, 0.07595, 0.101062, 0.151221, 0.201299, 0.251314, 0.301279,
                    0.401119, 0.500887, 0.600603, 0.700385, 0.800216, 0.900097, 1])
y_upper = np.array([0, 0.033131, 0.044865, 0.061035, 0.072505, 0.081076, 0.093219, 0.099163, 0.100308, 0.097653,
                    0.085445, 0.067738, 0.046032, 0.029425, 0.016517, 0.007409, 0])

x_lower = np.array([0, 0.012274, 0.024717, 0.049677, 0.074602, 0.099569, 0.149516, 0.199489, 0.24948, 0.299472,
                    0.399455, 0.499437, 0.599473, 0.699552, 0.799669, 0.899821, 1])
y_lower = np.array([0, -0.017261, -0.021624, -0.024651, -0.030377, -0.032904, -0.036959, -0.039013, -0.039668, -0.040323,
                    -0.041633, -0.042943, -0.040253, -0.034164, -0.025276, -0.013688, 0])

# Interpolate lower Y at upper X points
y_lower_interp = np.interp(x_upper, x_lower, y_lower)

# Compute thickness and camber at each x_upper
thickness = y_upper - y_lower_interp
camber = (y_upper + y_lower_interp) / 2

# Find maximum thickness and maximum camber
max_thickness = np.max(thickness)
x_max_thickness = x_upper[np.argmax(thickness)]

max_camber = np.max(camber)
x_max_camber = x_upper[np.argmax(camber)]

# Chord length (normalized to 1, but shown here for completeness)
chord_length = x_upper[-1] - x_upper[0]
thickness_ratio = max_thickness / chord_length

# Display results
print(f"Maximum Thickness = {max_thickness:.6f} mm at x = {x_max_thickness:.6f} mm")
print(f"Maximum Thickness Ratio = {thickness_ratio * 100:.2f}%")
print(f"Maximum Camber = {max_camber:.6f} mm at x = {x_max_camber:.6f} mm")
