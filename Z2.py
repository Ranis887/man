import re


def check():
    try:
        a = input('Введите слово: ')

        class MyExeption(Exception):
            pass

        if re.search("[!@#$%^&*]", a, re.I) is None:
            print(a)
        else:
            raise MyExeption
    except MyExeption:
        print("Ошибка")
