import os

path1 = r"B:\Lab_1\Lab_6\dir-and-files\txt1.txt"

if os.path.exists(path1):
    os.remove(path1)