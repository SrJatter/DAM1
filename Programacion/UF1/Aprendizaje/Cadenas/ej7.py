fin = True
num = input("Introduce un numero entero positivo: ")
while fin == True:
    ok = 0
    if num == "0":
        ok -= 1
    for i in num:
        if i in "1234567890":
            ok += 1
        else:
            ok -= 1
    if len(num) == ok and ok != 0:
        print("Perfecto!")
        fin = False
    else:
        print("Lee lo que te pido")
        num = input("Introduce un numero entero positivo: ")