import random
l = []
for i in range(10):
    l.append(random.randint(-100, 100))
print(l)
l.sort(reverse=True)
print(l)