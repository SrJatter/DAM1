#Pedimos un numero
num = int(input("Introduce un numero (numero negativo para salir): "))
#Creamos una lista vacia
lista = []
#Creamos otra lista vacia esta para que no hayan numeros repetidos
norep = []
#Mientras num sea negativo
while num >= 0:
    #Si num no esta en lista añade el numero a la lista
    if num not in lista:
        norep.append(num)
    #Añadimos num a la lista
    lista.append(num)
    #Volvemos a pedir el numero
    num = int(input("Introduce un numero (numero negativo para salir): "))
#Mostramos la lista de numeros separados por espacios
print("Lista de numeros")
for i in lista:
    print(i, end = " ")
#Mostramos los numeros de la lista sin repeticiones separados por espacios
print("\nlista de numeros sin repeticiones")
for i in norep:
    print(i, end = " ")