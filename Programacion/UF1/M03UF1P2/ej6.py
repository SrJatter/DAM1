#Ejercicio 6
#Creamos las variables de los minutos totales, el tramo, y los tramos 
total_minutos = 0
tramo = 0
tramos = 1
#Imprimimos este mensaje
print("Hola Alba! Introduce el tiempo de los tramos en minutos. Indica -1 para finalizar.")
#Mientras tramo no sea -1 hara el bucle
while tramo != -1:
    #Pedimos los minutos del tramo
    tramo = int(input(f"Tramo {tramos}: "))
    #Si tramo es menor o igual que 0 y no es igual a -1 mostrara un error
    if tramo <= 0 and tramo != -1:
            print("El tramo no puede durar 0 o numeros negativos")
    #Si tramo es diferente a -1, le sumamos 1 a tramos y a total_minutos sumamos tramo
    elif tramo != -1:
        tramos += 1
        total_minutos+=tramo
#Ahora creamos las variables horas y minutos
#horas se lleva la division de total minutos entre 60 (valor exacto)
horas=total_minutos//60
#minutos se lleva el residuo de total minutos entre 60
minutos=total_minutos%60
#Mostramos el tiempo total caminado y el total de tramos que ha hecho
print(f"Tiempo total caminado: {horas} horas {minutos} minutos\nTotal de tramos: {tramos-1}")