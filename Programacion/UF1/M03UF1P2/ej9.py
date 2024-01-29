#Ejercicio 9
#creamos una variable para letra
letra=input()
#creamos variables para inicial y final con un valor fuera del rango:
inicial=-1
final=-1
#creamos el bucle while para que mientras sea diferente a D se realice.
while letra!="D":
    #si letra es igual a A, B o C:
    if letra=="A" or letra=="B" or letra=="C":
        #si letra es igual a A, pedirá el numero inicial.
        if letra=="A":
            inicial=int(input("Introduce un numero inicial entre el 0 y el 10: "))
            #si no está dentro del rango, volverá a pedir el numero inicial.
            while 0 > inicial or inicial > 10:
                inicial=int(input())
        #si letra es igual a B pedirá el numero final.
        elif letra=="B":
            final=int(input("Introduce un numero final entrel el 0 y el 10: "))
            #si no está dentro del rango, volverá apedir el numero final. 
            while 0 > final or final > 10:
                final=int(input("Introduce un numero final entrel el 0 y el 10: "))
        #si letra es igual a C, imprimirá el rango entre inicial a final.
        elif letra=="C":
            #si inicial es mayor a final o si en final no se ha colocado numero o en inicial tampoco, imprimirá error.
            if inicial>final or final==-1 or inicial==-1:
                print("ERROR")
            else: 
            #en caso de que todo esté correcto, imprimirá el rango de inicial a final.
                for i in range(inicial,final+1):
                    #se imprime i que es el 
                    print(i)
    letra=input()
print("BYE")