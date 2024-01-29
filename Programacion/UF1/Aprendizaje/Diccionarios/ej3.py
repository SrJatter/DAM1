producto = input("Introduce el articulo a comprar y su precio o exit para salir:\n")
diccionario = {}
while producto != "exit":
    producto = producto.split()
    if producto[0] in diccionario:
        print("El producto ya esta añadido")
    else:
        diccionario[producto[0]] = producto[1]
    producto = input("Introduce el articulo a comprar y su precio o exit para salir:\n")
print("Lista de la compra")
suma = 0
for i in diccionario:
    print(f"{i}: {diccionario[i]}")
    suma += float(diccionario[i])
print("Total:", suma)