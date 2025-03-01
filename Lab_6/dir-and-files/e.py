import os

path = r"B:\Lab_1\Lab_6\dir-and-files\txt.txt"

list = ["asdad", "bobobobobo", "ababbab"]

f = open(path, 'a')

for i in list:
    f.write("\n" + i)

f = open(path, "r")
print(f.read())

f.close()