class Father():
    def __init__(self, name, surname):
        self.surname = surname
        self.name = name


class Child(Father):
    def __init__(self, patronim):
        super().__init__('Petrov', 'Vlad')
        self.patronim = patronim


child = Child('Olegovich')
print(child.name)
print(child.surname)
print(child.patronim)