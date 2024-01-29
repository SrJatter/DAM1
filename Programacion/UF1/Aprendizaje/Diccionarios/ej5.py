lista = {}
option = int(input("Escoge una de las siguientes opciones:\n1) Añadir personaje.\n2) Borrar personaje.\n3) Mostrar personaje.\n4) Mostrar todos los datos de todos los personajes.\n5) Mostrar los datos de un tipo de personaje.\n6) Salir.\n"))
while option != 6:
    if option == 1:
        personaje = input("Nombre del personaje: ")
        choose = ""
        if personaje in lista:
            print("El Personaje ya esta añadido")
            choose = input("Quieres reemplazar los datos del personaje [s/n]?")
        if choose == "" or choose == "s":
            stats = {}
            stats["Fuerza:"] = int(input("Fuerza: "))
            stats["Resistencia:"] = int(input("Resistencia: "))
            stats["Vida:"] = int(input("Vida: "))
            stats["Tipo:"] = input("Tipo [guerrero o mago]: ")
            while stats["Tipo:"] != "mago" and stats["Tipo:"] != "guerrero":
                print("Tipo incorrecto, solo puede ser guerrero o mago")
                stats["Tipo:"] = input("Tipo [guerrero o mago]: ")
            if stats["Tipo:"] == "guerrero":
                stats["Armadura:"] = int(input("Armadura: "))
            else:
                stats["Mana:"] = int(input("Mana: "))
            lista[personaje] = stats
            print("Personaje añadido correctamente")
    elif option == 2:
        if lista != {}:
            print("Que personaje quieres eliminar:")
            for i in lista:
                print(i, end = (" "))
            personaje = input("\n")
            if personaje in lista:
                lista.pop(personaje)
                print("El personaje se ha eliminado correctamente")
            else:
                print("El personaje no esta en la lista")
        else:
            print("La lista esta vacia")
    elif option == 3:
        if lista != {}:
            print("De que personaje quieres ver los datos:")
            for i in lista:
                print(i, end = (" "))
            personaje = input("\n")
            if personaje in lista:
                for d in lista[personaje]:
                    print(d, lista[personaje][d], end = " ")
                print()
            else:
                print("El personaje no esta en la lista")
        else:
            print("La lista esta vacia")
    elif option == 4:
        if lista != {}:
            for i in lista:
                print("Nombre:", i)
                for n in lista[i]:
                    print(n, lista[i][n], end = "   ")
                print()
                print("------------------------------------------------------------")
        else:
            print("La lista esta vacia")
    elif option == 5:
        if lista != {}:
            tipo = input("De que tipo de personaje quieres ver los datos [guerrero o mago]: ")
            while tipo != "mago" and tipo != "guerrero":
                print("Tipo incorrecto, solo puede ser guerrero o mago")
                tipo = input("De que tipo de personaje quieres ver los datos [guerrero o mago]: ")
            hay = 0
            for i in lista:
                if lista[i]["Tipo:"] == tipo:
                    hay += 1
                    print("Nombre:", i)
                    for n in lista[i]:
                        print(n, lista[i][n], end = "   ")
                    print()
                    print("------------------------------------------------------------")
            if hay == 0:
                print("No hay personaje de ese tipo")
        else:
            print("La lista esta vacia")
    else:
        print("No es ninguna de las opciones, por favor introduce el nr correspondiente a la opcion que deseas ejecutar.")
    option = int(input("Escoge una de las siguientes opciones:\n1) Añadir personaje.\n2) Borrar personaje.\n3) Mostrar personaje.\n4) Mostrar todos los datos de todos los personajes.\n5) Mostrar los datos de un tipo de personaje.\n6) Salir.\n"))
print("¡Adios!")