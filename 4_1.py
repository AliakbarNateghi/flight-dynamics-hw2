import numpy as np
import matplotlib.pyplot as plt

# Aerodynamic parameters (assumed from previous discussion)
C_L0 = 0.05
C_L_alpha = 0.07        # per degree
C_L_delta_e = 0.02      # per degree

C_m0 = 0.0
C_m_alpha = -0.0125     # per degree
C_m_delta_e = 0.013     # per degree

alpha_ref = 0.0         # reference angle (degrees)

# Define the range of angle of attack (in degrees)
alpha_deg = np.linspace(-2, 16, 200)

# Elevator deflection values (in degrees)
delta_e_list = np.array([-10, -5, 2])

# Create the plots
plt.figure(figsize=(12, 5))

# Plot Lift Coefficient (C_L) vs. Angle of Attack (alpha)
plt.subplot(1, 2, 1)
for delta_e in delta_e_list:
    # Compute C_L using the linear model
    CL = C_L0 + C_L_alpha*(alpha_deg - alpha_ref) + C_L_delta_e*delta_e
    plt.plot(alpha_deg, CL, label=f'δₑ = {delta_e}°')
plt.xlabel('Angle of Attack, α (deg)')
plt.ylabel('Lift Coefficient, C_L')
plt.title('C_L vs. α for Different Elevator Deflections')
plt.legend()
plt.grid(True)

# Plot Moment Coefficient (C_m) vs. Angle of Attack (alpha)
plt.subplot(1, 2, 2)
for delta_e in delta_e_list:
    # Compute C_m using the linear model
    Cm = C_m0 + C_m_alpha*(alpha_deg - alpha_ref) + C_m_delta_e*delta_e
    plt.plot(alpha_deg, Cm, label=f'δₑ = {delta_e}°')
plt.xlabel('Angle of Attack, α (deg)')
plt.ylabel('Moment Coefficient, C_m')
plt.title('C_m vs. α for Different Elevator Deflections')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('4_1.png')
plt.show()

plt.show()
