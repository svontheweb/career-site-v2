import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
ssl_args = {'ssl': {
            'ssl_ca': "/etc/ssl/cert.pem"}
          }
engine = create_engine(db_connection_string,
                      connect_args=ssl_args)

# Connect to the database using 'with' statement
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_all = result.all()
  column_names = result.keys() 
  first_result = result_all[0]
  first_result_dict = dict(zip(column_names, first_result))
  print(first_result_dict)

  # OR,
# CREATE "LIST" OF all rows of database table with id
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  column_names = result.keys()
    
  result_dicts = []
    
  for row in result.all():
    result_dicts.append(dict(zip(column_names, row)))
  print(result_dicts)