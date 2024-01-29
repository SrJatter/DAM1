def CalcularFactorial(num):
    if num < 0:
        return 0
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
    
def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(CalcularFactorial(5))
print(factorial(5))