#Ejercicio 7
#Creamos las 3 primeras variables del piso menor, mayor y el inicial
piso_menor = int(input())
piso_mayor = int(input())
inicio = int(input())
#creamos la variable movimiento como str, mas adelante la convertiremos a int
movimiento = ""
#Creamos otras tres variables que equivalen al cambio de piso, el desplazo, el piso final y una para contar numeros invalidos como error
cambio_piso = 0
desplazo = 0
piso_final = 0
error = 0
#Mientras movimiento no sea X hara el bucle
while movimiento != "X":
    #Pedimos el numero de piso al que quiere ir
    movimiento = input()
    #Si movimiento no es igual a X hara lo siguiente:
    if movimiento != "X":
        #Convertimos movimiento a int
        movimiento = int(movimiento)
        #Si movimiento esta en el rango del piso menor y el mayor hara lo siguiente:
        if piso_menor <= movimiento <= piso_mayor:
            #Si movimiento es menor a inicio
            if movimiento < inicio:
                #Hatra un for que va de inicio a movimiento restando 1 cada vez
                for i in range(inicio,movimiento,-1):
                    #Sumamos 1 a desplazo
                    desplazo += 1 
                #Sumamos 1 al cambio de piso
                cambio_piso+=1
            #Si movimiento es mayor a inicio
            elif movimiento > inicio: 
                #Hara un for de inicio a movimiento
                for i in range(inicio,movimiento):
                    #Sumamos 1 a desplazo
                    desplazo += 1
                #Sumamos 1 al cambio de piso
                cambio_piso+=1
            #Asignamos a inicio el valor de movimiento para saber en que piso se ha quedado
            inicio = movimiento
        #Si el numero esta fuera de rango sumara 1 a error
        else:
            error += 1
#Asignamos a piso final el valor de inicio
piso_final = inicio
#Si no ha habido ningún número erróneo imprimirá el cambio de piso, desplazo y piso final
if error == 0:
    print(cambio_piso, desplazo, piso_final)
#Si ha tenido algún error, imprimirá lo mismo + la E
else:
    print(cambio_piso, desplazo, piso_final, "E")