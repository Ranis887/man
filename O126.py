from tkinter import *
def Summ():
    a = entry_box.get()
    b = output_box["text"]
    a = int(a)
    b = int(b)
    r = a + b
    output_box["text"] = r

def Clear():
    r = 0
    output_box["text"] = 0
    entry_box.delete(0, END)

window = Tk()
window.title('СУММА')
window.geometry("300x200")

label = Label(text = "Введите число:")
label.place(x=40, y=10, width = 220, height = 20)

entry_box = Entry(text=0)
entry_box.place(x=40, y=40, width = 220, height = 30)

output_box = Message(text=0)
output_box ["bg"] = "yellow"
output_box.place(x=40, y=80, width = 220, height = 30)

button1 = Button(text = "Итог", command = Summ)
button1.place(x = 40, y = 120, width = 100, height = 30)

button2 = Button(text = "Очистить", command = Clear)
button2.place(x = 160, y = 120, width = 100, height = 30)
window.mainloop()