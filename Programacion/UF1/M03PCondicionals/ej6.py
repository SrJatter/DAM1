#Ejercicio 6
#Creamos 3 variables para las horas de la UF, las faltas justificadas y las no justificadas
horas = int(input("Introduce las horas de la UF: "))
justificadas = int(input("Introduce las faltas justificadas: "))
nojustificadas = int(input("Introduce las faltas no justificadas: "))
#Este if comprueba si las faltas no justificadas superan el 10% de horas de la UF
#Si se cumple devuelve NO
if nojustificadas >= horas * 0.1:
    print("NO")
#Este elif comprueba si las faltas justificadas y no justificadas superan el 20% de horas de la UF
#Si se cumple devuelve NO
elif justificadas + nojustificadas >= horas * 0.2:
    print("NO")
#Si no se cumple ninguna de las condiciones devuelve SI
else:
    print("SI")
