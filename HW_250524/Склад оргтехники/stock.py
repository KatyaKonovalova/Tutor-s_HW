class Stock:
    def __init__(self, tipe, volume, design):
        self.__tipe = tipe
        self.__volume = volume
        self.__design = design

    @property
    def tipe(self):
        return self.__tipe

    @property
    def volume(self):
        return self.__volume

    @property
    def design(self):
        return self.__design


stock1 = Stock('Временного хранения', '5000 кв.м.', 'Закрытый')
print(stock1.tipe)