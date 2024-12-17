# 3. Import Class
# shapes.py
from math import pi

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def display(self):
        print(f"Radius: {self.radius}")

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return pi * (self.radius ** 2)

    def circumference(self):
        return 2 * pi * self.radius

# Rectangle operations
r = Rectangle(1, 1)
r.display()
r.setWidth(1.25)
r.setHeight(1.25)
print(f"Get Width: {r.getWidth()}")
print(f"Get Height: {r.getHeight()}")
print(f"Area: {r.area()}")

# Circle operations
c = Circle(0)
c.display()
c.setRadius(10)
print(f"Get Radius: {c.getRadius()}")
print(f"Area: {c.area():.5f}")
print(f"Circumference: {c.circumference():.5f}")
