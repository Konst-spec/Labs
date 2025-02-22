import re

with open("row.txt", 'r', encoding="utf-8") as file:
    a = file.read()

b = re.sub(r"([A-Z][a-z]+)",lambda f: " " + f.group(1), a)
print(b)