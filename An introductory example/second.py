import numpy as np
import matplotlib.pyplot as plt


ts_length = 100
ϵ_values = []   # empty list

for i in range(ts_length):
    rng = np.random.default_rng()
    e = rng.standard_normal()
    ϵ_values.append(e)

plt.plot(ϵ_values)
plt.show()



#just a less efficient way of doing the same thing as in first.py