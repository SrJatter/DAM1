#Ejercicio 4
#Creamos las variables de los diferentes instrumentos
#A cada una le asignamos el numero de partituras
guitarra = 696
piano = 718
bateria = 256
saxo = 310
#Creamos esta variable y le pedimos al usuario que introduzca un instrumento
instrumento = input("De que instrumento quieres las partituras, guitarra, piano, bateria o saxo: ")
#Ahora con una estructura if-elif-else para comprobar que instrumento ha introducido
#Si es uno de estos mostrara el numero de partituras que tiene ese instrumento
#Si no es ninguno mostraremos el error
if instrumento == "guitarra":
    print(f"La guitarra tiene {guitarra} partituras")
elif instrumento == "piano":
    print(f"La piano tiene {piano} partituras")
elif instrumento == "bateria": 
    print(f"La bateria tiene {bateria} partituras")
elif instrumento == "saxo":
    print(f"La saxo tiene {saxo} partituras")
else:
    print("Has introducido un instrumento diferente")