import sys
k = float(input('k (коефіціент): '))
a = float(input('a (см): ')) * k
h = float(input('h (см): ')) * k
b = float(input('b (см): ')) * k

print('Розміри сторін подібного пряамокутного паралелепіпеда з k=' +  str(k) +':')
print('\ta = ' + str(a))
print('\tb = ' + str(b))
print('\th = ' + str(h))
print('V = ', (a * b * h))
print('S поверхні = ', 2 * (a * b + a * h + b * h))