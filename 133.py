from tkinter import *

def call():
    output_box = Message()
    output_box.place(x=110, y=400, width=140, height = 30)
    output_box["text"] = f"Hello, {entry_box.get()}!!"
    output_box["bg"] = "red"

win = Tk()
win.title("133")
win.geometry("900x620")
win["bg"] = "black"
photo = PhotoImage(file = "loggo.png")
win.iconphoto(False, photo)
label = Label(text = "Введите свое имя: ")
label.place(x=630, y=290, height = 20)
photo1 = PhotoImage(file = "bobo.png")
photobox = Label(win, image = photo1)
photobox.image = photo1
photobox.place(x = 10, y = 10, width = 600, height = 600)
entry_box = Entry (text = 0)
entry_box.place(x=760, y=290, width= 130, height = 20)
button = Button(text = "Press Me", command=call)
button.place(x=760, y=590, width=130, height = 20)
win.mainloop()