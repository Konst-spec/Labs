import re

with open("row.txt", 'r', encoding="utf-8") as file:
    a = file.read()

b = re.sub(r"(\B[A-Z][a-z]+)", lambda f: "_" + f.group(1).lower(), a)
print(b)