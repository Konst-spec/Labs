import os

path = "C:\Windows"

print(f"Путь: {path}")
print("Существует:", os.path.exists(path))
print("Читаемый:", os.access(path, os.R_OK))
print("Записываемый:", os.access(path, os.W_OK))
print("Исполняемый:", os.access(path, os.X_OK))
