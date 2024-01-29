err = 1
while err == 1:
    try:
        presupuesto = float(input("Presupuesto del mes: "))
        err = 0
    except ValueError:
        print("¡Por favor, no introduzca otros caracteres no númericos!")
comida = presupuesto * 0.15
juegos = presupuesto * 0.6
material_otaku = presupuesto * 0.25
print("Has gastado:", comida, "en comida")
print("Has gastado:", juegos, "en juegos")
print("Has gastado:", material_otaku, "en material otaku")
