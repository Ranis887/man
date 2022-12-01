class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print(f'Я - User. Могу просматривать содержимое')


class Moderator(User):
    def __init__(self, group_id):
        super().__init__('ranis', '123456788')
        self.group_id = group_id

    def view(self):
        print(f'Я - Moderator. Могу просматривать содержимое')

    def redact(self):
        print(f'Я - Moderator. Могу редактировать содержимое')


u = User('ranis', '123456789')
m = Moderator("32432423")
u.view()
m.view()
m.redact()
