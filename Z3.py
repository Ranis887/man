import re


def find_email():
    try:
        str = 'Всем привет! Меня зовут Алексей.Мой email: alexVB@gmail.com . Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru'
        email = re.findall(r'\w+@\w+.\w+', str)
        print(email)
    except:
        print('Адреса почт не найдены!')
find_email()
