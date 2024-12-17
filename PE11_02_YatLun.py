# 2. Import Class 
# class Rectangle 
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

# Instantiate two objects
r1 = Rectangle(4, 5)
r2 = Rectangle()

# Call display()
r1.display()
r2.display()

# Call area()
print(f"Area: {r1.area()}")
print(f"Area: {r2.area()}")

# Update r2 dimensions and display
r2.setWidth(6)
r2.setHeight(6)
print(f"Get Width: {r2.getWidth()}")
print(f"Get Height: {r2.getHeight()}")
print(f"Area: {r2.area()}")