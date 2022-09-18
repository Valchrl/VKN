import math

def func_12_1(x):
    a = (math.cos(x) + math.sin(2*x)) / math.pow(4,2*x) - math.log10(math.fabs(x+1))
    return a

result = func_12_1(float(input("Введіть число для обчислення: ")))
print(result)

    
    