l = []
l.append(int(input()))
l.extend([2.3, 6, 2])
l.insert(0,1)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l)
print(l[-1])
print(l[2:4])
if 3 in l:
    print("El 3 esta en la lista")
else:
    print("El 3 no esta en la lista")
print(min(l))
print(max(l))

nombres = ["Pepe", "Maria"]
for nombre in nombres:
    for letra in nombre:
        print(letra*2)