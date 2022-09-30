import math
x=float(input('Введіть число x: '))
def f1(x1):
    
    rez=math.log10(math.fabs(x1 + 1)) + 2.9*math.e**(0.1*x1)
    return(rez)
def f2(x2):
    
    rez=math.sqrt(x2) + x2*(1./3.)+ - math.sin(x2)
    return(rez)
def f3(x3):
    
    rez=4*(x3) + math.e**(x3) - 4*math.sqrt(math.fabs(x3))
    return(rez)
y=0.0
if x>1:
    y=f1(x)
elif -1.1<x<= 1:
    y=f2(x)
elif x<=-1.1:
    y=f3(x)
print(y)

