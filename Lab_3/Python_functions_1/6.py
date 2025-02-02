def myReverse(str):
    a = str.split()
    b = a[::-1]
    c = ""
    for i in b:
        c += i + " "
    return c

a = "We are ready"
print(myReverse(a))