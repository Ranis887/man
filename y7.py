from checkin import *

login()

print("\nЖелаете удалить пользователя? да/нет: ")
otv = input()
if otv == "да":
    del_user()