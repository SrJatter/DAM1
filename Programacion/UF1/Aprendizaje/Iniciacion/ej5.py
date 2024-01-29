print("Cálculo de la media de 4 notas entre el 0 i 10")
i = 1
sum = 0
while i <= 4:
    err = 1
    while err == 1:
        try:
            n = float(input(f"Nota {i}: "))
            err = 0
        except ValueError:
            print("¡Por favor, introduce un NÚMERO del 0 al 10")
    if n < 0 or n > 10:
        print("¡Por favor, introduce un número del 0 al 10")
    else:
        sum += n
        i += 1
m = sum / 4
print("La media de tus notas es:", m)