from DB_config_file import get_config
import psycopg2
from datetime import datetime

def insert_many_records(users_list):
  query = "INSERT INTO users (name, email, date_joined) VALUES (%s, %s, %s)"
  config = get_config()
  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.executemany(query, users_list)

      connection.commit()

  except Exception as error:
    print


if __name__ == "__main__":
  insert_many_records([
      ('John', 'john@gmail.com', datetime.now(),),
      ('James', 'james@gmail.com', datetime.now(),),
      ('Ada', 'ada@gmail.com', datetime.now(),),
      ('Williams', 'williams@gmail.com', datetime.now(),),
      ('Cain', 'cain@gmail.com', datetime.now(),),
      ('Paul', 'paul@gmail.com', datetime.now(),),
    ])
