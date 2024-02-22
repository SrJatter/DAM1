#Este archivo se encarga de leer y modificar los datos de los archivos
#Y tambien usando la libreria os se usa para verificar si la ruta existe o no

import os

rutaCarpeta = "./documents"
rutaInscripcions = rutaCarpeta + "/inscripcions.txt"
rutaMitjana = rutaCarpeta + "/mitjana.txt"


def createDir():
    if not os.path.exists(rutaCarpeta):
        os.mkdir(rutaCarpeta)

def addInscripcio(dni, gs, nota, fecha):
    f = open(rutaInscripcions, "a")
    f.write(f"{dni}/{gs}/{nota}/{fecha}\n")
    f.close()

def addInfoToDicts():
    dict = {}
    if os.path.exists(rutaInscripcions):
        f = open(rutaInscripcions, "r")
        lines = f.readlines()
        for line in lines:
            info = line.strip().split("/")
            dict[info[0]] = {'gs': info[1], 'nota': float(info[2]), "fecha": info[3]}
        f.close()
    return dict

def delAlumne(inscripcions, dni):
    f = open(rutaInscripcions, "w")
    for inscripcio in inscripcions:
        gs = inscripcions[inscripcio]['gs']
        nota = inscripcions[inscripcio]['nota']
        fecha = inscripcions[inscripcio]['fecha']
        if inscripcio != dni:
            f.write(f"{inscripcio}/{gs}/{nota}/{fecha}\n")
    f.close()

def list(cicle, list):
    if os.path.exists(rutaInscripcions):
        f = open(rutaInscripcions, "r")
        lines = f.readlines()
        count = 0
        for line in lines:
            info = line.strip().split("/")
            dni = info[0]
            gs = info [1]
            nota = info[2]
            fecha = info[3]
            if cicle == "*":
                for ciclo in list:
                    if gs == ciclo:
                        print(f"{fecha}\t{dni}\t{nota}\t{gs}")
                        count += 1
            else:
                if gs == cicle:
                    print(f"{fecha}\t{dni}\t{nota}\t{gs}")
                    count += 1
        if count == 0:
            print("No hi ha alumnes inscrits")
        else:
            print(f"Nº total d'inscripcions: {count}")
            if cicle != "*":
                if count < 30:
                    print(f"Encara queden {30-count} places disponibles")
                elif count > 30:
                    print(f"Ni han {count-30} places de mes")
                else:
                    print("El cupo d'inscripcions esta just a 30")
        f.close()
    else:
        print("No hi ha alumnes inscrits")

def addMitjana(str):
    f = open(rutaMitjana, "w")
    f.write(f"{str}")
    f.close()