import os

path = r"B:\Lab_1\Lab_6\dir-and-files\txt.txt"
path1 = r"B:\Lab_1\Lab_6\dir-and-files\txt1.txt"
f = open(path, 'r')
a = f.read()
f1 = open(path1, 'w')
f1.write(a)
