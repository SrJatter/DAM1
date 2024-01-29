err = 1
while err == 1:
    try:
        num = int(input("Pon un numero: "))
        err = 0
    except ValueError:
        print("¡Por favor, no introduzca otros caracteres no númericos o números con decimales!")
print("El numero anterior a", num, "es:", num - 1)
print("El numero posterior a", num, "es:", num + 1)