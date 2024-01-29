def usr(nom, cognom, dni):
    result = nom.replace(" ", "") + str(len(cognom)) + dni[:3]
    return result

nom = input("Nom: ")
cog = input("Cognom: ")
dni = input("DNI: ")
print("Usuari:", usr(nom, cog, dni))