import estudi1
import estudi2
import estudi3
import sys

if len(sys.argv) == 2:
    option = sys.argv[1]
else:
    print("1. Precipitación anual en Gavà")
    print("2. Comparacion de precipitacion mensual en Gavà")
    print("3. Comparacion de temperaturas maximas y minimas de Gavá")
    option = input("Opción: ")

if option == "1":
    estudi1.show()
elif option == "2":
    estudi2.show()
elif option == "3":
    estudi3.show()
else:
    print("Opción incorrecta")
    print("Saliendo del programa...")