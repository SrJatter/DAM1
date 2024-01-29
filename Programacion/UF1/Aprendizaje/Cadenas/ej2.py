cadena = input("Cadena: ")
caracter = input("Caracter: ")
while len(caracter) != 1:
    print("Por favor introduce solo un caracter")
    caracter = input("Caracter: ")
total = 0
for l in cadena.lower():
    if caracter.lower() in l:
        total += 1
print(f"El caracter {caracter} aparece {total} veces en la frase introducida")