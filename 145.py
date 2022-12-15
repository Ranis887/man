from tkinter import *
import sqlite3

with sqlite3.connect("TestScores.db") as db: cursor=db.cursor()

def add():
    a = entry_box1.get()
    b = entry_box2.get()
    cursor.execute("""INSERT INTO Students(name, grade)
    VALUES(?, ?)""",(a, b))
    db.commit()
    entry_box1.delete(0, END)
    entry_box2.delete(0, END)

def clear():
    entry_box1.delete(0, END)
    entry_box2.delete(0, END)

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
 name text NOT NULL,
 grade integer NOT NULL);""")

window = Tk()
window.title("TextScores")
window.geometry("400x150")

label1 = Label(text = "Enter student's name: ")
label1.place(x=20, y=20, width=130, height=30)

entry_box1 = Entry (text="")
entry_box1.place(x=180, y=20, width=200, height=30)

label2 = Label(text = "Enter student's grade: ")
label2.place(x=20, y=60, width=130, height=30)

entry_box2 = Entry (text=0)
entry_box2.place(x=180, y=60, width=200, height=30)

button1 = Button(text = "Add", command=add)
button1.place(x=180, y=100, width= 95, height=30)

button2 = Button(text = "Clear", command=clear)
button2.place(x=280, y=100, width=95, height=30)


window.mainloop()
db.close()