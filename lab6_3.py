import math
spisok1=[1]
x=float(input('Введіть а: '))
y=float(input('Введіть b: '))
h=float(input('Введіть h: '))
for i in range(10):     
    y= x ** (1. / 3.) + math.sin(x)   
    spisok1=(-y + math.sqrt(h)) / (2 * x)
    print("%i x=%.1f     y=%.3f"%(i,x,y)) 
    x=x+h
    print(spisok1)
    
spisok2=[2]
x=float(input('Введіть а: '))
y=float(input('Введіть b: '))
h=0.5
while x<10:     
    y= x ** (1. / 3.) + math.sin(x)  
    spisok2=(-y + math.sqrt(h)) / (2 * x)

    print("x=%.1f y=%.3f"%(x,y))
    x=x+1
    print(spisok2)
     
