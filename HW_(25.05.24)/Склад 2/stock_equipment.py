from stock import *
from equipment import *


class StockEquipment:
    __db = {}

    @staticmethod
    def append(stock: Stock, equipment: Equipment, amount: int):
        StockEquipment.__db[(stock, equipment)] = StockEquipment.__db.get((stock, equipment), 0) + amount

    @staticmethod
    def get_all():
        return StockEquipment.__db