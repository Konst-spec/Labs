class MyString():
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())

x = MyString()
x.getString()
x.printString()