import math


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x = x
        self.y = y

def dist(a = Point(), b = Point()):
    print(math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)) 

x = Point(2, 2)
y = Point(1, 1)
x.move(4, 6)
dist(x, y)