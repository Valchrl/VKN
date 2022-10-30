import csv
div_csv = []
f = "div.csv"
fl = open(f, "w")
w = int(input('Введіть число: '))

for i in range(w, 0, -1):
    if (w % i == 0):
        div_csv.append([i])
        print(i, end=' ')
print('->', f)

header = 'Дільники числа {num}:'.format(num=w)
with open("div.csv", "w", encoding='utf-8') as outfile:
    csv_writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
    csv_writer.writerow([header])
    csv_writer.writerows(div_csv)

