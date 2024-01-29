from commands import *
clist = ["quit", "addllibre", "startprestec", "endprestec", "listllibres", "listprestecs", "listgenere", "maxllibre", "stats", "info"]
command = [""]
while command[0] != "quit" or len(command) != 1:
    command = input("> ").strip().split("-")
    lc = len(command)
    c0 = command[0].lower()
    if c0 == "addllibre" and lc == 6:
        addLlibre(command)
    elif c0 == "startprestec" and lc == 4:
        startPrestec(command)
    elif c0 == "endprestec" and lc == 3:
        endPrestec(command)
    elif c0 == "listllibres" and lc == 1:
        listLlibres()
    elif c0 == "listprestecs" and lc == 1:
        listPrestecs()  
    elif c0 == "listgenere" and lc == 2:
        listGenere(command)
    elif c0 == "maxllibre" and lc == 1:
        maxLlibre()
    elif c0 == "stats"and lc == 1:
        stats()
    elif c0 == "info" and lc == 2:
        info(command)
    elif c0 not in clist:
        print("Error: Comanda incorrecte")
    elif c0 != "quit" or lc != 1:
        print("Error: nº d'arguments incorrecte")