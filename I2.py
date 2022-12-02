class Queue:
    def __init__(self):
        self.inside = ['Ranis', 'Roma', 'Ildar', 'Angelina']

    def __str__(self):
        return '->'.join(self.inside)

    def __add__(self, other):
        self.inside.append(other)
        return self

    def __isub__(self, other):
        self.inside.pop(other)
        return self

    def add(self):
        a = input('Введите имя пришедшего: ')
        self.inside.append(a)

    def take_out(self):
        self.inside.pop(0)


q = Queue()
print(q)
q.add()
q.take_out()
print(q)
