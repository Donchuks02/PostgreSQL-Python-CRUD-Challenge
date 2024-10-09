from DB_config_file import get_config
import psycopg2


def view_recent_data():
  config = get_config()
  query = "SELECT * FROM users ORDER BY id;"

  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        return data
  except Exception as error:
    print(error)

if __name__ == "__main__":
  data = view_recent_data()
  if data:
    for row in data:
      print(row)
  else:
    print("No data found")