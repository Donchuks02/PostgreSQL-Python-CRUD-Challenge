from DB_config_file import get_config
import psycopg2

def delete_user(name):
  config = get_config()
  query = "DELETE FROM users WHERE name = %s"
  rows_deleted = 0
  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        rows_deleted = cursor.rowcount
        cursor.execute(query,(name,))
      connection.commit()
  except Exception as error:
    print(error)

if __name__ == '__main__':
  delete_user("Ada",)