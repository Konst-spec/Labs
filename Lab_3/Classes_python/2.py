class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length: int):
        self.area = length*length



x = Shape()
y = Square(5)
x.Area()
y.Area()