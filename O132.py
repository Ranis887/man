import csv
from tkinter import *


def spis():
    a_list = []
    with open("O1311.csv", "r") as f:
        reader = csv.reader(f)
        a = list(reader)
    for row in a:
        a_list.append(row)
        x = 0
    for i in a_list:
        ss = a_list[x]
        list_box1.insert(END, ss)
        x = x + 1

def save():
    a = entry_b1.get()
    b = entry_b2.get()
    lst = []
    lst.extend([a, b])
    with open("O1311.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(
            lst
        )
        entry_b2.delete(0, END)
        entry_b1.delete(0, END)


win = Tk()
win.title("ФИО без ИО и возраст")
win.geometry("400x350")

label1 = Label(text="Введите свое имя: ")
label1.place(x=20, y=20, width=140, height=30)

entry_b1 = Entry(text="")
entry_b1.place(x=170, y=20, width=210, height=30)

label2 = Label(text="Введите свой возраст: ")
label2.place(x=20, y=60, width=140, height=30)

entry_b2 = Entry(text=0)
entry_b2.place(x=170, y=60, width=210, height=30)

button1 = Button(text="Сохранить", command=save)
button1.place(x=20, y=100, width=360, height=30)

button2 = Button(text="Список", command=spis)
button2.place(x=20, y=140, width=360, height=30)



label3 = Label(text = "Список: ")
label3.place(x = 20, y = 180, width = 100, height = 30)

list_box1 = Listbox()
list_box1.place(x = 20, y = 220, width = 360, height = 100)

win.mainloop()
