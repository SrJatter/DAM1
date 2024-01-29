l = [0]
while l[-1] > -1:
    l.append(int(input()))
print("los numeros introducidos son:")
for i in range(1,len(l)):
    print(l[i], end = " ")