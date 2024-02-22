#Este archivo realiza diferentes validaciones de los argumentos que se introduzcan

import datetime as dt

def checkLenCommand(args, n):
    if len(args) == n:
        return True
    print("Error: Numero d'arguments incorrecte")

def dniChecker(dni):
    letra = dni[-1].upper()
    if len(dni) != 9 or (not dni[:-1].isdigit() or not letra.isalpha()):
        return False
    letrasValidas = "TRWAGMYFPDXBNJZSQVHLCKE"
    controlLetra = int(dni[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        return False
    return dni

def floatChecker(num):
    nums = num.split(".")
    if ((nums[0].isdigit() and len(nums) == 1) or (len(nums) == 2 and nums[1].isdigit())) and float(num) > 0:
            return float(num)
    return None

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