#Lista vacia
lista = []
#Pedimos al usuario que escoga una de las opciones
option = int(input("Escoge una de las siguientes opciones:\n1) Añadir palabra.\n2) Contar.\n3) Modificar.\n4) Eliminar.\n5) Mostrar.\n6) Sortir.\n"))
#Mientras option no sea 6...
while option != 6:
    #Si selecciona la opcion 1 se le pedira al usuario que ingrese una palabra
    if option == 1:
        lista.append(input("Escribe la palabra: "))
    #Si selecciona la opcion 2 se le pedira que introduzca una palabra para ver las veces que aparece en la lista
    elif option == 2:
        palabra = input("Inroduce la palabra que deseas contar las veces que aparece en la lista: ")
        #Creamos esta variable para contar las veces que aparece la palabra
        contar = 0
        #Si la palabra esta en la lista... Si no mostrara un mensaje
        if palabra in lista:
            #Pasamos por cada elemento de la lista
            for i in lista:
                #Si la palabra introducida por el usuario es igual al elemento "i" de la lista, contar +1
                if palabra == i:
                    contar += 1
            print(f"La palabra '{palabra}' aparece {contar} veces en la lista.")
        else:
            print(f"La palabra '{palabra}' no esta en la lista.")
    #Si selecciona la opcion 3 se le pedira que introduzca dos palabras en la misma linea, la primera sera la que se quiera modificar y la segunda sera para modificar la en la lista
    elif option == 3:
        palabras = input("Inroduce la palabra que deseas cambiar y la palabra por la que la quieres sustituir, separadas por un espacio: ").split()
        #Si la primera palabra esta en la lista... Y mostrara que lo ha hecho, si no mostrara un mensaje
        if palabras[0] in lista:
            #Pasamos por cada nr de posicion de la lista
            for i in range(len(lista)):
                #Si la lista con la posicion "i" es igual a la primera palabra, se modifica de la lista la posicion "i" por la segunda palabra
                if lista[i] == palabras[0]:
                    lista[i] = palabras[1]
            print("¡Hecho!")
        else:
            print(f"La palabra '{palabras[0]}' no esta en la lista, no se han hecho cambios.")
    #Si selecciona la opcion 4 se le pedira al usuario una palabra para eliminarla de la lista
    elif option == 4:
        palabra = input("Inroduce la palabra que deseas eliminar de la lista: ")
        #Si la palabra esta en la lista... Si no mostrara un mensaje
        if palabra in lista:
            #Creamos esta variable para que si la palabra aparece varias veces no salte un error de fuera de rango ya que la lista va modificando su tamaño por asi decirlo
            n = 0
            #Pasamos por cada nr de posicion de la lista
            for i in range(len(lista)):
                #Si la posicion n de lista es igual a palabra, se elmina la palalabra y n -1 "el remove solo elimina la primera palabra que encuentra pero al repetir el bucle se eliminan todas las palabras que coincidan, y se le resta 1 a n para reducir el tamaño de la lista"
                if lista[n] == palabra:
                    lista.remove(palabra)
                    n -= 1
                n += 1
            print("¡Hecho!")
        else:
            print(f"La palabra '{palabra}' no esta en la lista, no se han hecho cambios.")
    #Si selecciona la opcion 5 se muestran los elementos de la lista
    elif option == 5:
        #Si la lista no esta vacia... Si no mostrara un mensaje
        if len(lista) != 0:
            print("Estos son los elementos de la lista:")
            #Pasamos por cada elemento de la lista y lo mostramos separado por un tab
            for i in lista:
                print(i, end = "\t")
            print(end = "\n")
        else:
            print("La lista esta vacia.")
    #Si no es ninguna de las opciones imprime un mensaje de error
    else:
        print("No es ninguna de las opciones, por favor introduce el nr correspondiente a la opcion que deseas ejecutar.")
    #Volvemos a pedir al usuario que seleccione una opcion
    option = int(input("Escoge una de las siguientes opciones:\n1) Añadir palabra.\n2) Contar.\n3) Modificar.\n4) Eliminar.\n5) Mostrar.\n6) Sortir.\n"))
#Si selecciona la opcion 6 sale del bucle y muestra un mensaje
print("¡Adios!")