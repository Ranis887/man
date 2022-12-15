import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)

a = input("Введите имя автора: ")

f = open("Author.txt", "w")
cursor.execute("SELECT * FROM Books WHERE Author = ?", [a])
for x in cursor.fetchall():
    f.write(f"{x[0]} - {x[1]} - {x[2]} - {x[3]}\n")
f.close()
db.close()