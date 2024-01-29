gcharhp = {}
gcharhp["Kazuha"] = 21000
gcharhp["Yelan"] = 42000
gcharhp["Hu Tao"] = 40000
gcharhp["Furina"] = 55000
print(gcharhp)
name = input("De quien quieres saber la vida max.? ")
if name in gcharhp:
    print(gcharhp[name])
else:
    print("No tengo ese personaje")
for gc in gcharhp:
    print(gc, end="\t")
print()
for gc in gcharhp.values():
    print(gc, end="\t")
print()

gchar = {}
gchar["Kazuha"] = {"hp": 21000, "atk": 1800, "EM": 800}
gchar["Yelan"] = {"hp": 42000, "atk": 1400, "EM": 180}
gchar["Hu Tao"] = {"hp": 40000, "atk": 1200, "EM": 200}
gchar["Furina"] = {"hp": 55000, "atk": 1100, "EM": 50}
print(gchar["Hu Tao"])