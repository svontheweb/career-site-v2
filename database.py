import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
ssl_args = {'ssl': {
            'ssl_ca': "/etc/ssl/cert.pem"}
          }
engine = create_engine(db_connection_string,
                      connect_args=ssl_args)

def load_jobs_from_db():
  # CREATE "LIST" OF all rows of database table with id
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
      
    result_dicts = []
      
    for row in result.all():
      result_dicts.append(dict(zip(column_names, row)))
    return (result_dicts)

def load_job_from_db(id):
  # CREATE "LIST" OF row with id
  with engine.connect() as conn:
    query = "SELECT * FROM jobs WHERE ID={}".format(id)
    result = conn.execute(text(query))
    column_names = result.keys()
      
    result_dicts = []
    rows = result.all()

    if len(rows) == 0:
      return None
    for row in rows:
      result_dicts.append(dict(zip(column_names, row)))
    return (result_dicts)