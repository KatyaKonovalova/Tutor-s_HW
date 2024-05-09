import random


class Knight:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def __str__(self):
        return self.name

    def knights_list(self, knights=[]):
        knights.append(self)
        return knights

    def wound(self):
        self.hp -= 20
        return self.hp

    def attack(self):
        print(f'{self.name} атаковал')


knight_1 = Knight('1')
knight_2 = Knight('2')

knight_1.knights_list()
knights = knight_2.knights_list()
# print(knights)

while knight_1.hp != 0 and knight_2.hp != 0:

    random_knight = random.choice(knights)
    # print(random_knight)
    random_knight.attack()

    if random_knight == knight_1:
        knight_2.wound()
        print(f'{knight_2.name} потерял 20 хп\n'
              f'{knight_1} = {knight_1.hp} хп\n'
              f'{knight_2} = {knight_2.hp} хп\n')
    else:
        hp = knight_1.wound()
        print(f'{knight_1.name} потерял 20 хп\n'
              f'{knight_2} = {knight_2.hp} хп\n'
              f'{knight_1} = {knight_1.hp} хп\n')

