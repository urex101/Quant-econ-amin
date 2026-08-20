

def f(seq_a, seq_b):
    x = 0
    for i in seq_a:
        if i not in seq_b:
            return False
    return True

print(f("ab", "cadb"))
print(f("ab", "cjdb"))
print(f([1, 2], [1, 2, 3]))
print(f([1, 2, 3], [1, 2]))