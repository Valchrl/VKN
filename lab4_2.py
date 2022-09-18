import math

a = float(input('Введіть a: '))
b = float(input('Введіть b: '))
h = float(input('Введіть h: '))
x = float(input('Введіть x: '))
y = float(input('Введіть y: '))

res = 1/3*a*b*h*math.cos(x)+math.log10(y) 
print(res)
    

