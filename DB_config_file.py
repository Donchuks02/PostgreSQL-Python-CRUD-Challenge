from configparser import ConfigParser


#  define a function that reads database.ini file and returns if the database credentials are available
def get_config(filename='database.ini', section='postgresql'):
  parser = ConfigParser()
  parser.read('database.ini')

  config = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      config[param[0]] = param[1] # config {'host': '127.0.0.1', 'port': '5432', dbname: 'testdb'}
  else:
    raise Exception(f'Section {section} not found in the {filename} file')


  return config

if __name__ == '__main__':
  configuration = get_config()
  print(configuration)
