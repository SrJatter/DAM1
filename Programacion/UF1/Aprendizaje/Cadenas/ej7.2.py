fin = True
num = input("Introduce un numero entero positivo: ")
while fin == True:
    if num.isnumeric():
        num = int(num)
        if num > 0:
            print("Perfecto")
            fin = False
        else:
            print("Lee lo que te pido ¨0 no es positivo¨")
            num = input("Introduce un numero entero positivo: ")
    else:
        print("Lee lo que te pido")
        num = input("Introduce un numero entero positivo: ")