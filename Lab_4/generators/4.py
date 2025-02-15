def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = 5
b = 12
for i in squares(a, b):
    print(i)