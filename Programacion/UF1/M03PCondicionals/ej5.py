#Ejercicio 5
#piedra-papel-tijera(ppt)
#Creamos esta variable ppt1 y pedimos al usuario que introduzca una de las opciones
ppt1 = input("Pon una de estas opciones (piedra, papel, tijera): ")
#Este if comprueba si el usuario ha introducido una de las opciones
#Si se cumple creamos la variable ppt2 y pedimos al usuario que introduzca una de las opciones...
#Si no se cumple finalizaremos el programa mostrando el error
if ppt1 == "piedra" or ppt1 == "papel" or ppt1 == "tijera":
    ppt2 = input("Vuelve a poner una de estas opciones (piedra, papel, tijera): ")
    #Este if comprueba si el usuario ha introducido una de las opciones, igual que el otro if
    #Si se cumple, mediante una estructura if-elif-else comprobaremos si ha habido un empate o cual de los jugadores ha ganado
    #Si no se cumple finalizaremos el programa mostrando el error
    if ppt2 == "piedra" or ppt2 == "papel" or ppt2 == "tijera":
        if ppt1 == ppt2:
            print("Empate")
        elif ppt1 == "piedra" and ppt2 == "tijera":
            print("Gana el primer jugador")
        elif ppt1 == "tijera" and ppt2 == "piedra":
            print("Gana el segundo jugador")
        elif ppt1 == "piedra" and ppt2 == "papel":
            print("Gana el segundo jugador")
        elif ppt1 == "papel" and ppt2 == "piedra":
            print("Gana el primer jugador")
        elif ppt1 == "tijera" and ppt2 == "papel":
            print("Gana el primer jugador")
        elif ppt1 == "papel" and ppt2 == "tijera":
            print("Gana el segundo jugador")
    else:
        print("No has introducido lo que te he pedido")
else:
    print("No has introducido lo que te he pedido")