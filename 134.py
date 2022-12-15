from tkinter import *
from random import randint

def proverka():
    button['state'] = DISABLED
    r1 = randint(10, 50)
    r2 = randint(10, 50)
    a = r1 + r2
    msg = Message(win, text=f"Сумма 2 рандомных чисел равна {a}")
    msg.place(x=5, y=470, width=390, height = 60)
    if int(entry_box.get()) == a:
        photo = PhotoImage(file="gal.png")
        photobox = Label(win, image=photo)
        photobox.image = photo
        photobox.place(x=20, y=100, width=360, height=360)
    else:
        photo1 = PhotoImage(file="kre.png")
        photobox = Label(win, image=photo1)
        photobox.image = photo1
        photobox.place(x=20, y=100, width=360, height=360)
        button1 = Button(text="Next", command=next)
        button1.place(x=50, y=540, width=300, height=30)




def next():
    button['state'] = NORMAL
    entry_box.delete(0, END)


win = Tk()
win.title("Вычисли сумму")
win.geometry("400x580")

button = Button(text = "Проверить", command = proverka)
button.place(x = 50, y = 50, width=300, height = 30)
entry_box = Entry (text = 0)
entry_box.place(x=100, y=10, width=200, height = 30)
win.mainloop()
