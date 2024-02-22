#Archivo principal, se ejecuta con argumentos
#Cada comando se ejecuta a traves de una funcion del archivo gestion.py, que es el que lleva los diccionarios
#Tambien usa unas funciones de comprobacion del archivo commands.py

import commands as c
import gestion as g
import sys

#Para comprobar si existe la carpeta y crearla en caso contrario
g.start()

if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == "afegir":
        if len(sys.argv) == 6 and sys.argv[2].lower() == "habitacio":
            args = sys.argv[3:]
            hab = c.intChecker(args[0])
            cap = c.intChecker(args[1])
            preu = c.floatChecker(args[2])
            g.addHabitacioGest(hab, cap, preu)
        elif len(sys.argv) == 8 and sys.argv[2].lower() == "reserva":
            args = sys.argv[3:]
            hab = c.intChecker(args[0])
            nom = args[1].capitalize()
            cog = args[2].capitalize()
            dni = c.dniChecker(args[3])
            tel = c.telChecker(args[4])
            g.addReservaGest(hab, nom, cog, dni, tel)
        else:
            print("Error: Numero d'arguments incorrecte")
    elif arg1 == "finalitzar":
        if c.checkLenCommand(sys.argv, 4):
            args = sys.argv[2:]
            hab = c.intChecker(args[0])
            dies = args[1]
            g.endReservaGest(hab, dies)
    elif arg1 == "netejar":
        if c.checkLenCommand(sys.argv, 3):
            hab = c.intChecker(sys.argv[2])
            g.cleanHabitacioGest(hab)
    elif arg1 == "list":
        if c.checkLenCommand(sys.argv, 2):
            g.listar()
    elif arg1 == "info":
        if c.checkLenCommand(sys.argv, 3):
            dni = c.dniChecker(sys.argv[2])
            g.info(dni)
    elif arg1 == "reserves":
        if c.checkLenCommand(sys.argv, 2):
            g.listReserves()
    else:
        print("Error: Comanda incorrecta")
else:
    print("Error: No se han introducido argumentos")