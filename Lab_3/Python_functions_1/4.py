def filter_prime(a: list):
    b = []
    for i in a:
        c = True
        if (int(i) < 2):
            c = False
        else:
            for j in range(2, int(i)):
                if int(i) % j == 0:
                    c = False
        if c:
            b.append(i)
    return b

str = input()
a = str.split()
print(filter_prime(a))
