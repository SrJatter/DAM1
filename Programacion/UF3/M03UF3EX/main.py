#Archivo principal, se ejecuta con argumentos
#Cada comando se ejecuta a traves de una funcion del archivo gestion.py
#Tambien usa unas funciones de comprobacion del archivo validaciones.py

import validaciones as v
import gestion as g
import sys

g.start()

if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == "alta":
        args = sys.argv[2:]
        if v.checkLenCommand(args, 4):
            dni = v.dniChecker(args[0])
            gs = args[1]
            nota = v.floatChecker(args[2])
            fecha = v.convertDate(args[3])
            g.alta(dni, gs, nota, fecha)
    elif arg1 == "baixa":
        args = sys.argv[2:]
        if v.checkLenCommand(args, 1):
            dni = v.dniChecker(args[0])
            g.baixa(dni)
    elif arg1 == "llistat":
        args = sys.argv[2:]
        if v.checkLenCommand(args, 1):
            g.llistat(args[0])
    elif arg1 == "mitjana":
        args = sys.argv[2:]
        if v.checkLenCommand(args, 0):
            g.mitjana()
    elif arg1 == "stats":
        args = sys.argv[2:]
        if v.checkLenCommand(args, 0):
            g.stats()
    else:
        print("Error: Comanda incorrecta")
else:
    print("Error: No se han introducido argumentos")