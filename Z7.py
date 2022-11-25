#на стадии разработки
from Z6 import Checker

import hashlib

class User:
    def __init__(self):
        self.get_login()
        self.get_password()

    def get_login(self):
        b = Checker()
        if b != Exception:
            self.login = b
            return

    def get_password(self):
        password = input('Введите пароль: ')
        self.get_hash(password)

    def get_hash(self, ):


us = User()
print(us.__dict__)