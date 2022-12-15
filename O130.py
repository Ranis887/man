from tkinter import *
import csv

def save():
    with open("Spisok.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        lst = list_box1.get(0, END)
        writer.writerow(lst)

def chistka():
    list_box1.delete(0, END)

def spisok():
    a = entry_box1.get()
    if a.isdigit():
        list_box1.insert(END, a)
        entry_box1.delete(0, END)
    else:
        entry_box1.delete(0, END)

win = Tk()
win.title("Целые числа")
win.geometry("300x300")

label1 = Label(text = "Введите число: ")
label1.place(x = 20, y = 20, width = 90, height = 30)

entry_box1 = Entry(text = 0)
entry_box1.place(x = 120, y = 20, width = 160, height = 30)

list_box1 = Listbox()
list_box1.place(x = 20, y = 120, width = 260, height = 100)

button1 = Button(text = "Проверить", command = spisok)
button1.place(x = 20, y = 70, width = 120, height = 30)

button2 = Button(text = "Очистить список", command = chistka)
button2.place(x = 160, y = 70, width = 120, height = 30)

button3 = Button(text = "Сохранить", command = save)
button3.place(x = 20, y = 240, width = 260, height = 30)

win.mainloop()