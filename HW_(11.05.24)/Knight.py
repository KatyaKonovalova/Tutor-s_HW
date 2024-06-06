import random


class Knight:
    knights = []

    def __init__(self, name):
        self.name = name
        self.hp = 100
        Knight.knights.append(self)

    def __str__(self):
        return self.name

    def wound(self):
        self.hp -= 20
        return self.hp

    def attack(self, other):
        if isinstance(other, Knight):
            other.hp -= 20
            print(f'{self} атаковал воина {other}')
            print(f'{other} потерял 20 хп\n'
                  f'{self} = {self.hp} хп\n'
                  f'{other} = {other.hp} хп\n')


knight_1 = Knight('1')
knight_2 = Knight('2')

# print(knights)

while knight_1.hp != 0 and knight_2.hp != 0:
    knights = Knight.knights.copy()

    random_knight = random.choice(knights)
    knights.remove(random_knight)

    random_knight2 = random.choice(knights)
    # print(random_knight)
    random_knight.attack(random_knight2)
