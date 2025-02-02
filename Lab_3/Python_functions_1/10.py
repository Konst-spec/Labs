def uniq(a):
    b = []
    for i in a:
        if i in b:
            continue
        else:
            b.append(i)
    return b

a = [1,2,4,0,0,7,5]
print(uniq(a))