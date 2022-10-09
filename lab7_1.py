from ast import List
import random
from secrets import choice
s1=input('Введіть рядок: ')
lst = s1.split(' ')
tLst = filter(lambda item: item.istitle(), lst)
print(' '.join(tLst))
lst = random.sample(lst, len(lst))
print(' '.join(lst))




