from tkinter import *


def chel():
    n = entry_box1.get()
    list.insert(END, n)
    entry_box1.delete(0, END)


def clear():
    list.delete(0, END)


win = Tk()
win.title("Список")
win.geometry("310x390")
win["bg"] = "blue"
entry_box1 = Entry(text="")
entry_box1.place(x=140, y=20, width=150, height=30)
lb1 = Label(text="Введите свое имя: ")
lb1.place(x=20, y=20, width=110, height=30)
button = Button(text="Добавить", command=chel)
button.place(x=20, y=320, width=275, height=30)
button2 = Button(text="Очистить", command=clear)
button2.place(x=20, y=355, width=275, height=30)
list = Listbox()
list.place(x=20, y=110, width=275, height=200)

win.mainloop()
