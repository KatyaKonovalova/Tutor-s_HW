from abc import ABC, abstractmethod


class Equipment(ABC):
    def __init__(self, name):
        self.name = name


class OfficeEquipment(Equipment):
    pass


class FurnitureEquipment(Equipment):
    pass


class Table(FurnitureEquipment):
    pass


class Printer(OfficeEquipment):
    pass


class Scaner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass
