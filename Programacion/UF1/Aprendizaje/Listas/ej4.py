n = []
print("Introduce 5 notas entre el 0 y el 10")
for i in range(1,6):
    nota = int(input(f"Nota {i}: "))
    while 0 > nota or nota > 10:
        print("Nota fuera de rango, repite por favor")
        nota = int(input(f"Nota {i}: "))
    n.append(nota)
suma = 0
print("Tus notas son:")
for i in n:
    suma += i
    if i == n[-1]:
        print(i, end="\n")
    else:
        print(i, end = ", ")
mediana = suma/5
for i in range(len(n)):
    if i == 0:
        minimo = n[i]
        maximo = n[i]
    if minimo > n[i]:
        minimo = n[i]
    if maximo < n[i]:
        maximo = n[i]
print(f"La mediana de las notas es: {mediana}\nLa nota mas alta es: {maximo}\nLa nota mas baja es: {minimo}")