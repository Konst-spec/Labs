import os

path = r"B:\Lab_1\Lab_6\dir-and-files\txt.txt"

with open(path, 'r') as a:
    count = 0
    for i in a:
        count += 1
print("кол-во строк:", count)