a = [6, 1, 3, 7, 2]

print(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) if x >= 2 else False, a)))
