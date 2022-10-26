# without a constructor
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.draw()
print(point1.x)


# with a constructor
class Point2:
    def __init__(self, x, y):  # initialise
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point2 = Point2(10, 20)
print(point2.x)


# Person
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print("Im talking right now!")


person = Person("Beray", "Syuleyman", 21)
print(person.first_name)
person.talk()
