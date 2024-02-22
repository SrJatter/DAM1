#Este archivo se encarga de leer y modificar los datos de los archivos
#Y tambien usando la libreria os se usa para verificar si la ruta existe o no

import os

rutacarpeta = "./dades"
rutaHabitacions = rutacarpeta + "/habitacions.txt"
rutaReserves = rutacarpeta + "/reserves.txt"

#Esta funcion comprueba que la carpeta dades este creada, si no la crea
def createDir():
    if not os.path.exists(rutacarpeta):
        os.mkdir(rutacarpeta)

#Esta funcion añade una habitacion al archivo habitaciones.txt
#Recibe la informacion de la habitacion
def addHabitacio(hab, cap, preu):
    f = open(rutaHabitacions, "a")
    f.write(f"{hab},{cap},{preu},DISPONIBLE\n")
    f.close()

#Esta funcion se lleva la informacion que tienen los archivos y la pone en un diccionario
#Recibe un str que tiene que ser habitacions o reserves
#Devuelve un diccionario con la informacion del archivo seleccionado
def addInfoToDicts(file):
    dict = {}
    rutaArchivo = {"habitacions": rutaHabitacions, "reserves": rutaReserves}
    ruta = rutaArchivo[file]
    if os.path.exists(ruta):
        f = open(ruta, "r")
        lines = f.readlines()
        for line in lines:
            info = line.strip().split(",")
            if file == "habitacions":
                dict[int(info[0])] = {'capacitat': int(info[1]), 'preu': float(info[2]), 'disp': info[3]}
            elif file == "reserves":
                dict[int(info[0])] = {'nom': info[1], 'cog': info[2], 'dni': info[3], 'tel': info[4]}
        f.close()
    return dict

#Esta funcion sobreescribe el archivo habitacions.txt para cambiar la disponibilidad de una habitacion
#Recibe un diccionario, el nr de habitacion y un str que es la disponibilidad(DISPONIBLE, OCUPADA, BRUTA)
def saveInfoToHab(habitacions, hab, newDisp):
    f = open(rutaHabitacions, "w")
    for habitacio in habitacions:
        cap = habitacions[habitacio]['capacitat']
        preu = habitacions[habitacio]['preu']
        if habitacio == hab:
            disp = newDisp
        else:
            disp = habitacions[habitacio]['disp']
        f.write(f"{habitacio},{cap},{preu},{disp}\n")
    f.close()

#Esta funcion añade una reserva al archivo reserves.txt
#Recibe un diccionario y la informacion de la reserva
def addReserva(habitacions, hab, nom, cog, dni, tel):
    saveInfoToHab(habitacions, hab, "OCUPADA")
    f = open(rutaReserves, "a")
    f.write(f"{hab},{nom},{cog},{dni},{tel}\n")
    f.close()

#Esta funcion finaliza una reserva, sobreescribiendo el archivo reserves.txt para eliminar la informacion sobre la reserva
#Recibe dos diccionarios, el nr de habitacion y un str que es la disponibilidad
def endReserva(habitacions, reserves, hab, newDisp):
    saveInfoToHab(habitacions, hab, newDisp)
    f = open(rutaReserves, "w")
    for reserva in reserves:
        nom = reserves[reserva]['nom']
        cog = reserves[reserva]['cog']
        dni = reserves[reserva]['dni']
        tel = reserves[reserva]['tel']
        if reserva != hab:
            f.write(f"{reserva},{nom},{cog},{dni},{tel}\n")
    f.close()

#Esta funcion comprueba que el archivo seleccionado no esta vacio
#Recibe un str que tiene que ser habitacions o reserves
#Devuelve True si no esta vacio, si esta vacio devuelve False
def checkNotVoid(file):
    rutaArchivo = {'habitacions': rutaHabitacions, 'reserves': rutaReserves}
    ruta = rutaArchivo[file]
    if os.path.exists(ruta):
        f = open(ruta, "r")
        cont = f.read()
        if cont != "":
            f.close()
            return True
        f.close()
    return False

#Esta funcion comprueba si el dni tiene alguna reserva
#Recibe un dni
#Devuelve True si tiene alguna reserva, si no la tiene devuelve False
def checkReservaDNI(dni):
    if os.path.exists(rutaReserves):
        f = open(rutaReserves, "r")
        lines = f.readlines()
        for line in lines:
            info = line.strip().split(",")
            if info[3] == dni:
                f.close()
                return True
    return False