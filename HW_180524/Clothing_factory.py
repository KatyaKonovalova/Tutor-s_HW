from abc import ABC

# В чем разница абстрактного(базового) класса от родительского? Не поняла, что поменялось когда сделала
# родительский класс Clothes абстрактным классом.
class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class Coat(Clothes):
    def __init__(self, title, size):
        # надо ли повторять в классе наследнике поле 'title' (если есть другие поля, то не надо?)
        super().__init__(title)
        self.size = size

    def fabric(self):
        coat_fabric = round(self.size / 6.5 + 0.5, 1)
        return f'для {self} в размере {self.size} расход ткани составит {coat_fabric}'

    # @property
    # def size(self):
    #     return self.size
    #
    # @size.setter
    # def size(self, size):
    #     if size >= 1:
    #         self.size = size
    #     else:
    #         raise ValueError('size must be greater than 0')
    """"не работает. не понимаю по какой причине. В целом не могу понять
    для чего использовать @property, если не для замены значения поля с защищенным доступом"""


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    def fabric(self):
        suit_fabric = 2 * self.height + 0.3
        return f'для {self} в размере {self.height} расход ткани составит {suit_fabric}'


coat1 = Coat('пальто', 2)
print(coat1.fabric())

suit1 = Suit('костюм', 2)
print(suit1.fabric())
