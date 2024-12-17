# 1. Class Implementation
class Rectangle: 
    def __init__(self, width=1, height=1):
        self.width= width 
        self.height= height 

    def display(self):
        print ("width :", self.width, " height :", self.height)
        
# Instantiate two objects of type rectangle
r1 = Rectangle(4, 5) 
r1.display() 

r2 = Rectangle()
r2.display()

print ("width of r1 and r2 : ", r1.width, ' , ' , r2.width)
print ("height of r1 and r2 : ", r1.height, ' , ' , r2.height)