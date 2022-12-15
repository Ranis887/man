import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

god = int(input("Введите год: "))

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books WHERE DatePublished > ? ORDER BY DatePublished """, [god])
for x in cursor.fetchall():
    print(x)

db.close()
