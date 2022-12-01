from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    def set_color(self):
        self.color = "yellow"
        return self.color

    @abstractmethod
    def draw(self):
        print('Zapusk otrisovki')


class Pen(Stationery):
    def __init__(self, color):
        super().__init__('Ручка')
        self.color = color


    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'{self.title} пишет, но нужно поточить')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'{self.title} пишет замечательно')

pen = Pen('Blue')
pencil = Pencil()
handle = Handle()
print(pen.color)
pen.draw()
pencil.draw()
handle.draw()
print(pen.title, pen.set_color())
print(pencil.title, pencil.set_color())
print(handle.title, handle.set_color())