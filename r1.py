def countdown(v):
    for i in range(v, -1, -1):
        yield i


lst = countdown(10)

# next()
i = 10
while i >= 0:
    print(next(lst))
    i -= 1
