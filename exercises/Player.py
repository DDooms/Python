import math


class Player:
    def __init__(self, name, hp=10, xp=0, level=1):
        self._name = name
        self._hp = hp
        self._xp = xp
        self._level = level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value

    @property
    def level(self):
        if self.xp < 300:
            self._level = 1
        else:
            self._level = 2 + math.log2(self.xp / 300)
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def __str__(self):
        return f"Player, that goes by name {self.name}, has {self.hp} hp, {self.xp} xp and is level {self.level}!"

    def __repr__(self) -> str:
        return f"Player, that goes by name {self.name}, has {self.hp} hp, {self.xp} xp and is level {self.level}!"


player1 = Player("Beray", 50, 560)
print(player1.__str__())
