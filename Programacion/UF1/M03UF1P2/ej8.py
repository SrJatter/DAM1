#Ejercicio 8
#Creamos las variables para asignar los puntos anotados
l = 0
v = 0
#creamos equipo para asignarle L o V
equipo = ""
#El numero de veces que queremos que pida los datos
veces = int(input())
#Este for es para asignar el rango de veces
for i in range(veces):
    #pedimos letra de equipo y los puntos
    equipo = input()
    puntos = int(input())
    #aqui comprovamos que letra es para asignar los puntos a cada uno
    if equipo == "L":
        l += puntos
    elif equipo == "V":
        v += puntos
#Si l es mayor que v gana L
if l > v:
    print("L", l, v)
#Si v es mayor que l gana V
elif v > l:
    print("V", l, v)
#Si es empapte se pone una E    
else:
    print("E", l, v)