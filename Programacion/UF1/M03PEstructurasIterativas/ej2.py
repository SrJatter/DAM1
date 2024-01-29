err = 1
while err == 1:
    nr = int(input("introduce un numero entero positivo: "))
    if nr <= 0:
        print("Un numero entero POSITIVO (0 tampoco es positivo)")
    else:
        err = 0
for i in range(nr, nr * 2):
    print(i)
