import psycopg2
from DB_config_file import get_config

def create_table():
  '''
  create table in database
  '''
  queries = (
    """
      CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        date_joined VARCHAR(255) NOT NULL
      )
    """,
  )
  try :
    config = get_config()
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        #after the connection is established, execute the CREATE TABLE query but first drop the table if it already exists
        cursor.execute('DROP TABLE IF EXISTS users')
        for query in queries:
          cursor.execute(query)
  except Exception as error:
    print(error)


if __name__ == '__main__':
  create_table()