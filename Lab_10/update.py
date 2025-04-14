import psycopg2
from config import load_config

def update_number(table, name, number):
    updated_row_count = 0
    sql = " UPDATE " + table + " SET phonenumber = %s WHERE name = %s"
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (number, name))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count
    
def save_score(user_id, score, level):
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
        conn.commit()