from reg import *

paroli = {"Angelina": "ucsdc", "Dwayne": "asd", "Bulkin": "xsa887"}
passw = input("Введите пароль:\n")

def login():
    pas = paroli.get(log)
    if pas and pas == passw:
        print("Доступ разрешён!")
    elif not pas:
        register()
        paroli[log] = passw
        print("Регистрация прошла успешно!")
    else:
        print("Доступ запрещён!")


def del_user():
    delet = input("Какого пользователя хотите удалить?\n")
    paroli.pop(delet)
    print("подождите", end=" ")
    for i in range(3):
        print(".", end=" ")
    print("\nПользователь удалён!")
    return delet