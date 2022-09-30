import math
x=float(input('Введіть а: '))
y=float(input('Введіть b: '))
h=0.5
while x<10:     
    y= x ** (1. / 3.) + math.sin(x)   
    print("x=%.1f y=%.3f"%(x,y))
    x=x+1
    
    