productos = {"Refresco": "1,25 €", "Aperitivo": "0,90 €", "Pastelito": "1,05 €", "Galletas": "1,35 €", "Zumo": "0,95€"}
print("¿De que producto quieres ver el precio?\n[Refresco, Aperitivo, Pastelito, Galletas, Zumo] o introduce Salir")
cual = input()
while cual != "Salir":
    if cual in productos:
        print(productos[cual])
    else:
        print("El producto no esta en el diccionario")
    print("¿De que producto quieres ver el precio?\n[Refresco, Aperitivo, Pastelito, Galletas, Zumo] o introduce Salir")
    cual = input()