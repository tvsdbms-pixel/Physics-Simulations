import numpy as np
import matplotlib.pyplot as plt

# 1. Constants
mass = 50 

# 2. Create a RANGE of velocities (from 0 to 100 m/s)
v_range = np.linspace(0, 100, 100) 

# 3. Calculate KE for EVERY velocity in that range
KE_range = 0.5 * mass * v_range**2

# 4. Plotting
plt.figure(figsize=(10, 5))
plt.plot(v_range, KE_range, color='red', label='Kinetic Energy')

# 5. Correct Labels
plt.title("Kinetic Energy vs Velocity (Mass = 50kg)")
plt.xlabel("Velocity (v) in m/s")
plt.ylabel("Kinetic Energy (KE) in Joules")
plt.grid(True)
plt.legend()
plt.show()
