import string

a = list(string.ascii_lowercase)
b = 1

for i in range(len(a)):
    print(str(b) + " " + a[i])
    b += 1

for i in range(len(a)):
    print('{' + str(ord(a[i])) + ':' + a[i] + '}')