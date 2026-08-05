

def facrtorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * facrtorial(n-1)

n = int(input("Enter a number: "))
print(facrtorial(n))