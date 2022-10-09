import random     #999-ccc-nnn-nn-nn
a = int(input('Введіть кількість: '))
for i in range(a):
    s1 =random.randint(100, 999)
    s2 = random.randint(100, 999)
    s3 = random.randint(10, 99)
    s4 = random.randint(10, 99)
    first = str(s1)
    second = str(s2)
    third = str(s3)
    fourth = str(s4)
print('+999', s1, s2, s3, s4, sep='-')



    