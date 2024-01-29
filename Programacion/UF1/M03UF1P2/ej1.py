#Ejercicio 1
#pedimos un numero entre el 2 y 20
num = int(input("Introduce un numero entre el 2 y el 20: "))
#Si el numero introducido por el usuario esta en el rango hara lo siguiente
if 1 < num < 21:
    #Este for mostrara una sucesion de numeros del 1 al numero introducido
    for i in range(1,num+1):
        print(i)
#Si la condicion no se cumple mostrara este mensaje de error
else:
    print("El numero que has introducido esta fuera del rango (2-20)")
