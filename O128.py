from tkinter import *

def kilometr():
    k = entry_box1.get()
    k = int(k)
    mile = k * 0.6214
    output_txt.delete(0, END)
    output_txt.insert(END, mile)
    output_txt.insert(END, " Миль")
    entry_box1.delete(0, END)

def miles():
    m = entry_box1.get()
    m = int(m)
    km = m * 1.6093
    output_txt.delete(0, END)
    output_txt.insert(END, km)
    output_txt.insert(END, " Км")
    entry_box1.delete(0, END)


win = Tk()
win.title("Км в мили и наоборот")
win.geometry("320x205")
label1 = Label(text="Введите расстояние: ")
label1.place(x=20, y=20, width=280, height=30)

entry_box1 = Entry(text="")
entry_box1.place(x=20, y=55, width=280, height=30)

output_txt = Entry(text=0)
output_txt ["bg"] = "red"
output_txt.place(x=20, y=155, width=280, height=30)

button1 = Button(text="Мили в км", command=miles)
button1.place(x=20, y=90, width=280, height=30)
button2 = Button(text="Км в  мили", command=kilometr)
button2.place(x=20, y=120, width=280, height=30)

win.mainloop()
