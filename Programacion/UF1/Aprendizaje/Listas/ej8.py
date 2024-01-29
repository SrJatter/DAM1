lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    lista1.append(int(input("Valor para la lista 1: ")))
    lista2.append(int(input("valor para la lista 2: ")))
    lista3.append(lista1[i] + lista2[i])
print("lista 1:", lista1)
print("lista 2:",lista2)
print("lista 3:",lista3)