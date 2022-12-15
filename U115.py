import csv
with open("Books.csv", "r") as f:
    reader = csv.reader(f)
    a = 0
    for row in f:
        res = str(a) + " " + row
        print(res)
        a = a + 1
