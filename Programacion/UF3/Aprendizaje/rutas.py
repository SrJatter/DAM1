import os
import sys
alumnos = {}  # Diccionario para almacenar información de los alumnos
nombre_carpeta = "./Prueba1"  # Ruta de la carpeta donde se encuentra el archivo
ruta_archivo = nombre_carpeta+"/notas.txt"  # Ruta completa del archivo de notas

if os.path.exists(nombre_carpeta):  # Verifica si la carpeta existe
    if os.path.exists(ruta_archivo):  # Verifica si el archivo de notas existe
        f = open(ruta_archivo, "r")  # Abre el archivo en modo lectura
        lineas = f.readlines()  # Lee todas las líneas del archivo
        for linea in lineas:
            linea = linea.split("-")  
            nombre = linea[0]
            nota = linea[1].replace("/n","")
            nota = int(nota)
            alumnos[nombre] = nota 
        f.close()
    else:
        print()
else:
    os.mkdir(nombre_carpeta)

comando = sys.argv
if len(comando) > 1:
    if len(comando) == 2:
        if comando[1].lower() == "list":
            if len(alumnos) == 0:
                print("No hay alumnos registrados")
            else:
                for alumno in alumnos:
                    print(alumno, "-", alumnos[alumno])
        else:
            print("comando incorrecto")
    elif len(comando) == 3:
        nombre = comando[1]
        nota = comando[2]
        if nombre not in alumnos:
            alumnos[nombre] = nota
            f = open(ruta_archivo, "a")
            f.write(nombre+"-"+str(nota)+"\n")
            f.close()
            print("alumno registrado")
        else:
            print("alumno ya registrado")

else:
    print("uso fixer.py nombre_alumno nota (para añadir alumno)")
    print("uso fixer.py list (para listar alumnos)")