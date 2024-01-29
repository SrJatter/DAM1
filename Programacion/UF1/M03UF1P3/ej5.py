#Pedimos el nr de casos
casos = int(input("Nr de casos: "))
#Mientras casos sea negativo, mostrara un error y volvera a pedir el nr de casos
while casos < 0:
    print("Los casos no pueden ser negativos")
    casos = int(input("Nr de casos: "))
#Hacemos un for que se repetira el nr de casos que se ha introducido
for i in range(casos):
    #Pedimos los camiones y las patatas que lleva cada uno y se guardan como lista
    numeros = input(f"Caso {i + 1}\nEl primer numero son los camiones que llegan y los demas son las patatas que lleva cada camion.\nIntroduce los números separados por espacios:\n").split()
    #Mientras la longitud de numeros no sea igual al primer elemento de numeros +1 "+1 ya que si introduce un 3 y la cantidad de patatas de cada uno la serian 4 elementos en la lista no 3"
    while len(numeros) != int(numeros[0]) + 1:
        #Si el primer elemento de numeros es negativo mostrara un error, si no mostrara otro error "aclarando" el enunciado
        if int(numeros[0]) < 0:
            print("Los camiones no pueden ser negativos")
        else:
            print("Por favor introduce el numero de camiones y luego las patatas que lleva cada camion separados por espacios.")
        #volvemos a pedir el nr de camiones y las patatas de cada uno
        numeros = input(f"Caso {i + 1}\nEl primer numero son los camiones que llegan y los demas son las patatas que lleva cada camion.\nIntroduce los números separados por espacios:\n").split()
    #Creamos la variable first para comprobar que no sea el primer elemento de la lista
    first = 1
    #Variable para sumar las patatas
    suma = 0
    #Variable para comprobar si hay un error en la cantidad de patatas
    err = 0
    #Pasamos por cada elemento de la lista numeros
    for i in numeros:
        #Si first es 0... Si no first sera 0
        if first == 0:
            #Si "i" es negativo err +1, si no suma +"i" 
            if int(i) < 0:
                err += 1
            else:
                suma += int(i)
        else:
            first = 0
    #Si no ha habido patatas negativas muestra la suma, si no muestra un mensaje de error
    if err == 0:
        print(suma)
    else:
        print("Caso incorrecto, no pueden haber patatas negativas")