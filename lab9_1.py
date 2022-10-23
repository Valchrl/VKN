from re import T
import random as rd

T = ('black','white','orange','pink','green','blue','yellow','red','brown')
K = ('banana','watermelon','apple','pear','tangerine','peach')
n =int(input('Введіть кількість словосполучень N: '))

x = 0
while x<n:
    i = rd.randint(0, len(T)-1)
    w1 = T[i]
    i = rd.randint(0, len(K)-1)
    w2 = K[i]
    print('%s %s'%(w1, w2))
    x+=1
print('-----------------------------')
print('Згенеровано %i словосполучень'%(x))
    
    