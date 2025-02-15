def gen(n):
    a = range(n + 1)
    b = a[::-1]
    for i in b:
        yield i

for i in gen(10):
    print(i)