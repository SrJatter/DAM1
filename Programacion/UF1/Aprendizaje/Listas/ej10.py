import random
m=[]
for c in range(5):
    l=[]
    for f in range(5):
        l.append(random.randint(1,5))
    m.extend([l])
for i in m:
    suma = 0
    for x in i:
        print(x, end = "\t")
        suma += x
    print("=\t", suma, end="\n")
for i in range(5):
    print("=", end="\t")
print(end = "\n")
for i in range(5):
    suma = 0
    for n in range(5):
        suma += m[n][i]
    print(suma, end ="\t")