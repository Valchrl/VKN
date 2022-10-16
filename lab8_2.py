import numpy as np 
import math
a = input('Введіть а: ')
arr1 = np.array(list(map(int, a.split(' '))))

b = input('Введіть b: ')
arr2 = np.array(list(map(int, b.split(' '))))

c = input('Введіть c: ')
arr3 = np.array(list(map(int, c.split(' '))))

y = np.array([arr1,arr2,arr3])
print(y)
sum = 0
mess = 'i + j % 2 != 0: '
for i in range(len(y)):
    for j in range(len(y[i])):
        if (i+j)%2 != 0:
            mess += str(y[i][j]) + ' '
            sum += y[i][j]
print(mess)
    
print('Сума чисел з непарною сумою індексів: ', sum)
print('---------------------------')
#print(y, sep=',', end=' ')

    

