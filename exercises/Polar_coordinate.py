import math
from math import sqrt, sin, cos, atan  # you will need these
from math import pi, isclose  # the tests below will need these


class PolarCoordinate:
    def __init__(self, r=0, phi=0):
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

    def __hash__(self) -> int:
        return super().__hash__()

    @angle.setter
    def angle(self, value):
        self._phi = value

    def to_cartesian(self):
        rad = self.radius * math.cos(self.angle)
        phi = self.radius * math.sin(self.angle)
        return rad, phi

    @classmethod
    def from_cartesian(cls, rad, phi):
        rad = sqrt(x ** x + y ** y)
        phi = atan(y / x)
        return cls(rad, phi)

    def __str__(self):
        return f"Coordinates -> radius = {self.radius}, angle = {self.angle}"

    def __repr__(self):
        return f"Coordinates -> x = {self.radius}, y = {self.angle}"


p1 = PolarCoordinate(1, pi/6)

print(p1.radius == 1)
print(p1.angle == pi/6)

p2 = PolarCoordinate.from_cartesian(3, 4)
print(isclose(p2.radius, 5))
print(isclose(p2.angle, atan(4/3)))

x, y = p2.to_cartesian(3, 4)
print(isclose(x, 3))
print(isclose(y, 4))

p3 = PolarCoordinate(1, 0)
print(str(p3))
print(repr(p3))

pp1, pp2, pp3 = PolarCoordinate(1, pi/6), PolarCoordinate.from_cartesian(3, 4), PolarCoordinate(1, 0)
print(p1 == pp1)
print(p2 == pp2)
print(p3 == pp3)
