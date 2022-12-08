class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def surname(self):
        return self.__surname

    @age.setter
    def age(self, new_age):
        self.__age = new_age
        return self.__age

p = Person('Ranis', '18', 'Khayrutdinov')
print(p.name, p.surname, p.age)
p.age = '19'
print(p.age)