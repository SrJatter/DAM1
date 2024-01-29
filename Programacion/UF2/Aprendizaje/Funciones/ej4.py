def Convertir_A_Segons(h, m, s):
    s = s + m * 60 + h * 60 * 60
    return s
segundos = Convertir_A_Segons(3, 26, 59)
print(segundos)