#Ejercicio 1
#Pedimos al usuario 2 numeros entre 1 y 100
num1 = int(input("Pon un numero entero entre 1 y 100: "))
num2 = int(input("Pon otro numero entero entre 1 y 100: "))
#Mostramos al usuario los 2 numeros que ha introducido
print("el primer numero introducido es:", num1)
print("el segundo numero introducido es:", num2)
#Este if comprueba si el numero esta entre 1 y 100 ambos incluidos
#Si se cumple la condicion mostraremos que esta en el rango 
#Si no se cumple la condicion mostraremos que no esta en el rango
#Esto se hace con ambos numeros
if 1 <= num1 <= 100:
    print("El primer numero esta dentro del rango")
else:
    print("El primer numero no esta en el rango")
if 1 <= num2 <= 100:
    print("El segundo numero esta dentro del rango")
else:
    print("El segundo numero no esta en el rango")
#Ejercicio 2
#Este if comprueba si el residuo de num2 dividido entre 2 es 0
#Si se cumple mostraremos que es par
if num2 % 2 == 0:
    print("El segundo numero es par")
#Ejercicio 3
#Este if comprueba si el residuo de num1 y num2 divididos entre 2 es diferentes a 0
#Si se cumple mostraremos que es impar
if num1 % 2 != 0:
    print("El primer numero es impar")
if num2 % 2 != 0:
    print("El segundo numero es impar")
