#Este modulo es donde se guardaran y se leen todos los datos de las misiones.
import datetime as dt
#El tipo de dato usaso para guardar informacion es un diccionario y su estructura será:
#diccionario{Mision: {'lugar': lugar, 'fecha': fecha}}
#He usado esta estructura para poder organizarla por misiones,
#si lo hubiera hecho por lista no podria identificar rapidamente la informacion de una mision y habria que ir por posiciones.

misiones = {
    "mision1": {"lugar": "A", "fecha": "02-02-2024"},
    "mision2": {"lugar": "B", "fecha": "03-02-2024"},
    "mision3": {"lugar": "C", "fecha": "09-01-2024"},
    "mision4": {"lugar": "D", "fecha": "04-02-2024"},
    "mision5": {"lugar": "E", "fecha": "08-02-2024"},
    "mision6": {"lugar": "F", "fecha": "09-02-2024"}
}

def dateFormat(date):
    date = date.split("-")
    d = int(date[0])
    m = int(date[1])
    y = int(date[2])
    return dt.date(y,m,d)

def transcurseDays(start, today):
    day = today - start
    day = day.days
    if day == 0:
        print("Hoy es la mision mas antigua.")
    else:
        print(f"Han passat {day} dies.")

def voidMision():
    if misiones == {}:
        print("Error: Todavia no hay misiones registradas.")
    else:
        return False

def checkMision(mision):
    if mision in misiones:
        return False
    else:
        return True

def registrarMision(mision, lugar, fecha):
    misiones[mision] = {"lugar": lugar, "fecha": fecha}

def borrarMision(mision):
    del misiones[mision]

def checkAndListYearMision(year):
    check = 0
    for mision in misiones:
        date = misiones[mision]["fecha"].split("-")
        y = date[2]
        if y == year:
            check += 1
            print(f"{misiones[mision]['fecha']}\t{mision}")
    if check == 0:
        print("El año introducido no tiene misiones.")

def checkMisionesSemana(today, seven):
    check = 0
    dema = today + dt.timedelta(days = 1)
    for mision in misiones:
        misiondate = dateFormat(misiones[mision]["fecha"])
        if today <= misiondate <= seven:
            check += 1
            if misiondate == today:
                print(f"=> * AVUI *\t{mision}\t{misiones[mision]['lugar']}")
            elif misiondate == dema:
                print(f"=> DEMÀ\t{mision}\t{misiones[mision]['lugar']}")
            else:
                print(f"{misiones[mision]['fecha']} :\t{mision}\t{misiones[mision]['lugar']}")
    if check == 0:
        print("No hay misiones para esta semana.")

def oldestMision():
    first = 0
    today = dt.date.today()
    for mision in misiones:
        fecha = dateFormat(misiones[mision]["fecha"])
        if first == 0:
            first = 1
            oldest = mision
            oldestdate = fecha
        else:
            if fecha < oldestdate:
                oldest = mision
                oldestdate = fecha
    print(f"La misio més antiga és: {oldest}")
    print(f"Lloc: {misiones[oldest]['lugar']}")
    print(f"Data: {oldestdate.strftime('%d-%m-%Y')}")
    transcurseDays(oldestdate, today)
