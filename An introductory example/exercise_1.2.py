import numpy as np
import matplotlib.pyplot as plt
#simulate and plot the correlated time series

T = 200 
a = [0,0.8,0.98]
x = np.empty(T)

for a_i in a:
    x[0] = 0
    for t in range(T - 1):
            x[t + 1] = a_i * x[t] + np.random.standard_normal()
            plt.plot(x, label=f'a = {a_i}')

plt.legend()
plt.show()