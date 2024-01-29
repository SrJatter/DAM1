books = {}
students = {}
lending = {}

def checkBookCode(code):
    if code in books:
        return False
    else:
        return True

def updateBooks(code, title, author, genre, pags):
    books[code] = {'title': title,
                   'author': author,
                   'genre': genre,
                   'pags': pags,
                   'lending': False}

def checkLendingCode(code):
    if books[code]['lending'] == True:
        return False
    else:
        return True

def updateLendings(code, name, start, end):
    books[code]['lending'] = True
    if name not in students:
        students[name] =[]
    students[name].append([code, start, end, "", False])
    lending[code] = name

def matchLendingStudentCode(code):
    name = lending[code]
    return name

def checkPosition(name, code):
    position = -1
    count = -1
    for c in students[name]:
        count += 1
        if c[0] == code:
            position = count
    return  position

def incidencesCheck(code, realend):
    name = matchLendingStudentCode(code)
    position = checkPosition(name, code)
    if realend > students[name][position][2]:
        students[name][position][4] = True
        print("El llibre s'ha retornat amb retard. Incidència registrada.")
    if realend >= students[name][position][1]:
        books[code]['lending'] = False
        students[name][position][3] = realend
        del lending[code]
        print("El llibre ha quedat disponible.")
    else:
        print("Error: La data de retorn no pot ser anterior a la data d'inici del préstec.")

def numbooks():
    count = 0
    for b in books:
        count += 1
    return count
def incidences():
    count = 0
    for n in students:
        for l in students[n]:
            if l[-1] == True:
                count += 1
    return count

def avgpags():
    pags = 0
    totalbooks = numbooks()
    for b in books:
        pags += books[b]['pags']
    return pags / totalbooks

def studentLendingBooks(name):
    if name in students:
        count = 0
        for l in lending:
            position = checkPosition(name, l)
            if lending[l] == name:
                count += 1
                print(f"Llibre: {l} - {books[l]['title']} Inici: {students[name][position][1]} Data fi: {students[name][position][2]}")
        if count == 0:
            print("L'alumne indicat no té cap llibre en préstec.")
    else:
        print("L'alumne indicat no té cap llibre en préstec.")

def studentIncidences(name):
    if name in students:
        count = 0
        for l in range(len(students[name])):
            if students[name][l][4] == True:
                code = students[name][l][0]
                count += 1
                print(f"Llibre: {code} Data Inici Préstec: {students[name][l][1]} Data Fi: {students[name][l][2]} Data Retorn: {students[name][l][3]}")
        if count == 0:
            print("L'alumne indicat no té cap incidència registrada.")
    else:
        print("L'alumne indicat no té cap incidència registrada.")