from tkinter import *
def Call():
    msg = Label(window, text = f"Hello, {entry_box.get()} ")
    msg.place(x = 130, y = 80)
    button["bg"] = "Yellow"
    button["fg"] = "Black"

a = "Hello, "
window = Tk()
window.geometry("300x120")
label = Label(text = "Введите свое имя: ")
label.place(x=30, y=20)
entry_box = Entry(text = 0)
entry_box.place(x=150, y=20, width = 80, height = 20)
button = Button(text = "love you!", command = Call)
button.place(x = 50, y = 45, width = 200, height = 30)
window.mainloop()