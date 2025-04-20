import psycopg2
from config import load_config

def delete_number(name=None, number=None):
    config = load_config(filename='B:/Lab_1/Lab_11/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_user(%s, %s)", (name, number))
                conn.commit()
    except Exception as e:
        print("Ошибка:", e)
