nombre = ""
alumnos=[]
while nombre != "*":
    nombre = input("Introduce el nombre: ")
    if nombre != "*":
        edad = int(input("Introduce la edad: "))
        alumnos.append([nombre, edad])
print("Los mayores de edad son:")
mayore = alumnos[0][1]
mayorn = alumnos[0][0]
for i in range(len(alumnos)):
    if alumnos[i][1] >= 18:
        print(alumnos[i][0], alumnos[i][1])
    if alumnos[i][1] > mayore:
        mayore = alumnos[i][1]
        mayorn = alumnos[i][0]
print("El alumno mayor es:", mayorn, mayore)