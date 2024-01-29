#Ejercicio 3
#Pedimos la cantidad de veces que queremos introducir un numero
cantidad = int(input("Introduce la cantidad de numeros que quieres introducir: "))
#Si la cantidad es 0 o numero negativo mostrara un error
if cantidad < 1:
    print("Cantidad invalida, no puedes introducir 0 o numeros negativos")
#Si no se cumple la condicion continuamos con el programa
else:
    #Creamos la variable total que sera la suma de todos los valores que se introduzcan
    total = 0
    #Este for repite la cantidad de veces que nos pedira num
    for i in range(cantidad):
        #pedimos el numero en un rango del -100 al 100
        num = int(input("Introduce un numero entre el -100 y 100: "))
        #comprobamos que este dentro del rango pedido
        if -100 <= num <= 100:
            #la primera vez que se ejecuta el bucle asignara a mayor y menor el primer numero
            if i == 0:
                mayor=num
                menor=num
            #A total se le suma num
            total += num
            #Si mayor es menor que num, se le asigna el valor de num a mayor
            if mayor < num:
                mayor = num
            #Si menor es mayor que num, se le asigna el valor de num a menor
            if menor > num:
                menor = num
        #Si esta fuera de rango se mostrara un error
        else:
            print("Numero fuera de rango, no se cuenta el numero.")
    #Si total es 0, significa que todos los numeros han sido invalidos
    if total == 0:
        print("Todos los numeros son invalidos")
    #Mostramos el numero mayor, menor y la mediana aritmetica
    else:
        print(f"El numero mayor es {mayor}\nEl numero menor es {menor}\nLa mediana aritmetica es {total/cantidad}")