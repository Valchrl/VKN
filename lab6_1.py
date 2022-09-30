import math
#for i in range(m,n,h)
x=float(input('Введіть а: '))
y=float(input('Введіть b: '))
h=float(input('Введіть h: '))
for i in range(10):     
    y= x ** (1. / 3.) + math.sin(x)   
    print("%i x=%.1f\ty=%.3f"%(i,x,y)) 
    x=x+h
  
