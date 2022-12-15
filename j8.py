from random import randint

print("Вам дается 10 попыток")
def chislo(a = randint(0, 100), n = 0):
    while n != 10:
        b = int(input("Введите число: "))
        if b == a:
            return print(f"Вы угадали! Число - {b}")
        elif b < a:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")
        return chislo(a, n + 1)
    return print(f'Вы проиграли! Число - {a}')
chislo()