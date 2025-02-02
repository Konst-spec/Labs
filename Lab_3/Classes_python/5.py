class Account():
    def __init__(self, owner = ""):
        self.owner = owner
        self.balance = 0
    def deposit(self, money):
        self.balance += money
        print(f"Сумма добавлена, ваш баланс: {self.balance}")
    def withdraw(self, money):
        if(money >= self.balance):
            print("Сумма снятия превышает доступный баланс")
        else:
            self.balance -= money
            print(f"Сумма успешно снята, ваш баланс {self.balance}")

x = Account("Konstantin")
x.deposit(5000)
x.deposit(10000)
x.withdraw(500)
x.withdraw(15000)
x.deposit(500)
