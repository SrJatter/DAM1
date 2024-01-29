import random
nr = random.randint(1, 50)
i = 0
win = 0
print("Adivina el numero del 1 al 50, tienes 5 oportunidades")
while i < 5:
    user = int(input(f"Oportunidad {i+1}, introduce el numero: "))
    if user < 1  or user > 50:
        print("Has perdido una oportunidad, el numero tiene que ser entre el 1 y el 50")
        i += 1
    else:
        if user == nr:
            print("¡Felicidades, lo has adivinado!")
            i = 5
            win = 1
        elif user < nr:
            print("Muy pequeño")
            i += 1
        elif user > nr:
            print("Muy grande")
            i += 1
if win == 0:
    print(f"Has perdido, era el {nr}")
#Pequeña broma
    import time
    factor_retraso = 1.0
    while True:
        try:
            print("Haber estudiado")
            time.sleep(factor_retraso)
            factor_retraso -= 0.05
            if factor_retraso <= 0:
                for i in range(6):
                    factor_retraso = 0.04
                    time.sleep(factor_retraso)
                    print("Haber estudiado")
                for i in range(12):
                    factor_retraso = 0.03
                    time.sleep(factor_retraso)
                    print("Haber estudiado")
                for i in range(25):
                    factor_retraso = 0.02
                    time.sleep(factor_retraso)
                    print("Haber estudiado")
                for i in range(50):
                    factor_retraso = 0.01
                    time.sleep(factor_retraso)
                    print("Haber estudiado")
                for i in range(100):
                    factor_retraso = 0
                    time.sleep(factor_retraso)
                    print("Haber estudiado")
                factor_retraso = -1
        except ValueError:
            print ("FatalError: Game has crashed, cause(You loose the game)")
            break
