

def factorial(n):
    mult = n
    while n >1:

        mult *= (n-1)

        n = n-1
    return mult

print(factorial(5))