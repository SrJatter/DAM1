#Importamos random
import random
#Creamos una lista vacia
lista = []
#Hacemos un for que se repetira 30 veces
for i in range(30):
    #Añadimos un numero random entre el 0 y 29 a la lista
    lista.append(random.randint(0, 29))
    #Mostramos cada elemento añadido separado por un espacio
    print(lista[-1], end = " ")
#Cambiamos el final de print a salto de linea
print(end = "\n")
#Creamos la variable rep para ver si hay coincidencias o no
rep = 0
#Hacemos otro for que se repetira 30 veces
for i in range(30):
    #Si "i" es igual a la posicion "i" de lista, mostramos que el que el nr coincide con su posicion y rep +1
    if i == lista[i]:
        print(f"El numero {lista[i]} esta en la posicion {i}")
        rep += 1
#Si rep es 0 mostrara un mensaje para decir que no hay coincidencias
if rep == 0:
    print("Ningun numero coincide con su posicion")