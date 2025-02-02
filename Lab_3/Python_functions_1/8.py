def spy_game(nums):
    a = [0, 0, 7]
    for i in nums:
        if i == a[0]:
            a.pop(0)
        if not a:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
