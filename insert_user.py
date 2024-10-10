from DB_config_file import get_config
import psycopg2
from datetime import datetime

def insert_many_users(users_list):
  query = """INSERT INTO users (name, email, date_joined) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING;"""
  config = get_config()
  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.executemany(query, users_list)

      connection.commit()
    print("users inserted successfully")
  except Exception as error:
    print(error)


def insert_many_departments(departments_list):
  """Inserts departments into the 'departments' table"""
  query = """INSERT INTO departments (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;"""
  config = get_config()

  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.executemany(query, departments_list)

      connection.commit()
    print("departments inserted successfully")
  except Exception as error:
    print(error)


def insert_user_departments(user_department_list):
  """Inserts a user-department relationship into the 'user_departments' table"""
  query = """INSERT INTO user_departments (user_id, department_name) VALUES (%s, %s) ON CONFLICT (user_id, department_name) DO NOTHING;"""
  config = get_config()

  try:
    with psycopg2.connect(**config) as connection:
      with connection.cursor() as cursor:
        cursor.executemany(query, user_department_list)

      connection.commit()
    print("user-department relationship inserted successfully")
  except Exception as error:
    print(error)

if __name__ == "__main__":
  # inserting users
  insert_many_users([
      ('John', 'john@gmail.com', datetime.now(),),
      ('James', 'james@gmail.com', datetime.now(),),
      ('Ada', 'ada@gmail.com', datetime.now(),),
      ('Williams', 'williams@gmail.com', datetime.now(),),
      ('Cain', 'cain@gmail.com', datetime.now(),),
      ('Paul', 'paul@gmail.com', datetime.now(),),
    ])

  #inserting departments
  insert_many_departments([
      ('Engineering',),
      ('Sales',),
      ('Marketing',),
      ('Finance',),
      ('HR',),
      ('Legal',),
      ('Customer service',),
      ('IT',),
      ('Admin',),
      ('Accounting',),
      ('Public Relations',),
  ])


  #inserting user-department relationships
  insert_user_departments([
      (1, 'Engineering',),
      (1, 'Sales',),
      (1, 'Marketing',),
      (2, 'Sales',),
      (3, 'Engineering',),
      (3, 'Sales',),
      (3, 'Marketing',),
      (4, 'Engineering',),
      (4, 'Sales',),
      (5, 'Engineering',),
      (6, 'Accounting',),
  ])

