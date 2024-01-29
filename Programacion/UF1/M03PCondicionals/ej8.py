#Ejercicio 8
#Pedimos al usuario la longitud de cada lado de un triangulo y guardamos la informacion en las variables a, b y c
a = float(input("Intoduce el la longitud de un lado del triangulo: "))
b = float(input("Intoduce el la longitud de otro lado del triangulo: "))
c = float(input("Intoduce el la longitud de otro lado del triangulo: "))
if a > 0 and b > 0 and c > 0:
    #Ahora con esta estructura de condicionales comprobaremos que tipo de triangulo es
    #Si cualquiera de los lados es mas grande que la suma de los otros dos, es invalido
    if a + b < c or a + c < b or b + c < a:
        print("No es un triangulo valido")
    #Si todos los lados son iguales, es equilatero
    elif a == b == c:
        print("El triangulo es equilatero")
    #Si todos los lados son diferentes, es escaleno
    elif a != b != c != a:
        print("El triangulo es escaleno")
    #Si no se cumple ninguna de las anteriores, es isosceles
    #Se podria poner otro elif para comprobar si hay dos lados iguales y uno diferente, pero en este caso no es necesario
    else:
        print("El triangulo es isosceles")
else:
    print("Numeros introducidos invalidos")