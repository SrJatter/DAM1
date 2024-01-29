#Ejercicio 5
#Importamos la libreria de random
import random
#Generamos un valor aleatorio en num en el rango -10,10
num = random.randint(-10,10)
#Variable para contar numeros generados totales incluyendo el 0 como numero generado
generados = 1
#Variables para contar numeros positivos y negativos
positivo = 0
negativo = 0
#Mientras no sea 0 entra en bucle
while num != 0:
    #Si es menor a 0 se cuenta como negativo
    if num < 0:
        print(f"El numero {num} es negativo")
        negativo += 1
    #Si es mayor a 0 se cuenta como positivo
    else:
        print(f"El numero {num} es positivo")
        positivo += 1
    #Se vuelve a generar un numero aleatorio
    num = random.randint(-10,10)
    #Se añade un digito a generado
    generados += 1
#Mostramos el total de positivos, negativos y el total de generados   
print(f"Numeros positivos: {positivo}\nNumeros negativos: {negativo}\nTotal generados: {generados}")
