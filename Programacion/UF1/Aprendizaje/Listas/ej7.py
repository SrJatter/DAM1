meses = [["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril", 30], ["Mayo", 31], ["Junio", 30], ["Julio", 31], ["Agosto", 31], ["Septiembre", 30], ["Octubre", 31], ["Noviembre", 30], ["Diciembre", 31]]
user = int(input("Introduce un numero de mes [1-12]: "))
while 0 >= user or user > 12:
    print("Fuera de rango, porfavor vuelve a intentarlo")
    user = int(input("Introduce un numero de mes [1-12]: "))
dias = meses[user-1][1]
mes = meses[user-1][0]
print(f"{mes} tiene {dias} dias")