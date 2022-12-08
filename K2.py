class Cloth():

    @property
    def clothes(self):
        return self.__clothes

class Coat(Cloth):
    reversed = 0
    def __init__(self, V):
        self.V = V
        Coat.reversed += self.V/6.5 + 0.5
        self.__clothes = self.V/6.5 + 0.5

class Suit(Cloth):
    reversed = 0
    def __init__(self, H):
        self.H = H
        Suit.reversed += self.H * 2 + 0.3
        self.__clothes = self.H * 2 + 0.3


s1 = Suit(13)
c1 = Coat(87)
s2 = Suit(63)
c2 = Coat(196)
c3 = Coat(33)

print(f"Для костюмов - {Suit.reversed}")
print(f"Для пальто - {Coat.reversed}")
