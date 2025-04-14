from config import load_config
import psycopg2

def create_tables():
    config = load_config(filename='B:/Lab_1/Lab_10/database.ini')
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
        """
    )
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
        conn.commit()

create_tables()