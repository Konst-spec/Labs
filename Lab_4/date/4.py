import datetime

x = datetime.datetime(2025, 2, 15, 20, 30, 0)
y = datetime.datetime(2025, 2, 15, 20, 45, 30)


dif = (x - y).total_seconds()

print(abs(dif))