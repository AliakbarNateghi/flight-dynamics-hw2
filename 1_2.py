import matplotlib.pyplot as plt
import numpy as np

# Upper surface coordinates
x_upper = np.array([0, 0.012934, 0.025588, 0.0508, 0.07595, 0.101062, 0.151221, 0.201299, 0.251314, 0.301279,
                    0.401119, 0.500887, 0.600603, 0.700385, 0.800216, 0.900097, 1])
y_upper = np.array([0, 0.033131, 0.044865, 0.061035, 0.072505, 0.081076, 0.093219, 0.099163, 0.100308, 0.097653,
                    0.085445, 0.067738, 0.046032, 0.029425, 0.016517, 0.007409, 0])

# Lower surface coordinates
x_lower = np.array([0, 0.012274, 0.024717, 0.049677, 0.074602, 0.099569, 0.149516, 0.199489, 0.24948, 0.299472,
                    0.399455, 0.499437, 0.599473, 0.699552, 0.799669, 0.899821, 1])
y_lower = np.array([0, -0.017261, -0.021624, -0.024651, -0.030377, -0.032904, -0.036959, -0.039013, -0.039668, -0.040323,
                    -0.041633, -0.042943, -0.040253, -0.034164, -0.025276, -0.013688, 0])

# Interpolating lower surface Y-values at upper surface X-positions
y_lower_interp = np.interp(x_upper, x_lower, y_lower)

# Camber line: mean of upper and interpolated lower surface
y_camber = (y_upper + y_lower_interp) / 2

# Chord line: straight from (0,0) to (1,0)
x_chord = [0, 1]
y_chord = [0, 0]

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(x_upper, y_upper, label='Upper Surface', marker='o')
plt.plot(x_lower, y_lower, label='Lower Surface', marker='o')
plt.plot(x_upper, y_camber, label='Camber Line', linestyle='--', color='green')
plt.plot(x_chord, y_chord, label='Chord Line', linestyle='-.', color='black')
plt.title('Airfoil with Chord and Camber Lines')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
