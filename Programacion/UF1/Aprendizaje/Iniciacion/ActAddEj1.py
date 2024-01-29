def error_control(w):
    err = 1
    while err == 1:
        try:
            v = int(input(w))
            err = 0
        except ValueError:
            print("¡Por favor, no introduzcas caracteres no numericos o numeros con decimales!")
    return v
pies = error_control("Introduce el numero de pies que quieras: ")
pulgadas = error_control("Introfuce el numero de pulgadas que quieras: ")
pulgadas_totales = pies * 12 + pulgadas
milimetros = pulgadas_totales * 25.4
metros = milimetros // 1000
centimetros = (milimetros % 1000) / 10
if centimetros - int(centimetros) > 0.5:
    centimetros += 1
print(f"{int(metros)}m {int(centimetros)}cm")