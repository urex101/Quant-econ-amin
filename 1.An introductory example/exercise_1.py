import numpy as np
import matplotlib.pyplot as plt
#simulate and plot the correlated time series

T = 200 
a = 0.9
x = np.empty(T)
x[0] = 0
for t in range(T - 1):
    x[t + 1] = a * x[t] + np.random.standard_normal()


plt.plot(x)
plt.show()