from insert import *
from update import *
from delete import *
from get import *

table = "PhoneBook"

while True:
    a = input("""Выберите что вы хотите сделать:
      1. Добавить номер
      2. Изменить номер
      3. Удалить номер
      4. Посмотреть номера
      5. Загрузить номера из CSV файла  
      6. Выход  \n""")

    if a == "1":
        b = input("Введите имя и номер:\n")
        c = b.split(" ")
        name, number = c[0], c[1]
        insert_number(table, name, number)
        print("Запись сохранена\n")
    elif a == "2":
        b = input("Введите имя и номер:\n")
        c = b.split(" ")
        name, number = c[0], c[1]
        update_number(table, name, number)
        print(f"Номер у {name} изменен\n")
    elif a == "3":
        name = input("Введите имя:\n")
        delete_number(table, name)
        print("Номер удален\n")
    elif a == "4":
        b = input("""1. По имени 
2. По номеру
3. Все номера \n""")
        if b == "1":
            c = input("Введите имя: ")
            get_numbers(table, name=c)
        elif b == "2":
            c = input("Введите номер: ")
            get_numbers(table, number=c)
        elif b == "3":
            get_numbers(table)
        else:
            print("Данной опции не существует\n")
    elif a == "5":
        path = input("Введите имя файла или путь:\n")
        upload_from_csv(path)
    elif a == "6":
        break
    else:
        print("Данной опции не существует\n")
