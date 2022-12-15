import math
def calc():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    print("Введите:\nroot - для извлечения корня\npower - для возведения в степень")
    c = input()
    if str(c) == 'root':
        res = math.sqrt(a)
        print(res)
    elif str(c) == 'power':
        res = math.pow(a, b)
        print(res)
    else:
        print("Введена неверная операция!")
calc()