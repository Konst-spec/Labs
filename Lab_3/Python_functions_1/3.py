def solve(nh, nl):
    r = (nl  - 2 * nh) // 2
    c = nh - r
    return c, r

numheads = 35
numlegs = 94
c, r = solve(numheads, numlegs)

print(f"Chickens: {c}, Rabbits: {r}")