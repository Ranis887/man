log = input("Введите логин:\n")

login = ["Angelina", "Ilnur", "Jason"]


def checker():
    if log not in login:
        chk = True
    else:
        chk = False
    return chk


def validate():
    zap = ["#", "$", "%", "&"]
    if zap[0] in log:
        return
    elif zap[1] in log:
        return
    elif zap[2] in log:
        return
    elif zap[3] in log:
        return
    else:
        chk = True
    return chk


def register():
    if checker() == True and validate() == True:
        login.append(log)
        print("Вы успешно зарегистрировались!")
    else:
        print("Error")