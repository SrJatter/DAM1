def parells(lista):
    result = []
    for i in lista:
        if i % 2 == 0:
            result.append(i)
    return result
numeros = [-12, 84, 13, 20, -33, 101, 9]
print(parells(numeros))

def parells2(lista):
    for i in lista:
        if i % 2 != 0:
            lista.remove(i)
        
parells2(numeros)
print(numeros)