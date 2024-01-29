cadena = input("Introduce una frase: ")
sinvocales = ""
for i in cadena:
    if i.lower() not in "aeiou":
        sinvocales += i
print(sinvocales)