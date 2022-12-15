lst = []
new_lst = []

with open("Names.txt", "r") as f:
    lst = f.read().split("\n")
    print(" ".join(lst))

name = input("Введите имя: ")

for row in lst:
    if name == row:
        continue
    new_lst.append(row)

file = open("Names2.txt", "w")
str = "\n".join(new_lst)
file.write(str)
file.close()