from equipment import Equipment
from equipment import Printer
from equipment import Scaner
from equipment import Xerox  # как ниже вызвать класс, чтобы не импортировать каждый из файла equipment
                             # запись Equipment.Printer не прошла - unresolved references


class Stock:
    list_of_equipment = []

    def __init__(self, tipe, volume, design):
        self.__tipe = tipe
        self.__volume = volume
        self.__design = design
        self.dict_equipment = {}

    @property
    def tipe(self):
        return self.__tipe

    @property
    def volume(self):
        return self.__volume

    @property
    def design(self):
        return self.__design

    @staticmethod
    def get_new_equipment():
        return Equipment.dict_equipment

    # 1. Определить, что хотим отправить на предприятие.
    # 2. Проверить, есть ли такой товар в списке
    # 2. определить количество, которое нужно отправить на предприятие.
    # 3. требуемое количество не должно быть <= 0 и должно быть integer.
    # 4. сравнить есть ли нужное количество на складе.
    # 5. если количество >= нужному, то ок.
    # 6. если нет, то выводится сообщение, что нужного количества нет.
    # 7. Вывести сообщение сколько есть.

    @staticmethod
    def send_into_stock():
        dict_of_equipment = Stock.get_new_equipment()
        item_eq = (input('Что хотите отправить на предприятие? ')).title()
        # for elem in list_of_equipment:
        #     print(elem)
        #     if item_eq in elem:
        #         print(f'Товар {item_eq} имеется на складе в количестве {elem.get(item_eq)} шт.')
        #
        #     if int(amount) <= elem.get(item_eq):
        #         print('Можно предоставить требуемое количество')
        #     else:
        #         print(f'Можно предоставить {elem.get(item_eq)}')
        if dict_of_equipment.get(item_eq):
            print(f'Товар {item_eq} имеется на складе в количестве {dict_of_equipment.get(item_eq)} шт.')
            amount = int(input('\nСколько данного товара требуется? '))

            # Не получается пройти валидацию на соответствие типа данных
            # Все что вводится пользователем - str
            # В дальнейшем надо чтобы amount было int

            if not isinstance(amount, int):
                raise TypeError('Неверный формат. Должно быть число.')
            if amount <= 0:
                raise ValueError('Запрашиваемое количество должно быть больше 0')

            if amount <= dict_of_equipment.get(item_eq):
                print('Можно предоставить требуемое количество')
                print(dict_of_equipment)
                dict_of_equipment[item_eq] = int(dict_of_equipment.get(item_eq)) - amount

                if dict_of_equipment.get(item_eq) == 0:
                    dict_of_equipment.pop(item_eq)

                print(dict_of_equipment)

            else:
                print(f'Можно предоставить только {dict_of_equipment.get(item_eq)}')
                agreement = (input('\nБудете брать? Напишите Да/Нет ')).title()

                if agreement == 'Да':
                    dict_of_equipment.pop(item_eq)
                print(dict_of_equipment)

        else:
            print('Такого товара нет на складе')


# if __name__ == '__main__':
#     stock1 = Stock('Временного хранения', '5000 кв.м.', 'Закрытый')
#     print(stock1.tipe)
