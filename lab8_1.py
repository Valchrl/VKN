from array import *
from email.policy import strict
import random as rd
#Виводе масив як строку, Title - назва, arr - масив
def show_array(title, arr):
    print(title, end=' ')
    for i in arr:
        print(i, end=' ')
    print()
    
#Генерує масив цілих чисел, count - кількість згенерованих чисел, 
# from_num - з числа, to_num - по число
def generate_array(count, from_num, to_num):
    new_arr = array('i')
    for i in range(count):
        new_arr.append(rd.randint(from_num, to_num))
    return new_arr
    
a  = generate_array(10, 0, 15)
print('------Лабораторна робота 8 зав.1-----------')
show_array('Початковий масив:', a)
a = sorted(a)
print('-------------------------------------------')
show_array('Відсортований масив:', a)
print('-------------------------------------------')
a = a[5:10] + a[:5]
show_array('Масив "друга половина/перша половина":', a)
print('-------------------------------------------')

