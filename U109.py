print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
print("Make a selection 1, 2 or 3:")
a = int(input())
if a == 1:
    file = open("Subject.txt", "w")
    name = input("Введите название школьного предмета - ")
    file.write(name + "\n")
    file.close()
elif a == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
elif a == 3:
    file = open("Subject.txt", "a")
    name = input("Введите название нового предмета - ")
    file.write(name + "\n")
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
else:
    print("Error")