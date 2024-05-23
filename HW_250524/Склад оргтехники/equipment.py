from abc import ABC, abstractmethod


class Equipment(ABC):
    dict_equipment = {}

    def __init__(self, title, version, price, amount_in_stock):
        self.__title = title
        self.__version = version
        self.__price = price
        self.__amount_in_stock = amount_in_stock
        self.amount_check(amount_in_stock)
        # Как понять на начальных этапах, какой режим доступа выбрать правильнее private или protected?
        # Какой надежнее и избавляет от при дальнейшей работе?

    def new_equipment(self, title, amount_in_stock):
        # а если мне нужно всю информацию о товаре занести? А в каждом классе разные поля color/speed/quality
        self.dict_equipment[title] = amount_in_stock
        return self.dict_equipment  # почему нет разницы между self.list_of_equipment и Equipment.list_of_equipment?

    @property
    def title(self):
        return self.__title

    @property
    def version(self):
        return self.__version

    @property
    def price(self):
        return self.__price

    @property
    def amount_in_stock(self):
        return self.__amount_in_stock

    def amount_check(self, amount_in_stock):
        if isinstance(amount_in_stock, int):
            self.__amount_in_stock = amount_in_stock
        else:
            raise TypeError("Неверный формат. Должно быть число.")
        if self.__amount_in_stock <= 0:
            raise ValueError("Количество в наличии должно быть больше 0")

    @amount_in_stock.setter
    def amount_in_stock(self, amount_in_stock):
        self.amount_check(amount_in_stock)


class Printer(Equipment):
    def __init__(self, title, version, price, amount_in_stock, color):
        super().__init__(title, version, price, amount_in_stock)
        self.__color = color

    @property
    def color(self):
        return self.__color


class Scaner(Equipment):
    def __init__(self, title, version, price, amount_in_stock, speed):
        super().__init__(title, version, price, amount_in_stock)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed


class Xerox(Equipment):
    def __init__(self, title, version, price, amount_in_stock, quality):
        super().__init__(title, version, price, amount_in_stock)
        self.__quality = quality

    @property
    def quality(self):
        return self.__quality
