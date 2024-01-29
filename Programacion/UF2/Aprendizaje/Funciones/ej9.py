def isNIF(nif):
    digits = 0
    letra = 0
    for i in nif:
        if i in "1234567890":
            digits += 1
        elif i in "TRWAGMYFPDXBNJZSQVHLCKE":
            letra += 1
    if digits == 8 and letra == 1:
        return True
    else:
        return False
    
nif = isNIF("3162A2376")
if nif:
    print("OK")
else:
    print("NO")