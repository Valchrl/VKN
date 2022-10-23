import json as js
    
islands ={
    "Острів Диявола" : "140000 кв.км",
    "Острів Сомерсет" : "24786 кв.км",
    "Острів Городище" : "21690000 кв.км",
    "Острів Карспатос" : "324100000 кв.км",
    "Острів Капрі" : "10400000 кв.км",
    "Острів Орчіла" : "43000000 кв.км",
    "Острів Принца Уельського" : "6675 кв.км",
    "Острів Врангеля" : "7866 кв.км",
    "Острів Рузвельта" : "7500 кв.км",
    "Північний острів (Нова Зеландія)" : "111583 кв.км",
    "Острів Девон" : "55247 кв.км",
    "Острів Короля Вільяма" : "13111 кв.км"
}
    
with open("islands.txt", "w") as outfile:
    js.dump(islands, outfile)

with open('islands.txt') as f:
    data = f.read()
      
dict_from_file = js.loads(data)

while True:
    a = input('Добавити запис в словник так/ні?: ')
    if a.lower().startswith('ні'):
        break
    
    island_name = input('Введіть назву острова:')
    island_area = input('Введіть площу:')
    islands[island_name] = island_area

print(islands)

    


    


