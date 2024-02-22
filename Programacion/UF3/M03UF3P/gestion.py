#Este archivo es el que gestiona los diccionarios
#Se le importa el archivo persistencia.py para guardar los datos en los archivos y copiar los datos de los archivoa a los diccionarios
#Ademas lleva a cabo todas las comprobaciones de los datos que recibe

import persistencia as p

#Esta funcion llama a otra funcion de persistencia
def start():
    p.createDir()

#Esta funcion añade una habitacion al archivo habitacions.txt si cumple las condiciones
#Recibe los datos de la habitacion
#Muestra un mensaje de confirmacion si se cumplen las condiciones, si no, muestra un error
def addHabitacioGest(hab, cap, preu):
    if hab is None:
        print("Némero d'habitacio incorrecte. Ha de ser més gran de 0.")
    elif cap is None:
        print("Capacitat incorrecte. Ha de ser més gran de 0.")
    elif preu is None:
        print("Preu incorrecte. Ha de ser més gran de 0..")
    else:
        habitacions = p.addInfoToDicts("habitacions")
        if hab not in habitacions:
            p.addHabitacio(hab, cap, preu)
            print("Habitació registrada")
        else:
            print("Ja existeix una habitacio amb el número indicat.")

#Esta funcion añade una reserva al archivo reservas.txt si se cumplen las condiciones y cambia su estado a ocupada
#Recibe los datos de la reserva
#Muestra un mensaje de confirmacion si se cumplen las condiciones, si no, muestra un error
def addReservaGest(hab, nom, cog, dni, tel):
    if hab is None:
        print("Error: La habitació ha de ser un numero major que 0.")
    else:
        habitacions = p.addInfoToDicts("habitacions")
        if hab in habitacions:
            if habitacions[hab]['disp'] == "DISPONIBLE":
                if dni != False:
                    if tel != False:
                        for habitacio in habitacions:
                            if habitacio == hab:
                                habitacions[hab]['disp'] = "OCUPADA"
                        p.addReserva(habitacions, hab, nom, cog, dni, tel)
                        print("Reserva registrada")
                    else:
                        print("Error: El telèfon es invalid")
                else:
                    print("Error: El DNI es invalid")
            else:
                print("L'habitació no està disponible per a reserves.")
        else:
            print("No existeix una habitació amb el número indicat.")

#Esta funcion finaliza una reserva y cambia su estado a disponible o sucia
#Recibe el nr de habitacion y los dias de estada
#Muestra un mensaje de confirmacion si se cumplen las condiciones, si no, muestra un error
def endReservaGest(hab, dies):
    if hab is None:
        print("Error: La habitació ha de ser un numero major que 0.")
    else:
        habitacions = p.addInfoToDicts("habitacions")
        if hab in habitacions:
            if habitacions[hab]['disp'] == "OCUPADA":
                reserves = p.addInfoToDicts("reserves")
                d = dies.split("-")
                if dies.isdigit() or (dies[0] == "-" and dies[1:].isdigit()):
                    dies = int(dies)
                    if dies < 0:
                        print("El número de dies no pot ser negatiu. Si vols anul·lar la reserva indica número de dies 0.")
                    else:
                        if dies > 0:
                            estat = "BRUTA"
                            preu = float(habitacions[hab]['preu']) * dies
                            print(f"Preu total de l'estada: {preu}€. L'habitació queda en espera del servei de neteja.")
                        else:
                            estat = "DISPONIBLE"
                            print("Reserva anul·lada. Sense cost pel client. L'habitacio torna a estar disponible.")
                        p.endReserva(habitacions, reserves, hab, estat)
                else:
                    print("Els dies han de ser un numero")
            else:
                print("L'habitació no està reservada")
        else:
            print("No existeix una habitació amb el número indicat.")

#Esta funcion cambia el estado de la habitacion a disponible
#Recibe el nr de habitacion
#Muestra un mensaje de confirmacion si se cumplen las condiciones, si no, muestra un error
def cleanHabitacioGest(hab):
    if hab is None:
        print("Error: La habitació ha de ser un numero major que 0.")
    else:
        habitacions = p.addInfoToDicts("habitacions")
        if hab in habitacions:
            if habitacions[hab]['disp'] == "BRUTA":
                p.saveInfoToHab(habitacions, hab, "DISPONIBLE")
                print("Habitació netejada. Queda disponible")
            else:
                print("L'habitació no està bruta.")
        else:
            print("No existeix una habitació amb el número indicat.")

#Esta funcion lista las habitaciones que hay, con su estado y la persona que la ocupa en caso de estar ocupada
def listar():
    if p.checkNotVoid("habitacions"):
        habitacions = p.addInfoToDicts("habitacions")
        reserves = p.addInfoToDicts("reserves")
        total = 0
        d = 0
        o = 0
        b = 0
        print("========\tINFO HOTEL\t========")
        print("hab\tCap\tEstat")
        for hab in habitacions:
            cap = habitacions[hab]['capacitat']
            disp = habitacions[hab]['disp']
            if hab in reserves:
                o += 1
                nom = reserves[hab]['nom']
                cog = reserves[hab]['cog']
                print(f"{hab}\t{cap}\t{disp}\t\t=> Client: {nom} {cog}")
            else:
                if disp == "DISPONIBLE":
                    d += 1
                elif disp == "BRUTA":
                    b += 1
                print(f"{hab}\t{cap}\t{disp}")
            total += 1
        print("========================================")
        print("Total habitacions:", total)
        print(f"Disponibles: {d}\tOcupades: {o}\tBrutes: {b}")
    else:
        print("No hi han habitacions registrades.")

#Esta funcion lista las reservas de un cliente a partir de su dni
#recibe el dni
def info(dni):
    if dni != False:
        if p.checkReservaDNI(dni):
            reserves = p.addInfoToDicts("reserves")
            habs = ""
            first = 0
            for reserva in reserves:
                habd = reserves[reserva] 
                if reserves[reserva]['dni'] == dni:
                    if first == 0:
                        first += 1
                        print(f"Dades del client:\t{habd['nom']} , {habd['cog']} - Tfn: {habd['tel']}")
                    habs += f"Habitació:  {reserva}\n"
            print(habs.strip())
        else:
            print(f"L'hotel no te cap reserva del dni: {dni}")
    else:
        print("Error: El DNI es invalid")

#Esta funcion lista todas las reservas si es que hay alguna
def listReserves():
    if p.checkNotVoid("reserves"):
        reserves = p.addInfoToDicts("reserves")
        print("========\tRESERVES\t========")
        for reserva in reserves:
            habd = reserves[reserva]
            print(f"{reserva} : {habd['dni']} - {habd['nom']} {habd['cog']} - {habd['tel']}")
    else:
        print("No ni han reserves registrades")