from DB_config_file import get_config
import psycopg2


def view_recent_data():
  config = get_config()
  query = """
            SELECT
            users.id,
            users.name,
            users.email,
            departments.name
            FROM
            users
            JOIN
            user_departments
            ON users.id = user_departments.user_id
            JOIN
            departments ON user_departments.department_name = departments.name;
          """

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