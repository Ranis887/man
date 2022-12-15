def count(i):
    a = 0
    b = 0
    while i < 11:
        if i%2==0:
            a += 1
            i += 1
        else:
            b += 1
            i += 1
    print(f"Количество четных чисел - {a}")
    print(f"Количество нечетных чисел - {b}")
count(1)

def count(i,x=0,y=0):
    if i % 2 == 0:
        x += 1
    elif i % 2 > 0:
        y += 1
    if i == 1:
        print(f"Количество четных чисел - {x}")
        print(f"Количество нечетных чисел - {y}")
        return
    else:
        return count(i - 1, x, y)
count(10)