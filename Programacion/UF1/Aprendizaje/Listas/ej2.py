import random
l =[]
for i in range(10):
    l.append(random.randint(1,10))
    print(f"Elemento {i+1}: {l[i]}\nSu quadrado: {l[i]**2}\nSu cubo: {l[i]**3}\n")