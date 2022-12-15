import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

print("Main Menu\n1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit")
a = int(input("Введите номер:\n"))

if a == 1:
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
elif a == 2:
    newid = int(input("Введите ID: "))
    firstname = input("Введите Имя: ")
    surname = input("Введите Фамилию: ")
    phone = int(input("Введите телефон: "))
    cursor.execute(""" INSERT INTO Names(ID, First Name, Surname, Phone Number)
        VALUES (?, ?, ?, ?)""", (newid, firstname, surname, phone))
    db.commit()
elif a == 3:
    surrname = input("Введите фамилию: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [surrname])
    for x in cursor.fetchall():
        print(x)
elif a == 4:
    idd = int(input("Введите ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [idd])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()
elif a == 5:
    exit()
else:
    print("Такого пункта нет")
db.close()

