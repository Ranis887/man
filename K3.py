from random import randint

class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    @property
    def postcode(self):
        a = randint(100000, 999999)
        return a

    @property
    def name(self):
        return self.__name

    @property
    def from_city(self):
        return self.__from_city

    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city(self, new_target_city):
        self.__target_city = new_target_city
        return self.__target_city

b = Box(randint, 'Ranis', 'Kazan', 'Nursultan')
print(b.postcode, b.name, b.from_city, b.target_city)
b.target_city = 'Moscow'
print(b.target_city)