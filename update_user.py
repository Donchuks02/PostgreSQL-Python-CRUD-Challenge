from DB_config_file import get_config
import psycopg2

def update_user(id, name):
  config = get_config()
  query = "UPDATE users SET name = %s WHERE id = %s "
  updated_row_count = 0

  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.execute(query, (name, id))
        updated_row_count = cursor.rowcount
      connection.commit()
  except Exception as error:
    print(error)
  finally:
    updated_row_count


if __name__ == '__main__':
  update_user(1, "John Doe")