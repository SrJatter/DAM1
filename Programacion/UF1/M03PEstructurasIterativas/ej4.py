suma = 0
for i in range(0, 101, 3):
    suma += i
    if i == 99:
        print(i, end = "=")
    else:
        print(i, end = "+")
print(suma)