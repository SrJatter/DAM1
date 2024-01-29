import datetime
def demanarEdad():
    edad = -1
    while edad < 0 or edad > 130:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 130:
            print("Porfavor, introduce una edad entre 0 y 130")
    return edad

def validarUsuari(usuari, clau):
    comp = []
    if len(usuari) < 4:
        comp.append(False)
    else:
        comp.append(True)
    if len(clau) < 6:
        comp.append(False)
    else:
        vocales = 0
        for i in clau:
            if i.lower() in "aeiou":
                vocales += 1
        if vocales > 0:
            comp.append(True)
    if comp[0] == True and comp[1] == True:
        return True
    else:
        return False

def esBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def demanarNaixement():
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    checker = True
    while checker:
        dia = int(input("Introduce el dia de nacimiento: "))
        while dia < 1 or dia > 31:
            print("Porfavor, introduce un dia entre 1 y 31")
            dia = int(input("Introduce el dia de nacimiento: "))
        mes = int(input("Introduce el mes de nacimiento: "))
        while mes < 1 or mes > 12:
            print("Porfavor, introduce un mes entre 1 y 12")
            mes = int(input("Introduce el mes de nacimiento: "))
        any = int(input("Introduce el año de nacimiento: "))
        while any < 1900 or any > 2021:
            print("Porfavor, introduce un año entre 1900 y 2020")
            any = int(input("Introduce el año de nacimiento: "))
        if esBisiesto(any):
            meses[1] = 29
        if dia <= meses[mes - 1]:
            checker = False
        else:
            print("La fecha introducida es incorrecta porfavor comprueba que el dia del mes corresponde con los dias que tiene el mes")
    return datetime.date(any, mes, dia).strftime("%d/%m/%Y")

def login(diccionari, usuari, clau):
    if usuari in diccionari:
        if diccionari[usuari]["pass"] == clau:
            return True
        else:
            return False
    else:
        return False
