cadena = input("Introduce una frase: ")
vocales = 0
for i in cadena:
    if i in "aeiou":
        vocales += 1
print(f"Hay {vocales} vocales")