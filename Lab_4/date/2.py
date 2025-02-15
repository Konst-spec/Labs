import datetime

x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day - 1)
z = datetime.datetime(x.year, x.month, x.day + 1)

print(y)
print(x)
print(z)
