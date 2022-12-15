def factorial():
    a = int(input("Введите число:"))
    fac = 1
    while a > 0:
        fac *= a
        a -= 1
    return fac
print(factorial())



def factor(b,a=1,f=0):
    if f == b:
        print(a)
        return
    else:
        a *= b
        return factor(b-1,a)
factor(4)