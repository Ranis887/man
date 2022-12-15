def cesar(s):
    a = []
    for i in range(len(s)):
        a.append(chr(ord(s[i]) + 3))
    print("".join(a))

b = input("Введите строку: ")
cesar(b)