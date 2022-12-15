from random import *
from tkinter import *
def Call():
    ya = randint(1, 6)
    msg = Label(window, text = ya)
    msg.place(x = 130, y = 80)
    button["bg"] = "Red"
    button["fg"] = "Green"
window = Tk()
window.geometry("300x120")
button = Button(text = "Spin the wheel!", command = Call)
button.place(x = 50, y = 45, width = 200, height = 30)
window.mainloop()