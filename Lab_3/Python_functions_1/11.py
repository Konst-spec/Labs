def isPolindrome(a):
    if a == a[::-1]:
        return True
    return False

print(isPolindrome("abba"))