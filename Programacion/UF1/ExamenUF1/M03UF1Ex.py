expediente = {}
option = int(input("Escoge una de las siguientes opciones:\n1) Alta de modulo\n2) Alta de nota de una unidad formativa de un modulo\n3) Ver datos de un modulo\n4) Ver % de unidades formativas aprovadas\n5) Salir\n"))
while option != 5:
    if option == 1:
        modulo = input("Introduce el nombre del modulo: ").upper()
        if modulo in expediente:
            print("El modulo ya estaba creado\nNo hay cambios")
        else:
            expediente[modulo] = {}
            print("Modulo agregado correctamente")
    elif option == 2:
        modulo = input("Introduce el nombre del modulo: ").upper()
        if modulo in expediente:
            uf = input("Introduce el nombre de la unidad formativa: ").upper()
            if uf in expediente[modulo]:
                #Cualquier cosa diferente a "s" no modificara nada
                sn = input("La unidad formativa ya existe\nQuieres modificar la nota de la uf? [s/n]: ")
                if sn.lower() == "s":
                    expediente[modulo][uf] = int(input("Introduce la nota de la unidad formativa: "))
                    while 0 >= expediente[modulo][uf] or expediente[modulo][uf] > 10:
                        print("Nota introducida invalida, 0 o menor no se considera valido y numeros mayores a 10 tampoco")
                        expediente[modulo][uf] = int(input("Introduce la nota de la unidad formativa: "))
                    print("Nota modificada correctamente")
                else:
                    print("No se han hecho cambios")
            else:
                expediente[modulo][uf] = int(input("Introduce la nota de la unidad formativa: "))
                while 0 >= expediente[modulo][uf] or expediente[modulo][uf] > 10:
                    print("Nota introducida invalida, 0 o menor no se considera valido y numeros mayores a 10 tampoco")
                    expediente[modulo][uf] = int(input("Introduce la nota de la unidad formativa: "))
                print("La unidad formativa y la nota de esta se han agregado correctamente")
        else:
            print("El modulo no existe\nNo se han hecho cambios")
    elif option == 3:
        modulo = input("Introduce el nombre del modulo: ").upper()
        if modulo in expediente:
            if expediente[modulo] == {}:
                print("El modulo no tiene notas agregadas\nNo hay nada que mostrar")
            else:
                print(f"Modulo: {modulo}")
                long = len(expediente[modulo])
                print(f"Nº de unidades formativas registradas: {long}")
                mediana = 0
                for uf in expediente[modulo]:
                    print(uf, ":", expediente[modulo][uf])
                    mediana += expediente[modulo][uf]
                mediana = mediana // long
                print(f"Nota mediana del modulo: {mediana} **** Expediente Academico ****")
        else:
            print("El modulo no existe")
    elif option == 4:
        if expediente == {}:
            print("No hay modulos agregados")
        else:
            ufstotal = 0
            ufsap = 0
            for m in expediente:
                for u in expediente[m]:
                    if expediente[m][u] >= 5:
                        ufsap += 1
                    ufstotal += 1
            if ufstotal == 0:
                print("No hay ninguna unidad formativa agregada")
            else:
                pufsap = (ufsap / ufstotal) * 100
                print(f"Tienes el {pufsap}% de las unidades formativas aprovadas")
    else:
        print("No es ninguna de las opciones, por favor introduce el nr correspondiente a la opcion que deseas ejecutar.")
    option = int(input("\nEscoge una de las siguientes opciones:\n1) Alta de modulo\n2) Alta de nota de una unidad formativa de un modulo\n3) Ver datos de un modulo\n4) Ver % de unidades formativas aprovadas\n5) Salir\n"))
print("¡Adios!")