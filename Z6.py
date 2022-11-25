import re


def Checker():
    try:
        log = input("Логин: ")
        a = re.search(r"[!@#$%^&*()_+]", log)
        if a != None:
            raise ValueError
        return log

    except ValueError:
        print('Неправильный логин! Введены недопустимые символы.')


Checker()
