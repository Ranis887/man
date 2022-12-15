import csv

a = int(input("Введите начальный год: "))
b = int(input("Введите конечный год: "))
lst = []
with open("Books.csv", "r") as f:
    reader = csv.reader(f)
    for pow in f:
        for n in range(a, b):
            if str(n) in str(pow):
                print(pow)
