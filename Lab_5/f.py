import re

with open("row.txt", 'r', encoding="utf-8") as file:
    a = file.read()

b = re.sub(r'[ ,.]', ':', a)
print(b)