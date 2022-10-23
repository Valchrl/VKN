from array import array
import re
cmd_nf_str = 'Команда не знайдена'
pop_temp = '\t{key}: {val} чол.'
pop_str = 'Населення:'
area_str = 'Площа:'
notfound_str = '\tне знайдено'
area_temp = '\t{key}: {val} кв.км'
population = {'Україна': '40 000 000', 'Польша':'30 000 000'}
areas = {'Україна':'603 700', 'Венгрія':'20 000 000'}

def add_to_dict(params:list):
    p = re.split('\' | \'', ' '.join(params[1:]))
    if len(p) > 1:
         for i in range(len(p)):
            p[i] = p[i].strip('\'')
    else:
        p = p[0].split(' ')
    if params[0] == '-a':
        areas[p[0]] = p[1] 
        print(area_str)
        show_dict(areas, area_temp)
    elif params[0] == '-p':
        population[p[0]] = p[1]
        print(pop_str)
        show_dict(population, pop_temp)

def show_dict(dict:dict, str_temp:str, search:str = None):
    counter = 0
    if search != None:
        for kv in dict.items():
            if search in kv[0]:
                print(str_temp.format(key=kv[0], val=kv[1]))
                counter += 1
    else:
        for kv in dict.items():
            print(str_temp.format(key=kv[0], val=kv[1]))
            counter +=1
    if counter == 0:
        print(notfound_str)

def show(params:list):
    if len(params) != 0:
        if params[0] == '-all':
            if(len(params) >= 2):
                print(pop_str)
                show_dict(population, pop_temp, params[1])
                print(area_str)
                show_dict(areas, area_temp, params[1])
            else:
                print(pop_str)
                show_dict(population, pop_temp)
                print(area_str)
                show_dict(areas, area_temp)
                
        elif params[0] == '-p':
            if(len(params) >= 2):
                print(pop_str)
                show_dict(population, pop_temp, params[1])
            else:
                print(pop_str)
                show_dict(population, area_temp)
        elif params[0] == '-a':
            if(len(params) >= 2):
                print(area_str)
                show_dict(areas, area_temp, params[1])
            else:
                print(area_str)
                show_dict(areas, area_temp)
             

exec_command = {'add': add_to_dict, 'show': show}

while(True):
    print('Введіть команду або help для справки')
    cmd = input()
    if cmd.startswith('exit'):
        break
    if cmd == 'help':
        print(cmd)
    else:
      cmds = cmd.split(' ')
      f_cmd = cmds[0]
      exec_cmd = exec_command.get(f_cmd)
      exec_cmd(cmds[1:])