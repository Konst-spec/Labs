import psycopg2
import csv
from config import load_config

def insert_number(table, name, number):
    sql = "INSERT INTO " + table + " VALUES(%s, %s);"
    config = load_config(filename='B:/Lab_1/Lab_11/database.ini')
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (name, number))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def add_users_from_csv(filename):
    config = load_config(filename='B:/Lab_1/Lab_11/database.ini')
    names = []
    numbers = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                names.append(row['name'])
                numbers.append(row['phonenumber'])
    except Exception as e:
        print("Ошибка чтения файла:", e)
        return

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_users(%s, %s)', (names, numbers))  # Передаем массивы
                conn.commit()
                print("Номера успешно добавлены.")
    except Exception as e:
        print("Ошибка базы данных:", e)

def add_or_update_user(name, number):
    config = load_config(filename='B:/Lab_1/Lab_11/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.callproc('add_or_update_user', (name, number))
                conn.commit()
    except Exception as e:
        print("Ошибка:", e)

def add_many_users_from_input():
    names = []
    phones = []

    print("Введите данные пользователей (имя и номер через пробел).")
    print("Введите 'end' для завершения ввода.\n")

    while True:
        line = input("Пользователь: ")
        if line.lower() == 'end':
            break
        try:
            name, phone = line.split()
            names.append(name)
            phones.append(phone)
        except ValueError:
            print("Ошибка: введите данные в формате 'Имя Номер'.")

    if not names:
        print("Нет данных для добавления.")
        return

    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_users(%s, %s)", (names, phones))

                invalid = cur.fetchone()
                if invalid and invalid[0]:
                    print("\nНекорректные номера (имя => номер):")
                    for entry in invalid[0]:
                        print(" -", entry)
                else:
                    print("\nВсе номера успешно добавлены.")
    except Exception as e:
        print("Ошибка базы данных:", e)