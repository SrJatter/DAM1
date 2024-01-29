#Ejercicio 9
#Pedimos al usuario que introduzca el numero de juegos ganado por el jugador A y el B
a = int(input("Juegos ganados por A (0-8): "))
b = int(input("Juegos ganados por B (0-8): "))
#Este if comprueba si el numero esta en el rango (0-8), si no se cumple la condicion el programa finaliza mostrando un mensaje
if 0 <= a <= 8 and 0 <= b <= 8:
    #Ahora con una estructura condicional comprobamos los diferentes resultados segun lo que el ususario introduzca
    #Si a es mas grande que 6 y b es mas pequeño que a - 2, o lo mismo cambiando a por b y b por a, o a o b es igual a 8, o tanto a como b son 7; El resultado sera invalido
    if a > 6 and b < a -2 or b > 6 and a < b -2 or a == 8 or b == 8 or a == 7 and b == 7:
        print("Resultado invalido")
    #Si a es mayor o igual que 6 y b es mas pequeño o igual que a - 2, o a es igual a 7; Gana A
    elif a >= 6 and b <= a-2 or a == 7:
        print("Gana A")
    #Si b es mayor o igual que 6 y a es mas pequeño o igual que b - 2, o b es igual a 7; Gana B
    elif b >= 6 and a <= b-2 or b == 7:
        print("Gana B")
    #Si ninguna de estas condiciones se cumple; Aun no ha acabado
    else:
        print("Aun no ha acabado")
else:
    print("Numero/s introducido/s fuera de rango")