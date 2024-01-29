casos = int(input("Nr alumnos: "))
alumnos = {}
for c in range(casos):
    alumno = input("Nombre alumno: ")
    notas = []
    nota = int(input("Nota: "))
    while nota >= 0:
        if nota <= 10:
            notas += [nota]
        else:
            print("nota invalida rango(0 - 10)")
        nota = int(input("Nota: "))
    alumnos[alumno] = notas
print("Lista de alumnos + nota media")
for i in alumnos:
    media = 0
    v = 0
    for n in alumnos[i]:
        v += 1
        media += n
    media /= v
    print(f"{i}: {media:.2f}")