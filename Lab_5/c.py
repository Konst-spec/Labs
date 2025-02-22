import re

with open("row.txt", "r", encoding="utf-8") as file:
    a = file.read()

b = re.findall(r"[a-z]+_[a-z]+", a)
print(b)