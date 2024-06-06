from equipment import *
from stock import *
from stock_equipment import *

stock1 = Stock()
printer1 = Printer('принтер')
StockEquipment.append(stock1, printer1, 100)
print(StockEquipment.get_all())
StockEquipment.append(stock1, printer1, 100)
print(StockEquipment.get_all())
print(list(StockEquipment.get_all().keys())[0][1].name)
