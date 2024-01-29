def error_control(w, r1, r2):
    err = 1
    while err == 1:
        try:
            v = int(input(f"Introduce {w} (entre {r1}-{r2}): "))
            if v < r1 or v > r2:
                print(f"¡Por favor, introduce un número ENTRE {r1} Y {r2}!")
            else:
                err = 0
        except ValueError:
            print("¡Por favor, no introduzcas otros caracteres no númericos o numeros con decimales!")
    return v
h = error_control("una hora", 0, 23)
m = error_control("un minuto", 0, 59)
s = error_control("un segundo", 0, 59)
s_total = h * 60 * 60 + m * 60 + s
print(f"La hora introducida es {h} : {m} : {s} que corresponde a {s_total} segundos")