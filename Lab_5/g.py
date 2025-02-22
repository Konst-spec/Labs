import re

with open("row.txt", 'r', encoding="utf-8") as file:
    a = file.read()

b = re.sub(r'_([a-z])',lambda f: f.group(1).upper(), a)
c = re.findall(r'(\b[a-z]+[A-Z][a-z]+)+', b)
print(c)