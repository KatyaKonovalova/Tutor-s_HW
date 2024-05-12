class Stationary:
    def __init__(self, title):
        self.title = title

    # @staticmethod - будет ли правильно поставить staticmethod
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationary):
    def draw(self):
        print('Рисуем маркером')


pen1 = Pen('карандаш')
pen1.draw()

pencil1 = Pencil('ручка')
pencil1.draw()

handle1 = Handle('маркер')
handle1.draw()