def toCelsius(F):
    C = (5 / 9) * (F - 32)
    return C

a = int(input())
print(toCelsius(a))