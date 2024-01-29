#Sentencias alternativas
#2
#and: 11=1 10=0 01=0 00=0 or: 11=1 10=1 01=1 00=0 nor: 1=0 0=1
#Comparaciones de valores, == igual, != diferente, > mayor que, < menor que, >= menor o igual que, <= mayor o igual que
num =int(input("Introduce un numero entre 10 y 20 no incluidos: "))
if num > 10 and num < 20: #if 10 < num < 20:
    print("Me has hecho caso")
elif num <= 10:
    print ("Has puesto un numero menor o igual que 10")
else:
    print("Has puesto un numero mayor o igual que 20")