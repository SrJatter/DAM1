def error_control(w):
    err = 1
    while err == 1:
        try:
            v = float(input(w))
            err = 0
        except ValueError:
            print("¡Por favor, no introduzcas otros caracteres no númericos!")
    return v
dinero = error_control("Introduce la cantidad de dinero que tienes: ")
precio = error_control("Introduce el precio de la pieza de ropa: ")
descuento = precio - precio * 0.25
print("Tras aplicar un descuento del 25% la pieza de ropa queda en:", descuento)
print("Despues de hacer la compra te quedaran:", dinero - descuento)