err = 1
while err == 1:
    try:
        mt = int(input("Introduce la cantidad de minutos que quieras: "))
        err = 0
    except ValueError:
        print("¡Por favor, no introduzca otros caracteres no numericos o numeros con decimales!")
m = mt
h = 0
while m >= 60:
    m -= 60
    h += 1
print(mt, "minutos són", h, "horas y", m, "minutos")