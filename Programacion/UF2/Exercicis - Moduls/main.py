from dades import *
from user import *
diccionari = {}
def regitrar():
    usuari = input("Introdueix el nom d'usuari: ")
    if usuari in diccionari:
        print("Usuari ja registrat")
    else:
        clau = input("Introdueix la contrasenya: ")
        if validarUsuari(usuari, clau):
            diccionari[usuari] = {}
            diccionari[usuari]["pass"] = clau
            diccionari[usuari]["age"] = demanarEdad()
            diccionari[usuari]["birth"] = demanarNaixement()
            print("Usuari registrat correctament")
        else:
            print("Usuari o contrasenya no valides, l'usuari ha de tenir 4 caracters i la contrasenya ha de tenir almenys 6 digits i una vocal ")

def iniciar():
    usuari = input("Introdueix el nom d'usuari: ")
    clau = input("Introdueix la contrasenya: ")
    inici = login(diccionari, usuari, clau)
    if inici:
        print(f"Benvingut/da {usuari}")
        print(avui())
        if aniversari(diccionari[usuari]["birth"]):
            print("Aquest mes es el teu aniversari")
        else:
            print("Aquest mes no es el teu aniversari")
        print(quantFalta(diccionari[usuari]["birth"]))
    else:
        print("Usuari o contrasenya incorrectes")

def informacio():
    usuari = input("Introdueix el nom d'usuari:")
    if usuari in diccionari:
        print(f"Dades de {usuari}")
        print(f"Edat: {diccionari[usuari]['age']}")
        print(properAniversari(diccionari[usuari]["birth"]))
    else:
        print("L'usuari no existeix")

def menu():
    opcio = ""
    while opcio != "4":
        print()
        print("1) Registrar usuari")
        print("2) Login")
        print("3) Mostrar dades d'un usuari")
        print("4) Sortir")
        opcio = input("Introdueix una opcio: ")
        if opcio == "1":
            regitrar()
            input("Prem enter per continuar")
        elif opcio == "2":
            iniciar()
            input("Prem enter per continuar")
        elif opcio == "3":
            informacio()
            input("Prem enter per continuar")
        elif opcio == "4":
            print("Adeu")
        else:
            print("Opcio incorrecta")
            input("Prem enter per continuar")

menu()