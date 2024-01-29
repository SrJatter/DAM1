#Ejercicio 7
#Pedimos al usuario que introduzca el numero de alumnos y guardamos la informacion en esta variable
alumnos = int(input("Introduce el numero de alumnos que van al viaje: "))
#Creamos la variable coste para ir poniendo el coste dependiendo del nr de alumnos
coste = 0
#Ahora mediante una estructura de condicionales comprobaremos en que rango se encuentra el nr de alumnos 
#dependiendo del nr mostraremos un precio por alumno y el coste total del autobus
if alumnos >= 100:
    coste = 65
    print(f"Cada alumno tiene que pagar {coste}€, el coste total del autobus es {alumnos * coste}€")
elif 50 <= alumnos <= 99:
    coste = 70
    print(f"Cada alumno tiene que pagar {coste}€, el coste total del autobus es {alumnos * coste}€")
elif 30 <= alumnos <= 49:
    coste = 95
    print(f"Cada alumno tiene que pagar {coste}€, el coste total del autobus es {alumnos * coste}€")
else:
    coste = 4000
    print(f"Cada alumno tiene que pagar {coste / alumnos}€, el coste total del autobus es {coste}€")