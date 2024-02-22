#Funciones de validacion

#Esta funcion omprueba si la longitud de los argumentos es igual a n
#Recibe una lista de argumentos y un número
#Devuelve True si se cumple la condicion, si no, imprimirá un mensaje de error
def checkLenCommand(args, n):
    if len(args) == n:
        return True
    print("Error: Numero d'arguments incorrecte")

#Esta funcion verifica si lo que recibe es un entero mayor a 0
#Recibe un str
#Devuelve el numero convertido a entero si se cumple la condicion, si no, devuelve None
def intChecker(num):
    if num.isdigit() and int(num) > 0:
            return int(num)
    return None

#Esta función verifica si lo que recibe es un entero o float mayor a 0
#Recibe un str
#Devuelve el numero convertido a float si se cumple la condicion, si no, devuelve None 
def floatChecker(num):
    nums = num.split(".")
    if ((nums[0].isdigit() and len(nums) == 1) or (len(nums) == 2 and nums[1].isdigit())) and float(num) > 0:
            return float(num)
    return None

#Esta funcion verifica si lo que recibe es un DNI valido
#Recibe un str
#Devuelve el dni si es valido, si no, devuelve False
def dniChecker(dni):
    letra = dni[-1].upper()
    if len(dni) != 9 or (not dni[:-1].isdigit() or not letra.isalpha()):
        return False
    letrasValidas = "TRWAGMYFPDXBNJZSQVHLCKE"
    controlLetra = int(dni[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        return False
    return dni

#Esta funcion verifica si lo que recibe es un telefono valido
#Recibe un str
#Devuelve el telefono si es valido, si no, devuelve False
def telChecker(tel):
    if tel.isdigit() and len(tel) == 9:
        return tel
    else:
        return False