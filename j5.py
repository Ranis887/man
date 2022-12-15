def Fibbonacci():
    lst = [0, 1]
    a = 1

    while True:
        x = lst[a]
        y = lst[a - 1]
        z = x + y
        if z >= 100:
            break
        lst.append(z)
        a =  a + 1
    return lst

print(Fibbonacci())

def fibbonacci(lst = [0, 1]):
    a = len(lst)
    x = lst[a - 1]
    y = lst[a - 2]
    z = x + y
    if z >= 100:
        return
    lst.append(z)
    fibbonacci(lst)
    return lst
print(fibbonacci())