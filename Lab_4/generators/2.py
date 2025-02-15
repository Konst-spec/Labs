def gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

a = int(input())
for i in gen(a):
    print(i)