import numpy as np


#Here’s a harder exercise, that takes some thought and planning.

# The task is to compute an approximation to pie using Monte Carlo.

n = 1000000
inside = 0
for _ in range(n):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside += 1

pie_approximation = 4 * inside / n

print(f"Approximation to pie: {pie_approximation}")