import psycopg2
from config import load_config

def delete_number(name):
    """ Delete data from the PhoneBook table """
    config  = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

