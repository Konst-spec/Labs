import psycopg2
from config import load_config

def get_numbers(table=None, name=None, phone=None):
    config  = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM " + table 
                conditions = []
                params = []

                #Фильтр по имени
                if name:
                    conditions.append("name ILIKE %s")
                    params.append(f"%{name}%")
            
                #Фильтр по номеру
                if phone:
                        conditions.append("phonenumber ILIKE %s")
                        params.append(f"%{phone}%")

                # Добавляем условия к SQL
                if conditions:
                    sql += " WHERE " + " AND ".join(conditions)

                cur.execute(sql, tuple(params))
                rows = cur.fetchall()
                print("Всего номеров: ", cur.rowcount, "\n")
                for row in rows:
                    print(row[0], "   ", row[1], "\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


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


def get_last_score(user_id):
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level FROM user_score
                WHERE user_id = %s ORDER BY id DESC
            """, (user_id,))
            return cur.fetchone() or (0, 1)