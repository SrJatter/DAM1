numeros = [6, 1, 2, 3, 8, 1, 0, 3, 0, 0, 4, 5, 7]
#a
print("La lista numeros", numeros)
#b
print("La lista tiene", len(numeros), "elementos")
#c
print(f"En la posicion 4 esta el: {numeros[4]}")
#d
numeros.append(9)
#e
numeros.insert(1, 4)
#f
print("La lista numeros", numeros)
#g
numeros.remove(6)
#h
print("La lista numeros", numeros)
#i
print(f"El ultimo numero de la lista es {numeros[-1]}")
#j
suma = 0
for i in numeros:
    suma +=i
print(f"La suma de todos los numeros de la lista es {suma}")
#k
num1 = int(input("Introduce un numero: "))
if num1 in numeros:
    print("El numero esta en la lista")
else:
    print("El numero no esta en la lista")
#l
numeros.append(6)
#m
print(numeros)
#n
num2 = int(input("Introduce un numero: "))
t = 0
for i in numeros:
    if num2 == i:
        t += 1
print(f"El numero {num2} aparece {t} veces")
#o
num3 = int(input("Introduce un numero: "))
f=0
if num3 in numeros:
    for i in range(len(numeros)):
        if num3 == numeros[i] and f == 0:
            p = i
            f += 1
    print(f"El numero {num3} esta en la posicion {p}")
else:
    print("El numero no esta en la lista")
#p
numeros.reverse()
print(f"Lista invertida {numeros}")
#q
numeros.sort()
print(f"Lista ordenada {numeros}")