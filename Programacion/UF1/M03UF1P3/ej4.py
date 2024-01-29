#Pedimos el nr de casos
casos = int(input("Nr de casos: "))
#Mientras casos sea negativo, mostrara un error y volvera a pedir el nr de casos
while casos < 0:
    print("Los casos no pueden ser negativos")
    casos = int(input("Nr de casos: "))
#Hacemos un for que se repetira el nr de casos que se ha introducido
for i in range(casos):
    #Creamos la variable frase como lista
    frase = input().split()
    #Creamos la frasep que sera la frase que aparezca con puntos
    frasep = ""
    #Pasamos por cada nr de posicion de la lista frase
    for p in range(len(frase)):
        #Añadimos el contenido de la posicion p de frase a frasep
        frasep += frase[p]
        #Si p es diferente a la longitud de frase -1 "Este if es para que a la ultima palabra no le añada los puntos"
        if p != len(frase)-1:
            #Si la longitude de la palabra de la posicion "p" de frase es menor a la palabra siguiente: se añade "... ", si no: se añade " "
            if len(frase[p]) < len(frase[p+1]):
                frasep += "... "
            else:
                frasep += " "
    #Mostramos la frase con los puntos, si es que tiene
    print(frasep)