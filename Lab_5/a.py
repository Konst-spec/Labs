import re

with open("row.txt", "r", encoding="utf-8") as file:
    a = file.read()

b = re.findall(r"аб*", a)
print(b)