import numpy as np

rng = np.random.default_rng()

def binomial_rv(n,p):
        w = int(0)
        for i in range(n):
            land = rng.uniform(0,1)
            if float(land) < float(p):
                w += 1
            else:
                pass
        return w

print (binomial_rv(10,0.5))