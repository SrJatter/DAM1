#Archivo con las funciones principales que se ejecutan en el menu y tambien accede al archivo misiones.py
import datetime as dt
import misiones as m

def checkParametros(comando, n):
    if len(comando) == n:
        return True
    else:
        print("Error: Numero de parametros incorrecto")

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def convertDate(date):
    d, m, y = date.split('-')
    if d.isdigit() and m.isdigit() and y.isdigit() and 0 < int(y) and 0 < int(m) < 13:
        d, m, y = int(d), int(m), int(y)
        m_days = isLeap(y)
        if 0 < d <= m_days[m-1]:
            start = dt.date(y, m, d).strftime("%d-%m-%Y")
            return start
        else:
            return False
    else:
        return False


def registrar(comando):
    if checkParametros(comando, 4):
        if m.checkMision(comando[1]):
            if convertDate(comando[3]) != False:
                m.registrarMision(comando[1], comando[2], comando[3])
                print("La mision se ha registrado correctamente")
            else:
                print("Error: La fecha es incorrecta")
        else:
            print("Error: La mision ya estaba registrada")


def esborrar(comando):
    if checkParametros(comando, 2):
        if m.voidMision() == False:
            if not m.checkMision(comando[1]):
                m.borrarMision(comando[1])
                print("La mision se ha borrado correctamente")
            else:
                print("Error: La mision no existe")


def list(comando):
    if checkParametros(comando, 2):
        if comando[1].isdigit() and int(comando[1]) > 0:
            if m.voidMision() == False:
                m.checkAndListYearMision(comando[1])

        else:
            print("Error: Año invalido")


def setmana(comando):
    if checkParametros(comando, 1):
        if m.voidMision() == False:
            today = dt.date.today()
            seven = today + dt.timedelta(days = 6)
            m.checkMisionesSemana(today, seven)

def primera(comando):
    if checkParametros(comando, 1):
        if m.voidMision() == False:
            m.oldestMision()