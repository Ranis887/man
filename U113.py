import csv
buk = []
a = int(input("Сколько записей вы хотите добавить? - "))
if a <= 0:
    print("Хорошо")
else:
    with open("Books.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        for x in range(0, a):
            writer = csv.writer(f, delimiter=";")
            n = input("Введите название книги: ")
            a = input("Введите автора: ")
            g = int(input("Введите год: "))
            buk.extend([n, a, str(g)])
            writer.writerow(
                buk
            )

author = input("Введите нужного вам автора: ")
with open("Books.csv", "r") as f:
    reader = csv.reader(f)
    for row in f:
        if author in str(row):
            print(row)