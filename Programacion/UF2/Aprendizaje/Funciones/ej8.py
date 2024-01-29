def esPrimer(num):
    if num == 1 or num <= 0:
        return "No es primo"
    for i in range(2, num):
        if num % i == 0:
            return "No es primo"
    return "Es primo"
num = int(input("Introduce un numero: "))
print(esPrimer(num))