def validar(string):
    arr = string.find("@")
    dot = string.find(".")
    if string[0] != "@" and string[-1] != "@" and "@" in string and "." in string and arr < dot and string[-1] != ".":
        return True
mail = validar("yvin@uin.dw")
if mail == True:
    print("OK")
else:
    print("NO")