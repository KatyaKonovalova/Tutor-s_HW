from abc import ABC, abstractmethod


class Equipment(ABC):
    def __init__(self, title, version, price, amount_in_stock):
        self.__title = title
        self.__version = version
        self.__price = price  # как понять, какой режим доступа выбрать private или protected?
        self.__amount_in_stock = amount_in_stock
        self.amount_check(amount_in_stock)

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


if __name__ == '__main__':
    printer1 = Printer('Sony', '111', 10000, '', 'color')
    print(printer1.amount_in_stock)

    try:  # программа падает, хотя, сделала так, как было на уроке(
        printer1.amount_in_stock = 2
        print(printer1.amount_in_stock)
    except TypeError:
        print('Неверный формат номера телефона')
    except ValueError:
        print('Количество не может быть 0 или меньше')

    printer2 = Printer('Sony', '222', 20000, 10, 'white and black')
    print(printer2.color)
