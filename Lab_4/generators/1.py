def gen(n): 
    for i in range(n + 1):
        yield i**2

for i in gen(5):
    print(i)