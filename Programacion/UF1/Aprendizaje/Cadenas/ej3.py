cadena = input("Cadena: ")
subc = input("Subcadena: ")
total = 0
long = len(subc)
for i in range(len(cadena)):
    if subc == cadena[i:long]:
        total += 1
    long += 1
print(f"La sub cadena {subc}, aparece {total} vezes en la cadena")