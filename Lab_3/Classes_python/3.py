class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        print(self.area)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.area = length * width

x = Rectangle(4, 5)
x.Area()