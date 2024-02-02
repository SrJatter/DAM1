#Este archivo contiene el menu y ejecuta las funciones del archivo comandos.py
import comandos as c
check = True
comandList = ["registrar", "esborrar", "list", "setmana", "primera"]
while check:
    comando = input().lower().split(",")
    c0 = comando[0]
    if c0 == "registrar":
        c.registrar(comando)
    elif c0 == "esborrar":
        c.esborrar(comando)
    elif c0 == "list":
        c.list(comando)
    elif c0 == "setmana":
        c.setmana(comando)
    elif c0 == "primera":
        c.primera(comando)
    elif comando == ["quit"]:
        if c.checkParametros(comando, 1):
            check = False
            print("Adios")
        else:
            print("Error: Numero de parametros incorrecto")
    else:
        print("Error: Comando incorrecto")