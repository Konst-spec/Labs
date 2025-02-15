def gen(n):
    for i in range(n + 1):
        if i == 0:
            continue
        if i % 3 == 0 and i % 4 == 0:
            yield i

a = int(input())
for i in gen(a):
    print(i)