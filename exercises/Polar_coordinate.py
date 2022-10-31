import math
from math import sqrt, sin, cos, atan  # you will need these
from math import pi, isclose  # the tests below will need these


class PolarCoordinate:
    def __init__(self, r, phi):
        self._r = r
        self._phi = phi

    @property
    def radius(self):
        return self._r

    @property
    def angle(self):
        return self._phi

    @radius.setter
    def radius(self, value):
        self._r = value

    @angle.setter
    def angle(self, value):
        self._phi = value

    def to_cartesian(self, x, y):
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        return x, y

    @classmethod
    def from_cartesian(cls, x, y):
        x = sqrt(x**x + y**y)
        y = atan(y/x)
        cls(x, y)

    def __str__(self):
        pass


polar = PolarCoordinate(5, 60)
print(PolarCoordinate.__str__())
