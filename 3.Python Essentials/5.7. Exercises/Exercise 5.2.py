def polyq(x, coeff):
    return sum(a * x**i for i, a in enumerate(coeff))

print(polyq(1, (2, 4)))