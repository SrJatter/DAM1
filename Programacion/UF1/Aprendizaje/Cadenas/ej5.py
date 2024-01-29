frase = input("Introduce una frase: ")
m = 0
cadena = ""
for i in frase:
    if m == 0:
        cadena += i
        m = 1
    else:
        m = 0
print(cadena)