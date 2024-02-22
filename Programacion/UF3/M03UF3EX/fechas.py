#Este archivo gestiona las fechas usando datetime

import datetime as dt

def fecha2Date(fechaString):
    fecha = dt.datetime.strptime(fechaString, "%d-%m-%Y")
    return dt.date(fecha.year, fecha.month, fecha.day)

def today():
    return dt.date.today()

def todays():
    return dt.date.today().strftime("%d/%m/%Y")

def times():
    return dt.datetime.today().strftime("%H:%M:%S")

def dateFormat(date):
    date = date.split("-")
    d = int(date[0])
    m = int(date[1])
    y = int(date[2])
    return dt.date(y,m,d)

def transcurseDays(start):
    today = dt.date.today()
    day = today - start
    day = day.days
    if day == 0:
        print("Es Avui")
    elif day > 0:
        print(f"Han passat {day} dies.")
    else:
        day = start - today
        day = day.days
        print(f"Faltan {day} dies.")