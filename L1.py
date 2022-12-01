from abc import ABC, abstractmethod


class AnimalClass(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Cat(AnimalClass):
    def say(self):
        print('Meow!')

class Dog(AnimalClass):
    def say(self):
        print('Woof!')
cat = Cat()
dog = Dog()
cat.say()
dog.say()