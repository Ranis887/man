def calcul():
    a = int(input("введите первое число - "))
    b = int(input("введите второе число - "))
    calculate = input("введите операцию:\n")
    print(eval(f'{a}{calculate}{b}'))
calcul()