import json as js
import os
py_list = ''
whl_list = ''
zip_list = ''

for (dirpath,dirnames,filenames) in os.walk('C:\\PYTHON_PROGS'):
    
    
    print(dirpath)
    new_line = '\n'
    for n in filenames:
        s = n.split('.')
        f_name = '{name}{nl}'.format(name=n, nl=new_line)
        if s[1] == 'py':
            py_list += f_name
        elif s[1] == 'whl':
            whl_list += f_name
        elif s[1] == 'zip':
            zip_list += f_name
            
py_list = py_list.rstrip('\n')
whl_list = whl_list.rstrip('\n')
zip_list = zip_list.rstrip('\n')
print(py_list)
print(whl_list)
print(zip_list)
with open("py.txt", "w") as outfile:
    outfile.write(py_list)
with open("whl.txt", "w") as outfile:
    js.dump(whl_list, outfile)
with open("zip.txt", "w") as outfile:
    js.dump(zip_list, outfile)


    