def error_control(w):
    err = 1
    while err == 1:
        try:
            v = int(input(w))
            err = 0
        except ValueError:
            print("¡Por favor, no introduzcas otros caracteres no númericos o numeros con decimales!")
    return v
i = 1
aire = []
while i <= 4:
    aire += [str(error_control(f"Introduce el angulo del aire {i}: "))]
    i+=1
for angulo in aire:
    if int(angulo) % 180 == 0:
        print("OK")
    else:
        print("BRONCA")