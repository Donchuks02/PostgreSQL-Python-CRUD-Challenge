import psycopg2
from DB_config_file import get_config

def connect_to_db():
  '''
  Connect to the database
  '''
  try:
    config = get_config()
    with psycopg2.connect(**config) as connection:
      print("Yes, Connected to the database server")
      return connection
  except Exception as error:
    print(error)


if __name__ == '__main__':
  connect_to_db()
