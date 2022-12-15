def get_password(a):
    hash_p = hex(hash(a))
    print(hash_p)


get_password(a = input("Введите  пароль: "))