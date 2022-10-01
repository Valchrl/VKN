import math
a=float(input('Введіть координати точки А (вісь ОХ): ')) 
b=float(input('Координати точки А (вісь ОУ): '))
c=float(input('Координати точки В (вісь ОХ): ')) 
d=float(input('Координати точки В(вісь ОУ): '))
e=float(input('Введіть координати точки С (вісь ОХ): '))
f=float(input('Введіть координати точки С (вісь ОУ): '))


if a+b>c+d and a+b>e+f:
    print('Точка А більша')
    
elif c+d>a+b and c+d>e+f:
    print('Точка В більша')
    
elif e+f>a+b and e+f>c+d:
    print('Точка С більша')
