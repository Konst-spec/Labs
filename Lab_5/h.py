import re

with open("row.txt", 'r', encoding="utf-8") as file:
    a = file.read()

b = re.split(r'[A-Z]', a)

print(b)