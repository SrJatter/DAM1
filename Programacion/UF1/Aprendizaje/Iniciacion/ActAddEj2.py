err = 1
while err == 1:
    try:
        invitados = int(input("Introduce el numero de invitados: "))
        err = 0
    except ValueError:
        print("¡Por favor, no introduzcas caracteres no numericos o numeros con decimales!")
def a_comprar(personas, producto, consumo):
    v = personas * consumo / producto
    if v - int(v) > 0:
        v += 1
    return int(v)
def sobrante(personas, producto, consumo, compra):
    v = compra * producto - personas * consumo
    return int(v)
cola = 6
pan = 20
nutella = 15
ncola = a_comprar(invitados, cola, 1)
npan = a_comprar(invitados, pan, 4)
nnutella = a_comprar(invitados, nutella, 2)
rcola = sobrante(invitados, cola, 1, ncola)
rpan = sobrante(invitados, pan, 4, npan)
print("Lista de la compra:")
print(ncola, "packs de coca cola")
print(npan, "paquetes de pan")
print(nnutella, "botes de nutella")
print("Sobran:")
print(rcola, "latas de coca cola")
print(rpan, "rebanadas de pan")