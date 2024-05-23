import stock
import equipment

printer1 = equipment.Printer('Sony', '111', 10000, 20, 'color')
print(printer1.new_equipment(printer1.title, printer1.amount_in_stock))

try:
    printer1.amount_in_stock = -1
    print(printer1.amount_in_stock)
except TypeError:
    print('Неверный формат. Должно быть число.')
except ValueError:
    print('Количество не может быть 0 или меньше')

scaner1 = equipment.Scaner('Epson', '222', 20000, 10, 2000)
print(scaner1.new_equipment(scaner1.title, scaner1.amount_in_stock))

#
try:
    stock.Stock.send_into_stock()
except TypeError:
    print('Неверный формат. Должно быть число.')
except ValueError:
    print('Запрашиваемое количество должно быть больше 0')

# Как сделать, чтобы количество товара после изменения не возвращалось к исходному, после следующего запуска программы?
