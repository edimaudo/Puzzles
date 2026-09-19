"""
Ponder this May 1998
If a belt were placed around the Earth's equator, and then had six meters of length added to it, and you grabbed it at a point and lifted it until all the slack was gone, how high above Earth's surface would you be?
"""
import math

# Inputs
R = 6_371_000  # Radius of the Earth in meters
slack = 6      # Extra length in meters

# Target value: delta_s / (2 * R)
target = slack / (2 * R)

# Objective function: f(theta) = tan(theta) - theta - target
# Derivative: f'(theta) = sec^2(theta) - 1 = tan^2(theta)

# Newton's Method solver
theta = 0.01  # Initial guess in radians
for _ in range(20):
    f = math.tan(theta) - theta - target
    f_prime = (math.tan(theta)) ** 2
    theta = theta - f / f_prime

# Calculate height h
h = R * ((1 / math.cos(theta)) - 1)

# Results
print(f"Angle theta : {theta:.6f} radians ({math.degrees(theta):.4f}°)")
print(f"Height (h)  : {h:.2f} meters")