import psycopg2
import csv
from config import load_config

def insert_number(table, name, number):
    sql = "INSERT INTO " + table + " VALUES(%s, %s);"
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name, number))
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def upload_from_csv(filename):
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')  
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)  # читает строки как словари
                    for row in reader:
                        name = row['name']
                        phone = row['phonenumber']
                        cur.execute("INSERT INTO PhoneBook (name, phonenumber) VALUES (%s, %s)", (name, phone))
                conn.commit()
                print("CSV успешно загружен в базу данных.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)