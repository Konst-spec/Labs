import os

path = "C:\Windows"

if os.path.exists(path):
    print("Каталог:", os.path.dirname(path))
    print("Имя файла:", os.path.basename(path))
else:
    print("Указанный путь не существует")
 