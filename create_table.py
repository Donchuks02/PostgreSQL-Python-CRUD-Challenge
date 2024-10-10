import psycopg2
from DB_config_file import get_config

def create_table():
    '''create table in database'''
    queries = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            date_joined VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE departments (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE user_departments (
            user_id INT REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE,
            department_name VARCHAR(255) REFERENCES departments(name) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY (user_id, department_name)
        )
        """,
    )

    try:
        config = get_config()
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                # After the connection is established, execute the CREATE TABLE query but first drop the table if it already exists
                cursor.execute('DROP TABLE IF EXISTS user_departments CASCADE')
                cursor.execute('DROP TABLE IF EXISTS departments CASCADE')
                cursor.execute('DROP TABLE IF EXISTS users CASCADE')
                for query in queries:
                    cursor.execute(query)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    create_table()