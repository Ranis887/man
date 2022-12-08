from tkinter import *
def klik():
    c = col.get()
    win.configure(bg = c)

win = Tk()
win.title("Цвет фона")
win.geometry("250x400")
button = Button(text = "Click Me", command = klik)
button.place(x = 50, y = 90, width = 150, height = 50)
col = StringVar(win)
col.set("Выберите цвет")
color = OptionMenu(win, col, "Black", "Red", "Orange", "Yellow")
color.place(x = 25 , y = 20, width = 200, height = 50)
mainloop()