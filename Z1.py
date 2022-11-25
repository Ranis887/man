def validator():
    try:
        a = int(input('Введите число - '))
        print(a * a)

    except:
        print('Ошибка')


validator()
