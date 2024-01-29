#Ejercicio 4
#Creamos num con valor 0 para que entre en el bucle
num = 0
#creamos total con 0 para asignarle un valor despues
total = 0
#creamos un rango que mientras este fuera de rango vaya haciendo lo siguiente:
while num <= 1 or num >= 31:
    #pedimos un numero con el rango sugerido.
    num = int(input("Introduce un numero entre 2 y 30: "))
    #si num esta fuera del rango, da mensaje de error
    if num <= 1 or num >= 31:
        print("Numero fuera de rango")
#Este for ira desde el numero introducido hasta el 1
for i in range(num,0,-1):
        #sumamos i al total
    total += i
    #Si es la ultima vez que se ejecutara el bucle, es decir i sea 1 acabara con un "="
    if i == 1:
        print(i, end = " = ")
    #Si no pondra un "+"
    else:
        print(i, end= " + ")
#Finalmente mostramos el valor total
print(total)
 