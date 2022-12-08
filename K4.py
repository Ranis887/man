from K3 import *
b1 = Box(randint, 'Artur', 'Kazan', 'Nursultan')
b2 = Box(randint, 'Sergey', 'Cheboksary', 'Vladivostok')
b3 = Box(randint, 'Roma', 'Kazan', 'Nursultan')

class Truck:
    def __init__(self, car_brand, power, capacity):
        self.car_brand = car_brand
        self.power = power
        self.capacity = capacity

    def __str__(self):
        return f"{self.car_brand}, {self.power}, {self.capacity}"

    def __add__(self, box):
        self.capacity.append(box)

    def __sub__(self, other):
        self.capacity.pop()

t = Truck('scania', '554', [b1])
t + b2
print(str(t))
#не до конца понял задание