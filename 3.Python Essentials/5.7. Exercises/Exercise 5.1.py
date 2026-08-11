"""
Part 1: Given two numeric lists or tuples x_vals and y_vals of equal length, compute their inner product using zip().

Part 2: In one line, count the number of even numbers in 0,…,99.

Part 3: Given pairs = ((2, 5), (4, 2), (9, 8), (12, 10)), count the number of pairs (a, b) such that both a and b are even.
"""

x_vals = [1, 2, 3]
y_vals = [4, 5, 6]
sum_product = sum(x * y for x, y in zip(x_vals, y_vals))
print(sum_product)



sum_even = sum(1 for x in range(100) if x % 2 == 0)
print(sum_even)

pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
even_pairs_count = sum(1 for a, b in pairs if a % 2 == 0 and b % 2 == 0)
print(even_pairs_count)