err = 1
while err == 1:
    nr = int(input("Introduce un numero mas grande que 0: "))
    if nr <= 0:
        print("Un numero mas GRANDE que 0")
    else:
        err = 0
print("Los divisores de", nr, "son:")
for i in range(1, nr + 1):
    if nr % i == 0:
        print(i)
