import datetime as dt
from library import *

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def convertDate(date):
    d, m, y = date.split('/')
    if d.isdigit() and m.isdigit() and y.isdigit() and 0 < int(y) and 0 < int(m) < 13:
        d, m, y = int(d), int(m), int(y)
        m_days = isLeap(y)
        if 0 < d <= m_days[m-1]:
            start = dt.date(y, m, d)
            return start
        else:
            return False
    else:
        return False

def addLlibre(command):
    if checkBookCode(command[1]):
        if command[5].isdigit() and int(command[5]) > 0:
            updateBooks(command[1], command[2], command[3], command[4].lower(), int(command[5]))
            print("Llibre registrat.")
        else:
            print("Error: nº pagines incorrectes")
    else:
        print("Error: Ja existeix un llibre amb aquest codi")

def startPrestec(command):
    if not checkBookCode(command[1]):
        if checkLendingCode(command[1]):
            if convertDate(command[3]) != False:
                start = convertDate(command[3])
                end = start + dt.timedelta(days = 15)
                updateLendings(command[1], command[2].capitalize(), start, end)
                print(f"Préstec registrat. El llibre s’ha de retornar: {end}")
            else:
                print("Error: Data incorrecte")
        else:
            print("Error: El llibre indicat ja està en préstec")
    else:
        print("Error: No hi ha cap llibre registrat amb el codi indicat")

def endPrestec(command):
    if not checkBookCode(command[1]):
        if not checkLendingCode(command[1]):
            if convertDate(command[2]) != False:
                realend = convertDate(command[2])
                incidencesCheck(command[1], realend)
            else:
                print("Error: Data incorrecte")
        else:
            print("Error: El llibre no està en préstec")
    else:
        print("Error: No hi ha cap llibre registrat amb el codi indicat")

def listLlibres():
    if books != {}:
        sortedBooks = sorted(books.keys())
        for c in sortedBooks:
        #for c in books:
            if books[c]['lending'] == False:
                print(f"{c} : {books[c]['title']} , {books[c]['author']} - ESTAT: disponible")
            else:
                print(f"{c} : {books[c]['title']} , {books[c]['author']} - ESTAT: en préstec")
    else:
        print("No hi ha cap llibre registrat.")

def listPrestecs():
    if lending != {}:
        actualDate = dt.date.today()
        sortedLending = sorted(lending.keys())
        for l in sortedLending:
        #for l in lending:
            name = matchLendingStudentCode(l)
            position = checkPosition(name, l)
            if students[name][position][2] < actualDate:
                print(f"Llibre: {l} {books[l]['title']} Alumne: {name} Data inici: {students[name][position][1]} Data fi: {students[name][position][2]} * FORA DE TERMINI *")
            else:
                print(f"Llibre: {l} {books[l]['title']} Alumne: {name} Data inici: {students[name][position][1]} Data fi: {students[name][position][2]}")   
    else:
        print("No hi ha cap prestec registrat.")

def listGenere(command):
    genre = command[1].lower()
    checkGenre = 0
    for c in books:
        if books[c]['genre'] == genre:
            if books[c]['lending'] == False:
                print(f"{c} : {books[c]['title']} , {books[c]['author']} - ESTAT: disponible")
            else:
                print(f"{c} : {books[c]['title']} , {books[c]['author']} - ESTAT: en préstec")
            checkGenre += 1
    if checkGenre == 0:
        print("No hi ha cap llibre del gènere indicat.")

def maxLlibre():
    if books != {}:
        maxpags = 0
        maxbook = ""
        for c in books:
            if books[c]['pags'] > maxpags:
                maxpags = books[c]['pags']
                maxbook = books[c]['title']
        print(f"El llibre amb més pàgines de la biblioteca és: {maxbook} , amb {maxpags} pàgines")
    else:
        print("No hi ha cap llibre registrat.")

def stats():
    if books != {}:
        nrb = numbooks()
        i = incidences()
        ap = avgpags()
        print(f"Número de llibres registrats: {nrb}\nNúmero d'incidències registrades: {i}\nMitjana de pàgines per llibre: {ap}")
    else:
        print("No hi ha cap llibre registrat.")

def info(command):
    print("Llibres en préstec:")
    studentLendingBooks(command[1].capitalize())
    print("Incidències:")
    studentIncidences(command[1].capitalize())
