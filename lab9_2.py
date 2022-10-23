a = {11,'d',12,'s','w','/','a','g',';',':',14,20,'e','t','K',34,',',87,'.','h'}
print('A:', (a))
b = ('B:')
print((b), set(i for i in a if isinstance(i, int)))
c = ('C:')
print((c), set(i for i in a if isinstance(i, str) and (97 <= ord(i) <= 119 or 65 <= ord(i) <= 90)))
e = ('E:')
print((e),set(i for i in a if isinstance(i, str) and (33 <= ord(i) <= 47 or 58 <= ord(i) <= 63)))
    
    




