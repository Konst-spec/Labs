from insert import *
from delete import *
from get import *

table = "PhoneBook"

while True:
    a = input("""Выберите что вы хотите сделать:
      1. Добавить номер или изменить номер
      2. Удалить номер
      3. Посмотреть номера
      4. Загрузить номера из CSV файла
      5. Добавить пользователей с проверкой номеров вручную
      6. Выход  \n""")

    if a == "1":
        b = input("Введите имя и номер:\n")
        c = b.split(" ")
        name, number = c[0], c[1]
        add_or_update_user(table, name, number)
        print("Запись сохранена\n")
    elif a == "2":
        name = input("Введите имя (или оставьте пустым):\n") or None
        number = input("Введите номер (или оставьте пустым):\n") or None
        delete_number(name=name, number=number)
        print("Номер удален\n")
    elif a == "3":
        b = input("""1. По имени 
2. По номеру
3. Все номера
4. Пагинация\n""")
        if b == "1":
            c = input("Введите имя: ")
            get_numbers(table, name=c)
        elif b == "2":
            c = input("Введите номер: ")
            get_numbers(table, number=c)
        elif b == "3":
            get_numbers(table)
        elif b == "4":
            page = int(input("Номер страницы: "))
            limit = 10
            offset = (page - 1) * limit
            get_users_from_db(limit, offset)
        else:
            print("Данной опции не существует\n")
    elif a == "4":
        path = input("Введите имя файла или путь:\n")
        add_users_from_csv(path)
    elif a == "5":
            add_many_users_from_input()
    elif a == "6":
        break
    else:
        print("Данной опции не существует\n")
