


def linapprox(f, a, b, n, x):
    length_interval = (b - a)
    number_of_subintervals = n - 1
    step = length_interval / number_of_subintervals
    poi = a
    while poi <= x:
        poi += step
    u , v = poi - step, poi
    return f(u) + (x - u) * (f(v) - f(u)) / (v - u) 