def EsBisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
year = EsBisiesto(2024)
if year:
    print("Es bisiesto")
else:
    print("No es bisiesto")