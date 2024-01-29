print("parte 1")
def error_control(w):
    err = 1
    while err == 1:
        try:
            v = float(input(w))
            err = 0
            if v == int(v):
                v = int(v)
        except ValueError:
            print("¡Por favor, no introduzcas otros caracteres no númericos!")
    return v
a = error_control("Introduce un número: ")
b = error_control("Introduce otro número: ")
sum = a + b
res = a - b
mul = a * b
if b == 0:
    div = f"{a} no se puede dividir por 0"
else:
    div=a/b
print("El número guardado en la variable a es:", a)
print("El número guardado en la variable b es:", b)
print("El resultado de la suma:", sum)
print("El resultado de la resta:", res)
print("El resultado de la multiplicación:", mul)
print("El resultado de la división:", div)

print("\nparte 2")
print("Valor de a:", a)
print("Valor de b:", b)
c = a
a = b
b = c
print("¡Intercambo hecho!")
print("Valor de a:", a)
print("Valor de b", b)

print("\nparte 3")
result = a + b / 2 * (a + b)
print("a + b / 2 * ( a + b )",)
print(a, "+", b, "/ 2 * (", a,"+", b,")")
print(a, "+", b / 2, "*", (a + b))
print(a, "+", b / 2*(a + b))
print(result)
print("a + b / 2 * (a + b) =", result)