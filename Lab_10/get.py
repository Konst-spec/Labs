import psycopg2
from config import load_config

def get_numbers(name=None, phone=None):
    """ Retrieve data from the PhoneBook table """
    config  = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM PhoneBook"
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


