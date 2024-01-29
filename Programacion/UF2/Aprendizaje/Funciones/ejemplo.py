def hello(name = "Default", age = 25):
    print('Hello World!', name)
    if age > 50:
        print('You are yong and funny')
    else:
        print('You are a baby')

def suma(num1, num2):
    return num1 + num2

hello()
hello('Alice', 28)
hello(age=54, name='Pepe')
x = suma(8, 2)
print(x)