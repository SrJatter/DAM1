salir = input("Quieres salir? si/no: ")
while salir != "si":
    if salir == "no":
        print("Como quieras...")
    else:
        print("Solo hay dos opciones o ¨si¨ o ¨no¨")
    salir = input("Quieres salir? si/no: ")
print("Adios")