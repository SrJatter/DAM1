suma = 0
for i in range(101):
    suma += i
    if i == 100:
        print(i, end = "=")
    else:
        print(i, end = "+")
print(suma)