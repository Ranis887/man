import csv

buk = []
with open("Books.csv", "a", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    n = input("Введите название книги: ")
    a = input("Введите автора: ")
    g = input("Введите год: ")
    buk.extend([n, a, str(g)])
    writer.writerow(
        buk
    )
