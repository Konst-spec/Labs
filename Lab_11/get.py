import psycopg2
from config import load_config

def get_numbers(table, name=None, number=None):
    config = load_config(filename='B:/Lab_1/Lab_11/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if name:
                    cur.execute("SELECT * FROM search_phonebook(%s)", (name,))
                elif number:
                    cur.execute("SELECT * FROM search_phonebook(%s)", (number,))
                else:
                    cur.execute("SELECT * FROM get_users(100, 0)")  #Показывает первые 100
                rows = cur.fetchall()
                for row in rows:
                    print(f"{row[0]}: {row[1]}")
    except Exception as e:
        print("Ошибка:", e)

def get_or_create_user(username):
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                return cur.fetchone()[0]


def get_users_from_db(limit, offset):
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM get_users(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(f"Name: {row[0]}, Phone: {row[1]}")
    except Exception as e:
        print("Ошибка:", e)