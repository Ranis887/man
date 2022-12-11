import csv

lst = []
with open("Books.csv", "r") as f:
    reader = csv.reader(f)
    a = 0
    for row in f:
        lst.append(row)
        res = str(a) + " " + row
        print(res)
        a = a + 1
d = int(input("Какую строку хотите исключить? - "))
#del lst[d]

a = 0
for x in lst:
    x = str(a) + " " + x
    print(x)
    a = a + 1
i1 = int(input("Какую строку хотите изменить? - "))
print(str(lst[i1]))
n = input("Введите название книги: ")
v = input("Введите автора: ")
g = int(input("Введите год: "))
lst[i1] = f'{n};{a};{str(g)}\n'
print(str(lst))

with open("Books.csv", "w") as f:
    writer = csv.writer(f, delimiter=";")
    for z in lst:
        writer.writerow(z) #Я не понял... Вот так вот бывает в жизни.