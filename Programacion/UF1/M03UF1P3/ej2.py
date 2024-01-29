#Importamos random
import random
#Creamos la variable num para introducir un numero entre el 10 y 50
num = int(input("Introduce un numero entre 10 y 50: "))
#Si num no esta en el rango de 10-50 se mostrara un mensaje y se volvera a pedir num hasta que este en el rango
while 10 > num or num > 50:
    print("Numero fuera de rango, recuerda, un numero entre el 10 y el 50")
    num = int(input("Introduce un numero entre 10 y 50: "))
#Creamos la lista numeros
numeros = []
#Hacemos un bucle que se repetira num veces
for i in range(num):
    #Añadimos un nr aleatorio entre 1 y 4
    numeros.append(random.randint(1, 4))
    #Mostramos cada numero añadido separado por un espacio
    print(numeros[-1], end=" ")
#Cambiamos el final de print a salto de linea
print(end = "\n")
#maxrep cuenta las veces que se repite el nr que mas veces aparece
maxrep = 0
#max es el numero que mas veces aparece, se le asigna la primera posicion de la lista por defecto
max = numeros[0]
#Creamos la variable para sumar todos los numeros
suma = 0
#Pasamos por cada numero de la lista numeros
for i in numeros:
    #Creamos la variable reps para contar las veces que se repite "x"
    reps = 0
    #Pasamos otra vez por cada numero de la lista numeros
    for x in numeros:
        #Si "x" es igual a "i", reps +1
        if x == i:
            reps += 1
    #Si reps es mayor que maxrep, maxrep sera reps y max sera "i"
    if reps > maxrep:
        maxrep = reps
        max = i
    #A suma le sumamos "i"
    suma += i
#Calculamos la mediana
mediana = suma / num
#Mostramos el numero que mas veces aparece y las veces que aparece
print(f"El numero que mas veces ha aparecido es el {max} con {maxrep} apariciones")
#Mostramos la mediana
print(f"La mediana de los numeros es:", mediana)