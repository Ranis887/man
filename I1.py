class Batary():
    def __init__(self):
        self.capacity = []
        self.charge_max = 5
        self.charge_min = 0

    def charge(self):
        if len(self.capacity) == self.charge_max:
            print('max charge')
        else:
            self.capacity.append('I')

    def discharge(self):
        if len(self.capacity) == 0:
            print("min charge")
        else:
            self.capacity.pop(0)

    def __str__(self):
        return '[' + ''.join(self.capacity) +']'

b = Batary()
b.charge()
b.charge()
b.charge()
b.charge()
b.charge()
b.charge()
print(b)
b.discharge()
b.discharge()
b.discharge()
b.discharge()
b.discharge()
b.discharge()
print(b)