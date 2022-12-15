def get_login():
    login = input("введите логин:\n")
    return login

def get_password():
    password = input("введите пароль:\n")
    new_pas = hex(hash(password))
    return new_pas