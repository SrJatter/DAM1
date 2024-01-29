import datetime
import locale
from user import esBisiesto
locale.setlocale(locale.LC_ALL, 'ca_ES.UTF-8')

def avui():
    return datetime.date.today().strftime("Avui és: %d de %B del %Y")

def properAniversari(fecha):
    fecha = fecha.split("/")
    d = int(fecha[0])
    m = int(fecha[1])
    y = datetime.date.today().year
    if datetime.date.today().month > m or (datetime.date.today().month == m and datetime.date.today().day >= d):
        y += 1
    if d == 29 and m == 2:
        while esBisiesto(y) == False:
            y += 1
    return datetime.date(y,m,d).strftime("El proper aniversari es el: %d/%m/%Y")

def quantFalta(fecha):
    fecha = properAniversari(fecha).replace("El proper aniversari es el: ", "").split("/")
    d = int(fecha[0])
    m = int(fecha[1])
    y = int(fecha[2])
    ad = datetime.date.today().day
    am = datetime.date.today().month
    if m == am and d == ad:
        return "Felicitats!!! És el teu aniversari!!"
    else:
        queda = datetime.date(y, m, d) - datetime.date.today()
        return f"Falten {queda.days} dies per al teu aniversari"

def aniversari(fecha):
    fecha = fecha.split("/")
    m = int(fecha[1])
    if m == datetime.date.today().month:
        return True
    else:
        return False