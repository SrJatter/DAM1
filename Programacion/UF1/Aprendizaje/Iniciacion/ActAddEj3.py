def error_control(w):
    err = 1
    while err == 1:
        try:
            v = int(input(w))
            err = 0
        except ValueError:
            print("¡Por favor, no introduzcas otros caracteres no númericos o numeros con decimales!")
    return v
cent = error_control("Pon un numero de centimos entre 0-900: ")
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
m7 = 0
m8 = 0
while cent != 0:
    if cent >= 200:
        m8 += 1
        cent -= 200
    else:
        if cent >= 100:
            m7 +=1
            cent -= 100
        else:
            if cent >= 50:
                m6 +=1
                cent -= 50
            else:
                if cent >= 20:
                    m5 +=1
                    cent -= 20
                else:
                    if cent >= 10:
                        m4 +=1
                        cent -= 10
                    else:
                        if cent >= 5:
                            m3 +=1
                            cent -= 5
                        else:
                            if cent >= 2:
                                m2 +=1
                                cent -= 2
                            else:
                                if cent >= 1:
                                    m1 +=1
                                    cent -= 1
print(f"{m8}\n{m7}\n{m6}\n{m5}\n{m4}\n{m3}\n{m2}\n{m1}")