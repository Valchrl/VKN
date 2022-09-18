a = int(input("Введіть тризначне число "))
firstNum = a%10
a = int(a/10)
secondNum = a%10
a = int(a/10)
thirdNum = a%10
print(firstNum * 100 + secondNum * 10 + thirdNum)
