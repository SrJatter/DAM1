print("Calculo del perimetro y area de un rectangulo")
def error_control(w):
    err = 1
    while err == 1:
        try:
            v = float(input(w))
            err = 0
            if v == int(v):
                v = int(v)
        except ValueError:
            print("¡Por favor, no introduzca otros caracteres no númericos!")
    return v
b = error_control("Pon la base: ")
a = error_control("Pon la altura: ")
perimetro = 2 * (a + b)
area = a * b
print("El perimetro és:", perimetro)
print("El area es:", area)