nombrec = input("Tu nombre completo: ")
print(nombrec.lower())
print(nombrec.upper())
capital=""
nombre=""
for i in nombrec:
    if i != " ":
        capital+=i
    else:
        nombre=capital
        capital=""
        print(nombre.capitalize(), end = " ")
nombre=capital
print(nombre.capitalize())