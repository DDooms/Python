import random

members = ['John', 'Mary', 'Beray']
leader = random.choice(members)
print(leader)

for i in range(3):
    print(random.randint(10, 20))
    print(random.random())


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
dice.roll()
