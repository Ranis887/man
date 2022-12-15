def fibbonacci():
    a = 0
    b = 1
    for x in range(10):
        yield a
        a, b = b, a + b

print(list(fibbonacci()))