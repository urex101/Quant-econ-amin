

def factorial(n):
    k = 1
    for i in range(int(n)):
        k = k * i+1
    return k

print (factorial(0))