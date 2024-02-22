#Este archivo es el que gestiona todas las comprobaciones y muestra el resultado de la accion realizada
#Se le importa el archivo persistencia.py para guardar los datos en los archivos y copiar los datos de los archivoa a los diccionarios
#Tambien se le importa el archivo fechas.py para todo lo que tenga que ver con fechas 


import persistencia as p
import fechas as f

ciclos = ["AIF", "TIL", "MIN", "DAM", "ASIC"]

def start():
    p.createDir()

def alta(dni, gs, nota, fecha):
    if dni == False:
        print("El DNI es invalido")
    elif not gs in ciclos:
        print("El ciclo indicado no esta disponible")
    elif nota is None:
        print("La nota ha de ser un numero")
    elif nota < 5:
        print("La nota tiene que estar aprobada es decir almenos un 5")
    elif fecha == False:
        print("La fecha es incorrecta")
    elif f.fecha2Date(fecha) > f.today():
        print("La fecha no puede ser posterior al dia de hoy")
    else:
        inscripcions = p.addInfoToDicts()
        if dni in inscripcions:
            print("El alumno indicado ya esta inscrito a un ciclo")
        else:
            p.addInscripcio(dni, gs, nota, fecha)
            print("Alumno inscrito correctamente")

def baixa(dni):
    inscripcions = p.addInfoToDicts()
    if dni == False:
        print("El DNI es invalido")
    elif not dni in inscripcions:
        print("El alumno no esta inscrito, por lo tanto no se puede dar de baja")
    else:
        p.delAlumne(inscripcions, dni)
        print("El alumno se ha dado de baja correctamente")

def llistat(cicle):
    if cicle in ciclos or cicle == "*":
        p.list(cicle, ciclos)
    else:
        print("El ciclo indicado no esta disponible")

def mitjana():
    inscripcions = p.addInfoToDicts()
    if inscripcions == {}:
        print("No hi ha alumnes inscrits")
    else:
        cadena1 = ""
        cadena2 = ""
        cadena1 = f"Mitjanes a: {f.todays()} {f.times()}\n"
        cadena2 += f"{f.todays()} {f.times()}\n"
        for c in ciclos:
            count = 0
            total = 0
            for inscripcio in inscripcions:
                if inscripcions[inscripcio]['gs'] == c:
                    count += 1
                    total += inscripcions[inscripcio]['nota']
            if count == 0:
                cadena1 += f"{c}\tNo hi ha alumnes inscrits en aquest cicle.\n"
                cadena2 += f"{c}-No hi ha alumnes inscrits en aquest cicle.\n"
            else:
                mitj = total / count
                cadena1 += f"{c}\t{mitj}\n"
                cadena2 += f"{c}-{mitj}\n"
        print(cadena1.strip())
        p.addMitjana(cadena2.strip())


def stats():
    inscripcions = p.addInfoToDicts()
    if inscripcions == {}:
        print("Encara no hi ha alumnes inscrits")
    else:
        print("***\tESTADÍSTIQUES INSCRIPCIONS EL CALAMOT\t***")
        first = True
        for inscripcio in inscripcions:
            if first:
                antiga = inscripcio
                notaA = inscripcio
                notaB = inscripcio
                first = False
            else:
                if f.dateFormat(inscripcions[antiga]['fecha']) > f.dateFormat(inscripcions[inscripcio]["fecha"]):
                    antiga = inscripcio
                if inscripcions[notaA]['nota'] < inscripcions[inscripcio]['nota']:
                    notaA = inscripcio
                if inscripcions[notaB]['nota'] > inscripcions[inscripcio]['nota']:
                    notaB = inscripcio
        print("Inscripcio més antiga:")
        dic = inscripcions[antiga]
        print(f"Data: {dic['fecha']}")
        print(f"Dni: {antiga} Cicle {dic['gs']} Nota: {dic['nota']}")
        f.transcurseDays(f.dateFormat(dic['fecha']))
        print("*************************************************")
        dic = inscripcions[notaA]
        print("Inscripció amb la nota més alta:")
        print(f"Nota: {dic['nota']}")
        print(f"Dni: {notaA} Cicle {dic['gs']} Data: {dic['fecha']}")
        print("*************************************************")
        dic = inscripcions[notaB]
        print("Inscripció amb la nota més baixa:")
        print(f"Nota: {dic['nota']}")
        print(f"Dni: {notaB} Cicle {dic['gs']} Data: {dic['fecha']}")
