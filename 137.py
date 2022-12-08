from tkinter import *
def chel():
    n = entry_box1.get()
    poll = pol.get()
    chelov = f"{n}, {poll}"
    list.insert(END, chelov)
    entry_box1.delete(0, END)
    pol.set("Выберите свой пол:")
    file = open("spisok.txt", "a")
    file.write(chelov + '\n')
    file.close()

def spisokk():
    file = open("spisok.txt", "r")
    print(file.read())

win = Tk()
win.title("Список")
win.geometry("310x430")
win["bg"] = "blue"
entry_box1 = Entry(text = "")
entry_box1.place(x = 140, y = 20, width = 150, height = 30)
pol = StringVar(win)
pol.set("Выберите свой пол:")
m = OptionMenu(win, pol, "МУЖ", "ЖЕН")
m.place(x = 20, y = 70, width = 275, height = 30)
lb1 = Label(text = "Введите свое имя: ")
lb1.place(x = 20, y = 20, width = 110, height = 30)
button = Button(text = "Добавить", command = chel)
button.place(x = 20, y = 320, width = 275, height = 30)
list = Listbox()
list.place(x = 20, y = 110, width = 275, height = 200)
button1 = Button(text = "Открыть лист", command = spisokk)
button1.place(x = 20, y = 360, width = 275, height = 30)


win.mainloop()