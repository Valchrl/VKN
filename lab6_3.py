import math

x=float(input('Введіть х: '))
y=float(input('Введіть у: '))
h=0.3
spisok=[]
while x <= y:
    y=math.pow((x) ,1/3) + math.fabs(math.sin(x))
spisok.append(y)
x=x+h
print(spisok)
