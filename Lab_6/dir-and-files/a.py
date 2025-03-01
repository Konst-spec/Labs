import os

path = "C:\Windows"
d = []
f = []
fd = []
for i in os.listdir(path):
    fd.append(i)
    if os.path.isdir(path + "\\" + i):
        d.append(i)
    if os.path.isfile(path + "\\" + i):
        f.append(i)


print(""" _______________________________________________________________________________________________________
|                                      |                                |                               |
|       files and directories:         |          directories:          |            files:             |
|______________________________________|________________________________|_______________________________|""")

for i in range(len(fd)):
    print("| " + fd[i], " " * (36 - len(fd[i])), end = "|")
    if i >= (len(fd) - len(f)):
        print(" " * 32, end = "|")
        if i >= (len(fd) - len(d)):
            print(" " * 31, end = "|")
    if i < (len(fd) - len(f)):
        print("  " + d[i], " " * (29 - len(d[i])), end = "|")
        if i >= (len(fd) - len(d)):
            print(" " * 31, end = "|")
    if i < (len(fd) - len(d)):
        print("  " + f[i], " " * (28 - len(f[i])), end = "|")
    
    print("")

print("|______________________________________|________________________________|_______________________________|")