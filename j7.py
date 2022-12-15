def login():
    log = input("Введите логин: ")
    par = input("Введите пароль: ")
    users = dict(zip(["lognn"], ["parl"]))
    users1 = users.copy()
    if log in users1.keys():
        print("Доступ разрешён")
        return
    elif log not in users1.keys():
        users.setdefault(log, par)
        print("Регистрация прошла успешно")
        return
    else:
        print("Доступ запрещён")
        return
login()