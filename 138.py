from tkinter import *


def clicked():
    a = selection.get()
    s = a + ".gif"
    photo = PhotoImage(file=s)
    photo_box.image = photo
    photo_box["image"] = photo
    photo_box.update()


win = Tk()
win.title("Гифки")
win.geometry("300x250")

gif = PhotoImage(file="1.gif")
photo_box = Label(win, image=gif)
photo_box.image = gif
photo_box.place(x=50, y=20, width=200, height=150)

label = Label(text="Введите номер 1-3: ")
label.place(x=50, y=170, width=110, height=30)

selection = Entry(text="")
selection.place(x=160, y=175, width=90, height=30)

button = Button(text="Посмотреть", command=clicked)
button.place(x=50, y=210, width=200, height=30)

win.mainloop()
